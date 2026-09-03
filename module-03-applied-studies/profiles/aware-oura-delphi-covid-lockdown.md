# Moshe et al. 2021 - AWARE on iOS plus a participant-owned Oura Ring, 30 days under Finnish COVID-19 restrictions, N=60

## Quick Facts

| Field | Details |
|---|---|
| Citation | Moshe I, Terhorst Y, Opoku Asare K, Sander LB, Ferreira D, Baumeister H, Mohr DC, Pulkki-Råback L. "Predicting Symptoms of Depression and Anxiety Using Smartphone and Wearable Data." *Frontiers in Psychiatry* 2021;12:625247. DOI [10.3389/fpsyt.2021.625247](https://doi.org/10.3389/fpsyt.2021.625247). PMID 33584388 / PMC7876288. Published 2021-01-28. |
| Study design | Longitudinal observational study over 30 days. DASS-21 at days 1, 16 and 31. Mood EMA three times a day. Multilevel models predicting symptom scores from phone and ring features. |
| Sample size (enrolled / analyzed) | 60 at intake, 55 analysed. |
| Population | General-population adults recruited online, non-clinical. Ages 24 to 68, mean 42.8 (SD 11.6). 54.5% female. 92.7% White. 80% held a bachelor's degree or higher. 66% were in Finland. Recruited 12 to 29 April 2020, during first-wave COVID-19 restrictions. |
| Duration | 30 days per participant. |
| Devices/platforms used | A custom iOS app, Delphi, built on the [AWARE framework](../../module-02-digital-phenotyping/profiles/aware-framework.md) (Battery, GPS, Screen and Timezone sensors plus the ESM Scheduler plugin). A participant-owned [Oura Ring](../../module-01-wearables/profiles/oura.md), generation not stated, read through Apple HealthKit. Both devices were the participant's own. |
| Funding/COI | Academy of Finland grants 316253, 320089 and 318927; NIMH P50 MH119029 and R01 MH111610; the Wihuri and Yrjö Jahnsson Foundations. The authors declare no commercial or financial relationships. Denzil Ferreira, who created AWARE, is a co-author. No Oura relationship is stated. No payment to participants. |
| Last verified | 2026-09-03 |

## Summary

The only study in the module that pairs AWARE with a consumer ring, and the only AWARE deployment here that ran on iOS alone. Every other AWARE profile is Android or mixed. It is also the module's second Finnish cohort and one of few outside North America and the UK.

Its operational content is thin, which the authors do not hide. The paper is about prediction. What it reports on deployment is a dropout breakdown, two questionnaire completion rates, two missingness figures, a monitoring dashboard, and an inclusion rule that did the recruitment work.

Five of 60 left. One over privacy, two over the burden of self-report, two for unknown reasons. Of the 55 who stayed, 47 (85.5%) completed the midpoint questionnaire and 54 (98.2%) the endpoint one. Missingness was 10% for the DASS-21 and 9.1% for the sensing variables. The study paid nothing. Participants received a personalised mental-health report reviewed by a clinical psychologist at the end.

The inclusion rule is the part worth copying or avoiding. Participants had to already own an iPhone and an Oura Ring. That removed provisioning, sizing, shipping and setup from the study's cost, and it produced a cohort that was 93% White, 80% degree-holding, and iOS by construction. The authors name the iOS restriction as a sampling bias in their limitations.

## Instrumentation and Deployment Model

Bring your own device on both instruments. After online consent, participants received an emailed link to install Delphi. The app needed always-on location permission, HealthKit access and notification permission. Delphi collected the phone sensors through AWARE and pulled the ring's activity, sleep and HRV data through HealthKit. Data were stored on the phone and uploaded to a cloud server when Wi-Fi was available.

Mood prompts came three times a day, randomised within a 30-minute window around 09:00, 14:30 and 20:00, through AWARE's ESM Scheduler. The DASS-21 ran at days 1, 16 and 31.

Monitoring was continuous. A secure web dashboard showed each participant's incoming data and refreshed every 15 minutes. "Cases of missing data were resolved via email." How often that happened is not reported. At the end participants were asked to uninstall the app.

The AWARE iOS integration was custom work by the study team. Sampling frequencies are in a supplementary table that is not part of the PDF.

## Recruitment and Retention

Recruitment was posts on online communities and social media. The target was 40, taken from an earlier GPS study. Because "dropout rates in longitudinal observation studies using digital phenotyping data are typically high," recruitment ran for two more weeks after the target was reached and closed at 60. The number who saw the posts or were screened out for lacking an iPhone or a ring is not reported.

| Stage | n |
|---|---|
| Enrolled | 60 |
| Dropped out over privacy concerns | 1 |
| Dropped out over self-report burden | 2 |
| Dropped out for unknown reasons | 2 |
| Analysed | 55 |
| Completed the midpoint DASS-21 (of 55) | 47 (85.5%) |
| Completed the endpoint DASS-21 (of 55) | 54 (98.2%) |

Retention is not formally defined. Nobody was paid.

## Data Completeness and Technical Issues

Missingness "only occurred in the DASS-21 assessment (10%) and the sensing variables (9.1%)." The sensing figure is a single number across all phone and ring features aggregated to the day. There is no breakdown by sensor, by device, by participant or over time, and no definition of what makes a sensing day missing. Missingness was assumed missing at random and handled by multilevel multiple imputation with 20 datasets.

The EMA mood response rate is not reported.

The one technical failure mode named is in GPS. Preprocessing removed duplicate records, points with accuracy worse than the 80th percentile, and "GPS coordinates with latitude 0.0 and longitude 0.0 that arose due to sensing errors." Nothing is said about battery, app stability, HealthKit sync from the ring, or upload gaps.

Ring wear time is not reported and no ring generation is stated.

## Feasibility Findings

The authors frame no feasibility conclusions. Their limitations are analytic and demographic. The sample was small, skewed toward White, employed and educated people, restricted to iOS users, non-clinical, and observed after restrictions had already begun so that no pre-pandemic movement baseline exists. Their recommendations are for larger samples, longer windows, both operating systems and clinical populations.

## Relevance to Future Study Design

A "bring your own ring" inclusion rule is the cheapest possible wearable deployment. Here it cost nothing in hardware and lost only 5 of 60 in a month. The price is the cohort. Anyone who already owns a ring and an iPhone in 2020 is not a general population, and the authors say so.

Running AWARE on iOS required a custom app and framework integration work. That is a real engineering cost that the paper does not itemise, and it sits with the study team rather than the platform. Compare the Android-side deployments in [`aware-momo-mood-mood-disorders.md`](aware-momo-mood-mood-disorders.md) and [`aware-binge-drinking-jitai-sensor-loss.md`](aware-binge-drinking-jitai-sensor-loss.md).

Reading the ring through HealthKit rather than the vendor's API means the study sees only what the vendor app writes to HealthKit. The paper does not discuss what that excluded.

A 15-minute dashboard plus email follow-up is a low-cost support model. It is not costed, and its contribution to the 9.1% sensing missingness cannot be separated from the cohort's motivation.

## Evidence Confidence

Verified. The enrolment and dropout figures with reasons, the midpoint and endpoint completion rates, the two missingness percentages, the recruitment window and method, the inclusion criteria, the sensor list and EMA schedule, the dashboard and email support description, the compensation model, and the funding statement were read from the published PDF (Frontiers in Psychiatry, CC BY) on 2026-09-03.

Not assessed here. The prediction results (location variance, sleep duration, time in bed and HRV as predictors of DASS-21 subscales) are the paper's subject. Oura metric validity belongs to Module 1's [Oura profile](../../module-01-wearables/profiles/oura.md) and AWARE's capabilities to Module 2's [AWARE profile](../../module-02-digital-phenotyping/profiles/aware-framework.md).

Scope note. The deployment reporting here is one paragraph and two sentences. The profile exists because the combination is unique in the module, not because the operational evidence is deep, and any cross-study comparison should weight it accordingly.

## Key Links

- Paper (OA, CC BY): https://doi.org/10.3389/fpsyt.2021.625247
- Europe PMC: https://europepmc.org/article/PMC/PMC7876288
- Local PDF: `../../module-01-wearables/literature/oura/2021-moshe-frontierspsychiatry-predicting-depression-anxiety.pdf` (already held by Module 1; not duplicated)

## Related profiles

- Platform: [AWARE framework](../../module-02-digital-phenotyping/profiles/aware-framework.md)
- Device: [Oura](../../module-01-wearables/profiles/oura.md)
- Other AWARE deployments: [`aware-stand-mood-prediction-adherence.md`](aware-stand-mood-prediction-adherence.md), [`aware-momo-mood-mood-disorders.md`](aware-momo-mood-mood-disorders.md), [`aware-msavorus-loneliness-multidevice.md`](aware-msavorus-loneliness-multidevice.md) (the other AWARE plus Oura pairing, with provisioned rings)
- Other Oura deployments: [`oura-tempredict-healthcare-worker-adherence.md`](oura-tempredict-healthcare-worker-adherence.md), [`oura-university-freshmen-sleep.md`](oura-university-freshmen-sleep.md)
- Finland: [`aware-momo-mood-mood-disorders.md`](aware-momo-mood-mood-disorders.md)

## Sources

1. Moshe I, Terhorst Y, Opoku Asare K, et al. *Front Psychiatry* 2021;12:625247. DOI 10.3389/fpsyt.2021.625247. Full text and Table 1 read from the published PDF, 2026-09-03. Establishes every figure in this profile.
