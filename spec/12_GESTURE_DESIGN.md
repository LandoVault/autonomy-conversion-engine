# PA-4 — Interaction Design: Gesture / Agentic / Ceremony (v1.1)

**Status: `PROPOSED — operator-originated principle (2026-07-20), refined same day: three-mode alternation; Epoch-1 mutation candidate M1; awaits one-word confirm (R4-1)`**

## The principle (the operator's words, paraphrased; confirmation pending)

The PKM system was efficient because *writing is thinking* and *editing is organizing* — moving an item IS deciding its priority. Cognition and decision should be embedded in the act of execution, never extracted into separate ceremonies. Ceremonies (clarify sessions, batch reviews, approval queues) are where all five predecessor systems died (01 §Lineage guard).

## Mechanisms

1. **Gesture watcher** (`engine/gesture_watcher.py`, Phase 2): diffs the hub vault (`F:\ACE_hub`) against the engine's last-written baseline; **operator-authored** changes (git author = the operator, per PA-2 attribution) are recorded as already-approved audited transitions. Agent proposals still queue in `pending/`. Human authority is exercised physically, not procedurally.
2. **Two-way generated views**: before regenerating, the engine harvests the operator's edits as decisions. Gesture grammar (complete; anything else is ignored, never guessed):

| Gesture in a view/note | Decision recorded |
|---|---|
| reorder lines | priority rank (top 3 feed Today) |
| move line/note between sections/folders | state transition (e.g. waiting → actionable) |
| `[x]` on a pending item | accept that package |
| `~~strikethrough~~` | defer → idea queue |
| `>>YYYY-MM-DD` suffix | `no_action_before` that date |
| `@name` suffix | waiting-for that person |

3. **Location-as-classification capture**: text written inside a project note is filed by that act; inbox holds only genuinely homeless captures; panels extract exit packages from working text rather than asking for restatement.

## Why better than the PKM ingest (the bar this must beat)

PKM: gesture encoded the decision, but nothing executed it, no history, silent debt. ACE: same gesture + deterministic execution (returns fire, views recompose) + audit/rollback + the system initiates contact (morning brief, return dates). Decision cost identical to PKM; consequence and memory strictly greater.

## Red-Queen mutation compliance (07 rules 1–6)

1. observed failure: five-system ceremony-death lineage + the operator's 2026-07-20 report ✓
2. reduces deciding operations: decisions ride existing acts ✓
3. no new routine surface: reuses the hub the operator already touches ✓
4. pass/fail test: ≥80% of routine transitions made via gesture (not command/ceremony) over 14 days; harvester misread rate <5% (misread = the operator reverts an auto-recorded transition) ✓
5. deletion condition: misread rate ≥5% or the operator reports gesture friction → revert views to one-way, keep command accept ✓
6. no evaluator degraded: strengthens Hub trust (every gesture audited); Clinical safety untouched ✓

## Interactions

- `hub/views` READMEs change from "hand edits are lost" to "hand edits are harvested, then regenerated" — only after M1 is adopted.
- Backpressure (Q-D11 aging) becomes a fallback, not the primary mechanism: gestures should drain the queue before aging ever fires.
- Morning brief answers (voice) are gestures in audio form — same harvest principle, Phase 2.

---

### Change log
- **v1.0 (2026-07-20)** — created from the operator's design insight; PROPOSED as Epoch-1 mutation M1.

---

# v1.1 refinement — three-mode alternation (operator, 2026-07-20)

Ceremony is not eliminated — it is **kept at key steps and purified**. Three modes, assigned per phase ("taste per phase"), alternating by design:

- **G (gesture)** — human in flow. Best in brainstorming/inbox/daily-touch phases. Writing is thinking; moving is deciding; the 6-mark grammar above harvests it.
- **A (agentic)** — operations belong to agents. Archiving, PARA filing updates, memory-system updates, context assembly run as scalable agentic processes (fan-out search, propose/execute per approval class). Agents facilitate cognition and offload burden; the operator never performs an operation an agent could have prepared.
- **C (ceremony)** — decision-pure human junctures. Required where **multiple steps must be taken to reorganize a task/project/decision**: the agent computes a decision-complete plan (all steps, impacts, rollback), the operator makes ONE decision, execution is atomic. Weekly review: ≤20 min, ≤5 decisions (roadmap Phase-3 exit). **A ceremony containing a manual operation is a design bug.**

