# White et al. 2024 - RADAR-base with Fitbit, randomised test of in-app engagement components in former RADAR-MDD participants, N=100, 12 weeks

## Quick Facts

| Field | Details |
|---|---|
| Citation | White KM, Carr E, Leightley D, Matcham F, Conde P, Ranjan Y, Simblett S, Dawe-Lane E, Williams L, Henderson C, Hotopf M. "Engagement With a Remote Symptom-Tracking Platform Among Participants With Major Depressive Disorder: Randomized Controlled Trial." *JMIR mHealth and uHealth* 2024;12:e44214. DOI [10.2196/44214](https://doi.org/10.2196/44214). PMID 38241070 / PMC10837755. Epub 2024-01-19. |
| Study design | Single-centre, two-arm, parallel-group, participant-blinded RCT with 1:1 simple randomisation. ClinicalTrials.gov NCT04972474. Primary outcome was objective engagement, the percentage of 12 weekly PHQ-8 questionnaires completed. |
| Sample size (enrolled / analyzed) | 347 contacted. 114 agreed. 100 enrolled (50 per arm). 87 completed 12-week follow-up. 97 in the primary analysis and 92 in the combined-adherence analysis after technical exclusions. |
| Population | Adults with MDD who had previously taken part in RADAR-MDD at the London site. Mean age 53.3 (SD 14.3). 76% female. 12% reported suicidal ideation at baseline. |
| Duration | 12 weeks per participant. Follow-up April to September 2021, during UK COVID-19 lockdown periods. |
| Devices/platforms used | [RADAR-base](../../module-02-digital-phenotyping/profiles/radar-base.md) Android app with three weekly tasks (PHQ-8, Rosenberg Self-Esteem Scale, speech task). [Fitbit Charge](../../module-01-wearables/profiles/fitbit-google.md) for continuous passive data. Android phones carried over from RADAR-MDD. REDCap for consent, baseline and follow-up questionnaires. |
| Funding/COI | NIHR Maudsley Biomedical Research Centre. The RADAR-CNS project is IMI2 grant 115902 (EU Horizon 2020 and EFPIA). The senior author leads RADAR-CNS, a consortium with funding from Janssen, UCB, MSD, Biogen and Lundbeck. Participant compensation is not reported. |
| Last verified | 2026-10-31 |

## Summary

This is the module's only randomised test of whether interface changes raise engagement with a phenotyping platform. The answer was no.

The intervention arm got three additions. Notifications explained why symptom tracking mattered. A progress graph showed task completion. The home page listed research-team contact details. PHQ-8 completion was 68% in the intervention arm and 69% in control (P=.83).

The trial is also a clean measure of low-touch RADAR-base engagement. The team made one planned contact, a check-in email at week 6. Across both arms participants completed a median of 9 of 12 PHQ-8 tasks and had sufficient Fitbit data on a mean 74 of 84 days. 87% completed follow-up.

The sample sets the ceiling. Everyone had already used RADAR-base in RADAR-MDD and volunteered again. The authors read the null result partly as a ceiling effect in a motivated, altruistic cohort.

## Instrumentation and Deployment Model

Participants kept the Android phone RADAR-MDD had provided and were sent a Fitbit Charge. Enrolment was fully remote because of COVID-19. The principal investigator generated QR codes linking each participant's devices to the RADAR-base management portal and emailed personalised login instructions. Enrolment was by email for 89%, video call for 9% and phone for 2%.

All three tasks opened on the same day each week, an hour apart, and each closed after 24 hours. Control notifications read "Questionnaire Time. Won't usually take longer than 3 minutes." Intervention notifications added a sentence on the benefits of monitoring and said the task could be done "any time today."

Combined adherence was defined as completing at least 50% of the weekly tasks and having more than 2 Fitbit heart rate data points on at least 50% of days. The definition was chosen to match RADAR-MDD reporting.

App-use data came from Google Analytics.

## Recruitment and Retention

Up to three email invitations went to each eligible former RADAR-MDD London participant.

| Stage | n |
|---|---|
| Contacted | 347 |
| Agreed to participate | 114 (32.9%) |
| Enrolled | 100 (28.8%) |
| Withdrew | 1, citing technical issues with the study apps |
| Completed 12-week follow-up | 87 |

The trial was underpowered. The power calculation called for 132 participants to detect a 25-point difference in PHQ-8 completion.

Participants were not withdrawn for loss to follow-up. Confidence in the technology was not universal. 59% "strongly agreed" they were confident with the study phone and 51% with the Fitbit.

## Data Completeness and Technical Issues

Technical failures removed participants from analysis before any engagement question arose.

| Failure | n of 100 |
|---|---|
| Could not use the app or the Fitbit immediately after enrolment | 2 |
| Received no app notifications during follow-up | 1 |
| Could not sync the Fitbit with the phone | 4 |
| Opted out of the Fitbit at enrolment | 1 |
| Provided any app data | 97 |
| Provided any Fitbit data | 93 |

The authors treated these as technical limitations rather than non-engagement. They excluded 3 from the primary analysis and 8 from the combined-adherence analysis.

| Stream | Completion |
|---|---|
| PHQ-8 | Median 9 of 12 (IQR 6 to 10). 7 participants completed all 12. |
| Rosenberg Self-Esteem Scale | Median 9 of 12 (IQR 6 to 10) |
| Speech task | Median 8 of 12 (IQR 6 to 9) |
| Fitbit, days with at least 2 heart rate recordings | Mean 74 of 84 (SD 19.7) |
| Combined adherence, control | 67% (32/48) |
| Combined adherence, intervention | 80% (35/44), P=.98 as reported |

Google Analytics recorded a mean 22.0 notifications received in the intervention arm and 22.6 in control. Participants opened 34.3% and 39.9% of them. Control participants opened a higher share. Many participants in interviews were unsure whether they had seen all notifications their phone received.

Of 48 intervention participants, 29 (60%) viewed the progress report at least once. Those viewers completed 75.3% of PHQ-8 tasks against 57.0% for non-viewers. The complier analysis still found no between-arm difference.

No iOS breakdown applies. The app was Android-only.

## Feasibility Findings

The authors conclude that the adapted app did not raise objective or subjective engagement. They also conclude the system gave good data availability in a fully remote trial without planned researcher contact. They cite 87% follow-up, a median 75% task completion and 74 of 84 wear days.

They name design constraints. Working inside an established system meant some COM-B-derived features could not be built, including in-app reporting of technical malfunctions.

They recommend dynamic, context-tailored notifications and data insights. They recommend testing how research-team support interacts with in-app components. They recommend replicating with non-help-seeking or less tech-literate cohorts.

## Relevance to Future Study Design

Static engagement features do not move a motivated cohort. If budget must choose between in-app nudges and human contact, this trial gives no evidence for the nudges.

Expect about 7 of 100 participants to lose a data stream to setup or sync failure in the first weeks, even among experienced users. Count them separately from disengagement, as this trial did.

Do not trust notification analytics without checking. A companion RADAR-MDD paper reports that Google Analytics showed more questionnaires completed than notifications received ([`radar-mdd-usability-predictors-engagement.md`](radar-mdd-usability-predictors-engagement.md)). Here the received count averaged about 22 against three tasks a week for 12 weeks.

A progress graph sorts participants rather than changing them. The 18-point completion gap between viewers and non-viewers did not survive the complier analysis.

## Evidence Confidence

Verified. The recruitment funnel, withdrawal, follow-up rate, technical exclusions, per-task completion medians, Fitbit wear days, arm-level PHQ-8 and combined-adherence figures, complier figures, Google Analytics counts and the funding and conflicts statements were read from the Europe PMC full-text XML (PMC10837755, CC BY 4.0) on 2026-10-31.

Unclear. The text says 60% (35/58) of participants able to view the progress report did so more than once. Table 6 gives 29 of 48 (60%). The combined-adherence P value of .98 sits oddly beside a 67% versus 80% split. Both are reported here as printed.

Not assessed here. Whether Fitbit or speech features predicted depression is outside Module 3.

## Key Links

- Paper (OA, CC BY 4.0): https://doi.org/10.2196/44214
- Europe PMC: https://europepmc.org/article/PMC/PMC10837755
- Registration: https://clinicaltrials.gov/study/NCT04972474
- Local PDF: none held

## Related profiles

- Platform: [RADAR-base](../../module-02-digital-phenotyping/profiles/radar-base.md)
- Device: [Fitbit / Google](../../module-01-wearables/profiles/fitbit-google.md)
- Parent cohort the participants came from: [`radar-mdd-recruitment-retention.md`](radar-mdd-recruitment-retention.md), [`radar-mdd-longterm-engagement.md`](radar-mdd-longterm-engagement.md)
- Same cohort, usability and engagement: [`radar-mdd-usability-predictors-engagement.md`](radar-mdd-usability-predictors-engagement.md)
- RADAR-base during active treatment: [`radar-base-treatment-engagement.md`](radar-base-treatment-engagement.md)

## Sources

1. White KM, Carr E, Leightley D, Matcham F, Conde P, Ranjan Y, Simblett S, Dawe-Lane E, Williams L, Henderson C, Hotopf M. *JMIR Mhealth Uhealth* 2024;12:e44214. DOI 10.2196/44214. Full text, Tables 1 to 6 and figure captions read from the Europe PMC full-text XML (PMC10837755), 2026-10-31. The first author is taken from the XML author records, not a PDF byline. Establishes every figure in this profile.
