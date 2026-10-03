#!/usr/bin/env python3
"""ACE manifest loop — content plane -> control plane metadata mirror (spec 11 §Manifest bridge).

Hashes $ACE_LOCAL content into ACE_local/manifests/manifest.json, then mirrors
METADATA ONLY to ACE_storage/local_manifests/manifest.json under the path-disclosure
policy: inbox/ and research/ entries mirror as opaque IDs + hash (ID->path map stays
local, never mirrored); artifacts/ and aliases/archive entries stay local-only too —
only artifacts/ mirrors real paths. Single writer. Atomic writes (META-2).

Privacy note for deployers: both manifests record the host machine name
(COMPUTERNAME, "?" if unset), and the mirrored copy is committed and pushed to the
control-plane remote — keep that remote private.
"""
import json, os, hashlib, subprocess
from datetime import datetime, timezone

LOCAL = os.environ.get("ACE_LOCAL", r"F:\ACE_local")        # same env overrides as ace_engine (deploy/README.md)
STORE = os.environ.get("ACE_STORE", r"F:\git\ACE_storage")
OPAQUE_DIRS = ("inbox", "research")          # mirror as opaque id + hash
REAL_DIRS = ("artifacts",)                   # mirror with real path
NEVER_MIRROR = ("aliases.md", "archive")     # alias key + provenance originals: local existence only, no entry

def now(): return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")

def atomic(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        json.dump(obj, f, indent=1, ensure_ascii=False)
    os.replace(tmp, path)

def run():
    local_entries, mirror_entries, idmap = [], [], {}
    for root, dirs, files in os.walk(LOCAL):
        dirs[:] = [d for d in dirs if d not in (".git", "manifests")]
        for fn in files:
            p = os.path.join(root, fn)
            rel = os.path.relpath(p, LOCAL).replace("\\", "/")
            h = hashlib.sha256(open(p, "rb").read()).hexdigest()
            st = os.stat(p)
            entry = {"path": rel, "sha256": h, "size": st.st_size,
                     "mtime": datetime.fromtimestamp(st.st_mtime).isoformat(timespec="seconds")}
            local_entries.append(entry)
            top = rel.split("/")[0]
            if rel == NEVER_MIRROR[0] or top == NEVER_MIRROR[1]:
                continue  # local existence only
            if top in OPAQUE_DIRS:
                oid = "ID-" + hashlib.sha256(("ace-path:" + rel).encode()).hexdigest()[:16]
                idmap[oid] = rel
                mirror_entries.append({"id": oid, "sha256": h, "size": st.st_size, "mtime": entry["mtime"]})
            elif top in REAL_DIRS:
                mirror_entries.append(entry)
            else:  # READMEs and misc at root: harmless, mirror real
                mirror_entries.append(entry)
    stamp = now()
    atomic(os.path.join(LOCAL, "manifests", "manifest.json"),
           {"generated": stamp, "machine": os.environ.get("COMPUTERNAME", "?"), "entries": local_entries})
    atomic(os.path.join(LOCAL, "manifests", "idmap.json"), {"generated": stamp, "map": idmap})
    atomic(os.path.join(STORE, "local_manifests", "manifest.json"),
           {"generated": stamp, "machine": os.environ.get("COMPUTERNAME", "?"),
            "policy": "inbox/research opaque; artifacts real; aliases/archive omitted", "entries": mirror_entries})
    A = ["-c", "user.name=ACE Loop", "-c", "user.email=loop@ace.local"]
    for repo, msg in ((LOCAL, "manifest: refresh"), (STORE, "manifest: mirror metadata from content plane")):
        subprocess.run(["git", "-C", repo] + A + ["add", "-A"], capture_output=True)
        r = subprocess.run(["git", "-C", repo] + A + ["commit", "-q", "-m", msg], capture_output=True)
        if r.returncode == 0 and repo == STORE:
            subprocess.run(["git", "-C", repo, "push", "-q"], capture_output=True)
    print(f"manifest: {len(local_entries)} local entries; {len(mirror_entries)} mirrored ({len(idmap)} opaque); {stamp}")

if __name__ == "__main__":
    run()
