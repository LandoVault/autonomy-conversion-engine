# ACE Workspace Atlas

**v1.1 (2026-07-19).** The researched instantiation of `02_FINAL_DESIGN.md` §Workspace localization. Sources: 7 parallel survey agents (Desktop, Documents, data drive, PKM vaults, git workspace, spec corpus, docx diff) + a completeness critic, 2026-07-19. Workspace manifests and session packets select roots **from this atlas**; agents never crawl outside their manifest.

*Public release: the roots, folder names and counts below are illustrative examples; a deployer builds its own atlas. The spec's provenance folders (`reference materials/`, `dev_log/`) are not included in the public release.*

**Method discipline carried from the research**: observed vs inferred is marked; staleness by mtime is *provisional* (see §Signal pollution); privacy zones are indexed by name only — their contents were never opened and must never be.

## Access classes

| Class | Meaning |
|---|---|
| `RW` | ACE loops/panels may write (only `ACE`, `ACE_storage`, and `F:\ACE_local` qualify) |
| `RO-REF` | read-only reference; ACE may index and cite, never modify |
| `NAME-ONLY` | index by file/folder name only; contents never read by any ACE agent |
| `EXCLUDED` | out of ACE scope entirely; existence may be noted, nothing else |
| `UNRULED` | pending the operator's Round-1 ruling |

## Universe table

*(Rows below the three ACE stores are illustrative.)*

| Root | Role for ACE | Class | Staleness (evidence) |
|---|---|---|---|
| `F:\git\ACE` | engine repo (specs, schemas, loops, skills) — code only, holds no instance state | RW | live — this build |
| `F:\git\ACE_storage` | **control plane**: state, hub, audit, quality, hashed manifests — private remote only; no clinical/IP content | RW | live — this build |
| `F:\ACE_local` | **content plane**: captures, research/IP, evidence artifacts — local git, NO remote ever | RW | live — created 2026-07-19 per the operator's ruling |
| `%USERPROFILE%\Desktop` | active working tree, numbered domains, own agent contract | RO-REF (+NAME-ONLY zones) | one-shot index snapshot, drifted (un-indexed workstreams) |
| `%USERPROFILE%\Documents` | archive + notebook cache + live scheduled-skill configs | RO-REF (+NAME-ONLY zones) | mostly archive; only the Claude scheduled-skills folder live |
| `<data drive>` | main work-data drive, flat topic/project folders | RO-REF (+NAME-ONLY zones) | mixed; active cluster listed below |
| `<legacy PKM vault>` | legacy PKM corpus (notebook→Obsidian import) | RO-REF (+NAME-ONLY zones) | stalled weeks after import; app opened 2026-07-19 |
| `<per-purpose literature vault>` | empty per-purpose vault (proto-ACE literature plan) | UNRULED (Q-E4) | created, never populated |
| `<git workspace>` (other repos) | prior-art workshop; reuse sources | RO-REF (+NAME-ONLY zones) | recent cluster active |
| `<secondary drive>` | unknown — discovered by critic, never mapped | UNRULED (Q-A1) | unknown |
| `<archive drive>` (legacy trees) | unknown — never mapped | UNRULED (Q-A1) | unknown |
| `%LOCALAPPDATA%\Microsoft\OneNote\16.0\Backup\<notebook>` | notebook backup snapshots — freshest local copy of the notebook | RO-REF (+NAME-ONLY zones) | dated snapshots; newest over a year old |
| `<cloud notebook>` / `<cloud drive>` / `<task log>` / `<read-later service>` / email / calendar | off-filesystem parts of the historical system of record | UNRULED (Q-A2, Q-F2) | unknown — uninspectable from disk |

## Per-root notes

*(Illustrative — each bullet records a pattern a deployer should expect in its own territory.)*

### %USERPROFILE%\Desktop

