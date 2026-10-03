# ACE Implementation Plan

**v1.1 (2026-07-19).** Subsumes `reference materials/05_HANDOFF.md` (not included in the public release); aligned with the v1.0 package's `08_IMPLEMENTATION_ROADMAP.md` (its Phases 0–7 map onto Phase 0/1/2+ below). Status: `research_complete — build gated on Round-1 answers (10_OPEN_QUESTIONS)`.

## The 14 accepted decisions (inlined verbatim from 05_HANDOFF — the frozen foundation)

1. ACE has two co-equal P0 goals: generic productivity and durable conversion.
2. The primary personal work surface is scoped Cowork/agent panels.
3. Obsidian is the durable human hub, not necessarily the first interaction surface.
4. Deterministic loops preserve state, deadlines, receipts, and auditability.
5. Skills package repeatable judgment procedures; plugins are limited to integration and UI boundaries.
6. Agents are temporary executors, not persistent owners of the system.
7. ACE-P and ACE-C are separate application layers.
8. Cross-layer movement uses reviewed, sanitized passing packages with target receipts.
9. Agents never receive assumed full access and must declare missing context.
10. Poor filenames and nested folders are handled through workspace maps and aliases before renaming.
11. Strategic interview conclusions remain hypotheses, loaded only when relevant.
12. PROJECT-W (the canonical handoff-example project) continues through publication, then follows the approved handoff.
13. The current architecture is evaluated through a frozen Red-Queen epoch.
14. The system must reduce cognitive operations, not merely create better organization.

## Phase 0 — Adjudication (NOW; blocks build)

1. The operator answers Round-1 questions (`10_OPEN_QUESTIONS.md`). Multiple rounds until clear — per the operator's instruction, building does not start before this.
2. Record every ruling in `10_OPEN_QUESTIONS.md` (inline answer) and, where it changes a spec, as a change-log entry in the affected doc. The research package in this repo now serves as the Phase-A evidence v0.1 mandated; reopening a frozen decision requires either an operator ruling here or a Red-Queen epoch (07) — there is no third path.

## Phase 1 — First vertical slice (unchanged scope from 05_HANDOFF)

One end-to-end personal-layer slice:

1. create a session packet from a workspace manifest (generated from `08_WORKSPACE_ATLAS.md`);
2. run one `produce` panel on selected folders;
3. generate an exit package;
4. validate required fields and access scope (deterministic validator);
5. create a pending update in the hub;
6. approve or reject the update;
7. update durable state in `ACE_storage`;
8. generate a resume packet;
9. verify audit history and rollback.

**Test-project candidates** (real, non-clinical, non-PHI, active — the operator picks, R2-1):

| Candidate | Location | Notes |
|---|---|---|
| **The operator's planning session** (rec — R2-1) | new; artifact into `F:\ACE_local` | a real, near-term planning need; the produce panel IS the planning session; bootstraps portfolio triage |
| PROJECT-P (a research proposal) | `<data drive>\<proposal folder>` | active 2026-07-18; already RQGM-wrapped; poorly named root ✔ |
| PROJECT-E (an evaluation project) | `<data drive>\<evaluation folder>` | active; has handoff/memory conventions ACE formalizes |
| PROJECT-Q (a research project) | `%USERPROFILE%\Desktop\<research folder>` | active per STATUS |
| PROJECT-L (a literature-workflow project) | the PROJECT-L vault + legacy PKM plan note | resurrects the operator's own proto-ACE plan; fate per Q-E4 |

*(v1.2: MANUSCRIPT-1 dropped — corrections are past (L10); WORKSTREAM-1 (template update) done, now being tested in use (Q-E3 partial).)*

`05_HANDOFF` warns against using the most complex project first. Caveat from the completeness critic: the agent-tooling candidates make the first evidence unit self-referential ("agent system manages agent project") — a manuscript or research project is a more honest P0 test.

**Prohibited first-slice work** (carried, condensed — full wording in 05_HANDOFF): no custom Obsidian plugin, no semantic search, no vector DB, no knowledge graph, no broad Gmail/Teams integrations, no autonomous portfolio reprioritization, no complete PARA migration, no continuous multi-agent daemon, no global file renaming system.

**Acceptance criteria** (inlined from 05_HANDOFF §Acceptance): panel receives only selected folders and states this clearly · exit package validates or fails with actionable errors · no accepted result remains only in chat · Obsidian visibly shows a pending update · review takes less than three minutes · accepted durable state is traceable to sources · rejected changes leave an audit record · a fresh panel resumes within ten minutes after a seven-day simulated gap · no extra dashboard or plugin is needed · maintenance burden is recorded. Plus v1.1: all writes attributable (design rule 9, if adopted) and zero ACE state written outside `ACE_storage`.

