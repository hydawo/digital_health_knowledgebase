# Weekly Literature Scan — routine specification

**Last updated: 2026-09-02.** Canonical, version-controlled copy of the automated weekly
literature-scan routine: what it does, how it is configured, and its **full prompt**.

## Why this file exists

The routine is a **claude.ai/code Routine** — a cloud scheduled agent — **not** a locally-scheduled
task. Its prompt therefore lives only in the claude.ai Routines UI and is **invisible to anyone
working in this repository**, including future Claude sessions. That has already caused confusion
once: the 2026-08-31 session found the routine failing but could not inspect what it was supposed to
do.

**This file is the canonical copy. If the prompt is edited in the UI, update this file in the same
change.** Nothing here executes; it is documentation plus the exact prompt text.

---

## Current configuration

| Setting | Value |
|---|---|
| Type | claude.ai/code Routine (cloud), fires weekly on **Monday** |
| Operating mode | **Fully unattended** — the prompt instructs "Do not ask for confirmation at any step" |
| Repo access | **Push access to this repo's GitHub remote (public)** |
| Environment | "Default" — the environment ID is deliberately not recorded here; find it in the Routines UI |
| Network access | **Custom** allowlist — `eutils.ncbi.nlm.nih.gov`, `export.arxiv.org`, plus the default package-manager list |
| Connectors | Official Anthropic-hosted PubMed MCP (`https://pubmed.mcp.claude.com/mcp`) as a secondary PubMed path |
| Coverage | Module 1 (wearables), Module 2 (phenotyping platforms), **Module 3 (applied studies — triage only)** |

### Publishing-permission status

`CLAUDE.md` carries a hard guardrail requiring the literal phrase **"confirmed, post it"** before
anything is published where other people can see it, and it covers GitHub in full. **This routine is
a named exception**, because it runs unattended and cannot obtain the phrase.

The exemption is **conditional**, and the conditions are the point:

1. **This file is the reviewed specification.** The exemption covers the routine *as specified here* —
   not whatever the prompt says after an unreviewed edit in the claude.ai UI. **That is the main
   reason to keep this file in sync.**
2. **Writes are bounded to logging and bookkeeping** — `research-log.md`, the three `*-index.json`
   ledgers, `_scan-queue.md`, and appends to the Module 1/2 literature libraries. Module 3 profiles,
   `feasibility-matrix.md`, module READMEs and `sources.md` are off limits.
3. **Output is mechanical** — counts, search results, retrieval statuses — not authored argument.

**The exemption lapses** if the routine is ever extended to open issues or pull requests, comment
anywhere, @-mention anyone, or write narrative beyond run logging.

**Do not re-add the PubCrawl connector** without confirming who operates the specific hosted
instance. See `research-log.md` (2026-09-01): an unattended, no-confirmation, push-access routine has
little margin for prompt injection arriving through an MCP tool result from an unverified operator.

---

## Dedup ledgers

| Module | Ledger | Key fields |
|---|---|---|
| 1 | `module-01-wearables/research-library-index.json` | `pmids_seen`, `dois_seen`, `records`, `runs`, `last_run_date` |
| 2 | `module-02-digital-phenotyping/literature-library-index.json` | `ids_seen`, `records`, `runs`, `last_run_date` |
| **3** | **`module-03-applied-studies/literature-index.json`** | `dois_seen`, `pmcids_seen`, `records`, **`rejected`**, `runs`, `last_run_date` |

Module 3's ledger adds a **`rejected`** array. It rejects far more of what it screens than the other
two (reviews, protocols, validation studies, unobtainable full text, duplicate cohorts), and without
recording rejections *with a reason* the routine would re-litigate the same papers every Monday. It
was seeded on 2026-09-02 with all **55 already-profiled studies** (55 DOIs, 54 PMCIDs).

---

## Design decisions worth preserving

1. **The routine triages Module 3; it does not write it.** Modules 1 and 2 catalogue *papers about a
   technology*, which is safely automatable from abstracts. Module 3 asserts *what happened
   operationally in a deployment*, which is not — every figure in its 55 profiles came from full
   text, and the two discovery passes that screened on abstracts alone produced three wrong platform
   attributions out of the first ~12 candidates examined.
2. **One commit and one push, at the very end, covering all three modules.** Module 3 was originally
   drafted with its own commit step and no push; appended after Part D's push, that would have left
   its work committed-but-unpushed every week. Fixed 2026-09-02 by restructuring rather than patching.