- **Contract**: its own agent contract (`CLAUDE.md`) — read `_INDEX.md` → `STATUS.md`, ≤3 levels, inbox triage, `<personal zone>` filename-only. ACE inherits and must not weaken these rules.
- **Drifted index layer**: the `_INDEX.md`/`STATUS.md` files were all auto-generated in one pass, self-labeled "verify", never updated since (the contract's update rule never fired — lineage-guard evidence). Of the projects STATUS lists as active (e.g. MANUSCRIPT-1, PROJECT-Q (a research project), PROJECT-L (a literature-workflow project)), only PROJECT-L moved on disk since; the newest activity sits in two *un-indexed* workstreams, WORKSTREAM-1 (a template-update workstream) and WORKSTREAM-2, possibly the same effort — relationship unconfirmed (Q-E3).
- **Traps**: 0-byte cloud placeholders in some project folders (real payloads in adjacent .zip); an archive index listing folders that don't exist; nested empty shells (contents below level 3 unknown); a folder assumed to be an empty shell that actually held real files.
- **NAME-ONLY**: `<personal zone>` entirely (incl. its `<personal zone index>` — unopened; boundary procedure is Q-G1).

### %USERPROFILE%\Documents

- **Role**: tidy archive (PARA shells all stamped on a single day), not a working tree; the bulk is inert application cache. It holds a non-updating notebook cache (`<archive>\<notebook cache>`, PARA/GTD-organized, long stalled) whose section names are a ground-truth life/work taxonomy as of its last sync.
- **Notebook backup store** *(added v1.2 per the operator's ruling)*: `%LOCALAPPDATA%\Microsoft\OneNote\16.0\Backup\<notebook>` — dated per-section snapshots of the **same notebook**, newer than the archive cache. **This is the freshest known local copy and the preferred rescue source.** Class: RO-REF; personal-named sections stay NAME-ONLY. Whether a cloud copy is newer still is Q-A2.
- **Live and orphaned**: the Claude scheduled-skills folder holds four legacy scheduled skills that reference `<another meta-system repo>` (registry/firing state unverified, Q-C2); an orphaned empty vault folder in Documents (unregistered in Obsidian) awaits a fate ruling (Q-B2); `<reference-manager library folder>` is EndNote-owned — never agent-written (Q-E5).
- **NAME-ONLY**: personal folders, personal-admin folders (examples withheld), loose personal documents.

### `<data drive>`

- **Shape**: flat, organic, no master index. Misleading names exist — e.g. a `<Projects>` folder that is a stale notebook export, not an index; `<A>` ≠ `<A-suffix>` (name overlap only); an empty `New folder`. Top-level mtimes lag subtrees (verified: one project's top level 06-18 vs subtree write 07-18) — staleness must walk subtrees.
- **Active cluster** (examples): PROJECT-P (a research proposal; live git repo + RQGM loop), PROJECT-E (an evaluation project), a review toolkit (packaged skill + state machine), the existing seal folders. **Seals** = frozen gold JSON + `_sha256` (+ exploit logs) emitted by a sibling anomaly-loop prototype — loop machinery evidence, the convention `ACE_storage/seals/` adopts (Q-B4 rules where future seals land).
- **ACE antecedent pattern** (4 independent 2026 projects converged on it): router `CLAUDE.md` + state machine + `dev_log/` + `HANDOFF_YYYY-MM-DD.md` + packaged `dist/` skill + RQGM gating. ACE formalizes this, not invents it.
- **NAME-ONLY**: sensitive personal folders (examples withheld). **Clinical-side folders → ACE-C at most** — never into ACE-P unbridged.

### `<legacy PKM vault>` (and the PKM document set)

- **What it is**: Obsidian vault created by importing two OneNote notebooks — a GTD notebook (standard GTD lists) and a PARA notebook (Projects / Areas / Resources / Archives). Only a handful of notes were ever edited in Obsidian — the last one (`<a literature-workflow plan note>`) sketches an agentic literature workflow: the operator's own proto-ACE.
- **Verdict**: read-only legacy corpus. No Obsidian conventions to inherit (no tags, one wikilink, no templates); what IS inheritable: the PARA + role-based-Areas taxonomy, the GTD list vocabulary (ACE state names reuse it), and the import-time project portfolio as registry seed **after the operator's live/dead triage** (Q-E2 — seeding without triage launches ACE pre-polluted with zombie projects).
- **System documentation**: `<data drive>\<legacy PKM docs>` — the legacy review notes are the operator's own record of what the earlier system (OneNote GTD+PARA, notebook-based) was and exactly where it hurt (maintenance burden, recurring next actions, waiting-for mechanics, strategic-planning homelessness, duplicate Projects trees). These unsolved requirements are ACE feature drivers.
- **Zones and registry**: personal folders are NAME-ONLY; third-party private items are EXCLUDED (existence noted only — content-based rule). GTD list notes mix personal+professional in single files — any legacy ingestion needs per-item review, not blanket import (Q-G1). Vault registry (`%APPDATA%\obsidian\obsidian.json`): exactly two vaults — the legacy PKM vault and the per-purpose literature vault — both opened 2026-07-19 (actor unknown, Q-C3); the orphaned Documents vault is a third, unregistered.

### `<git workspace>`

- **Canonical prior art**: another meta-system (loop taxonomy, recommendation ledger, session-close ritual), `rqgm-loop` (mature RQGM skill), a sibling anomaly-loop prototype, prior-art session-handoff and memory plugins.
- **NAME-ONLY / EXCLUDED**: clinical-side audit folders → ACE-C at most; out-of-scope personal files found in any repo folder are NAME-ONLY; third-party private items are EXCLUDED (content-based rule per CLAUDE.md). Session-derived operator corpora (e.g. the operator-session audit corpus): sensitive, never redistribute.

## Signal pollution (why naive staleness detection will lie)

Documented in research; design rule 9 (02) and PA-2 (03) respond to it:

1. 0-byte cloud placeholders (Desktop project folders) — filename inventories overcount; hydration state unverified.
2. App-open config touches (Obsidian stamped both vaults' configs 2026-07-19 without any note edit).
3. Top-level mtimes lag subtree writes (one project: 30 days).
4. One-shot auto-generated snapshots read as "maintained" (Desktop index layer, all generated the same day).
5. Non-human or unattributed writes already mutate the territory (a vault canvas changed *during* the research window — actor unknown, Q-C3; 4 scheduled skills declare their own cadence, firing unverified, Q-C2).
6. Generated-docx metadata carries library-default timestamps.

## Standing operational rules *(added v1.2 per the operator's rulings)*

- **Never delete.** ACE never deletes any file or folder outside its own stores — including external roots it merely inspects (an empty `New folder` on an inspected root is explicitly not deletable); inside ACE stores, supersede-by-move only.
- **Legacy non-updating sources** (legacy PKM vault, notebook caches): surface as `pending`/`known_stale` in the hub — never sync their content in.
- **Two-plane sensitivity rule**: content (personal/IP) → `F:\ACE_local`; state/metadata/hashes → `ACE_storage`; clinical → institution-side ACE-C (institution-approved tools), bridged only as approved non-PHI packages.

## Standing privacy rules (aggregate — bind every manifest)

1. No PHI, patient-identifying data, or restricted clinical content in ACE-P, ever (NFR-6).
2. Other people's private personal matters (third-party content): EXCLUDED wherever encountered — including unlisted locations (the rule is content-based, not path-based). No third-party names in remoted docs.
3. NAME-ONLY zones above are floors, not ceilings — when a new personal-looking item appears, default to NAME-ONLY until the operator classifies.
4. Interview record (06) and the operator-session audit corpus load only for strategic tasks.
5. Your instance's state and content stores stay private (control plane on a private remote only; no AI-training use); `F:\ACE_local` never gets a remote at all.
6. *(R2-11 ruled)* Clinical trial/committee identifiers appear in remoted docs only as short aliases (e.g. TRIAL-A, COMMITTEE-1); the key stays in `F:\ACE_local\aliases.md`, never mirrored.

---

### Change log

- **Public release** — genericized: the real roots, drives, folder and vault names, cloud services, counts, personal-system staleness dates and NAME-ONLY zone names were replaced with illustrative examples; access classes, method discipline, universe-table structure, observed patterns and standing rules are kept. Privacy rule 6 updated to the R2-11 ruling.
- **v1.2 (2026-07-19)** — Round-1 rulings: added `F:\ACE_local` root (RW), recast ACE_storage as control plane, notebook backup store row, standing operational rules (no-delete, legacy-pending, two-plane), RW definition updated, third-party names removed from operating text, clinical-identifier interim gate.
- **v1.1 (2026-07-19)** — created from the 7-mapper survey + completeness critique. Unknowns are marked UNRULED with Q-refs rather than guessed.
