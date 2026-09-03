# Truslow et al. 2024 - Apple Heart & Movement Study, first-year retention and engagement in an 82,809-person Apple Watch cohort

## Quick Facts

| Field | Details |
|---|---|
| Citation | Truslow J, Spillane A, Lin H, Cyr K, Ullal A, Arnold E, Huang R, Rhodes L, Block J, Stark J, Kretlow J, Beatty AL, Werdich A, Bankar D, Bianchi M, Shapiro I, Villalpando J, Ravindran S, Mance I, Phillips A, Earl J, Deo RC, Desai SA, MacRae CA. "Understanding activity and physiology at scale: The Apple Heart & Movement Study." *npj Digital Medicine* 2024;7:242. DOI [10.1038/s41746-024-01187-5](https://doi.org/10.1038/s41746-024-01187-5). PMID 39256546 / PMC11387614. Brief communication, published 2024-09-10. |
| Study design | App-based longitudinal cohort, site-less, ongoing. Enrolment opened 2019-11-14 with a target of up to 500,000 and a planned duration of five years. This paper describes design and first-year data for everyone who enrolled in year one. ClinicalTrials.gov NCT04198194. Advarra IRB. |
| Sample size (enrolled / analyzed) | 82,809 in the analysed cohort after three exclusions (29 QA test accounts, 100 with eligibility that became ambiguous, 1,751 who never submitted the Demographics survey). The pre-exclusion total is not stated. |
| Population | US residents aged 18 or over who own an iPhone and a paired Apple Watch (Series 1 or later). 72% White, 74% male at birth, mean age 39.3 (SD 13.1), 62% college graduates, 80% employed. Self-enrolled through Apple's Research app after outreach by Apple, the American Heart Association and Brigham and Women's Hospital. |
| Duration | Each participant observed for at least one year and at most two (enrolled 2019-11-14 to 2020-11-13, observed to 2021-11-13). |
| Devices/platforms used | Participant-owned [Apple Watch and iPhone](../../module-01-wearables/profiles/apple-watch-healthkit.md) through Apple's Research app. HealthKit samples, watch and phone sensor data (including SensorKit streams), 16 in-app surveys, optional FHIR clinical records. No third-party phenotyping platform. |
| Funding/COI | All authors are Apple employees or partially funded by Apple through the American Heart Association. Apple is sponsor, device manufacturer and data custodian. No participant compensation. Data are not publicly available. |
| Last verified | 2026-09-03 |

## Summary

The largest Apple Watch research deployment in this module and one of two large BYOD cohorts here alongside [Presby 2025](whoop-mental-health-survey-engagement.md). It is included for the retention and engagement figures, which are unusually explicit for a cohort paper, and for the way the authors separate formal withdrawal from going quiet.

Formal withdrawal was rare. 2,684 participants (3.24%) withdrew within a year. Of those, a quarter left inside 13 days and half within 111 days. Fewer than 1% of withdrawals were automatic eligibility removals.

Going quiet was common. By day 365, 38% of the cohort had not uploaded anything from the Research app on that day, and 44% had not shared a Stand Hour sample (the paper's proxy for wearing the watch). The authors then ask a sharper question. Of those quiet participants, how many had stopped for good? 28% of the cohort had permanently stopped uploading by one year, and 34% had permanently stopped sharing Stand Hours. The gap between the daily figure and the permanent figure is small, so the authors conclude that the decline is mostly people leaving permanently rather than active people contributing less.

Surveys fell faster than the passive stream. The monthly Stress Scale went from a 69.55% response rate at the first delivery to 32.48% after a year. The quarterly Changes in Health survey went from 60.69% to 34.06%. The authors say the survey-based loss-to-follow-up estimate is higher than their other retention measures and that survey length and cadence had not yet been optimised.

## Instrumentation and Deployment Model

Bring your own device. Eligibility required an iPhone with the Research app installed, an Apple Watch paired at the time of enrolment, English, US residence and a unique iCloud account. Age minimums were 18, or 19 in Alabama and Nebraska, or 21 in Puerto Rico. The app checked watch pairing before letting a person proceed to consent.

Participants can opt in or out of sharing each data type at any time from inside the app, and the study cannot directly see when they do. That matters for the Stand Hour measure. A missing Stand Hour sample can mean no watch on the wrist, a broken upload path, or a participant who switched that sample type off. The authors state all three and say their data suggest the third is unusual.

Survey burden was stated up front. About 30 minutes in the first month and about 10 minutes a month thereafter. Each survey expires 28 days after delivery except Demographics, which never expires. Five surveys are triggered only by watch-detected events (potential falls, irregular rhythm notifications, ECG results).

Identifiable data are held only by Brigham and Women's Hospital staff. Apple sees coded data. A separate workflow lets hospital staff phone participants who consent to follow-up after a triggered survey.

## Recruitment and Retention

Recruitment ran through study websites hosted by Apple, the AHA and the hospital, plus AHA social media and email campaigns from October 2020. An in-app update channel was added the same month to encourage continued participation. The number of app installs, screen failures or consent refusals is not reported. The funnel in the paper starts at consent.

| Stage | n |
|---|---|
| Enrolled in year one, before exclusions | not stated |
| Excluded: QA test accounts | 29 |
| Excluded: eligibility became ambiguous after enrolment | 100 |
| Excluded: never submitted the Demographics survey | 1,751 |
| Analysed cohort | 82,809 |
| Withdrew within one year | 2,684 (3.24%) |

The 1,751 who never completed Demographics were on average 3.2 years younger than the cohort (95% CI 2.58 to 3.79 years).

The cohort is skewed against the US population and the authors say so. 74% male against 49%, 72% White against 60%, and 89% with more than 12 years of education against 62%. They also report that first-year dropout "skew[s] participation further in the direction of initial recruitment biases." Female recruitment was growing over time and female retention is described as high, without a figure.

Two participation indices are tracked daily over the first year, with the full 82,809 as denominator throughout.

| Index | Not participating on day 0 | Not participating on day 365 | Permanently stopped by day 365 |
|---|---|---|---|
| Any Research app upload | about 1% | about 38% | 28% |
| Stand Hour sample shared (watch-wear proxy) | 5% | 44% | 34% |

## Data Completeness and Technical Issues

The paper is a design and baseline description, and technical failures are not itemised. What it does report is which streams arrived and from what share of the cohort.

In a representative week two years after launch (2021-11-07 to 2021-11-13, chosen after a Mahalanobis test against 145 other weeks), step count, heart rate and stand hours were shared by about half the cohort. 30.6% shared at least one logged workout that week, averaging 6.54 workouts each. Mindfulness sessions were shared by 5.5% and third-party blood glucose by 1.1%.

ECG participation was high among those with a capable watch. 66,752 (80.6%) had an ECG-capable Series 4, 5 or 6 for at least a day in year one, and 55,740 of them (83.5%) recorded and shared at least one ECG, for 1,132,473 ECGs in total. 2.2% of ECGs were classified as atrial fibrillation, from 1,641 participants, and 29.1% of those participants had already reported known atrial fibrillation.

Clinical-record sharing was the weakest stream. About 10% of participants could share FHIR records, which the authors attribute to local FHIR compliance and the sign-in process. 8,408 shared at least one record in the observation window and 7,757 did so within their first year.

Triggered follow-up shows the cost of human contact at this scale. 2,055 survey responses from 1,735 participants met protocol criteria for a phone call. 1,179 participants consented to be called. Staff reached 829 of them, or 48% of participants with an eligible survey.

The Limitations section lists the missing-data problems the authors expect but have not yet measured. Timing of data loss around phone upgrades, what participation looked like before a person dropped out, frequency of contact, survey length, and prior survey completion. None is quantified in this paper.

No iOS version, watch model or OS effect on completeness is reported beyond the ECG-capability split.

## Feasibility Findings

The authors' own conclusions are about what the design makes possible. Passive collection over time of validated reference biometrics, an app that can be modified quickly with IRB approval, participant-generated annotation of workouts, and consented access to clinical records and claims. They describe survey engagement as "considerably improved from prior studies of serial health questionnaires" without naming a comparator.

They state two operational lessons directly. Survey-based loss to follow-up overstates attrition relative to passive measures, and dropout in year one made the cohort less representative than it was at enrolment, so representativeness needs quantitative recruitment and retention strategies rather than scale alone.

## Relevance to Future Study Design

Report withdrawal, daily non-participation and permanent inactivity as three separate numbers. Here they are 3.2%, 38% and 28% at one year, and any one of them alone would give a different impression of retention. The permanent-inactivity curve is the most useful of the three and the least often reported elsewhere in this module.

Half of all formal withdrawals happened in the first 111 days and a quarter in the first 13. If a study can only afford one retention intervention, the evidence here puts it early.

A watch-wear proxy built on a passively generated sample type is cheap and nearly complete, but it cannot distinguish non-wear from a participant switching that stream off. Choose a proxy the participant cannot silently disable, or accept that ambiguity and say so.

A survey response rate in the 30s after a year is what an uncompensated, low-touch, iPhone-only cohort delivers, even with in-app delivery and 10 minutes a month of stated burden. Compare [Presby 2025](whoop-mental-health-survey-engagement.md), where a monthly two-item survey in a consumer app produced 1.84 responses per person in 13 months.

Every BYOD cohort in this module inherits the product's customers. This one is three quarters male and nearly three quarters White, and dropout made it more so. That is the same mechanism as [Cho 2022](byod-demographic-imbalance.md) and [Presby 2025](whoop-mental-health-survey-engagement.md), now at 82,809 people.

## Evidence Confidence

Verified. The exclusion counts and the 82,809 figure, the withdrawal count, share and timing, both participation indices at day 0 and day 365 including the permanent-inactivity figures, the survey participation table and the two response-rate trajectories, the ECG and FHIR figures, the follow-up call funnel, the demographic comparison against US figures, the stated survey burden, and the competing-interests statement were all read from the published PDF (npj Digital Medicine, CC BY 4.0) on 2026-09-03.

Reported. The Stand Hour figures are read from the text's description of Figure 1 rather than from the figure itself. The paper's text gives them as approximate values ("around 38%," "around 1%") and this profile keeps that wording.

Not assessed here. The physiological content, the ECG classification performance and the activity findings belong to Module 1's [Apple Watch profile](../../module-01-wearables/profiles/apple-watch-healthkit.md). Whether the Apple Research app is a platform other researchers can use is answered there too, and the answer is no.

Conflict note. Every author is employed or funded by the sponsor, which also makes the device and holds the data. The retention figures reported are not flattering, which is the main reason they are treated as Verified rather than discounted.

## Key Links

- Paper (OA, CC BY 4.0): https://doi.org/10.1038/s41746-024-01187-5
- Europe PMC: https://europepmc.org/article/PMC/PMC11387614
- Registration: https://clinicaltrials.gov/study/NCT04198194
- Local PDF: `../../module-01-wearables/literature/apple-watch/2024-truslow-npjdigitalmedicine-heart-movement-study-scale.pdf` (already held by Module 1; not duplicated)

## Related profiles

- Device: [Apple Watch / HealthKit](../../module-01-wearables/profiles/apple-watch-healthkit.md)
- The other Apple site-less cohort, on data management: [`apple-heart-data-management-lessons.md`](apple-heart-data-management-lessons.md)
- Consumer-cohort representativeness: [`byod-demographic-imbalance.md`](byod-demographic-imbalance.md), [`allofus-fitbit-step-counts.md`](allofus-fitbit-step-counts.md), [`whoop-mental-health-survey-engagement.md`](whoop-mental-health-survey-engagement.md)
- Multi-device Apple Watch deployment: [`connect-multi-wearable-psychosis.md`](connect-multi-wearable-psychosis.md)
- Passive outlasting active: [`oura-tempredict-healthcare-worker-adherence.md`](oura-tempredict-healthcare-worker-adherence.md), [`beiwe-adolescent-feasibility.md`](beiwe-adolescent-feasibility.md)

## Sources

1. Truslow J, Spillane A, Lin H, et al. *npj Digital Medicine* 2024;7:242. DOI 10.1038/s41746-024-01187-5. Full text, Tables 1 to 7 and the descriptions of Figures 1 and 2 read from the published PDF, 2026-09-03. Establishes every figure in this profile.
