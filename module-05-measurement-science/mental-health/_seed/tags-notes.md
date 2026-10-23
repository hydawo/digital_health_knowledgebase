# Mental health domain tags: notes

Generated for the Mental health hub. 107 entries in `tags.json`, all keys unique.

## Counts

| Module | Primary | Secondary | Total |
|---|---|---|---|
| 1 (11 papers, 1 profile) | 7 | 5 | 12 |
| 2 (37 papers, 6 profiles) | 33 | 10 | 43 |
| 3 (36 profiles) | 34 | 2 | 36 |
| 4 (papers) | 12 | 4 | 16 |
| Total | 86 | 21 | 107 |

Module 1 profile: Empatica (secondary). Module 2 profiles: mindLAMP and LifeData primary; m-Path, Beiwe, RADAR-base and legacy-and-adjacent-platforms secondary.

## Borderline calls

- Avicenna smoking-youth EMA profile: primary, on substance use (smoking) as the subject; could be argued secondary.
- Alcohol: WHOOP alcohol trajectories (Grosicki) primary; the WHOOP alcohol-effects paper secondary because physiology is the focus and alcohol the exposure.
- Vaping (L034): secondary; vaping is the exposure and respiratory symptoms the outcome.
- Swimmers energy deficiency and psychological stress (10.1177/17479541231206424): secondary, stress is one of two outcomes.
- L003 (neuropsychiatric health, abstract truncated) and L080 DPSleep (sleep versus mental health, abstract truncated): secondary on title and partial abstract.
- mSavorUs pair: loneliness intervention profile primary (loneliness outcome); companion profile primary (depressive symptom detection). They are one cohort, so do not count them as two independent studies.
- Spinal cord injury incentives profile: primary because the parent study measures depression and psychosocial well-being, though the profile itself is about incentives.
- Beiwe NHS burst profile (Yi 2025): primary, the parent paper is about psychological well-being measurement.
- Beiwe type 2 diabetes profile: secondary, a mood-and-behaviour study nested in a diabetes cohort.
- GENEActiv inpatient psychiatry profile: secondary; the population is psychiatric but the measured construct is sleep and activity reporting.
- L054 (returning results in psychiatry): primary, but the repo notes the Europe PMC match is uncertain.
- L012 commentary on a psychopathology special issue: secondary.
- L062 digital pill in severe mental illness: secondary; medication adherence, not symptoms.
- L066 mentalizing imagery therapy for dementia caregivers: primary, caregiver stress is the target.
- L090, L095, M4-033, M4-038 (general digital phenotyping or brain disorder reviews with psychiatric framing): secondary.
- m-Path, Beiwe, RADAR-base, legacy-and-adjacent profiles: secondary; mental health is a major but not sole documented use. LifeData primary because its documented domains skew to psychology and psychiatry.
- Profiles in the 2026 scan ledger for Oura (stress after wildfire, green dose, WARN-D, depression/anxiety severity): kept under `research-library-wearables.md` as in the other domains.

## Skipped (considered, not tagged)

- Module 3: mindLAMP LINC (non-clinical data quality), Beiwe missing-data meta-study, Beiwe chronic-disease substudy, AWARE chemotherapy, Avicenna adolescent school-ban ESM, m-Path dementia ESM, m-Path Sense/CARP, VPN traffic, dementia-caregiver Apple Watch (rest-activity rhythm), TemPredict adherence, Apple Heart & Movement, Apple Heart Study and others with only passing mentions.
- Module 1 and 2 papers: Empatica E4 dyadic EDA validation (arousal during interaction, not a mental-health construct), L032 chronic disease drivers, L047 speech emotion recognition (technical), L101 and L089 methods papers.
- Module 1 profiles with only stress or sleep metrics listed (Oura, WHOOP, Garmin, data-intermediaries and others), and Module 2 profiles for AWARE, Avicenna, MetricWire, CARP, Evidation.
- MetricWire profile has no mental-health text although its Module 3 deployments are mostly suicidality EMA; left untagged because the profile does not document it.

## Dedup

- Module 3 profile DOIs that match Module 1 or 2 rows, kept as profile entries only: Moshe 2021 (10.3389/fpsyt.2021.625247), Presby 2025 (10.2196/64955), Matcham 2022, Nock 2026 (L008), Huang 2025 (L013), Yi 2025 (L023), Weingarden 2025 (L024), Vidal Bustamante 2022 (L068), Pellegrini 2022 (L079), Mercier 2020 (L083), Liu 2019 (L096), Torous 2018 (L103).
- Papers listed in both Module 2 and Module 4 (L073, L086, L090, L092, L095, L102, L110, L111) appear once, under Module 4.
- 10.2196/mental.5165 appears twice in the Module 2 file (platform table and L112); one entry, row_id L112.
- No DOI appears in both Module 1 files with two entries.

## Rows I could not classify

- L003, L080 (truncated abstracts), L019, L035, L054 (no abstract): calls rest on titles.

## Keys that are not DOIs

- `module-02-digital-phenotyping/literature-library.md#L100` and `#L106`: no DOI or indexed record in the repo, so keyed by file and row id.
- All 36 `m3-profile`, 1 `m1-profile` and 6 `m2-profile` entries are keyed by repo-relative profile path; M3 entries carry the DOI in `doi`.
- No `pmid:` keys were needed: every PMID in `research-library-wearables.md` that is mental-health relevant maps to a DOI via `research-library-index.json`.
