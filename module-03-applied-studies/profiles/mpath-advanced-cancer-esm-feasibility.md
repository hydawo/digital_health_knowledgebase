# Geeraerts et al. 2026 - High-intensity m-Path ESM on provisioned Android phones in advanced breast and lung cancer, N=40 over 7 days

## Quick Facts

| Field | Details |
|---|---|
| Citation | Geeraerts J, Pivodic L, de Nooijer K, Rosquin L, Decoster L, Fontaine C, Joris S, Naert E, Crombez G, De Ridder M, Van den Block L. "Uncovering fluctuations in daily symptoms and well-being among people with advanced cancer: An experience sampling methods study." *Palliative Medicine* 2026;40(4):535-545. DOI [10.1177/02692163261416264](https://doi.org/10.1177/02692163261416264). PMID 41677574. No PMCID found. Read from the author manuscript in the Ghent University repository. |
| Study design | Observational feasibility and acceptability study with a baseline session, 7-day ESM period and follow-up session. Protocol published separately. Reported against the STROBE checklist adapted for EMA. |
| Sample size (enrolled / analyzed) | 79 invited, 40 consented (50.6%). 1 dropped out after 2 days. 2 more were excluded from the ESM analysis for misreading the response scales. 37 contributed 1703 valid assessments. |
| Population | Adults with stage III or IV lung cancer or stage IV breast cancer and ECOG performance status of 2 or better, at University Hospitals Brussels and Ghent, Belgium. Stratified to four equal subgroups by age (under or over 70) and tumour site. Mean age 66.3 (range 35 to 83). 72.5% female. Data collected September 2023 to March 2024. |
| Duration | 7 consecutive days per participant. 60 assessments were scheduled across 6 days, with day 7 used to make up beeps lost on the baseline day. |
| Devices/platforms used | [m-Path](../../module-02-digital-phenotyping/profiles/m-path.md) on a study-provided Motorola e20 Android smartphone. The ESM-AC questionnaire, developed and content-validated by the same group. No passive sensing. |
| Funding/COI | Research Foundation Flanders (FWO) G0C8120N, plus an FWO postdoctoral fellowship 12AEO24N for one author. Authors declare no conflicts. Participant compensation is not reported. |
| Last verified | 2026-10-31 |

## Summary

This is the first study in the module to run ten-a-day ESM in advanced cancer. It is included for its full funnel, its compliance figure, and its finding that compliance did not depend on age.

Half of those invited took part. 40 of 79 (50.6%) consented. Most who declined cited no time or no interest.

Compliance was 71%. The study kept 1703 of 2400 scheduled assessments from 37 participants. No participant characteristic, time variable or symptom level significantly predicted compliance.

Age did not predict compliance, but it did affect data validity. The two participants excluded for misinterpreting the response scales were aged 81 and 82.

Participants opened a prompt a mean of 37 seconds after the beep (SD 66). They took 3.8 minutes to complete it (SD 1.9).

## Instrumentation and Deployment Model

Provisioned. Every participant received a Motorola e20 Android phone for the study, training in the m-Path app and a take-home manual. The team therefore controlled the OS and device model.

Beeps were auditory, about 30 seconds long and randomly timed within 10 daily blocks at least 30 minutes apart. The day started an hour after the participant's wake time and ended an hour before sleep, both set at baseline. The response window per beep is not stated in the main text.

The ESM-AC questionnaire had 29 to 33 items, with longer morning (30 to 34) and evening (34 to 39) versions. Responses used 0 to 100 visual analogue scales. Participants could add personally meaningful items at baseline. Four did.

Support was active. A researcher phoned each participant after day 1 to check for distress and help with the questionnaire. Phone and email support stayed available throughout. A safety protocol was published with the study protocol.

## Recruitment and Retention

Treating physicians identified eligible patients. Two researchers then approached them. 40 of 79 invited (50.6%) consented.

One participant (2.5%) withdrew after 2 days, citing stress from repetitive questions. Nobody else left the study.

The authors read the 50% enrolment rate, and the over-representation of highly educated and digitally skilled participants, as a likely selection bias against less digitally skilled people.

## Data Completeness and Technical Issues

Compliance was defined as completed divided by scheduled assessments. The study kept 1703 of 2400 (71%). This figure is net of the dropout, the two scale-reversal exclusions, and whole questionnaires that participants flagged as mistaken at follow-up.

The paper is internally inconsistent here. The Discussion's limitations paragraph refers to "the 80% completion rate". The Results give 71% of scheduled assessments. The text does not reconcile the two.

Participants reported consciously missing an assessment on 17 days in total. Most reasons related to doing activities.

Response-scale reversal was a real failure mode with single-item VAS questions. Participants rated their own reversal mistakes as rare (mean 2.1 on a 1 to 7 scale). Yet two participants were excluded for it. Discussing a visual summary with each participant at follow-up is how the team found erroneous responses.

No device, app, notification or battery problems are reported.

## Feasibility Findings

The authors conclude that high-intensity ESM was feasible and acceptable for people with advanced breast or lung cancer of all ages in the sample.

Burden ratings were low on 7-point scales, with item means from 1.4 to 3.6. Ease of use ranged from 4.3 to 6.6. Instruction clarity ranged from 6 to 6.9. Reactivity ranged from 1.1 to 1.5. The highest burden item was "The questionnaire became boring during the past week" at 3.6.

They credit training and the day-1 check-up call with improving experience and data quality. They suggest pen-and-paper alternatives to widen inclusion. They also suggest that more days at lower intensity may yield similar data with better enrolment.

## Relevance to Future Study Design

Provisioning one Android model removed device heterogeneity. It also adds hardware cost and a return step that the paper does not discuss.

Ten beeps a day for a week held 71% compliance in a population with a mean age of 66. Age did not predict compliance.

Screen older participants for comprehension of the response scale. The only age signal in this study was invalid data, not missing data.

Budget for one support call after day 1. The paper describes it as standard procedure and credits it with better data.

ECOG 2 or better was required. The results do not cover sicker patients, and the authors say so.

## Evidence Confidence

Verified for the funnel, the dropout and its reason, the compliance count, latency, completion time, the device and the funding statement. These were read from the author manuscript held by the Ghent University repository on 2026-10-31.

Unclear for the true compliance figure, because the manuscript gives both 71% and 80%. The published typeset version was not read. The supplements, including the app interface screenshots, were not read.

## Key Links

- Published article: https://doi.org/10.1177/02692163261416264
- Author manuscript: https://biblio.ugent.be/publication/01KK8VGXSQT3AB6AJMJXSGW1EH
- Local PDF: none held. Not stored by this screening pass.

## Related profiles

- Platform: [m-Path](../../module-02-digital-phenotyping/profiles/m-path.md)
- Other m-Path deployments: [`mpath-dementia-esm-feasibility.md`](mpath-dementia-esm-feasibility.md), [`mpath-avatar2-esm-engagement.md`](mpath-avatar2-esm-engagement.md)
- Other cancer deployments: [`aware-chemotherapy-engagement.md`](aware-chemotherapy-engagement.md), [`beiwe-fitbit-gynecologic-cancer-hope.md`](beiwe-fitbit-gynecologic-cancer-hope.md), [`samsung-palliative-pain-ecuador.md`](samsung-palliative-pain-ecuador.md)

## Sources

1. Geeraerts J, Pivodic L, de Nooijer K, Rosquin L, Decoster L, Fontaine C, Joris S, Naert E, Crombez G, De Ridder M, Van den Block L. *Palliative Medicine* 2026;40(4):535-545. DOI 10.1177/02692163261416264. Author manuscript read from the Ghent University repository PDF, 2026-10-31. Establishes every figure in this profile.
