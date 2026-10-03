# ACE Product Specification

## 1. Product definition

ACE is a local-first, federated personal operations and conversion engine for the operator.

It coordinates panel-based work, durable hub state, deterministic lifecycle loops, and a minimal clinical application layer.

## 2. User stories

1. As the operator, I want to capture a task or concern without choosing a folder or tag, so that capture does not interrupt work.
2. As the operator, I want deferred issues to return with enough context, so that I can release them from working memory.
3. As the operator, I want Cowork panels to receive selected context, so that they can perform bounded work without scanning every folder.
4. As the operator, I want panel outputs to become durable project state, so that work does not die in conversation history.
5. As the operator, I want Obsidian to show pending, current, stale, and unknown states, so that I can trust what I see.
6. As the operator, I want ordinary productivity and evidence conversion measured separately, so that efficient coordination does not masquerade as original progress.
7. As the operator, I want handoffs to remove recurring ownership, so that delegation actually reduces cognitive burden.
8. As the operator, I want the clinical layer to remain minimal and approved, so that the personal system does not create privacy or governance risk.
9. As the operator, I want transfer packages to declare missing context, so that receiving systems do not mistake partial data for complete truth.
10. As the operator, I want the system to challenge scope expansion only when evidence requires it, so that architecture revision does not consume shipping time.

## 3. Functional requirements

### FR-1 Universal capture

- One primary capture path in ACE-P.
- Capture requires only free text and optional explicit date.
- Classification occurs later and may be proposed by an agent.
- Capture must not require project, priority, or tag selection.

### FR-2 Today view

Show only:

- up to three ordinary obligations;
- due return items;
- one protected work target;
- one next evidence unit;
- genuine urgent exceptions.

### FR-3 Commitment and return

A consequential deferred item must support:

- next action;
- return date;
- waiting person or context;
- urgency class;
- closure evidence;
- explicit `no_action_before` state.

### FR-4 Session packets

The system shall generate a scoped packet for each consequential panel.

### FR-5 Panel exit packages

The system shall reject incomplete exit packages and mark accepted packages as pending hub updates.

### FR-6 Hub synchronization

The hub shall show the latest accepted durable state and visibly flag newer unprocessed panel packages.

### FR-7 Resume packets

Every meaningful work session shall support:

- completed state;
- exact next action;
- files;
- unresolved decision;
- decision lock;
- missing context.

### FR-8 Evidence records

Evidence records shall include:

- artifact;
- proof location;
- external or internal status;
- associated project;
- anchor contribution;
- impact or reuse;
- date.

### FR-9 Handoff

Handoff shall require:

- recipient acceptance;
- next milestone;
- the operator's retained role;
- rescue threshold;
- provenance record;
- independent action by successor;
- observation period.

### FR-10 Clinical transfer

No clinical package may cross layers without the complete review state machine.

### FR-11 Weekly review

The weekly review shall take less than 20 minutes and show:

- reliability exceptions;
- conversion result;
- coordination displacement;
- stalled work;
- handoff or closure candidate;
- one process simplification.

### FR-12 Red-Queen validation

Design changes shall be tested against frozen epoch criteria before adoption.

### Cognitive-burden limits *(consolidated v1.1 — previously scattered across codex.md, 01_GOALS, v0.1 config, and the design docx; codex.md, the v0.1 package and the docx are provenance not included in the public release)*

| Limit | Target | Source | Status |
|---|---|---|---|
| Capture time | under 20 seconds | v0.1 + design docx | carried — confirm (Q-D3) |
| Daily hub review | under 7 minutes | codex.md (v0.1 said 10) | **conflict — adjudicate (Q-D3)** |
| Weekly review | under 20 minutes | FR-11, consistent | firm |
| Panel exit-package review | under 3 minutes | codex.md + 05, consistent | firm |
| Manual classification | fewer than 10 decisions/week | codex.md | firm |
| ACE maintenance | below 5% of planning/review time | NFR-3, consistent | firm |
| New field | none without 3 observed cases | codex.md | firm |
| New plugin | none without a measured workflow failure | codex.md | firm |
| New agent | none where a deterministic script suffices | codex.md | firm |

**Hard failure gates** (targets→gates reclassification approved in the R2-2 sign-off; Q-D3 ruled: daily 7 min, capture <20s carries).

## 4. Nonfunctional requirements

### NFR-1 Local and portable

Core state shall remain inspectable without a proprietary service.

### NFR-2 Partial observability

All agent outputs shall declare access scope and missing context.

### NFR-3 Low maintenance

Routine system maintenance shall remain below 5% of professional planning/review time.

### NFR-4 Replaceable interfaces

Removing Obsidian, Codex, Claude, or a plugin shall not destroy the underlying state.

### NFR-5 Auditability

All accepted state changes shall be traceable and reversible.

### NFR-6 Privacy

No PHI in ACE-P. Clinical export must be minimum necessary and human approved.

### NFR-7 Human authority

Consequential decisions remain human controlled.

### NFR-8 No false completeness

The system shall prefer `unknown` to unsupported certainty.

## 5. Approval classes

### Auto-acceptable

- file existence;
- source pointers;
- session completion;
- ordinary resume-state update;
- deterministic deadline calculation.

### Batch-reviewable

- proposed task;
- proposed commitment;
- proposed evidence classification;
- proposed project-state update.

### Explicit approval

- ownership change;
- project closure;
- strategic priority change;
- clinical transfer;
- external message;
- persistent personal-hypothesis update.

## 6. Initial technical constraints

- No custom Obsidian plugin in the first slice.
- No vector database in the first slice.
- No full historical migration.
- No continuous autonomous agent.
- No global filesystem crawl.
- No more than one primary capture path.
- No more than six stable hub views.

## 7. Acceptance test

The first prototype passes only when one real `produce` panel completes the full lifecycle from session packet to durable hub state and a future session resumes correctly from the generated packet.

## 8. Amendments *(ADOPTED 2026-07-19 — R2-2 sign-off; in force)*

- **PA-1 — WIP limits (restore).** v0.1 `starter/SYSTEM/config.yaml` set `active_frontier_projects_max: 1` and `active_institutional_projects_max: 1` (a second corroborating source exists in the 06 interview answers — not included in the public release — strategic-load only) — yet no v1.0 FR encodes any limit. Proposed: new FR enforcing configurable WIP limits at the Active Work hub view and project state machine (`Proposed → Active` guard). *(Q-D4)*
- **PA-2 — Write attribution (new NFR).** All loop/agent writes carry an actor identity (git author + event-log actor field); staleness detection reads human-attributable signals only. *Evidence: mtime pollution documented in 08_WORKSPACE_ATLAS.* *(Q-D5)*
- **PA-3 — Sanitization criteria (restore).** v1.0 dropped the only written sanitization criteria for the cross-layer `Sanitized` state (v0.1 `10_CLINICAL_COPILOT_PROMPTS` allowed/remove lists). Proposed: restore them as the normative checklist behind FR-10 before any clinical transfer is implemented. *(Q-D6)*

---

### Change log

- **v1.1 (2026-07-19)** — carried from `reference materials/03_PRODUCT_SPEC.md` (not included in the public release); added consolidated Cognitive-burden limits table (with the 7-vs-10-minute conflict flagged, not resolved); added section 8 Proposed amendments (PA-1..PA-3, none in force). FR/NFR text unchanged.
