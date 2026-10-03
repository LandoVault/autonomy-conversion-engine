# ACE Storage and Filing Orchestration

**v1.3 (2026-07-19).** Status: `APPROVED (R2-2 sign-off) — four stores scaffolded; Phase-1 build underway`. v1.3 per R2-9: **the hub vault is local at `F:\ACE_hub`** (cross-device via Obsidian Sync, operator-enabled; local git, no remote) — not inside ACE_storage; the engine generates its `views/` from control-plane `state/` + `pending/`. R2-8 confirmed quality/audit layers on the control plane **with the compliance gate**: marginal/edge cases are scrubbed of personal information, PHI/regulated health content, and IP before recording. v1.2 implements the operator's Round-1 storage ruling: **two-plane storage — everything primary locally; the GitHub repo is the control plane** (cross-vendor + cross-computer communication, versioning, hashed metadata, FMEA/eval/audit layers), holding no clinical content and no significant IP-bearing work. Blindspot-pass findings remain baked in: rollback semantics, single-approver backpressure, atomic writes (META-2), state-sync gate (FMEA-001), re-annunciation (analog:alarm-management).

## Division of the three stores

| | `ACE` (engine, GitHub) | `ACE_storage` (control plane, GitHub) | `F:\ACE_local` (content plane, LOCAL ONLY) |
|---|---|---|---|
| Contains | specs, schemas, loop code, skills, templates, tests, dev_log (not included in the public release) | durable **state**: hub, packets, audit, seals, quality (FMEA/edge-cases/evals), local-content manifests | primary **content**: captures, personal research/proposals/prototyping (IP), evidence artifacts |
| Mutability | commits reviewed like code | **state transitions only** | Operator + bounded panel writes; local git versioning |
| Remote | any (code only; holds no instance state) | private only — the cross-vendor/cross-computer channel | **no remote, ever** |
| Sensitive content | never | never — pointers + sha256 only | yes (personal/IP; still no PHI, no clinical) |
| Clinical (ACE-C) | never | never (bridge/ carries approved non-PHI packages only) | never — committee/audit-level work stays institution-side (institution-approved AI tools) |

