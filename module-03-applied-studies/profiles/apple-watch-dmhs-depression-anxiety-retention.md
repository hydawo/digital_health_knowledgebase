# Douglas et al. 2026 - Digital Mental Health Study, provisioned Apple Watch with participant iPhones for 12 months in a depression-stratified UCLA cohort, N=4,539

## Quick Facts

| Field | Details |
|---|---|
| Citation | Douglas CS, Congdon E, Huang C, Seok D, Cohen ZD, Akre S, Tozzo V, Huang F, Ramo-Larios D, Bernier RA, Flint J, Naeim A, Balliu B, Bui AAT, Bartlett MS, Craske MG, Freimer NB. "The Digital Mental Health Study assessed feasibility of large-scale digital sensing for depression and anxiety." *npj Digital Public Health* 2026;1:27. DOI [10.1038/s44482-026-00029-3](https://doi.org/10.1038/s44482-026-00029-3). PMID 42558176 / PMC13437235. Published 2026-08-04. |
| Study design | Prospective 12-month observational cohort with recruitment stratified by depression severity, sex at birth, age and ethnicity. Preceded by two pilots (DMHS-P1, 8 weeks; DMHS-P2, 12 weeks). This paper reports design, recruitment, retention and adherence. UCLA IRB #21-001558. |
| Sample size (enrolled / analyzed) | 17,150 screened. 5,684 eligible and consented. 4,542 completed intake. 3,333 completed the full 12 months. Three later asked for deletion, leaving 4,539 and 3,332. |
| Population | UCLA students and UCLA Health patients, coastal Southern California, USA. 57.0% female at birth. 44.7% aged 18 to 25 and 7.4% over 65. 47% had PHQ-8 of 10 or more at intake. |
| Duration | 52 weeks per participant. Enrolment January 2022 to January 2023. |
| Devices/platforms used | Study-provided [Apple Watch](../../module-01-wearables/profiles/apple-watch-healthkit.md) paired to the participant's own iPhone (70 used a loaner iPhone). Apple Research app for surveys, EMA and video journals, collecting HealthKit and SensorKit data. REDCap for interviewer-rated scales and some surveys. The pilots also used the Beddit sleep tracker. No third-party phenotyping platform. The citation-graph pass tagged this paper RADAR-base. That is wrong. |
| Funding/COI | Funded by Apple Inc. and UCLA. Four authors were Apple employees during the work and own Apple stock. A fifth was an Apple intern in 2023. Data access is governed in part by agreements with Apple. Compensation was tiered by data completion, up to US$1,070 a year, and participants could keep the watch. |
| Last verified | 2026-10-31 |

## Summary

This is the largest mental health deployment in the module and the first in it to stratify recruitment by symptom severity. It is included for an explicit 12-month funnel and for adherence figures that are high and specific about how they were achieved.

Retention was 73.4% (3,332 of 4,539) over a protocol the authors estimate at 37 hours of participant time. The 1,207 who dropped out stayed a median of 241 days. Data kept flowing until each formally left the roster.

Adherence among completers was high on every modality. Mean daily watch wear was 21.0 hours (SD 2.2). The average completer met the wear target on 87.4% of weeks. Biweekly PHQ-8 completion was 90.5%. Daily mood-survey compliance fell from 86.9% in week 1 to 67.2% in week 52.

The paper is unusually direct about the support model behind those numbers. Automated daily compliance reports flagged missing data for fast staff contact. Compensation was tied to completion in quarterly tiers. Participants could see their own task completion in the app.

## Instrumentation and Deployment Model

Hybrid. The watch was provisioned and the phone was the participant's own. Participation required an eligible iPhone or willingness to use a loaner. 70 participants used a loaner, about 2% of the sample. Participants paid for their own data plans.

A study kit with the watch, instructions and any loaner phone was mailed before intake. Staff then guided setup over a remote intake session. They confirmed the iOS version, paired the watch, enrolled the participant in the Apple Research app and reiterated charging rules. Participants authorised each data type on the device and could change those permissions at any time.

The wear instruction was at least 20 hours a day including sleep. Participants were told to charge for at least two hours daily while the watch was connected to the iPhone and Wi-Fi.

Wear was measured from HealthKit StandHour data. An hour counted as worn if the StandHour field held either 0 or 1. Data went to Apple, were processed, and were then shared with UCLA.

Passive collection drew on HealthKit and SensorKit. Streams included accelerometer, gyroscope and ambient light on both devices, call and message metadata, app-usage categories, keyboard dynamics, on-device speech and facial-expression features, PPG-derived vitals and opportunistic ECG. SensorKit reported location as visits to anonymised places, and raw GPS was never transmitted. More than 200 features were extracted.

The pilots shaped the main protocol. DMHS-P2 gave each participant two watches to wear alternately so one could charge. The authors judged that "too complex" and dropped it. Watch-based mood ratings in P2 were moved back to the iPhone because participants preferred one place to track tasks.

## Recruitment and Retention

Recruitment ran through the UCLA Health patient portal, automated phone calls to health-system patients, the student registrar, campus lists, social media and a participant registry. Screening was online and included the PHQ-8 for severity binning.

| Stage | n |
|---|---|
| Screened | 17,150 |
| Eligible and consented | 5,684 |
| Completed intake | 4,542 (4,539 after 3 deletions) |
| Completed the full 12 months | 3,333 (3,332 after deletions) |
| Dropped out | 1,207, median 241 days in |

Completion varied by subgroup in ways a study designer can plan for.

| Subgroup | Completed 12 months |
|---|---|
| Age 18 to 25 | 65.3% |
| Age 26 to 45 | 75.6% |
| Age 46 to 65 | 83.6% |
| Age over 65 | 90.2% |
| PHQ-8 under 10 at intake | 77.7% |
| PHQ-8 of 10 or more at intake | 68.5% |
| Severe (PHQ-8 20 or more) | 61.6% |
| White, Hispanic | 69.7% |
| Black | 70.8% |
| White, non-Hispanic | 75.8% |
| Bachelor's degree or more (non-students) | over 80% |

Sex at birth and employment status did not predict completion.

Dropout clustered around milestones. It rose near month 4, at the first mandatory check-in (weeks 10 to 13) and the end of the first compensation quarter. It rose again near the second check-in (weeks 46 to 49) and before the exit assessment. Participants who could not finish the first check-in were excluded from the rest of the study. The authors say they do not yet understand why participants dropped out.

## Data Completeness and Technical Issues

Completeness was monitored daily with stream-specific flags. Three consecutive missed Daily Reflection surveys, for example, triggered a flag. The full criteria are in Supplementary Table 7, which was not read.

| Measure, completers only | Figure |
|---|---|
| Biweekly PHQ-8 completion | 90.5%, above 80% to the final assessment |
| Daily Reflection compliance (at least 4 per week) | 86.9% in week 1, 67.2% in week 52 |
| Daily Reflection completion, weekdays versus weekends | 67.1% versus 64.2% |
| Daily Reflection, most severe intake group | 86.8% first 12 weeks, 72.8% overall |
| Daily Reflection, no-depression intake group | 88.0% first 12 weeks, 77.4% overall |
| Mean daily watch wear | 21.0 hours (SD 2.2) |
| Weeks meeting the wear target (20 hours on 4 or more days) | 87.4% for the average completer |
| Completers meeting the wear target on 90% of their weeks | 67.5% |

Quarterly EMA bursts gave a temporary lift in daily compliance with a smaller carry-over. Baseline depression affected daily-survey compliance and wear time but not PHQ-8 compliance.

Adherence is reported for completers only. Comparable figures for the 1,207 who dropped out are not given.

No technical failure modes are itemised. Sync failures, battery problems, lost or broken watches and iOS-version effects are not reported. The paper does not say how often a StandHour gap reflected a participant switching that stream off rather than removing the watch.

## Feasibility Findings

The authors conclude that a sample of more than 4,000, diverse by age, sex, ethnicity and severity, could be enrolled and mostly retained for a year of intensive, nearly fully remote collection. They describe the battery's time cost as likely not feasible for further scale-up.

They offer four candidate explanations for the retention. Devices participants found easy, manageable burden with adequate pay, perceived benefit from daily mood logging, and proactive staff monitoring with regular contact. Participant feedback supports each, but none was tested.

Feedback surveys were favourable. 96% at baseline reported satisfaction across tasks, pay, compliance confidence and staff. 60% found daily mood logging helpful. 3% said biweekly symptom surveys made their mental health worse.

## Relevance to Future Study Design

Severity stratification costs retention at the top of the scale. Severe depression at intake completed at 61.6% against 79.9% for no symptoms. Over-recruit the severe bins if the analysis needs them.

Age is the bigger gradient. The youngest band completed at 65.3% against 90.2% for those over 65, in a cohort where most of the youngest were students.

Place mandatory visits with care. Dropout spiked at each required check-in and at the first compensation boundary. Making a check-in a condition of continued participation converted a scheduling problem into attrition.

The support stack here is heavy and replicable only with funding. It combined automated missing-data flags, staff outreach, tiered pay up to US$1,070, a kept watch and quarterly progress emails. The 21-hour wear figure should be read as the product of that stack.

Two-watch rotation to avoid charging gaps was tried and abandoned as too complex. A single watch with a daily two-hour charge was the workable compromise.

## Evidence Confidence

Verified. The screening-to-completion funnel, the Table 1 completion rates by subgroup, the median time to dropout, the PHQ-8, Daily Reflection and wear-time figures, the wear definition, the compensation tiers and total, the loaner count, the pilot funnels and the funding and competing-interests statements were read from the Europe PMC full-text XML (PMC13437235) on 2026-10-31.

Reported. The milestone clustering of dropout is read from the text's description of Figure 1B rather than the figure itself.

Not assessed here. Supplementary Tables 1, 2, 6 and 7 and Supplementary Figures 1 to 12 were not retrieved. The per-task adherence table, full eligibility and the missing-data criteria sit there.

Conflict note. Apple funded the study, made the devices and processed the data before UCLA received it. Four authors were Apple employees with stock. The headline figures are simple counts from Table 1 and the text.

## Key Links

- Paper (OA): https://doi.org/10.1038/s44482-026-00029-3
- Europe PMC: https://europepmc.org/article/PMC/PMC13437235
- Local PDF: none held

## Related profiles

- Device: [Apple Watch / HealthKit](../../module-01-wearables/profiles/apple-watch-healthkit.md)
- Other Apple Research app cohorts: [`apple-heart-movement-study-retention.md`](apple-heart-movement-study-retention.md), [`apple-womens-health-study-retention.md`](apple-womens-health-study-retention.md)
- SensorKit in another population: [`sensorkit-techsans-older-adults.md`](sensorkit-techsans-older-adults.md)
- Same UCLA group, earlier student cohort on AWARE: [`aware-stand-mood-prediction-adherence.md`](aware-stand-mood-prediction-adherence.md)
- Large depression cohort on a different stack: [`radar-mdd-recruitment-retention.md`](radar-mdd-recruitment-retention.md)

## Sources

1. Douglas CS, Congdon E, Huang C, et al. *npj Digit Public Health* 2026;1:27. DOI 10.1038/s44482-026-00029-3. Full text, Table 1 and figure captions read from the Europe PMC full-text XML (PMC13437235), 2026-10-31. The first author is taken from the XML author records, not a PDF byline. Establishes every figure in this profile.
