#!/usr/bin/env python3
"""ACE clarify loop (minimal deterministic v1) — inbox notes -> proposed commitments.

Reads capture notes from $ACE_HUB/inbox/ and $ACE_LOCAL/inbox/ (*.md, not _-prefixed),
parses ONLY the deterministic gesture marks (spec/13):
  @YYYY-MM-DD    return date (>> legacy)          @name        person (agenda/waiting-for)
  @call/@read/@desk  category         hedge words  ("maybe", "thinking loud", trailing "..") -> idea queue
Packages all proposals as one exit package in outbox/, runs the standard validator so they land
in pending/ and surface in the hub Pending view. The operator's tick accepts them into state (batch class).
Processed notes move to inbox/clarified/ (supersede-by-move; never deleted).
Agentic enrichment (project matching, smarter next actions) is the Phase-2 upgrade; this v1 never guesses.
"""
import os, re, sys, json, importlib.util
from datetime import date

spec = importlib.util.spec_from_file_location("ace_engine", os.path.join(os.path.dirname(__file__), "ace_engine.py"))
eng = importlib.util.module_from_spec(spec); spec.loader.exec_module(eng)
HUB, LOCAL, STORE = eng.HUB, eng.LOCAL, eng.STORE  # one source of truth (env-overridable in ace_engine)
HEDGES = re.compile(r"\b(maybe|not sure|thinking (out )?loud|i think|probably)\b|\.\.\s*$", re.I)
CATS = {"call", "read", "desk", "msg"}

def parse_note(path):
    text = open(path, encoding="utf-8").read().strip()
    if not text: return None
    first = text.splitlines()[0].strip("# ").strip()
    rec = {"commitment": first[:160], "source_note": os.path.basename(path), "state": "clarified"}
    md = re.search(r"(?:@|>>)\s*(\d{4}-\d{2}-\d{2})", text)
    if md: rec["return_date"] = md.group(1); rec["state"] = "scheduled_return"
    for tag in re.findall(r"@([A-Za-z][A-Za-z0-9_-]*)", text):
        if tag.lower() in CATS: rec["category"] = tag.lower()
        else: rec["person"] = tag
    if HEDGES.search(text): rec["state"] = "idea_queue"; rec["hedged"] = True
    return rec

def run():
    notes = []
    for root in (os.path.join(HUB, "inbox"), os.path.join(LOCAL, "inbox")):
        if not os.path.isdir(root): continue
        for f in sorted(os.listdir(root)):
            p = os.path.join(root, f)
            if os.path.isfile(p) and f.endswith(".md") and not f.startswith("_"):
                notes.append(p)
    props = [r for r in (parse_note(p) for p in notes) if r]
    if not props:
        print("inbox empty — nothing to clarify"); return 0
    stamp = date.today().strftime("%Y%m%d")
    xid = f"X-CLARIFY{stamp}"
    n = 1
    # an X-id is never reused — the engine's replay gate (filesystem + audit log) is the single source of truth
    while eng.check_replay(xid) or os.path.isdir(os.path.join(eng.STORE, "outbox", xid)):
        n += 1; xid = f"X-CLARIFY{stamp}{chr(96+n)}"
    pkg = {"session_id": xid.replace("X-", "P-"), "panel_type": "review",
           "objective": "Clarify loop: inbox captures -> proposed commitment records (deterministic marks only)",
           "sources_seen": notes, "sources_not_seen": ["none"],
           "outcome": f"{len(props)} capture(s) parsed into proposals; hedged items routed to idea queue",
           "proposed_state_changes": [], "commitments_detected": props,
           "next_action": "The operator ticks proposals in the hub Pending view",
           "resume_context": "clarify v1 deterministic", "hub_destination": "commitments", "confidence": 0.7}
    os.makedirs(os.path.join(STORE, "outbox", xid), exist_ok=True)
    with open(os.path.join(STORE, "outbox", xid, "EXIT_PACKAGE.json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump(pkg, f, indent=1, ensure_ascii=False)
    rc = eng.validate(xid)
    if rc == 0:
        for p in notes:
            dest = os.path.join(os.path.dirname(p), "clarified")
            os.makedirs(dest, exist_ok=True)
            os.replace(p, os.path.join(dest, os.path.basename(p)))
        print(f"{len(props)} proposal(s) staged as {xid} — tick them in views/Pending Panel Updates.md")
    return rc

if __name__ == "__main__":
    sys.exit(run())
