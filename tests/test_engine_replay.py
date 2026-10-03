"""Replay / crash / interleaving / rollback tests for the ace_engine accept path
(external-review failure checks F1 and F4; EV3 red-team attacks 1b, 1c, 1d, 1e, 2e, 4b, 4g, 5b, 4f).
Runs entirely in temp sandboxes: STORE/HUB/LOCAL are redirected and git commits are stubbed — real
ACE_STORE and ACE_HUB stores are never touched. Sandboxes are kept, never deleted (project no-delete rule).
Run: python tests/test_engine_replay.py
Non-vacuity check: ACE_ENGINE=<path to an older ace_engine.py> python tests/test_engine_replay.py
"""
import sys, os, json, hashlib, tempfile, importlib.util

ENGINE = os.environ.get("ACE_ENGINE") or os.path.join(os.path.dirname(__file__), "..", "engine", "ace_engine.py")
_real_replace = os.replace

def load():
    spec = importlib.util.spec_from_file_location("ace_engine", ENGINE)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m

PKG = {"session_id": "P-X", "panel_type": "produce", "objective": "x",
       "sources_seen": ["F:\\git\\ACE\\spec\\09_STATE.md"], "sources_not_seen": ["none"],
       "outcome": "ok", "proposed_state_changes": [{"project_id": "p", "state": "active"}],
       "commitments_detected": [{"commitment": "follow up"}, {"id": "C-FIX", "commitment": "named"}],
       "next_action": "n", "hub_destination": "projects/p", "confidence": 0.9,
       "evidence_created": ["F:\\ACE_local\\artifacts\\a\\f.md sha256:abc"]}
EMPTY = {"projects": {}, "commitments": {}}

def sandbox():
    eng = load()
    root = tempfile.mkdtemp(prefix="ace_sbx_")
    eng.STORE, eng.HUB, eng.LOCAL = (os.path.join(root, d) for d in ("store", "hub", "local"))
    eng.commit = lambda repo, msg: None
    return eng

def drop(eng, xid, pkg=PKG, extra=None):
    d = os.path.join(eng.STORE, "outbox", xid); os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "EXIT_PACKAGE.json"), "w", encoding="utf-8") as f:
        json.dump({**pkg, "session_id": "P-" + xid.split("-", 1)[1]}, f)
    for name, text in (extra or {}).items():
        with open(os.path.join(d, name), "w", encoding="utf-8") as f: f.write(text)

def events(eng):
    out = []
    for l in open(os.path.join(eng.STORE, "audit", "events.jsonl"), encoding="utf-8").read().splitlines():
        try: out.append(json.loads(l))
        except json.JSONDecodeError: out.append(None)
    return out

def accepted(eng, xid): return [e for e in events(eng) if e and e.get("id") == xid and e.get("to") == "accepted"]
def ncm(eng): return len(eng.load_state()["commitments"])
def call(f, *a):
    try: return f(*a)
    except Exception as ex: return f"EXC {type(ex).__name__}"
def archive_dirs(eng, xid):
    d = os.path.join(eng.STORE, "archive", "applied")
    return sorted(n for n in os.listdir(d) if n.startswith(xid)) if os.path.isdir(d) else []

results = []
def t(name, cond): results.append(bool(cond)); print(("PASS " if cond else "FAIL ") + name)

def crash_once(eng, attr, when):
    """Make eng.<attr> raise the first time when(*args) is true, then behave normally."""
    real, fired = getattr(eng, attr), []
    def wrapped(*a, **k):
        if not fired and when(*a):
            fired.append(1); raise RuntimeError("simulated crash")
        return real(*a, **k)
    setattr(eng, attr, wrapped)
    return lambda: setattr(eng, attr, real)

# --- F1 replay -----------------------------------------------------------------------------------------
eng = sandbox(); drop(eng, "X-R1"); eng.validate("X-R1"); eng.accept("X-R1")
arch = os.path.join(eng.STORE, "archive", "applied", "X-R1", "EXIT_PACKAGE.json")
before = hashlib.sha256(open(arch, "rb").read()).hexdigest(); n1 = ncm(eng)
drop(eng, "X-R1", {**PKG, "next_action": "replayed variant"}); rc = eng.validate("X-R1")
if rc == 0: call(eng.accept, "X-R1")
t("F1 replay of an applied X-id is refused at validation", rc == 1)
t("F1 replay leaves commitments unchanged", ncm(eng) == n1)
t("F1 replay leaves the archived package byte-identical", hashlib.sha256(open(arch, "rb").read()).hexdigest() == before)

eng = sandbox(); drop(eng, "X-R2"); eng.validate("X-R2"); eng.accept("X-R2")
os.makedirs(os.path.join(eng.STORE, "archive", "superseded"), exist_ok=True)
_real_replace(os.path.join(eng.STORE, "archive", "applied", "X-R2"), os.path.join(eng.STORE, "archive", "superseded", "X-R2"))
drop(eng, "X-R2"); rc = eng.validate("X-R2")
t("F1 replay is refused even after the archive folder was superseded-by-move (audit log)", rc == 1 and ncm(eng) == 2)

# --- F4 crash points --------------------------------------------------------------------------------------
def crash_case(label, attr, when, extra=None):
    eng = sandbox(); drop(eng, "X-C", extra=extra); eng.validate("X-C")
    undo = crash_once(eng, attr, when); r1 = call(eng.accept, "X-C"); undo()
    r2 = call(eng.accept, "X-C")
    acc = accepted(eng, "X-C")
    ok = (r2 == 0 and ncm(eng) == 2 and len(acc) == 1 and acc[0].get("prev_state") == EMPTY
          and not os.path.exists(os.path.join(eng.STORE, "pending", "X-C")) and len(archive_dirs(eng, "X-C")) == 1)
    t(f"F4 crash {label}: recovery leaves 2 commitments, 1 accepted event, correct inverse, 1 archive dir", ok)
    return eng

