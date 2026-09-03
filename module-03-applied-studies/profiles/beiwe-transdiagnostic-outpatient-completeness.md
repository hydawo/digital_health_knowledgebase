# Pellegrini et al. 2022 - Beiwe across four diagnostic groups, 8 weeks, paid and visit-supported, N=45

## Quick Facts

| Field | Details |
|---|---|
| Citation | Pellegrini AM, Huang EJ, Staples PC, Hart KL, Lorme JM, Brown HE, Perlis RH, Onnela JP. "Estimating longitudinal depressive symptoms from smartphone data in a transdiagnostic cohort." *Brain and Behavior* 2022;12:e2077. DOI [10.1002/brb3.2077](https://doi.org/10.1002/brb3.2077). PMID 35076166 / PMC8865149. Accepted 2021-02-05. Pellegrini and Huang are joint first authors. |
| Study design | Prospective cohort, 8 weeks, five in-person visits with a rater-administered MADRS every two weeks. Linear mixed models predicting MADRS from phone surveys and passive data. |
| Sample size (enrolled / analyzed) | 45 consented and completed baseline. 41 analysed. 38 completed the 8 weeks (84% of 45). |
| Population | Outpatients from Massachusetts General Hospital clinics plus advertised healthy controls, recruited 2015 to 2018. Target groups of 11 with major depressive disorder, 11 with bipolar disorder, 11 with schizophrenia or schizoaffective disorder, and 12 controls. Of the 41 analysed, 63% female, mean age 43 (SD 12, range 21 to 68), 71% White, 20% African-American. |
| Duration | 8 weeks per participant. |
| Devices/platforms used | [Beiwe](../../module-02-digital-phenotyping/profiles/beiwe.md) on participant-owned iOS and Android phones. Accelerometer 10 s on, 10 s off. GPS 2 min on, 10 min off. Anonymised call logs on Android only. Daily four-item survey and weekly PHQ-8 in the app. |
| Funding/COI | NIMH and NHGRI 1P50MH106933 (Perlis); NIH 1DP2MH103909 (Huang, Staples, Lorme, Onnela). Staples is employed by Mindstrong Health. Perlis holds equity and advisory roles in several companies. Onnela receives research funding from Otsuka and Apple and an unrestricted gift from Mindstrong. Sponsors had no role in design or analysis. |
| Last verified | 2026-09-03 |

## Summary

A short, well-supported clinical deployment where retention was high and passive completeness was poor, in the same people at the same time. That combination is the reason it is here.

Retention first. 38 of 45 (84%) completed the eight weeks. Participants were paid $50 after baseline and $100 at completion, came to the clinic five times, and had to answer the daily survey at least five days a week to stay enrolled. The authors are careful about what that buys. "While the participant payment employed in this study precludes strong conclusions about acceptability, the high retention rate suggests that, with compensation, participants are willing to adopt this technology."

Completeness second. The paper defines it at the participant level as minutes of data collected divided by minutes expected, over every full day between baseline and the last visit. Accelerometer expected every minute. GPS expected one minute in six. The proportions ranged from 0 to 0.99 for accelerometer and 0 to 0.87 for GPS. Only 23 of 41 (56%) reached 0.5 for accelerometer. Only 16 of 41 (39%) reached 0.5 for GPS. Weekly PHQ-8 completion, by contrast, went from 95% for the first survey to 80% for the last.

So in a paid, visit-supported, two-month study, fewer than half the participants delivered even half the expected GPS. The paper does not attribute this to any specific cause. It shows per-participant heatmaps with long gaps and notes that "the timing of the missing gaps may not be random." Its design recommendation follows from that. Monitor each participant's missingness during the study and intervene.

The cohort is also the only transdiagnostic psychiatric outpatient Beiwe deployment in the module.

## Instrumentation and Deployment Model

Bring your own device. Eligibility required owning an iOS or Android smartphone and being judged by the site investigator as likely able to comply. Study staff installed and activated the app at the baseline visit with a random eight-character Beiwe ID.

Data were encrypted on the phone and uploaded only over Wi-Fi "to avoid charges associated with uploading large volumes of data, roughly 1GB per subject-month." After upload the data were deleted from the phone. Identifiers were hashed on the device.

Active data were a daily four-item Likert survey on mood, social interest, sleep quality and activity level, and a PHQ-8 every Saturday. The suicidality item was omitted at the IRB's determination that including it would require real-time monitoring the investigators considered infeasible. The daily survey carried the enrolment rule. "To remain enrolled in the study, participants were required to respond to the surveys at least five times a week." Whether anyone was removed under this rule is not reported.

Participants were reimbursed for parking and travel at each visit. Those who withdrew early received $25 on top of the initial $50.

## Recruitment and Retention

Recruitment was from MGH outpatient clinics for the three diagnostic groups and by advertisement for controls, with SCID confirmation of primary diagnosis. Numbers approached or screened are not reported, and nothing is said about how many were excluded for not owning a smartphone.

| Stage | n |
|---|---|
| Consented and completed baseline | 45 |
| Terminated before the first follow-up visit | 4 |
| of which unable to download the app | 1 |
| of which unable to use the app | 1 |
| of which declined to continue | 2 |
| Included in analysis | 41 |
| Terminated after the first follow-up visit | 3 |
| of which inconsistent access to a mobile phone | 1 |
| of which declined to continue | 1 |
| of which duplicate or had already completed the study | 1 |
| Completed the 8-week study | 38 (84% of 45) |

Final group sizes were 9 with depression, 9 bipolar, 9 schizophrenia or schizoaffective, and 11 controls. Two of the seven losses were app-usability failures at onboarding and a third was phone access, which puts three of seven on the technology rather than on the participant's choice.

## Data Completeness and Technical Issues

The completeness definition is one of the clearest in the module and is worth restating. For each participant, the number of minutes with data is divided by the number of minutes expected between the day after baseline and the day before the final visit. Accelerometer is expected every minute because its cycle is 10 seconds on and 10 off. GPS is expected in one minute of every six because its cycle is 2 minutes on and 10 off.

| Stream | Range of participant proportions | Participants at or above 0.5 |
|---|---|---|
| Accelerometer | 0 to 0.99 | 23 of 41 (56%) |
| GPS | 0 to 0.87 | 16 of 41 (39%) |

The study still captured 674,969,086 accelerometer and 14,733,731 GPS measurements. "The quantity of collected data for iOS phones tended to be greater on average than for Android phones." No figures are given and the iOS-to-Android split is not printed. Android communication logs were available for 19 of the 41.

Survey completion was defined per survey as the share of participants who completed it, with a late completion credited to the later week. The first weekly PHQ-8 reached 95% and the last, about two months in, 80%. 78% of participants completed a PHQ-8 in eight or more weeks. Daily survey completion is not reported.

Per-participant hourly heatmaps in the supplement show one participant with near-complete data, one with long gaps, and one with medium-quality stretches broken by periods of nothing. The authors avoided naive averaging over available data because it "would overweight time intervals during which data tended to be collected," and warn that predictors "may be inaccurate when the proportions of data collected are low."

Technical failure modes named in the paper are the app that could not be downloaded, the app that could not be used, and the participant with inconsistent phone access. No server, sync, upload or battery incidents are reported. The Discussion raises phone carriage as a confound, since activity curves depend on "how often each participant carried their phone."

The collection window (2015 to 2018) predates Beiwe's 2024 heartbeat feature, so these completeness figures are pre-heartbeat lower bounds like the other Beiwe entries in the module.

## Feasibility Findings

The authors conclude that compensated participants were willing to adopt the technology, that passive predictors did not improve on baseline MADRS plus demographics, and that low per-participant completeness is a plausible reason. They contrast their supported design with the unpaid, unsupported schizophrenia pilot in [`beiwe-schizophrenia-state-clinic-pilot.md`](beiwe-schizophrenia-state-clinic-pilot.md), and state the limit of their own evidence directly. The design "precludes conclusions about application of smartphone apps in longer-term studies or those using 'lighter touch' designs without in-person visits."

Their recommendation is procedural. "Strategies to reduce missing data (for example, by monitoring data missingness for each participant during the course of the study and intervening where required) merit consideration."

## Relevance to Future Study Design

Retention and completeness are different outcomes, and this study is the cleanest small demonstration of that in the module. 84% of people finished. 39% of people delivered half the expected GPS. Both numbers are true of the same eight weeks. Compare [Matcham 2022](radar-mdd-recruitment-retention.md), where the same gap appears at ten times the scale.

State the expected denominator. The completeness figures here are only interpretable because the paper says what one minute of GPS every six means. A study quoting "completeness" against wall-clock time on a duty-cycled sensor is not comparable to this one.

Budget for onboarding failures. Two of 45 could not install or use the app at the first visit. That is small in absolute terms and large as a share of the seven losses.

Monitoring during the study, not after it, is the authors' own answer. The module's later entries show what that costs when it is done. [Calvert 2026](mindlamp-linc-passive-data-quality.md) reports the staff time.

Wi-Fi-only upload is a cost decision that becomes a data decision. This study chose it to spare participants data charges. The schizophrenia pilot on the same platform lost one participant's entire dataset to it.

## Evidence Confidence

Verified. The CONSORT flow with itemised reasons, the completion rate, the compensation schedule, the enrolment rule, the sampling configuration, the Wi-Fi upload policy and data-volume estimate, the completeness definition and both threshold counts, the measurement totals, the PHQ-8 completion figures, the demographic table, and the funding and conflict statements were read from the published PDF (Brain and Behavior, CC BY) on 2026-09-03.

Reported. The heatmap descriptions and the per-participant completeness distributions are in supplementary figures not included in the PDF. The profile relies on the paper's text about them.

Not assessed here. The MADRS prediction results are the paper's subject and not deployment findings.

Conflict note. The senior author leads the platform, one co-author is employed by a commercial digital-phenotyping company, and the other senior author has extensive industry roles. The completeness figures reported are unflattering to the platform, which is the main reason they are treated as Verified rather than discounted.

## Key Links

- Paper (OA, CC BY): https://doi.org/10.1002/brb3.2077
- Europe PMC: https://europepmc.org/article/PMC/PMC8865149
- Local PDF: `../../module-02-digital-phenotyping/literature/beiwe/2022-pellegrini-brainbehav-estimating-longitudinal-depressive-symptoms-smartphone-data.pdf` (already held by Module 2; not duplicated)

## Related profiles

- Platform: [Beiwe](../../module-02-digital-phenotyping/profiles/beiwe.md)
- The unpaid, unsupported contrast on the same platform: [`beiwe-schizophrenia-state-clinic-pilot.md`](beiwe-schizophrenia-state-clinic-pilot.md)
- Retention and completeness diverging: [`radar-mdd-recruitment-retention.md`](radar-mdd-recruitment-retention.md), [`beiwe-als-adherence.md`](beiwe-als-adherence.md)
- Beiwe missingness by sociodemographics and OS: [`beiwe-missing-data-sociodemographic.md`](beiwe-missing-data-sociodemographic.md)
- Monitoring missingness during a study: [`mindlamp-linc-passive-data-quality.md`](mindlamp-linc-passive-data-quality.md)
- Incentives and what they buy: [`beiwe-spinal-cord-injury-incentives.md`](beiwe-spinal-cord-injury-incentives.md)

## Sources

1. Pellegrini AM, Huang EJ, Staples PC, et al. *Brain Behav* 2022;12:e2077. DOI 10.1002/brb3.2077. Full text, Figure 1 and Tables 1 to 3 read from the published PDF, 2026-09-03. Establishes every figure in this profile.
