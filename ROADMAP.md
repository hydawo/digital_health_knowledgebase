# Roadmap

**Last updated: 2026-10-10.** What is done, what is running, and what comes next. Detail for each
item lives in the file it links to; `shared/research-log.md` has the dated history.

## Waiting on Hassan

| Item | Where |
|---|---|
| Point the Monday scan routine at `main` instead of a new branch each run | claude.ai routine settings; see `shared/weekly-literature-scan.md` |
| Add `www.ebi.ac.uk`, `pmc.ncbi.nlm.nih.gov` and `www.ncbi.nlm.nih.gov` to the scan routine's network allowlist so it can save PDFs | claude.ai environment settings |
| Four scope decisions: Q109, Q114, Q122, Q123 | `shared/unresolved-questions.md`, "Needs a decision" |
| Move the Wearable Data Atlas's public share link to the latest version | the Atlas page's Share menu |

## In progress

### Vendor fact records, baseline research run (sub-project 2)

Fill every company's record in `facts/` from scratch: for each company, two independent
researchers and a gap hunter, then a judge who merges, keeps disagreements as conflicts and checks
every quote. See `facts/README.md` and `shared/agents.md`.

| Batch | Companies | Status |
|---|---|---|
| 1 | Oura, WHOOP, Apple, Fitbit / Google, Garmin, Samsung, Empatica, Withings, Beiwe, RADAR-base | Done 2026-10-10: 436 facts, 275 Verified. Profile and matrix corrections listed in each `judgement.md`, not yet applied |
| 2 | Polar, Ametris, Axivity, Activinsights, Movesense, mindLAMP, AWARE, Avicenna, MetricWire, m-Path, CARP, LifeData, Evidation | Next |
| 3 | Fitabase, Labfront, Fitrockr, Terra, Thryve, Ultrahuman, Sensor Bio, RingConn, Circular, Zepp, Verily, Purple Robot | After batch 2 |

After each batch: generate the tables, opt the completed profiles in to the generated facts block,
and replace the hand-written research-program tables in both comparison matrices with the
generated ones.

## Next

1. **Vendor confirmation sheets (sub-project 3).** One page per company listing what is on record,
   for the vendor to confirm or correct. Hassan reviews and sends each one ("confirmed, send it").
   Answers become `vendor_confirmation` sources.
2. **Re-check schedule.** Weekly: the fact monitor (running, GitHub Actions, Mondays). Monthly:
   re-verify pricing, access and terms facts as their `recheck_by` dates fall due. Quarterly: an
   independent review like `shared/reviews/2026-10-10-independent-review.md`.
3. **Module 3 queue.** Screen the 18 queued candidates, starting with Zawada 2025 (the first Beiwe
   deployment mostly after the heartbeat change); write the leftover profiles (Vidal 2022, Nock
   2026, Weingarden 2025) and the two ALS addenda.
4. **Fitbit profile follow-up** after 2026-10-30, when the legacy Web API is turned off.
5. **Module 4 scan proposal:** approve or drop `shared/weekly-literature-scan-module4-proposal.md`.

## Later

- An OpenAlex citation-graph pass for Module 3 (the weekly scan's known blind spots).
- Module 4 write-ups beyond the catalogue.
- Future modules listed in `CLAUDE.md` (analytics tools, data aggregation platforms, and others),
  only when asked.

## Done

| Date | What | Record |
|---|---|---|
| 2026-10-10 | Vendor fact records built: schema, 35 starter records, validator, weekly checker, generator, tests, GitHub Actions monitor; Oura pilot (18 facts); first live run and first issue closed | `facts/README.md` |
| 2026-10-10 | Repair pass: every Critical and Major review finding fixed or rejected with a source; both comparison matrices and the atlas rebuilt from the profiles | `shared/research-log.md` |
| 2026-10-10 | Independent review: 742 claims checked, 140 wrong | `shared/reviews/2026-10-10-independent-review.md` |
| 2026-10-10 | Weekly scan output checked; merge-and-check step and `verify_scan_additions.py` added | `shared/weekly-literature-scan.md` |
| 2026-10-10 | Agent roles and rules written down; architecture page with diagrams | `shared/agents.md` |
| 2026-10-09 | Open questions regrouped by who can close them; 34 researched | `shared/unresolved-questions.md` |
| 2026-10-09 | Six weeks of unmerged scan branches consolidated into `main` | `shared/research-log.md` |
| 2026-10-09 | Android and iOS background-limit reference | `shared/os-background-limits.md` |
| 2026-09-03 | Module 4 created; explorer published; Module 3 coverage pass (65 profiles) | `shared/research-log.md` |
| 2026-08-31 | Module 3 initial build | `module-03-applied-studies/README.md` |
| 2026-08-24 | Modules 1 and 2 initial research | module READMEs |
