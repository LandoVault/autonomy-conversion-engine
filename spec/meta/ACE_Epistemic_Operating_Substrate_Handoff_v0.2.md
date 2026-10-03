# ACE Epistemic Operating Substrate
## Design Handoff / Reference-Agent Review Draft

| | |
|---|---|
| **Version** | **0.2** |
| **Date** | 2026-08-22 |
| **Supersedes** | v0.1 — `reference materials/AACE_Epistemic_Operating_Substrate_Handoff.md` (not in public release; received 2026-08-22, sha256 `028741cd…583d6`; frozen, never edited) |
| **Status** | Working specification — reference-agent review round 1 incorporated (ACE digest `spec/14_META_LOOP_AND_LAYERS.md`, literature annex `spec/14_LITERATURE_ANNEX_2026-08.md`) |
| **Scope** | ACE's meta-loop and layer specification — general across ACE's projects and model platforms. The Phase-1 engine (live 2026-07-19) is the first validation; **PROJECT-V (a research project) is the second validation project**, not the target-specific architecture |
| **Name** | "AACE" in v0.1 was a naming error in the peer-agent draft — these documents specify **ACE** itself (operator ruling, 2026-08-22). No separate substrate exists |
| **Confidentiality** | Public release (Apache-2.0); instance-specific context removed |

**Change log v0.1 → v0.2** — (0) name corrected: AACE → ACE (one system); (1) activation made a first-class invariant (I13) after the observed ACE stall (2026-07-21 → 08-22: memory correct, loops never started); (2) deterministic-authority invariant (I14): models propose, validated loops record, humans decide consequential classes; (3) the meta-loop is specified as a *deterministic scheduled tick* rather than a model-driven runtime; (4) the knowledge layer bound to storage planes (content local, pointers + hashes on the control plane); (5) review depth reframed around delegation value and a finite, fatiguing human capacity; (6) cognitive-event capture restricted to workflow-observable signals, captures kept verbatim; (7) self-evolution classes A–D mapped to governance channels with evidence-tier bounds, sealed acceptance, epoch boundaries, step caps; (8) human interface specified as attention packets with typed reasons, delivered only at workflow boundaries, input through a gesture grammar; (9) socket contract field set fixed (incl. a `Propose` control decision and a verification criterion written before execution); (10) metrics made log-derived and measured, never self-reported; (11) §16 questions answered in round 1 and replaced by the round-2 list; (12) validation plan reordered: remediate the stall first. Literature behind each change: annex sections A–F.

---

## 1. Purpose

ACE is a general human–agent interaction and orchestration substrate for increasingly large, multi-project, multi-model research and engineering environments.

The central problem is not lack of agent capability. It is that, as agentic workflows, generated knowledge, project count, and autonomous activity increase, the **human cost of understanding and governing the system can grow faster than the system's useful output** — and, as the Phase-1 build showed, that a system whose memory is correct but whose activation is manual simply goes dormant.

ACE therefore treats the reduction, relocation, and productive investment of cognitive burden as a first-class design problem, and treats **activation** (what runs without being remembered) as its precondition.

The substrate should help a human:

- maintain direction across many projects without continuously reconstructing project state;
- use multiple agent/model families without inheriting their workflow fragmentation;
- distinguish meaningful conceptual progress from high-volume execution;
- capture high-impact but weakly articulated human intuitions — without inferring psychological state;
- automate repetitive review and handoff behaviors without forcing the human to remember which skill to invoke;
- preserve evidence, uncertainty, decisions, provenance, and unresolved tensions;
- identify reusable abstractions and propagate them across projects;
- adapt review depth to expected decision impact, risk, novelty — and to the human's remaining review capacity;
- allow the system itself to evolve without silently drifting into a local optimum, and without ever rewriting its own acceptance criteria.

The success criterion is not "more autonomous agents." It is a **lower marginal human cognitive cost per additional unit of useful intellectual complexity**, *measured from logs rather than reported by the human* (v0.2 — self-reported gains are miscalibrated; annex: METR 2025).

---

## 2. Core Thesis

### 2.1 Decisions, not tasks, are the primary coordination primitive

