#!/usr/bin/env python3
"""ACE engine — Phase-1 deterministic loops (stdlib only, per NFR-1).

Subcommands:
  validate  X-ID     validate outbox/X-ID/EXIT_PACKAGE.json -> pending/ (or actionable errors)
  accept    X-ID     apply pending package -> state/ + hub note + resume packet (+audit, +attributed commit)
  reject    X-ID     archive pending package with audit record
  views              regenerate hub views (Today, Pending Panel Updates, Weekly Review)
  rollback  EVENT_ID reverse an accepted transition as a NEW audited transition

Spec: ACE/spec/04 (machines), 11 (writer matrix, flows, content-class gate).
Models propose; only this validated loop records (CLAUDE.md state-change policy).
"""
import json, os, re, sys, time, hashlib, subprocess, tempfile
from datetime import datetime, timezone

# Store locations: defaults are the reference deployment; another machine sets ACE_STORE / ACE_LOCAL / ACE_HUB
# (see deploy/README.md). The repo is wherever this file lives.
ACE = os.environ.get("ACE_REPO") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STORE = os.environ.get("ACE_STORE", r"F:\git\ACE_storage")
LOCAL = os.environ.get("ACE_LOCAL", r"F:\ACE_local")
HUB = os.environ.get("ACE_HUB", r"F:\ACE_hub")
SCHEMA = json.load(open(os.path.join(ACE, "schemas", "panel_exit_package.schema.json"), encoding="utf-8"))
LOOP_AUTHOR = ["-c", "user.name=ACE Loop", "-c", "user.email=loop@ace.local"]

def now(): return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")
def sha256(b): return hashlib.sha256(b).hexdigest()

def atomic_write(path, text):
    """META-2 discipline: tmp + os.replace, never partial writes."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path), prefix=".ace_tmp_")
    with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    for attempt in range(6):  # Windows: AV/indexer can briefly lock a just-written target (observed 2026-10-02)
        try:
            os.replace(tmp, path); return
        except PermissionError:
            if attempt == 5: raise
            time.sleep(0.1 * (attempt + 1))

def audit(event):
    event.setdefault("ts", now())
    event.setdefault("event_id", f"E{int(datetime.now().timestamp()*1000)}-{os.urandom(2).hex()}")
    p = os.path.join(STORE, "audit", "events.jsonl")
    os.makedirs(os.path.dirname(p), exist_ok=True)
    lead = ""
    if os.path.exists(p) and os.path.getsize(p):  # a torn tail (crash mid-append) must not swallow this record
        with open(p, "rb") as f:
            f.seek(-1, 2); lead = "" if f.read(1) == b"\n" else "\n"
    with open(p, "a", encoding="utf-8", newline="\n") as f:
        f.write(lead + json.dumps(event, ensure_ascii=False) + "\n")
    return event["event_id"]

def commit(repo, msg):
    subprocess.run(["git", "-C", repo] + LOOP_AUTHOR + ["add", "-A"], check=True, capture_output=True)
    r = subprocess.run(["git", "-C", repo] + LOOP_AUTHOR + ["commit", "-q", "-m", msg], capture_output=True, text=True)
    if r.returncode == 0 and repo == STORE:
        subprocess.run(["git", "-C", repo, "push", "-q"], capture_output=True)  # META-1 durability gate

def check_schema(pkg):
    errs = []
    for k in SCHEMA["required"]:
        if k not in pkg: errs.append(f"missing required field: {k}")
    for k in pkg:
        if k not in SCHEMA["properties"]: errs.append(f"unknown field: {k}")
    if "panel_type" in pkg and pkg["panel_type"] not in SCHEMA["properties"]["panel_type"]["enum"]:
        errs.append(f"panel_type must be one of {SCHEMA['properties']['panel_type']['enum']}")
    if "confidence" in pkg and not (isinstance(pkg["confidence"], (int, float)) and 0 <= pkg["confidence"] <= 1):
        errs.append("confidence must be a number in [0,1]")
    for k in ("sources_seen", "sources_not_seen", "evidence_created", "unresolved"):
        if k in pkg and not (isinstance(pkg[k], list) and all(isinstance(i, str) for i in pkg[k])):
            errs.append(f"{k} must be a list of strings")
    for k in ("proposed_state_changes", "commitments_detected"):
        if k in pkg and not (isinstance(pkg[k], list) and all(isinstance(i, dict) for i in pkg[k])):
            errs.append(f"{k} must be a list of objects")
    return errs

def check_content_class(pkg):
    """Spec 11 sensitivity gate: state proposals + pointers only — no content excerpts on the control plane."""
    errs, raw = [], json.dumps(pkg, ensure_ascii=False)
    for field in ("outcome", "next_action", "resume_context", "objective"):
        v = pkg.get(field, "")
        if isinstance(v, str) and len(v) > 1500:
            errs.append(f"{field} exceeds 1500 chars — reads as content excerpt; reference by path+sha256 instead")
    if len(raw) > 20000:
        errs.append("package exceeds 20KB — control plane carries state, not content")
    if re.search(r"[A-Za-z0-9+/]{400,}={0,2}", raw):
        errs.append("embedded base64-like blob detected — artifacts belong in ACE_local, referenced by path+sha256")
    for ev in pkg.get("evidence_created", []):
        if not re.search("(" + re.escape(LOCAL.rstrip("\\/") + "\\") + r"|sha256:)", ev, re.I):
            errs.append(f"evidence entry lacks ACE_local path or sha256 pointer: {ev[:80]}")
    return errs

def check_scope(pkg, packet_text):
    """Source-scope check: sources_seen must be within the session packet's visible roots (prefix match)."""
    errs = []
    roots = [l.strip("- `").rstrip("`").split(" ")[0].strip("`")
             for l in packet_text.splitlines() if l.strip().startswith("- `")]
    roots = [r for r in roots if ":" in r]
    if not pkg.get("sources_not_seen"):
        errs.append("sources_not_seen is empty — partial-observability rule requires declaring unseen sources (or ['none'])")
    for s in pkg.get("sources_seen", []):
        if roots and not any(s.lower().startswith(r.lower().rstrip("\\")) for r in roots):
            errs.append(f"source outside declared visible roots: {s}")
    return errs

