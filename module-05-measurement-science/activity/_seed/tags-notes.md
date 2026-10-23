# Activity domain tags: notes

Generated for the Physical activity and fitness hub. 66 entries in `tags.json`.

## Counts

| Module | Primary | Secondary | Total |
|---|---|---|---|
| 1 (papers 10 + 6 + profiles) | 10 | 16 | 26 |
| 2 (papers and Beiwe profile) | 8 | 10 | 18 |
| 3 (profiles) | 9 | 8 | 17 |
| 4 (papers) | 5 | 0 | 5 |
| Total | 32 | 34 | 66 |

Module 1 includes 7 technology profiles (2 primary: ActiGraph, Axivity/GENEActiv; 5 secondary: Fitbit, Apple Watch, Garmin, Samsung, Empatica). Module 2 includes 1 technology profile (Beiwe, secondary).

## Borderline calls

- Upper-limb ALS accelerometry (Straczkiewicz 2024 profile, EBioMedicine L044): tagged primary because free-living wrist accelerometry movement is the subject; L007 (prescribed exercises) secondary.
- Rest-activity rhythm papers (L003 Shim; Stahl 2026 profile; Sleepsight profile): secondary, since the focus is circadian rhythm rather than activity volume.
- Apple Heart & Movement Study profile: primary on the study's subject (activity and mobility), though the profile itself is about retention.
- Beiwe HOPE profile (Fitbit steps plus Beiwe): primary, since Fitbit step data is half the instrumentation; could be argued secondary.
- Garmin nursing-home profile: primary (wrist ENMO physical activity levels), alongside sleep.
- GPS-only mobility (L078, L088, L099, L051, L040, L026, Cote 2019 profile): secondary per the rule. L026, L051 and L019 have no abstract in the repo, so the call rests on title only.
- L082 and L097 (ALS smartphone studies): secondary, abstracts truncated in the repo.
- Holmes 2026 (10.1093/sleep/zsaf318): PDF not obtained; primary judged from the title (cardiorespiratory fitness is the outcome).
- Khodr WHOOP systematic review, Choe and Lambe Apple Watch reviews: secondary, because steps and energy expenditure are some of many metrics pooled.
- Azadifar 2026, Choi 2026, Liao 2026, Yusuf 2026, Alshamrani 2026: secondary; activity is one reported measure among several.
- L071 (HAR systematic review) appears in both the Module 2 and Module 4 catalogues; kept once, filed under Module 4.
- L049 and L055 are the journal and preprint versions of one step-counting paper; both kept because they have different DOIs.
- Technology profiles skipped though they list activity data: Oura (VO2 max route, but profile says steps are weak), WHOOP (strain and one step total per cycle), Polar and Movesense (raw accelerometer, but profile advises against activity endpoints), Withings, data-intermediaries, emerging-platforms. mindLAMP, RADAR-base, AWARE, CARP, m-Path, Avicenna and MetricWire list step or accelerometer streams only as ordinary sensors, not as a major output.
- Module 3 profiles skipped: accelerometer or GPS only as a completeness figure (stroke/TIA, dp-schizophrenia, Kiang missing data, NHS3 burst, transdiagnostic, pain clinic, mindLAMP LINC, sensorkit TechSANS, AWARE-MoMo, AWARE-Light, spinal cord injury).

## Dedup

- Module 3 profile DOIs that match Module 1 or 2 rows (Truslow 2024, Straczkiewicz 2024 L029, Johnson 2023 L056, Yi 2024 L032, Vidal Bustamante L068, Cote 2019 L098, Stahl 2026, HOPE L104): only the profile entry is kept.
- No paper DOI appears in both Module 1 files with two entries.
- The 2026 Oura and Apple papers cited only in `research-library-wearables.md` had their DOIs taken from `research-library-index.json` or the file text.

## Rows I could not classify

- L019 (advanced cancer functional status), L026 (acromegaly), L051 (SMI mobility): no abstract in the repo, title-level only.
- Holmes 2026 PDF not obtained.

## Keys that are not DOIs

- `module-01-wearables/literature/apple-watch/2021-apple-whitepaper-vo2max-cardio-fitness.pdf`: Apple VO2 max white paper, no DOI, key is the repo PDF path.
- All 17 `m3-profile`, 7 `m1-profile` and 1 `m2-profile` entries are keyed by repo-relative profile path. M3 profiles carry the DOI in a `doi` field.
- No `pmid:` keys were needed.
