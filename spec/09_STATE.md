# ACE Project State

**As of: 2026-10-02** · Status: `phase_1_engine_live — DORMANT since 2026-07-21 (73 d; no scheduled loop; 9 proposals pending 73 d; 2 exit packages never validated) — external GTD/PARA report digested as spec/15; engine replay/crash fixes uncommitted in review branch; Round 6 issued` *(public release: these engine changes are included in `engine/`)*
This is the living state document — every consequential session updates it (keep ≤60 lines of current state; move history to the log).

## Current state

- Repos `ACE` + `ACE_storage` created; v1.1 corpus committed and pushed this session.
- Spec corpus landed in `reference materials/` (not included in the public release) — v0.1 zip, v1.0 set + docx, and the full `ACE_Final_Design_Package_v1_0/` export (schemas, templates, RQ contract, roadmap; arrived 2026-07-19) — preserved untouched as provenance.
- Workspace research (7 parallel mappers + completeness critic) complete; findings grounded into spec v1.1; doc set adversarially verified (4 lenses, 43 findings triaged and applied).
- Spec v1.1 written to `spec/` (01–09 + atlas + storage design); `07_RED_QUEEN_VALIDATION.md` materialized (PROPOSED).
- Storage skeleton designed and scaffolded in `ACE_storage` (hub location marked provisional pending Q-B1).
- Blindspot pass run; Round 1 issued and **largely answered** — rulings in `10_OPEN_QUESTIONS.md` §Rulings record.
- **Two-plane storage built per the operator's ruling**: `F:\ACE_local` content plane created (local git, no remote, initial commit); `ACE_storage` recast as control plane (+ `quality/`, `local_manifests/`); spec 11 → v1.2. Obsidian confirmed as control/review hub; work runs in Cowork panels.
- **Engine live 2026-07-19/21** (validator, accept/reject, rollback, views, clarify loop, gesture watcher, manifest loop); planning panel X-0001 accepted; gesture self-test passed; EC-001 mark migration.
- **Dormant 2026-07-21 → 2026-08-22** (observed this session): zero audit events, no hub edits, `pending/X-CLARIFY20260721` (9 proposals) unreviewed 32 d, aging rule not executing, gesture watcher never activated (awaits R4-1), only `ACE_backup_daily` scheduled. Evidence: spec/14 §2.
- **2026-08-22**: two meta-loop/layers documents (peer agent; "AACE" = naming slip for ACE, ruled same day) added to `reference materials/`; digested in `spec/14_META_LOOP_AND_LAYERS.md` (PROPOSED) with literature annex; mutation candidates M2–M8; **Round 5 issued** (R5-2 `ace tick` unblocks the stall).
- **2026-08-22 (export)**: both documents re-issued as **ACE v0.2** in `spec/meta/` (handoff + state machine; dated, change-logged, name corrected; v0.1 originals stay frozen in `reference materials/`).
- **2026-10-02 (deploy)**: local-storage deployment packet added (`deploy/`: README, agent packet, bootstrap + verify + backup-task scripts; engine/loops/backup read `ACE_STORE`/`ACE_LOCAL`/`ACE_HUB`, defaults unchanged); `verify_deploy.py` on this machine: DEPLOY OK (13 checks). External round paused (vendor usage limit) — resume via `dev_log/rqgm/2026-10-02-ext-review/RESUME_EXTERNAL_ROUND.md` (not included in the public release).
- **2026-10-02**: external research report (from a ChatGPT conversation, r1.1; the operator placed it in `reference materials/`) digested in `spec/15` (PROPOSED) via RQGM run `dev_log/rqgm/2026-10-02-ext-review/` (2 epochs, accept-first; EV1 canary caught). Verdict: corroborates v1.0, no new architecture; its F1/F4 checks **failed on the engine** → write-ahead accept, replay gate, rollback guard, torn-log tolerance (a review branch, uncommitted at the time — included in this release's `engine/`; 11/11 + 19/19 tests; pre-change engine fails 16/19). Observed: outbox holds 2 never-validated packages (Aug 22, Sep 17). Peer review Round 1 uploaded to the author thread (per the standing vendor-training precondition for instance content, 10 §Round 6); the author's reply is pending.

## Pending decisions (blocking)

`10_OPEN_QUESTIONS.md` §ROUND 6: **R5-2 restated — still the only blocking item (73 d)**; merge of the review branch (incl. rollback newest-first amendment) is a separate safe act; R6-1 optional wording. Still open: R5-3..R5-6, Round 3 (R3-1..R3-5), Round 4 (R4-1, R4-2 — subsumed by R5-2/R5-3 if approved).

## Exact next action

Operator: (1) say "activate" (R5-2) and merge the review branch; (2) no-ruling option today — T4: open `ACE_storage/packets/RESUME_X-0002.md`, time to first correct action; (3) retry the author reply in the thread and drop `ACE_Author_Response_Round_1.md` into `reference materials/` for digestion. Builder after R5-2: as below, plus spec/15 §5 M2-a..e builder-level acceptance tests (the operator may veto).

*(2026-08-22, still valid)* The operator answers R5-2 (one word). Then: build `engine/tick.py` (composes gesture_watcher + clarify_loop + validator + aging + returns + views, idempotent, <10 s), register it in Task Scheduler (30 min + 07:00), run it once against the 32-day-old pending item (expect `known_stale` degrade + one Weekly line), and write the M2 pass/fail test into `tests/`. Decision records (M3) follow only after R5-3.

*(superseded 2026-08-22)* Build the engine core (validator, packet/manifest/view generators, backup schedule), then run the planning `produce` panel against `ACE_storage/packets/P-0001_planning.md` — it also collects the deadline inventory and seeds the portfolio triage checklist (promised next session). Operator: enable Obsidian Sync on F:\ACE_hub when convenient (R3-5).

*(superseded)* The operator answers R2-1/R2-2 (a one-line "approve all + planning pilot" suffices) → Phase-1 vertical slice build begins per `05_PLAN.md`, targeting the operator's planning session as the first real `produce` panel.

## Loops running

`ACE_backup_daily` (Task Scheduler, 18:00) only. Engine loops (validator, clarify, gesture watcher, manifest, views) exist but are hand-run — none scheduled (the §2 stall in spec/14). Legacy scheduled skills: out of scope per R2-5.

## Known-Unknowns (blindspot pass v2.1, 2026-07-19)

Nine ranked unknowns (filed across Q-B1, Q-C3, Q-C4, Q-D10, Q-D11, Q-F3, Q-G3, L1 — tagged `[BSP]`) + 12 one-pass confirmables (L1–L12) in `10_OPEN_QUESTIONS.md`. Highest-impact: hub-tool evidence gap (Obsidian chosen without usage evidence), post-acceptance rollback semantics, single-approver backpressure (analog:alarm-management), clinical-metadata confidentiality on the control plane, panels-write-state convention vs target architecture (Q-C4). Sourced pitfalls imported: FMEA-001 (state-sync gate), META-2 (stale mount — atomic writes + probes for all loops), META-1 (push gate), score-inflation (maker≠checker). Institutional AI-tooling policy reference: NONE-FOUND.

## Top risks (full register in research + 08 atlas)

1. Lineage risk: 5th predecessor meta-system; maintenance-step mortality (01 §Lineage guard).
2. Two live meta-systems in contention (another meta-system + scheduled skills) — state-forking risk.
3. Staleness-signal pollution (08 §Signal pollution) — naive loops will misfire.
4. Privacy: name-only filters leak on mixed-content legacy notes if ingested blindly.
5. Data drive nearly full; spec corpus was a single point of loss until this session's commit+push of both repos (backup posture still unverified — L9).

## Session log

| Date | Session | Outcome |
|---|---|---|
| 2026-07-19 | Repo creation | ACE + ACE_storage repos initialized and pushed |
| 2026-07-19 | Research + surgical map | 7-mapper survey + critic; spec v1.1; atlas; storage design; blindspot pass; verification (43 findings fixed); Round-1 questions issued |
| 2026-07-19 | Engine build + acceptance test | Phase-1 engine core built (validator w/ content-class+scope+FMEA-001 gates, accept/reject, audited rollback, view generator); full lifecycle acceptance test PASSED incl. rollback + 8-error rejection; empty-dir bug found+fixed; daily backup task registered (18:00) |
| 2026-07-19 | Round-1 rulings + two-plane storage | Rulings recorded; `F:\ACE_local` created; ACE_storage → control plane (quality/, local_manifests/); spec 11 v1.2; no-delete standing rule; Round 2 issued |
| 2026-07-20/21 | Gesture design + engine loops | PA-4 three-mode design (12), gesture registry (13), gesture watcher + clarify loop + manifest loop built and self-tested; EC-001 mark migration (`>>` → `@date`) |
| 2026-08-22 | Meta-loop docs digest (explore panel) | Two peer-agent meta-loop docs ("AACE" = ACE) digested → spec/14 (concept map, tensions, meta-loop-as-scheduler rethink, M2–M8, §16 answers) + literature annex (verified 2025–26 sweep); stall observed and documented; Round 5 issued |
| 2026-10-02 | External report review (review panel, RQGM 2 epochs) | ChatGPT GTD/PARA report read via Claude in Chrome; digested → spec/15; F1/F4 executed → 3 engine defects fixed (review branch), first fix broken by red team and redesigned; Fable adjudication; Round 6; peer review Round 1 to the author thread |
