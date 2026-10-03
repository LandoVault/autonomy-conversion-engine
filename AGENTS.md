# Agents operating in this repo (Codex, GPT, any non-Claude vendor)

Read **`CLAUDE.md`** — it is the vendor-neutral operating contract for every agent session in this repo (the name is historical; it supersedes `reference materials/codex.md`, not included in the public release). Then follow the read order in `spec/00_INDEX.md`.

Non-negotiables regardless of vendor: no PHI or clinical content; no significant IP or personal content on GitHub (content plane is `F:\ACE_local`, local only); never delete any file or folder outside ACE's own stores; never write outside `ACE`, `ACE_storage`, `F:\ACE_local`; never silently decide anything listed in `spec/10_OPEN_QUESTIONS.md`.

Panel write routes (per the binding writer matrix in `spec/11_STORAGE_AND_FILING.md`):

1. `ACE_storage/outbox/` — exit packages (state proposals + pointers + sha256; no substantive content excerpts);
2. `F:\ACE_local\inbox\` — single capture lines;
3. `ACE_storage/inbox/` — capture metadata stubs (append only);
4. content artifacts — only inside the panel's **declared `F:\ACE_local` write boundary** (produce panels); the exit package references them by path+hash.

Everything else is read-only or off-limits per `spec/08_WORKSPACE_ATLAS.md` access classes.