def unique_dir(path):
    """Never overwrite an existing archive folder (no-delete rule): suffix a timestamp instead."""
    return path if not os.path.exists(path) else f"{path}_{datetime.now().strftime('%Y%m%dT%H%M%S%f')}"

def read_events():
    p = os.path.join(STORE, "audit", "events.jsonl")
    if not os.path.exists(p): return []
    evs, bad = [], 0
    for line in open(p, encoding="utf-8").read().splitlines():
        if not line.strip(): continue
        try: evs.append(json.loads(line))
        except json.JSONDecodeError: bad += 1
    if bad: print(f"WARNING: {bad} undecodable audit line(s) skipped (torn write?) — inspect audit/events.jsonl")
    return evs

def lifecycle(xid, evs):
    """Events for xid since its latest validation (hub_pending) — the current review cycle."""
    last = max((i for i, e in enumerate(evs) if e.get("id") == xid and e.get("to") == "hub_pending"), default=-1)
    return [e for e in evs[last + 1:] if e.get("id") == xid]

def in_flight(evs):
    """X-ids whose accept is logged but whose pending folder still exists (a crash mid-accept)."""
    pend = os.path.join(STORE, "pending")
    return [x for x in (sorted(os.listdir(pend)) if os.path.isdir(pend) else [])
            if any(e.get("to") == "accepted" for e in lifecycle(x, evs))]

def check_replay(xid):
    """Replay gate (external-review F1): an X-id already pending or processed is never re-applied."""
    for where in (("pending", xid), ("archive", "applied", xid), ("archive", "rejected", xid)):
        if os.path.exists(os.path.join(STORE, *where)):
            return [f"replay: {xid} already exists at {'/'.join(where)} — a new submission needs a new X-id"]
    if any(e.get("id") == xid and e.get("to") in ("accepted", "rejected") for e in read_events()):
        return [f"replay: {xid} was already accepted or rejected (audit log) — a new submission needs a new X-id"]
    return []

