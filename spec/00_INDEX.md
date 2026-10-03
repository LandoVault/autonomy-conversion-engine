# ACE Spec Index

**Generation: v1.1 (2026-07-19).** `spec/` is the canonical living spec. `reference materials/` (not included in the public release) is frozen provenance — v0.1 zip, v1.0 loose set + docx, and `ACE_Final_Design_Package_v1_0/` (the full v1.0 export: schemas, templates, 07_RED_QUEEN_VALIDATION, 08_IMPLEMENTATION_ROADMAP; arrived on disk 2026-07-19), plus the two meta-loop documents drafted by a peer agent (`AACE_Epistemic_Operating_Substrate_Handoff.md`, `AACE_State_Machine_and_Orchestration_Spec.md`, added 2026-08-22 — "AACE" is a naming slip for ACE; digested in spec/14, re-issued as v0.2 in spec/meta/) — never edited, never deleted.

## Read order (agents)

1. `/CLAUDE.md` — operating contract (supersedes `reference materials/codex.md`)
2. `spec/01_GOALS.md`
3. `spec/02_FINAL_DESIGN.md`
4. `spec/03_PRODUCT_SPEC.md`
5. `spec/04_STATE_MACHINES.md` (+ `.yaml` machine projection)
6. `spec/05_PLAN.md`
7. `spec/07_RED_QUEEN_VALIDATION.md`
8. `spec/08_WORKSPACE_ATLAS.md` — before touching any filesystem root
9. `spec/09_STATE.md` — current state; update it when you change anything
10. `spec/10_OPEN_QUESTIONS.md` — what is undecided; never silently decide these
11. `spec/11_STORAGE_AND_FILING.md` — before writing anything to ACE_storage or `F:\ACE_local`

`spec/06_INTERVIEW_RECORD.md` loads **only** for strategic review, behavioral assumptions, system design, or portfolio decisions — never into ordinary work sessions. *(Public release: 06 is a prompt template only; the operator's answers are not included.)*

## Registry

| Doc | Status | Supersedes (`ref/` = `reference materials/`, not included in the public release) |
|---|---|---|
| 01_GOALS | v1.1 carried + lineage guard | ref/01_GOALS.md |
| 02_FINAL_DESIGN | v1.1 carried + coexistence, rule 9 (PROPOSED) | ref/02_FINAL_DESIGN.md |
| 03_PRODUCT_SPEC | v1.1 carried + limits table, PA-1..3 (PROPOSED) | ref/03_PRODUCT_SPEC.md |
| 04_STATE_MACHINES .md/.yaml | v1.1 carried + 3 bug fixes (PROPOSED, Q-D2) | ref/04_* |
| 05_PLAN | v1.1 new (subsumes handoff) | ref/05_HANDOFF.md |
| 06_INTERVIEW_RECORD | v1.1 carried + docx-only restorations (public release: prompt template only) | ref/06_INTERVIEW_RECORD.md |
| 07_RED_QUEEN_VALIDATION | v1.1 — carried in full from the v1.0 package, PROPOSED pending freeze (Q-D1); blocks but cannot approve until ruled | ref/ACE_Final_Design_Package_v1_0/.../07 |
| 08_WORKSPACE_ATLAS | v1.2 — ACE_local root, standing rules, name/identifier hygiene (public release: illustrative roots) | — |
| 09_STATE | living | — |
| 10_OPEN_QUESTIONS | living — Round 1 ruled (see Rulings record), **Round 2 open** | — |
| 11_STORAGE_AND_FILING | v1.2 — two-plane design per the operator's Round-1 ruling | — |
| /CLAUDE.md | v1.2 operating contract (no-delete, two-plane, identifier gate) | ref/codex.md |
| /AGENTS.md | vendor-neutral pointer to CLAUDE.md (Codex/GPT) | — |
| 12_GESTURE_DESIGN | PROPOSED — PA-4 three-mode interaction design v1.2 (R4-1) | — |
| 13_GESTURE_REGISTRY | PROPOSED — evidence-derived unified gesture grammar (R4-2) | — |
| 14_META_LOOP_AND_LAYERS | PROPOSED — digest of the peer-agent meta-loop documents (2026-08-22; "AACE" = naming slip for ACE, ruled same day); meta-loop as scheduler; mutation candidates M2–M8; Epoch-2 candidate (R5) | ref/AACE_*.md (v0.1, frozen) |
| 14_LITERATURE_ANNEX_2026-08 | reference — verified 2025–26 citations behind spec/14 §7–§8 | — |
| 15_EXTERNAL_REVIEW_DIGEST_2026-10 | PROPOSED — digest of the external GTD/PARA research report (ChatGPT, r1.1, 2026-10-02): compare matrix vs spec + engine, executed failure checks F1/F4, proposed M2 acceptance tests, engine fixes on a review branch, Round 6; RQGM run `dev_log/rqgm/2026-10-02-ext-review/` (not included in the public release) | — (input: `reference materials/ACE_Research_Findings_and_Design_Variants.md`, sha `49d8fc28…`) |
| meta/ACE_Epistemic_Operating_Substrate_Handoff_v0.2 | exported 2026-08-22 — meta-loop handoff v0.2 (name corrected to ACE) (I13 automated activation, I14 deterministic authority, classes A–D channel table, §16 round 1 answered / round 2 open) | ref/AACE_Epistemic_Operating_Substrate_Handoff.md (v0.1, frozen) |
| meta/ACE_State_Machine_and_Orchestration_Spec_v0.2 | exported 2026-08-22 — deterministic tick runtime (name corrected to ACE), heartbeat, depth table, socket field set, trigger thresholds | ref/AACE_State_Machine_and_Orchestration_Spec.md (v0.1, frozen) |

## Amendment mechanism

The architecture remains `frozen_for_first_vertical_slice`. Exactly two doors reopen a frozen decision:

1. **The operator's explicit ruling**, recorded as an answer in `10_OPEN_QUESTIONS.md` plus a change-log entry in the affected doc;
2. **A Red-Queen epoch** (`07`) whose mutation passes Pareto + human approval.

Everything tagged `PROPOSED` is *not in force* until door 1 approves it. The 2026-07-19 research package serves as the Phase-A evidence that v0.1 required and v1.0 skipped; that inversion is documented, not hidden (Q-D9).

## Provenance chain

v0.1 research package (zip, 2026-07-19) → v1.0 consolidated set (same day) → v1.0 full export package (`ACE_Final_Design_Package_v1_0/`, arrived later the same day — restored 07, 08_IMPLEMENTATION_ROADMAP, 3 schemas, 4 templates) → **v1.1 surgical grounding (this generation)** — carried except changes listed in each doc's change log.

Recovered v0.1→v1.0 drops: WIP limits (as PA-1), sanitization criteria (as PA-3), burden-limit consolidation. Surfaced from docx/package into canonical markdown: RQ contract (07), per-hypothesis test implications, "dual scoreboards" (also in the package's 08 roadmap Phase 3).