crash_case("after the audit write, before the state write", "save_state", lambda *a: True)
crash_case("after the state write, before the hub note", "atomic_write", lambda path, text: os.sep + "projects" + os.sep in path and "hub" in path)
crash_case("after the hub note, before the resume packet", "atomic_write", lambda path, text: os.path.basename(path).startswith("RESUME_"))

eng = sandbox(); drop(eng, "X-M", extra={"HOLD_UNTIL.txt": "2026-10-09\n"}); eng.validate("X-M")
moves = []
def flaky_replace(src, dst):
    if os.sep + "archive" + os.sep in dst and "X-M" in dst:
        moves.append(dst)
        if len(moves) == 1: raise RuntimeError("simulated crash mid-move")
    return _real_replace(src, dst)
os.replace = flaky_replace
r1 = call(eng.accept, "X-M")
os.replace = _real_replace
r2 = call(eng.accept, "X-M")
t("F4 crash during the archive moves: re-run finishes without double-apply",
  r2 == 0 and ncm(eng) == 2 and len(accepted(eng, "X-M")) == 1 and not os.path.exists(os.path.join(eng.STORE, "pending", "X-M")))
t("F4 crash during the archive moves: one archive dir holds both files",
  archive_dirs(eng, "X-M") == ["X-M"] and sorted(os.listdir(os.path.join(eng.STORE, "archive", "applied", "X-M"))) == ["EXIT_PACKAGE.json", "HOLD_UNTIL.txt"])

# --- interleaving (EV3 1e / 4g / 1d) -----------------------------------------------------------------------
eng = sandbox(); drop(eng, "X-Z", {**PKG, "commitments_detected": []}); eng.validate("X-Z"); eng.accept("X-Z")
z = accepted(eng, "X-Z")[0]["event_id"]
drop(eng, "X-A"); drop(eng, "X-B", {**PKG, "commitments_detected": [{"commitment": "b work"}]})
eng.validate("X-A"); eng.validate("X-B")
undo = crash_once(eng, "atomic_write", lambda path, text: os.path.basename(path).startswith("RESUME_")); call(eng.accept, "X-A"); undo()
st_mid = eng.load_state()
t("in-flight A: a second accept (B) is refused", call(eng.accept, "X-B") == 1 and eng.load_state() == st_mid)
t("in-flight A: reject of A is refused (no unaudited state left behind)", call(eng.reject, "X-A") == 1)
t("in-flight A: rollback of an earlier, completed accept is refused", call(eng.rollback, z) == 1 and eng.load_state() == st_mid)
t("after finishing A, B accepts and nothing is lost", call(eng.accept, "X-A") == 0 and call(eng.accept, "X-B") == 0 and ncm(eng) == 3)

eng = sandbox(); drop(eng, "X-S"); eng.validate("X-S")
undo = crash_once(eng, "save_state", lambda *a: True); call(eng.accept, "X-S"); undo()
eng.save_state({"projects": {}, "commitments": {"C-OTHER": {"commitment": "written by someone else"}}})
t("recovery refuses when state changed since the logged accept (no lost update)",
  call(eng.accept, "X-S") == 1 and list(eng.load_state()["commitments"]) == ["C-OTHER"])

# --- sensitivity gate at accept (EV3 epoch-2 3b) ------------------------------------------------------------
eng = sandbox(); drop(eng, "X-E"); eng.validate("X-E")
pp = os.path.join(eng.STORE, "pending", "X-E", "EXIT_PACKAGE.json")
edited = {**json.load(open(pp, encoding="utf-8")), "next_action": "x" * 1600}
with open(pp, "w", encoding="utf-8") as f: json.dump(edited, f)
t("a pending package edited into a content excerpt is refused at accept, state untouched",
  call(eng.accept, "X-E") == 1 and eng.load_state() == EMPTY)

# --- rollback chain (EV3 4a / 4b)---------------------------------------------------------------------------
eng = sandbox(); drop(eng, "X-1"); drop(eng, "X-2", {**PKG, "commitments_detected": [{"commitment": "second"}]})
eng.validate("X-1"); eng.accept("X-1"); eng.validate("X-2"); eng.accept("X-2")
a = accepted(eng, "X-1")[0]["event_id"]; b = accepted(eng, "X-2")[0]["event_id"]
t("rollback: older event refused while a later accept stands", call(eng.rollback, a) == 1 and ncm(eng) == 3)
t("rollback: newest-first chain works (B then A) back to the initial state",
  call(eng.rollback, b) == 0 and call(eng.rollback, a) == 0 and eng.load_state() == EMPTY)
t("rollback: the same event cannot be rolled back twice", call(eng.rollback, b) == 1)

# --- audit log robustness (EV3 5b / 4f) ---------------------------------------------------------------------
eng = sandbox(); drop(eng, "X-T"); eng.validate("X-T")
with open(os.path.join(eng.STORE, "audit", "events.jsonl"), "a", encoding="utf-8") as f: f.write('{"type": "panel_tra')
r = call(eng.accept, "X-T")
evs = events(eng)
t("torn audit tail: accept still works and the next record stays parseable", r == 0 and evs[-1] is not None and evs[-1].get("to") == "accepted")
eng = sandbox()
ids = [eng.audit({"type": "probe"}) for _ in range(200)]
t("audit event ids are unique under tight loops", len(set(ids)) == 200)

print(f"\n{sum(results)}/{len(results)} PASS")
print("ALL PASS" if all(results) else "FAILURES PRESENT"); sys.exit(0 if all(results) else 1)