def validate(xid):
    xdir = os.path.join(STORE, "outbox", xid)
    pkg_path = os.path.join(xdir, "EXIT_PACKAGE.json")
    if not os.path.exists(pkg_path):
        print(f"REJECT: {pkg_path} not found"); return 1
    pkg = json.loads(open(pkg_path, encoding="utf-8").read())
    packet_path = os.path.join(STORE, "packets", f"P-{xid.split('-',1)[1]}_planning.md")
    packet_text = open(packet_path, encoding="utf-8").read() if os.path.exists(packet_path) else ""
    errs = check_replay(xid) + check_schema(pkg) + check_content_class(pkg) + check_scope(pkg, packet_text)
    # FMEA-001 sync gate: session_id in package must match the outbox id
    if pkg.get("session_id") and pkg["session_id"].replace("P-", "X-") != xid and pkg["session_id"] != xid:
        errs.append(f"FMEA-001 sync gate: session_id '{pkg.get('session_id')}' does not correspond to outbox id '{xid}'")
    if errs:
        atomic_write(os.path.join(xdir, "VALIDATION_ERRORS.md"),
                     "# Validation failed — actionable errors\n\n" + "\n".join(f"- {e}" for e in errs) + "\n")
        audit({"type": "panel_transition", "machine": "panel_lifecycle", "id": xid,
               "from": "exit_package_drafted", "to": "validation_failed", "errors": errs})
        print(f"VALIDATION FAILED ({len(errs)}):\n" + "\n".join(f"  - {e}" for e in errs)); return 1
    dest = os.path.join(STORE, "pending", xid)
    os.makedirs(dest, exist_ok=True)
    for f in os.listdir(xdir):
        os.replace(os.path.join(xdir, f), os.path.join(dest, f))
    os.rmdir(xdir)  # empty shell only — files were moved, not deleted
    audit({"type": "panel_transition", "machine": "panel_lifecycle", "id": xid,
           "from": "exit_package_drafted", "to": "hub_pending", "pkg_sha256": sha256(json.dumps(pkg).encode())})
    gen_views()
    commit(STORE, f"transition(panel_lifecycle): exit_package_drafted -> hub_pending {xid}")
    print(f"VALIDATED -> pending/{xid}; hub Pending view updated. Review target <3 min."); return 0

def load_state():
    p = os.path.join(STORE, "state", "projects.json")
    return json.loads(open(p, encoding="utf-8").read()) if os.path.exists(p) else {"projects": {}, "commitments": {}}

def save_state(st):
    atomic_write(os.path.join(STORE, "state", "projects.json"), json.dumps(st, indent=1, ensure_ascii=False))

def state_sha(st): return sha256(json.dumps(st, sort_keys=True).encode())

def apply_package(st, pkg, xid, ts):
    """Pure and deterministic for a given (state, package, ts) — so a recovery re-run reproduces it exactly."""
    st = json.loads(json.dumps(st))
    for ch in pkg.get("proposed_state_changes", []):
        pid = ch.get("project_id", "unfiled")
        pr = st["projects"].setdefault(pid, {"state": "proposed", "sync": "completeness_unknown"})
        pr.update({k: v for k, v in ch.items() if k != "project_id"})
        pr["sync"] = "current"; pr["last_accepted"] = ts; pr["source_package"] = xid
    for cm in pkg.get("commitments_detected", []):
        cid = cm.get("id") or f"C{len(st['commitments'])+1:04d}"
        st["commitments"][cid] = {**cm, "state": cm.get("state", "clarified"), "captured_via": xid}
    return st

def accept(xid):
    """Write-ahead accept (external-review F4): the accepted event — carrying prev_state and the expected
    post-state hash — is logged BEFORE state changes. A re-run after a crash compares the current state with
    both hashes: post = finish only; prev = apply now; anything else = refuse (never overwrite later work)."""
    pdir = os.path.join(STORE, "pending", xid)
    pkg_path = os.path.join(pdir, "EXIT_PACKAGE.json")
    evs = read_events()
    others = [x for x in in_flight(evs) if x != xid]
    if others:
        print(f"REFUSED: accept of {', '.join(others)} is unfinished — re-run accept on it first"); return 1
    logged = [e for e in lifecycle(xid, evs) if e.get("to") == "accepted"]
    if not os.path.exists(pkg_path):
        if logged and os.path.isdir(pdir):  # the package moves last: only the final moves remain
            return finish_accept(xid, None, logged[0])
        print(f"REFUSED: {pkg_path} not found"); return 1
    pkg = json.loads(open(pkg_path, encoding="utf-8").read())
    # Sensitivity gate again at accept: the operator may annotate pending/, but nothing reaches state/hub unchecked (spec 11)
    errs = check_schema(pkg) + check_content_class(pkg)
    if errs:
        print(f"REFUSED: {xid} no longer passes validation — fix the package or reject it:\n" + "\n".join(f"  - {e}" for e in errs)); return 1
    st = load_state(); cur = state_sha(st)
    if logged:
        ev = logged[0]
        if cur == ev.get("post_state_sha256"):
            pass
        elif cur == ev.get("prev_state_sha256"):
            save_state(apply_package(st, pkg, xid, ev["ts"]))
        else:
            print(f"REFUSED: state changed since {xid}'s logged accept {ev['event_id']} — reconcile by hand "
                  f"(the event holds prev_state)"); return 1
    else:
        ts = now(); new = apply_package(st, pkg, xid, ts)
        ev = {"type": "panel_transition", "machine": "panel_lifecycle", "id": xid, "from": "hub_pending",
              "to": "accepted", "ts": ts, "prev_state_sha256": cur, "post_state_sha256": state_sha(new),
              "prev_state": st, "archive_dir": os.path.relpath(unique_dir(os.path.join(STORE, "archive", "applied", xid)), STORE)}
        audit(ev)
        save_state(new)
    return finish_accept(xid, pkg, ev)

