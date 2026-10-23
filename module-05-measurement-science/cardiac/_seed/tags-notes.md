# Cardiac tagging notes

61 entries in `tags.json`.

## Counts

| Module | Primary | Secondary | Total |
|---|---|---|---|
| 1 (40 papers, 11 profiles) | 37 | 14 | 51 |
| 2 (1 profile) | 0 | 1 | 1 |
| 3 (profiles) | 2 | 4 | 6 |
| 4 (papers) | 3 | 0 | 3 |
| Total | 42 | 19 | 61 |

Module 1 breakdown: 31 primary and 9 secondary papers; 6 primary profiles (Apple Watch, Movesense, Polar, Withings, Samsung, Fitbit/Google) and 5 secondary profiles (Garmin, WHOOP, Oura, Empatica, emerging-platforms).

Module 2 literature library: no cardiac papers. Module 2 profiles other than CARP (AWARE, MetricWire, mindLAMP, RADAR-base, Beiwe) list heart rate or HealthKit streams only in passing and were not tagged.

## Overlaps the hub should handle

- Presby 2025 (10.2196/64955) and Truslow 2024 (10.1038/s41746-024-01187-5) have Module 1 paper rows too; only the Module 3 profile entry is kept, per the dedup rule.
- DOIs present in both Module 1 files (e.g. Liang, Cao, Dial, Miller 2022, Gong) are filed under `literature-library.md`.
- Tagged Module 1 papers filed only in `research-library-wearables.md`: Cohen (Hypertension), Cohen (JAMA), Al-Falahi (Heart Watch protocol), Yusuf (HiGHmed), Das (Cureus case), Jansen (Resuscitation Plus case), the Springer HRV living review, Liao (wildfire). PMID-only entries were mapped to DOIs through `research-library-index.json`.

## Keys that are not DOIs

- Apple hypertension notification white paper (no DOI): key is the repo PDF path `module-01-wearables/literature/apple-watch/2025-apple-whitepaper-hypertension-notifications.pdf`.
- Inocian 2024 (Philippine Journal of Cardiology, no DOI in the repo): `pjc:2024.0712.055060`, taken from the publisher URL.
- Gonzalez 2026 uses the bioRxiv preprint DOI listed first in the library; the published DOI is 10.1038/s41746-026-02799-9.

## Borderline calls

- Fudolig 2024 (LEMURS): overnight heart rate time series is the signal, but the question is sleep and mental health; primary, could be secondary.
- Hirten 2025 (IBD flares): HRV is a key predictive feature among several; secondary.
- Gonzalez 2026 and Presby 2025: HR and HRV are two of several physiology metrics; secondary.
- Miller 2022 (six wearables) and Milstein 2020 (Empatica EDA and HRV): HR and HRV are one of two or three validated outcomes; primary.
- Heydari 2025: commentary rather than primary data, but HRV is the subject; primary.
- Springer living review on wearable HRV across the menstrual cycle: surfaced but not read in the repo; primary on title alone.
- Jansen 2026 (cardiac arrest case): the detection came from fall detection, not a cardiac sensor; secondary.
- Liao 2026 (wildfire): sleep HR and HRV are among several outcomes; secondary.
- Truslow, Movesense Support trial, Withings Connecare, WHOOP Presby profiles: cardiac streams are present but not the deployment question; secondary.
- Apple Heart Study data-management profile: primary because the study's objective is AF, though the profile is about operations.
- Garmin, WHOOP, Oura, Empatica: cardiac data is core but research access is limited or aggregate-only; secondary.

## Considered and not tagged

- Apple VO2max white paper and Lambe VO2max validation (cardiorespiratory fitness, not cardiac measurement).
- Holmes 2026 (cardiorespiratory fitness and sleep), Ong 2026 (cardiometabolic implications), L038 (irregular cycles and cardiometabolic conditions): cardiovascular terms without a cardiac device outcome.
- Zawada 2025 Beiwe stroke/TIA profile: stroke population, outcome is mood and Beiwe data quality.
- Mason TemPredict papers, Empatica epilepsy profile, connect-multi-wearable (heart rate only as a wear proxy).
- Walzel and Jiang pulse oximetry papers (SpO2, not cardiac).

## Could not classify

- Stove and Hansen 2023 (WHOOP vs Apple Watch HR during resistance exercise): cited in `research-library-wearables.md` with no DOI, PMID or full citation; would be primary if located.
- "Readiness, recovery, and strain" (10.1515/teb-2025-0001): surfaced, not fetched; not tagged.
