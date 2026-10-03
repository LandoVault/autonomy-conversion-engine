#!/usr/bin/env python3
"""ACE gesture watcher — harvests the operator's hub gestures as decisions (spec/12 M1, spec/13).

Watches the ACE_HUB views for operator-made edits against the engine-generated baseline.
The engine wrote the view; any diff is human by definition (engine regenerates after
every harvest, so its own writes are always the baseline).

Gestures harvested (v1 — Pending Panel Updates view):
  - [x] `X-ID`      tick     = ACCEPT the package (runs ace_engine.accept)
  ~~ ... `X-ID` ~~  strike   = REJECT the package (runs ace_engine.reject)
  @YYYY-MM-DD (or legacy >>) suffix = DEFER: hold the package, re-annunciate on that date

Anything unparseable is ignored, never guessed (registry rule). Each harvest is audited
with actor=operator, channel=hub-gesture. Run manually or on a schedule.
Activation as the standing loop awaits R4-1 confirmation; running it by hand is the operator's call.
"""
import os, re, sys, json, importlib.util
from datetime import datetime

spec = importlib.util.spec_from_file_location("ace_engine", os.path.join(os.path.dirname(__file__), "ace_engine.py"))
eng = importlib.util.module_from_spec(spec); spec.loader.exec_module(eng)
HUB, STORE = eng.HUB, eng.STORE  # one source of truth for store locations (env-overridable in ace_engine)

def harvest():
    view = os.path.join(HUB, "views", "Pending Panel Updates.md")
    if not os.path.exists(view):
        print("no Pending view"); return 0
    text = open(view, encoding="utf-8").read()
    actions = []
    for line in text.splitlines():
        m = re.search(r"`(X-[A-Za-z0-9_-]+)`", line)
        if not m: continue
        xid = m.group(1)
        if not os.path.isdir(os.path.join(STORE, "pending", xid)):
            continue  # already handled or unknown — ignore, never guess
        low = line.strip().lower()
        defer = re.search(r"(?:@|>>)\s*(\d{4}-\d{2}-\d{2})", line)
        if low.startswith("- [x]"):
            actions.append(("accept", xid, None))
        elif line.strip().startswith("~~") or "~~" in line.split("`")[0]:
            actions.append(("reject", xid, None))
        elif defer:
            actions.append(("defer", xid, defer.group(1)))
    if not actions:
        print("no gestures found (view unchanged)"); return 0
    refused = []
    for act, xid, arg in actions:
        eng.audit({"type": "gesture", "actor": "operator", "channel": "hub-gesture",
                   "gesture": act, "id": xid, "arg": arg})
        if act == "accept":
            print(f"gesture: tick on {xid} -> accept")
            if eng.accept(xid): refused.append(xid)
        elif act == "reject":
            print(f"gesture: strike on {xid} -> reject")
            if eng.reject(xid): refused.append(xid)
        elif act == "defer":
            hold = os.path.join(STORE, "pending", xid, "HOLD_UNTIL.txt")
            open(hold, "w", encoding="utf-8").write(arg + "\n")
            print(f"gesture: defer {xid} until {arg} (no_action_before; re-annunciates)")
    eng.gen_views()  # regenerate: baseline is engine-authored again
    eng.commit(STORE, f"gesture harvest: {', '.join(a+' '+x+(' (refused)' if x in refused else '') for a,x,_ in actions)}")
    return 1 if refused else 0

if __name__ == "__main__":
    sys.exit(harvest())
