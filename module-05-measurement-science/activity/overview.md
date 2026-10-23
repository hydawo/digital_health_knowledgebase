# Physical activity and fitness: what the evidence says

This page is for study teams measuring physical activity, steps, energy expenditure, sedentary time or cardiorespiratory fitness with wearables or phones. It was written on 2026-10-23 from the 66-row [catalogue](literature-library.md). Every claim cites a catalogue row. "PDF" means the claim was checked in the stored paper.

## What the field agrees on

- No single instrument suits every study. That is the American Heart Association's position [P-001].
- Studies need to disclose monitor specifications and processing protocols to be comparable. This is an expert Delphi judgment, not a measured result [P-007].
- Methods reporting has been poor and inconsistent [P-026; P-028, PDF].
- Processing choices change the result. In 7,650 older women, the wear-time algorithm alone shifted sedentary time by roughly 30 to 60 min [P-042]. Valid-day rules of 12 h or less underestimated steps and intensity time [P-043].
- Wear site matters. Hip and wrist raw output differed significantly [P-032]. Wrist and waist step counts are not interchangeable [P-063]. The dominant wrist read higher than the non-dominant wrist [P-039].
- Cut-points belong to one monitor, one site and one population [P-033, P-039, P-065].
- Raw-data metrics allow comparison without cut-points [P-036, P-037]. No single raw metric was best in all conditions [P-031]. Mapping between metrics works, but not exactly [P-038].
- Daily steps need 3 to 7 days for a reliable estimate [P-041].

## Where devices fall short

- Energy expenditure is the weakest output. A 65-study review found no wrist-worn device that measured it accurately [P-061]. Error varied by activity type. Adding heart rate or heat sensing reduced it [P-058].
- Research monitors also underestimated total energy expenditure, most often at slow walking speeds [P-062].
- The standard 1 MET baseline of 3.5 ml/kg/min underestimated activity METs [P-045].
- Wrist steps are less accurate than waist steps. On a treadmill, wrist ActiGraph error was about 41% against near zero for waist devices [P-064].
- Slow walking and impaired gait reduce step agreement in older adults [P-060].
- Wrist step algorithms vary widely. In free living, reference models had mean absolute percent error of 65% to 231%. A self-supervised model reached 12.5% [P-052].
- Sedentary cut-points from hip counts may sit far from the standard. In adults with a mean age of 78, the optimal hip cut-point was under 22 counts/min, not under 100 [P-065].
- Consumer VO2max estimates from resting data overestimated fitness. Bias was 2.17 ml/kg/min, with limits of agreement from -13.07 to 17.41. Exercise-based algorithms had less bias [P-059].
- Resting heart rate tracks fitness only at population level. The Fenland authors do not validate it for individuals [P-066].
- Free-living validation quality is low. Of 237 studies, 72.9% were rated high risk of bias. Of 163 wearables, 58.9% were validated only once [P-021, PDF].

## What a study team should do

1. Name the outcome first. Then use a structured method choice, such as the AHA decision matrix [P-001].
2. Choose the wear site on purpose. Wrist wear gave 14% more participants meeting minimum wear criteria than waist wear [P-028, PDF]. Wrist step counts are less accurate, though [P-063, P-064].
3. For sedentary time and posture, use a device with an inclinometer or posture function. This is the CROSBI consensus recommendation [P-030].
4. Hand devices out in person where you can. In-person distribution gave 30% more consent and 15% more adherence to wear criteria than postal distribution [P-028, PDF].
5. Collect raw acceleration. Report open metrics such as ENMO, MAD or MIMS [P-031, P-034, P-035]. Add average acceleration and intensity gradient for cross-study comparison [P-036].
6. Fix wear-time and non-wear rules before analysis. Check that mailing days are not counted as wear days [P-042]. With default settings, the raw-data van Hees non-wear algorithm performed best. Tuned epoch-based algorithms matched it [P-049].
7. Take cut-points only from the same monitor, site and a similar population [P-033, P-039, P-065].
8. Do not treat consumer energy expenditure as an outcome without your own validation [P-061]. If you validate it, the INTERLIVE network's checklist is one option [P-013].
9. For VO2max, prefer exercise-based estimates over resting-data ones [P-059]. Research models from free-living heart rate and movement exist [P-055, P-056].
10. For heart-rate-based activity, see the INTERLIVE network's protocols. A wearable manufacturer partly funded that work [P-019].
11. Plan at least 3 to 7 days of wear for steps [P-041].
12. Report methods with a published template [P-026]. Pick the analysis with the GRANADA decision tree [P-027].

## Open gaps

- Validation guidelines disagree on statistics. INTERLIVE, CTA, Welk and Keadle each favour different tests [P-020].
- No item in the ProPASS thigh-wear survey reached the agreement threshold [P-008].
- Before INTERLIVE, no universal recommendations existed for free-living heart rate [P-019].
- The CTA step and intensity standards were not read. Both are sold [P-023, P-024].
- Evidence in chronic disease and older adults is thin. Only 16 of 134 monitor validation studies were in chronic disease [P-062]. One older-adult review found 7 studies [P-060].
- Posture and activity type are under-validated in free living. They made up 15.6% of validation studies [P-021, PDF].
- Most of the evidence comes from high-income countries: 92.5% in one meta-analysis of 123 collection waves from 95 studies [P-028, PDF].
- This catalogue holds no pooled review of phone-based step counting. Phone step algorithm validation sits in Module 2 and is listed in the [hub](hub.md).

## Read these first

| Row | Why |
|---|---|
| [P-001] | AHA decision matrix for choosing a measurement method by outcome and resources. |
| [P-028] | Meta-analysis showing how wear site and distribution change consent, wear and data loss. |
| [P-036] | Average acceleration and intensity gradient, the cut-point-free pair for raw data. |
| [P-058] | Meta-analysis of energy expenditure error across 60 studies. |
| [P-059] | Meta-analysis of consumer VO2max estimates, with INTERLIVE validation advice. |

## Related in this library

- [Hub](hub.md). Every tagged paper and profile in Modules 1 to 4.
- [Axivity and GENEActiv](../../module-01-wearables/profiles/axivity-geneactiv.md) and [Ametris (ActiGraph)](../../module-01-wearables/profiles/ametris-actigraph.md). Research raw accelerometers.
- [Apple Watch](../../module-01-wearables/profiles/apple-watch-healthkit.md). Consumer steps and VO2 max.
- [All of Us Fitbit cohort](../../module-03-applied-studies/profiles/allofus-fitbit-step-counts.md). Years of daily steps as the exposure.
- [CONNECT](../../module-03-applied-studies/profiles/connect-multi-wearable-psychosis.md). Valid step-count days compared across three wearables.
- [Beiwe, ActiGraph and StepWatch in ALS](../../module-03-applied-studies/profiles/beiwe-actigraph-modus-als-progression.md). Two form factors compared for wear compliance.
