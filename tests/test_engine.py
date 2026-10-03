"""Unit tests for ace_engine validation gates (no side effects — pure checks only).
Run: python tests/test_engine.py
"""
import sys, os, importlib.util
spec = importlib.util.spec_from_file_location("ace_engine", os.path.join(os.path.dirname(__file__), "..", "engine", "ace_engine.py"))
eng = importlib.util.module_from_spec(spec); spec.loader.exec_module(eng)

GOOD = {"session_id": "P-0001", "panel_type": "produce", "objective": "x",
        "sources_seen": ["F:\\git\\ACE\\spec\\09_STATE.md"], "sources_not_seen": ["none"],
        "outcome": "ok", "proposed_state_changes": [{"project_id": "p"}],
        "next_action": "n", "hub_destination": "projects/p", "confidence": 0.9,
        "evidence_created": ["F:\\ACE_local\\artifacts\\a\\f.md sha256:abc"]}

def t(name, cond): print(("PASS " if cond else "FAIL ") + name); return cond

ok = True
ok &= t("schema: good package passes", eng.check_schema(GOOD) == [])
ok &= t("schema: missing field caught", any("missing" in e for e in eng.check_schema({k: v for k, v in GOOD.items() if k != "outcome"})))
ok &= t("schema: unknown field caught", any("unknown" in e for e in eng.check_schema({**GOOD, "extra": 1})))
ok &= t("schema: bad confidence caught", any("confidence" in e for e in eng.check_schema({**GOOD, "confidence": 2})))
ok &= t("content: excerpt >1500 chars caught", any("1500" in e for e in eng.check_content_class({**GOOD, "outcome": "x" * 1600})))
ok &= t("content: base64 blob caught", any("base64" in e for e in eng.check_content_class({**GOOD, "resume_context": "QUJD" * 200})))
ok &= t("content: evidence without pointer caught", any("pointer" in e for e in eng.check_content_class({**GOOD, "evidence_created": ["just a claim"]})))
ok &= t("content: good package passes", eng.check_content_class(GOOD) == [])
packet = "## Visible roots\n\n- `F:\\git\\ACE\\spec\\` (x)\n- `F:\\ACE_local\\` (y)\n"
ok &= t("scope: in-root source passes", eng.check_scope(GOOD, packet) == [])
ok &= t("scope: out-of-root source caught", any("outside" in e for e in eng.check_scope({**GOOD, "sources_seen": ["C:\\Windows\\x"]}, packet)))
ok &= t("scope: empty sources_not_seen caught", any("partial-observability" in e for e in eng.check_scope({**GOOD, "sources_not_seen": []}, packet)))
print("\nALL PASS" if ok else "\nFAILURES PRESENT"); sys.exit(0 if ok else 1)
