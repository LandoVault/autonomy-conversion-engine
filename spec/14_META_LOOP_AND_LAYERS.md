# Meta-loop and layers — digest of the peer-agent meta-loop documents (v0.1) and the Epoch-2 candidate

**Status: `PROPOSED (Round 5) — output of an explore panel, 2026-08-22. Not in force. Nothing here reopens a frozen decision except through door 1 (the operator's ruling) or door 2 (a Red-Queen epoch).`**

**Naming (ruled 2026-08-22, operator):** "AACE" in the two documents was a naming slip by the peer agent that drafted them — *they describe ACE itself; there is no separate substrate.* In this file **MLD** ("the meta-loop documents") names those two v0.1 documents wherever they are contrasted with the existing spec and engine.

Inputs digested (`reference materials/` is not included in the public release): `reference materials/AACE_Epistemic_Operating_Substrate_Handoff.md` (sha256 `028741cd…583d6`) and `reference materials/AACE_State_Machine_and_Orchestration_Spec.md` (sha256 `b5afc781…67ea4`), both added to the repo 2026-08-22 (provenance: "working specification for multi-agent review and co-evolution"; authored by a peer agent; name was a slip — R5-7 ruled). Companion: `spec/14_LITERATURE_ANNEX_2026-08.md` (verified citations behind §7–§8). **Exports:** both documents re-issued as **ACE** v0.2 (2026-08-22) with this digest folded in — `spec/meta/ACE_Epistemic_Operating_Substrate_Handoff_v0.2.md`, `spec/meta/ACE_State_Machine_and_Orchestration_Spec_v0.2.md`.

---

## 0. Verdict in one paragraph

The two documents are ACE's own meta-layer specification — the right *next layer* for the existing spec and engine, not a replacement for them. They name, in general form, the thing the ACE build ran into in practice: **a system whose memory is correct but whose activation is manual goes dormant** (I11 "activation over storage"; §2.2 attention as the scarce resource). The observed record supports this exactly — the engine went live 2026-07-19, one real planning panel ran, and from 2026-07-21 to today nothing has moved (§2). The correct way to build on the documents is therefore not to maintain two vocabularies but to (a) treat the meta-loop as the **layer that schedules the existing object-level machines**, (b) admit only the constructs that answer an *observed* failure now — activation, decision records, trigger learning, review-depth routing — under the frozen Red-Queen mutation rules, and (c) file the rest (representation/objective mutation, cross-project reuse extraction, monthly meta-review, the metric set) as the **Epoch-2 contract candidate**, with PROJECT-V (a research project) as the second validation project. The 2025–26 literature (§7–§8) is strongest precisely on the constructs ACE needs first (when-to-ask policies, agentic memory with provenance, workflow-search governance) and weakest on the ones the documents are most ambitious about (detecting genuine representation change; measuring oversight burden) — which is where ACE's own evidence base (gesture registry, lineage guard, hard gates) is ahead of the field.

---

## 1. What the two documents say (compressed, faithful)

**Handoff (18 sections).** ACE as a general human–agent orchestration substrate for many projects and many model families, optimizing *marginal human cognitive cost per unit of useful intellectual complexity* (North Star §18, Cognitive Scaling Ratio §14). Core thesis: **decision events**, not tasks, are the coordination primitive (§2.1); attention is the scarce resource (§2.2); review must recover implicit human judgment, not only verify execution (§2.3). Twelve invariants I1–I12 (cognitive sustainability; representation evolution with the three-way split *parametric optimization / representation search / objective evolution*; decision traceability; incremental delta updates; adaptive review depth; multi-resolution coherence; reasoning portability; validation before generalization; asymmetric attention; reusable-abstraction emergence; activation over storage; optimization-vs-conceptual-change separation). Five layers: knowledge / decision / attention / execution / autonomy-policy (§4). Eight review dimensions (§5), four nested cadences (§6), typed **open debt** (§7), five human projections — attention, decision, landscape, trajectory, representation (§8), role-based **agent sockets** (§9), the meta-loop (§10), **cognitive-event capture** from interaction signals (§11), four **self-evolution classes A–D** with escalating verification (§12), PROJECT-V as first validator with a no-project-specific-primitive rule (§13), eight candidate metrics (§14), non-goals (§15), ten questions for reference agents (§16), a replay-based validation plan (§17).

**State-machine spec (30 sections).** Event-driven state graph (§1) over a canonical state object with scope/knowledge/decisions/attention/representation/execution/debt/policy/provenance (§2); human/agent/system event taxonomy (§3); cognitive-event detector that "should not infer psychological state" (§4); states S0 WAIT → S1 OBSERVE → S2 INTERPRET → S3 DETECT_TENSION → S4 PRIORITIZE (utility function) → S5 SELECT_DEPTH (D0–D5) → S6 DELEGATE (socket) → S7 EXECUTE → S8 VERIFY → S9 FAILURE_ANALYSIS (eight failure classes; *repeated failure inside the same framing raises the probability of a representation problem*) → S10 INTEGRATE (transition record) → S11 REPRESENTATION_CHECK → S12 REPRESENTATION_REVIEW (compare current / minimally-modified / genuinely-alternative framing) → S13 OBJECTIVE_REVIEW (rare, human-approved) → S14 ATTENTION_UPDATE (attention packet: now / automatic / latent) → S15 POLICY_UPDATE → S16 META_REVIEW; stopping policy (§17); recurring-review template (§18); DepthScore heuristic (§20); trigger-learning lifecycle *observe → candidate → shadow → compare → promote → monitor → decay* (§21); cross-project reuse ladder (§22); structured disagreement with distinct questions per reviewer (§23); four-phase MVI (§25); PROJECT-V replay protocol (§26); twelve failure modes to test (§27); invariant check with `NEW_INVARIANT_CANDIDATE` (§28).

**What the documents do not contain** (and ACE does): privacy/clinical boundaries; storage planes and a writer matrix; a frozen evaluation contract with mutation budgets; hard cognitive-burden gates with deletion conditions; a human-side gesture grammar; the deterministic/model/human authority split; any usage evidence.

---

## 2. The stall — observed evidence (partial-observability statement in §11)