def finish_accept(xid, pkg, ev):
    pdir = os.path.join(STORE, "pending", xid)
    if pkg is not None:
        note = [f"# {pkg.get('hub_destination', 'project')}", "",
                f"- state updated from panel `{xid}` ({ev['ts']}) — sync: `current`",
                f"- outcome: {pkg['outcome']}", f"- next action: {pkg['next_action']}",
                f"- evidence: " + ("; ".join(pkg.get("evidence_created", [])) or "none"),
                f"- unresolved: " + ("; ".join(pkg.get("unresolved", [])) or "none")]
        atomic_write(os.path.join(HUB, "projects", f"{pkg.get('hub_destination','unfiled').replace('/', '_')}.md"), "\n".join(note) + "\n")
        resume = [f"# Resume packet — {pkg['session_id']}", f"Generated {ev['ts']} on accept of {xid}.", "",
                  f"## Completed state\n{pkg['outcome']}", f"## Exact next action\n{pkg['next_action']}",
                  f"## Files\n" + "\n".join(f"- {e}" for e in pkg.get("evidence_created", [])),
                  f"## Unresolved\n" + "\n".join(f"- {u}" for u in pkg.get("unresolved", [])),
                  f"## Resume context\n{pkg.get('resume_context','')}"]
        atomic_write(os.path.join(STORE, "packets", f"RESUME_{xid}.md"), "\n\n".join(resume) + "\n")
    dest = os.path.join(STORE, ev.get("archive_dir") or os.path.join("archive", "applied", xid))
    os.makedirs(dest, exist_ok=True)
    for f in sorted(os.listdir(pdir), key=lambda n: n == "EXIT_PACKAGE.json"):  # the package moves last
        os.replace(os.path.join(pdir, f), os.path.join(dest, f))
    os.rmdir(pdir)  # empty shell only
    gen_views()
    commit(STORE, f"transition(panel_lifecycle): hub_pending -> accepted -> durable_state_updated {xid}")
    commit(HUB, f"transition(hub_sync): panel_update_awaiting_review -> current {xid}")
    print(f"ACCEPTED {xid}: state updated, hub note written, resume packet packets/RESUME_{xid}.md, audit {ev['event_id']}."); return 0

def reject(xid):
    pdir = os.path.join(STORE, "pending", xid)
    if not os.path.isdir(pdir):
        print(f"REFUSED: pending/{xid} not found"); return 1
    if any(e.get("to") == "accepted" for e in lifecycle(xid, read_events())):
        print(f"REFUSED: {xid} has a logged accept — re-run accept to finish it, then roll back if needed"); return 1
    dest = unique_dir(os.path.join(STORE, "archive", "rejected", xid)); os.makedirs(dest, exist_ok=True)
    for f in os.listdir(pdir): os.replace(os.path.join(pdir, f), os.path.join(dest, f))
    os.rmdir(pdir)  # empty shell only
    audit({"type": "panel_transition", "machine": "panel_lifecycle", "id": xid, "from": "hub_pending", "to": "rejected"})
    gen_views(); commit(STORE, f"transition(panel_lifecycle): hub_pending -> rejected {xid}")
    print(f"REJECTED {xid} -> archive/rejected/ (audit record written)."); return 0

def rollback(event_id):
    evs = read_events()
    if in_flight(evs):
        print(f"REFUSED: unfinished accept ({', '.join(in_flight(evs))}) — finish it first"); return 1
    idx = next((i for i, e in enumerate(evs) if e.get("event_id") == event_id), None)
    ev = evs[idx] if idx is not None else None
    if not ev or "prev_state" not in ev: print("event not found or not reversible"); return 1
    undone = {e.get("of_event") for e in evs if e.get("type") == "rollback"}
    if event_id in undone: print(f"REFUSED: {event_id} was already rolled back"); return 1
    # Restoring a snapshot under a later, still-standing accept would silently discard it: newest-first only.
    later = [e["event_id"] for e in evs[idx + 1:] if e.get("to") == "accepted" and e["event_id"] not in undone]
    if later:
        print(f"REFUSED: later accepted transitions stand ({', '.join(later)}) — roll back newest-first"); return 1
    save_state(ev["prev_state"])
    audit({"type": "rollback", "of_event": event_id, "machine": "panel_lifecycle"})
    gen_views(); commit(STORE, f"rollback: reverse {event_id} as new audited transition")
    print(f"ROLLED BACK to pre-{event_id} state (as a new transition — history preserved)."); return 0

