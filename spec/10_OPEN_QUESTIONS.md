# ACE Open Questions

**Round 1 issued 2026-07-19; Round-1 rulings recorded below (see Rulings record). Round 2 — the remaining set — is at the top.** `[BSP]` = surfaced by the blindspot pass. **Rec** = my recommendation where I have one.

## ROUND 6 (open — issued 2026-10-02 by the external-review panel; full text in `spec/15_EXTERNAL_REVIEW_DIGEST_2026-10.md` §7)

- **R5-2 restated (73 d) — the only blocking item.** One word activates M2 `ace tick` as specified in spec/14. The external report's value lands as builder-level M2 acceptance tests of requirements already in force (spec/15 §5 M2-a..e) — no ruling needed; veto any you dislike. Merging the review branch (engine fixes, spec/15 §6) is a separate, independently safe act; it includes one semantics amendment for your OK: rollback becomes newest-first (Q-D10 / spec/11 flow 4 said "reverses to the prior snapshot").
- **R6-1 (optional, wording only).** Default scope sentence: *"ACE is a single-owner executive system that converts bounded human–AI work sessions into accepted, resumable state and durable evidence — models propose, deterministic code records, the owner approves — and brings other people in only through explicit handoffs."* The report's two framings stay on record as direction; team scope is a later door-1 item (preconditions: privacy/permission model + one observed second-principal case).
- **No-ruling action available now: T4** — open `ACE_storage/packets/RESUME_X-0002.md` (most recent, 2026-07-20) after the real 74-day gap; note minutes to first correct action (target ≤10).
- Notes: the cross-vendor exchange follows the operator's 2026-10-02 instruction (`.md` in/out) and stops after the author's reply (another round only on request). Standing precondition: before uploading a deployment's own instance content (ACE_storage / `F:\ACE_local` material) to any external vendor, confirm that vendor's model-training setting is off. The review is uploaded and the author's reply is pending — retry it in the thread and drop the returned `.md` into `reference materials/` (not included in the public release). `CLAUDE.md:56` still calls the burden-limit gates PROPOSED although R2-2 ruled them (10:160) — align when convenient.

## ROUND 5 (open — issued 2026-08-22 by the meta-loop-docs digest panel; full text and recommendations in `spec/14_META_LOOP_AND_LAYERS.md` §10)

