---
name: add-paper
description: Manually add one paper to the knowledge base (Modules 1 to 4) from a DOI, PMID, PMCID, arXiv ID, URL or local PDF. Decides which module(s) it belongs to, stores the PDF if open access, writes the entry in each module's own format, updates the dedup ledgers and research log, then commits and pushes. Use when Hassan says "add this paper", "file this paper", "put this in the knowledge base", or pastes a paper link and asks to add it.
---

# Add a paper by hand

Hassan supplies one paper (or a short list). This skill files it the way the weekly scan and the
earlier manual passes did. Each module has its own format. **Read the target file and copy its
existing entries' format exactly. Never invent a fourth format.**

Input can be any of: DOI, PMID, PMCID, arXiv ID, a publisher URL, or a path to a PDF Hassan already
has. He may add a hint ("this is a Garmin sleep paper", "Module 3"). Treat the hint as a starting
guess and check it against the paper.

## 1. Identify the paper

- Resolve metadata from a primary index, not a search snippet:
  - DOI: `https://api.crossref.org/works/<doi>`
  - PMID or PMCID: Europe PMC, `https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:<pmid>&format=json&resultType=core` (use `PMCID:<id>` for a PMCID)
  - arXiv: `https://export.arxiv.org/api/query?id_list=<id>`
- Record title, first author, year, journal, DOI, PMID, PMCID.
- **Take the first author from the PDF byline once you have the PDF.** PMC's JATS ordering for JMIR
  papers sometimes lists editors first.

## 2. Check it isn't already in

Search all three ledgers, and grep the libraries for the DOI and the title:

| Module | Ledger | Look in |
|---|---|---|
| 1 | `module-01-wearables/research-library-index.json` | `dois_seen`, `pmids_seen`, `records` |
| 2 | `module-02-digital-phenotyping/literature-library-index.json` | `ids_seen` (`pmid:`, `arxiv:` and `doi:` prefixes), `records` |
| 3 | `module-03-applied-studies/literature-index.json` | `dois_seen`, `pmcids_seen`, `records`, `rejected` |
| 4 | `module-04-methods-and-reviews/literature-library-index.json` | `ids_seen` (`doi:` prefix) |

If it's already there, say where and stop. Exception: Hassan wants it in another module, or a
Module 3 rejection was for `unobtainable` and he now has the PDF.

## 3. Get the full text

- Try in order:
  1. Europe PMC `https://europepmc.org/articles/<PMCID>?pdf=render` or `fullTextXML`
  2. arXiv PDF
  3. The publisher's open-access PDF
- Then check it's real: the first bytes must be `%PDF`, and `pypdf` text extraction must return the
  paper's own text. A paywall or CAPTCHA page saved as `.pdf` doesn't count.
- If Hassan gave a local PDF, use it, but run the same checks.
- If you can't get an open copy, **don't bypass paywalls or bot checks.** Record the OA status
  (Verified OA / OA but not obtained this pass / Paywalled / Preprint OA, publisher-blocked / Not a
  formal publication). Ask Hassan whether he has a copy, especially if the paper is a Module 3
  candidate.
- PDF filename convention: `<year>-<firstauthor>-<venueabbrev>-<short-title-slug>.pdf`, lowercase.
  Match the files already in the target folder.
- A paywalled PDF Hassan supplies through his own access is for reading only. Don't commit it to
  this public repo. Mark it `Paywalled` with a note that it was read from his copy.

## 4. Decide where it belongs

Read the abstract and Methods. A paper can belong in more than one module.

