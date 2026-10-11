# Agents and their rules

**Last updated: 2026-10-11.** Every agent that works on this knowledge base, what it is for, what it
may and may not change, and where its full instructions live. The agent names (scout, detective and
so on) are descriptive labels; in practice each specialist is a Claude agent launched with a task
prompt that follows the rules below.

## Rules every agent follows

These come from `CLAUDE.md` and apply to all of them.

- Primary sources first: vendor and developer documentation, code repositories, FDA records, and the
  papers themselves. Secondary sources only when primary ones run out.
- Every claim carries a confidence marker: **Verified**, **Corroborated**, **Reported** or
  **Unclear**. A vendor's statement about itself is Corroborated at most.
- When sources disagree, record both. Never pick one silently.
- Every fact written must come from a source read in that session. Never reconstruct a title,
  author, date or figure from memory or a filename.
- No accounts, sign-ins, form submissions or getting past bot checks.
- No GitHub issues or comments anywhere. New issues or replies in the Beiwe repositories need Hassan's
  explicit "confirmed, post it".
- No em dashes in new text.

## The agents

### 🗓️ Monday scout (weekly literature scan)

- **What it is:** a claude.ai cloud routine that fires every Monday, fully unattended.
- **Full prompt:** [`weekly-literature-scan.md`](weekly-literature-scan.md), Parts A to D. Any edit to
  the routine in the claude.ai UI must be mirrored there.
- **Does:** searches PubMed and arXiv by publication date for papers since its last run. Appends
  Module 1 papers (Oura, WHOOP, Apple Watch) and Module 2 papers (each platform) to their libraries,
  with a sponsorship tier read from the paper's conflict-of-interest text. Adds Module 3 candidates to
  `_scan-queue.md` and records every rejection with a reason. Writes one research-log entry, then one
  commit and one push.
- **May change:** the three `*-index.json` ledgers, the Module 1 and 2 libraries (append only),
  `_scan-queue.md`, `research-log.md`.
- **Must not change:** any profile, comparison or feasibility matrix, README or `sources.md`. It never
  writes a Module 3 profile, because a study's figures must come from the full paper.
- **Checked by:** the coordinator at every merge, using
  [`verify_scan_additions.py`](verify_scan_additions.py) (procedure in the scan file).

### 🔎 Device detective

- **Does:** checks what wearable makers actually document: developer docs, API references, product
  pages, code repositories, FDA records. Settles conflicts between a vendor's own pages and checks
  whether products and tools are still maintained.
- **May change:** only the Module 1 device profiles it is assigned for that task, and only when the
  coordinator gives it ownership of them.
- **Returns:** one row per question or finding (resolved, partly, still open, or rejected with a
  reason), new source rows for the coordinator to add to `sources.md`, and proposed edits for files
  it does not own.

### 📖 Literature reader

- **Does:** searches PubMed, PMC and Europe PMC for validation studies; reads full texts where
  available and every funding and conflict-of-interest statement; files open-access PDFs in the
  device's `literature/` folder.
- **May change:** `validation-evidence.md`, the research library and its index, the PDF catalogue,
  and the device profiles it is assigned.
- **Extra rule:** "No study found" is a valid answer only after a documented search, with the search
  strings recorded.

### 📱 Platform inspector

- **Does:** reads the code repositories, manuals and app-store listings of the phone research
  platforms. Answers maintenance, hosting, licensing and background-collection questions.
- **May change:** the Module 2 profiles, its `sources.md`, and in a repair pass the Module 2
  comparison matrix and README.
- **Extra rule:** for Beiwe, use the beiwe-backend wiki and forest.beiwe.org before the repositories.

### ⚙️ Systems analyst

- **Does:** maps the Android and iPhone rules that limit background data collection, version by
  version, and reads full study papers to pin down dates and completeness figures.
- **May change:** nothing by default. It returns findings, and the coordinator writes them up (for
  example [`os-background-limits.md`](os-background-limits.md)).

### 🏥 Study checker (repair pass)

- **Does:** re-reads Module 3 study papers to check sample sizes, retention, completeness, durations,
  funding and first authors, and checks the feasibility matrix against the profiles.
- **May change:** Module 3 profiles, the feasibility matrix, its README and `sources.md`, and the
  Module 4 catalogue.
- **Extra rule:** verify the first author from the paper's byline, never search metadata.

