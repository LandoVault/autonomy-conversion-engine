# ACE Red-Queen Validation Contract

**Status: `FROZEN — Epoch-1 contract confirmed by the operator (R2-2 sign-off, 2026-07-19)`**

Provenance: this file was a dangling reference in codex.md until the full package `reference materials/ACE_Final_Design_Package_v1_0/` (not included in the public release) arrived on disk 2026-07-19 (during this session — L1 asks you to confirm you placed it). Its `07_RED_QUEEN_VALIDATION.md` is carried below **in full**. The 10-row table earlier recovered from the design docx is that package's evaluator panel in condensed wording (e.g. docx "Reliability" = package "Generic productivity"; "Handoff" = "Handoff durability"; "Partial access" = "Partial-access honesty") — the package wording governs.

In-force semantics until Q-D1 is ruled: this contract may **block** design mutations (conservative direction) but cannot **approve** any — amendment door 2 in `00_INDEX.md` is closed until the operator confirms the freeze.

## Purpose

ACE will be validated through adversarial co-evolution. Each architecture epoch faces stronger attacks derived from the previous epoch's failures. The evaluation contract is frozen within an epoch. Criteria may change only after an epoch is complete.

## Generator under test

> scoped Cowork panel → typed stop condition → structured exit package → deterministic validation → tiered approval → Obsidian durable hub → scheduled return/resume loops

## Adversarial roles

1. Cognitive-burden attacker
2. Fragmentation attacker
3. Trajectory attacker
4. Trust attacker
5. Partial-observability attacker
6. Clinical-boundary attacker
7. Complexity attacker

## Frozen evaluator panel

| Dimension | Pass requirement |
|---|---|
| Cognitive off-loading | Fewer repeated remembering, reconstruction, monitoring, and deciding operations |
| Generic productivity | Routine tasks and commitments remain reliable |
| Conversion | Protected work creates inspectable evidence |
| Continuity | Work resumes after interruption and attention gaps |
| Handoff durability | Ownership transfers without default rescue returning |
| Hub trust | Obsidian shows current, pending, stale, or unknown correctly |
| Partial-access honesty | Outputs declare what was and was not inspected |
| Clinical safety | No unreviewed or identifying clinical transfer |
| Simplicity | Component and maintenance burden remain bounded |
| Trajectory | At least one asset compounds beyond proportional operator attention |

## Ten baseline adversarial rounds

1. **Hub becomes a system-building hobby** — pass only if the hub remains within six stable surfaces and UI modification stays minimal.
2. **Capture and triage add labor** — pass only if capture is under 20 seconds and classification is deferred and batched.
3. **Hub increases awareness instead of reducing burden** — pass only if Today remains narrow and inactive work stays hidden.
4. **Agents cannot understand the file environment** — pass only if session packets and workspace maps allow accurate localization without global scanning.
5. **Work still dies outside attention** — pass only if a seven-day gap can be resumed within ten minutes.
6. **High-salience concerns bypass the system** — pass only if noncritical high-salience issues can be acknowledged, deferred, and safely returned.
7. **Generic productivity consumes conversion** — pass only if reliability and conversion are separately scored.
8. **Handoff remains nominal** — pass only if recurring ownership actually leaves the operator and successor action is observed.
9. **Self-reflection entrenches a fixed identity** — pass only if personal interpretations remain evidence-backed, revisable hypotheses.
10. **Operations improve but trajectory does not** — pass only if durable externalized value, reuse, publication, adoption, or autonomy increases.

## Current panel-first attack set

- **A — valuable work dies in chat**: ≥90% of consequential panels create valid exit packages; no accepted evidence remains only in chat.
- **B — Obsidian becomes stale**: no project displays `current` when a newer validated package is pending.
- **C — exit-package review becomes another inbox**: median review below three minutes and fewer than ten manual batch decisions per week.
- **D — panel proliferation increases fragmentation**: every panel has a type, stop condition, and one expected artifact; Explore does not auto-create a project.
- **E — partial folders create false completeness**: seeded missing-source cases do not produce unsupported complete-state claims.

## Mutation rules

A proposed change survives only if:

1. it addresses an observed or credibly simulated failure;
2. it reduces total cognitive operations;
3. it does not create another routine surface to monitor;
4. it has an objective pass/fail test;
5. it has a deletion condition;
6. it does not materially degrade another frozen evaluator.

## Epoch constraints

- at most three design mutations;
- at most three retries for a failed test;
- one human decision gate;
- no automatic change to strategic goals;
- baseline and new tests must both pass;
- criteria cannot be rewritten during the epoch.

## Current prototype acceptance thresholds

90% valid panel exit packages · zero accepted evidence existing only in conversation history · accurate pending and stale hub states · package review under three minutes on average · seven-day resume under ten minutes · no false completeness claim in seeded tests · no unapproved clinical transfer · weekly ACE maintenance under 5% · ordinary reliability not worse than baseline · at least one durable evidence unit shipped.

## Stop rule

Do not continue theoretical adversarial review after the first implementation epoch unless actual use creates a new failure or a frozen test fails. Further theory without use evidence is itself an ACE failure mode.

## Quantitative seed (optional, Q-D1b)

v0.1's `12_EVALUATION_SCORECARD` (100-point weighting) may attach as the measurement rubric under this panel for the 30-day checkpoint. It does not replace the panel.

## Relationship to the enhancement loops *(v1.1 addition)*

- **RQGM** (the public `rqgm-loop` repo, mature): runs the epochs. The panel above fills the EVALUATORS slot; DONE must be machine-verifiable; maker ≠ checker; gates G1–G5 apply.
- **Anomaly loop** (a sibling prototype, outside this repo): runs beside RQGM on an explore share, mining anomalies the frozen contract did not anticipate; certified findings feed the **next** epoch's attack cases, never the current epoch's contract. Maturity ruling: Q-D8.

---

### Change log

- **v1.1 (2026-07-19, rev 2)** — initial materialization used the docx's condensed table as "only known source"; superseded the same day when the full v1.0 package arrived on disk. Now carries the package's 07 in full (roles, panel, rounds, attacks, mutation rules incl. condition 6, epoch constraints, thresholds, stop rule); added the block-not-approve interim semantics, scorecard-seed note, and loop-relationship section.
