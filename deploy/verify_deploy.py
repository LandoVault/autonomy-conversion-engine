#!/usr/bin/env python3
"""ACE deployment check — read-mostly verification of an ACE install on this machine.

Checks: Python/git present · the three stores exist with the spec/11 layout · a write/readback probe per
store (kept inside the store's .git folder: never committed, never deleted, overwritten each run) ·
the content plane has NO git remote (hard rule) · the control plane's remote, if any, is private ·
the engine resolves the same store paths · the engine test suites pass · the backup task is registered.
Writes nothing else. Exit code 0 = no FAIL.

Usage:  python deploy/verify_deploy.py [--store PATH] [--local PATH] [--hub PATH] [--skip-tests]
"""
import argparse, importlib.util, json, os, shutil, subprocess, sys
from datetime import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
spec = importlib.util.spec_from_file_location("bootstrap_stores", os.path.join(HERE, "bootstrap_stores.py"))
boot = importlib.util.module_from_spec(spec); spec.loader.exec_module(boot)

rows = []
def row(status, check, detail=""): rows.append((status, check, detail))

def git(root, *a):
    r = subprocess.run(["git", "-C", root] + list(a), capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else None

def probe(root):
    target = os.path.join(root, ".git") if os.path.isdir(os.path.join(root, ".git")) else root
    p = os.path.join(target, "ace_probe")
    stamp = datetime.now().isoformat(timespec="seconds")
    tmp = p + ".ace_tmp_"
    with open(tmp, "w", encoding="utf-8") as f: f.write(stamp)
    os.replace(tmp, p)
    return open(p, encoding="utf-8").read() == stamp

def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    for k in boot.REF: ap.add_argument(f"--{k}")
    ap.add_argument("--skip-tests", action="store_true")
    args = ap.parse_args()
    roots = boot.paths(args)

    row("PASS" if sys.version_info >= (3, 9) else "FAIL", "python >= 3.9", sys.version.split()[0])
    row("PASS" if shutil.which("git") else "FAIL", "git on PATH", shutil.which("git") or "missing")

    missing = [p for kind, p, _ in boot.plan(roots) if kind in ("dir", "git")]
    row("PASS" if not missing else "FAIL", "store layout (spec/11) + git repos",
        "complete" if not missing else f"{len(missing)} missing — run deploy/bootstrap_stores.py --apply")
    names = {"store": "control plane", "local": "content plane", "hub": "hub vault"}
    for k, root in roots.items():
        label = f"{names[k]} write/readback probe"
        if not os.path.isdir(root):
            row("FAIL", label, f"{root} does not exist"); continue
        try: row("PASS" if probe(root) else "FAIL", label, root)
        except OSError as e: row("FAIL", label, f"{root}: {e}")

    remotes = git(roots["local"], "remote") if os.path.isdir(roots["local"]) else None
    row("PASS" if not remotes else "FAIL", "content plane has NO remote (hard rule)",
        "none" if not remotes else f"remote(s) found: {remotes} — remove them; personal content never leaves this machine")
    hub_r = git(roots["hub"], "remote") if os.path.isdir(roots["hub"]) else None
    row("PASS" if not hub_r else "WARN", "hub vault is local (R2-9)", "no remote" if not hub_r else f"remote(s): {hub_r}")
    views = [v for v in ("Today.md", "Pending Panel Updates.md", "Commitments and Return.md", "Weekly Review.md")
             if not os.path.exists(os.path.join(roots["hub"], "views", v))]
    row("PASS" if not views else "WARN", "hub views generated (gesture baseline)",
        "4/4" if not views else f"missing {', '.join(views)} — run: python engine/ace_engine.py views")
    try:
        app = json.load(open(os.path.join(roots["hub"], ".obsidian", "app.json"), encoding="utf-8"))
        ok = app.get("newFileLocation") == "folder" and app.get("newFileFolderPath") == "inbox"
        row("PASS" if ok else "WARN", "Obsidian new notes land in inbox/", "set" if ok else
            "Obsidian: Settings > Files and links > Default location for new notes > In the folder specified below > inbox")
    except (OSError, ValueError):
        row("WARN", "Obsidian new notes land in inbox/", "no .obsidian/app.json — open the hub as a vault, then set the default note folder to inbox")
    url = git(roots["store"], "remote", "get-url", "origin") if os.path.isdir(roots["store"]) else None
    if not url:
        row("INFO", "control-plane remote", "none (local-only control plane is valid; engine pushes are skipped)")
    elif shutil.which("gh") and "github.com" in url:
        vis = subprocess.run(["gh", "repo", "view", url, "--json", "visibility", "-q", ".visibility"], capture_output=True, text=True).stdout.strip()
        row("PASS" if vis == "PRIVATE" else "FAIL", "control-plane remote is private", f"{url} -> {vis or 'unknown'}")
    else:
        row("WARN", "control-plane remote is private", f"{url} — confirm it is PRIVATE (gh not available to check)")

    env = {**os.environ, "ACE_STORE": roots["store"], "ACE_LOCAL": roots["local"], "ACE_HUB": roots["hub"]}
    code = ("import importlib.util,json,sys;s=importlib.util.spec_from_file_location('e',sys.argv[1]);"
            "m=importlib.util.module_from_spec(s);s.loader.exec_module(m);print(json.dumps([m.STORE,m.LOCAL,m.HUB,m.ACE]))")
    r = subprocess.run([sys.executable, "-c", code, os.path.join(REPO, "engine", "ace_engine.py")], capture_output=True, text=True, env=env)
    try:
        st, lo, hu, rp = json.loads(r.stdout)
        same = [boot.norm(x) for x in (st, lo, hu)] == [boot.norm(roots[k]) for k in ("store", "local", "hub")]
        row("PASS" if same else "FAIL", "engine resolves the same store paths", f"repo {rp}")
    except (ValueError, TypeError):
        row("FAIL", "engine imports", (r.stderr or r.stdout).strip()[-200:])

    if not args.skip_tests:
        for t in ("test_engine.py", "test_engine_replay.py"):
            r = subprocess.run([sys.executable, os.path.join(REPO, "tests", t)], capture_output=True, text=True)
            tail = (r.stdout.strip().splitlines() or ["(no output)"])[-1]
            row("PASS" if r.returncode == 0 else "FAIL", f"tests/{t}", tail)
    else:
        row("INFO", "engine tests", "skipped (--skip-tests)")

    if os.name == "nt":
        r = subprocess.run(["schtasks", "/query", "/tn", "ACE_backup_daily"], capture_output=True, text=True)
        row("PASS" if r.returncode == 0 else "WARN", "backup task ACE_backup_daily",
            "registered" if r.returncode == 0 else "not registered — deploy/register_backup_task.ps1 (needs the owner's backup destination)")

    w = max(len(c) for _, c, _ in rows)
    for s, c, d in rows: print(f"{s:4}  {c:<{w}}  {d}")
    fails = sum(s == "FAIL" for s, _, _ in rows)
    print(f"\n{'DEPLOY OK' if not fails else f'{fails} FAIL'} - {sum(s == 'WARN' for s, _, _ in rows)} warning(s)")
    return 1 if fails else 0

if __name__ == "__main__":
    sys.exit(main())
