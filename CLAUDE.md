# ACE Operating Contract — v1.2

*Supersedes `reference materials/codex.md` (not included in the public release). Deltas vs codex.md: paths updated to `spec/`; added — coexistence rule, storage rules, private-stores rule, atlas access-class rule, never-silently-decide-open-questions rule, 09_STATE update duty in the completion format. Codex rules re-homed rather than dropped: PROJECT-W closure prohibition → spec/02; dashboard-replacement condition → spec/02. This file governs every agent session in this repo.*

## Mission

Implement and operate ACE — a local-first Autonomy Conversion Engine for its operator that reduces cognitive burden, improves ordinary execution reliability, and converts selected work into durable evidence and increased autonomy.

## Scope and hard rules

- Personal productivity, clinical/professional work organization, research, literature/practice surveillance, professional service, evidence, sanitized clinical coordination.
- **Exclude other people's private personal matters (third-party content) wherever encountered — content-based, not path-based.** (No third-party names in any remoted doc; R2-11 governs legacy material.)
- **Never** place PHI, patient-identifying data, restricted clinical content, credentials, or secrets in this repo or ACE_storage.
- Your instance's state and content stores stay **private** and are never used for AI training: the control plane (`ACE_storage`) goes only to a private remote, if any; `F:\ACE_local` never gets a remote.
- Respect every access class in `spec/08_WORKSPACE_ATLAS.md`: `NAME-ONLY` zones are never opened; `RO-REF` roots are never written; only `ACE`, `ACE_storage`, and `F:\ACE_local` are writable.
- **Never delete.** Never delete any file or folder outside ACE's own stores — including external roots being inspected; inside ACE stores, supersede-by-move only (the operator's standing rule, 2026-07-19, conservatively generalized — confirm scope in R2-2).
- **Two-plane rule**: personal/IP content → `F:\ACE_local` only; state/metadata/hashes → `ACE_storage`; clinical/committee/audit-level work → institution-side ACE-C (institution-approved tools), never in these repos.
- **Clinical identifier convention (R2-11 ruled)**: short initials-style aliases only in remoted docs and records (e.g. TRIAL-A, COMMITTEE-1); full protocol names/numbers never leave the local plane; the alias key lives at `F:\ACE_local\aliases.md` and is never mirrored.

## Read order

`spec/00_INDEX.md` defines it. Load `spec/06_INTERVIEW_RECORD.md` only for strategic tasks — never inject interview interpretations into ordinary sessions.

## Fixed architecture (unchanged from v1.0)

Two layers: **ACE-P** (Cowork/panel-first work surface; Obsidian durable hub; deterministic loops; plain files + git as portable state) and **ACE-C** (institutionally approved clinical tools, minimal loops). Only reviewed, sanitized, minimum-necessary packages cross layers — with target acknowledgment; export alone is never completion.

> Ask agents to do bounded cognitive work; use loops to preserve continuity; use Obsidian to preserve human legibility and control.

## Panel rules (every consequential session)

1. Read the session packet; declare panel type (`explore` / `decide` / `produce` / `review`) and its stop condition (02 table).
2. State visible roots and unavailable sources; work only inside them.
3. Write a structured exit package to the declared outbox (`ACE_storage/outbox/`); a chat response alone is not durable completion.
4. Never claim completeness beyond observed sources — distinguish observed / inferred / missing / unknown.
5. Every synthesis states (codex.md partial-observability checklist, carried): folders and files inspected · communication channels inspected · date range · authoritative sources used · known inaccessible sources · confidence in completeness.

## Deterministic vs model vs human

- **Code**: state transitions, dates/recurrence, overdue/stale detection, schema validation, existence/hash checks, receipts, report assembly, audit logging.
- **Model**: ambiguous classification, synthesis, missing-context identification, proposing next evidence units, drafting summaries — always *propose*, never *apply*.
- **Human (explicit approval)**: clinical transfer, external communication, project kill/closure, ownership transfer, strategic changes, belief promotion, privacy-sensitive actions.

A model may propose a transition; only a validated loop records it. Never silently close a commitment, transfer ownership, kill a project, import a clinical package, or rewrite user hypotheses.

## Coexistence rule (v1.1, until Q-C1/C2 are ruled)

ACE durable state lives **only in ACE_storage**. Do not write ACE state into other meta-systems' memory stores, paths, or ledgers. Treat other meta-systems' observations as foreign input.

## Storage rules

`spec/11_STORAGE_AND_FILING.md` defines who writes where; the writer matrix is **binding** (R2-2 sign-off). Attributed loop authorship (`ACE Loop <loop@ace.local>`, one commit per accepted state transition) is in force (PA-2 adopted). The hub vault is local: `F:\ACE_hub` (R2-9).

## Cognitive-burden constraints

The consolidated limits table in `spec/03_PRODUCT_SPEC.md` — targets per v1.0; upgrading them to hard gates is PROPOSED (01 §Lineage guard, Q-D3). Add no field without three observed cases; no plugin without a measured failure; no agent where a script suffices.

## Undecided matters

`spec/10_OPEN_QUESTIONS.md` is the registry. **Never silently decide an open question** — flag, propose, wait.

## Completion format (end of every implementation session)

Work completed · files changed · tests run · observed failures · decisions proposed · decisions requiring approval · exact next action · access limitations · outbox path. Update `spec/09_STATE.md`.