| Observation | Source |
|---|---|
| Audit log: 14 events, first 2026-07-19, last **2026-07-21**; nothing since | `ACE_storage/audit/events.jsonl` |
| Last control-plane commit 2026-07-21; last hub commit 2026-07-21 ("Capture marks: @date canonical") | `git log` ACE_storage, F:\ACE_hub |
| Newest hub file mtime 2026-07-21; no human edit to any view or note after | `ls -lt F:\ACE_hub` |
| `pending/X-CLARIFY20260721` — 9 capture proposals "staged for tick" — untouched **32 days**; spec 11 §Flow-5 prescribes 7/14-day aging → `known_stale`, but no loop executes it | `ACE_storage/pending/`, spec 11 |
| Commitments C0001–C00xx from the planning panel carry return dates 2026-07-20..24; all still `clarified`; no return loop exists, so nothing re-annunciated | `ACE_storage/state/projects.json` |
| Only scheduled ACE task: `ACE_backup_daily` (18:00, last run today, result 0). No clarify / gesture / aging / return / brief loop is scheduled | Task Scheduler |
| Gesture watcher docstring: "Activation as the standing loop awaits R4-1 confirmation." R4-1, R4-2 and R3-1..R3-5 are unanswered | `engine/gesture_watcher.py`, spec 10 |

**Interpretation (inferred).** Nothing in the engine failed. The system stopped at the step where the design required a human act to *start the loops* and a human ruling to *permit the activation* — and the decision queue that would have released both sat in a document (spec 10) that is not an in-flow surface. This is the lineage-guard failure mode (01) — a queue on a non-activated surface stalls — repeating at the earliest possible point, and it is the concrete instance of three MLD claims: I11 (a skill that is never triggered is functionally absent), §2.2 (the blocking resource was attention, not capability), and the stopping policy's warning against treating activity as progress — except here the absence of activity was not even visible to anyone. The build's own backpressure rule (aging) could not fire because it lived in the same unactivated engine. **Every proposal in §5 is ranked by whether it removes a manual activation step.**

---

## 3. Concept map — MLD construct → closest ACE counterpart

Status key: **impl** = code exists in `engine/`; **spec** = in force in `spec/`; **prop** = PROPOSED; **partial**; **absent**.

