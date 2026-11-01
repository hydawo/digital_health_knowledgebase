# Hackett et al. 2024 - mindLAMP GPS phenotyping in Philadelphia older adults, self-hosted, 4 weeks, N=37

## Quick Facts

| Field | Details |
|---|---|
| Citation | Hackett K, Xu S, McKniff M, Paglia L, Barnett I, Giovannetti T. "Mobility-Based Smartphone Digital Phenotypes for Unobtrusively Capturing Everyday Cognition, Mood, and Community Life-Space in Older Adults: Feasibility, Acceptability, and Preliminary Validity Study." *JMIR Human Factors* 2024;11:e59974. DOI [10.2196/59974](https://doi.org/10.2196/59974). PMID 39576984 / PMC11624463. Published 2024-11-22. Companion paper on the same cohort: Calvert E, Hackett K, Torous J, Giovannetti T. "Barriers and facilitators to usability of a smartphone-based digital mental health tool in older adults: Insights from a secondary analysis of mindLAMP." *International Psychogeriatrics* 2026;38(2):100123. DOI [10.1016/j.inpsyc.2025.100123](https://doi.org/10.1016/j.inpsyc.2025.100123). PMID 40925804 / PMC13142898. Published online 2025-09-08. |
| Study design | Single-arm feasibility, acceptability and preliminary validity study. Feasibility and acceptability are primary aim 1. The Calvert paper is a post hoc usability analysis of the same 37 people. |
| Sample size (enrolled / analyzed) | 37 enrolled and 37 completed. All 37 in the feasibility analysis. 34 in the validity analysis after 3 were excluded for major health events during monitoring. All 37 in the Calvert usability analysis. The number screened or approached is not reported. |
| Population | Community-dwelling adults aged 63 to 85 in the Philadelphia region, recruited from specialty dementia clinics and the community. 31 healthy cognition, 5 MCI, 1 mild dementia per Hackett. Calvert classifies the same cohort as 30 healthy, 5 MCI, 1 "impaired, not MCI" and 1 mild dementia. 27 iPhone and 10 Android users. Highly educated (76% bachelor's degree or higher per Calvert). |
| Duration | About 4 weeks per participant between two study visits. Participation ran April 2022 to January 2024. Participants with unplanned travel had their monitoring extended and travel days removed. |
| Devices/platforms used | [mindLAMP](../../module-02-digital-phenotyping/profiles/mindlamp.md) on participants' own phones (BYOD), served from a self-deployed LAMP platform on a Temple University cloud server. Passive GPS was the analysed stream. A nightly 5-item mindLAMP survey ran alongside it. No wearable. |
| Funding/COI | National Institute on Aging (F31AG069444, T32AG066598, R01AG062503, R21AG066771) and R01MH116884. Hackett declares no conflicts. Calvert declares no conflicts. Torous, corresponding author of the companion paper only, is in the BIDMC Department of Psychiatry. Hackett states that mindLAMP is developed by the BIDMC Division of Digital Psychiatry. |
| Last verified | 2026-10-31, from the Europe PMC full-text XML of both papers |

## Summary

This is a mindLAMP deployment in community-dwelling older adults across healthy cognition, MCI and mild dementia. It is small and highly educated. Its operational value is in what the authors logged about keeping GPS flowing on personal phones.

Retention was complete. All 37 participants finished the 4-week period and the second visit without requesting withdrawal. Participants were paid US$50 upfront rather than on completion.

Battery was the main participant-side cost. 41% (15/37) said they charged their phone more during the study. 46% (17/37) reported a major change in how they used their phone.

Passive data loss was moderate and patterned by OS. Participants averaged 423 (SD 352) minutes of missing GPS a day, about 29% of the day. iPhone users had significantly less missing GPS than Android users (r=-0.64, surviving Bonferroni correction). Black participants had more missing GPS than White or Asian participants, and Black participants were more often Android owners.

The companion paper adds the active stream. Mean nightly survey completion was 80% (SD 20%) over the 4 weeks.

## Instrumentation and Deployment Model

BYOD on iOS or Android. Eligibility required at least one year of existing smartphone use, home Wi-Fi, daily phone use and no plan to change phones during the study (Hackett, Recruitment).

Configuration was done in person at session 1. Staff downloaded mindLAMP, logged the participant in with a study-generated 10-digit user ID and enabled continuous location services (Hackett, Study Timeline). Calvert adds that staff also enabled push notifications for the nightly survey.

GPS was set to record "at a maximum frequency of 1 Hz" (Hackett, Digital Phenotyping). Features were computed after the study with the Barnett and Onnela R script, which multiply imputes missing GPS before feature calculation.

The server was self-hosted. The team bought a 1-TB Temple-approved cloud server, configured it with the LAMP API, and stored data in CouchDB (Hackett, Backend Technical Implementation). Temple IT handled security monitoring and backup. The BIDMC team continued to maintain the app itself.

The team wrote its own missing-data alert. A cron job emailed the study team when a participant had more than 3 days of missing sensor data, giving the user ID and the missing sensor. A staff member then contacted the participant.

Each participant had an informant. Informants corroborated clinical history and were asked to help with technical problems, particularly for participants with MCI or dementia.

Participants were told not to enter low-battery or airplane mode and not to log out of the app. The app was deleted at session 2.

The training protocol took a mean of 20.2 minutes (SD 6.5) per Calvert. Participants needed a mean of 1.0 attempt (SD 0.2) to complete a mock nightly survey. They took home a printed binder of the training slides.

## Recruitment and Retention

Recruitment drew on specialty dementia clinics, previous participants of the lab's other studies, community outreach events and educational talks at community centres (Hackett, Recruitment). Recruitment began in January 2022. Screening and refusal counts are not reported.

Retention was 100% (37/37). No participant requested withdrawal. The retention definition is completing the 4-week period and session 2.

Three participants (8%) had major health events during monitoring. These were an eye surgery, a fall with loss of consciousness, and a fall with head trauma plus COVID-19 infection. They completed the study but were excluded from the validity analysis only.

Compensation was US$50, paid upfront at session 1. No completion-contingent payment was used.

Consent comprehension was measured with a 10-item quiz. The mean score was 97% (SD 5.7%). 76% (28/37) scored 100% on the first attempt. The most often missed item was the false statement that using mindLAMP would improve cognition, answered "yes" by 13% (5/37). Quiz scores were associated with education (rs=0.65) and differed by race.

## Data Completeness and Technical Issues

Mean missing GPS was 423 (SD 352) minutes a day before imputation (Hackett, Preliminary Analyses). The authors describe this as about 29% of the day. Per-participant distributions and the share of zero-data days are in Multimedia Appendix 2, which was not retrieved.

OS mattered for completeness. Phone type was unrelated to every mean-level GPS feature except minutes missing. iPhone users had less missing GPS (r=-0.64, P<.0038). Day-to-day variability in minutes missing was also higher for iPhone users and survived correction.

Race differences appeared only in missingness. Black participants had more missing GPS than White (P=.003) and Asian (P=.02) participants. A greater share of Black participants owned Android phones (chi-square 6.9, P=.03). The authors suggest the race difference may be an OS effect. iPhone ownership was also correlated with income (r=0.49).

Six troubleshooting incidents were logged for missing GPS, affecting 5 participants (14%). The named causes were an Android phone entering safe mode, location permission reset from "always" to "only while using app", an outdated mindLAMP version, low-battery mode, and accidental deletion of the app. All were resolved remotely by phone.

Participant-reported phone problems were few. 92% (34/37) reported no new phone problems. One reported technical issues judged unrelated to the app. One reported disrupted text messages. One said the phone was "a little slow and lack of charge."

Charging behaviour changed. 41% (15/37) charged more. 14% (5/37) carried their phone more. 5% (2/37) carried it less. 3% (1/37) used it less overall.

Nightly survey completion averaged 80% (SD 20%) per Calvert. Calvert found no significant usability differences by phone type. The per-OS survey completion figure is not reported.

Not reported. Accelerometer or other sensor completeness, though Calvert says "GPS and other sensor data" were collected. Server downtime. Number of cron alerts that fired. Battery percentage data.

## Feasibility Findings

Hackett concludes that mobility phenotypes "are feasibly captured from older adults' personal smartphones." The authors flag increased charging as the main feasibility cost. They note it may undermine naturalistic collection, particularly if battery is itself treated as a biomarker.

Their recommendations are to test lower GPS sampling frequencies through the LAMP platform, to consider giving participants portable batteries, to revise consent language with more diverse co-designers, and to state expected benefits more clearly. They also recommend the automated missing-data check as a practice for future studies.

Calvert concludes that older adults "may be able to successfully engage" with a phenotyping app after modest training. Calvert cautions that the sample was highly educated and technologically proficient.

## Relevance to Future Study Design

A team running passive GPS in older adults can expect near-complete retention over 4 weeks with in-person setup, an informant and upfront payment. The cohort was mostly cognitively healthy and highly educated, so the figure may not hold in impaired samples.

Budget for battery complaints. Continuous 1 Hz GPS led 41% of participants to charge more. The authors propose lower sampling as the fix but did not test it.

Expect Android to lose more GPS than iPhone. In this cohort the OS effect also surfaced as an apparent race difference in missingness. A study comparing demographic groups should model phone type.

Write an automated gap alert. A more-than-3-days rule caught permission resets, low-power modes, an outdated app version and an app deletion. All six incidents were fixed by phone without a visit.

The self-hosted deployment needed a purchased cloud server and institutional IT for monitoring and backup. Server cost is not reported.

## Evidence Confidence

Verified. Retention, the consent-quiz results, the debriefing counts, the six troubleshooting incidents and their causes, the missing-GPS mean and its OS and race associations, and the deployment details were read from the Europe PMC full-text XML of Hackett et al. (PMC11624463, CC BY 4.0) on 2026-10-31. Training time and nightly survey completion were read from the Europe PMC full-text XML of Calvert et al. (PMC13142898, CC BY 4.0) on the same date.

Unclear. The two papers classify the cognitive groups differently (31 healthy in Hackett, 30 healthy plus 1 "impaired, not MCI" in Calvert). Recruitment start is January 2022 in both, while Hackett gives April 2022 as the start of participation. Multimedia appendices of both papers were not retrieved.

Not assessed here. Whether the GPS features are valid markers of cognition is the paper's aim 2 and belongs with Module 2's [mindLAMP profile](../../module-02-digital-phenotyping/profiles/mindlamp.md).

## Key Links

- Hackett 2024 (OA, CC BY 4.0): https://doi.org/10.2196/59974
- Europe PMC, Hackett: https://europepmc.org/article/PMC/PMC11624463
- Calvert 2025 (OA, CC BY 4.0): https://doi.org/10.1016/j.inpsyc.2025.100123
- Europe PMC, Calvert: https://europepmc.org/article/PMC/PMC13142898
- Local PDF: not held. Neither paper is in `module-02-digital-phenotyping/literature/mindlamp/`.

## Related profiles

- Platform: [mindLAMP](../../module-02-digital-phenotyping/profiles/mindlamp.md)
- Other mindLAMP deployments in this module: [`mindlamp-linc-passive-data-quality.md`](mindlamp-linc-passive-data-quality.md), [`mindlamp-global-cognitive-multisite.md`](mindlamp-global-cognitive-multisite.md), [`mindlamp-relapse-3site.md`](mindlamp-relapse-3site.md)
- Older adults or cognitive impairment: [`sensorkit-techsans-older-adults.md`](sensorkit-techsans-older-adults.md), [`mpath-dementia-esm-feasibility.md`](mpath-dementia-esm-feasibility.md), [`radar-ad-feasibility-usability.md`](radar-ad-feasibility-usability.md)
- OS and demographic patterning of missingness: [`beiwe-missing-data-sociodemographic.md`](beiwe-missing-data-sociodemographic.md), [`byod-demographic-imbalance.md`](byod-demographic-imbalance.md)

## Sources

1. Hackett K, Xu S, McKniff M, Paglia L, Barnett I, Giovannetti T. *JMIR Human Factors* 2024;11:e59974. DOI 10.2196/59974. PMC11624463. Full text read from the Europe PMC XML, 2026-10-31. Establishes the deployment, retention, completeness and troubleshooting figures.
2. Calvert E, Hackett K, Torous J, Giovannetti T. *International Psychogeriatrics* 2026;38(2):100123. DOI 10.1016/j.inpsyc.2025.100123. PMC13142898. Full text read from the Europe PMC XML, 2026-10-31. Establishes training time, nightly survey completion and the usability ratings.