3. **Date-sorted, never citation-sorted.** Established empirically: a citation-sorted pass on this
   corpus missed **62 of 64** recent candidates.
4. **Grouped queries for Module 3** (three, not twenty-one) — keeps an unattended run inside rate
   limits and avoids timeouts.
5. **Rejections are recorded with a reason**, not merely excluded.
6. **The queue is a repo file, not a message** — it survives between runs and is reviewable in a diff.
7. **Module 3's inclusion bar is deliberately high, so an empty week is the expected normal case**,
   not a failure. The prompt says so explicitly to stop a future run from loosening the bar to
   produce output.

## Known limitations

- **Three structural discovery blind spots** apply to this routine exactly as to manual passes:
  ordinary-word platform names (PubMed's `[tiab]` does not reliably enforce quoted phrases for
  "AWARE", "CARP", "Polar", "Avicenna"), framework-shaped platforms (CARP publishes under the names
  of apps built on it), and venue-shaped invisibility (AWARE's operational literature is in
  CSCW/IMWUT/UbiComp, which NCBI does not index).
- The known workaround is a periodic **OpenAlex citation-graph pass**, deliberately **not** part of
  this routine — anchor selection requires judgment that should not run unattended, and a poorly
  chosen anchor set skews the yield badly (see
  `module-03-applied-studies/_citation-graph-scan-2026-09.md`).
- The routine cannot obtain paywalled or ACM Digital Library full text, so some genuine Module 3
  candidates will be queued and later prove unbuildable.

---

## Full prompt (canonical — mirror any UI edit back here)

