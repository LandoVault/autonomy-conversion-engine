# External review digest — "ACE research findings and design variants" (GTD/PARA report, r1.1)

**Status: `PROPOSED — output of a review panel, 2026-10-02. Not in force.`** Nothing here reopens a frozen decision except through door 1 (the operator's ruling) or door 2 (a Red-Queen epoch). The engine changes in §6 are uncommitted changes in worktree branch `claude/chrome-review-system-update-1208cf`; one of them amends rollback behaviour and is flagged for the operator. *(Public release: these changes are included in `engine/`.)*

**Input.** `F:\git\ACE\reference materials\ACE_Research_Findings_and_Design_Variants.md` (`reference materials/` is not included in the public release) — sha256 `49d8fc28…81f92573`, 437 lines, revision 1.1. Written by a model in an external ChatGPT conversation (the composer showed the model label "GPT-6 Astra", observed via Claude in Chrome 2026-10-02). Sources: public material plus two ACE design records it was given (the v1.0 design docx and a 2026-09-17 resume seed). The operator downloaded it and placed it in `reference materials/` 2026-10-02. It is untracked on `main` and byte-identical to the copy this panel captured. The report asks for a peer review in a fixed format (its §13). That review is `dev_log/rqgm/2026-10-02-ext-review/ACE_Peer_Review_Round_1.md` (`dev_log/` is not included in the public release; the same holds for the run-folder files cited below).

**Method.** RQGM run `dev_log/rqgm/2026-10-02-ext-review/`: `DONE.json` criteria D1–D9, `archive.jsonl`, `LOG.md`. The run uses the accept-first shape of the latest rqgm-loop design (§8): one strong pass, then acceptance of that exact version by separate evaluators, then repair of failed criteria only.

- Epoch 1: EV1 (fidelity, with a planted canary — caught), EV2 (burden and lineage), EV3 (reliability red team), and Fable 5.1 adjudicating design.
- Epoch 2: repairs.
- Sources re-verified against the live pages (§1).

---

## 0. Verdict

The report re-derives ACE v1.0's architecture independently, from public practitioner sources:

- **Shared pipeline:** panel → structured package → validation → human acceptance → durable state → resume packet.
- **Sync status:** kept separate from work status, with the same four labels as 04 §6.
- **Handoff machine:** a near-equivalent of ACE's machine 4.

That is **corroboration, not new architecture**.

Its sharpest sentence names the main risk of its own minimal variant: *"pending updates never reviewed"* (§5 table). For ACE this is not a hypothesis. It is the observed failure, now 73 days old (§2).

The report's useful new contribution is **executable failure checks** (§12.4):

- **F1 (replay) and F4 (crash after acceptance)** **failed** when run against the engine.
- **Its rule O3 (updates name their base state)** exposed a rollback lost-update.

All three are fixed in the worktree branch. The first fix attempt was itself broken by this run's red team, so the epoch-2 design is what stands (§6).

Its two product framings move ACE from one owner to a team. That is an objective-level change, filed as a wording-only question (R6-1).

**Net:** no new architecture. The binding constraint is still activation (R5-2). The report's value lands as acceptance tests for M2 plus one test that can run today (T4).

## 1. Evidence status of the report's sources (verification pass 2026-10-02)

All 15 ledger URLs were reachable. Verdicts on the claims checked:

**Verified on the live pages**

- **S10, Dropbox survey.** 504 US AI-using B2B professionals; fieldwork Jul 28–30; 74% move AI output between apps ≥3× per AI workday; 11% "finished work without further barriers"; published Sept 23. It is a sponsored self-report.
- **S6, PM Co-Pilot README.** Scheduled runs appear to run in the cloud and cannot reach local memory, so the author runs workflows locally. The README hedges ("seems to") and calls this temporary.
- **S2–S5, S8, S9 (content), S10, S12, S13, S15.**

**Partly verified**

- **S1.** The five stages are verified; the actionable-vs-reference split was not separately confirmed.
- **S7.** The mechanisms appear in the publisher's write-up, not on the episode page.
- **S14.** The 16:15 chapter is a *voice* guide; "decision guide" is not on the page.

**Unchecked**

- **S11.** The Tapesearch transcript excerpt.
- **S9.** The talk date.

No claim was contradicted. Raw table: run folder `source_verification.md`.

The report saw ACE's v1.0 docx and a Sept-17 resume seed only. It did not see spec v1.1/v1.2, the engine, the audit log, or Rounds 2–5. That explains why several of its "new" proposals are already ACE proposals (M2–M8, spec/14).

## 2. Observed ACE state, 2026-10-02

| Observation | Source (read 2026-10-02) |
|---|---|
| 14 audit events; last 2026-07-21 — **no transition in 73 days** | `ACE_storage/audit/events.jsonl` |
| `pending/X-CLARIFY20260721` (9 commitment proposals, no project changes) unreviewed 73 d; its engine hash (sha256 of the re-serialized JSON) equals the validated `735faba6…` | `ACE_storage/pending/`, audit line 14 |
| **Two real exit packages never validated**: Aug 22 (41 d) and Sep 17 (15 d) | `ACE_storage/outbox/` |
| Scheduled: `ACE_backup_daily` only (last run 2026-10-02, result 0) | Task Scheduler |
| `main` unchanged since 2026-08-22; Round 5 (R5-2..R5-6) unanswered 41 d | `git log`, spec/10 |
| 15/15 projects carry `sync: current`; the engine writes only `completeness_unknown` and `current` (ace_engine.py `apply_package`) | `ACE_storage/state/projects.json` |

Panels keep producing durable packages, so rule 3 is honoured. Nothing turns those packages into accepted state.

Even when the engine runs, `gen_views` lists only `pending/`. So an outbox package is invisible in the hub until something validates it.

spec/07's attack A ("valuable work dies in chat") has a sibling the contract does not name: **valuable work dies in the outbox.**

## 3. Compare / contrast matrix

**Status tokens:**

| Token | Meaning |
|---|---|
| IMPL | Implemented in `engine/` |
| SPEC | In-force spec, not running |
| PROP | Proposed in ACE (spec/14 M-ids; not in force) |
| GAP | Absent |
| CONFLICT | Disagrees with ACE's in-force design (a frozen rule or an approved spec) |
| OOS | Out of scope for this review |

Each row carries one primary token; nuance goes in the last column.

### 3.1 Scope and framings (report §11, §3)

| ID | Report claim | ACE counterpart | Status | Delta / verdict |
|---|---|---|---|---|
| R-01 | §11 "two accepted framing directions"; "the operator considers both perspectives useful". F1: "helps people move projects forward … making sure work gets finished" | 01_GOALS.md:5 (external executive system for the operator), :9–35 (P0-A/P0-B) | CONFLICT | The report records the operator's in-conversation reaction; it is not a ruling. ACE is single-principal; other people enter only through handoff (03:87–97) and waiting-for (04:37–59). The report itself suggests softening "making sure". Team scope is an objective change → R6-1 (wording only) |
| R-02 | F2: "AI carrying tasks forward and bringing people in when their judgment is needed" | CLAUDE.md (models propose, never apply); 03:194–202 (no continuous autonomous agent); 01:61 | CONFLICT | Read literally, it conflicts with "model proposes". It is compatible if "carrying" means deterministic loops. The report's own §11 caveat says human involvement is set by authority and risk |
| R-03 | One-liner: "coordinates human and AI contributions through accepted, resumable outcomes" | 02:5, 02:9–20 | SPEC | Accurate for the current design. Fable's sharper candidate is in §7 |
| R-04 | The defensible distinction is explicit transitions | 04 machines 1, 2, 4, 5 (04:7–155) | SPEC | Agree |
| R-05 | First slice: "finish a session with a reviewed result and a clear place to restart" | 03:204–206 | IMPL | Ran end-to-end 2026-07-19/20 (X-0001 accepted 07-19, X-0002 07-20). The restart half has never been timed (T4) |
| R-06 | GTD layer: commitments, next actions, waiting, return dates | 04:37–67; FR-3 03:41–50; `Commitments and Return` view (`gen_views`) | IMPL | Records and view exist. The return/aging loop (11:98) never runs — that is M2 |
| R-07 | PARA layer: supporting material by project/area/resource/archive | 02:180–196; 08 atlas | SPEC | Deliberately not PARA folders: stable IDs plus manifests |
| R-08 | Persistent-inquiry layer: 3–5 enduring questions linked to evidence, no obligation | 14:114 "latent questions [new field]" | PROP | No observed ACE case → fails the 3-cases rule (03:128). Filed F-4 |
| R-09 | "Folder location must not be the sole indicator of obligation status" (§3) | `state/projects.json`, commitment records (11 flows 1–3) | IMPL | Obligation state lives in records, not folders |
| R-43 | Human involvement is set by explicit authority and risk, not by agent uncertainty (§11) | 03:168–192 approval classes | SPEC | Identical in substance |

### 3.2 Findings A–G (report §4)

| ID | Report claim | ACE counterpart | Status | Delta / verdict |
|---|---|---|---|---|
| R-10 | A: the missing step is acceptance plus continuation | 04:7–35; ace_engine.py `validate`/`accept`; 07:57 attack A | IMPL | Strongest agreement. The mechanism exists but is **observed failing at activation** (§2) |
| R-11 | B: a context gap becomes a question only if it could change an action. S6: cloud-scheduled runs may not reach local memory | clarify_loop.py ("never guesses"); 13 rule 5; 14 §8 M8 | PROP | S6 is direct evidence for M2's design: the tick must run locally (Task Scheduler) |
| R-12 | C: promote a procedure after repeated reuse; owner, check, and retirement per skill | 14:157–159 M4; 14 §7 Q9 | PROP | Agree. S7 attribution tightened |
| R-13 | D: persistent questions as a home for exploration | see R-08 | PROP | — |
| R-14 | E: knowledge transfer has social costs | 03:87–97 FR-9 (handoff and knowledge-transfer design) | SPEC | Agree |
| R-15 | F: one record, several views | `finish_accept` writes hub note + resume packet from one package; `gen_views` from `state/` | IMPL | Already the design |
| R-16 | G: ask about purpose only when it changes commitment state | 02:210–211 rules 1–2; 13 rule 5; clarify_loop.py:32 | SPEC | The obvious-filing half is IMPL (deterministic marks; hedged items go to the idea queue); the clarify loop never asks a question — the one-line clarify exists only as 13 rule 5 |

### 3.3 Variants V1–V5 (report §5)

| ID | Variant | ACE counterpart | Status | Delta / verdict |
|---|---|---|---|---|
| R-17 | V1 minimal accepted-state workflow (first choice) | Phase-1 engine; 03 §7; 05 Phase 1 | IMPL | **V1 is what ACE built.** Its named risk is ACE's observed failure. So "begin with V1" becomes "activate V1" (R5-2) |
| R-18 | V2 review by change and exception; planted-case test | M2 (14:124–138), M6 (14:161–163), M8; FR-11 | PROP | Adopt the three planted cases into M2's acceptance tests (§5) |
| R-19 | V3 question-centred learning | R-08 | PROP | Filed |
| R-20 | V4 improvement from corrections, with fixed criteria and withheld examples | M4; rqgm-loop; `quality/edge_cases/EC-001`; 07:74–81 | PROP | Matches 07 ("criteria cannot be rewritten during the epoch") |
| R-21 | V5 reviewed expertise handoffs | 04:95–132; FR-9 | SPEC | No engine support. First real case is PROJECT-W (the canonical handoff-example project); its plan artifact was missing as of the 07-19 research (Q-H2), not re-checked |

### 3.4 Operational rules O1–O8 (report §6)

| ID | Rule | ACE counterpart | Status | Delta / verdict |
|---|---|---|---|---|
| R-22 | O1 reading ≠ inferring | CLAUDE.md panel rule 4 | SPEC | — |
| R-23 | O2 tool call ≠ accepted outcome | pending → accept gate | IMPL | — |
| R-24 | O3 updates name their base state; conflicts are reconciled | — | GAP | Accept-time protection is now the logged pre/post state hashes (recovery refuses on mismatch) and the rollback guard (§6). A `base_revision` field for concurrent panels fails the 3-cases rule → F-1 |
| R-25 | O4 repeated delivery must not create repeated work | replay gate (§6) | IMPL | New, uncommitted in the worktree branch. Content replay under a *new* X-id is not caught — [OPEN] |
| R-26 | O5 unavailable sources produce an explicit incomplete status | `check_scope`: empty `sources_not_seen` rejected | IMPL | — |
| R-27 | O6 scheduled work checks access and persistence before reasoning | 11:99 write-safety probe (META-2) | SPEC | Fold into M2 acceptance (§5 c) |
| R-28 | O7 policy and criteria never change as a side effect | 14 §5.7 classes A–D | PROP | — |
| R-29 | O8 a manual path and the last accepted version are preserved | NFR-4/NFR-5 (03:148–154); `rollback` | IMPL | — |

### 3.5 Limits, evaluation plan, adversarial table (report §2, §7, §8)

| ID | Report claim | ACE counterpart | Status | Delta / verdict |
|---|---|---|---|---|
| R-39 | §2 limits table (7 rows) and the list of deferrals (no plugin, vector DB, knowledge graph, migration, continuous runtime, global crawl, strategic re-prioritisation) | 03:118–132 (gated per R2-2); 03:194–202; 01:63–75 | SPEC | Limits identical; deferrals 5 of 7 in 03:196–200 (knowledge graph = 01:61; strategic re-prioritisation = 03:189 explicit-approval class and 07:79). The report calls the limits targets; ACE ruled them hard gates (spec/10:160) |
| R-30 | §7: baseline 5 → pilot 5; net time benefit including an explicit share of setup cost | 07:83–85; 07:74–81; 14 §5.10 | GAP | No baseline was ever run. Setup-cost amortisation is the one term ACE's <5% maintenance gate omits — filed as an Epoch-2 metric note |
| R-40 | §7 decision rule (keep only if it meets limits, reduces one burden, no reliability regression); accepted outcomes vs protected time tracked separately | 07:63–72 rules 2, 6; FR-11 dual scoreboards (P0-A/P0-B) | SPEC | Equivalent |
| R-31 | §8: the bottleneck may be capacity or authority, not software | 14:39 (interpretation of the stall) | PROP | **Agree, with evidence**: a decision queue (Round 5, 41 d) placed on a surface outside the daily working flow |
| R-32 | §8 failure table, 8 rows — mapped below | 07:44–61 | SPEC | 6 of 8 have a counterpart |

R-32 mapping, the report's eight rows against spec/07:

1. Automation creates obligations → attack D ("Explore does not auto-create a project").
2. The review queue becomes the bottleneck → attack C. **Now observed.**
3. Context gets stale → attack B / round 3.
4. Learned preferences overreach → **no direct counterpart.** Round 9 is about self-interpretation, not rules.
5. Learning becomes avoidance → **no direct counterpart.** Round 7 separates reliability from conversion, not inquiry from output.
6. File organisation becomes a hobby → round 1.
7. Team handoff is nominal → round 8.
8. A polished dashboard hides missing data → attack E.

Rows 4 and 5 are candidate attack cases for the next epoch's contract (filed).

### 3.6 State machines and fields (report §12)

| ID | Report claim | ACE counterpart | Status | Delta / verdict |
|---|---|---|---|---|
| R-33 | 12.1: one work lifecycle (Captured…Ready→Running(lease)→Proposed→Checking→AwaitingAcceptance→Accepted→Committed→Closed) | 04 machines 1–3 kept separate (04:7–93); →Closed at 04:23 | CONFLICT | The report keeps work, sync and ownership apart, but folds commitment, panel and project lifecycles into one machine; 04 (approved, Q-D2) keeps those separate. Matches: Accepted vs Committed = `Accepted → DurableStateUpdated` (04:34); Closed requires resume = `ResumePacketGenerated → Closed` (04:23, 04:35). The lease, Ready and Blocked states address multi-executor concurrency that has not been observed → F-2 |
| R-41 | 12.1 Reference and Deferred states; reopening preserves the old completion record | 04:37–67 (ScheduledReturn, `no_action_before`); idea queue 04:75, clarify_loop.py:32; supersede-by-move (11:111) | GAP | Deferred ≈ ScheduledReturn (SPEC) and reopen-preserves-record = supersede-by-move (SPEC); there is **no Reference state** |
| R-42 | 12.1 transition/guard table (actor, evidence, failure behaviour per transition) | 04 "Required transitions" (04:27–35); 04.yaml guards | SPEC | ACE encodes guards for its machines; there are no actor columns because there is a single principal |
| R-34 | Sync status is separate: current / pending review / known stale / completeness unknown | 04:157–170; 02:173–178 | SPEC | Same labels. The engine writes only `completeness_unknown` and `current`. `panel_update_awaiting_review` and `known_stale` are never written; only a Today banner shows pending items. This is a latent attack-B gap — not triggered today because the only pending package has no project changes. Moved to M2's acceptance tests (§5 e) |
| R-35 | No self-acceptance by the proposer; pre-authorised routine acceptance comes later | 03:168–192 | SPEC | Identical |
| R-36 | Cancellation from nonterminal states; late output is kept but not committed | 04:53–58 (commitments only) | GAP | No cancel exists for panels. Not observed → F-3 |
| R-37 | 12.2 ownership handoff | 04:95–115 (+ v1.1 decline fix 04:113, 04:132) | SPEC | **Near-equivalent.** ACE adds `OperatorRoleConfirmed`; its rescue path is `RescueReentry → OwnershipTransferred`, where the report uses `Reopened → Prepared`. The analogous rule "export alone is not completion" belongs to machine 5 (04:155) |
| R-38 | 12.3 field contract — 11 rows, 24 fields | exit-package schema; `state/projects.json`; session packet (02:132–145); audit | GAP | 13 of 24 implemented, 5 specified only, 6 absent (breakdown below) |

R-38 field breakdown:

| | Fields |
|---|---|
| **Implemented (13)** | work_id, goal (objective), work_state, sync_status, scope (visible roots, `check_scope`), artifact_links (`evidence_created`), evidence_links (`sources_seen`), missing_sources (`sources_not_seen`), blockers (`unresolved`), next_action, return_trigger (`no_action_before`/`return_date`), event_id, resume_note (resume packet) |
| **Specified only (5)** | allowed_actions (write boundary — prose in hand-written packets; no engine check), finish_condition (panel stop condition, not a field), handoff_status, receiving_owner (FR-9 recipient), receipt (`receipts/`) |
| **Absent (6)** | revision, base_revision, owner, executor, acceptor, budget |

Each absent field fails the 3-cases rule for a single-principal system.

### 3.7 Failure checks F1–F8 (report §12.4)

| ID | Check | Status | Executed result 2026-10-02 | Evidence |
|---|---|---|---|---|
| F1 | Replay → one accepted update | IMPL | **failed on the pre-session engine**; passes on the branch (4 assertions, incl. after supersede-by-move) | `tests/test_engine_replay.py`; `archive.jsonl` |
| F2 | Conflicting updates on one base | GAP | not executable (no base revision) | F-1 |
| F3 | Missing source → incomplete | IMPL | passes (package level) | `tests/test_engine.py` |
| F4 | Crash after acceptance → no false closure, no double write | IMPL | **failed on the pre-session engine**; the first fix failed EV3's attacks (lost update, crash mid-move); the epoch-2 design passes 3 crash points + mid-move + 2 interleavings | test_engine_replay.py |
| F5 | Cancelled run, late output | GAP | not executable | F-3 |
| F6 | Recipient silence keeps ownership | SPEC | handoff machine not in engine | — |
| F7 | Resume after gap ≤10 min | SPEC | never executed; a natural 74-day gap exists since the most recent real resume packet (`packets/RESUME_X-0002.md`, 2026-07-20; the planning packet `RESUME_X-0001.md` is 07-19) | **T4 — run now, no dependency** |
| F8 | Burden regression rejects a correct-but-heavy change | SPEC | gates in 01:105–117 | — |

Report §9 (listening guide) and §13–§14 (exchange protocol) are **OOS** for the matrix. They are handled in §1 and in the run log.

## 4. Where each side is stronger

**The report is stronger on four points:**

1. Failure checks written as executable tests. Two of them found real defects in an engine that had passed its own acceptance test.
2. Planted cases for exception review.
3. Explicit setup-cost accounting.
4. The "capacity or authority, not software" alternative, stated up front.

**ACE is stronger on five points:**

1. Privacy planes and a writer matrix.
2. A frozen evaluation contract with a mutation budget and a stop rule.
3. Usage evidence: the gesture registry and the stall record.
4. Separate machines where the report merges them.
5. The 3-cases rule, which correctly turns away the report's lease, base-revision and budget fields.

## 5. Proposed acceptance tests for M2 (tests, not scope)

R5-2 stays the one-word ruling it was (activate M2 as specified in spec/14). The items below are **builder-level acceptance tests of requirements already in force** — each row names the requirement it checks — so they need no ruling and add no scope; the operator may veto any of them.

| ID | Test | Licensing failure | Pass condition |
|---|---|---|---|
| M2-a | Replay and crash suite stays green (NFR-5) | F1/F4 failed on the real engine | `tests/test_engine_replay.py` passes on every build |
| M2-b | Three planted cases (due return, changed dependency, inaccessible source) | report V2; 07 attack E (in force) | each appears, or is marked `unknown`, within one tick |
| M2-c | Preflight before any transition: write/readback probe plus local-runtime check | S6; 11:99 write-safety probe (in force) | on probe failure the tick makes no transition and exits non-zero, so Task Scheduler records it |
| M2-d | Outbox handling (FR-6 03:60–62; 14:128 tick reads `outbox/`) | two packages invisible 41 d / 15 d | every outbox package is validated within one tick; failures are listed once in the Pending view with their errors and re-validated only when their bytes change (no audit line every 30 min) |
| M2-e | Sync flag (04 §6; 11:98 aging) | R-34 latent gap | validating a package that changes project P sets P to `panel_update_awaiting_review`; 14 days pending → `known_stale` plus one weekly line |
| M2-f | Single-writer lock around validate/accept/reject/rollback (11:61 audit is single-writer) | EV3 epoch-2 N3: two engine processes racing on one base silently lost an audited accept — likely once the tick runs beside hand gestures | two concurrent engine processes never both write; the second waits or refuses |
| T4 | Resume after the real 74-day gap | F7 never run | **run now, no ruling needed:** the operator opens `packets/RESUME_X-0002.md` (most recent; or the richer planning packet `RESUME_X-0001.md`) and records minutes to first correct action (≤10) |

**Filed** (spec/07 rule 1 not met — no observed failure):

| ID | Item | Path |
|---|---|---|
| F-1 | `base_revision` and reconciliation | — |
| F-2 | lease / Ready / Blocked states | — |
| F-3 | panel cancel and late-output quarantine | — |
| F-4 | persistent-question record | — |
| F-5 | owner/executor/acceptor split and team scope | door 1 only |
| F-6 | exact-version acceptance (K1) | §8 |
| F-7 | report §8 rows 4–5 as Epoch-2 attack cases | — |
| F-8 | setup-cost amortisation in the maintenance metric | — |

**Open defects (owner: the operator; none blocking — EV3 epoch 2, `eval_e2_EV3.md`)** — per EV2's dissent, none is built before an observed failure or R5-2:

- A package resubmitted under a new X-id with identical content is not caught (the clarify loop can produce this if a note move fails).
- Rollback is still write-behind: a crash inside `rollback` (state restored, event not yet written) leaves an unaudited reversal (pre-existing; fix = log first, like accept).
- Fail-closed wedge: if `state/` is hand-edited while an accept is in flight, every accept/reject/rollback refuses and no audited exit exists (needs a `resolve --restore-prev | --abandon` subcommand).
- Minor: a crash after `rmdir` makes the re-run print "not found" although the accept completed; recovery does not re-check the post-state hash after applying; event-id suffix is 16 bits; a torn audit line warns on every read; a refused gesture's reason is not shown in the hub.
- The dead-man's switch must live outside the tick, because a dead tick leaves a normal-looking stale view. The candidate is a check of heartbeat age from the audit log at the 14-day checkpoint, or the existing daily backup job. This needs design. It is not adopted.

## 6. Engine changes in the worktree branch (uncommitted) — for the operator's merge decision

| Defect | Found by | Fix (epoch 2) | Tests |
|---|---|---|---|
| Replay re-applied commitments that had no id, and overwrote the archived copy | report F1, executed | `check_replay` (filesystem + audit log); `unique_dir` never overwrites an archive folder | F1 ×4 |
| A crash mid-accept double-applied and recorded the wrong rollback inverse | report F4, executed | **write-ahead**: the `accepted` audit event carries `prev_state`, `prev/post_state_sha256` and `archive_dir`, with a deterministic ts, and is logged before the state write. A re-run finishes, applies, or refuses by comparing hashes. The package moves last. The first attempt (a journal file) lost updates — EV3 1e/4g — and was removed | 3 crash points, mid-move ×2 |
| A second accept or a rollback during an unfinished accept could overwrite state | EV3 1e/4g | `in_flight` guard on accept, reject and rollback | interleave ×4, external-change refusal ×1 |
| Rollback restored a snapshot over later accepts | report O3 | newest-first; undone accepts excluded; no double rollback. **This amends the Q-D10 / 11 flow-4 wording ("reverses to the prior snapshot") — the operator decides** | chain ×3 |
| One torn audit line would break every accept; event ids collided under tight loops | EV3 5b/4f | `read_events` skips and warns; `audit` starts on a fresh line; ids get a random suffix | ×2 |
| The clarify loop reused a rejected X-id (observed 2026-07-21, audit lines 12–14) | this panel | uses `eng.check_replay` | not separately tested — [OPEN] |
| `gesture_watcher` ignored refusals and committed "accept X" | EV2 | records `(refused)` and returns non-zero | — |
| `os.replace` hit a transient `PermissionError` (1 of 4 runs) | this panel, 2026-10-02 (`LOG.md` line 12) | bounded retry, ≤1.5 s; `.ace_tmp_` prefix on temp files | repeated runs |
| A pending package edited into a content excerpt passed straight to state and hub (pre-existing; reopened by withdrawing K1) | EV3 epoch-2 3b | `accept` re-runs the schema and content-class gates; refuses with the errors (compatible with "annotate pending") | ×1 |
| *Withdrawn:* exact-version acceptance (K1) | EV2, EV3 | conflicts with the writer matrix's "annotate pending" and stranded packages → filed F-6 | — |

**Interpretation for the operator.** The write-ahead keys added to the `accepted` audit event (`post_state_sha256`, `archive_dir`) are engine-internal audit metadata, written and read only by the engine; this panel reads the 3-cases rule (03:128) as covering fields a panel or the operator must author or maintain — which is also why `base_revision` stays rejected (panels would author it). EV2 accepted this reading.

**Compatibility.** The real pending package still matches its validated hash, and old accepted events stay valid. Pre-change audit events have no `post_state_sha256` field, but recovery only reads events written after the change.

**Discrimination.** Epoch 2 (`archive.jsonl` line 19, 2026-10-02): 11/11 + 19/19 on the branch, pre-session engine 3/19. EV3 re-ran it independently (`eval_e2_EV3.md`: D7 PASS; three mutants each kill exactly one of the 3 positive controls). Final (2026-10-02, after the sensitivity-gate test): 11/11 + 20/20 on three runs; the pre-session engine passes 3/20 on three runs. One extra pre-session run aborted on the same transient Windows `PermissionError` the retry fixes — a second independent sighting.

**Whitelist.** `clarify_loop.py` and `gesture_watcher.py` changed outside the run's declared whitelist. This is recorded as a deviation [OPEN: operator].

## 7. Round 6 — for the operator (flag · propose · wait)

- **R5-2 restated (73 d), the only blocking item.** One word activates M2 as specified. Merging this branch is a separate act and is safe on its own. The rollback amendment in §6 is part of that merge.
- **R6-1 (optional, wording only).** Default scope sentence (Fable):

  > *"ACE is a single-owner executive system that converts bounded human–AI work sessions into accepted, resumable state and durable evidence — models propose, deterministic code records, the owner approves — and brings other people in only through explicit handoffs."*

  The report's two framings stay on record as direction, not scope. Team scope is a later door-1 item with two preconditions: a privacy/permission model, and one observed case of a second principal needing state access.
- **Notes, not questions:**
  - The cross-vendor exchange follows the operator's in-chat instruction of 2026-10-02 (`.md` attachment in, `.md` out; quoted in `archive.jsonl`). It stops after the author's reply; another round only if the operator asks.
  - **Precondition (standing rule):** instance content goes to an external vendor only after that vendor's model-training setting is verified off; the check is logged in `archive.jsonl`. The review was then uploaded; the author's reply is **pending**.
  - Persistent questions: hold under the 3-cases rule.
  - `CLAUDE.md:56` still says the burden-limit gates are "PROPOSED". They were ruled in R2-2 (spec/10:160, 03:132) — align the contract text.

## 8. Latest rqgm-loop design → spec/07 (pointer)

Full digest: run folder `rqgm_v4_digest.md`, covering the public `rqgm-loop` repo, main line (loop v4.5) and the accept-first branch (v4.1). Both lines converge: one strong pass plus independent acceptance of that exact version did at least as well as a full loop on small tasks (Stage 4: 0 false completions in 23 valid cells; the loop arm used 44–56 calls against 6). The tasks were synthetic and used a single model family.

This run used that shape, with a matched canary for EV1. Candidates filed for an Epoch-2 contract:

- F-9 S-first admission;
- F-10 fail-closed tri-state scores;
- F-11 evaluator versioning;
- F-12 one canary per evaluator version;
- F-6 exact-version acceptance.

Not to import: EXPLORE/DERIVE machinery, the probe-bank lifecycle, relay drivers.

## 9. Preserved dissent

**EV2 (Opus, burden and lineage):**

> "Plainly: this exercise is a lineage-guard symptom (01:105-117). The last accepted ACE transition was 2026-07-21. … Accepted transitions in that time: zero. … The minimal honest output is three items: (1) the replay, journal, unique_dir and atomic-retry fixes plus their tests as one merge request, with K1 withdrawn; (2) a note to the operator of 10 lines or fewer … ; (3) if the operator wants to answer the author at all, a terminal reply that requests no response." (`eval_e1_EV2.md` lines 43–45, elided)

Epoch 2 (`eval_e2_EV2.md` line 44): "from here on, further reliability work on a dormant engine is building instead of activating, and needs an observed failure first. … The next acceptance should be of use, not documents: did T4 run, and did R5-2 get its one word?"

This panel accepts it: Round 6 is one optional line, §8 is a pointer, internal epochs stop at 2, and the next acceptance is about use. It departs from EV2 on one point only: the author round requests one bounded reply, because the operator asked for `.md` output.

## 10. Partial-observability statement (CLAUDE.md panel rule 5)

- **Inspected:**
  - The input report, in full.
  - spec 00–14: 01, 02, 03, 04 and 07 in full; 14 §0–§10; Rounds 2–5 of 10; the layouts, writer matrix and flows of 11.
  - `engine/*.py`, `tests/`, the exit-package schema.
  - `ACE_storage` (read only): audit, pending, outbox, archive listings, `state/projects.json` counts, git log.
  - `F:\ACE_hub` git log and Task Scheduler.
  - The 15 public sources (verification subagent) and the public `rqgm-loop` repo (RO-REF, digest subagent).
- **Channels:** the ChatGPT thread that produced the input, read via Claude in Chrome. The downloaded `.md` is the source of record.
- **Date range:** ACE records 2026-07-19 → 2026-10-02; sources Apr–Oct 2026.
- **Not inspected:** `F:\ACE_local` contents; the two outbox packages beyond their headers; the Sept-17 resume seed; the rendered Obsidian views.
- **Confidence in completeness:** high for the spec + engine comparison; medium for the report's reading of the resume seed (not opened).

---

### Change log

- **v0.1 (2026-10-02, epoch 0)** — created by the external-review panel.
- **v0.2 (2026-10-02, epoch 2)** — repaired against EV1 (14 failed rows, canary caught), EV2 (governance/burden), EV3 (engine) and Fable's adjudication. Status tokens normalised; coverage rows R-09, R-39–R-43 added; R-32 mapped row by row; R-34 corrected to two of four sync labels written; R-37/R-38 recounted; credit to the report limited to F1/F4/O3; K1 withdrawn; engine redesigned to write-ahead; Round 6 collapsed to R5-2 plus one optional wording line; §8 cut to a pointer; EV2's dissent preserved. Fable's Q-D3 correction rejected with evidence (spec/10:160).
- **v0.3 (2026-10-02, epoch-2 residuals)** — EV1 re-check (cites :160, R-16/R-41 tokens, R-38 13/5/6, R-43 id, R-39 6-of-7, verbatim dissent, D6 sources, branch wording) and EV2 re-check (M2-a..e as builder-level tests of in-force requirements, exchange ends after the author's reply, audit-key interpretation, F-9..F-12 ids, T4 → RESUME_X-0002); vendor training setting checked before upload.
- **v0.4 (2026-10-02, close)** — EV1 final residuals (R-39 5-of-7, verbatim epoch-2 quote, R-25 wording, precondition observation sourced; D6 PASS); EV3 epoch-2 D7 PASS folded in (sensitivity gate at accept, M2-f lock test, open-defect list). Internal epochs closed at 2 (Fable Q5; spec/07 stop rule).