def title_of(v):
    return v.get("title") or v.get("commitment") or v.get("next_action") or ""

def gen_views():
    st = load_state()
    pend = sorted(os.listdir(os.path.join(STORE, "pending"))) if os.path.isdir(os.path.join(STORE, "pending")) else []
    pend = [p for p in pend if p.startswith("X-")]
    pv = ["# Pending Panel Updates", f"*Generated {now()} — hand edits are lost.*", ""]
    pv += [f"- [ ] `{x}` — review package at `ACE_storage/pending/{x}/EXIT_PACKAGE.json`" for x in pend] or ["Nothing pending. All current."]
    atomic_write(os.path.join(HUB, "views", "Pending Panel Updates.md"), "\n".join(pv) + "\n")
    today = ["# Today", f"*Generated {now()} — narrow view: ≤3 obligations + due returns + 1 protected block + 1 evidence unit.*", ""]
    actionable = [(k, v) for k, v in st["commitments"].items() if v.get("state") in ("actionable", "in_progress")][:3]
    today += [f"- [ ] **{k}** {title_of(v)} → {v.get('next_action', '?')}" for k, v in actionable] or ["No actionable commitments recorded yet — run the planning panel (P-0001)."]
    if pend: today.append(f"\n> ⚠ {len(pend)} panel update(s) awaiting review — hub must not be trusted as current until reviewed.")
    atomic_write(os.path.join(HUB, "views", "Today.md"), "\n".join(today) + "\n")
    cm = st["commitments"].items()
    cr = ["# Commitments and Return", f"*Generated {now()} — one source: commitment records. Gestures: tick=done, ~~strike~~=defer, @date=hold, @person=agenda.*", ""]
    cr.append("## Next Actions")
    by_cat = {}
    for k, v in cm:
        if v.get("state") in ("actionable", "in_progress") and not v.get("person"):
            by_cat.setdefault(v.get("category", "desk"), []).append((k, v))
    for cat in sorted(by_cat):
        cr.append(f"### @{cat}")
        cr += [f"- [ ] **{k}** {title_of(v)} ({v.get('project_id','general')})" for k, v in by_cat[cat]]
    if not by_cat: cr.append("none yet")
    cr.append("\n## Agenda / Waiting For (cumulative, by person)")
    by_p = {}
    for k, v in cm:
        if v.get("person") and v.get("state") not in ("closed", "canceled"):
            by_p.setdefault(v["person"], []).append((k, v))
    for pn in sorted(by_p):
        cr.append(f"### @{pn}")
        cr += [f"- [ ] **{k}** {title_of(v)}" + (f" (since {v['captured'][:10]})" if v.get('captured') else "") for k, v in by_p[pn]]
    if not by_p: cr.append("none yet")
    cr.append("\n## Scheduled Returns")
    rets = [(k, v) for k, v in cm if v.get("no_action_before") or v.get("return_date")]
    cr += [f"- **{k}** {title_of(v)} @{v.get('no_action_before') or v.get('return_date')}" for k, v in sorted(rets, key=lambda x: x[1].get('no_action_before') or x[1].get('return_date') or '')] or ["none yet"]
    atomic_write(os.path.join(HUB, "views", "Commitments and Return.md"), "\n".join(cr) + "\n")
    wk = ["# Weekly Review", f"*Generated {now()} — dual scoreboards (P0-A reliability / P0-B conversion). Target <20 min.*", "",
          f"- projects tracked: {len(st['projects'])} | commitments: {len(st['commitments'])} | pending reviews: {len(pend)}",
          "- reliability exceptions: (loop arrives Phase 2)", "- evidence shipped this week: see evidence records",
          "- one simplification decision: ____"]
    atomic_write(os.path.join(HUB, "views", "Weekly Review.md"), "\n".join(wk) + "\n")

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "views"
    sys.exit({"validate": lambda: validate(sys.argv[2]), "accept": lambda: accept(sys.argv[2]),
              "reject": lambda: reject(sys.argv[2]), "rollback": lambda: rollback(sys.argv[2]),
              "views": lambda: (gen_views(), print("views regenerated"))[1] or 0}[cmd]())
