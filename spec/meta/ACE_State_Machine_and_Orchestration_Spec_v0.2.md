# ACE State Machine and Orchestration Specification
## Cross-Platform Recurring Workflow

| | |
|---|---|
| **Version** | **0.2** |
| **Date** | 2026-08-22 |
| **Supersedes** | v0.1 — `reference materials/AACE_State_Machine_and_Orchestration_Spec.md` (not included in the public release; received 2026-08-22, sha256 `b5afc781…67ea4`; frozen, never edited) |
| **Status** | Implementation-oriented draft; companion to `ACE_Epistemic_Operating_Substrate_Handoff_v0.2.md` |
| **Validation** | Phase-1 engine (live 2026-07-19; dormant 2026-07-21 → 08-22 — the stall this version remediates) · PROJECT-V (the second research validation project) |
| **Name** | "AACE" in v0.1 was a naming error — this specifies **ACE** itself (operator ruling, 2026-08-22) |
| **Primary constraint** | General and portable across projects and model platforms; **deterministic authority** (models propose, loops record, humans decide) |

**Change log v0.1 → v0.2** — (0) name corrected: AACE → ACE (one system); (1) runtime is a scheduled deterministic tick (§1, §19), not an expected-value runtime; (2) canonical state fields tagged core vs candidate under the three-observed-cases rule; bi-temporal claim fields (§2); (3) new events: `Heartbeat`, `HeartbeatMissing`, `WouldFire`/`Fired`, `ModelUpgraded`, `ConstraintViolated`, `InvalidationCascade`; human interrupts typed addition / revision / retraction (§3); (4) cognitive-event detector restricted to workflow-observable signals; boundary rule; `noisy` flag (§4); (5) S4 and S5 are table lookups; S5 depth table bound to deterministic triggers; S8 gains `uncertain` → second verifier of a different model family; S9 gains `activation_failure`; S10 records debt created/closed and reusable assets (§5–§11); (6) representation review gains pre-filters and a threshold; objective review is epoch-boundary only with a goal-adherence probe (§12–§13); (7) attention packet fields and boundary delivery (§14); policy update = trigger promotion only (§15); meta-review = constraint checks + ≤5-decision ceremony (§16); stopping policy gains a step cap and a wrong-action budget (§17); (8) DepthScore deferred in favour of the table (§20); trigger-learning thresholds fixed (§21); reuse ladder gains transfer matrix and prospective scoring (§22); disagreement protocol hardened (§23); MVI reordered around the tick (§25); PROJECT-V protocol scoped to project files (§26); failure modes extended (§27); invariant checks extended to I13–I14 (§28). Literature: `spec/14_LITERATURE_ANNEX_2026-08.md`.

---

## 1. Runtime Model

ACE is an **event-driven state graph executed by a scheduled deterministic tick**, not a fixed linear chain and not a resident model-driven runtime.

On every tick the runtime evaluates, *by table lookup over record fields*:

> Given the current epistemic state, decision state, attention state, execution state, and budget, which transitions are due, which proposals are ready for a human verdict, and which constraints are violated?

The graph may revisit earlier states, branch, suspend work, escalate review, or terminate. Model calls are made only from INTERPRET (ambiguous classification) and REPRESENTATION_CHECK (anomaly naming), and only to produce proposals that re-enter through the validation path. A tick that finds nothing to do writes nothing except its heartbeat.

---

## 2. Canonical State Object

Every project or research thread exposes a compact canonical state. *(v0.2)* Fields are **core** (three observed cases in the Phase-1 build) or **candidate** (adopted only when three cases are logged). Knowledge-bearing content lives on the local plane; the control plane holds pointers and hashes.