## Phase 2+ — Later slices (order carried from 05_HANDOFF; only after slice 1 passes)

1. commitment-and-return loop (capture → clarify → return; deterministic scheduler);
2. weekly reliability + conversion review (dual scoreboards, 06);
3. handoff state machine (first real case: PROJECT-W post-publication);
4. clinical transfer-package prototype (ACE-C; needs PA-3 sanitization criteria);
5. recurring tasks and scheduled resurfacing;
6. memory hygiene and hypothesis review (H1–H5 test implications, 06).

## Build conventions (builder decisions — smallest reversible option, recommendations)

| Open decision (05_HANDOFF) | Recommendation | Rationale |
|---|---|---|
| Hub record format | Markdown + YAML frontmatter; package schemas govern (`ACE_Final_Design_Package_v1_0/schemas/`, copied into this repo's `schemas/`: panel_exit_package, transfer_package, workspace_manifest), v0.1 `11_INITIAL_FOLDER_AND_DATA_SPEC` supplements for project/commitment/evidence records | official v1.0 schemas now on disk; Obsidian-native |
| Validation language | Python 3 (stdlib-first) | matches prior-art tooling and the operator's stack |
| Obsidian views | native properties + Bases; generated Markdown for Today/Weekly | no plugin in slice 1 (constraint) |
| Scheduling | Windows Task Scheduler for durable loops; Claude scheduled tasks only for judgment loops | v0.1's own argument: vendor schedules are session-scoped |
| Git convention | loops commit with attributed author (e.g. `ACE Loop <loop@ace.local>`); one commit per accepted state transition; humans commit normally | write attribution (PA-2); auditability NFR-5 |
| Panel launch | session-packet file handed to a Cowork/Claude panel; packet generator is a script, not an agent | deterministic-vs-model split |

## Reuse plan (from workshop research — import, don't reinvent)

- **rqgm-loop** skill — Red-Queen epochs (07).
- **A sibling anomaly-loop prototype** — runs beside RQGM (maturity ruling Q-D8); adopt its single-writer append-only `archive.jsonl` typed-event convention for the ACE audit log, and the seal convention (`gold_seedN.json` + `_sha256.txt`) for frozen references → `ACE_storage/seals/`.
- **session-close triple** (another meta-system) — a handoff / session-state / kickoff-prompt triple maps onto exit package + durable state + resume packet; reuse the ritual shape (coexistence ruling Q-C1).
- **prior-art session-handoff/memory plugins** — an episodic-log → distilled-card → gated-promotion memory pattern as the memory-hygiene substrate for Phase 2.6 (stdlib-only, JSON, local-first — matches NFR-1).
- **Loop taxonomy** (another meta-system) — loop vocabulary and binding rules (deterministic-verifier-first, blind confirmation on shipping verdicts).
- **v1.0 package templates** (`ACE_Final_Design_Package_v1_0/templates/`, copied into this repo's `templates/`: SESSION_PACKET, PANEL_EXIT_PACKAGE, HANDOFF_PACKAGE, CLINICAL_TRANSFER_PACKAGE) — the canonical package formats for slice 1.
- **v0.1 starter templates** (in the v0.1 zip, not included in the public release) — INBOX/RETURN/COMMITMENTS/WEEKLY + config.yaml, updated to v1.1 states and adopted limits.
- **A multi-model orchestration protocol (prior art)** — orchestrator/executor split and conflict ladder for any multi-model panel.

## End-state packaging (the operator's stated target: a plugin, loops, and scheduled tasks at multiple levels)

- **Skills/plugin**: ACE panel contracts packaged as a Claude plugin (scaffold per prior-art plugin conventions) — `/ace-capture`, `/ace-panel <type>`, `/ace-review`, `/ace-close`.
- **Loops**: deterministic scripts (validator, staleness, return-scheduler, brief generator) runnable standalone or via Task Scheduler.
- **Scheduled tasks**: daily brief, weekly review assembly, return-date firing — after the four legacy scheduled skills are reconciled (Q-C2).

---

### Change log

- **v1.1 (2026-07-19)** — created; carries 05_HANDOFF's slice definition, prohibitions, and acceptance criteria; adds Phase 0 gating, researched test-project candidates, build-convention recommendations, reuse plan, packaging targets.