- **Module 1: the paper is about a wearable** (validation against a reference, a use-case study using
  the device's data, or a review).
  - Category: Validation, Use-case or Review.
  - Sponsorship tier from the conflict-of-interest and funding statements in the full text:
    - **A** if vendor employees are authors.
    - **B** if the vendor funded the work or an author has a vendor tie (advisory board, joint lab).
    - **C** if neither.
  - **Quote the statement.** Mark the tier Verified only if you quoted the actual disclosure. Without
    full text, mark C as Corroborated and say that the absence of a disclosed conflict suggests
    independence but doesn't prove it.
- **Module 2: the paper is substantively about a phenotyping platform** (methods or architecture,
  validation, or a deployment using it as the main instrument). A passing mention doesn't count.
- **Module 3: a real deployment with a cohort that reports how the deployment went** (recruitment,
  retention, adherence or wear time, completeness, technical failures). Apply
  `module-03-applied-studies/_screening-and-profile-rules.md`, Part A, in full. It needs the full
  text. **Check from Methods which device or platform was actually deployed.** Abstracts misattribute
  this about 3 times in 12.
- **Module 4: the paper is about how digital-health research is done, not about one technology or
  one deployment.** This covers reviews, meta-analyses, consensus and guideline statements, ethics
  and position papers, and research-practice methods papers (adherence, missing data, validation
  frameworks, reporting, equity, privacy). See `module-04-methods-and-reviews/README.md` for scope.
  A multi-device review or recommendation goes here, not in Module 1. A review rejected from Module
  3 as `review` usually belongs here too.
- **The technology isn't profiled yet.** Still file it, under a new `literature/<slug>/` folder and a
  new section in the Module 1 or 2 library. Note in the research log that it's a candidate for a new
  profile. For Module 3, flag it as a Module 1/2 expansion candidate. Don't write a Module 3 profile
  for an unprofiled technology.
- **None of the above** (for example a general methods paper): tell Hassan and suggest where it
  could go. Don't force it in.

If the module or tier is a judgment call, say so in one or two sentences and ask before writing.

## 5. Write the entries

**Module 1**
- Add the PDF to `module-01-wearables/literature/<device-slug>/`.
- For Oura, WHOOP and Apple Watch, add the full citation entry under the right device, tier and
  category in `research-library-wearables.md`. Format: authors, year, title, journal, affiliations,
  funding or COI finding with confidence marker, one-sentence key finding, URL.
- Add the matching row to `literature-library.md`.
- For other devices, add only to `literature-library.md`, following the Movesense and Empatica
  section. Create a device section if none exists.
- Add a `records` entry to `research-library-index.json` with the same fields as the last record:
  pmid, doi, pmcid, title, year, device, category, tier, tier_confidence, pdf, pdf_status, source.
  Use source `manual add-paper <date>`. Add the PMID and DOI to the `*_seen` arrays.

**Module 2**
- Add the PDF to `module-02-digital-phenotyping/literature/<platform-slug>/`.
- Add a row to that platform's table in `literature-library.md`: Title | Authors | Venue/Year | DOI/URL | OA status | PDF | Relevance.
- Add the id to `ids_seen` and a `records` entry to `literature-library-index.json`.

**Module 4**
- Add the PDF to `module-04-methods-and-reviews/literature/` if it's open access.
- Add a row after the last `M4-NNN` row in `literature-library.md`, numbered next in sequence:
  # | Title | Authors | Venue / Year | DOI / URL | OA status | PDF | What it establishes. "What it
  establishes" starts with a topic label used by other rows (Adherence and engagement, Missing data
  and data quality, Ethics and consent, Validation frameworks, Reporting guidelines, and so on). It
  then says in one plain sentence what the paper settles or proposes. If you wrote it from the
  abstract only, say so.
- Add `doi:<doi>` to `ids_seen` in `literature-library-index.json`, which uses a one-space indent.
- Update the paper and paywalled counts in the module `README.md` status line and in `explorer/kb-map.html`.

**Module 3, included**
1. Write the screening extraction to `module-03-applied-studies/_screening-reports/<date>-manual-<slug>.md`, using Part A's field list.
2. Write the profile to `module-03-applied-studies/profiles/<slug>.md` with the CLAUDE.md Module 3 template, following Part B's writing rules exactly. Use the two exemplar profiles named there. **Every number must come from the full text, or be written as "not reported".**
3. Add a row to `feasibility-matrix.md` and the sources to `sources.md`.
4. Store the PDF under `module-03-applied-studies/literature/` if it's open access.
5. Add the DOI and PMCID to the ledger's `*_seen` arrays, and a `records` entry with `"profiled": true` and source `manual add-paper <date>`.
6. Link the new profile from the related Module 1/2 profile's evidence section if that section lists Module 3 studies.
7. Rebuild the explorer with `python3 explorer/build.py`. Tell Hassan the KB Explorer page needs republishing; republish it if he says yes.

**Module 3, rejected:** add `{"doi", "pmcid", "reason"}` to `rejected` with one reason code from Part A, and add the DOI to `dois_seen`.

**Module 3, no full text yet:** append a row to the Pending table in `_scan-queue.md`, matching its columns, with the technology marked as what the search suggests.

## 6. Log, check, commit

1. Append a short dated entry to `shared/research-log.md` in its existing style. Say which paper,
   which module(s), the OA status, the tier and confidence, and anything uncertain.
2. Commit with a message like `Add paper: <first author> <year>, <short title> (Module N)`.
3. Run the checker against that commit. It compares title, first author, year and journal with
   Crossref, and prints COI passages:
   ```
   python3 shared/verify_scan_additions.py HEAD~1 HEAD
   ```
   Fix any FLAG, amend or add a fix commit, then push. Pushes in this repo aren't gated.
4. Report back in a few lines: where it went, the OA status, the tier, and anything Hassan should look at.

## Rules that always apply

- No em dashes or en dashes in anything you write.
- Don't create accounts, sign in, submit forms or get past bot checks to fetch a paper.
- Never send Hassan's email address or any personal identifier to a lookup service. Unpaywall requires one, so use OpenAlex or Crossref instead.
- Don't cite the private `beiwe-discussions` repo.
- Don't upgrade any confidence marker beyond what the quoted source supports.
- For several papers at once, work through them one by one. Use subagents only if Hassan asks, and
  keep to about four at a time.