```yaml
state:
  scope:                         # core
    project_id:
    objective:
    current_phase:
    reference_adapter:

  knowledge:                     # candidate except evidence[]
    claims: []                   # each: id, text_ptr, hypotheses: {h: p}, valid_from, valid_to,
                                 #       recorded_at, retracted_at, evidence_ids[], depends_on[]
    hypotheses: []
    evidence: []                 # core: artifact ptr + sha256, proof location, status, project, date
    contradictions: []           # each: claim_a, claim_b, status: open|resolved, opened_by
    unresolved_questions: []     # each: text, activation_condition
    confidence_map: {}

  decisions:                     # core (decision record shape)
    open: []                     # question, options[], recommendation, decided_by?, reversal_condition,
    committed: []                #   affects[], evidence[], status: proposed|accepted|rejected|deprecated|superseded_by
    reversible: []
    reversal_conditions: []

  attention:                     # core: human_required, latent; candidate: costs
    human_required: []           # each: item, why_now, consequence_of_delay, typed_reason, requested_action
    latent_questions: []         # each: question, activation_condition
    recurring_friction: []
    capacity_C:                  # declared weekly human review capacity (minutes or items)
    headroom:
    urgency:
    novelty:
    cognitive_cost:
    interruption_cost:

  representation:                # candidate (Epoch-2)
    current_model:
    unresolved_anomalies: []     # each: observed, recorded_at, mechanism, edge_case_id
    candidate_abstractions: []
    competing_representations: []

  execution:                     # core
    active_tasks: []
    pending_tools: []
    failures: []
    artifacts: []
    budgets:
      token:
      compute:
      wall_time:
      human_attention:

  debt:                          # core — a PROJECTION, recomputed each tick, never hand-maintained
    open_items: []               # typed: unverified_claim | unintegrated_handoff | ambiguous_state | pending_contradiction
                                 #        | repeated_manual_action | stale_skill | untested_assumption | intent_debt
                                 #        | invalidated_dependent | shadow_trigger_awaiting_verdict
    debt_score:
    projected_cost:

  policy:                        # core
    autonomy_level:              # human role per action class: operator|collaborator|consultant|approver|observer
    approval_classes:            # auto | batch | explicit — fixed; never changed by the policy layer
    depth_table_version:
    escalation_thresholds:
    agent_selection_policy:
    stopping_policy:
    live_triggers: []            # ≤10; each: condition, action, promoted_on, precision, last_true_positive

  provenance:                    # core
    last_updated:
    sources: []
    transitions: []              # each: event, from, to, actor, prev_state_sha256, commit
    heartbeat_last:
```

Concrete storage: plain files + git in the current build (event log as the single source of truth; every human-readable view regenerated from it). A graph store or database may be used only as a derived index.

---

## 3. Core Event Types

All important updates enter through events. *(v0.2)* Every event carries `actor ∈ {human, loop, panel:<id>}` and a timestamp; human events map 1:1 onto the gesture grammar.

### 3.1 Human Events

```yaml
HumanIntent                # launch / scope (paste-back of a kickoff, one-liner)
HumanCorrection            # "not X, Y" — surgical re-anchor
HumanInterruption          # typed: addition | revision | retraction   (v0.2)
HumanApproval              # tick / "1" / "go" on a presented referent
HumanRejection             # strike
HumanDeferral              # @date  — no_action_before                (v0.2)
HumanPriorityShift         # reorder / move
HumanQuestion
HumanHandoffRequest
HumanBlindSpotRequest
HumanAdversarialReviewRequest   # honest probe
HumanUncertainIntuition    # hedge lexicon — non-binding by definition (v0.2)
HumanComplementaryVerdict  # "this option is definitely wrong"        (v0.2)
```

### 3.2 Agent Events

```yaml
PlanGenerated
EvidenceFound
EvidenceConflict
ExecutionSucceeded         # only after a deterministic state check     (v0.2)
ExecutionClaimedComplete   # agent's own claim — a risk feature, not a transition (v0.2)
ExecutionFailed
VerificationPassed
VerificationFailed
VerificationUncertain      # → second verifier, different model family (v0.2)
NewHypothesis
NewAbstractionCandidate
RepresentationConflict
BudgetWarning
AgentDisagreement          # carries a disagreement map, not a winner  (v0.2)
```

### 3.3 System Events

```yaml
Tick                       # (v0.2)
Heartbeat                  # (v0.2) written to the weekly surface every tick
HeartbeatMissing           # (v0.2) raised by the next observer if a tick is overdue
ScheduledReview
ReturnDue                  # no_action_before reached                  (v0.2)
OpenDebtThresholdExceeded
PendingAged                # 7 d / 14 d aging                          (v0.2)
StaleStateDetected         # human-attributable signals only
RepeatedActionDetected
TriggerCandidateDetected
WouldFire / Fired          # shadow vs live trigger                    (v0.2)
ConstraintViolated         # named constraint past tolerated rate      (v0.2)
InvalidationCascade        # claim invalidated → dependents open debt  (v0.2)
ModelUpgraded              # reopens verification suites               (v0.2)
CrossProjectReuseCandidate
InvariantViolation
StateCorruptionSuspected
ExternalFrontierDelta
```

---

## 4. Cognitive Event Extraction

A lightweight detector for workflow-relevant human interaction patterns. *(v0.2)* It observes **behaviour in the workflow**, never affect; it never guesses a binding.

Candidate conditions:

```text
repeated_correction                 (same correction ≥ 3 times)
repeated_manual_trigger             (same skill/loop hand-invoked ≥ 3 times after the same event type)
strong_rejection
unexpected_reframe
new_question_outside_scope
repeated_handoff_pattern
repeated_blind_spot_request
repeated_adversarial_review_request
high_impact_low_frequency_statement
boundary_change                     (project | decision | artifact | surface changed)   (v0.2)
binding_status_marker               (hedge | paste-as-reference | escalation-by-repetition | honest probe) (v0.2)
```

Removed in v0.2: `persistent_hesitation_or_tension`, `semantic_discontinuity` (affective or psychological inference — forbidden).

Candidate events enter a buffer on the content plane (stub mirrored):

```yaml
cognitive_event:
  observation:                 # verbatim span pointer — never a paraphrase
  possible_meaning:
  confidence:
  noisy: true|false            # implicit signals start noisy; cleared by repetition ≥3 or explicit confirmation
  related_state:
  urgency:
  requires_human_interpretation:
  suggested_future_trigger:
```

Low-confidence items remain latent. A `noisy` event changes no policy.

---

## 5. State Machine

### S0 — IDLE / WAIT
No high-value transition is justified. **Exit triggers:** new human input; `Tick`; agent result; contradiction; budget threshold; trigger activation; external delta.