Tasks are implementation objects. ACE models the more important object:

> **Decision Event:** a bounded change in belief, commitment, priority, representation, or action policy that is supported by evidence and has consequences for future behavior.

Human and agent actions can both encode decision events. A click, interruption, rejection, repeated correction, handoff request, or spontaneous question may contain more decision information than a long generated report.

*(v0.2)* Two units coexist and must not be conflated: the **validated state transition** is the unit of *record* (audited, attributed, reversible — ACE's primitive); the **decision event** is the unit of *meaning* (alternatives, rationale, reversal condition). A decision record is the durable residue of a decision event; a transition may be recorded without a decision (auto class) and a decision may be recorded without a transition (a ruling that changes nothing yet). Tasks are not demoted: routine execution reliability remains a co-equal goal with conversion (ACE P0-A/P0-B), because the two are scored separately so that coordination cannot masquerade as progress.

### 2.2 Attention is a scarce, finite, fatiguing resource

The system optimizes not only compute, latency, or token consumption, but also:

- what deserves human attention;
- when human attention is required — **only at workflow boundaries for anything non-urgent** (v0.2; annex B: boundary delivery reaches ~52% engagement, mid-flow far less);
- at what abstraction level the human should engage;
- what can remain latent until a relevant trigger appears;
- when repeated human intervention should become an automated policy;
- *(v0.2)* how much review capacity remains in the period — reviewer reliability decays with load, so escalation is chosen against a declared weekly capacity **C**, not item by item.

### 2.3 Review is not merely verification

Review must recover information that execution logs alone do not contain:

- implicit human judgments;
- recurrent friction;
- failed or abandoned lines of thought;
- pre-articulated intuitions;
- contradictions that were repeatedly corrected but never formalized;
- new abstractions that emerged without being named;
- skills or mechanisms that were created but later stopped being activated.

*(v0.2)* The Phase-1 build showed the cheapest place to recover implicit judgment is **at input time, through a gesture grammar with an epistemic channel** (hedge = non-binding; repetition-with-compression = escalation; honest probe → adversarial routing), rather than by mining transcripts afterward. ACE keeps a cognitive review subsystem, but its primary sensor is the grammar.

---

## 3. Design Invariants

### I1. Cognitive Sustainability
The cost of understanding, supervising, and redirecting the system should grow more slowly than the useful complexity of the system. A component should be questioned if it creates a new obligation for the human to remember, inspect, or trigger it manually. *(v0.2)* Every surface carries a numeric budget and a **deletion condition**; a surface that exceeds its budget is removed, not tuned.

### I2. Representation Evolution
The system must be capable of improving the language or representation in which a problem is expressed, not only optimizing within a fixed representation. Three processes stay distinguishable: **parametric optimization** (search within a representation), **representation search** (alter concepts, decomposition, state variables, interfaces), **objective evolution** (change what is optimized). *(v0.2)* These are distinguished by *channel*, not by detection: parametric changes are parameter updates inside a frozen contract; representation changes are certified anomaly findings entering the *next* epoch; objective changes are human rulings only (§12).

### I3. Decision Traceability
Important actions must be traceable to evidence, prior state, uncertainty, rationale, agent/human source, and resulting state transition. *(v0.2)* Every transition records a hash of the prior state and is reversible as a *new* audited transition; history is never rewritten. Every write carries an actor identity (human / loop / panel).

### I4. Incremental Epistemic Evolution
Prefer *prior state + meaningful delta + affected dependencies*. Full reconstruction is reserved for integrity checks, major architectural shifts, or suspected corruption. *(v0.2)* Agents never rewrite a knowledge file wholesale: they emit itemized deltas (add / modify / retire with ids) that code merges; "context collapse" and "brevity bias" are tracked failure modes (annex C).

### I5. Adaptive Review Depth
Review depth varies with expected value: shallow health check · targeted contradiction scan · evidence audit · representation review · architecture review · strategic/portfolio review · deep adversarial reconstruction. *(v0.2)* Depth is chosen **before** the cheap pass from pre-generation signals (event type, content class, prior failure rate), on **delegation value** — P(the human would change the outcome) × cost of being wrong — not on raw uncertainty; the D0/D1 floor is deterministic recomputation, never a model.

### I6. Multi-Resolution Coherence
The human moves among strategic intent, project state, decision history, evidence, implementation, and execution traces without losing semantic continuity. *(v0.2)* The continuity object is the chain *packet → exit package → decision record → hub record → resume packet*, all stable-ID'd.

### I7. Reasoning Portability
Project and decision state are not trapped in one model, vendor, framework, or chat history. Stable sockets make heterogeneous agents substitutable. *(v0.2)* Portability is bounded by the **two-plane rule**: knowledge-bearing content lives only on the local plane; the shared control plane carries pointers + hashes. A cross-vendor socket therefore transports *paths and hashes*, and the agent on the owning machine dereferences.

### I8. Validation Before Generalization
Abstractions earn permanence through reference validation. *(v0.2)* Concretely: no new state field without three observed cases; no plugin without a measured failure; no agent where a script suffices; no primitive promoted to the core substrate until it transfers to a second, materially different project.

### I9. Asymmetric Attention Allocation
Not all projects or issues deserve equal review frequency or depth: high-leverage active fronts, stable areas needing only health checks, dormant opportunities, unresolved high-risk uncertainty, low-value work to pause or retire. *(v0.2)* Allocation is enforced by WIP limits and an attention packet of ≤3–5 items; pausing, killing, or retiring is always a human decision on a prepared brief.

### I10. Reusable Abstraction Emergence
The review process searches for transformations, representations, and policies that can be reused. *(v0.2)* Promotion is **prospective** (expected reuse over the forecast next N project slices), with a reuse-first / add-on-failure rule and a mandatory naming/documentation step before any library entry.

### I11. Activation Over Storage
A remembered skill that is never triggered is functionally absent. The system needs contextual trigger recognition and policy-based activation, not only memory retrieval. *(v0.2)* Measured, not assumed: invocation rate = invocations ÷ *applicable* sessions per skill (annex A: correctly installed skills went unused in 56% of applicable tasks in an industry eval); always-applicable procedures are inlined into the always-loaded contract, rarely-applicable ones stay gated.

### I12. Separation of Optimization and Conceptual Change
The system must explicitly detect when it is optimizing an existing solution, questioning the representation, questioning the objective, or spawning a new research question. *(v0.2)* Repeated failure inside the same framing raises the probability that the problem is representational; ≥3 rejections of the same proposal class, or ≥2 recorded edge cases on one mechanism, open a representation review.

### I13. Automated Activation *(new, v0.2)*
No loop, review, or re-annunciation may depend on a human remembering to start it. The substrate runs as a **scheduled deterministic tick**; the tick emits a **heartbeat** into the human's weekly surface so that *silence is itself an observed event*. A substrate whose dormancy is invisible has failed this invariant (the ACE stall: 32 days, nine proposals unreviewed, no loop scheduled, no signal).

### I14. Deterministic Authority *(new, v0.2)*
A model may *propose* — classification, synthesis, anomaly naming, candidate triggers, depth suggestions. Only a **validated deterministic loop records** a transition, and only a **human** decides the consequential classes (closure, ownership, strategy, objectives, privacy-sensitive actions, representation adoption). The allowed autonomy of any self-change is bounded by its **evidence tier** (formal check > executed test > external data > human judgment > model self-assessment).

---

## 4. Layered Architecture

The architecture is deliberately small at the top level. *(v0.2)* Each layer is bound to concrete stores and files in the current build; the bindings are listed so that they can be replaced without touching the layer.

### 4.1 Knowledge Layer
Stores and connects claims, hypotheses, evidence, contradictions, uncertainty, provenance, references, unresolved questions, reusable abstractions, project dependencies. Answers: *What do we currently believe, and why?*

*(v0.2)* Claims carry **bi-temporal** fields (`valid_from · valid_to · recorded_at · retracted_at`) and may hold several live hypotheses with weights; a synthesis statement without a pointer to a primary artifact is not admitted; raw captures are retained **verbatim** and interpretations are additive overlays. Graphs are derived projections computed at tick time — never sources of truth. Binding: hub records (projects, commitments, evidence) + claim records on the local plane; pointers + hashes on the control plane.

### 4.2 Decision Layer
Stores decisions, alternatives considered, assumptions, confidence, expected consequences, reversal conditions, decision owners, downstream dependencies. Answers: *What has been committed to, what remains open, and what would cause us to change course?*

*(v0.2)* Record shape: `question · options · recommendation · verdict · decided_by · reversal_condition · affects[] · evidence[]`, status lifecycle `proposed → accepted | rejected → deprecated | superseded-by`. Rationale is content (local plane); title + state + pointer is control-plane metadata. A decision without a recorded `why` is **intent debt** (§7). Binding: the open-questions registry (system decisions) mirrored into `hub/decisions/`; project decisions recorded the same way.

### 4.3 Attention Layer
Maintains human attention requests, priority, urgency, novelty, cognitive cost, interruption cost, unresolved tension, review debt, open loops, latent questions awaiting a trigger. Answers: *What deserves human cognition now, later, or not at all?*

*(v0.2)* Adds per-period **capacity C** and headroom; every deferral carries a date (shelving without expiry is structurally impossible); latent questions carry an activation condition. Binding: Today / Pending / Commitments-and-Return / Weekly views, aging rules, `no_action_before` re-annunciation.

### 4.4 Execution Layer
Planners, coding agents, retrieval agents, experiment runners, evaluators, reviewers, reporting agents, platform adapters, tools. Answers: *What operation should be performed, by which agent/tool, under which constraints?*

*(v0.2)* Execution happens in **scoped panels** (Explore / Decide / Produce / Review, each with a typed stop condition) and **deterministic loops**; the socket is a session packet in and an exit package out (§9). Binding: `packets/` → panel → `outbox/` → validator → `pending/`.

### 4.5 Autonomy / Policy Layer
Acts across all four layers; decides whether to act autonomously, ask, wait, obtain evidence, invoke another model, initiate adversarial review, escalate depth, defer, merge, branch, stop, propose an abstraction, open a research question.

*(v0.2)* Policy = **approval classes** (auto / batch / explicit) × **gesture grammar** (the human-side API) × **trigger registry** (learned activations, §12 Class A) × **depth table** (§5 of the state-machine spec). Learning from repeated corrections is allowed only as *trigger promotion through shadow mode*; the policy layer never changes an approval class or an objective.

---

## 5. Review Subsystem

5.1 **Execution review** — was the action performed correctly? *(v0.2)* Completion is a deterministic state check (file exists, hash changed, test passed), never the agent's own claim; confident closing language is a risk feature.
5.2 **Evidence review** — supported, current, relevant, reproducible? *(v0.2)* Invalidating one claim opens review debt on its dependents (cascading invalidation).
5.3 **Epistemic review** — did confidence change appropriately; were alternatives suppressed? *(v0.2)* Multi-agent output is checked for **fact survival** (did critical claims disappear while agreement rose?) and for agreement at the premise level, not only the answer level.
5.4 **Cognitive review** — which human judgments were implicit? *(v0.2)* Primary sensor = the gesture grammar's epistemic channel; secondary = repetition detectors over the event log. Affective signals are excluded.
5.5 **Attention review** — where is attention spent repeatedly; which recurring actions should become triggers? *(v0.2)* Measured by invocation rate per applicable session, Ask-F1, and oversight time by type (a-priori / co-plan / live / post-hoc).
5.6 **Representation review** — is the representation still appropriate? *(v0.2)* Entered by the triggers in I12; run by the anomaly-mining side-loop outside the frozen contract; adopted only at an epoch boundary.
5.7 **Infrastructure review** — what is reused; what exists but is never activated; which patterns create state or token debt? *(v0.2)* A separate **library-time loop** computes per-skill health (last_used, success, failure, conflicts, validation status) and proposes prune / deprecate / merge as tick-able items; scope is the substrate's own inventory.
5.8 **Strategic / portfolio review** — marginal-value allocation, pause, infrastructure, publication, product, dependency. *(v0.2)* Always a human ceremony on a prepared brief; the system ranks, never decides.

*(v0.2)* Two structural rules for every review: the **reviewer's model family must differ from the producer's** (self-preference survives rubrics; models that both err agree ~60% of the time), and reviewers with high detection but poor correction are constrained to **flag-only** roles (raise debt, never rewrite). High-impact reviews add a **critic-of-the-review** with an explicit disagreement prompt.

---

## 6. Review Cadence

Nested cadences, **event-driven first**:

- **Event-driven** — failed verification; contradiction; repeated human correction; unexpectedly high cost; major uncertainty change; new reusable abstraction; architecture-boundary crossing; new research question; *(v0.2)* a named constraint's tolerated violation rate exceeded (e.g., "no commitment silently closed", "no pending item older than 14 days unflagged"); heartbeat missing.
- **Tick** *(v0.2)* — every 30 minutes while logged in and once at 07:00: observe, interpret deterministically, fire returns and aging, regenerate projections, run constraint checks, emit heartbeat. The 07:00 run is also where consolidation belongs (offline reasoning between sessions is cheaper than at query time).
- **Session / milestone** — integrate deltas; close or carry open loops; capture decisions; identify reusable transformations; identify deferred cognitive questions. *(v0.2)* Non-urgent agent output is delivered here, at the boundary, never mid-flow.
- **Weekly** — portfolio health and drift: active fronts, open debt, recurring friction, under-triggered tools, repeated review actions that should become policy. *(v0.2)* ≤20 minutes, ≤5 decisions, one simplification; the weekly surface shows the heartbeat and the debt line.
- **Monthly / bimonthly deep meta-review** — architecture, representation quality, cross-project coherence, autonomy policy, external frontier comparison, commercialization/publication, invariant failures or new invariants. *(v0.2)* A **ceremony**: a generated brief, ≤5 decisions, output = decisions and policy changes only. It reuses the weekly slot once a month — no new surface.

---

## 7. Open Debt

Any unresolved state that consumes future cognitive or computational resources: unverified claims; unintegrated handoffs; ambiguous project state; pending contradictions; repeated manual review actions; stale skills; unmerged branches; untested assumptions; interfaces needing human translation; unresolved representation problems; *(v0.2)* **intent debt** — decisions, goals, or constraints whose rationale was never recorded; dependents of an invalidated claim; shadow triggers awaiting verdict.

Open debt is detected, typed, costed, impact-scored, and scheduled. *(v0.2)* It is a **projection computed at tick time** over existing records — never a table the human maintains — shown as one line ("N items, oldest X days, est. cost") and burned down by the same ticks that create it. "Intentionally ignored" debt still carries a date.

---

## 8. Human Interface

Do not expose internal graphs directly; present cognitively useful projections. *(v0.2)* At most six stable views; a new view must replace one and demonstrate reduced burden. **Input** is a gesture grammar (tick = accept; strike = reject; reorder = priority; move = state transition; `@date` = hold; `@name` = waiting-for; one-token verdicts on numbered queues; silence = defer) — the same grammar on every surface.

8.1 **Attention view** — "What deserves me now?" 3–5 items, each with `why-now · consequence-of-delay · typed reason (input ambiguous / policy underspecified / evidence missing) · recommended action · what proceeds automatically`. *(v0.2)* Goal-type questions surface immediately; input-type questions queue to the next boundary.
8.2 **Decision view** — open/reversible decisions with alternatives, evidence, uncertainty, consequences, reversal trigger. *(v0.2)* Accepts complementary verdicts ("this option is definitely wrong") as first-class answers.
8.3 **Landscape view** — concept-centered portfolio change. *(v0.2)* Epoch-2; must replace an existing view.
8.4 **Trajectory view** — compressed causal/decision timeline, not a transcript. *(v0.2)* Derived from the transition log with progressive disclosure (one line → paragraph → diff).
8.5 **Representation view** — current representation, anomalies, competing representations, newly emerged abstractions. *(v0.2)* Epoch-2; fed by certified anomaly findings and edge cases.

The human should rarely need raw execution traces unless a review escalates.

---

## 9. Agent/Model Sockets

A socket defines: input state contract; allowed tools; expected output schema; evidence/provenance requirements; confidence format; failure format; token/cost budget; handoff semantics; verification expectations; whether the agent may mutate shared state.

*(v0.2)* Fixed field set. **Input**: objective · panel type and stop condition · state slice as *paths + hashes* · allowed tools · **mutable regions** (explicit delimiters; everything else read-only) · budgets · **verification criterion written before execution** · autonomy level expressed as the human's role per action class. **Output**: one of the control decisions **Propose / Act / Ask / Refuse / Stop / Confirm / Recover** · conclusions as candidates with verbatim evidence and serials (code adjudicates precedence) · uncertainty · contradictions · `proposed_state_delta` · `reusable_assets` · `unresolved_questions` · `failure_modes` · typed escalation reason · `recommended_next_transition` · model family · provenance. Every state element is stamped with six axes: authority · scope · mutability · provenance · reversibility · licensed actions.

`mutation_permissions` ≡ a declared write boundary on the content plane. **Canonical state mutation is never grantable to an agent.** Roles: planner, explorer, coding/execution agent, evidence verifier, adversarial reviewer, representation critic, critic-of-the-review, synthesis agent, policy/meta-review agent. Identity is secondary to role contract; the cross-vendor transport may map 1:1 onto a published task lifecycle (SUBMITTED → WORKING → INPUT_REQUIRED → COMPLETED / FAILED / CANCELED).

---

## 10. Core Meta-Loop

**Observe → Interpret → Detect Tension → Prioritize → Select Depth → Delegate → Execute → Verify → Integrate → Review Representation → Update Attention → Update Policy → Stop / Branch / Recur**

*(v0.2)* The loop is implemented as a **deterministic scheduled tick** over records, not as a resident model-driven runtime. Model calls occur only at *Interpret* (classification of ambiguous input) and *Review Representation* (naming an anomaly), and both return proposals into the validation path. Prioritize and Select Depth are **table lookups over record fields** until enough outcomes exist to calibrate a score. The tick is idempotent (writes nothing when nothing changed), bounded (< 10 s), and emits a heartbeat.

---

## 11. Cognitive Event Capture

Idea density is not proportional to token frequency. Signals: repeated correction; strong interruption; sudden reframing; contradiction with established direction; new question outside the original objective; recurrent manual behavior; repeated invocation of the same review pattern; a low-frequency phrase associated with a large downstream decision; *(v0.2)* a boundary change (project · decision · artifact · surface) as the deterministic event delimiter; the binding status of the human's own words (hedge lexicon = non-binding; paste = reference by default; repetition-with-compression = escalation dial; honest probe = stress-test request).

*(v0.2)* Removed: hesitation, "mumbled exploration", semantic discontinuity, or any affective inference — the detector identifies workflow-relevant interaction signals only. Captures are stored **verbatim**; interpretations are overlays pointing at the raw span. Implicit signals are hypotheses flagged `noisy`; they change nothing until repeated ≥3 times or explicitly confirmed. Candidate events may stay latent until context accumulates; the buffer lives on the content plane with stub-only mirroring.

---

## 12. Self-Evolution Mechanism

Self-evolution is decomposed into controlled update classes with channels, not merely verification strength:

| Class | Examples | Channel *(v0.2)* | Required evidence tier | Approval |
|---|---|---|---|---|
| **A** parameter / policy tuning | agent choice, thresholds, review depth, retry count, tool budget, **trigger promotion** | loop configuration inside the frozen contract; shadow-mode comparison | executed test or external data | batch — a human tick |
| **B** workflow mutation | insert verifier, add adversarial branch, reorder, add event trigger, add a registry mechanism | epoch mutation: ≤3 per epoch, each with observed failure · fewer cognitive operations · no new surface · pass/fail test · deletion condition · no evaluator degraded | executed test | epoch human gate |
| **C** representation mutation | new state primitive, change project abstraction, split/merge classes, redefine evidence object | certified anomaly finding → **next** epoch's contract; ≥3 anomalies the current representation cannot explain; similarity pre-filter; author-anchored comparison; falsifiable prediction of which metric moves; migration + rollback plan; transfer test on a second project | deterministic check + human judgment | human ruling at the epoch boundary |
| **D** objective mutation | change optimization target, elevate an invariant, redefine success | human ruling only; forbidden inside an epoch; criteria pinned by hash within an epoch | human | explicit |

*(v0.2)* Governance rules for every class: **Propose → Evaluate → Commit → Serve**, with Commit the only state-writing step; the acceptance gate is **sealed** (pre-registered criteria outside the proposer's reach; prior version retained); superseded versions stay addressable (archive, not lineage); consecutive unaudited self-changes are capped and review depth rises with steps since the last grounded verification; four drift pathways (prompt/policy, accumulated memory, created tools, workflow graph) each get a meta-review check; the evaluator is never edited by the thing it evaluates.

---

## 13. Reference Validation

*(v0.2)* The **Phase-1 build** (July 2026: validator, accept/reject, audited rollback, views, clarify loop, gesture watcher, planning panel) is the first validation: it supplied the invariants I13–I14, the gesture grammar, the hard gates, the two-plane storage rule, and the first recorded stall. **PROJECT-V** is the second validation project because it exposes hypotheses, observable evidence, competing mechanisms (e.g., a recorded non-sequitur between two of the project's claims), explicit uncertainty, experimental verification, project-state transitions, and reusable reasoning patterns — the claim/contradiction material the productivity use lacks.

> No substrate feature should exist solely because one validator needs it unless it is clearly marked as a project adapter. A primitive becomes core to the spec only after it transfers to a materially different project.

PROJECT-V adapter rules: read the project root as read-only reference; record claims and decisions on the content plane; pointers + hashes on the control plane; replay from project files first (session transcripts only by explicit ruling).

---

## 14. Success Metrics

Avoid task throughput or token efficiency alone. *(v0.2)* Every metric below is derived from the event log and gesture timestamps; none is self-reported.

| Metric | Definition | Derivation |
|---|---|---|
| **Cognitive Return on Attention (CRA)** | useful decision/knowledge change per unit of human attention | decisions + accepted transitions ÷ minutes of hub-edit time |
| **State Reconstruction Cost** | effort to understand current state after absence | time from packet open to first gesture; gate: 7-day gap resumed < 10 min |
| **Activation Recall** | fraction of relevant skills/policies surfaced when needed | shadow-trigger true-positive rate; invocations ÷ applicable sessions |
| **Review Yield** | fraction of review cycles producing a decision, corrected belief, abstraction, or policy change | decisions recorded ÷ ceremonies held |
| **Reuse Yield** | downstream applications per abstraction | reuse events in evidence records; per-skill transfer matrix |
| **Open-Debt Burn Rate** | debt retired vs created | projection deltas per week |
| **Representation Gain** | explanatory power, compression, prediction, coordination, transfer | anomalies explained; transfer test outcome |
| **Cognitive Scaling Ratio** | growth of oversight burden vs growth of complexity | slope of (weekly hub minutes ÷ active records) over months; target ≤ 0 |
| **Ask-F1** *(new)* | precision of agent questions × recall of true blockers | logged questions vs post-hoc blockers |
| **Headroom** *(new)* | remaining review capacity in the period | C − escalations routed to the human |
| **Extraneous load** *(new)* | attention spent off the current task node | model-initiated context switches per session |

The long-term objective remains a sublinear Cognitive Scaling Ratio.

---

## 15. Explicit Non-Goals

ACE is not: another dashboard humans must maintain; a large static ontology; a universal agent framework replacing every platform; a transcript warehouse; an autonomous system whose self-modification is unaudited; a monthly reporting engine producing prose without decisions; a collection of skills requiring the human to remember when to call them; *(v0.2)* **a system whose loops must be started by hand**; a judge of its own novelty (novelty of abstractions is decided by a human on structural pre-filters — model judges reward fluent restatement); a store of affective inferences about the human.

---

## 16. Questions for Reference Agents

### 16.1 Round 1 — answered (2026-08-22; full text in `spec/14` §7)

1. *Emergence vs local optimization* — structural tests, not judges: pool-manipulation axioms, author-anchored reference, similarity rejection before review, prospective reuse; verdict stays human.
2. *Trigger learning* — repetition ≥3 or explicit confirmation; shadow mode 14 days; promote at precision ≥70%; ≤10 live triggers; retire after 30 days without a true positive; promotion never changes an approval class.
3. *Review-depth allocation* — delegation value under a declared capacity C; decide before the cheap pass; two thresholds on one weak-verifier score; deterministic D0/D1 floor; escalate only on model–record disagreement.
4. *Cognitive-event detection* — workflow-observable boundaries; verbatim capture with overlays; gesture grammar as sensor; no affective inference.
5. *Minimal socket* — §9 field set; Propose added to the control decisions; knowledge slice as paths + hashes.
6. *Representation-mutation threshold* — ≥3 unexplained anomalies + falsifiable prediction + rollback + transfer test; only at an epoch boundary.
7. *Self-evolution* — §12 table with evidence-tier bounds, sealed gate, step cap.
8. *Sublinear scaling* — §14 metric set, timed from logs; activation automated; packets bounded; delivery at boundaries.
9. *Reusable transformation extraction* — recurrence counts, transfer matrix, per-task-class effects, practise-before-promote, AutoDoc, descendant-outcome scoring.
10. *Failure modes* — compression, aggregated confidence, excessive autonomy — plus two omitted in v0.1: the overseer's own confirmation bias and fatigue, and **activation failure** (silence invisible to an unactivated review).

### 16.2 Round 2 — open

1. **Capacity estimation** — how does a single overseer estimate their own review capacity C and its decay without a labelled set? Candidate: infer from gesture-latency and revert-rate trends.
2. **Novelty without a judge** — can a deterministic pre-filter (similarity, author-anchored delta, anomaly count) be tight enough that the human verdict is rarely needed, without suppressing genuine reframings?
3. **Transfer test design** — what is the minimum second-project evidence that justifies promoting a PROJECT-V-derived claim/contradiction primitive to core?
4. **Heartbeat semantics** — what is the right escalation when the heartbeat itself is missing (mail? calendar? a morning voice brief?), given that every such channel is a new surface?
5. **Decision records for project work** — do researchers actually record reversal conditions, or only verdicts? What is the minimal record that still enables cascading invalidation?
6. **Intent-debt detection** — can "decision without rationale" be detected deterministically from records, or does it require a model pass?
7. **Two-plane sockets across vendors** — what breaks when a remote agent holds only hashes and must ask the owning machine to dereference?

---

## 17. Near-Term Validation Plan

1. *(v0.2, first)* **Remediate the stall**: one scheduled deterministic tick (I13) with heartbeat; first run against the 32-day-old pending items; record the first activation metrics.
2. Implement decision records and the attention-packet fields in the existing views (replace, do not add).
3. Implement the trigger registry in shadow mode; first shadow run = dormancy audit of the substrate's own loops and skills.
4. Build the PROJECT-V adapter (read-only root, content-plane records); replay selected historical episodes from project files; compare state reconstruction cost, decisions recovered, debt surfaced, abstractions identified, attention requests, false-positive cognitive events.
5. Run the same core substrate against one materially different project (a proposal or a second research project); remove any "general" primitive that fails to transfer.
6. Hold the first monthly ceremony (≤5 decisions); send invariant and transition failures back into the meta-review loop.
7. Only then consider Epoch-2 contract candidates: representation review as a state, landscape/representation views, reuse extraction, the metric set as gates.

---

## 18. Current North Star

> **Increase the amount of coherent, reusable, verifiable intellectual work that a human can direct while making the marginal cognitive cost of additional complexity grow as slowly as possible.**

The substrate preserves human direction while allowing machine-managed continuity. The desired end state is not a system that remembers everything. It is a system that reliably **activates the right evidence, representation, question, review depth, agent, and human attention at the moment they become consequential** — *and that keeps running, visibly, when no one is looking at it.*
