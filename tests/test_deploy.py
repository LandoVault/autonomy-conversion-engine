"""Deployment packet tests: bootstrap -> verify on fresh temp folders (never the real stores).
Temp folders are kept, never deleted (project no-delete rule).
Run: python tests/test_deploy.py
"""
import os, subprocess, sys, tempfile

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOT = os.path.join(REPO, "deploy", "bootstrap_stores.py")
VERIFY = os.path.join(REPO, "deploy", "verify_deploy.py")
results = []
def t(name, cond): results.append(bool(cond)); print(("PASS " if cond else "FAIL ") + name)
def run(*a, env=None): return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, env=env)

root = tempfile.mkdtemp(prefix="ace_deploy_")
P = {k: os.path.join(root, d) for k, d in (("store", "ACE_storage"), ("local", "ACE_local"), ("hub", "ACE_hub"))}
args = sum(([f"--{k}", v] for k, v in P.items()), [])

r = run(BOOT, *args)
t("plan mode writes nothing", r.returncode == 0 and "would" in r.stdout and not any(os.path.exists(p) for p in P.values()))

r = run(BOOT, "--apply", *args)
t("apply creates the three stores", r.returncode == 0 and all(os.path.isdir(os.path.join(p, ".git")) for p in P.values()))
t("control-plane layout present", all(os.path.isdir(os.path.join(P["store"], *d.split("/"))) for d in
  ("outbox", "pending", "state", "audit", "archive/applied", "archive/rejected", "bridge/imports", "quality/evals")))
hub_files = subprocess.run(["git", "-C", P["hub"], "ls-files"], capture_output=True, text=True).stdout
t("hub initialized: engine-generated views committed as the gesture baseline",
  "views/Today.md" in hub_files and "views/Pending Panel Updates.md" in hub_files)
t("hub initialized: Ctrl+N lands in inbox/ and the root note carries the marks",
  '"newFileFolderPath": "inbox"' in open(os.path.join(P["hub"], ".obsidian", "app.json"), encoding="utf-8").read()
  and "## Marks" in open(os.path.join(P["hub"], "README.md"), encoding="utf-8").read())
t("scaffold committed with machine attribution",
  subprocess.run(["git", "-C", P["local"], "log", "-1", "--format=%an"], capture_output=True, text=True).stdout.strip() == "ACE Loop")

readme = os.path.join(P["local"], "inbox", "README.md")
with open(readme, "a", encoding="utf-8") as f: f.write("owner note\n")
own = os.path.join(P["local"], "research", "mine.md")
with open(own, "w", encoding="utf-8") as f: f.write("personal\n")
r = run(BOOT, "--apply", *args)
t("re-run is a no-op and overwrites nothing", "nothing to do" in r.stdout and open(readme, encoding="utf-8").read().endswith("owner note\n"))
t("owner files are never committed by the bootstrap",
  "mine.md" not in subprocess.run(["git", "-C", P["local"], "ls-files"], capture_output=True, text=True).stdout)

r = run(BOOT, "--store", P["store"], "--local", os.path.join(P["store"], "x"), "--hub", P["hub"])
t("nested stores are refused", r.returncode == 2 and "REFUSED" in r.stdout)

r = run(VERIFY, *args, "--skip-tests")
t("verify passes on a fresh deployment", r.returncode == 0 and "DEPLOY OK" in r.stdout)
t("verify confirms the engine resolves the same paths", "PASS  engine resolves the same store paths" in r.stdout)

subprocess.run(["git", "-C", P["local"], "remote", "add", "origin", "https://example.invalid/x.git"], check=True)
r = run(VERIFY, *args, "--skip-tests")
t("verify FAILS when the content plane has a remote (hard rule)", r.returncode == 1 and "FAIL  content plane has NO remote" in r.stdout)

print(f"  sandbox kept (no-delete rule): {root}")
print(f"\n{sum(results)}/{len(results)} PASS")
print("ALL PASS" if all(results) else "FAILURES PRESENT"); sys.exit(0 if all(results) else 1)