| MLD construct | Existing spec/engine counterpart (evidence) | Status |
|---|---|---|
| Decision Event as primitive (§2.1) | No record type. Decision-shaped things exist: `decision lock` / `unresolved decision` fields in resume packets (FR-7); the rulings table in spec 10 (R-rounds = decision events with alternatives, recommendation, verdict); change-log entries | **partial** |
| Knowledge layer — claims / hypotheses / evidence / contradictions (§4.1) | Evidence records FR-8 (impl: `evidence_created` pointers); interview hypotheses H1–H5 as revisable beliefs (06); no claim/contradiction record | **partial** |
| Decision layer (§4.2) | spec 10 for the *system's* decisions only; none for project decisions | **partial** |
| Attention layer (§4.3); attention packet now/automatic/latent (S14) | Today view (FR-2: ≤3 obligations + due returns + 1 protected + 1 evidence); Pending view with ⚠ banner; backpressure aging 7/14 d (11 §Flow-5); `no_action_before` re-annunciation | **impl** (views) / **spec** (aging, not running) |
| Execution layer + agent sockets (§4.4, §9, spec §6) | Session packet (input contract) + exit-package schema (output contract) + validator gates: schema, content-class, source-scope, FMEA-001 sync; panel types with stop conditions (02) | **impl** — *more concrete than MLD* |
| Autonomy/policy layer (§4.5) | Approval classes auto / batch / explicit (03 §5); deterministic-vs-model-vs-human split (CLAUDE.md); gesture grammar (13) | **spec** |
| Meta-loop S0–S16 (§10, spec §5) | No scheduler. Object-level machines 1–7 exist (04); loops are hand-invoked subcommands | **absent** (the gap) |
| Cognitive-event capture (§11, spec §4) | spec 13 epistemic channel: hedge lexicon → non-binding; repetition-with-compression → escalation dial; honest-probe → adversarial routing; `HEDGES` regex in `clarify_loop.py` | **impl/prop** — *evidence-derived (122 sessions), narrower and safer than MLD's list* |
| Trigger learning with shadow mode (spec §21) | None. ACE validates human-proposed triggers (M1's 14-day test) but never learns them; its own loops (clarify, gesture watcher, manifest) and skills (rqgm, disagree, blindspot, session-close) are hand-invoked — the dormancy problem in ACE's own inventory. (The four legacy scheduled skills were ruled out of scope: R2-5, Q-C2 closed) | **absent** |
| Adaptive review depth D0–D5, DepthScore (S5, §20) | Human-review depth = approval classes; agent-output verification = validator only; adversarial = RQGM epochs (07); disagree/blindspot/understanding-check skills exist but are hand-invoked | **partial** |
| Structured disagreement (spec §23) | RQGM (maker≠checker, roles), a multi-model orchestration conflict ladder, a disagree skill, blind audit agent | **spec/tooling** |
| Failure analysis with representation-vs-parametric distinction (S9) | FMEA log + edge cases (`quality/`); EC-001 is a representation-level fix (mark grammar vs host grammar) recorded as an edge case | **partial** |
| INTEGRATE transition record (S10) | Audit event with `prev_state` snapshot + sha256, audited-inverse rollback, attributed commits (PA-2) | **impl** — *stronger (reversible)* |
| Representation check / review (S11–S12) | The anomaly loop (a sibling prototype): mines anomalies the frozen contract did not anticipate → next epoch's attack cases (07 §loops) | **spec** (Q-D8 unruled) |
| Objective review (S13) | Amendment door 1 only (the operator's ruling); "no automatic change to strategic goals" (07 epoch constraints) | **spec** — *correctly human-only* |
| Policy update (S15) | None automated; Red-Queen mutation ≤3/epoch with pass/fail + deletion condition | **spec** |
| Meta-review (S16), cadences (§6) | Weekly review FR-11 (<20 min, ≤5 decisions, one simplification); RQ epoch = architecture review; no monthly/bimonthly | **partial** |
| Open debt, typed (§7) | Pending aging; at-risk project 21 d (Q-D7); `unresolved[]` in exit packages; no unified typing or cost | **partial** |
| Self-evolution classes A–D (§12) | 07 mutation rules + epoch constraints (≤3 mutations, one human gate, no strategic change); anomaly loop → next epoch | **spec** — *maps cleanly, see §5 M7* |
| Human projections: attention / decision / landscape / trajectory / representation (§8) | Views: Today, Pending, Commitments & Return, Weekly (4 of ≤6 allowed); hub notes per project; no landscape/trajectory/representation view | **partial** |
| Metrics §14 (CRA, state reconstruction cost, activation recall, review yield, reuse yield, debt burn, representation gain, scaling ratio) | 30/90-day success criteria (01); hard gates table (03); 7-day resume <10 min *is* state-reconstruction cost; dual scoreboards | **partial** |
| Stopping policy (§17) | Panel stop conditions per type (02); RQ stop rule ("theory without use evidence is itself a failure") | **spec** |
| Incremental delta (I4) | Accept applies `proposed_state_changes` only; views regenerated from state | **impl** |
| Reasoning portability (I7) | AGENTS.md vendor-neutral pointer; plain files + git; NFR-4 replaceable interfaces | **spec** |
| Validation before generalization (I8, §13) | "No field without 3 observed cases; no plugin without a measured failure; no agent where a script suffices" (03) | **spec** — *stricter* |
| Failure modes §27 | FMEA-001, META-1/2, score-inflation, signal pollution (08), compression → partial-observability rule, consensus illusion → maker≠checker | **partial** |

**Genuinely novel in the documents (no existing counterpart):** the meta-loop as scheduler; trigger learning with shadow mode; decision records for project work; typed open debt with cost; review-depth routing for *agent* outputs; representation review as a named state; cross-project reuse extraction; latent questions with activation conditions; the metric set; the four-class self-evolution ladder as an explicit governance table.

**Where the existing spec is already stronger (the documents must inherit, not regress):** sockets are concrete schemas with gates; transitions are reversible and attributed; the gesture grammar makes the human API one token wide; privacy planes and the writer matrix; frozen contract with mutation budgets and deletion conditions; hard burden gates backed by lineage evidence; the deterministic/model/human split.

**Mapper precision (116-row independent map, same session — deltas worth naming):** ACE's primitive is the *validated transition*, MLD's is the *decision object* carrying alternatives/rationale/reversal condition — complementary, not competing. Concretely missing in `engine/` today: a packet-generator subcommand (S6 DELEGATE), an `uncertain` verification outcome routed to a second verifier of a different model family (S8), exit-package fields `contradictions · reusable_assets · failure_modes · recommended_next_transition` (socket output), `open_debt_created/closed` on accept (S10), any contradiction / correction-frequency / cost-anomaly trigger (S3), and dependencies between decisions/projects (4.2). ACE views cover Attention≈Today and Decision≈Pending; Landscape (8.3) and Representation (8.5) views are absent and would each have to *replace* a view. MLD's §16 questions were not registered in spec/10 — §7 below answers them; they are filed under Round 5 rather than as new Q-IDs.

---

## 4. Tensions with frozen rules — and how each resolves

| The documents say | Existing rule | Resolution |
|---|---|---|
| "The runtime … selects the next operation" via a utility function (S4) and DepthScore (§20) with model-estimated terms | Models *propose*, only a validated loop *records* (CLAUDE.md); no continuous autonomous agent (03 §6) | The meta-loop is a **deterministic script** (`ace tick`). Any model-estimated term enters as a logged proposal field on a record; the transition policy is a table over record fields, not a model call. Model calls are allowed only in INTERPRET (classification) and REPRESENTATION_CHECK (anomaly naming) — both produce packages into `outbox/` |
| Rich canonical state object (spec §2: ~40 fields) | No field without three observed cases (03) | Adopt fields one at a time on evidence. Three already qualify: decision record (R-rounds ×3 rounds), open-debt item (pending aging, at-risk, `unresolved[]`), trigger candidate (four dormant scheduled skills + hand-run loops) |
| "The machine may maintain many graphs" (§8) | No knowledge graph / vector DB in the first slice (03 §6); derived views never sources of truth (11 rule zero) | Graphs are **derived projections** computed at tick time from records; never stored as truth. Retained indefinitely, not only for slice 1 |
| Four cadences incl. monthly/bimonthly deep meta-review (§6) | No new routine surface to monitor (07 mutation rule 3); weekly <20 min hard gate | Monthly meta-review is a **C-mode ceremony**: ≤5 decisions, generated brief, output = decisions only (MLD §6 agrees: "decisions and policy changes, not a long descriptive report") — no new surface, it reuses the weekly review slot once a month |
| Cognitive-event signals include "persistent hesitation or tension" (spec §4) | Registry rule: the model never guesses a binding; hedges are non-binding (13) | Keep only **workflow-observable** signals already in the registry (repetition, correction, reframing, out-of-scope question, repeated manual invocation). Drop affective signals — MLD §4 itself forbids psychological inference |
| Self-evolution classes C/D (representation, objective) may be system-initiated | Never rewrite user hypotheses; no automatic change to strategic goals (CLAUDE.md, 07) | Class C proposals come only from anomaly-loop-certified findings into the *next* epoch; Class D only through door 1. See §5.7 |
| PROJECT-V as reference validator (§13) | Research content is IP → content plane only; `<PROJECT-V repo>` is RO-REF (08) | PROJECT-V adapter reads RO-REF, writes records (pointers + hashes) to the control plane, content/claims to `F:\ACE_local\research\<project>\`. Replay of *session transcripts* carries operator-session-corpus sensitivity — R5-5 |
| Portfolio/landscape/trajectory views (§8.3–8.4) | ≤6 stable hub views; dashboard-replacement condition (02) | Any new view must replace one. Candidate: Weekly Review absorbs the attention packet (it is already a projection), leaving room for one Decisions view |
| Autonomy policy "should learn from repeated human corrections" (§4.5) | Consequential decisions remain human (NFR-7); backpressure exists because the single approver is the bottleneck (Q-D11) | Learning = promotion of *trigger candidates* through shadow mode, each promotion a batch-class tick. The policy never changes approval classes |
| `agent_request.relevant_state_slice` carries claims/evidence/contradictions to any vendor (spec §6, I7) | Two-plane rule: content/IP only in `F:\ACE_local`; control plane holds pointers + hashes; clinical knowledge never in the substrate (CLAUDE.md) | A knowledge-bearing state slice **cannot transit ACE_storage**. Cross-vendor sockets pass local paths + sha256; the panel on the owning machine dereferences. PROJECT-V claims live on the content plane; their existence and hashes on the control plane |
| Trigger promotion after shadow comparison (§21) is a policy change | Red-Queen: ≤3 mutations per epoch, each with pass/fail + deletion condition (07) | The **registry mechanism** is one Class-B mutation (M4). Individual trigger promotions inside it are Class-A parameter changes (like the 21-day / 7-14-day thresholds) — approved by the operator's tick, which *is* the ruling in gesture form; never by the engine alone |
| Infrastructure review of under-triggered tools (§5.5, §5.7) | R2-5 ruling: the four legacy scheduled skills are maintenance-insight oriented, not useful for ACE — coexist untouched, ACE ignores them; Q-C1/C2 **closed** | The dormancy audit targets **ACE's own inventory only** (its loops and the skills it names in 05/07/13). The legacy skills are not re-opened |
| S5 may select D0 "no review" adaptively | Validator rejects incomplete packages; every state change has an approval class (03 §5, 04) | A model-chosen D0 on a state change is a silent decision. Depth is computed by code from the record's content class; D0 exists only for the auto class |
| `mutation_permissions` on a socket may grant canonical-state writes (spec §6) | Writer matrix: panels write `outbox/` and their declared `ACE_local` boundary only; `state/` is loop-only (11) | `mutation_permissions` ≡ the declared write boundary in `ACE_local`. State mutation is never grantable to an agent |


No tension requires reopening a frozen decision. One touches a ruling that is still open: Q-D8 (anomaly-loop maturity) — required for D4 in §5.4.

---

## 5. The rethink — the meta-loop as the layer that schedules ACE's machines

### 5.1 The layer stack, made of files that already exist

```
POLICY      approval classes (03 §5) · gesture grammar (13) · trigger registry [new] · depth table [new]
ATTENTION   views/Today, Pending, Commitments&Return, Weekly (impl) · aging + returns (spec) · latent questions [new field]
DECISION    spec/10 rulings (system) · hub/decisions/ [new record type, project-level]
KNOWLEDGE   hub/projects, commitments, evidence (impl) · claims + contradictions [PROJECT-V adapter first]
EXECUTION   panels via packets/outbox (impl) · loops in engine/ (impl) · skills (rqgm, disagree, blindspot, multi-model orchestration)
            └── SOCKET = session packet + exit package + validator gates (impl)
META-LOOP   `ace tick` [new]: one deterministic scheduler running S1→S15 over the records above
```

The four ACE object-level machines (panel, commitment/return, project/evidence, handoff — 04) are unchanged; the meta-loop is what *calls* them on a schedule, the thing that has been missing.

### 5.2 One tick, deterministic

`ace tick` (Task Scheduler, every 30 min while logged in + 07:00 daily) runs, in order and idempotently:

1. **OBSERVE** — diff hub vault vs engine baseline (gesture watcher), read inbox (clarify loop), read `outbox/` (validator), read clock (returns due, pending age, project at-risk).
2. **INTERPRET** — deterministic marks only; anything ambiguous becomes a one-line clarify proposal, never a guess (13 rule 5).
3. **DETECT_TENSION** — contradictions are *structural* in v1: a commitment closed without evidence; a project `current` with newer pending; a return date passed; a decision whose reversal condition fired; repeated rejection of the same proposal class.
4. **PRIORITIZE / SELECT_DEPTH** — table lookup (§5.4), not a utility function.
5. **DELEGATE / EXECUTE** — write packets for anything needing a panel; execute auto-class transitions; stage batch-class proposals in `pending/`.
6. **VERIFY / INTEGRATE** — existing validator + accept path (unchanged).
7. **ATTENTION_UPDATE** — regenerate views; Today gains the attention-packet fields (*why now · consequence of delay · what proceeds automatically*) in place of nothing new.
8. **POLICY_UPDATE** — append repetition counters; emit trigger candidates (§5.5) as batch proposals.
9. Audit + attributed commit per transition (unchanged).

Budget: one tick must finish in <10 s and write nothing when nothing changed (idempotence test). A tick is not an agent (03 §6 holds): every model call it needs is a packet it *leaves* for a panel.

### 5.3 Decision records (MLD §2.1) — the one new record type with three observed cases

Three rounds of rulings in spec 10 are already decision events with alternatives, recommendation, verdict and downstream effects. Promote the shape, not the content: `hub/decisions/D-<ulid>.md` with frontmatter `question · options · recommendation · verdict · decided_by · reversal_condition · affects[] · evidence[]`. The C-mode ceremony format (12 v1.2 §4 — numbered queue, defaults marked, one-token verdicts, silence = defer) is the *input surface*; the record is its durable residue. For the system's own decisions, spec 10 remains the human-readable registry and the loop mirrors rulings into records. **This is the mechanism by which a decision sitting in a document becomes an item in the Pending view** — the direct fix for §2.

### 5.4 Review depth D0–D5 bound to what exists

| Depth | MLD | ACE binding | Trigger (deterministic) |
|---|---|---|---|
| D0 | continue | auto class | existence / pointer / deterministic date |
| D1 | integrity check | validator gates | every exit package |
| D2 | targeted verification | tests / second-model check via a cross-vendor review bridge | `evidence_created` claims a shipped artifact; commitment closure |
| D3 | adversarial | `rqgm-loop` epoch, `disagree`, blind audit | explicit-approval class; kill / handoff / transfer / strategy |
| D4 | representation review | anomaly-loop pass → certified finding | ≥3 rejections of the same proposal class; ≥2 edge cases on one mechanism (EC-001 would have fired it); repeated `validation_failed` with the same error |
| D5 | architectural / strategic | Red-Queen epoch + operator ruling | frozen-test failure; monthly ceremony |

DepthScore (MLD §20) is replaced by this table until outcomes exist to calibrate weights; the table is the "bootstrap heuristic" MLD itself asks for, with the advantage that every term is a record field.

### 5.5 Trigger learning (MLD §21) — repetition counters, shadow mode, batch promotion

`quality/triggers/` holds candidates. A candidate is created by code when: the same ACE skill/loop is invoked by hand ≥3 times after the same event type (e.g., `rqgm-loop` after a produce panel; `disagree` on an honest-probe gesture; `clarify_loop` after a capture); the same gesture sequence recurs ≥3 times; or a return/aging condition is handled manually that a loop could have fired. Shadow mode = the tick writes `WOULD_FIRE` lines to `quality/evals/` for 14 days; the Weekly Review shows `candidate → fired-when-you-did n/m`; promotion is a tick in the hub (Class A inside the M4 mechanism, §4); retirement is automatic after 30 days without a true positive. **First shadow run = the dormancy audit of ACE's own inventory** — every loop in `engine/` and every skill the spec names — scored by invocations ÷ applicable sessions (the Vercel metric, annex A). The legacy scheduled skills stay outside per R2-5.

### 5.6 Open debt as a projection, not a table

`open_debt` = pending age ≥7 d ∪ at-risk projects ∪ `unresolved[]` from accepted packages ∪ decisions past reversal check ∪ shadow triggers awaiting verdict. Computed at tick; shown as one line in Weekly Review ("N debt items, oldest X d, cost est."). No new file, no new surface.

### 5.7 Self-evolution classes A–D (MLD §12) → existing governance

| Class | MLD | ACE channel | Approval |
|---|---|---|---|
| A parameter/policy | thresholds, depth, agent choice | loop config in `engine/`; trigger promotion | batch (tick) |
| B workflow mutation | insert verifier, add trigger, reorder | Red-Queen mutation, ≤3 per epoch, pass/fail + deletion condition | epoch human gate |
| C representation mutation | new primitive, split/merge classes | anomaly-loop-certified finding → next epoch's contract; new record type needs 3 observed cases | operator ruling at epoch boundary |
| D objective mutation | change success criterion, elevate invariant | amendment door 1 only | operator, explicit |

This is the table MLD §16 Q7 asks for. It already exists in ACE; MLD gives it names.

### 5.8 Representation review — the anomaly loop's job, and the question MLD cannot yet answer

MLD I2/I12 asks the system to distinguish representation search from parametric tuning. In ACE that split is institutional: RQGM optimizes *inside* a frozen contract (A/B); the anomaly loop hunts anomalies the contract did not anticipate (C). The lineage-guard table (01) is itself a history of un-governed representation mutations (OneNote GTD → legacy PKM vault → PARA reorg → folder agent contract → another meta-system → ACE → the meta-loop documents): each was a reframing that kept the same objective. The honest implication is that **adopting the meta-loop documents is itself a Class C event** — their representation changes (five layers, decision events, meta-loop states) enter the Epoch-2 contract as certified findings with a migration plan and rollback (the documents' own `representation_proposal` schema), not as a rewrite of the spec.

### 5.9 PROJECT-V as the second validation project

Why it fits: a hypothesis program, a dependency graph of intermediate results, a reviewed critique with explicit contradictions (e.g., a recorded non-sequitur), competing representations, and an unanswered empirical question — exactly the claim/contradiction/decision material the knowledge layer lacks in ACE's productivity use. Adapter: RO-REF read of `<PROJECT-V repo>`, claims and decisions recorded on the local plane, pointers + hashes on the control plane; replay per MLD §26 starting from its earliest framework materials forward. Transfer test (I8): the same adapter shape must work on a project other than PROJECT-V (PROJECT-P, a research proposal, or PROJECT-E, an evaluation project) before any field it introduced becomes core.

### 5.10 Metrics — derive, don't instrument

| MLD metric | Derivation from existing logs |
|---|---|
| State reconstruction cost | already gated: 7-day resume <10 min (01); measure = time from packet open to first gesture |
| Review yield | decisions recorded ÷ ceremonies held (audit `gesture` events with verdicts ÷ weekly views generated) |
| Activation recall | shadow-trigger true-positive rate (§5.5) |
| Open-debt burn | debt items closed ÷ created per week (§5.6) |
| CRA | decisions + accepted transitions per minute of hub-edit time (gesture-watcher diff timestamps as proxy) |
| Cognitive scaling ratio | (weekly hub minutes) ÷ (active projects + open commitments), monthly slope; target slope ≤0 |
| Reuse yield, representation gain | Epoch-2 — need evidence records with `impact or reuse` populated first (FR-8) |

### 5.11 Sequencing

**Epoch-1-compatible now** (address observed failures, no contract change): M2 `ace tick`; M3 decision records; M8 attention-packet fields in Today; M6 debt projection. **Epoch-1 mutation budget** (≤3, one already used by M1 gestures): M4 trigger registry; M5 depth table. **Epoch-2 candidate contract**: M7 class table as written doctrine; representation review state; PROJECT-V adapter; metrics §5.10; monthly ceremony; reuse extraction. Nothing proceeds before the Round-5 rulings (§10).

---

## 6. Mutation candidates — Red-Queen compliance (07 rules 1–6)

| ID | Mutation | 1 observed failure | 2 fewer cognitive ops | 3 no new surface | 4 pass/fail test | 5 deletion condition | 6 evaluators |
|---|---|---|---|---|---|---|---|
| **M2** | `ace tick` scheduled deterministic loop | §2 stall: loops exist, never run | removes "remember to run the loop" and "remember to look" | reuses views; Task Scheduler | 14 days of ticks with ≥1 auto transition/day and zero duplicate writes; pending never ages past 14 d unflagged | tick errors ≥2/week or the operator disables it | Hub trust ↑, Simplicity neutral (one task) |
| **M3** | Decision records + Decisions view | rulings stalled in spec 10 for 32 d | rulings become ticks in the hub | replaces nothing yet → must absorb the Round format (spec 10 stays registry) | ≥80% of system decisions answered via hub tick within 7 d over 30 d | answered-in-hub rate <50% | Cognitive off-loading ↑ |
| **M4** | Trigger registry + shadow mode | every ACE loop is hand-run; gesture watcher never activated; skills (rqgm, disagree, blindspot) invoked only when remembered | removes "remember which skill to invoke" | quality/ dir + one Weekly line | shadow precision ≥70% on promoted triggers; false-fire <1/week | trigger spam (>3 unwanted fires/week) | Simplicity must stay bounded (≤10 live triggers) |
| **M5** | Depth table D0–D5 | none observed yet — *candidate only* | — | — | — | — | hold until an observed mis-depth (a verified-wrong accept or a wasted epoch) |
| **M6** | Debt projection | 9 items aged silently | one line replaces scanning pending/ | none | weekly line present; oldest-debt age trending down | ignored 4 weeks running | — |
| **M8** | Attention-packet fields in Today | Today has shown one item since Jul 21 with no "why" | no re-deriving urgency | modifies existing view | Today ≤5 lines; each item has why-now + consequence | the operator reports noise | Cognitive off-loading ↑ |

M5 fails rule 1 today and is filed, not proposed — consistent with 07's stop rule.

---

## 7. Answers to the ten reference-agent questions (MLD §16)

Citations are short names; full references with verification marks are in `spec/14_LITERATURE_ANNEX_2026-08.md`.

**Q1 — Emergence vs local optimization: when is a new abstraction genuinely novel rather than a reparameterization?**
The literature's honest answer is that *LLM judges cannot tell* (RQ-Bench: judges reward fluent restatement; the Ideation–Execution Gap: LLM-rated novelty decays after execution more than human-rated novelty). What does work is structural: (i) the three axioms of the novelty benchmark as unit tests — add the researcher's own prior notes to the reference pool and the score must *drop*; (ii) an author-anchored reference (the operator's own prior framing, e.g. the lineage-guard table) in every comparison set; (iii) ShinkaEvolve's similarity rejection *before* review, so near-duplicates never consume attention; (iv) Prospective Compression — promote only if expected reuse over the next N project slices justifies the library cost. ACE binding: a representation proposal must name ≥1 observed anomaly the current representation cannot explain (MLD's `anomaly_explained`, EC-001 is the existing example), pass the similarity gate, and be certified by the anomaly loop (Class C, §5.7); the verdict stays a C-mode human decision. Novelty credit is granted only after the abstraction survives on a second project (I8).

**Q2 — Trigger learning without overfitting to accidental behavior.**
MLD §21's shadow lifecycle is well supported. The guardrails the literature adds: implicit signals are hypotheses, not rewards (*User Feedback … Noisy as a Learning Signal*, EMNLP 2025) — require repetition ≥3 or explicit confirmation; compile a correction into an enforced check only on recurrence (TRACE); patch typed, canary on past cases, one attributed commit with rollback (ANNEAL); keep an evidence ledger per rule with reliability and an explicit ABSTAIN (*Closing the Feedback Loop*); downgrade checks that never change an outcome (*Self-Verification Dilemma*); survival score = use count · recency · success (Darwinian Memory); measure invocation rate per *applicable* session, not per session (Vercel). ACE binding (M4): candidates from code over `audit/events.jsonl`; 14-day shadow; precision ≥70% to promote; ≤10 live triggers; retire after 30 days without a true positive; promotion never changes an approval class.

**Q3 — Review-depth allocation under bounded budgets.**
Three results reshape MLD's DepthScore: escalate on **delegation value** — P(the human would change the outcome) × cost of being wrong — not on uncertainty, and calibrate so the human-review rate fits a declared weekly budget (*Calibrate-Then-Delegate*); the human reviewer is a **fatiguing, finite resource** — choose an escalation rate under capacity C rather than escalating everything (*Oversight Has a Capacity*); decide escalation *before* the cheap pass when a pre-generation signal exists, because try-cheap-then-escalate pays twice (*Is Escalation Worth It?*). Two thresholds on one weak-verifier score with an online ledger (*When to Trust the Cheap Check*) is the simplest implementable policy, and a user-declared wrong-action budget can be turned into the operating point directly (*Budgeted Act-or-Defer*); the D0/D1 floor should be deterministic recomputation, not an LLM (*Real-Time Detection and Repair*; *Specification as Quality Gate*); route to the human only on model–record disagreement (*Recursive Resolution*, KDD 2026). ACE binding: the weekly <20 min gate *is* capacity C; the depth table (§5.4) keys on record fields that exist before generation; DepthScore is deferred until outcomes exist to calibrate it.

**Q4 — Capturing weakly articulated intuition without over-interpreting speech.**
Use deterministic, workflow-observable boundaries, never affect: HingeMem's rule — emit an event when any of (person · time · location · topic) changes — transposed to (project · decision · artifact · surface); keep captures **verbatim** with interpretations as additive overlays (*Fidelity Before Structure*: verbatim beats extraction by 16–22 points); type atoms as evidence / cue / claim and bound claim reliability by attached evidence (MemIR); treat edits to agent output as the highest-quality signal (PRELUDE). ACE already has the strongest piece: the registry's epistemic channel (hedge = non-binding, repetition-with-compression = escalation dial, honest-probe → adversarial) is evidence-derived from 122 sessions, which no paper in the sweep matches. MLD §4's own rule — no psychological inference — holds; "persistent hesitation" is dropped from the detector list.

**Q5 — The minimal stable socket contract across Codex / Claude / GPT / future frameworks.**
The sweep converges on a small field set. Input: objective, state slice, allowed tools, mutable regions (AlphaEvolve's `EVOLVE-BLOCK` markers make the delegation boundary machine-checkable), budget, **verification criterion written before execution** (Meta-Agent), autonomy level as the human role per action class (*Levels of Autonomy*). Output: one of six control decisions — Act / Ask / Refuse / Stop / Confirm / Recover — plus **Propose** (AgentAtlas + ACE's own rule), candidates with verbatim evidence and serials rather than adjudicated conclusions (*Post-Retrieval Assembly*: +10.8 pp from separating extraction from policy), typed escalation reason (AAMAS 2026), model family (self-preference bias: reviewer ≠ producer family), reusable assets, recommended next transition. Each state element stamped with the six axes — authority · scope · mutability · provenance · reversibility · licensed actions (*Always-On Agents*). For the cross-vendor *transport*, A2A v1.0's Task lifecycle (SUBMITTED → WORKING → INPUT_REQUIRED → COMPLETED/FAILED/CANCELED) is the published analogue of the panel lifecycle (04 §1); ACE's socket stays a file, but the state names should be mappable 1:1. ACE binding: the session packet + exit-package schema already are this contract; add `control_decision`, `mutation_permissions`, `verification_criterion`, `model_family`, `reusable_assets` one field at a time under the 3-cases rule. Vercel's result also settles where always-applicable procedure lives: inlined in CLAUDE.md/AGENTS.md, not as a skill.

**Q6 — Evidence threshold before a representation or objective changes.**
Objective changes are forbidden inside an epoch and allowed only at a boundary with pinned criteria (*Red Queen Gödel Machine* — the published form of spec/07); the coverage critic found only one operationalization of objective *drift* (Apollo's goal-drift report: all models drift under competing pressure, and drift correlates with pattern-matching), so OBJECTIVE_REVIEW needs a fixed goal-adherence probe set rather than a detector. For representation changes: ≥3 observed anomalies the current representation cannot explain (ACE's 3-cases rule), a **falsifiable contract** stating which metric will move and by how much (*Agentic Harness Engineering*), a paired with/without intervention test (SkillAudit), cascading-invalidation debt opened on every dependent claim (STALE), archive-not-lineage so the prior representation remains addressable (DGM; ACE supersede-by-move), and a transfer test on a second project (I8). Score decay after execution is the calibration signal for whoever proposed it.

**Q7 — Which changes may be autonomous, which need adversarial review, which need the human.**
The four-class table (§5.7) is consistent with every governance source found: allowed autonomy is bounded by **evidence tier** — formal check > executed test > external data > human judgment > model self-assessment (*Recursive Self-Improvement* survey); Propose → Evaluate → **Commit** → Serve with Commit the only state-writing step (*Safety in Self-Evolving Systems*) — identical to "model proposes, loop records"; layered gating per tier (*Self-Improvements* survey); intra-test-time changes are transient Class A, inter-test-time changes are persistent B–D (TMLR survey). Two hard rules the literature adds: the acceptance gate for any self-evolution proposal must be **sealed** — pre-registered criteria outside the proposer's reach, prior version retained (*Self-Authored Verification Is Unreliable*); and consecutive unaudited self-evolution steps must be capped, with depth rising as a function of steps since the last grounded verification (*Reward Hacking in Self-Improving Code Agents*). Review ~30–40% of evolution steps, concentrated at verification, tracking a frequency–gain ratio (ANCHOR).

**Q8 — Measurable properties that indicate sublinear cognitive scaling.**
Metrics — measured, never self-reported: METR's 2025 RCT found experienced developers 19% *slower* with AI while believing they were ~20% faster, so every scaling claim here is timed from logs. The slope of (weekly hub minutes ÷ active records) over months (§5.10 — must be ≤0); **Ask-F1** per agent (HiL-Bench); realized delegation value per escalation; review yield; **headroom to capacity** (*Oversight Has a Capacity*); extraneous-load proxy — model-initiated context switches per session (*Precision Proactivity*: extraneous load is ≈3× as harmful); state-reconstruction time (already gated at <10 min); fraction of transitions made by gesture (PA-4's ≥80% test); decisions per ceremony (≤5). Architecture properties: every surface has a deletion condition; activation is automated (no manual loop starts); attention packets are bounded trees (*Steering via Scalable Interactive Oversight*); delivery only at workflow boundaries (IUI 2026: 52% engagement at boundaries); oversight time reported by type — a-priori / co-plan / live / post-hoc (FAccT 2026).

**Q9 — Detecting when a one-off workflow has become a portable method.**
Count recurrence in successful trajectories (Agent Workflow Memory, k successes); maintain a per-skill **transfer matrix** — same task / other task / other project / other model — from actual reuse events, tagging low-transfer skills project-local (AFTER); per-(skill, task class) effect estimates because opposing effects cancel in aggregate (ASSAY); practise-before-promote with the test stored beside the procedure (SkillWeaver); mandatory naming/documentation step before a library entry (LILO AutoDoc); reuse-first, add-on-failure with the insufficiency logged (TheoryCoder-2); score a change by its descendants' outcomes (Huxley-Gödel clade metaproductivity); mine the event log for recurring activity clusters and promote a cluster to a role only on recurrence (BPM 2026 process-mining line). ACE binding: FR-8's `impact or reuse` field becomes the counter; promotion to substrate requires validated reuse on a second project.

**Q10 — Where the architecture could hide errors.**
*Compression*: verbatim beats extraction; context collapse and brevity bias are measured failure modes (*Agentic Context Engineering*); fact attrition under deliberation (*Deliberative Illusion*); belief entropy after consolidation. *Confidence aggregation*: models that both err agree ~60% (*Correlated Errors*); same answer with mutually exclusive reasons (*Consistency Illusion*); κ-deflation of 33–41 points in judge reliability; self-preference survives rubrics; teams lose up to 41% vs their own expert. *Excessive autonomy*: false-success 45–76% with judges ≤0.65 AUROC; a production judge that surfaced <¼ of systematic defects (*Catching One in Five* — review theater, measured); self-authored verification; misevolution across four pathways. Two the MLD list omits: the **human side** — confirmation bias raises the overseer's confidence without raising accuracy, and reviewer reliability decays under load; and **activation failure** — the stall in §2 was invisible precisely because the review that would have surfaced it was itself unactivated. Consequence: `ace tick` must emit a heartbeat into the Weekly view (a dead-man's switch), so silence is itself an observed event.

---

## 8. What the 2025–26 literature adds — by proposal

| Proposal | Borrowed mechanism (source) | Effect on the design |
|---|---|---|
| **M2 `ace tick`** | cheap wake-scorer before any LLM (*Do Proactive Agents Really Need an LLM to Decide When to Wake?*); library-time loop separate from task-time loop (SkillOps); constraints with tolerated violation rates tested on the event stream (*Auditing AI Systems in the Wild*, KDD 2026); heartbeat (Q10); Anthropic's long-running-harness pattern (progress log + feature list with pass/fail + git as rollback + session start = read logs and run tests) is the same shape as packets + state + attributed commits; consolidation belongs in the 07:00 run (*Sleep-time Compute*) | tick = deterministic scorer + constraint checks + projections; no model in the loop; emits `WOULD_FIRE`/`FIRED`/`HEARTBEAT` events |
| **M3 decision records** | events.jsonl with a `decision` event type as the single source of truth and `regenerate` projections (PROJECTMEM); MADR status lifecycle incl. `superseded-by`; MAEB seven fields; six control decisions + Propose (AgentAtlas); complementary labels ("definitely wrong") as a verdict type (ICLR 2026) | record = `hub/decisions/D-*.md` mirrored from a typed audit event; the C-mode queue accepts one-token verdicts *and* "not X" eliminations |
| **M4 trigger registry** | §7 Q2 set: TRACE · ANNEAL · Darwinian survival score · evidence ledger with ABSTAIN · noisy-feedback guard · invocation-rate metric (Vercel) · per-(skill, task class) effects (ASSAY) | thresholds in counts not days; shadow precision ≥70%; first run = dormancy audit of the four legacy scheduled skills |
| **M5 depth table** (filed) | delegation value (*Calibrate-Then-Delegate*) · capacity C (*Oversight Has a Capacity*) · decide before the cheap pass (*Is Escalation Worth It?*) · two-threshold ledger (*Cheap Check*) · deterministic D0/D1 floor · reviewer family ≠ producer · disagreement map instead of winner (ICML 2026) · a critic-of-the-review role with an explicit disagreement prompt (*Adversarial Review*, ICML 2026 DL4C) | the table (§5.4) becomes the bootstrap; calibration data accrue from the ledger before any score is trusted; D3 = reviewer + critic-of-review, never reviewer alone |
| **M6 debt projection** | cascading invalidation opens debt on dependents (STALE); reconstructability audit as a debt % (DES); residual contested claims → debt (*Collaborative Disagreement Resolution*); **intent debt** — missing rationale/goal/constraint that both humans and agents need (Storey 2026) — as the type name for decisions without a recorded `why` | debt = union of five existing queries + dependents of any invalidated claim + decisions lacking rationale |
| **M7 class table** | evidence-tier bound (RSI survey) · Propose/Evaluate/Commit/Serve (MLAS) · sealed gate (*Self-Authored Verification*) · epoch boundary rule (*Red Queen Gödel Machine*) · falsifiable contract (AHE) · archive-not-lineage (DGM) · step cap (*Reward Hacking*) | §5.7 gains three columns: evidence tier required · sealed criteria hash · max unaudited steps |
| **M8 attention packet** | typed escalation reason (AAMAS 2026) · delivery at workflow boundaries only (IUI 2026) · bounded decision tree (*Steering*) · ask iff EVPI > interruption cost (ACL 2026) · goal questions first, input questions queue (*Ask Early, Ask Late*) · presence indicator + context trace (CHI 2025) | Today line = `item · why-now · consequence-of-delay · typed-reason · what-proceeds-automatically`; non-urgent output waits for the next boundary (07:00 brief, session close) |
| **PROJECT-V adapter** | claims as `{hypothesis: p}` with Noisy-OR and explicit competing candidates (BeliefMem); bi-temporal claim edges (Zep); three STALE probes after each change; Proximity-before-ranking and Elo history as files (Co-Scientist); falsification role per claim (*Adversarial Experiments*); "no synthesis without a primary-artifact pointer" (Kosmos) | the hypothesis program + result-dependency graph becomes the first claim/contradiction graph; the recorded non-sequitur (§5.9) is the first contradiction record |
| **Metrics** | Ask-F1 · headroom · extraneous-load proxy · fact-survival · review-yield · invocation-rate · transfer matrix · score decay | all derivable from `events.jsonl` + gesture timestamps; none needs a questionnaire |

**Do not import.** RL-trained routers/verifiers and DPO-style skill selection (no volume, no ground truth); vector/graph databases as sources of truth (03 §6; derive instead); LLM-in-the-loop novelty judging (Q1); automatic memory "evolution" that rewrites old notes in place (A-MEM as shipped — stage as proposals); Elo tournaments over handfuls of options; any proactive surfacing mid-flow (IUI 2026, CHI 2026 group-chat result: read as disruptive).

**Where ACE is ahead of the sweep.** No paper found derives its human-side grammar from usage evidence the way spec/13 does; none has deletion conditions on every surface; none binds storage planes to privacy classes; the Red Queen Gödel Machine preprint (June 2026) formalizes what spec/07 froze in July 2026 with a concrete evaluator panel — ACE is a running instance of that protocol, which is itself publishable evidence (P0-B).

---

## 9. Failure modes — MLD §27 cross-checked against ACE

| MLD §27 | ACE status | Gap |
|---|---|---|
| Compression blindness | partial-observability rule + validator `sources_not_seen` gate | claims inside accepted packages are not re-verified — D2 binding (§5.4) |
| False cognitive inference | registry: hedge = non-binding; never guess | keep affective signals out (§4) |
| Trigger spam | — | M4 deletion condition; ≤10 live triggers |
| Ontology ossification | 3-cases rule; supersede-by-move | no explicit representation-review state until Epoch 2 |
| Local-optimum recursion | RQGM inside frozen contract; anomaly loop outside | anomaly-loop maturity unruled (Q-D8) |
| Agent consensus illusion | maker≠checker; blind audit agent; cross-vendor review | no rule that verifiers must be a *different model family* from the producer — propose as D3 requirement |
| Cross-project contamination | NAME-ONLY/EXCLUDED zones; alias rule | adapter transfer test (§5.9) |
| State drift | FMEA-001 sync gate; manifest loop hashes | manifest loop not scheduled (M2 fixes) |
| Open-debt explosion | aging rule (not running) | M2 + M6 |
| Review theater | 07 stop rule; weekly "one simplification" | review-yield metric (§5.10) |
| Human bypass | approval classes; explicit class list | trigger promotion must never change a class (§4) |
| Socket leakage | vendor-neutral AGENTS.md; plain files | state is neutral but `engine/` is Windows/git-specific; add a socket conformance test to `tests/` and keep the knowledge-bearing slice off the control plane (§4) |

---

## 10. Round 5 — questions for the operator (flag · propose · wait)

- ~~**R5-1** Stance question~~ — **ruled 2026-08-22 (operator): "AACE and ACE are essentially the same thing."** One system; the documents are reconciled into `spec/` (v0.2 exports in `spec/meta/`) and the name is retired. Their structural changes still enter through door 2 as Epoch-2 candidates (07 stop rule).
- **R5-2** Activate **M2 `ace tick`** as a scheduled deterministic loop (30 min + 07:00). This subsumes R4-1 (gesture watcher standing loop). One word activates both. *Rec: yes — it is the single change that addresses the observed stall.*
- **R5-3** Approve **M3 decision records** and the mirroring of spec-10 rulings into hub ticks (Decisions view replaces nothing; uses view slot 5 of 6). *Rec: yes.*
- **R5-4** Approve **M4 trigger registry** in shadow mode; first shadow run = dormancy audit of ACE's own loops and skills (invocations ÷ applicable sessions). Legacy scheduled skills stay outside per R2-5. *Rec: yes.*
- **R5-5** PROJECT-V adapter: may the replay (MLD §26) read **session transcripts** (sensitive, same class as the operator-session audit corpus) or only the project files under `<PROJECT-V repo>` (RO-REF)? *Rec: project files only for the first pass.*
- **R5-6** Monthly meta-review as a C-mode ceremony (≤5 decisions, generated brief) — first one when? *Rec: 2026-09-19 (30-day checkpoint from today's restart).*
- ~~**R5-7** Provenance~~ — **ruled 2026-08-22**: drafted by a peer agent; "AACE" was a naming slip. Recorded in `00_INDEX`.
- **R5-8** (carried) R3-1..R3-5, R4-1, R4-2 remain open; with M3 they become hub ticks rather than questions in this file.

---

## 11. Partial-observability statement (CLAUDE.md panel rule 5)

- **Inspected**: both MLD documents (full); `spec/01–13`, `CLAUDE.md`, `engine/*.py`, `schemas/`, `ACE_storage` (`audit/`, `state/`, `pending/`, `packets/`, `quality/`, git log), `F:\ACE_hub` (git log, mtimes, views), `F:\ACE_local` (directory mtimes only), Windows Task Scheduler (ACE tasks), `<PROJECT-V repo>` (one file header, RO-REF), git-workspace directory names.
- **Not inspected**: Cowork/Claude panel histories outside ACE stores; the operator-session audit corpus and session transcripts; the other meta-system's state; the four legacy scheduled-skill configs' firing state; the hub vault's sync state; any NAME-ONLY or EXCLUDED zone.
- **Date range**: repo history 2026-07-19 → 2026-08-22; literature sweep 2024-01 → 2026-08 (see annex).
- **Confidence in completeness**: high for the ACE-side map; medium for the stall interpretation (usage outside ACE stores is invisible); medium for the literature (verified citations only; venues' full 2026 proceedings not exhaustively enumerated — annex lists what was and was not reachable).

---

### Change log
- **v0.1 (2026-08-22)** — created by the explore panel digesting the meta-loop documents; concept map, tensions, rethink, mutation candidates M2–M8, §16 answers and literature digest (annex: 8 finders, 8 verifiers, 1 critic), Round-5 questions.