**Alternation pattern:** G collects → A organizes → C decides (only when consequential) → A executes → G continues.

## Per-step mode assignment

| Step | Mode | Operator | Agents/loops |
|---|---|---|---|
| Capture/brainstorm | G | write-as-you-think; location=classification | nothing |
| Inbox triage | G | drag/tick/strike | view + harvest |
| Clarification | A→G | gesture on low-confidence leftovers only | enrichment via agentic search; high-confidence auto-applies (batch class) |
| Filing/PARA maintenance | A | nothing routine | filing agent proposes/executes placements (reorganized PARA per R3 ruling) |
| Multi-step reorganization | **C** | one decision on a decision-complete plan | compute full plan; execute atomically post-approval |
| Panel work | G | think/produce | context assembly; exit package extracted from working text |
| Routine pending review | G | ticks in Pending view | validate/stage/harvest/execute |
| Kill / handoff / clinical transfer / strategy | **C** | decide from prepared brief | evidence, options, recommendation; execution + receipts |
| Weekly review | **C** (≤5 decisions) | the decisions | scoreboards, exceptions, simplification candidates pre-computed |
| Archiving | A | batch tick at most | staleness detection, moves, audit |
| Memory/hypothesis update | A (beliefs: C) | confirm belief changes only | consolidation, hypothesis staleness, drafts |
| Morning brief (voice) | G (voice) | one-word answers | assemble questions from returns/deadlines/pending |

## Unification with frozen approval classes (03 §5)

auto-acceptable → silent **A** · batch-reviewable → **G** harvest · explicit approval → **C** decision brief. No new approval semantics — this assigns each frozen class its interaction surface.

## Measurability + next-epoch feed

- Ceremony purity metric: manual operations per ceremony = 0; decisions per weekly review ≤5; decision latency per C-item.
- Candidate next-epoch attack case (cannot join the frozen Epoch-1 contract mid-epoch; queued anomaly-loop-style): "ceremony contains operations — pass only if every C-mode surface presents ≤N pure decisions and zero manual operations."
- Build order impact (Phase 2): gesture watcher → clarify agent (A-mode with confidence routing) → filing agent → decision-brief generator for C-mode → morning brief.

### Change log
- **v1.1 (2026-07-20)** — three-mode alternation refinement from the operator: ceremony retained and purified (decision-only), agentic mode for archiving/filing/memory operations, per-step mode table, approval-class unification, ceremony-purity metric.

---

# v1.2 addendum — unified grammar + compounding (2026-07-20, from the coding-session spawn analysis)

1. **One grammar, all surfaces**: the hub marks above and the session tokens in `spec/13_GESTURE_REGISTRY.md` are ONE language. Tick in Pending view ≡ "1" in chat ≡ "yes" in the voice morning brief. Consistent mapping across surfaces is what builds automaticity; the registry is the single source.
2. **Compounding principle**: gesture bandwidth = agent preparation × mapping consistency. To compound multiple cognitive activities into one gesture, enrich the prepared referent's bundle (accept-tick = accept + schedule + regenerate + commit), never the human act. Ceremonies compound by decision-completeness: one verdict releases many pre-computed operations.
3. **Epistemic channel added** (gap in v1.1): hedge lexicon = non-binding (clarify agent routes musings to idea-queue with propose-back); paste/drop = reference by default; repetition-with-compression = escalation dial the engine must detect and upshift to; honest-probes route to adversarial machinery. Binding status is part of capture, not an afterthought.
4. **C-mode surface formalized from evidence**: ceremony = stable-ID'd numbered decision queue, defaults marked, verdict-first agent output, one-token-per-item verdicts, partial answers legal, silence = defer, "approve all" affordance. (Our question rounds were already this shape; the 122-session evidence ratifies it as THE ceremony format.)
5. **Reciprocal agent contract** (13 §Agent-side) is normative for every ACE panel and loop output.

### Change log
- **v1.2 (2026-07-20)** — unified-surface rule, compounding principle, epistemic channel, evidence-ratified C-mode format; registry split out to spec/13.