```text
Working directory: repo root (a research knowledge base; see CLAUDE.md for the project's evidence standards - distinguish documented facts from inference, record confidence levels, never manufacture certainty). This repo has three modules with three different literature-tracking conventions - follow each module's own established convention exactly, do not invent a fourth format. Module 3 in particular is triage-only; see Part C.

=== PART A - MODULE 1 (Oura / WHOOP / Apple Watch) ===

Task: scan PubMed for new peer-reviewed papers about Oura, WHOOP, and Apple Watch published/indexed since the last run, and append qualifying ones directly to module-01-wearables/research-library-wearables.md.

1. Read module-01-wearables/research-library-index.json (create it if missing, with {"pmids_seen": [], "last_run_date": null}) - dedup ledger.

2. Query NCBI E-utilities (esearch.fcgi + efetch.fcgi at eutils.ncbi.nlm.nih.gov - public, no auth needed) for each device, restricted to entries published/indexed since last_run_date (or the trailing 10 days on first run):
   - Oura: ("Oura ring"[tiab] OR "Oura Health"[tiab] OR "Oura smart ring"[tiab])
   - WHOOP: ("Whoop strap"[tiab] OR "Whoop band"[tiab] OR "Whoop wearable"[tiab] OR "Whoop 4.0"[tiab] OR "Whoop 5.0"[tiab] OR "Whoop Inc"[tiab])
   - Apple Watch: ("Apple Watch"[tiab]) AND (wearable[tiab] OR cardiac[tiab] OR sleep[tiab] OR "heart rate"[tiab] OR validation[tiab] OR health[tiab])

3. For each PMID not already in pmids_seen, fetch the full record via efetch (XML). Apply this relevance bar - SKIP unless ALL of: device named explicitly in title/abstract; peer-reviewed journal article (not conference abstract/comment/erratum/letter); has an actual abstract; in English.

4. Classify each qualifying paper:
   - Category: "Validation" (accuracy/agreement/sensitivity/specificity/bias/kappa vs a reference standard), "Use-case" (uses device data to study a health outcome/behavior/population), or "Review" (systematic review/meta-analysis/scoping review in title or abstract). Default to "Use-case" if genuinely ambiguous and say so.
   - Sponsorship tier: parse the record's <CoiStatement> field if present. If it explicitly names the vendor (Oura Health, WHOOP Inc, Apple Inc) as funder/employer/consultant/stockholder/advisory-board member, classify Tier A (employment) or Tier B (funding/consulting without employment) with confidence "Verified", quoting the COI text directly. If no CoiStatement, or it doesn't mention the vendor, classify Tier C with confidence "Corroborated" and say explicitly that absence of a disclosed conflict is suggestive, not proof, of independence. Never mark "Verified" without quoting the actual source text.

5. Append each qualifying paper to module-01-wearables/research-library-wearables.md under the correct device section, following the file's existing citation format (authors, year, title, journal - affiliations - funding/COI finding with confidence marker - one-sentence key finding - URL), organized by device then Category then Tier. If that Category structure doesn't exist yet under a device, add it on first run, preserving all existing entry content and confidence markers exactly - reorganize, don't rewrite.

6. Update research-library-index.json: add new PMIDs to pmids_seen, set last_run_date to today.

Do NOT touch module-01-wearables/literature-library.md or module-01-wearables/literature/ in this pass - that file follows a different, PDF-storage convention that has not yet been extended to automated runs; leave it for a future manual or separately-scoped pass.

=== PART B - MODULE 2 (Mobile Digital Phenotyping Platforms) ===

Task: scan for new papers about this module's platforms and append them to module-02-digital-phenotyping/literature-library.md, following that file's EXISTING convention exactly (read the file first and match its format precisely): a table per platform with columns Title | Authors | Venue/Year | DOI/URL | OA status | PDF | Relevance, no sponsorship-tier system (these are software platforms, not vendor-funded device-accuracy studies), and the actual PDF downloaded and stored locally under module-02-digital-phenotyping/literature/<platform-slug>/ for legitimately open-access papers.

1. Read module-02-digital-phenotyping/literature-library-index.json (create if missing, with {"ids_seen": [], "last_run_date": null}) - dedup ledger, tracking PMIDs and arXiv IDs together (e.g. "pmid:12345", "arxiv:2006.11904").

2. Platforms and search approach - query BOTH NCBI E-utilities (PubMed, same eutils.ncbi.nlm.nih.gov endpoints as Part A) AND the arXiv API (export.arxiv.org/api/query, public, no auth) since some of these platforms publish primarily in CS/engineering venues not indexed by PubMed. Restrict to entries since last_run_date (or trailing 10 days on first run):
   - Beiwe: ("Beiwe"[tiab]) AND (Onnela[tiab] OR "digital phenotyping"[tiab] OR smartphone[tiab])
   - RADAR-base: ("RADAR-base"[tiab] OR "RADAR-CNS"[tiab])
   - mindLAMP: ("mindLAMP"[tiab] OR "LAMP platform"[tiab])
   - AWARE Framework: ("AWARE"[tiab]) AND ("mobile sensing"[tiab] OR "context instrumentation"[tiab] OR Ferreira[tiab] OR Kostakos[tiab]) - AWARE alone is too ambiguous, do not search it bare
   - Avicenna Research / Ethica: ("Avicenna Research"[tiab] OR "Ethica Data"[tiab] OR "Ethica app"[tiab])
   - m-Path: ("m-Path"[tiab]) AND (ecological[tiab] OR EMA[tiab] OR "ambulatory assessment"[tiab] OR Mestdagh[tiab] OR Kuppens[tiab]) - m-Path alone is too ambiguous, do not search it bare
   - CARP Mobile Sensing: ("CARP Mobile Sensing"[tiab] OR "CAMS framework"[tiab] OR Bardram[tiab] AND sensing[tiab])
   - MetricWire: ("MetricWire"[tiab])
   - LifeData: ("LifeData"[tiab] OR "RealLife Exp"[tiab]) - note the published literature sometimes renders this "Realtime EXP", which is an error; search both
   For arXiv, use matching plain-text queries (e.g. all:"CARP Mobile Sensing", all:"RADAR-base") since arXiv doesn't support PubMed's [tiab] field syntax - use its own field prefixes (ti:, abs:) instead.

3. Relevance bar - SKIP unless ALL of: platform named explicitly in title or abstract; the paper is substantively ABOUT the platform (methods/architecture, validation, or a deployment/use study using it as the primary instrument) rather than a passing mention; peer-reviewed journal article, arXiv preprint, or JOSS software paper (conference abstracts, comments, and errata excluded); has an actual abstract; in English. Per this module's own file: target only "the strongest and most decision-relevant evidence" per platform, not every incidental mention - if a platform already has 3+ papers in the library and a new candidate adds little beyond what's already there, skip it and say why in the log rather than padding the table.

4. For each qualifying paper, determine OA status using this file's existing confidence markers: attempt to fetch the actual PDF (via Europe PMC's render service for PubMed-indexed papers, or arXiv's own PDF URL for arXiv papers), and verify it's a genuine readable PDF (not an HTML paywall/CAPTCHA page saved with a .pdf name) - check the magic bytes (%PDF) AND, if python3 with pypdf or PyPDF2 is available in this environment, run a text-extraction check to confirm real content; if that library isn't available, fall back to the magic-byte check alone and note the lower confidence. Classify as: "Verified OA" (PDF fetched and inspected directly, confirmed genuine), "OA but not obtained this pass" (metadata says open access but the fetch failed - note why), "Paywalled" (no OA copy found), "Preprint OA, publisher-blocked" (open preprint exists, published version is paywalled - link both), or "Not a formal publication" (grey literature, no full text to obtain). Store successfully-verified PDFs under module-02-digital-phenotyping/literature/<platform-slug>/ using this repo's existing filename convention: <year>-<first-author-lastname>-<venue-abbreviation>-<short-title-slug>.pdf (match the pattern of existing files in that directory). Verify the first author against the publisher PDF byline, not search metadata - PMC's JATS contrib-group ordering for JMIR articles is not stable and sometimes lists handling editors before authors.

5. Append each qualifying paper as a new row to the relevant platform's table in module-02-digital-phenotyping/literature-library.md (create a new platform section only if the platform genuinely has no section yet, matching the existing heading style). Do not edit or remove any existing row's content.

6. Update module-02-digital-phenotyping/literature-library-index.json: add new ids to ids_seen, set last_run_date to today.

=== PART C - MODULE 3 (Applied Wearables and Digital Phenotyping Studies) ===

Your job for this module is TRIAGE, NOT AUTHORSHIP. Do not create or edit any file in module-03-applied-studies/profiles/, and do not modify module-03-applied-studies/feasibility-matrix.md, README.md, or sources.md - a human-initiated pass owns all of those. Append candidates to a queue instead.

Rationale, so this rule is not "optimised away": Module 3 profiles assert what happened operationally in a real deployment, and every figure in its 55 existing profiles came from full text. Abstract-level screening in this project has a measured platform-misattribution rate of roughly 3 in 12 - papers routinely cite a platform they did not deploy. An unattended run holding push access to a PUBLIC repository must not write unverified study claims into it.

1. Read module-03-applied-studies/literature-index.json (it exists; do not recreate it). Skip any candidate whose DOI appears in dois_seen, whose PMCID appears in pmcids_seen, or that appears in the rejected array.

2. Search NCBI E-utilities (and the arXiv API for CS/engineering venues), restricted to entries since last_run_date (or the trailing 10 days if last_run_date is null). Use these three grouped queries rather than one per technology - grouping keeps the run inside rate limits:

   DEPLOYMENT BLOCK (reuse in all three):
   (feasibility[tiab] OR adherence[tiab] OR retention[tiab] OR compliance[tiab] OR "wear time"[tiab] OR deployment[tiab] OR attrition[tiab] OR "data completeness"[tiab] OR "missing data"[tiab] OR acceptability[tiab] OR usability[tiab] OR engagement[tiab] OR longitudinal[tiab])

   C1 - consumer/research wearables:
   ("Apple Watch"[tiab] OR Fitbit[tiab] OR Garmin[tiab] OR "Oura ring"[tiab] OR "Whoop strap"[tiab] OR "Whoop band"[tiab] OR "Galaxy Watch"[tiab] OR Withings[tiab] OR Empatica[tiab] OR ActiGraph[tiab] OR Axivity[tiab] OR GENEActiv[tiab] OR Movesense[tiab] OR "Polar H10"[tiab] OR "Polar Vantage"[tiab]) AND DEPLOYMENT BLOCK

   C2 - digital phenotyping platforms:
   (Beiwe[tiab] OR "RADAR-base"[tiab] OR "RADAR-CNS"[tiab] OR mindLAMP[tiab] OR "AWARE framework"[tiab] OR "Avicenna Research"[tiab] OR "Ethica Data"[tiab] OR MetricWire[tiab] OR "m-Path"[tiab] OR "CARP Mobile Sensing"[tiab] OR LifeData[tiab] OR "RealLife Exp"[tiab]) AND DEPLOYMENT BLOCK

   C3 - arXiv, same two term sets using arXiv's own field prefixes (ti:, abs:, all:), since several of these platforms publish in CS venues PubMed does not index.

   Sort results by DATE, not by citation count or relevance. This is not a preference: a citation-sorted pass on this same corpus missed 62 of 64 recent candidates when it was tested.

3. Screen each candidate. Keep it only if ALL of:
   - a digital-health context term is present (wearable, smartphone, sensor, actigraphy, EMA/ESM, remote monitoring, digital phenotyping, mHealth);
   - at least TWO distinct deployment-reality signals appear (retention/attrition, adherence/compliance/wear time, feasibility/acceptability, data completeness/missingness, technical failure);
   - an actual participant cohort exists.
   REJECT reviews, meta-analyses, scoping reviews, protocol papers with no results, pure device-validation/accuracy studies, and platform-architecture or methods papers with no deployment cohort. All of these are explicitly out of Module 3 scope per CLAUDE.md.

   Known false-positive traps - several platform names are ordinary English words or common surnames, and PubMed's [tiab] matching does not reliably enforce the quoted phrase for them: "Polar" (polar bears/regions/polar coordinates), "Avicenna" (the historical physician), "AWARE" and "CARP" (ordinary word; a fish), "m-Path", "Oura", "Samsung". For any hit on these, require a co-occurring digital-health context term before keeping it, and if the platform is not named unambiguously in the abstract, reject it as no-cohort rather than guessing.

4. Append surviving candidates to the "## Pending" table in module-03-applied-studies/_scan-queue.md. Append only - never overwrite or reorder existing rows. Match the table's existing columns exactly:
   | Found | DOI | PMCID | Title | Venue / year | Apparent technology | Signals | OA |
   Use today's date for Found. In "Apparent technology", record what the SEARCH suggests, not a claim about what the study deployed. Below the table, ensure this line is present verbatim (add it once if absent):
   Platform attribution is Reported - verify from full text before profiling.

5. Record every rejection in the ledger's rejected array as {"doi": ..., "pmcid": ..., "reason": ...} with a one-word reason from: review, protocol, validation, architecture, no-cohort. This prevents the same out-of-scope paper being re-screened every week.

6. Update module-03-applied-studies/literature-index.json: set last_run_date to today, and append a runs entry with counts (searched / screened-in / queued / rejected). Do not remove or alter existing records entries.

=== PART D - LOGGING, COMMIT AND PUSH (all three modules) ===

1. Append ONE combined dated entry to shared/research-log.md in this file's established style (match existing entries' format), covering all three modules: how many papers each search returned (Module 1 per device, Module 2 per platform, Module 3 per grouped query), how many passed the relevance bar (with category breakdown for Module 1, OA-status breakdown for Module 2, queued-vs-rejected breakdown for Module 3), and a one-line reason for any notable exclusions. If a module found zero qualifying papers, say so in one line rather than omitting it - for Module 3 in particular, an empty week is the expected normal case given its deliberately high inclusion bar, not a failure.

2. If NCBI E-utilities or the arXiv API are unreachable or rate-limited for a given module, log that as a partial/failed run for that module specifically in research-log.md with the error, and do NOT update that module's last_run_date (so the next run retries the same window). The other modules should still proceed normally and update their own state if they succeeded.

3. Commit ALL changes across all three modules in ONE commit, with a message summarising each, e.g.:
   "Weekly scan: Module 1 +N papers (Oura x, WHOOP y, Apple Watch z), Module 2 +M papers (platform breakdown), Module 3 +Q queued / R rejected"
   Note explicitly in the message if a module found nothing new. Then PUSH to origin main. If truly nothing changed in any module, skip the commit and push entirely.

Do not ask for confirmation at any step - this must run fully unattended. Apply every relevance bar conservatively: when genuinely unsure whether a paper belongs, exclude it and say why rather than including it.
```

---

## Change history

| Date | Change |
|---|---|
| 2026-09-02 | **Module 3 added as Part C (triage-only).** Restructured the prompt so logging/commit/push became Part D covering all three modules — the initial draft had Module 3 appended after Part C's push with its own commit and no push, which would have left its work unpushed every week. Also: LifeData added to Part B; the JMIR byline-ordering trap added to Part B step 4; the Module 3 false-positive note corrected from "Europe PMC does not honour phrase quoting" to describe PubMed `[tiab]` behaviour, since that is the API the routine actually calls. |
| 2026-09-01 | Network egress fixed at the environment level (Custom allowlist) rather than by adding a third-party MCP connector; PubCrawl removed. See `research-log.md`. |