### 📌 Fact keeper

- **What it is:** the session that works the weekly `facts-monitor` GitHub issue.
- **Does:** re-reads every page the weekly check flagged (quote missing or reworded, page changed,
  dead link, check by hand, overdue), updates the affected facts in `facts/<company>.yaml` with a
  fresh exact quote and date, regenerates the tables, fixes any profile prose the change
  contradicts, logs the change and closes the issue.
- **May change:** the fact records, the generated files (only by running `generate.py`), and the
  profiles' prose where a fact changed.
- **Rules:** [`../facts/README.md`](../facts/README.md). A quote is always copied from the live page,
  never reconstructed. A company's own compliance claim stays Corroborated without independent evidence.

### 🔬 Fact researchers A and B (baseline run)

- **Does:** fill one company's fact record from scratch, independently of each other, so a fact
  either missed or misread by one shows up as a disagreement.
- **May change:** only their own draft, `facts/_drafts/<company>/A.yaml` or `B.yaml`.
- **Rules:** [`../tools/facts/prompts/researcher.md`](../tools/facts/prompts/researcher.md). Every
  quote copied from the page and probed with `quote_probe.py`.

### 🕳️ Gap hunter (baseline run)

- **Does:** looks for what both researchers would miss: changelogs, deprecation notices, developer
  forums, FDA and recall databases, partner press releases, papers describing access.
- **May change:** only `facts/_drafts/<company>/gaps.md`.
- **Rules:** [`../tools/facts/prompts/gap-hunter.md`](../tools/facts/prompts/gap-hunter.md).

### ⚖️ Judge (baseline run)

- **Does:** merges A, B and the gap hunter into `facts/<company>.yaml`, keeps genuine disagreements
  as conflicts, re-probes every quote, and lists the profile and matrix lines the record contradicts.
- **May change:** the company's record and `facts/_drafts/<company>/judgement.md`.
- **Rules:** [`../tools/facts/prompts/judge.md`](../tools/facts/prompts/judge.md).

### ✏️ Profile corrector (after each batch)

- **Does:** brings one company's profile into line with its committed record, checking each judge
  claim against the record first, and adds the generated facts block. Lists the matrix and README
  lines that need the same fix; one agent per module then applies those.
- **May change:** that one profile only.
- **Rules:** [`../tools/facts/prompts/profile-corrector.md`](../tools/facts/prompts/profile-corrector.md).

### 🧐 Independent reviewer

- **Does:** starts with no earlier conclusions and assumes nothing is correct until checked. Fact-checks
  every recent change, a stratified sample from both comparison matrices, a seeded random sample of
  Module 3 profiles, at least 50 bibliography rows against Crossref, every link, internal consistency
  across profiles, matrices and the explorer, research programs and academic data access for every
  device and platform, and every open question it can answer.
- **May change:** only its own report, in [`reviews/`](reviews/). Every correction goes to Hassan
  before anything in the library changes.
- **Output:** findings ranked Critical, Major, Minor or Note, each with the file and line, what the
  file says, what the source says, the source, and proposed replacement text.

### 🧑‍💼 Coordinator

- **What it is:** the Claude Code session Hassan works with directly.
- **Does:** plans the work, launches the other agents, gives each one a separate set of files so two
  agents never edit the same file at once, and merges the scout's weekly runs.
- **Before anything is committed:** re-checks agent output against sources (Crossref for every new
  bibliography row, spot checks of the most consequential claims), records corrections in
  `research-log.md` rather than overwriting silently, updates `unresolved-questions.md`, rebuilds
  the explorer with `explorer/build.py`, and republishes the web pages.
- **Also:** runs reader-facing prose through the humanizer rules, and never posts anything on
  Hassan's behalf without his approval.

## Repair pass agents (2026-10-10)

After the independent review, four agents applied its findings, each owning separate files:
Module 1 access vendors (Fitbit/Google, Garmin, Samsung, Apple, Withings, Polar, intermediaries);
Module 1 other devices and the Module 1 libraries; all of Module 2, including a rebuild of its
comparison matrix from the profiles; Module 3 and Module 4. Each had to re-verify every finding
against its source before applying it, and return a row per finding marked Applied, Applied with
changes, Rejected or Could not verify. A fifth pass rebuilds the Module 1 comparison matrix and
the atlas once the Module 1 profiles are settled.