- ~~**R5-1**~~ **Ruled 2026-08-22** — "AACE and ACE are essentially the same thing" (operator). One system; name retired; documents reconciled as `spec/meta/` v0.2 exports.
- **R5-2 [unblocks the stall]** Activate **M2 `ace tick`** — one scheduled deterministic loop (30 min + 07:00) running gesture harvest, clarify, validator, aging, returns, view regeneration. Subsumes R4-1. One word activates both.
- **R5-3** Approve **M3 decision records** (`hub/decisions/`, Decisions view = slot 5 of 6) and mirroring of these rulings into hub ticks.
- **R5-4** Approve **M4 trigger registry** in shadow mode; first shadow run = dormancy audit of ACE's own loops and skills (invocations ÷ applicable sessions). Legacy scheduled skills stay outside per R2-5.
- **R5-5** PROJECT-V adapter replay (PROJECT-V = a research project, ACE's second validation project): project files under `<PROJECT-V repo>` only (rec), or session transcripts too (operator-session-corpus sensitivity)?
- **R5-6** Monthly meta-review as a C-mode ceremony (≤5 decisions, generated brief): first date? Rec 2026-09-19.
- ~~**R5-7**~~ **Ruled 2026-08-22** — drafted by a peer agent; "AACE" was a naming slip. Recorded in `00_INDEX`.
- **R5-8** (carried) R3-1..R3-5, R4-1, R4-2 remain open; under M3 they become hub ticks.

**Observed 2026-08-22 (context for R5-2):** no ACE transition since 2026-07-21; 9 clarify proposals pending 32 days; no loop scheduled except the backup. Evidence table: spec/14 §2.

## ROUND 4 (open)

- **R4-2** Confirm `spec/13_GESTURE_REGISTRY.md` (evidence-derived, 122 sessions) as the unified gesture grammar across all ACE surfaces + the reciprocal agent output contract. Confirms with R4-1 in one word if you like.
- **R4-1** Confirm PA-4 "Manipulation-as-Decision" (`spec/12_GESTURE_DESIGN.md`) as Epoch-1 mutation M1: your gestures in the hub (moves, reorders, ticks, strikes) are harvested as already-approved transitions; agent proposals still queue. Includes the 6-mark gesture grammar and the <5% misread deletion condition. One word confirms.

## ROUND 3 (open)

- **R3-1 [needs your explicit go-ahead]** History reset for the name scrub: third-party names remained in **prior commits** of the ACE remote (including inside zip/docx blobs). Completing the "scrub" ruling requires replacing remote history with the clean baseline (prepared locally; pre-scrub history preserved as a bundle in `F:\ACE_local\archive\<provenance bundle>\`). Say "reset history" and I'll execute; or run it yourself; or accept names in old commits.
- **R3-2** R2-4 clarified: drives `<secondary drive>` (backup folders) and `<archive drive>` (old legacy trees) were never surveyed. Question: should ACE be able to **read** them as archive reference (mapped in a mini-survey), or ignore them completely?
- **R3-3** R2-12 clarified — leftover small questions, none blocking, answer whichever: (a) is anything in the OneNote *cloud* newer than the last local backup snapshot? (b) may an orphaned empty vault folder in Documents be archived (moved, not deleted)? (c) do old seals stay in the existing seal folders on the data drive? (d) want the portfolio live/dead triage checklist next session? (e) hard deadlines: which external professional and recurring dates should seed the deadline loop? (f) legacy personal zones: exclude entirely or name-only index?
- **R3-4** Backup target for `F:\ACE_local`/`F:\ACE_hub` (stated preference: local backup): which target — external drive letter/path, second internal disk, or NAS? The backup loop needs a destination.
- **R3-5** Obsidian Sync for `F:\ACE_hub`: you'll enable it in-app with your account (I can't/shouldn't touch credentials). Confirm once enabled so the staleness loop can treat Sync's config touches as expected noise.

## ROUND 2 (ruled 2026-07-19 — see Rulings record)

- **R2-1 [BLOCKING] First slice pilot.** MANUSCRIPT-1 is past; WORKSTREAM-1 (a template-update workstream) done. Given a real near-term planning need: run the first `produce` panel AS that planning session (artifact = your plan + extracted commitments, seeding the hub)? **Rec: yes** — real, immediate, non-clinical, and it bootstraps the portfolio triage (Q-E2) in the same pass. Alternatives still on the table: PROJECT-Q (a research project), PROJECT-P (a research proposal), PROJECT-E (an evaluation project).
- **R2-2 [BLOCKING] Spec sign-offs bundle** (one "approve all" is fine): Q-D1 freeze spec/07 as Epoch-1 contract (package version) · Q-D2 three state-machine fixes · Q-D3 daily 7 min + capture <20s + targets→hard gates · Q-D4 WIP limits 1+1 · Q-D5 write attribution · Q-D6 restore sanitization checklist · Q-D7 at-risk 21 days · Q-D10 audited-inverse rollback · Q-D9 research = retroactive Phase-A evidence.
- **R2-3** Q-D8 anomaly loop: run as experimental side-loop beside mature RQGM (rec), or hold until proven?
- **R2-4** Q-A1: `<secondary drive>` and `<archive drive>` — in ACE's universe, excluded, or archive-only mounts?
- **R2-5** Q-C2 remainder: are the four scheduled skills actually firing (check Task Scheduler / Claude scheduled tasks)? Retire, absorb into ACE loops, or leave? One owner for the loop registry.
- **R2-6** Backup mechanism for `F:\ACE_local` + F: generally (L9 follow-up): external drive on schedule, second internal disk, encrypted archive elsewhere? What hardware exists?
- **R2-7** Q-F1/F2 remainder: capture now lands in `F:\ACE_local\inbox\` on this machine — what's the capture path **away from this machine** (work computer, phone)? Email-to-self → triage? And where do commitments land today until ACE runs?
- **R2-8** Ambiguity from your answer #2: the FMEA/edge-case/eval + audit layers — I placed them **on the GitHub control plane** (`ACE_storage/quality/`, `audit/`) since they're system-level, with clinical/IP excluded from their contents. Confirm, or keep them local too?
- **R2-9** Q-B3: Obsidian Sync stays OFF for the control-plane vault (git is the sync)? Q-G2: are sibling repos' remotes private? Also from your answer #2: confirm the **whole hub** (projects/commitments/evidence/views as control-level records) living in `ACE_storage/hub/` matches your intent that at least part of the hub lives on GitHub — and was the repo you created ACE_storage, or a separate Obsidian repo I should know about?
- **R2-10** Q-H1..H3 (strategic mode, whenever): the 12-month anchor asset · PROJECT-W (the canonical handoff-example project) handoff plan location/recipient/thresholds · the six consequential v0.1 leftovers.
- **R2-11** Clinical **metadata** (Q-G3 remainder): may trial/committee identifiers and status metadata (e.g. study names) appear in ACE-P control-plane records under applicable confidentiality agreements/institutional rules, or should they be aliased (key kept in `ACE_local`)? Existing identifiers in the atlas predate this ruling and get aliased retroactively if you rule them out. Related: the frozen `reference materials/` (not included in the public release) contain third-party names in provenance docs already pushed — keep as-is (history rewrite required to scrub) or scrub? *(Operating docs are already name-free as of v1.2.)*
- **R2-12** Catch-all — still-open Round-1 items, none blocking, answer any time: Q-A2 (OneNote cloud newer than the last local snapshot? cloud drive/task log/read-later service still receiving?), Q-B2 (Documents orphan vault), Q-B4 (old seals stay in place?), Q-E2 (portfolio triage pass — I'll assemble the checklist), Q-E4 (the vault of PROJECT-L, a literature-workflow project), Q-E5 (EndNote outside ACE), Q-E6 (removed in the public release), Q-F3 (hard-deadline inventory), Q-G1 (legacy ingestion: exclude vs name-only + one-time classification pass).

---

## ROUND 1 (for reference; rulings in the record below)

## A. Scope and universe

- **Q-A1 [BLOCKING]** Drives `<secondary drive>` and `<archive drive>` exist and hold relevant-looking material (backup and legacy filing trees). In ACE's universe, excluded, or archive-only? **Rec:** archive-only mounts, mapped in a Round-2 mini-survey if included.
- **Q-A2** Off-filesystem surfaces: you pointed me to the OneNote backup store (`%LOCALAPPDATA%\Microsoft\OneNote\16.0\Backup\<notebook>`, snapshots over a year old — now the freshest known local copy, recorded in the atlas). Does a OneNote **cloud** copy exist that is newer still — i.e., did anything get written into OneNote after the last local snapshot? Are the cloud-drive filing tree, the cloud-document task log, or the read-later service still receiving anything? Email/calendar: which client, and is it in ACE's eventual scope (v1.0 prohibits broad integrations in slice 1)?

## B. Hub and storage

- **Q-B1 [BLOCKING]** The hub: fresh Obsidian vault at `ACE_storage/hub/` with `<legacy PKM vault>` mounted read-only as legacy reference (**Rec** — both research mappers independently recommend this), or adopt/clean an existing vault in place? Ruling also settles: [BSP] the spec assumes Obsidian-as-hub although no sustained Obsidian authoring has ever been observed (only a handful of note edits ever) — accept as a bet with a falsification checkpoint (e.g., 30-day review), or reconsider the hub surface now?
- **Q-B2** Fate of the two non-hub vaults: the PROJECT-L vault (an empty per-purpose literature vault) and an orphaned empty vault folder in Documents (unregistered). **Rec:** archive the Documents orphan once Q-B1 lands; the PROJECT-L vault's fate defers to Q-E4 (one ruling covers vault disposal *and* plan absorption).
- **Q-B3** Is Obsidian Sync configured/paired anywhere? ACE_storage uses git as its sync/durability layer — Obsidian Sync on the same vault would create a second writer (multi-writer collision risk). **Rec:** git only; Sync off for the hub vault.
- **Q-B4** Seal artifacts: do future RQGM/anomaly-loop seals land in `ACE_storage/seals/` (my scaffold assumes yes), and do the existing seal folders on the data drive migrate there or stay frozen in place? **Rec:** new seals in ACE_storage; old ones stay put, read-only, indexed by the atlas.

## C. Coexistence with live automation

- **Q-C1 [BLOCKING]** Another meta-system (live on this machine): does ACE **supersede** it, **consume** it as upstream (its own stated model: downstream projects consume from it), or coexist indefinitely? Via what mechanism (skill install / copy / reference)? Until ruled, ACE writes state only to ACE_storage (interim rule in 02/CLAUDE.md).
- **Q-C2 [BLOCKING]** The four legacy scheduled skills (the Claude scheduled-skills folder): are they actually registered and firing (did any of them fire ~07-18)? Which does ACE absorb, retire, or leave alone? Loop-registry authority (which scheduler owns which recurring job) needs one owner.
- **Q-C3** [BSP] Something opened both Obsidian vaults 2026-07-19 — was that you? Any other automated actors (indexers, sync agents) touching these trees I should know about before staleness loops are designed?
- **Q-C4** [BSP] The legacy session-close convention has panels writing durable state directly into project repos (HANDOFF/SESSION_STATE triple), while the ACE target says panels never own durable state (exit packages only). For ACE-scoped work: switch to exit-package-only now, or run both conventions during a transition period? **Rec:** exit-package-only for ACE from day one; legacy convention continues untouched elsewhere until Q-C1 rules.

## D. Spec adjudications (the spec is frozen — these need your sign-off, not mine)

- **Q-D1 [BLOCKING]** `07_RED_QUEEN_VALIDATION.md`: the full v1.0 package that arrived on disk during the session contains the complete contract — evaluator panel, 7 adversarial roles, 10 baseline rounds, attack set A–E, 6 mutation rules, epoch constraints, acceptance thresholds, stop rule — now carried into spec/07 in full (the docx table was its condensed rendering; package wording governs). Confirm the freeze of spec/07 as the Epoch-1 contract. Until then it blocks mutations but cannot approve any. **Q-D1b:** attach v0.1's 100-point scorecard as its measurement rubric? **Rec:** freeze as carried + yes.
- **Q-D2** Three state-machine bug fixes (04 v1.1, all marked PROPOSED): commitment `Canceled` terminal + cancel paths with explicit approval; handoff `RecipientReviewed → Rejected`; red-queen `MutationRejected → FailureIdentified | EpochFrozen`. Approve? **Rec:** yes — all three are unambiguous dead-end repairs.
- **Q-D3** Daily hub review target: **7** min (codex.md, the predecessor contract — not included in the public release) or **10** min (v0.1)? Does "capture <20s" carry into v1.1? And: v1.0 called all burden limits *targets* — approve the v1.1-proposed upgrade to **hard failure gates** (01 §Lineage guard)? **Rec:** 7, yes, and yes — the lineage evidence is exactly what gate semantics exist for.
- **Q-D4** PA-1 WIP limits: restore `1 frontier + 1 institutional` (v0.1 config + your interview's "two-project limit")? Enforced where — hub view warning only, or hard gate on `Proposed → Active`? **Rec:** restore, hard gate, override requires explicit approval.
- **Q-D5** PA-2 write attribution (git authors + audit actor field; staleness reads human signals only). **Rec:** adopt — the research documented six distinct mtime-pollution mechanisms.
- **Q-D6** PA-3 restore v0.1's sanitization allowed/remove lists as the normative checklist behind FR-10. **Rec:** adopt before any clinical-transfer work.
- **Q-D7** The "configured period" after which an active project without a next evidence unit is flagged at-risk: value? **Rec:** 21 days, tunable.
- **Q-D8** Enhancement loops: RQGM (mature) runs the epochs now; the anomaly loop is an early prototype (no published joint-capability demos) — run the anomaly loop as experimental side-loop feeding next-epoch attack cases only (**Rec**), or hold it until it matures, or commit fully?
- **Q-D9** Process acknowledgment: v1.0 froze ~2h after v0.1 mandated weeks of evidence-first work. Accept this research package as the Phase-A evidence retroactively, with the two-door amendment mechanism (operator ruling / RQ epoch) in `00_INDEX.md` as the only reopeners? **Rec:** yes — it makes the inversion explicit instead of silent.
- **Q-D10** [BSP] Rollback semantics (NFR-5): approve the audited-inverse design in `11` §Flow-4 (accepted-then-wrong updates reverse as *new* transitions; history never rewritten)?
- **Q-D11** [BSP] Backpressure: approve the 7/14-day pending-queue aging → auto-degrade-to-`known_stale` rule (11 §Flow-5) as the single-approver overload degradation mode?

## E. Portfolio and pilot

- **Q-E1 [BLOCKING]** First vertical-slice test project — pick one: PROJECT-P, PROJECT-E, **MANUSCRIPT-1**, PROJECT-Q, PROJECT-L. (Clinical-side work is ACE-C-side → disqualified; agent-tooling picks make the first evidence unit self-referential.) **Rec:** MANUSCRIPT-1 or PROJECT-Q — real, deadline-bound, non-clinical-data, honest P0 test.
- **Q-E2** Portfolio triage (one pass, ~15 min): I'll assemble the merged candidate list (OneNote sections + legacy PKM vault projects + Desktop STATUS + `<data drive>` active cluster) into a live/dead/handoff checklist in Round 2 — confirm you want it. Without triage, the hub seeds ~40 zombie projects (the exact failure the legacy review notes recorded).
- **Q-E3** Are the two un-indexed Desktop workstreams (WORKSTREAM-1, WORKSTREAM-2) the same? Merge/renumber per the prior workspace convention?
- **Q-E4** The PROJECT-L vault + the literature-workflow plan note in the legacy PKM vault (the last note ever edited there): superseded by ACE, or absorbed as an early ACE-managed loop (a legacy scheduled skill already automates a variant)?
- **Q-E5** `<reference-manager library folder>` (EndNote): wholly outside ACE (EndNote-owned, name-index only)? **Rec:** yes.
- **Q-E6** *(personal housekeeping item — removed in the public release)*

## F. Capture and deadlines

- **Q-F1 [BLOCKING]** The ONE primary capture path (CLI ruled out; v0.1 syntax dropped; nothing observed capturing today): hotkey→`inbox/` file, Obsidian quick-add, a `/ace-capture` skill in any panel, phone-capable route (email-to-self → inbox)? What does the 20-second path look like on a day away from this machine?
- **Q-F2 [BLOCKING]** Where do new commitments land *today* (email flags? memory? OneNote? nowhere?) — the honest answer calibrates how much trust-debt slice 1 must absorb.
- **Q-F3** Hard-deadline inventory (nothing on disk states any): external professional deadlines; MANUSCRIPT-1 corrections due ([BSP] already resolved?); other recurring or event deadlines. These seed the deadline loop.

## G. Privacy confirmations

- **Q-G1** Legacy ingestion boundary: personal zones (`<personal zone>`, legacy PKM vault personal folders, mixed GTD lists, OneNote personal sections) — **exclude entirely** from ACE indexing, or **name-only** index? And the boundary procedure for ambiguous items (e.g., `<personal zone index>`): one-time classification pass by you? **Rec:** name-only + one-time pass.
- **Q-G2** Remote privacy: the control-plane remote is verified private. Are sibling repos' remotes private too (session-derived operator data must never go public)?
- **Q-G3** [BSP] Clinical *metadata* in ACE-P: are trial/committee identifiers and status metadata (e.g. TRIAL-A, TRIAL-B, COMMITTEE-1) acceptable on the control plane under applicable confidentiality agreements/institutional rules — or must ACE-P hold only your own task layer (e.g. "deliverable due") without study identifiers? **Rec:** get this one explicit before any clinical-adjacent record is ingested.

## H. Strategy (loads 06 — answer when in strategic mode)

- **Q-H1** The 12-month anchor asset (asked in v0.1 Q9, named a trajectory-changing action in the interview, never answered): what is it? The Trajectory evaluator (07) cannot fire without it.
- **Q-H2** PROJECT-W: where does the "prepared and approved" handoff plan live? Recipient? Retained role? Rescue threshold values? (Artifact not found on any mapped drive.)
- **Q-H3** Of v0.1's 52 follow-up questions, the consequential unanswered core: authoritative-source-on-conflict (Q3), realistic protected blocks per work week (Q13), rescue-threshold definition (Q19), silent-handoff-failure detection (Q20), acceptable agent/compute cost (Q41), approved institutional clinical tools (Q43). Answer here or in Round 2.

## Lightning round — one-word confirmables [BSP]

| # | Confirmable | Answer |
|---|---|---|
| L1 | The full `ACE_Final_Design_Package_v1_0` appeared on disk during this session (schemas/templates/07/roadmap — now integrated). Confirm you placed it there? | |
| L2 | You opened Obsidian 07-19? | |
| L3 | *(personal item — removed in the public release)* | |
| L4 | An empty vendor-app folder in Documents (`%USERPROFILE%\Documents\<agent-tool folder>`) = app artifact, ignorable? | |
| L5 | Legacy PKM vault root `Untitled .base/.canvas` ×4 = idle clicks, ignorable? | |
| L6 | An empty `New folder` on an inspected root (2026-06) deletable? | |
| L7 | Out-of-scope personal files found in a repo folder — left for the operator to handle; ACE agents will not touch them (name-only, outside RW roots). Acknowledge? | |
| L8 | *(personal item — removed in the public release)* | |
| L9 | `<an existing backup-like folder>` = current backup of the data drive? (durability question) | |
| L10 | MANUSCRIPT-1 proof corrections: already returned? | |
| L11 | *(personal item — removed in the public release)* | |
| L12 | The operator's personal reference documents and the operator-session audit corpus stay standalone reference (not migrated into ACE)? | |

---

### Rulings record

*(answers land here as they arrive; each consequential ruling also gets a change-log entry in its affected doc)*

| Date | Q | Ruling |
|---|---|---|
| 2026-07-19 | **STORAGE (new)** | Two-plane design: everything primary **locally** (`F:\ACE_local`, local git, NO remote); GitHub `ACE_storage` = control plane for cross-vendor/cross-computer communication + versioning + **hashed metadata**. No clinical or significant-IP content on GitHub. → spec 11 v1.2, store scaffolded. *(FMEA/edge-case/eval + audit layer placement on the control plane is my interpretation of an ambiguous sentence — provisional, pending R2-8.)* |
| 2026-07-19 | Q-B1 | Obsidian confirmed as **control/review/surgical-update hub** — not a daily work surface; work runs in Cowork panels via spec routes. The legacy PKM vault = base-structure reference, stalled from lack of autonomy. Part of the hub lives on GitHub (control-level only). |
| 2026-07-19 | Q-B1 legacy | Non-updating sources (legacy PKM vault, OneNote): monitor as pending/stale; do not sync into the hub. *(ruling stated tentatively; confirm in R2-2 bundle.)* |
| 2026-07-19 | Q-G3 / ACE-C (partial) | Committee/audit-level clinical work stays entirely **ACE-C side, in institution-approved AI tools**. Personal research/proposal/prototyping stays local, out of any GitHub repo. *(Remainder open → R2-11: may clinical trial/committee IDENTIFIERS appear in ACE-P records?)* |
| 2026-07-19 | Q-D11 (spirit) | Single-approver backpressure confirmed as a *core problem ACE must solve* — aging/degradation design stands, mechanism details to Phase 1. |
| 2026-07-19 | Q-C4 | Durable state is written by the **review panel** step, not by cowork/code panels between sessions — exit-package-only for work panels. *(ruling stated tentatively; confirm in R2-2 bundle.)* |
| 2026-07-19 | Q-C1/C2 (partial) | The prior automation is itself a cognitive burden to manage; preference: **task-specific claude/codex cowork operation**. (Registry ownership + firing status still open → R2.) |
| 2026-07-19 | L1 | Confirmed — the operator downloaded/uploaded the full `ACE_Final_Design_Package_v1_0` into reference materials; package governs the previously unanswered spec questions. |
| 2026-07-19 | L2/L5 | The operator opened Obsidian (07-19); the legacy PKM vault was open and idle. No hidden automated actor. |
| 2026-07-19 | L3 | *(personal item — removed in the public release)* |
| 2026-07-19 | L4 | The vendor-app folder = that agent tool's analog of CLAUDE.md (its config home). Keep, ignore. |
| 2026-07-19 | L6 + standing rule | An empty `New folder` on an inspected root is NOT deletable. **Standing rule: never delete any file/folder outside ACE's own stores** — the operator's instruction was inspection-scoped; the "anywhere" generalization is a conservative design extension (confirm in R2-2). → CLAUDE.md + spec 11. |
| 2026-07-19 | L7 | Acknowledged; the files are outside ACE RW roots — agents will not touch them. |
| 2026-07-19 | L9 | `<an existing backup-like folder>` was a one-off copy, NOT a live backup. **A backup mechanism must be built for F: (the drive holding the ACE stores)** → open design item, R2. |
| 2026-07-19 | L10 | MANUSCRIPT-1 corrections are past — dropped as pilot candidate. |
| 2026-07-19 | Q-E3 (partial) | WORKSTREAM-1 (template update) is done, now being tested in use. |
| 2026-07-19 | First use | ACE is needed for **real planning work as soon as the system is built** — Phase-1 slice should serve a real planning session. |
| 2026-07-19 | **R2-1** | **YES** — first `produce` panel = the operator's planning session. Build unblocked. |
| 2026-07-19 | **R2-2** | **Signed off** — in force now: 07 Epoch-1 contract FROZEN (Q-D1); three state-machine fixes (Q-D2); daily 7 min + capture <20s + targets→hard gates (Q-D3); WIP limits 1+1 (Q-D4); write attribution (Q-D5); sanitization checklist (Q-D6); 21-day at-risk (Q-D7); audited rollback (Q-D10); research=Phase-A evidence (Q-D9); hedged rulings confirmed. |
| 2026-07-19 | R2-3 | **YES** — the anomaly loop runs as experimental side-loop beside mature RQGM (Q-D8). |
| 2026-07-19 | R2-5 | Some scheduled skills fire, but they are maintenance-insight/review oriented, **not project/action related — not useful for ACE**. Ruling: coexist untouched; ACE ignores them; ACE owns its own loop registry (Q-C1/C2 closed). |
| 2026-07-19 | R2-6 | Backup is **local** (the operator's preference). Target path → R3-4. |
| 2026-07-19 | R2-7 | Off-machine capture: **email** is acceptable; clinical commitments land in the clinical environment (institution-approved agents monitor — different orchestration); a parallel **ACE-C run exports a handoff package** carrying only task/project-level status updates back to ACE-P (bridge import). Clinical and personal are quite separate. |
| 2026-07-19 | R2-8 | **Confirmed** — quality/FMEA/eval/audit layers on the control plane, WITH the **compliance gate**: marginal cases scrubbed of personal information, PHI/regulated health content, and IP before recording. |
| 2026-07-19 | R2-9 | **Hub vault is LOCAL in F:\ (now `F:\ACE_hub`), NOT in ACE_storage** ("hub_in_ACE_storage is not my intent"). Obsidian Sync serves the vault cross-device. ACE_storage/hub/ superseded-by-move. |
| 2026-07-19 | R2-11 | Clinical identifiers: **initials/alias convention** (existing shortcodes conform; key at `F:\ACE_local\aliases.md`, never mirrored). Third-party names: **scrub** — working tree scrubbed + pushed; history reset pending R3-1 go-ahead. |
| 2026-07-19 | **R3-1** | **"reset"** — executed: ACE remote history replaced with a clean baseline; pre-scrub history kept only as a local branch + bundle on the local plane. |
| 2026-07-19 | R3-2 / scope | ACE must provide the **GTD + filing functions** that PARA/PKM served. Legacy filing directories = **archive for PKM** (RO-REF); **PARA gets reorganized fresh** with new projects and spawns under ACE. (Legacy filing trees on the secondary and archive drives fall under the same archive-reference role.) |
| 2026-07-19 | R3-3 | OneNote: built but unused — the bottleneck is system-maintenance burden, not the GTD method; orphan Documents vault **archived by move** (→ `<archive folder>`). Old seals belong to other projects — stay put. Portfolio triage checklist: **yes, next session**. Hard deadlines: refresh via LLM retrieval on the clinical/professional core + the operator's input **after the panel is built** (surface: cowork/claude-code/Obsidian, builder's choice). |
| 2026-07-19 | R3-3f / Q-G1 | "Legacy personal zones" clarified: the operator-session audit corpus = working habits (sensitive-handling stands). Legacy plans/roles notes in old OneNote/Obsidian = **still current duties and roles, content outdated** — not excluded, but they need organizing in triage sessions. |
| 2026-07-19 | NEW feature | **Morning question list (voice)** — approved concept: short, voice-friendly daily brief with the day's questions/returns (Phase-2 loop; candidate delivery: scheduled morning brief). |
| 2026-08-22 | R5-1 / R5-7 | **"AACE and ACE are essentially the same thing"** — the two meta-loop documents describe ACE; "AACE" was a naming slip by the peer agent that drafted them. No separate substrate; docs re-issued as `spec/meta/ACE_*_v0.2.md`; name retired. |
| 2026-07-19 | **R3-4** | Backup target = **`G:\ACE_backup`** — created; `engine/backup_ace.ps1` written (robocopy add-only + dated git bundles); first backup run verified (17 files). Schedule daily via Task Scheduler in Phase 1. |
| 2026-07-19 | **R3-5** | Obsidian: `F:\ACE_hub` registered in the vault registry and opened. **Obsidian Sync sign-in is the operator's step** (credentials — I don't handle them): Settings → Sync → sign in → Create remote vault ("ACE_hub") → choose what syncs. Confirm when on. |
