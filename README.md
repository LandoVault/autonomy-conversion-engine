# ACE — Autonomy Conversion Engine

A local-first, federated personal operations system: agent-panel-first, Obsidian-hub-centered, loop-backed, and two-layered — **ACE-P** (personal work surface) and **ACE-C** (institution-side tools for regulated/clinical work), bridged only by reviewed, sanitized, minimum-necessary packages.

ACE aims to reduce cognitive burden, improve ordinary execution reliability, and convert selected work into durable evidence and increased autonomy.

> Ask agents to do bounded cognitive work; use loops to preserve continuity; use Obsidian to preserve human legibility and control.

## About this release

This is a public, de-identified snapshot of a single-operator build. The specs were written for one person's instance; personal details have been replaced with generic placeholders ("the operator"), and the most personal records were reduced to templates. Two folders from the working repo are **not included**: the frozen provenance materials (`reference materials/`) and the build/telemetry log (`dev_log/`). References to them in the specs are kept for traceability only.

Paths such as `F:\ACE_local` or `F:\git\ACE_storage` are the defaults of the original instance — change them for your own deployment (set `ACE_STORE`, `ACE_LOCAL` and `ACE_HUB`; see Requirements below).

## Repo map

| Path | What |
|---|---|
| `CLAUDE.md` / `AGENTS.md` | operating contract for every agent session (vendor-neutral despite the name) |
| `spec/` | the living spec — `00_INDEX.md` has the read order |
| `engine/` | deterministic loops (standard-library Python): validator, accept/reject/rollback (write-ahead), views, clarify, gesture watcher, manifest, backup |
| `schemas/`, `templates/` | exit/transfer/manifest schemas; session-packet and package templates |
| `tests/` | `test_engine.py` (gates), `test_engine_replay.py` (replay/crash/rollback), `test_deploy.py` (deployment) |
| `deploy/` | local-storage deployment packet — `README.md` (by hand) or `DEPLOY_PACKET.md` (hand to a coding agent); bootstrap, verify, and backup-task scripts |

Durable state lives in a separate companion store (`ACE_storage`), never in this repo.

## Requirements

The engine is standard-library Python plus git. There are no packages to install, no API keys, and no model calls: Claude (Claude Code or Cowork) is the agent panel that works alongside the engine, not something the engine depends on. ACE was developed and tested on Windows. macOS should run the engine and tests but is untested; see the macOS notes below.

| Dependency | Used for | Windows | macOS |
|---|---|---|---|
| Python ≥ 3.9 (stdlib only; developed on 3.13) | engine, loops, tests, deploy scripts | `winget install Python.Python.3.13` or the python.org installer; run as `python` or `py` | Xcode Command Line Tools (`xcode-select --install`, which provides `python3` and git) or Homebrew `brew install python`; run as `python3` |
| git ≥ 2.28 (for `git init -b`) | the three stores, loop commits, backup bundles | `winget install Git.Git` (Claude Code on Windows usually has it already; check `git --version`) | Command Line Tools (above) or `brew install git` |
| PowerShell 5+, robocopy, Task Scheduler | `engine/backup_ace.ps1`, `deploy/register_backup_task.ps1`, `deploy/ace_env.example.ps1` | built in | not available as packaged; see the notes below |
| Obsidian (optional) | viewing and reviewing the hub vault | `winget install Obsidian.Obsidian` | download from obsidian.md, or `brew install --cask obsidian` |
| GitHub CLI `gh` (optional) | lets `verify_deploy.py` confirm a GitHub control-plane remote is private | `winget install GitHub.cli` | `brew install gh` |

You don't need a global git identity: loop and bootstrap commits set their own author (`ACE Loop`).

**macOS notes**

- Set `ACE_STORE`, `ACE_LOCAL` and `ACE_HUB` (for example with `export` lines in `~/.zprofile`) before you run the engine or the deploy scripts. The built-in defaults are Windows drive paths, and on macOS they resolve to oddly named folders inside the current directory.
- The backup and scheduling scripts are Windows-only. On macOS, set up your own add-only backup that keeps the never-delete rule: for example, `git bundle create … --all` for each store plus `rsync -a` **without** `--delete`, run from launchd or cron. `verify_deploy.py` skips its backup-task check off Windows.
- The engine has two known Windows assumptions. The evidence-pointer gate recognizes `ACE_LOCAL` paths only in backslash form, so on macOS reference evidence with `sha256:` pointers. The visible-roots scope check recognizes only drive-letter roots, so it is not enforced for POSIX paths.
- Commands in this README and in `deploy/` are written for Windows. On macOS, use `python3` and forward slashes.

## Quick start

```bash
python tests/test_engine.py
python tests/test_engine_replay.py
python tests/test_deploy.py
```

To stand up your own stores, follow `deploy/README.md` (written for Windows; on macOS, apply the notes above).

## Privacy model

- Two planes: personal/IP content stays in a local-only content store that never gets a remote; state, metadata, and hashes go to the control store; clinical or otherwise regulated work stays in institution-approved tools.
- Never commit PHI, patient-identifying data, credentials, or secrets to any ACE store.
- Agents propose; deterministic loops record; humans approve consequential transitions.

## License

[Apache License 2.0](LICENSE) — see also [NOTICE](NOTICE).