Rule zero, v1.2: **content that would hurt to lose lives in `F:\ACE_local`; state about it lives in `ACE_storage`; anything regenerable lives in `ACE` or is not stored at all.** The control plane knows *that* content exists, *where*, and *its hash* — never the content itself. Derived views (Today, briefs, dashboards) are generated, never sources of truth (carried from v0.1's derived-files rule).

## The manifest bridge (cross-computer / cross-vendor awareness without content leakage)

The engine's manifest loop hashes `F:\ACE_local` content into `ACE_local/manifests/` (path, sha256, size, mtime, project-ID) and mirrors those manifests — **metadata only** — to `ACE_storage/local_manifests/`. Any machine or vendor tool reading the control plane can therefore: verify integrity, detect staleness/divergence, and know what exists elsewhere — while a manifest referencing content this machine lacks is a **known-missing state**, never an error to "fix" by syncing content through GitHub. Hub evidence records point to artifacts by absolute path + sha256; Obsidian opens local links when on the owning machine.

**Path-disclosure policy** (filenames are content-derived slugs, so paths are themselves metadata-sensitive): `inbox/` and `research/` entries mirror as **opaque ULIDs + hash**, with the ID→path map staying in `ACE_local/manifests/` (never mirrored); `artifacts/` entries may mirror real paths.

## ACE engine repo layout (build phase will fill this)

```
ACE/
├── CLAUDE.md            # operating contract
├── spec/                # canonical living spec (this generation)
├── reference materials/ # frozen provenance — never edited (not included in the public release)
├── schemas/             # JSON-schema for every package type below   (slice 1)
├── engine/              # deterministic loops: validate, transition, staleness, return, brief
├── skills/              # packaged panel contracts (/ace-capture, /ace-panel, /ace-close)
├── templates/           # session-packet, exit-package, record templates (seed: v0.1 starter/)
├── tests/               # validator + state-machine tests (fixtures incl. FMEA-001 sync case)
└── dev_log/             # build log, skill telemetry, RQ epoch records (not included in the public release)
```

## Store layouts — both planes (scaffolded now, README in every directory; rules marked ⏳ are interim defaults pending Q-D3/D10/D11)

```
F:\ACE_local/            [CONTENT PLANE — local git, NO remote]
├── inbox/         # universal capture, CONTENT-PRIMARY (FR-1): free text + optional date
├── research/      # personal research / proposals / prototyping (IP) — operator + bounded panel writes
├── artifacts/     # shipped evidence artifacts, content-addressed, one folder per unit
├── manifests/     # GENERATED sha256+metadata index (single writer: manifest loop)
└── archive/       # superseded content — moved, never deleted

ACE_storage/             [CONTROL PLANE — GitHub private]
├── inbox/         # capture metadata stubs (hash+timestamp; content stays local)
├── packets/       # session packets GENERATED for panels (engine writes, panels read)
├── outbox/        # panel exit packages, awaiting validation (panels write here — only here)
├── pending/       # validated packages awaiting the operator's review  (= hub_pending state)
├── quality/       # FMEA_LOG.md, edge_cases/, evals/ — system-level quality layers (interim placement pending R2-8)
├── local_manifests/ # metadata-only mirror of ACE_local/manifests
├── hub/           # SUPERSEDED per R2-9 — vault is local at F:\ACE_hub; dir holds a pointer README only
│   ├── projects/  #   one note per project: state, next evidence, decision locks, resume
│   ├── commitments/ # commitments & returns (GTD vocabulary: waiting-for, no_action_before)
│   ├── evidence/  #   evidence records (FR-8) + handoff records (FR-9)
│   └── views/     #   GENERATED: Today, Pending Panel Updates, Weekly Review — never hand-edited
├── state/         # machine-readable truth the loops consume (YAML frontmatter mirrors hub)
├── audit/         # append-only events.jsonl (single-writer, typed events — anomaly-loop convention)
├── receipts/      # acknowledgments: transfer receipts, closure receipts, approval records
├── seals/         # frozen gold references + _sha256 manifests (RQGM/anomaly-loop seal convention)
├── bridge/
│   ├── exports/   # ACE-P → ACE-C packages (sanitized, approved, expiring)
│   └── imports/   # ACE-C → ACE-P packages + acknowledgment stubs (no PHI, ever)
└── archive/       # closed/rejected packages, superseded state — moved, never deleted
```

## Writer matrix (binding; enforced by validator + git author)

| Path | Panels/agents | Engine loops | Operator |
|---|---|---|---|
| `ACE_local/inbox/` (content) | append-only capture | read + clarify + stub-mirror | write |
| `ACE_local/research/` | write within declared panel write-boundary only | manifest loop reads | write freely |
| `ACE_local/artifacts/` | never | write on accepted evidence records | read |
| `ACE_local/manifests/`, `ACE_storage/local_manifests/` | never | single-writer manifest loop | read |
| `ACE_storage/inbox/` (stubs) | append stub only | write | read |
| `ACE_storage/quality/` | edge-case reports via exit packages | write | review |
| `packets/` | **read only** | write | read |
| `outbox/` | **sole agent-writable path for exit packages (state proposals + pointers)** — `ACE_local/inbox/` additionally accepts single capture lines; content artifacts go inside the panel's declared `ACE_local` write boundary | read + validate + move | read |
| `pending/` | never | write (from validated outbox) | review/annotate |
| `F:\ACE_hub\` (vault, except views/) | never | write accepted transitions | write freely (human authority) |
| `F:\ACE_hub\views\` | never | regenerate | read (edits are lost — generated) |
| `state/`, `audit/`, `receipts/`, `seals/` | never | single-writer append/update | read |
| `bridge/` | never | move approved packages | approve |
| `archive/` | never | move | read |

Git authorship encodes the actor (PA-2, **interim default pending Q-D5**): `<operator name>` (default), `ACE Loop <loop@ace.local>`, `ACE Panel <panel@ace.local>`. One commit per accepted state transition, message = `transition(<machine>): <from> -> <to> <id>`. Staleness loops read **human-authored** signals only.

## Flow → state-machine mapping

0. **Capture surfaces (v1.4)**: the human capture surface is `F:\ACE_hub\inbox\` (visible in Obsidian; Ctrl+N lands there; the vault is local so content-primary rules hold; if Obsidian Sync is on, captures travel via the operator's own Obsidian account per R3-5). `F:\ACE_local\inbox\` remains the capture path for panels and file drops. The clarify loop reads both.
1. **Capture**: anything → `F:\ACE_local\inbox\` (≤20s, no classification; content-primary because captures may contain personal content) → loop clarifies later and mirrors a metadata stub (hash + timestamp + engine-generated enumerated category tag; **never capture-derived prose**) to `ACE_storage/inbox/` → `commitment_return: captured → clarified`. **Clarify-time sensitivity rule**: control-plane commitment/project record text is title + state + dates + pointer; personal-sensitive items get an **alias title** with content staying in `ACE_local` (the NAME-ONLY pattern applied to ACE's own records).
2. **Panel cycle**: engine builds `packets/P-<id>.md` from atlas-derived manifest → panel works → writes `outbox/X-<id>/` → validator (schema + source-scope + FMEA-001 sync gate) → pass: move to `pending/`, hub flag `panel_update_awaiting_review`; fail: actionable errors back → `panel_lifecycle` states exactly.
3. **Review**: The operator reviews **in the hub vault** (`F:\ACE_hub`) — the generated `F:\ACE_hub\views\Pending Panel Updates.md` surfaces every item in `ACE_storage/pending/` (satisfying 02's hub view #2 and 05_HANDOFF's "Obsidian visibly shows a pending update", carried in 05_PLAN); `pending/` holds the package files the view links to. Approve/reject (target <3 min) → accepted: loop applies to `hub/` + `state/`, appends audit events, generates resume packet into `packets/`; rejected: → `archive/` with audit record.
4. **Rollback** *(blindspot #2)*: every accepted transition records its inverse in the audit event (`prev` snapshot hash + path). `ace rollback <event-id>` reverses hub+state to the prior snapshot **as a new audited transition** — history is never rewritten; git revert, not git reset.
5. **Backpressure** *(blindspot #3)*: `pending/` items age-tag at 7/14 days. At 14 days the item auto-degrades to `known_stale` on the hub (never silently accepted, never silently dropped) and enters the weekly review as a single line: "N pending updates expired unreviewed." Re-annunciation: `no_action_before` items re-fire at their date; shelving without expiry is structurally impossible (every deferral carries a date).
6. **Write safety** *(META-2)*: all engine writes are atomic (`tmp + os.replace`); session-start probe (write/readback) before any loop commits; never commit while a stale-mount signature is active.
7. **Seals**: RQ epoch contracts and gold references freeze into `seals/` with `_sha256` manifests (Q-B4 confirms whether existing seals on the data drive migrate or stay).

## Filing orchestration with the outside world

- External roots are **mounted read-only through the atlas** (08): manifests select roots; ACE never files into pre-existing personal folders (Desktop/Documents/`<data drive>`). Filing *into* those trees remains a human activity (or one governed by that folder's own agent contract) that ACE observes, not performs. No global renaming (frozen constraint).
- Legacy corpora (the legacy PKM vault, notebook caches/backup, the legacy PKM-system review docs on the data drive) are reference mounts: ACE may cite them in packets **excluding all NAME-ONLY and EXCLUDED items per 08 §Standing privacy rules** — citing requires reading, so the access classes bind citation exactly as they bind ingestion. Hub ingestion happens only via a reviewed panel proposal, per-item (mixed personal/professional content — never blanket import).
- The four legacy scheduled skills and another meta-system continue to own their paths until Q-C1/C2 rule; ACE_storage is disjoint from all of them by construction.

## Naming and retention

- Files: `YYYY-MM-DD_<slug>_vN.ext` (prior workspace convention, kept). Packets/packages: `P-`/`X-` + ULID. Records: stable project IDs (`prj-<slug>`), never renamed — aliases live in the record.
- Nothing in ACE_storage or ACE_local is ever deleted: superseded → `archive/`; the audit log is append-only; `git push` after every accepted transition is the control-plane durability gate (META-1; remote is private). **Standing rule (operator, 2026-07-19; scope conservatively generalized, confirm in R2-2): ACE never deletes any file or folder outside its own stores — including external roots it merely inspects; inside ACE stores, supersede-by-move only.**
- Content-plane durability is an open design item (R2-6): `<an existing backup-like folder>` was a one-off copy, not a live backup; F: needs a backup mechanism for `ACE_local` — **local/offline media only** (scheduled robocopy to external drive, second local disk, encrypted local archive); any cloud-touching backup, even encrypted, requires an explicit operator ruling in `10_OPEN_QUESTIONS.md`.
- Sensitivity gate on exit packages — **content-class rule, not size rule**: a control-plane package may carry state deltas, next actions, decision requests, and pointers + sha256 — **no substantive excerpts of research/proposal/personal text regardless of size**. Artifacts (draft text, data, figures) go to `ACE_local` inside the panel's declared write boundary, referenced by path+hash. The validator enforces the content-class rule (and rejects large blobs as a backstop).
- Bridge content bar: `bridge/` on the control plane holds **stubs, receipts, and hashes only** — package *bodies* live in `F:\ACE_local` (or transit institution-approved channels directly). "Non-PHI" is not "non-clinical": clinical-side work products do not transit GitHub.
- Quality/eval content bar: `quality/` and `seals/` carry no clinical, IP, or personal content; edge-case reports reference triggers by pointer+sha256 with synthetic minimal reproductions; gold references on the control plane are synthetic or pointer-based — real-content golds live in `ACE_local` with only their sha256 sealed.
- Legacy citation rule: packet citations of legacy corpora are pointer + line-range or short paraphrase of professional content only; mixed personal/professional files are cited by pointer only until per-item classified.

---

### Change log

- **v1.2 (2026-07-19)** — two-plane redesign per the operator's Round-1 rulings: added `F:\ACE_local` content plane (local-primary, no remote, IP/personal content), recast `ACE_storage` as the control plane (state + hashed metadata + FMEA/eval/audit; no clinical, no IP), added the manifest bridge, capture flow re-homed to local-primary, `quality/` + `local_manifests/` layers, no-delete standing rule, content-plane backup as open item. Hub confirmed as Obsidian control/review/surgical-update surface (work runs in Cowork panels).
- **v1.1 (2026-07-19)** — created; layout + writer matrix + flow mapping designed from spec v1.1, v0.1 folder/data spec, anomaly-loop/seal conventions, and blindspot-pass findings.
