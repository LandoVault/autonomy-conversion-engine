# Gesture Registry — the human-side API (all surfaces)

**Status: `PROPOSED (R4-2) — evidence-derived from a 122-session audit of the operator's agent sessions + another meta-system's audits + this session; companion to spec/12 v1.2`**

## First principles (what a gesture IS)

1. **A gesture is a reference into prepared structure, not a compressed command.** "1" carries a whole plan-approval only because the agent pre-structured the option space. Gesture bandwidth = agent preparation × mapping consistency. Corollary: to compound more cognition into one gesture, enrich what the referent bundles — never make the human's act richer.
2. **Automaticity requires consistent mapping.** Same act = same meaning on every surface (chat, hub vault, voice brief, Codex/Cowork). Small consistent set beats rich inconsistent set (Hick's law). Registry additions face the frozen feature gates (measured failure, deletion condition).
3. **Cognitive-burden levels**: L0 automatic act (tick, token, paste) · L1 recognition pick (letter vs prepared options) · L2 evaluative judgment (ceremony) · L3 generative flow (panel work). Gestures live at L0–L1; ceremonies at L2; anything forcing L2 processing for an L0 act is a grammar bug.
4. **Orthogonality**: capability (skills/loops) × intent channel (gestures) × consequence gating (approval classes) are independent axes. Skills are agent-side verbs; gestures are the human-side phonology; approval classes are the deontics. This registry is the **binding table** joining them. Skills stay vendor-portable; every surface parses this grammar identically via a thin adapter — the grammar itself is vendor-neutral ACE property.
5. **Parsing is deterministic and fuzzy**: typos/fragments are canonical input, never blocked on; semantic ambiguity gets exactly one one-line clarify ("reference or instruction?"); the model never guesses a binding.

## The registry (gesture → meaning → bundles → class)

### Commit / release (L0)
| Gesture | Meaning | Bundled operations | Class |
|---|---|---|---|
| `1` / `a` / `go` / `ok` / `approve` vs a presented referent | gate release | verdict + authorization + budget release at declared defaults + execute now; **re-confirming after release is a violation** | batch |
| `X: verdict` lines vs numbered queue (partial legal) | per-item rulings | decision + record + downstream execution per item; unanswered = defer (silence is a gesture; never re-prompt) | batch |
| `[x]` tick in Pending view | accept package | accept + apply state + schedule returns + regenerate views + attributed commit/push | batch |
| `READY?` ↔ READY/NOT-READY | run-readiness handshake | binary answer; the final run stays the operator's act | — |

### Scope / launch (L0–L1)
| Gesture | Meaning | Bundled operations | Class |
|---|---|---|---|
| Paste-back of a generated KICKOFF block | launch with full intent | context load + scope + budgets + arming ("Go.") | batch |
| one-liner `verb + target + macro` | light launch register | no heavyweight structure imposed on light asks | batch |
| macro token + bare budget (`rqgm loop epoch=15`, `effortlevel=max`, model tag) | method/effort/routing dial | skill invocation with parameter defaults persisted (never re-typed) | batch |
| mount / file-drop into a visible root | make-visible / ingest-as-reference | scoping; dropped files default to **reference** provenance | auto |

### Steering (in-flight)
| Gesture | Meaning | Bundled operations | Class |
|---|---|---|---|
| `also ...` | append scope | extend, never replace in-flight work | batch |
| `wait..` | hard interrupt | halt + re-verify state before proceeding | auto |
| `not X, Y` fragment | surgical re-anchor | correction absorbed; downstream re-derived; no restated context demanded | batch |
| terse world-status line ("git lock cleared") | state update | verify + resume immediately; blocking on already-cleared items is a violation | auto |
| raw output paste (no words) | "this broke → go" | parse + diagnose; never ask for what the paste contains | auto |

### Epistemic (binding status of the operator's own words)
| Gesture | Meaning | Bundled operations | Class |
|---|---|---|---|
| hedge lexicon ("thinking out loud", "maybe", "not sure", trailing `..`) | non-binding musing | propose-back for confirmation; **never implement as requirement**; captures auto-route to idea-queue | — |
| paste label ("not prompt", "reference") / unlabeled paste | provenance mark / default-reference | one-line clarify only if action seems intended | — |
| quote + short question (+ persona: "as a 5-min domain reviewer") | calibrated review request | rate-this-fragment with audience parameter | — |
| repetition-with-compression (repeated, shortened re-request, e.g. "still not working") | escalation signal | detected escalation upshifts response: re-verify → diff proof → completed work; never treated as new request | — |
| honest-probe ("will this approach still hold up later?") | stress-test my belief | route to adversarial/disagree machinery, never reassurance | — |

### Authority / boundary
| Gesture | Meaning | Bundled operations | Class |
|---|---|---|---|
| delegation grant ("you pick, justify briefly") | scoped authority | agent decides + 1–2-line justification; per-session, per-decision; no per-step confirm after grant | explicit→batch |
| "add to CLAUDE.md" / law-codification | durable rule injection | rule recorded + change-logged | explicit |
| gate-substitution attempt (agent side) | **forced ceremony** | any declared-mechanism downgrade = BLOCKING lettered decision to the operator, never a footnote | explicit |
| "instructions?" / "handoff" | close ritual | exit package + state update + kickoff generation — system-owned, one word | batch |
| "continue where we left off" | resume | must cost ONE token; needing a re-paste of state is a grammar failure | auto |

### Hub-vault marks (spec/12 §Mechanisms — same semantics, different surface)
reorder = priority · move = state transition · `[x]` = accept · `~~strike~~ (because …)` = defer (+harvested reason) · `@date` = no_action_before (was `>>` — retired 2026-07-21: collides with Obsidian blockquote grammar at line start; measured failure -> mark change; `>>` still parsed mid-line as legacy) · `@name` = waiting-for.

## Agent-side reciprocal contract (what makes one-token gestures possible)

Verdict-first output (PASS/FAIL line 1), bounded bullets, stable IDs on every decidable item, defaults marked, one question at a time with a recommended default, unprompted heartbeat + honest "stuck on X" during long runs (so probe gestures become unnecessary), no re-confirmation after release, no questions a paste already answers.

## Measurability

Tokens-per-decision (target: ≤2 for routine), re-prompt rate (target: ~0), grammar-violation count (re-confirms, blocked typos, ignored hedges) logged to `quality/edge_cases/` — each violation is an edge case; misparse ≥5% on any gesture = its deletion condition.

---
### Change log
- **v1.0 (2026-07-20)** — created from gesture-evidence mining (2 agents over the operator-session audit corpus, another meta-system's audits, the operator's session-close, interview and understanding-check skill records, this session's record).
