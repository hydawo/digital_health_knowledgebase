End-of-session wrap-up: compile, persist durable memory, commit, push, write a handoff file.

**Usage:** `/logoff`

Read [`../shared_context/session_close.md`](../shared_context/session_close.md) first — this file implements that shared four-phase contract with this project's specifics.

Invoking this command is itself the user's authorization to commit and push without asking again each time — don't re-confirm on every run. Still apply ordinary judgment: if something looks wrong (see the secret-scan check below), stop and flag it instead of proceeding. This repo has a GitHub remote (`digital_health_knowledgebase`, public) configured, so `/logoff` pushes after committing.

---

## Phase 1 — Compile the session

Review the full conversation for: which module(s) (`module-01-wearables/`, future modules) were touched, what research was added or revised, and any claims that changed confidence status (Verified/Corroborated/Reported/Unclear). Keep it to a short plain-language summary — this feeds both the commit message and the handoff file.

If `shared/research-log.md` wasn't already updated during the session with what changed, update it now — per this project's own Maintenance section in `CLAUDE.md`, material changes belong there. Check `shared/unresolved-questions.md` too, and update it if the session opened or closed any open questions.

## Phase 2 — Persist durable facts to memory

This project already has strong per-module continuity (module folders, `shared/research-log.md`, `shared/unresolved-questions.md`, `shared/terminology.md`), so memory here should be reserved for things that outlive any single research pass:
- Corrections or preferences about research standards or evidence-confidence conventions not yet reflected in `CLAUDE.md`
- Durable facts about how downstream projects actually use this knowledge base (a new consumer, a new way it gets referenced)
- New external references (a source worth returning to repeatedly)

Read `MEMORY.md` first; only write what isn't already captured durably in `CLAUDE.md` or the relevant module's own files. If nothing clears that bar, say so explicitly.

**Vault check (session_close.md phase 2b) — two parts, two bars:**
- **`../brainiac/activity/digital_health_knowledgebase.md` (routine, low bar):** if this session did real research work, update this project's rolling activity note with which module(s) are active and recent progress, sanitized (no unpublished competitive/strategic framing beyond what's already evidence-based and neutral per this project's own scope rule) — plain-language "what's being researched," not a data dump. Skip only for sessions with nothing another project would benefit from knowing.
- **`../brainiac/patterns/` or `../brainiac/conventions/` (rare, narrow bar):** if this session surfaced a research-methodology observation that's genuinely cross-project (evidence-confidence tiering, primary-source verification approach), log it there too. This project has no `writeup` skill of its own, but the same content-proofing filter that skill would apply still governs anything written to the vault — apply it here regardless.

## Phase 3 — Git commit and push

- **Secret-scan check:** before staging, scan the changed/untracked file list for anything that looks like a credential (`.env`, `*credentials*`, `*secret*`, `*apikey*`, `*token*`, `*.pem`, `*.key`).
- If `git status --short` is empty, skip to Phase 4.
- `git diff --stat` (and `git diff` for smaller diffs) to understand what actually changed.
- Stage the reviewed set of files, write a commit message reflecting the actual substance, matching this repo's existing commit style (`git log --oneline -5`). Sign off with `Co-Authored-By: Claude <noreply@anthropic.com>`.
- Commit, then push to `origin`. If push fails (no upstream, auth failure, diverged history), stop and report the exact issue rather than forcing past it or force-pushing.

## Phase 4 — Session handoff file

Write `.claude/session-logs/YYYY-MM-DD-HHMM.md` (create the folder if needed): what was accomplished, decisions made, open threads (cross-reference `shared/unresolved-questions.md` rather than duplicating it), and concrete next steps.

---

## Report

```
## Session saved

### Committed
[commit hash] "[commit message subject line]"
[N] files changed — pushed to origin
(or: "Nothing to commit.")

### Memory updated
- [New/updated memory file] — [one-line reason]
(or: "Nothing new met the bar for persistent memory this session.")

### Vault
- Activity: [updated brainiac/activity/digital_health_knowledgebase.md — one-line summary, or "skipped, nothing worth another project knowing"]
- Conventions/patterns: [file touched — one-line reason, or "nothing cross-project this session"]

### Handoff
Saved to `.claude/session-logs/[file].md`
```
