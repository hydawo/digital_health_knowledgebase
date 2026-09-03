# Vidal Bustamante et al. 2022 - GENEActiv wrist actigraphy plus Beiwe daily surveys across a full academic year in first-year students, N=49

## Quick Facts

| Field | Details |
|---|---|
| Citation | Vidal Bustamante CM, Coombs G 3rd, Rahimi-Eichi H, Mair P, Onnela JP, Baker JT, Buckner RL. "Fluctuations in behavior and affect in college students measured using deep phenotyping." *Scientific Reports* 2022;12:1932. DOI [10.1038/s41598-022-05331-7](https://doi.org/10.1038/s41598-022-05331-7). PMID 35121741. PMCID PMC8816914 (not printed in the PDF). Co-first authors Vidal Bustamante and Coombs. Second source on the same deployment: Vidal Bustamante CM, Coombs G III, Rahimi-Eichi H, Mair P, Onnela JP, Baker JT, Buckner RL. "Precision Assessment of Real-World Associations Between Stress and Sleep Duration Using Actigraphy Data Collected Continuously for an Academic Year: Individual-Level Modeling Study." *JMIR Formative Research* 2024;8:e53441. DOI [10.2196/53441](https://doi.org/10.2196/53441). PMCID PMC11094608 (not printed in the PDF). |
| Study design | Intensive longitudinal observational study over one full academic year and a few days of summer, with a fully remote 13-week follow-up two years later during the COVID-19 shutdown. Harvard IRB16-1230. The 2024 paper adds a 6-person pilot group of sophomores enrolled concurrently. |
| Sample size (enrolled / analyzed) | 68 enrolled. 19 excluded for data-acquisition reasons. 49 analysed. 43 of the 49 re-enrolled in the follow-up. |
| Population | First-year students living on campus at Harvard. Ages 18 to 19, mean 18.06. 25 women, 24 men. 63% White, 14% Black, 10% Asian, 4% American Indian, 4% mixed race. 12% reported a prior psychiatric diagnosis. 46 (94%) iPhone users, 3 (6%) Android. |
| Duration | 256 days from the first day of the Fall semester to the last day of Spring, including a five-week Winter Break. Actigraphy ran throughout. The follow-up ran 94 days from the week after Spring Break 2020. |
| Devices/platforms used | [GENEActiv Original](../../module-01-wearables/profiles/axivity-geneactiv.md) wristband, researcher-provisioned, worn continuously on the non-dominant wrist. [Beiwe](../../module-02-digital-phenotyping/profiles/beiwe.md) on participants' own phones, used for the nightly 46-item survey and a voice diary only. No passive smartphone sensing is reported. REDCap for the three questionnaire batteries. DPSleep pipeline for sleep detection. |
| Funding/COI | Gift from Kent and Liz Dauten, NIMH U01MH116925 and DP2MH103909, NIH T90DA022759, the Sackler Scholar Programme, and the Harvard Foundations of Human Behavior Initiative. Onnela, Beiwe's originator, is a co-author and declares being a cofounder and board member of a commercial digital-phenotyping entity (named "Beiwe" in the 2022 paper and "Phebe Health" in the 2024 paper). Baker declares Verily and Mindstrong fees and Mindstrong equity. Buckner declares Pfizer, Roche, Alkermes and Cognito fees in the 2024 paper. Participants were paid, with amounts given in the 2024 paper. |
| Last verified | 2026-09-03 |

## Summary

This is the only Module 3 deployment of a GENEActiv or Axivity logger, and the longest continuous wrist-actigraphy protocol on healthy young adults in the module. The research question is about affect and behaviour across the academic calendar. The profile is here for the operational model that made a year of continuous raw accelerometry possible with a device that has no cloud, no sync and no adherence view during wear.

That model is a swap cadence. Participants met study staff in person every 3 to 4 weeks and exchanged their wristband for a fully charged one with reset memory. Over the five-week Winter Break, when no swap was possible, the sampling rate was dropped from 30 Hz to 10 Hz to make battery and memory last. The 2022 paper reports 132 to 249 days of usable actigraphy per person (mean 220, median 227) out of 256, and 98 to 255 on-time daily surveys per person (mean 202, median 216).

The 68-to-49 funnel is worth copying. Seven withdrew early. One wristband failed. Two produced poor-quality actigraphy. Nine submitted too few surveys. The last of those criteria is worded differently in the two papers, which is recorded below. Two years later, 43 of the 49 (88%) re-enrolled in a remote follow-up during the pandemic.

## Instrumentation and Deployment Model

The wearable was provisioned and the phone was not. Eligibility required full-time enrolment and an iPhone or Android phone that could run the Beiwe app. The paper does not say whether any student was turned away for phone incompatibility. Consent was taken in person after an interested student scheduled a session.

The wristband protocol had four elements. Wear on the non-dominant wrist at all times, including sleep and bathing. Press the device button when trying to fall asleep and again on waking, to give the sleep pipeline a manual marker. Sample at 30 Hz on campus and 10 Hz over Winter Break. Exchange the device at every in-person check-in, every 3 to 4 weeks. The papers do not report the battery life achieved per cycle, the number of swaps per person, or whether any swap was missed.

Sleep was estimated by the group's own open-source DPSleep pipeline. It converts raw acceleration to minute-level activity, removes non-wear minutes using tri-axial variance, and finds the main sleep episode with a sliding window. A day is marked unusable if either boundary of the sleep episode cannot be detected because of missing data. Two trained raters checked every automatically detected sleep episode against the activity trace and the button presses, adjusted times and labels where needed, and took disagreements to the research team. The size of that manual effort for roughly 10,000 person-days is not reported, though four people are credited with actigraphy quality control in the acknowledgements.

Beiwe delivered the nightly 46-item survey. The 2022 paper says "payment structures and phone notifications were designed for participant compliance and retention." The notification schedule is not described. The voice-recorded diary collected through Beiwe is not analysed in either paper. Both papers credit one person for Beiwe support in the acknowledgements. No app, notification, upload or phone-related problem is reported anywhere in either text.

The 2024 paper describes storage. Data from all devices were imported automatically into a secure data warehouse. Each participant was labelled with a random ID and identifying information was kept in a locked cabinet and a password-protected database.

Compensation is spelled out in the 2024 paper. US $1 per daily survey submitted. US $1 per day of continuous wristband wear. US $20 per hour for web surveys and in-person visits. A US $100 bonus at the half-way point and US $300 on completing the full study. The 2022 paper gives the same structure without amounts. The follow-up paid US $10 per biweekly survey, US $1 per daily survey, and a completion bonus "scaled to reward few missed surveys."

### Timing relative to Beiwe's heartbeat feature

The students were in their third college year in March 2020, so the year-long deployment took place before 2020. It therefore predates the heartbeat mechanism added to Beiwe in 2024, described in [`beiwe-als-adherence.md`](beiwe-als-adherence.md). Because Beiwe here carried surveys rather than background sensors, the feature would have mattered less than in the passive-sensing Beiwe deployments elsewhere in this module.

## Recruitment and Retention

Recruitment used flyers on campus boards and email lists in the first two weeks of the Fall semester. The number of students who saw the advert, enquired, or were screened is not reported. Psychiatric diagnosis and medication were not exclusion criteria, and the 2024 paper adds that starting treatment during the study did not lead to exclusion.

| Stage | n |
|---|---|
| Enrolled | 68 |
| Withdrew early | 7 |
| Technical failure of actigraphy data | 1 |
| Poor-quality actigraphy data | 2 |
| Too few daily surveys | 9 |
| Analysed | 49 |
| Re-enrolled in the 2020 remote follow-up | 43 (88%) |

The 2024 paper states the 19 exclusions as 28% of those enrolled. No reason is given for any of the seven early withdrawals, and their timing is not reported. Whether the nine low-survey participants were still wearing the wristband is not reported.

The two papers describe the ninth exclusion criterion differently. The 2022 Methods say "completion of < 100 daily surveys across the data collection period (n = 9)." The 2024 Methods say "completion of <50% of the daily surveys (n=9, 47%)." Both papers then state the analysis-inclusion rule as at least 100 on-time daily surveys. One hundred surveys is fewer than half of a 256-day window, so the two wordings are not the same threshold, though they describe the same nine people. This profile takes the 100-survey rule as operative because both papers use it for inclusion.

Follow-up retention was reported by cluster. Each of the three first-year clusters retained more than 82%. The six who did not return were one from Cluster A (12 members), three from Cluster B (17) and two from Cluster C (20), and they "declined to participate or did not respond to our contacts." Three of the 43 provided only the biweekly REDCap surveys and no daily Beiwe surveys.

## Data Completeness and Technical Issues

The 2022 paper reports completeness as available observations per participant in Table 1.

| Stream | Range | Mean | Median | Between-person SD |
|---|---|---|---|---|
| Daily actigraphy (of 256 days) | 132 to 249 | 220 | 227 | 24.44 |
| Daily survey, on time (of 256 days) | 98 to 255 | 202 | 216 | 47.32 |

A survey counted as on time if submitted between 5 PM local time on the day it opened and 6 AM the next morning. Later submissions were "discarded and marked as missing." The number discarded as late is not reported. The actigraphy stream is more complete and less variable across people than the survey stream, and the 2022 Discussion singles out "the daily phone-based surveys toward the last few months of the study" as where missingness concentrated. The figures show the daily proportion of missing survey observations, with days above 50% missing shaded, but the paper gives no numeric time course.

The 2024 paper reports a stricter count. A usable observation there is a school-semester day with both a usable sleep episode and an on-time survey, out of 223 possible. The 49 target participants had a median of 178 usable days (range 84 to 214). The six pilot participants had a median of 178 (range 119 to 212). The abstract gives the IQR across all 55 as 65.5.

The 2024 paper also tests whether missingness was informative. The count of usable observations was not correlated with a participant's mean sleep duration (r=0.09, P=.53) or mean stress (r=-0.11, P=.42). Mean sleep did not differ on days with and without survey data (P=.59). Mean stress did not differ on days with and without actigraphy (P=.70). The 2022 paper states that missingness in the daily assessments was not associated with global clinical scores, without figures.

Documented technical failures are few and specific. One enrolee was excluded for "technical failure of the actigraphy data" and two for "poor quality actigraphy data." Among the 49 analysed, participant T15 "had no usable actigraphy data over the full spring semester due to a technical issue with their wristband." T15 was retained with 98 usable days, and the 2024 authors flag T15's one anomalous model result as a likely artefact of that structured gap. They state that "no other participant in the target sample showed this kind of systematic missingness in either the actigraphy or survey data streams." What the wristband issue was, and why it was not caught at a swap, is not reported.

Wear time is handled by the pipeline rather than by a threshold. Non-wear minutes are removed and a day is dropped if the sleep episode has no detectable boundary. No hours-per-day wear criterion and no per-person wear-hour figures are reported. No sync or upload problem can arise on a GENEActiv because the device logs to internal memory and is read by USB after each swap. No breakdown by phone operating system is given, and with 46 of 49 on iPhone one would not be informative.

## Feasibility Findings

The 2022 authors conclude that the structure in the data "validate the use of digital phenotyping tools to capture a wide range of behavioral metrics relevant to student life over extended periods of time." They then state the limitation directly. "Most enrolled participants were highly compliant, but there were non-trivial amounts of missing data, especially among the daily phone-based surveys toward the last few months of the study." They add that "future work should explore additional strategies" beyond payment and notifications.

The 2024 paper turns this into advice. "Long study periods require extra vigilance to ensure that participants remain compliant over time." Quality checks should confirm that the data show expected real-world structure, such as the semester-versus-break and weekday-versus-weekend differences seen here. They also note that ample data and high compliance are not enough when a participant's metric barely varies, giving a participant with consistently low stress as the example.

Both papers say the sample is small and drawn from one elite US campus, and "might not be representative of all first-year college students."

## Relevance to Future Study Design

A screenless logger can run for an academic year if the team is willing to see every participant every 3 to 4 weeks. That contact is the adherence mechanism, the charging mechanism and the data-retrieval mechanism at once. Budget for the visits, and for the day-per-participant payment that accompanied them here.

Plan the gap. The one period without swaps was handled by halving the sampling rate and more. A team using a GENEActiv or Axivity device over a holiday, a field placement or a long postal cycle should decide the rate in advance, because the change alters what can be derived from the raw signal afterwards.

The wearable failed once in 49 people over a semester and was not noticed until the data were processed. A logger gives no adherence view during wear, so a failure at the start of a cycle costs the whole cycle. The check-in is the only place to catch it, and this study did not report checking data at swaps.

The survey stream, not the wearable, is where completeness eroded. Actigraphy averaged 220 of 256 days and surveys 202, with twice the spread across people. The nine exclusions for low survey count outnumber the three for actigraphy. That is the same passive-outlasts-active pattern seen in [`oura-tempredict-healthcare-worker-adherence.md`](oura-tempredict-healthcare-worker-adherence.md) and [`apple-heart-movement-study-retention.md`](apple-heart-movement-study-retention.md), here with a device that cannot be forgotten to sync.

State the survey window and the exclusion rule in a form that survives to the next paper. Here the same nine people are described as under 100 surveys in one paper and under 50% in the other.

Two-rater manual review of every sleep episode is the price of the clean sleep series. A team without the staff for that should not expect the same usable-day counts from DPSleep or any other pipeline on its own.

## Evidence Confidence

Verified. The 68-to-49 funnel and its four categories, the 3-to-4-week swap cadence, the 30 Hz and 10 Hz rates, the on-time survey window, the 100-survey inclusion rule, the per-stream observation counts in Table 1, the three cluster sizes, the 43-of-49 follow-up re-enrolment and its cluster breakdown, the follow-up duration and payments, the funding statement and the competing-interests statement were read from the 2022 paper's published PDF (Scientific Reports, CC BY 4.0) on 2026-09-03. The compensation amounts, the IRB number, the 223-day usable-observation counts, the missingness-mechanism tests, the T15 wristband failure, the storage description and the 2024 conflict statement were read from the 2024 paper's published PDF (JMIR Formative Research, CC BY 4.0) on the same date.

Reported. The daily survey missingness time course exists only as a figure panel in the 2022 paper and is described here in words.

Not assessed here. The affect and stress findings, the three-cluster solution, the hidden Markov and individual-level models, and the stress-sleep associations are the papers' scientific content and are not deployment findings. DPSleep's accuracy against reference sleep measures belongs with Module 1's [GENEActiv profile](../../module-01-wearables/profiles/axivity-geneactiv.md).

Possible cohort overlap. [`beiwe-missing-data-sociodemographic.md`](beiwe-missing-data-sociodemographic.md) pools six Beiwe studies from 2015 to 2018, four of them healthy Harvard undergraduates, with Buckner, Baker and Coombs among the authors. Neither Vidal Bustamante paper cites that meta-study and neither reports passive smartphone sensing, whereas the meta-study analysed accelerometer and GPS metadata. Whether the same students appear in both cannot be determined from the texts.

Conflict note. Onnela, who built Beiwe, is a co-author, and the platform is a survey vehicle here rather than the object of study. The papers report the survey stream as the weaker of the two, which runs against any incentive to flatter the platform. The GENEActiv vendor has no declared role.

## Key Links

- 2022 paper (OA, CC BY 4.0): https://doi.org/10.1038/s41598-022-05331-7
- 2022 Europe PMC: https://europepmc.org/article/PMC/PMC8816914
- 2024 paper (OA, CC BY 4.0): https://doi.org/10.2196/53441
- 2024 Europe PMC: https://europepmc.org/article/PMC/PMC11094608
- DPSleep pipeline paper: https://doi.org/10.2196/29849
- Local PDF (2022): `../../module-02-digital-phenotyping/literature/beiwe/2022-vidal-scientificreports-fluctuations-behavior-affect-college-students-measured.pdf` (already held by Module 2; not duplicated)
- Local PDF (2024): `../../module-02-digital-phenotyping/literature/beiwe/2024-vidal-jmirformativeres-precision-assessment-real-world-associations-between-stress.pdf` (already held by Module 2; not duplicated)

## Related profiles

- Device: [Axivity / GENEActiv](../../module-01-wearables/profiles/axivity-geneactiv.md)
- Survey platform: [Beiwe](../../module-02-digital-phenotyping/profiles/beiwe.md)
- Possible student-cohort overlap: [`beiwe-missing-data-sociodemographic.md`](beiwe-missing-data-sociodemographic.md)
- Other first-year student cohort with a wearable: [`oura-university-freshmen-sleep.md`](oura-university-freshmen-sleep.md)
- Other research-grade actigraph deployment: [`actigraph-als-upper-limb-wear-time.md`](actigraph-als-upper-limb-wear-time.md)
- Passive stream outlasting active stream: [`oura-tempredict-healthcare-worker-adherence.md`](oura-tempredict-healthcare-worker-adherence.md), [`apple-heart-movement-study-retention.md`](apple-heart-movement-study-retention.md), [`beiwe-adolescent-feasibility.md`](beiwe-adolescent-feasibility.md)
- Beiwe heartbeat timeline: [`beiwe-als-adherence.md`](beiwe-als-adherence.md)

## Sources

1. Vidal Bustamante CM, Coombs G 3rd, Rahimi-Eichi H, Mair P, Onnela JP, Baker JT, Buckner RL. *Scientific Reports* 2022;12:1932. DOI 10.1038/s41598-022-05331-7. Full text, Table 1, the Methods and the figure captions read from the published PDF, 2026-09-03. Establishes the funnel, the deployment protocol, the per-stream observation counts, the survey window, the follow-up re-enrolment and the funding and conflict statements.
2. Vidal Bustamante CM, Coombs G III, Rahimi-Eichi H, Mair P, Onnela JP, Baker JT, Buckner RL. *JMIR Formative Research* 2024;8:e53441. DOI 10.2196/53441. Full text and Table 1 read from the published PDF, 2026-09-03. Establishes the compensation amounts, the IRB number, the usable-observation counts, the missingness tests, the T15 wristband failure, the pilot group and the restated exclusion criterion.
