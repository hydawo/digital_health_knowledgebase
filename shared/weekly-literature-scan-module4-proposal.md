# Proposed Part E for the weekly literature scan: Module 4 (methods and reviews)

**Status: proposal, 2026-09-03. Not in effect.** The routine's canonical prompt in
[`weekly-literature-scan.md`](weekly-literature-scan.md) is under a reviewed-change rule, and its
publishing exemption covers only the prompt as reviewed. This file is the draft for review. Once
approved, the block below is pasted into the routine in the claude.ai Routines UI and mirrored into
the canonical prompt in the same commit, with a change-history line.

## What changes elsewhere in the prompt

Two small edits outside the new part:

1. The opening line "This repo has three modules with three different literature-tracking conventions"
   becomes "four modules with four conventions", and Part D's scope becomes "all four modules".
2. Part C's rejection step gains one instruction. Papers rejected from Module 3 as "review" are not
   dropped; they are handed to Part E for screening against Module 4's bar. Everything else Part C
   rejects stays rejected.

## The new part

```text
=== PART E - MODULE 4 (Methods and Reviews) ===

Task: scan for new reviews, consensus statements, position papers and research-practice methods
papers about smartphone digital phenotyping and wearable research, and append qualifying ones to
module-04-methods-and-reviews/literature-library.md, following that file's existing convention
(read it first): one table, columns # | Title | Authors | Venue / Year | DOI / URL | OA status | PDF |
What it establishes, identifiers M4-NNN continuing from the last row, and the PDF stored under
module-04-methods-and-reviews/literature/ for open-access papers using the repo's filename
convention.

1. Read module-04-methods-and-reviews/literature-library-index.json (create if missing, with
   {"ids_seen": [], "last_run_date": null}) - dedup ledger.

2. Query NCBI E-utilities, restricted to entries since last_run_date (or the trailing 10 days on
   first run), sorted by date:
   ("digital phenotyping"[tiab] OR "passive sensing"[tiab] OR "mobile sensing"[tiab] OR wearable*[tiab] OR "ecological momentary assessment"[tiab])
   AND (review[ti] OR "scoping review"[tiab] OR "systematic review"[tiab] OR meta-analysis[tiab] OR consensus[ti] OR framework[ti] OR guideline*[ti] OR "reporting standard*"[tiab] OR "best practice*"[ti] OR "lessons learned"[ti])
   AND (research[tiab] OR study[tiab] OR studies[tiab])
   Also screen every candidate Part C rejected this run with reason "review".

3. Relevance bar - KEEP only if ALL of: the paper is about how digital-health research is done
   (adherence and engagement, missing data, ethics and consent, validation frameworks, reporting
   standards, equity and representativeness, privacy, study design), not about one device's accuracy
   or one platform's own analytics; it is a review, meta-analysis, consensus statement, position or
   framework paper, or a methods paper about research practice; peer-reviewed journal article or
   preprint with an abstract; in English. SKIP clinical-outcome reviews that merely use a wearable as
   a measurement (for example a meta-analysis of step counts and mortality), single-platform
   analytics papers (those belong next to the platform in Module 2), and statistics papers with no
   digital-health content. Apply the bar conservatively and say why when excluding.

4. For each keeper, determine OA status and fetch the PDF exactly as Part B does (magic-byte and
   text-extraction check), store it under module-04-methods-and-reviews/literature/, verify the first
   author from the PDF byline, and append one row. "What it establishes" is one plain sentence
   describing what the paper settles or proposes, not the abstract's first line.

5. Update module-04-methods-and-reviews/literature-library-index.json: add new ids to ids_seen,
   set last_run_date to today.

Do not create profiles, comparison tables or a README section for Module 4. Cataloguing only.
```

## Why this is safe under the exemption

The part writes only catalogue rows, PDFs and a ledger. It authors no argument, opens no issue or
pull request, and notifies nobody. Its output is the same class as Part B's.

## Checklist before it goes live

- [ ] Hassan reviews this file.
- [ ] Paste into the Routines UI; mirror into `weekly-literature-scan.md` (prompt block and change
      history) in one commit.
- [ ] Create `module-04-methods-and-reviews/literature-library-index.json` seeded with the ids of the
      baseline rows, so the first run does not re-surface them.
- [ ] Add Part E's output files to the "writes are bounded to" list in `CLAUDE.md`'s exemption text.
