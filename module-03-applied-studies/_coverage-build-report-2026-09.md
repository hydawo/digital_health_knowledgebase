# Module 3 coverage build report, 2026-09-03 (IN PROGRESS, stopped at session limit)

Status: the on-disk cross-screen (Part A) is complete. Part B (fresh search) did not run to completion.
Part C is half built. Nothing from this pass has been committed or pushed. The eight new profiles and the
edits to the ledger and this file are uncommitted in the working tree.

## What this pass set out to do

Screen all 51 stored Module 1 and Module 2 PDFs that carry three or more deployment-reality signals against
Module 3's scope, from full text, then build profiles for the survivors and run a fresh device-side search.

## Part A, cross-screen of the 51: complete

12 of the 51 were already profiled in Module 3. The other 39 were read in full text by five parallel screening
passes (reports in the session scratchpad, screen/batchA.md to batchE.md; the extractions there are not in
the repo). Verdicts:

Screened in, profile written (8 profiles from 10 papers):
- oura-tempredict-healthcare-worker-adherence (Shiba 2023, with Mason 2022 folded in as the parent study)
- apple-heart-movement-study-retention (Truslow 2024)
- apple-womens-health-study-retention (Mahalingaiah 2022)
- aware-oura-delphi-covid-lockdown (Moshe 2021, AWARE on iOS plus Oura, Finland)
- beiwe-transdiagnostic-outpatient-completeness (Pellegrini 2022)
- beiwe-schizophrenia-state-clinic-pilot (Torous 2018, Barnett 2018, Staples 2017, one cohort)
- beiwe-cancer-surgery-survey-retention (Panda 2021)

Screened in, profile NOT yet written (the writing agents were killed by the session limit):
- Vidal Bustamante 2022 + 2024, GENEActiv + Beiwe surveys, 49 students, one academic year
  (slug geneactiv-beiwe-college-year-deep-phenotyping; extraction in screen/batchE.md item 1 and 5)
- Nock 2026, LifeData EMA, N=619, DOI 10.1037/abn0001117, PMC13308188
  (slug lifedata-post-hospital-suicide-ema; batchE item 7; resolves unresolved-questions Q113)
- Weingarden 2025 + 2026, MetricWire EMA + Beiwe passive, N=87, NCT04254575
  (slug metricwire-beiwe-bdd-remote-ema-passive; batchE items 6 and 8)

Addenda to existing profiles, NOT yet written:
- beiwe-als-adherence.md: Berry 2019 (18 iOS / 3 Android; daily surveys dropped after 10 participants for
  burden; speech analysable for 11 of 22) and Beukenhorst 2021 (pandemic continuity, N=8).
- beiwe-actigraph-modus-als-progression.md: Straczkiewicz 2024 (21-hour valid-day rule gives median 124 valid
  days against Johnson's 158 on the same people; 15 iOS / 5 Android) and Karas 2024 (passive-stream companion:
  63 to 45 funnel, 558.7 valid accelerometer minutes a day, 68.6 GPS minutes a day, excluded participants older
  and more impaired).

Rejected: 25 papers, all recorded in literature-index.json's rejected array with a reason code.
Breakdown: validation 5, review 5, architecture 7, no-cohort 4, duplicate-cohort 4 (each with an addendum
note), unobtainable 1 (Hirten 2025, whose usage statistics sit in a PMC supplement behind a bot check).

Attribution corrections found in full text:
- 2024-doherty-sensors-hrv-rhr-validity-series9-ultra2.pdf: first author is O'Grady, not Doherty.
- Torous 2015 (onnela-lab folder) used a custom app called Mindful Moods, not Beiwe.
- Lee 2024 (onnela-lab folder) used a custom VHS app, not Beiwe.
- Nock 2026 used LifeData, not Beiwe.
- Qian 2024 confirmed as Ethica/Avicenna, Android only (iPhone users removed because Bluetooth beaconing
  failed on iOS).

## Part B, fresh search: did not complete

Both search agents (device-side, and across-the-board plus grey literature) were terminated before writing
output. Nothing from Part B exists. Re-run from the brief in the original task.

## Part C, integration: not started beyond the profiles

Still to do, in order:
1. Write the three missing profiles and the two addenda (extractions above; rules in the session's
   PROFILE-WRITING-RULES.md, which is not in the repo: no em dashes, few colons, one assertion per sentence,
   sparse bold, every number from full text).
2. feasibility-matrix.md: add Part E for this wave, one row per study, and update the cross-cutting patterns
   (see below).
3. README.md: profile count 55 to 63 (66 with the three pending), platform and device tallies, strike
   through the device-breadth gap partially, keep Polar as still absent.
4. sources.md: add the new entries with retrieval status (all read from PDFs already stored in Module 1 or
   Module 2 folders; nothing copied into module-03 literature/).
5. shared/research-log.md entry; shared/unresolved-questions.md (Hirten supplement; Panda Android zero;
   Q113 resolved by the Nock profile).
6. _scan-queue.md: add Panda 2020 JAMA Surg and Panda 2021 Ann Surg Oncol (passive streams of the surgical
   cohort), Kubala US Navy Oura N=853, the Hispanic pregnancy Oura cohort, and Hirten pending supplement.
7. Show all reader-facing prose to Hassan for "confirmed, post it" before pushing. Ledger and this report can
   be pushed freely.

## Findings this wave bears on (draft, to be written into the matrix)

- Finding 2 (passive outlasts active): confirmed in Shiba (87.8% ring nights vs 63.8% survey days),
  Truslow (28% permanently inactive vs survey response falling 69.6% to 32.5%), Mahalingaiah (72.4% HealthKit
  tracking vs 34.5% month-six survey). The Beiwe schizophrenia pilot supplies an early instance of survey
  cessation with passive data intact before relapse.
- Finding 4 (OS effects are stream-specific): Panda 2021 adds a contradicting data point, zero of 13 Android
  users completing the month-one survey on Beiwe in 2017 to 2019, the opposite direction to McInerney 2024.
  Torous 2018 already found GPS and accelerometer running opposite ways by OS on the same phones.
- Finding 1 (retention vs completeness): Pellegrini gives the cleanest small case, 84% completion with 39%
  of participants at half the expected GPS.
- Finding 5 (support intensity): the schizophrenia pilot is the unsupported floor (about 50% coverage, one of
  17 lost entirely to Wi-Fi-only upload).
- New: withdrawal, daily non-participation and permanent inactivity are three different retention numbers
  (Truslow: 3.2%, 38%, 28% at one year).
- New: an in-app "bring your own ring" inclusion rule costs nothing in hardware and buys a 93% White, 80%
  degree-holding, iOS-only cohort (Moshe).

## Counts

Before this pass: 55 profiles. After the eight written: 63. Oura 2 to 4 (Shiba, Moshe; Mason folded in).
Apple Watch 3 to 5. AWARE 8 to 9. Beiwe 12 to 15 (three primary), with two more Beiwe-as-survey-vehicle
profiles pending. Polar still 0. GENEActiv, LifeData and MetricWire+Beiwe pending.