### S1 — OBSERVE
Collect the smallest relevant delta: human gestures (diff of the hub against the engine's last baseline — any diff is human by definition), inbox captures, agent exit packages, clock (returns due, pending age, at-risk projects), changed artifacts (hash manifest), external frontier updates. **Output:** normalized events. → `INTERPRET`

### S2 — INTERPRET
Map events onto state. Deterministic marks are applied directly; anything ambiguous becomes a **one-line clarify proposal**, never a guess. Questions: what changed; which claims, decisions, dependencies, attention items are affected; routine or conceptual; cognitive-event candidate?
Transitions: routine delta → `PRIORITIZE` · contradiction → `VERIFY` · unclear → `CLARIFY_OR_WAIT` · representation anomaly → `REPRESENTATION_REVIEW` · high-risk → `ESCALATE`.

### S3 — DETECT_TENSION
Structural in v0.2 (no model): commitment closed without evidence; record `current` while a newer validated package is pending; return date passed; decision whose reversal condition fired; repeated rejection of the same proposal class; repeated `validation_failed` with the same error; constraint past its tolerated violation rate; agreement among agents with low premise overlap; heartbeat missing.

```yaml
tension:
  type:
  severity:
  uncertainty:
  downstream_scope:
  human_attention_needed:
```
→ `PRIORITIZE`

### S4 — PRIORITIZE
*(v0.2)* A **table over record fields**, not a utility function, until outcomes exist to calibrate one:

| Rank | Condition |
|---|---|
| 1 | explicit-class item with a due date or a fired reversal condition |
| 2 | constraint violation; heartbeat missing |
| 3 | goal-type open question (value decays fastest) |
| 4 | pending item aged ≥ 7 d; project at-risk |
| 5 | batch-class proposals ready for a tick |
| 6 | input-type open questions (queue to the next boundary) |
| 7 | shadow-trigger reports; debt line |

The conceptual utility function of v0.1 (decision impact + information gain + reuse value + risk reduction + debt reduction + burden reduction − token − compute − attention − interruption) is retained as the **target** for calibration; its terms are logged on each record as proposals until then. Ranked output carries the proposed depth and whether human attention is required.

### S5 — SELECT_DEPTH
*(v0.2)* Bound to deterministic triggers; D0 exists only for the auto class.

| Depth | Meaning | Bound to | Deterministic trigger |
|---|---|---|---|
| D0 | continue | auto class | existence / pointer / deterministic date |
| D1 | integrity check | validator gates (schema, content class, source scope, sync) | every exit package |
| D2 | targeted verification | tests; recomputation; second-model check | shipped-artifact claims; commitment closure |
| D3 | adversarial | epoch attack roles; structured disagreement; critic-of-review | explicit class: kill / handoff / transfer / strategy |
| D4 | representation review | anomaly-mining side-loop → certified finding | ≥3 rejections of one proposal class; ≥2 edge cases on one mechanism; repeated identical validation failures |
| D5 | architectural / strategic | epoch + human ruling | frozen-test failure; monthly ceremony |

Escalation to the human is decided **before** any cheap pass, on **delegation value** (P(outcome changes) × cost of being wrong) against remaining capacity C. → `DELEGATE`

### S6 — DELEGATE
Choose role / model / tool per socket contract (§6). Routing policy:

```text
planning / decomposition       -> planner
repo-level implementation      -> coding agent
claim verification             -> evidence verifier (different model family from the producer)
failure analysis               -> debugger / reviewer
blind-spot search              -> adversarial reviewer
high-impact review             -> reviewer + critic-of-the-review
cross-project synthesis        -> synthesis agent
representation challenge       -> representation critic
policy change                  -> meta-review agent (proposals only)
```

The selected model is a replaceable detail; per-(task class, model) outcome statistics may steer routing once enough delegations exist. Output must comply with the socket.

---

## 6. Agent Socket Contract

### Input
```yaml
agent_request:
  role:
  panel_type: explore|decide|produce|review     # with its typed stop condition      (v0.2)
  objective:
  relevant_state_slice:        # paths + sha256 — content is dereferenced on the owning machine (v0.2)
  explicit_constraints:
  evidence_requirements:
  allowed_tools:
  mutable_regions: []          # explicit delimiters; everything else read-only         (v0.2)
  token_budget:
  stop_conditions:
  mutation_permissions:        # ≡ declared write boundary on the content plane; canonical state: never
  verification_criterion:      # written BEFORE execution                              (v0.2)
  autonomy_level:              # human role per action class                           (v0.2)
  expected_output_schema:
```

### Output
```yaml
agent_result:
  control_decision: Propose|Act|Ask|Refuse|Stop|Confirm|Recover   # (v0.2)
  status:
  conclusions: []              # candidates with verbatim evidence + serials; code adjudicates precedence (v0.2)
  evidence: []                 # pointers + hashes
  sources_seen: []
  sources_not_seen: []         # mandatory — partial-observability rule
  uncertainty:
  escalation_reason: input_ambiguous|policy_underspecified|evidence_missing|none   # (v0.2)
  contradictions: []
  proposed_state_delta:
  reusable_assets: []
  unresolved_questions: []
  failure_modes: []
  recommended_next_transition:
  model_family:                # reviewer family must differ from producer family  (v0.2)
  provenance:
```

No agent rewrites canonical state. Every socket carries a small regression suite (procedure + expected artifact) re-run on `ModelUpgraded`.

---

## 7. EXECUTE

### S7 — EXECUTE
Code; retrieve; analyze; simulate; experiment; compare; summarize delta; generate proof; inspect failure; update artifact — inside the mutable regions only. Transitions: success (state check) → `VERIFY` · failure → `FAILURE_ANALYSIS` · budget exceeded → `BUDGET_REVIEW` · conceptual anomaly → `REPRESENTATION_REVIEW`.

---

## 8. VERIFY

### S8 — VERIFY
Depth-dependent checks: deterministic tests and recomputation (D1–D2 floor); independent model review from a different family; evidence triangulation; reproducibility; adversarial critique; logical and dependency consistency; requirement satisfaction. Completion claims are never accepted on the agent's text.

```yaml
verification:
  status: pass | fail | uncertain
  confidence:
  unsupported_claims: []
  contradictions: []
  detected: true|false               # (v0.2) detection and correction scored separately
  corrected_correctly: true|false|unknown
  rerun_needed:
```
Transitions: pass → `INTEGRATE` · fail → `FAILURE_ANALYSIS` · **uncertain → second verifier of a different model family**, then `SELECT_DEPTH` if still uncertain.

---

## 9. FAILURE ANALYSIS

### S9 — FAILURE_ANALYSIS
Classes: `execution_failure · tool_failure · evidence_failure · reasoning_failure · coordination_failure · representation_failure · objective_failure · state_failure · activation_failure` *(v0.2: the loop that should have fired did not; detected by heartbeat or by a human doing what a loop owns)*.

A repeated failure inside the same framing raises the probability that the problem is representational. Transitions: local correction → `DELEGATE` · conceptual → `REPRESENTATION_REVIEW` · corrupted state → `RECONSTRUCT_STATE` · objective invalid → `OBJECTIVE_REVIEW` (human) · activation → schedule the missing loop, record the edge case.

---

## 10. INTEGRATE

### S10 — INTEGRATE
Apply a verified delta. Rules: preserve prior state (snapshot hash); record the causal transition; update affected dependencies only; create open debt for unresolved issues; record reusable assets; update confidence; one attributed commit per transition.

```yaml
transition_record:
  from_state:
  event:
  action:
  actor:
  evidence:
  decision_id:
  delta:
  affected_nodes:
  confidence_change:
  open_debt_created: []
  open_debt_closed: []
  reusable_assets: []
  prev_state_sha256:
  timestamp:
```
→ `REPRESENTATION_CHECK`

---

## 11. REPRESENTATION CHECK

### S11 — REPRESENTATION_CHECK
Deterministic counters: anomalies accumulated on one mechanism; rejections of one proposal class; agents translating the same concept differently (premise-overlap score); a human repeatedly correcting the *framing* rather than the answer; a one-off transformation that recurred k times. Outcomes: no conceptual change → `ATTENTION_UPDATE` · candidate abstraction (thresholds in S5 D4) → `REPRESENTATION_REVIEW` · objective challenge → `OBJECTIVE_REVIEW`.

---

## 12. REPRESENTATION REVIEW

### S12 — REPRESENTATION_REVIEW
Pre-filters *(v0.2)*: similarity rejection against the existing library (near-duplicates are logged and dropped before review); an **author-anchored reference** (the human's own prior framing) in the comparison set; novelty scored on a separate source-boundedness axis. Compare at least: current; minimally modified; one genuinely alternative framing. Criteria: compression · explanatory power · predictive value · decision value · transferability · human cognitive cost · implementation cost · traceability.

```yaml
representation_proposal:
  current:
  proposed:
  anomalies_explained: []        # ≥ 3 that the current representation cannot explain   (v0.2)
  information_lost:
  expected_gain:
  falsifiable_prediction:        # which observable metric moves, by how much           (v0.2)
  affected_projects:
  migration_cost:
  rollback_plan:
  transfer_test:                 # second project on which it must also hold           (v0.2)
```
A mutation produces a proposal, never an overwrite; superseded representations stay addressable. Transitions: accept (human, epoch boundary) → `INTEGRATE_REPRESENTATION` · reject → `ATTENTION_UPDATE` · uncertain → `ADVERSARIAL_REVIEW`.

---

## 13. OBJECTIVE REVIEW

### S13 — OBJECTIVE_REVIEW
Rare; **forbidden inside an epoch**; entered only at a scheduled boundary with the epoch's criteria pinned by hash. Triggers: persistent inability to improve; discoveries invalidate the goal; an emergent opportunity dominates; invariant conflict; human priority shift; *(v0.2)* a fixed goal-adherence probe set shows drift.

```yaml
objective_change:
  current_objective:
  proposed_objective:
  why:
  evidence:
  tradeoffs:
  downstream_effects:
  reversibility:
```
Objective changes require explicit human approval — always.

---

## 14. ATTENTION UPDATE

### S14 — ATTENTION_UPDATE
Recalculate what the human should see; what stays autonomous; what is deferred; which latent questions activated; whether a repeated manual action should become a trigger candidate. Compress to a decision surface of ≤3–5 items; deliver non-urgent items only at a workflow boundary; respect capacity C.

```yaml
attention_packet:
  heartbeat: <timestamp of this tick>
  now:
    - issue:
      why_now:
      consequence_of_delay:
      typed_reason: input_ambiguous|policy_underspecified|evidence_missing|decision_due
      requested_human_action:          # one token where possible; complementary verdicts accepted
  automatic:
    - action:
      reason:
  latent:
    - question:
      activation_condition:
  debt_line: "N items · oldest X d · est. cost"
  headroom: <C − escalations this period>
```
→ `POLICY_UPDATE`

---

## 15. POLICY UPDATE

### S15 — POLICY_UPDATE
*(v0.2)* The only learning the policy layer performs is **trigger promotion** (§21). Candidate policy updates (auto-run blind-spot review after an event type; state-transfer review at a project boundary; independent verifier after a claim class; lower depth for stable modules; escalate recurring corrections; pre-load a reusable transformation on its trigger) are emitted as *candidates*; they enter shadow mode and are promoted by a human tick. Policy updates are reversible, logged, and **never alter an approval class or an objective**.

---

## 16. META-REVIEW

### S16 — META_REVIEW
Runs as (a) **constraint checks on every tick** — named constraints with tolerated violation rates, e.g., `no_commitment_silently_closed: 0`, `pending_unflagged_past_14d: 0`, `heartbeat_gap < 2 × tick`, `live_triggers ≤ 10`, `reviewer_family == producer_family: 0` — and (b) a **monthly ceremony** (generated brief, ≤5 decisions, decisions-only output).

Inputs: transition history; cognitive events; open debt; attention cost; agent performance (Ask-F1, detection vs correction, κ vs human labels, test-retest); representation changes; reuse events; cross-project patterns; drift checks on the four pathways (prompt/policy, memory, tools, workflow graph); a retained-capability regression set.

Questions: which loops generated decisions; which generated only prose; which actions repeatedly required correction; which skills never activated (invocations ÷ applicable sessions); which abstractions transferred; which state stayed stable; which project consumed disproportionate attention; did an invariant fail; did a new invariant emerge; are we optimizing inside an obsolete representation.

Output: policy changes · architecture decisions · trigger additions/removals · representation proposals · priority changes · retired mechanisms — each with a falsifiable prediction and a deletion condition. → `INTEGRATE` or `WAIT`.

---

## 17. STOPPING POLICY

Stop or suspend when any holds:

```text
objective_satisfied
decision_ready
verification_confidence_above_threshold
marginal_information_gain_below_cost
human_input_required                      (packet emitted at the next boundary)
budget_exhausted
blocked_on_external_dependency
representation_review_required
open_debt_intentionally_deferred          (with a date)
steps_since_grounded_verification ≥ cap   (v0.2) — illusory improvement grows with unaudited steps
wrong_action_budget_reached               (v0.2) — declared tolerated error rate for autonomous acts
```
This prevents indefinite agent activity from being treated as progress — and, with the heartbeat, prevents *absence* of activity from going unnoticed.

---

## 18. Recurring Task Template

```yaml
recurring_review:
  scope: portfolio | project | subsystem
  trigger:
    schedule:            # tick: */30 min while logged in; daily 07:00 (consolidation run)
    event_conditions: [] # ConstraintViolated, HeartbeatMissing, PendingAged, ReturnDue
  baseline:
    previous_state_id:
  collect:
    changed_artifacts_only: true
    changed_decisions_only: true
    new_evidence_only: true
    cognitive_events_since_last_review: true
  run:
    - observe_gestures_and_inbox
    - interpret_deterministic_marks
    - detect_structural_tension
    - fire_returns_and_aging
    - estimate_open_debt
    - select_review_depth_by_table
    - delegate_reviews            # writes packets; never calls a model inline
    - verify_findings
    - detect_representation_counters
    - detect_reusable_transformation
    - update_attention
    - propose_policy_delta        # candidates only
    - check_constraints
    - emit_heartbeat
  output:
    decisions: true
    attention_packet: true
    state_delta: true
    open_debt_delta: true
    new_abstractions: true
    provenance: true
    narrative_report: optional
  guarantees:
    idempotent: true              # nothing written when nothing changed
    max_duration_s: 10
```

---

## 19. Tick Pseudocode *(v0.2 — replaces the model-driven cycle)*

```python
def aace_tick(state, policy, clock):
    events = observe(state, clock)                 # gestures, inbox, outbox, returns due, aging, hashes
    normalized = interpret_deterministic(events)   # marks only; ambiguity -> clarify proposal
    tensions = detect_structural_tension(normalized, state)

    for item in rank_by_table(normalized, tensions, policy):
        depth = depth_table(item)                  # record fields -> D0..D5
        if item.approval_class == "auto" and depth == D0:
            state = record_transition(state, item) # validated loop writes; one attributed commit
        elif item.approval_class == "batch":
            stage_for_tick(item)                   # appears in Pending; human tick promotes
        else:
            stage_for_ceremony(item)               # explicit class -> decision brief
        if item.needs_panel:
            write_packet(item, depth)              # a model works later, in a panel, via the socket

    state = apply_returns_and_aging(state, clock)
    debt  = project_open_debt(state)
    cands = trigger_candidates(state.audit)        # repetition counters; shadow-mode WOULD_FIRE
    regenerate_views(state, debt, cands)           # attention packet, pending, returns, weekly line
    check_constraints(state)                       # ConstraintViolated events, never silent
    emit_heartbeat(clock)
    return state                                   # writes nothing if nothing changed
```

---

## 20. Review-Depth Policy

*(v0.2)* The v0.1 DepthScore (2.0·DecisionImpact + 2.0·BlastRadius + 1.5·Uncertainty + 1.5·Novelty + 1.5·CorrectionFrequency + 1.0·RepresentationAnomaly + 1.0·Irreversibility + 1.0·OpenDebt − 1.0·EvidenceStrength − 0.5·PriorStability) is **deferred**. The depth table of S5 is the bootstrap; each term above is logged on records as it becomes observable (blast radius = dependency count; irreversibility = approval class; correction frequency = audit counts), and the score is calibrated only from a ledger of accepted-then-wrong / rejected-then-right / human-review-fraction outcomes. A weak-verifier score, when it exists, is used with two thresholds: accept ≥ t_hi, rework ≤ t_lo, human in between.

---

## 21. Trigger-Learning Mechanism

```text
IF    the same skill/loop is hand-invoked ≥ 3 times after the same event type
   OR the same gesture sequence recurs ≥ 3 times
   OR a return/aging condition is handled manually that a loop could have fired
THEN  create trigger_candidate(condition, action)
```

Lifecycle *(v0.2 thresholds)*:

```text
observe repetition (counts, not days)
-> candidate (quality/triggers/)
-> shadow mode 14 days: tick writes WOULD_FIRE; weekly shows "fired-when-you-did n/m"
-> promote when precision ≥ 70%  (human tick; Class A inside the registry mechanism)
-> monitor: false-fire < 1/week; live_triggers ≤ 10
-> retire after 30 days without a true positive (supersede-by-move, never delete)
```

Learned triggers never change an approval class. The first shadow run is a **dormancy audit** of the substrate's own inventory (invocations ÷ applicable sessions per loop/skill).

---

## 22. Cross-Project Reuse

After a verified milestone:

```text
extract transformation (recurrence ≥ k successful uses)
-> test project-specific dependencies
-> generalize interface; document (name + when-to-use) before any library entry
-> search other project records (never roots) for matching triggers
-> propose reuse (prospective: expected uses over the forecast next N slices)
-> validate transfer on the second project
-> promote to substrate primitive only after repeated success
```

Each reusable asset keeps a **transfer matrix** (same task · other task · other project · other model) filled from actual reuse events; low-transfer assets are tagged project-local. Reuse classes: artifact; code; workflow; representation; decision-policy — the last two are the highest-level targets. Rule: *reuse first, add on failure* — a new abstraction may be created only after an existing one was tried and its insufficiency logged.

---

## 23. Multi-Agent Review Pattern

For high-impact decisions, structured disagreement, not unconstrained discussion:

```text
Primary Agent            -> proposal (named, checkable premises)
Evidence Verifier        -> supports / disputes each premise; records whether it VERIFIED or restated
Adversarial Reviewer     -> searches for failure conditions ("find the condition under which this fails")
Representation Critic    -> asks whether the framing itself is wrong
Critic-of-the-Review     -> audits the review with an explicit disagreement prompt   (v0.2)
Integrator (code)        -> deterministic aggregation with declared authority weights; no negotiated blend
Policy Gate              -> accept / rerun / human review
```

*(v0.2)* Each reviewer emits position + confidence **before** seeing the others; the output is a **disagreement map** (contested claims, evidence per claim, resolved / unresolved) whose residue becomes open debt; a minority position that cites a verifiable artifact and survives rebuttal is never discarded; high answer agreement with low premise overlap is flagged as consensus illusion and blocks any depth reduction; reviewer model family ≠ producer family. Default depth is one independent critique; rebuttal rounds open only when the critic's classification ability is known to exceed the judge's.

---

## 24. Cross-Platform Execution

Platform-neutral state; division of labour may vary: code/repository execution → coding-specialized model; long synthesis → synthesis model; independent verification → a separate model family; external evidence → retrieval agent; high-impact meta-review → heterogeneous team. *(v0.2)* The substrate never requires one provider for continuity, and never moves knowledge-bearing content off the local plane to achieve portability: remote agents receive paths + hashes and request dereferencing from the owning machine.

---

## 25. Minimum Viable Implementation

**Phase 1** *(v0.2 — remediate the stall)*: the scheduled tick (§19) with heartbeat and constraint checks · event log as single source of truth · decision records · open-debt projection · attention-packet fields in the existing views · socket schema (§6) with validator gates.
**Phase 2**: trigger registry in shadow mode with the dormancy audit · cognitive-event buffer (workflow signals only) · depth table bound to verifiers · adversarial/blind-spot loop on explicit-class items · state-transfer handoff.
**Phase 3**: representation-review state with pre-filters · PROJECT-V adapter and replay · cross-project reuse detector with transfer matrix · monthly ceremony · metric set from logs.
**Phase 4** (cautiously, Epoch-2 contract): representation mutation at epoch boundaries · objective review with goal-adherence probes · policy evolution beyond trigger promotion.

---

## 26. PROJECT-V Validation Protocol

For selected historical episodes (project files first; session transcripts only by explicit ruling):

1. reconstruct only minimal prior state from the project's own records (hypotheses, dependency structure, recorded critiques);
2. replay the next meaningful event;
3. run the tick logic;
4. compare the system-selected next action / depth / attention packet with the historical human action;
5. measure whether the system surfaced the right uncertainty; selected adequate depth; would have reduced manual triggering; preserved evidence; detected reusable abstractions; reduced reconstruction burden; produced false-positive cognitive events.

Then repeat on a project other than PROJECT-V. No feature is promoted to core without demonstrated transfer or a strong general rationale.

---

## 27. Failure Modes to Test Explicitly

- **Compression blindness** — summaries hide minority evidence (measure fact survival; keep verbatim captures).
- **False cognitive inference** — over-interpreting speech (affective signals excluded; `noisy` flag).
- **Trigger spam** — automatic reviews recreate burden (≤10 live triggers; false-fire < 1/week).
- **Ontology ossification** — early primitives block better representations (three-cases rule; archive, not lineage).
- **Local-optimum recursion** — self-improvement only tunes parameters (anomaly-mining side-loop outside the contract).
- **Agent consensus illusion** — correlated models create false confidence (family ≠ family; premise-overlap check).
- **Cross-project contamination** — reused abstraction carries hidden assumptions (transfer matrix; adapter test).
- **State drift** — canonical state diverges from artifacts (hash manifests; sync gate).
- **Open-debt explosion** — debt recorded faster than resolved (burn rate on the weekly line).
- **Review theater** — reports without changed decisions (review yield; a production judge surfaced < ¼ of systematic defects).
- **Human bypass** — autonomy grows faster than trust (approval classes immutable by policy).
- **Socket leakage** — platform assumptions enter neutral state (conformance test; knowledge slice off the control plane).
- **Activation failure** *(v0.2)* — loops exist but never run; silence invisible (heartbeat; I13).
- **Overseer confirmation bias and fatigue** *(v0.2)* — the human's own checking raises confidence without accuracy; reliability decays with load (disconfirming evidence first; capacity C).
- **Self-authored verification** *(v0.2)* — the proposer writes its own acceptance test (sealed, pre-registered criteria).
- **Intent debt** *(v0.2)* — decisions without rationale accumulate silently (typed debt item).

---

## 28. Invariant Checks

Every deep review evaluates:

```yaml
invariant_check:
  cognitive_sustainability:
  representation_evolution:
  decision_traceability:
  incremental_evolution:
  adaptive_review_depth:
  multi_resolution_coherence:
  reasoning_portability:
  validation_before_generalization:
  asymmetric_attention:
  reusable_abstraction_emergence:
  activation_over_storage:
  optimization_vs_conceptual_change:
  automated_activation:          # I13 (v0.2): heartbeat present; no hand-started loop
  deterministic_authority:       # I14 (v0.2): no model-written canonical state; evidence tier respected
```
Result: `PASS` · `WARN` · `FAIL` · `NEW_INVARIANT_CANDIDATE` — the last enters the next ceremony, never doctrine directly.

---

## 29. Compact Graph

```text
        +--------+   Tick / event   +---------+
        |  WAIT  | ---------------> | OBSERVE |
        +--------+                  +----+----+
             ^                           |
             |                           v
             |                     +-----+------+        +-----------------------+
             |                     | INTERPRET  |------->| REPRESENTATION REVIEW |
             |                     +-----+------+        +-----------+-----------+
             |                           |                           |
             |                           v                           |
             |                   +-------+--------+                  |
             |                   | DETECT TENSION |                  |
             |                   +-------+--------+                  |
             |                           v                           |
             |                   +-------+--------+   table          |
             |                   |  PRIORITIZE    |                  |
             |                   +-------+--------+                  |
             |                           v                           |
             |                   +-------+--------+   table          |
             |                   | SELECT DEPTH   |                  |
             |                   +-------+--------+                  |
             |                           v                           |
             |                   +-------+--------+  packet          |
             |                   |   DELEGATE     |----> panel -----+|
             |                   +-------+--------+                 ||
             |                           v                          ||
             |                   +-------+--------+                 ||
             |                   |   EXECUTE      |<----------------+|
             |                   +-------+--------+                  |
             |                           v                           |
             |        +----------+-------+--------+-----------+      |
             |        |          |    VERIFY      |           |      |
             |        |   pass   +-------+--------+  uncertain|      |
             |        v                  | fail              v      |
             |   +----+------+   +-------+----------+  +-----+----------------+
             |   | INTEGRATE |   | FAILURE ANALYSIS |  | 2nd VERIFIER (family≠)|
             |   +----+------+   +-------+----------+  +-----------------------+
             |        v                  +---------------------------+
             |   +----+-----------------+
             |   | REPRESENTATION CHECK |
             |   +----+-----------------+
             |        v
             |   +----+-----------------+
             |   |  ATTENTION UPDATE    |  packet at boundary; heartbeat
             |   +----+-----------------+
             |        v
             |   +----+-----------------+
             +---|   POLICY UPDATE      |  trigger promotion only
                 +----+-----------------+
                      v
            +---------+----------+
            | STOP / WAIT / NEXT |
            +--------------------+
```

---

## 30. Implementation Principle

The core runtime optimizes for:

> **the next consequential state change, not the next available task — and it runs without being remembered.**

The human interface optimizes for:

> **the smallest amount of human cognition required to preserve direction, judgment, and the ability to revise the system when the representation itself becomes wrong.**
