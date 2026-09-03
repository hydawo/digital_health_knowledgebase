# Mahalingaiah et al. 2022 - Apple Women's Health Study, six-month retention in the first 10,000 iPhone enrollees

## Quick Facts

| Field | Details |
|---|---|
| Citation | Mahalingaiah S, Fruh V, Rodriguez E, Konanki SC, Onnela JP, de Figueiredo Veiga A, Lyons G, Ahmed R, Li H, Gallagher N, Jukic AMZ, Ferguson KK, Baird DD, Wilcox AJ, Curry CL, Suharwardy S, Fischer-Colbrie T, Agrawal G, Coull BA, Hauser R, Williams MA. "Design and methods of the Apple Women's Health Study: a digital longitudinal cohort study." *American Journal of Obstetrics and Gynecology* 2022;226(4):545.e1-545.e29. DOI [10.1016/j.ajog.2021.09.041](https://doi.org/10.1016/j.ajog.2021.09.041). PMC10518829 (NIH author manuscript). |
| Study design | App-based longitudinal cohort, site-less, ongoing. Design paper with six months of follow-up results for the first 10,000 enrollees. Planned duration ten years to November 2029, target 500,000. ClinicalTrials.gov NCT04196595. Advarra IRB PRO00037562. |
| Sample size (enrolled / analyzed) | 11,113 clicked through to the study, 10,459 consented, 10,030 answered the demographics survey. The first 10,000 demographics responders are analysed. 11 formally withdrew in their first month. |
| Population | US iPhone users who have menstruated at least once, aged 18 or over (19 in Alabama and Nebraska, 21 in Puerto Rico), English speaking, sole user of their iCloud account. Mean age 33.6 (SD 10.3). 69.1% White non-Hispanic, 12.0% Hispanic, 6.1% Black, 4.3% Asian. 51% college graduates or above. 72.2% used an Apple Watch. All US states and Puerto Rico. |
| Duration | Enrolled 2019-11-14 to 2020-05-20, each with at least six months of follow-up. Monthly surveys through November 2020. |
| Devices/platforms used | Participant-owned iPhone (6s or later, iOS 13.2 or later) with an optional participant-owned [Apple Watch](../../module-01-wearables/profiles/apple-watch-healthkit.md), through the Apple Research app. HealthKit menstrual tracking, SensorKit heart-rate and location streams by separate opt-in, monthly in-app surveys. No third-party phenotyping platform. |
| Funding/COI | Funded by Apple Inc, which "had no role in the analysis and interpretation of data." Three authors are Apple Health employees who own Apple stock. Onnela is a cofounder of a commercial digital-phenotyping entity and received an unrestricted gift from Mindstrong Health in 2018. Four authors are supported by NIEHS intramural funds. No participant compensation. |
| Last verified | 2026-09-03 |

## Summary

The sister cohort to [Truslow 2024](apple-heart-movement-study-retention.md). The two studies launched on the same day inside the same Apple Research app, share a demographics survey and an eligibility template, and pay nobody. This one is included for a six-survey response curve with explicit denominators, a passive HealthKit measure of participation that the authors set against it, and a stated funnel from download to demographics.

The survey curve falls fast and then flattens. The first monthly menstrual update survey drew 62.2% of eligible participants. By the sixth it drew 34.5%. Two thirds of the cohort (65.2%) answered at least one of the six. The authors' own summary is that 38% of eligible participants never responded to the monthly survey at all after enrolling.

The passive measure held up better. 82.7% of the cohort had ever logged a bleeding event in HealthKit, and 72.4% logged at least one within the six months of follow-up. Among the people who did answer the sixth survey, 95.1% had HealthKit tracking data. The authors draw the design conclusion directly. Loss to follow-up measured by survey response "is higher than other retention metrics such as tracked menstrual bleeding events in HealthKit," and passive logging "will limit missingness and avoid reliance on survey responses."

Dropout was not neutral. Month-six responders were more often White (73.7% against 69.1% at baseline), more often college graduates, and more often Apple Watch users (82.5% against 72.2%).

## Instrumentation and Deployment Model

Bring your own device throughout. Eligibility was self-verified inside the Research app, consent was electronic, and participants were told they would be reconsented every two years. The consent form states there are "no incentives or compensation." The same app hosted the Apple Heart and Movement Study and the Apple Hearing Study, and Apple reviewed the survey drafts "to conform to their design standards across the 3 studies."

Three participation routes were defined. Survey responses, HealthKit data (menstrual logging from Apple's Cycle Tracking or any third-party app permitted to write to HealthKit), and SensorKit streams from the iPhone and paired watch (frequently visited locations with an anonymised identifier, watch-on-wrist state, optical sensor including heart rate). SensorKit required a separate opt-in and 24.4% gave it.

The monthly menstrual update survey has six questions, arrives on the first Sunday of each month from month two, and expires one week after delivery. The annual burden was split across the year to spread it out. Apple's usability testing estimated 25 minutes for enrolment and 5 minutes per monthly survey. Observed medians were 1.83 minutes for the demographics survey and 0.77 minutes for the monthly survey, which the authors call "considerably shorter than expected."

Identifiable data are restricted to the principal investigator's staff. Shared data sit in an Apple system "designed to meet the technical safeguard requirements" of HIPAA.

## Recruitment and Retention

Recruitment was general media coverage, a study website, a podcast, press interviews, and social media accounts created between March and August 2020 posting one to three times a week. The authors say recruitment "was generally not targeted to specific populations." Enrolment averaged 370 a week.

| Stage | n |
|---|---|
| Downloaded the Research app and clicked through to the study | 11,113 |
| Consented | 10,459 |
| Responded to the demographics survey | 10,030 |
| Analysed (first 10,000 demographics responders) | 10,000 |
| Formally withdrew within the first month | 11 |

The Discussion gives a slightly different framing of the same data. Of 10,502 who downloaded the app and were eligible, 96% enrolled and answered demographics. The 429 people who enrolled in the window but never answered demographics were more often from the South (40% against 35%), less often Apple Watch users (45% against 72%), and much less likely to have opted into SensorKit heart rate (5% against 24%).

The retention measure is the completion rate of the monthly menstrual update survey among those eligible to receive it. Eligibility excludes anyone who reported menopause or pregnancy at baseline or in an earlier month, and the 11 who withdrew. Consecutive responses were not required.

| Survey | Completed | Eligible | Rate |
|---|---|---|---|
| Baseline menstrual status | 9,751 | 10,000 | 97.5% |
| Month 1 | 5,748 | 9,238 | 62.2% |
| Month 2 | 4,413 | 9,145 | 48.3% |
| Month 3 | 3,902 | 9,091 | 42.9% |
| Month 4 | 3,752 | 9,045 | 41.5% |
| Month 5 | 3,437 | 9,008 | 38.2% |
| Month 6 | 3,099 | 8,972 | 34.5% |

Withdrawal reasons are not reported. Ineligibility accumulated to 1,028 by the sixth survey. The power calculation had assumed 20% loss to follow-up and a 90% to 95% incomplete-response rate over twelve cycles, so the design anticipated worse than it got.

## Data Completeness and Technical Issues

The passive stream is HealthKit menstrual logging, not sensor data, and it is reported against the survey stream on purpose.

| Measure | All 10,000 | Month-6 survey responders (3,099) |
|---|---|---|
| Tracked at least one cycle ever | 82.7% | 95.1% |
| Tracked at least one cycle within 3 months of enrolment | 70.6% | 89.5% |
| Tracked at least one cycle within 6 months of enrolment | 72.4% | 91.4% |
| Mean calendar months tracked within 6 months, among trackers | 4.44 (25th to 75th percentile 3 to 6) | 5.29 (5 to 6) |
| SensorKit heart-rate opt-in | 24.4% | 31.2% |

A calendar month counts as tracked if a logged bleeding event falls in it, so the six-month maximum is seven.

No technical failure modes are reported. Nothing on watch pairing, app crashes, sync or upload problems, and no watch wear statistics even though watch-on-wrist state is collected. The only design constraint stated is that the monthly survey expires after one week and that responses before four weeks of enrolment are not counted.

Missing-data handling is deferred. The authors say "further evaluation of the data must be conducted to understand whether nonrandom dropout may bias the longitudinal effect estimates."

## Feasibility Findings

The authors report four principal findings, two of which are operational. Non-White participants were slightly more likely to drop out over six months, and the enrolled cohort's racial and ethnic distribution was close to the US population at baseline. The other two are that the cohort spans every state and that most participants were college educated, employed and Apple Watch users.

Their stated retention response is "education, communication, and engagement through a study update feature within the app and on the study website." They add that "engagement strategies may be constructed to limit the loss to follow-up of certain subpopulations." No figures are given for the effect of any of this.

## Relevance to Future Study Design

Expect a monthly survey in an uncompensated consumer-app cohort to lose roughly half its respondents by month two and settle near a third by month six. Here the survey took under a minute. Burden was not the problem.

Build the primary outcome onto a passive stream the participant already maintains. Menstrual logging in HealthKit reached 72.4% of the cohort in six months against 34.5% for the survey, and 95% of survey responders also had it. A study that needs the survey is a study of the third who keep answering.

Report who stays, not only how many. The six-month responders here were whiter, better educated and more often watch owners than the people who enrolled. A representative baseline does not stay representative without work, and [Truslow 2024](apple-heart-movement-study-retention.md) reached the same conclusion in the sibling cohort.

Check the estimated burden against the observed one. Apple's 25-minute enrolment estimate became a 1.83-minute median. Over-estimating burden in a consent form is harmless. Under-estimating retention loss, as the 20% planning figure did here, is not.

## Evidence Confidence

Verified. The download, consent and demographics funnel, the 11 withdrawals, the six monthly completion counts and denominators, the HealthKit tracking percentages for the full cohort and the month-six responders, the SensorKit opt-in rates, the survey completion times, the demographic shifts between baseline and month six, the no-compensation statement, and the funding and conflict statements were all read from the NIH author manuscript (PMC10518829) on 2026-09-03.

Not assessed here. Whether Apple Watch or SensorKit data were complete, and anything about sensor validity, belongs to Module 1's [Apple Watch profile](../../module-01-wearables/profiles/apple-watch-healthkit.md). The Research app is Apple's own study platform and is not available to other researchers, which that profile records.

Conflict note. The sponsor makes the phone, the watch and the app, funded the study and employs three authors. The retention figures reported are not flattering to the survey stream, which is the main reason they are treated as Verified rather than discounted.

## Key Links

- Paper (author manuscript, CC BY-NC-ND): https://doi.org/10.1016/j.ajog.2021.09.041
- Europe PMC: https://europepmc.org/article/PMC/PMC10518829
- Registration: https://clinicaltrials.gov/study/NCT04196595
- Local PDF: `../../module-01-wearables/literature/apple-watch/2022-mahalingaiah-ajog-apple-womens-health-study-design.pdf` (already held by Module 1; not duplicated)

## Related profiles

- Device: [Apple Watch / HealthKit](../../module-01-wearables/profiles/apple-watch-healthkit.md)
- Sister cohort in the same app: [`apple-heart-movement-study-retention.md`](apple-heart-movement-study-retention.md)
- The other Apple site-less study: [`apple-heart-data-management-lessons.md`](apple-heart-data-management-lessons.md)
- Consumer-cohort representativeness: [`byod-demographic-imbalance.md`](byod-demographic-imbalance.md), [`allofus-fitbit-step-counts.md`](allofus-fitbit-step-counts.md)
- Passive outlasting active: [`oura-tempredict-healthcare-worker-adherence.md`](oura-tempredict-healthcare-worker-adherence.md), [`whoop-mental-health-survey-engagement.md`](whoop-mental-health-survey-engagement.md)

## Sources

1. Mahalingaiah S, Fruh V, Rodriguez E, et al. *Am J Obstet Gynecol* 2022;226(4):545.e1-545.e29. DOI 10.1016/j.ajog.2021.09.041. Full text and Tables 1 to 4 read from the NIH author manuscript (PMC10518829), 2026-09-03. Establishes every figure in this profile.
