# Sleep: what the evidence says

This page is for a study team choosing how to measure sleep with wearables or phones. It was written on 2026-10-23 from the 58-row [catalogue](literature-library.md). Many rows rest on abstracts only, so this page adds nothing beyond them. Where a point rests on guidance rather than data, the bullet says so.

## What the field agrees on

- Consumer sleep trackers should not be used to diagnose sleep disorders. This is the position of the AASM [S-001] and the Australasian Sleep Association [S-023]. Both are guidance, not data.
- Wrist devices detect sleep better than wake. Seven consumer trackers reached epoch sensitivity of 0.93 or more [S-050]. Their specificity was only 0.18 to 0.54 [S-050]. The Sadeh algorithm also agreed more for sleep than for wake [S-033]. The ASA guideline says actigraphs tend to overestimate sleep [S-023]. It adds that they are more accurate in good sleepers [S-023].
- Sleep and wake is a different task from staging. Accelerometer-only devices work for sleep and wake but not for multi-stage staging [S-054]. Devices that add PPG do better [S-054]. EEG is the only modality that identifies every stage [S-048].
- Heart-based staging comes closer but does not match PSG. In the three catalogued models using heart rate or PPG, four-class kappa was 0.65 to 0.75 [S-051, S-052, S-053].
- Device studies should report more than averages. A published framework with open R code covers Bland-Altman and epoch-by-epoch agreement [S-011]. Averaging across participants overstates agreement because most of the night is sleep [S-012].
- Shared definitions exist. The CTA/NSF 2052 series defines consumer sleep measures and how to measure them [S-013, S-014]. The row describes it as an industry standard.
- Several groups call for more standardisation. These include a World Sleep Society task force [M4-042] and a position piece in *Sleep* [S-007].

## Where devices fall short

- Total sleep time is biased, and the direction varies. Actigraphy overestimated it by about 22 minutes in adults with chronic conditions [S-046]. Consumer wrist trackers underestimated it by about 17 minutes in pooled data [S-049]. GGIR on ActiGraph data overestimated it by 26 to 31 minutes [S-038]. Agreement was poor, with ICC of 0.27 to 0.44 [S-038].
- Errors grow in poor sleepers. They were larger in chronic conditions than in healthy adults [S-046]. In insomnia, TST error was 29 minutes against 17 in controls [S-057]. Error rose with longer overnight wake [S-038]. Performance dropped on disrupted nights [S-050].
- WASO and sleep efficiency agree poorly, even when sleep period and duration hold up [S-037].
- Sleep onset latency looks fine on average but varies widely between people [S-047]. In insomnia, home actigraphy gave shorter latency than PSG [S-056].
- Algorithm choice changes results. Two open-source SRI calculators gave markedly different scores [S-027]. That choice alone changed associations with mortality, diabetes and atrial fibrillation [S-027]. Two classic algorithms beat one device's native scoring [S-039]. In one head-to-head, complex machine learning models generalised poorly [S-042].
- Staging from wrist motion alone is weak. One model showed fair to moderate agreement with wide limits for REM and NREM [S-041]. An open watch model reached about 72 percent for wake, NREM and REM [S-045].
- Skin tone may affect wrist PPG. The catalogue holds only a commentary on this, and its full text was not read [S-055].

## What a study team should do

1. Decide first whether you need sleep and wake, timing, regularity or stages. Do not plan staging on an accelerometer-only device [S-054].
2. Do not use consumer device output for diagnosis [S-001, S-023].
3. Prefer devices with raw data and disclosed algorithms. The AASM names raw data and algorithm access as needs [S-001, S-003]. The ASA guideline asks new devices for full disclosure of recorded data [S-023]. Open options include GGIR [S-036] and the Walch classifiers [S-045].
4. Check validation in a population like yours. Insomnia and chronic illness both raise error [S-046, S-057]. Validation samples should be diverse [S-054, S-055].
5. Plan enough nights. The ASA guideline recommends 72 hours to 14 days for actigraphy [S-023]. Standard deviation and interdaily stability need more than a week of data [S-025].
6. Separate nonwear from still sleep. Published algorithms do this for wrist and chest data [S-043, S-044].
7. If you can, run PSG on a subsample. Analyse it with the standard framework and report epoch-by-epoch results [S-011, S-012].
8. Use the CTA/NSF definitions for sleep measures [S-013, S-014].
9. Lock the algorithm or package before analysis and report it. For regularity indices, follow the RIRI checklist [S-027].
10. Report actigraphy methods in full. Guides exist for adults [S-019] and for infants and children [S-021]. The ASA list includes weekday and weekend coverage and diary discrepancies [S-023].

## Open gaps

- Several key guidance papers were catalogued from the abstract only. These include the World Sleep Society recommendations [M4-042], the SRS-published review [S-005] and the AASM update [S-003].
- The newest CTA/NSF performance standard (2052.3-A) is sold by CTA and was not read [S-015].
- Skin tone bias has no data row, only a commentary [S-055].
- Pediatric work has reviews of reporting practice [S-020, S-021]. No row pools consumer device accuracy in children.
- No Module 5 row covers phone-based sleep sensing. The one smartphone sleep review lives in Module 4 ([hub](hub.md)).
- Eight rows are paywalled. Another 28 need a hand download ([catalogue](literature-library.md)).

## Read these first

| Row | Why |
|---|---|
| [S-005] | Practical advice on choosing and using wearables in sleep and circadian research. |
| [S-011] | The standard analysis framework for any device against PSG, with open code. |
| [S-050] | Seven consumer trackers against PSG in one cohort, including disrupted nights. |
| [S-054] | Which sensors can stage sleep, and five validation recommendations. |
| [S-027] | Shows that the choice of SRI calculator alone can change study findings. |

## Related in this library

- [Sleep hub](hub.md) lists every paper and profile in Modules 1 to 4 tagged sleep.
- Module 1 profiles: [Oura](../../module-01-wearables/profiles/oura.md) (sleep staging is its core feature), [Fitbit / Google](../../module-01-wearables/profiles/fitbit-google.md) (documented sleep staging), [Ametris / ActiGraph](../../module-01-wearables/profiles/ametris-actigraph.md) (Sadeh and Cole-Kripke scoring).
- Module 3 studies: [Soon 2025, Oura freshmen sleep](../../module-03-applied-studies/profiles/oura-university-freshmen-sleep.md), [Haimovich 2026, Oura sleep in ED older adults](../../module-03-applied-studies/profiles/oura-ed-admitted-older-adults-sleep.md) and [Culhane 2026, GENEActiv inpatient sleep reporting](../../module-03-applied-studies/profiles/geneactiv-inpatient-psychiatry-sleep-reporting.md).
