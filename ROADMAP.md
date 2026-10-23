# Roadmap

**Last updated: 2026-10-22.** What is done, what is running, and what comes next. Detail for each
item lives in the file it links to; `shared/research-log.md` has the dated history.

## Waiting on Hassan

Everything Hassan needs to do by hand (browser checks, vendor contacts, decisions) is collected in
[`shared/manual-sweep.md`](shared/manual-sweep.md), worked in one sweep every week or two.

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
| 2 | Polar, Ametris, Axivity, Activinsights, Movesense, mindLAMP, AWARE, Avicenna, MetricWire, m-Path, CARP, LifeData, Evidation | Done 2026-10-21: all 13 records, profiles, both matrices, atlas and open questions corrected |
| 3 | Fitabase, Labfront, Fitrockr, Terra, Thryve, Ultrahuman, Sensor Bio, RingConn, Circular, Zepp, Verily, Purple Robot | 8 of 12 records committed by 2026-10-21 (all but Circular, Zepp, Verily, Purple Robot, not started). All 12 records committed by 2026-10-22 (Circular, Zepp, Verily and Purple Robot with one researcher plus a judge each). Profile and matrix pass done 2026-10-22: data-intermediaries, emerging-platforms and the Purple Robot section corrected, both matrices, READMEs, sources and open questions updated (79 open, Q47 reopened). Atlas resynced and republished (shared profiles: data-intermediaries, emerging-platforms). Fitrockr facts mostly Reported: its site blocks scripts; confirm in a browser |

After each batch: generate the tables, opt the completed profiles in to the generated facts block,
and replace the hand-written research-program tables in both comparison matrices with the
generated ones.

## Next

0. ~~**Google Health API onboarding.**~~ Done 2026-10-21 (profiles, matrix, atlas, open questions updated; the 2026-10-19 report worked). The weekly check of 2026-10-19 found Google no longer says it is closed to new projects; facts/fitbit-google.yaml is updated, but about 28 lines across the Fitbit profile, Module 1 matrix, README, atlas, explorer and open questions still say it is closed. One correction pass. Also work the rest of the 2026-10-19 report (15 missing quotes, 3 dead links).

1. **Vendor confirmation sheets (sub-project 3).** One page per company listing what is on record,
   for the vendor to confirm or correct. Hassan reviews and sends each one ("confirmed, send it").
   Answers become `vendor_confirmation` sources.
   **Pilot drafted 2026-10-22** for Verily, Zepp, Circular and Sensor Bio: saved as Gmail drafts and in
   `_private/vendor-sheets/` (not in git). Zepp and Sensor Bio have email addresses; Verily and Circular
   take contact forms, which Hassan submits. Generator: `tools/facts/confirm_sheet.py`.
2. **Re-check schedule.** Weekly: the fact monitor (running, GitHub Actions, Mondays). Monthly:
   re-verify pricing, access and terms facts as their `recheck_by` dates fall due. Quarterly: an
   independent review like `shared/reviews/2026-10-10-independent-review.md`.
   Since 2026-10-22 the Monday monitor extends `recheck_by` itself for stated facts whose quotes all
   still match (`facts/README.md`, "Automatic re-check extension"). The monthly pass covers only what
   it cannot confirm: about 180 of the 763 facts due by 2026-11-10, plus any whose quotes moved.
3. **Module 3 queue.** ~~Screen the queued candidates~~ done 2026-10-22: 16 screened, 7 profiled (72 profiles), 9 rejected; five free papers blocked by publisher bot checks wait for a PDF fetched by hand (list in `module-03-applied-studies/_scan-queue.md`). Zawada 2025 (the first Beiwe deployment mostly
   after the heartbeat change) profiled 2026-10-22 (73 profiles); heartbeat status not stated, Q115 still open. Vidal 2022, Nock 2026, Weingarden 2025 and the
   two ALS addenda were already written in an earlier repair pass; this line was stale.
4. **Fitbit profile follow-up** after 2026-10-30, when the legacy Web API is turned off.
5. **Module 4 scan proposal:** approve or drop `shared/weekly-literature-scan-module4-proposal.md`.
6. **Module 5, measurement science by domain (proposed 2026-10-22; Sleep started 2026-10-22).** Structure built (`module-05-measurement-science/`, `shared/domain-tags.json`, `tools/domains/build_hubs.py`), M4-042 moved to Sleep. Sleep seeded 2026-10-22: 58 papers in 7 sections, 49 papers and profiles in Modules 1 to 4 tagged, hub generated; 28 free PDFs wait for a hand download; 5 free-to-read documents not stored for licence reasons (manual sweep #10). Next domain (Cardiac) only when asked. One module, like Module 4, with
   a section per domain: Sleep first, then Cardiac, Physical activity and fitness, and maybe Mental
   health. It holds papers on the science of measuring that domain with wearables that are not tied
   to one device: consensus statements, standard metrics, validation methods, known physiological
   limits. Every existing paper in Modules 1 to 4 also gets a domain tag, and a script builds one hub
   page per domain across all modules (the explorer's `tags.json` already does something similar).
   The World Sleep Society recommendations (Module 4, M4-042) move to Sleep. Separate numbered
   modules per domain were considered and rejected, because most domain papers are also device or
   deployment papers and would need two homes. Cost: structure, small; tagging about 260 papers,
   one or two agents; seeding each domain, about two agents. Starts after vendor fact records
   batch 3.

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
