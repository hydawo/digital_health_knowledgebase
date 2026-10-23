# Sleep tagging notes

52 entries in `tags.json`.

## Counts

| Module | Primary | Secondary | Total |
|---|---|---|---|
| 1 (30 papers, 6 profiles) | 23 | 13 | 36 |
| 2 (papers) | 2 | 0 | 2 |
| 3 (profiles) | 6 | 7 | 13 |
| 4 (papers) | 1 | 0 | 1 |

Module 1 breakdown: 16 papers + 1 dissertation from the first literature-library table, 4 L-rows, 9 from research-library-wearables.md only, and 6 technology profiles (3 primary: Oura, WHOOP, Withings; 3 secondary: Fitbit/Google, Axivity/GENEActiv, Ametris/ActiGraph). Module 2 technology profiles: none qualified.

## Overlaps the hub should handle

- Four items appear as both a paper entry and a Module 3 profile entry (kept separate by `kind`; the profile carries a `doi` field): Soon 2025 (10.1093/sleep/zsaf156), Haimovich 2026 (10.2196/92359), Stahl 2026 (10.2196/88773), Presby 2025 (10.2196/64955). The Torous/Staples Beiwe pilot profile also covers the Staples 2017 paper tagged as L108.
- L092 (10.1007/s11920-019-1043-y) has rows in both Module 2 and Module 4 libraries; one entry, filed under Module 4 where it was moved.
- Module 1 DOIs also in research-library-wearables.md (e.g. Khan 2025, Miller 2022) are filed under literature-library.md.

## Keys that are not DOIs

- Jaworski and Park 2023 (Apple Watch vs PSG): `pmid:38083143`, no DOI in the repo.
- Harms 2018 WHOOP dissertation: `eric:ed595664`, no DOI.

## Borderline calls

- Fudolig 2024 (10.1159/000539487): sleep heart rate dynamics vs mental health; secondary, could be primary.
- Presby 2025 (paper and profile): sleep duration and consistency are two of several vendor physiology metrics; secondary.
- Khodr 2024 WHOOP systematic review: covers sleep validity among many metrics; secondary, based on title/context only.
- Grosicki 2026 alcohol: sleep is one of three named outcomes; secondary.
- Gonzalez 2026 menstrual cycle: "sleep" in title, one of several outcomes; secondary.
- Harms dissertation: sleep, recovery, performance; secondary.
- Azadifar 2026, Ong 2026: sleep stages/duration are among reported metrics; secondary.
- Choi 2026 DBS case report: Oura Sleep Score among reported scores; secondary.
- Zou 2026 green dose: sleep outcomes among daytime and emotional outcomes; secondary.
- Vidal Bustamante 2022 (GENEActiv profile): sleep pipeline is central to the data but the research question is affect and behaviour; secondary.
- CONNECT (Bladon) and Samsung palliative (Dominguez): sleep-data completeness reported per device but sleep is not a research question; secondary, weakest tags in the set.
- MoMo-Mood: sleep duration compared across groups with actigraph and bed sensor; secondary.
- Garmin nursing home (Boyle): "sleep quality" in title but sleep came from a radar sensor, not the watch; secondary.
- Technology profiles: Fitbit, GENEActiv/Axivity, ActiGraph tagged secondary because sleep staging or actigraphy sleep scoring is documented but the products are broader; Withings tagged primary for its Sleep / Sleep Rx mats. Samsung, Apple Watch, Garmin, Polar, Empatica (EmbraceMini sleep clearance only) not tagged: sleep is a listed metric.

## Considered and not tagged

- Oura TemPredict adherence (Shiba 2023): adherence is defined by nights with a sleep record, but sleep itself is not studied.
- Hatamiya 2026 athlete travel (10.1007/s40279-026-02455-y): likely covers jet lag and sleep, but the repo text does not say; left untagged, worth a check.
- Vidal Bustamante 2020 style behaviour paper L068 (Module 2 row): no sleep mention in the catalogue row.
- mindLAMP global cognitive (sleep mediation exploratory), AWARE STAND (sleep features), Moshe 2021 Delphi (sleep among predictors), Empatica epilepsy (diurnal data quality), Lundstrom 2024 swimmers, Altini 2024 nocturnal HRV.
- Module 1 and 2 literature-library abstract text is truncated, so Module 2 rows were screened on title plus first sentence of the abstract.

## Could not classify

None. Two rows lack DOIs (above); research-library-wearables.md papers with PMIDs only were mapped to DOIs via `module-01-wearables/research-library-index.json`.
