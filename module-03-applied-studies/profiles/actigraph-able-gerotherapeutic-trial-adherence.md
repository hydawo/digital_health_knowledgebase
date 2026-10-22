# Lu et al. 2026 - ActiGraph wGT3X-BT in the ABLE gerotherapeutic trial, Singapore, N=120

## Quick Facts

| Field | Details |
|---|---|
| Citation | Lu JK, Wang W, Chew YE, Guan L, Kennedy BK, Maier AB. "Optimizing accelerometer implementation in a gerotherapeutic trial: Feasibility, adherence, and operational insights of ABLE." *PLOS Digital Health* 2026;5(9):e0001691. DOI [10.1371/journal.pdig.0001691](https://doi.org/10.1371/journal.pdig.0001691). PMC13614584. ClinicalTrials.gov NCT05706389. |
| Study design | Exploratory analysis of operational data from a single-site, double-blind, randomised, placebo-controlled supplement trial (alpha-ketoglutarate, 1 g/day for 6 months). Device operations, wear adherence and dropout are the outcomes. Cox models with visit as the time scale. |
| Sample size (enrolled / analyzed) | 120 randomised (59 AKG, 61 placebo). 119 with accelerometer data, because one participant lost the device at baseline and then withdrew. Device data at each visit for 119, 110, 102 and 98. 20 dropped out (17%). |
| Population | Generally healthy, community-dwelling adults aged 40 to 60 in Singapore whose DNA methylation age was older than their chronological age. Mean age 51.1 (AKG) and 50.5 (placebo). 49.2% and 50.8% female. Mostly Chinese (86.4% and 91.8%). |
| Duration | 9 months per participant, with 7 days of wear after each of 4 visits (baseline, 3, 6 and 9 months). Enrolment 4 May 2023 to 19 December 2024. |
| Devices/platforms used | [ActiGraph](../../module-01-wearables/profiles/ametris-actigraph.md) wGT3X-BT (firmware 1.9.2), provisioned, non-dominant wrist, 30 Hz raw. Downloaded with ActiSync and processed in ActiGraph CentrePoint. Electronic activity diary. No phone platform. |
| Funding/COI | A gift from the Lien Foundation to BKK. The authors declare no competing interests. Participant compensation is not reported. |
| Last verified | 2026-10-22 |

## Summary

This is an operational report on a research-grade wrist accelerometer bolted onto a drug-style ageing trial. The trial question was whether a supplement lowers DNA methylation age. The accelerometer was a secondary instrument worn for one week after each of four visits. There were no reminders during wear and the device was returned by post.

Wear was very high. Median daily wear across all participant-days was 1400 minutes (IQR 1245 to 1440). At every visit at least 81% of each arm had 4 or more valid days of 16 hours. Device problems touched 8 of 432 participant-visits.

The finding the authors lead with is about dropout. Each extra minute of daily wear in the preceding week went with a lower hazard of missing the next visit (HR 0.998, 95% CI 0.997 to 0.999). Men were less likely to drop out than women (HR 0.208). Device wear tracked trial engagement rather than supplement adherence. Wear time showed no association with pill-count adherence.

## Instrumentation and Deployment Model

Provisioned. The device was handed over at each visit between 8 and 11 AM. Staff gave an in-person debrief at the end of the visit and a printed instruction sheet. Participants wore it continuously on the non-dominant wrist for 7 days. They removed it only for water activities.

The return path was postal. On day 8 participants mailed the device back in a prepaid, tracked, bubble-lined SingPost envelope. Staff then removed and washed the woven nylon strap with soap, a viral cleanser and a bacterial cleanser. The device body was wiped with alcohol.

Support ran through a WhatsApp chat and email. There were no reminder messages to encourage wear during monitoring. Device malfunctions could only be found after the device came back and was downloaded. The device has no buttons or display and runs about 25 days on a charge.

Participants logged exercise and device removals in an electronic diary. Where diary and accelerometer disagreed, the accelerometer's non-wear detection won. Staff estimated missing sleep and wake times from the movement trace and nearby diary days.

Processing used CentrePoint's wear-time validation. Non-wear was 90 or more consecutive minutes of zero vector-magnitude counts, allowing up to 2 minutes of non-zero counts. Idle sleep mode was on.

## Recruitment and Retention

Participants were recruited from residents of Singapore. Recruitment channels are not described in the text. The screening funnel is in the CONSORT diagram (Fig 1), which was not available as text, so screening numbers are not reported here.

Participants could refuse the device and stay in the trial. All 120 agreed to wear it at baseline.

Dropout was 20 of 120 (17%). It was defined as missing any follow-up visit after baseline or formally withdrawing. Reasons, recorded when offered voluntarily, were as follows.

| Reason | n |
|---|---|
| Work or schedule conflicts | 10 |
| Lost to follow-up or uncontactable | 4 |
| Study product issues | 2 |
| Protocol non-compliance or withdrawal of cooperation | 2 |
| Overall study burden | 1 |
| Medical reason unrelated to product | 1 |

Kaplan-Meier completion probability was about 83% in both arms (log-rank p=0.92). A reviewer had flagged an earlier version reporting 92% completion as inconsistent with the 17% figure. The published text reads about 83%.

## Data Completeness and Technical Issues

A valid day was at least 960 minutes of wear in 24 hours. A participant was adherent for a visit with at least 4 valid days of the 7 instructed days.

| Visit | n | Median wear, min/day (AKG / placebo) | Adherent, n (%) (AKG / placebo) |
|---|---|---|---|
| Baseline | 119 | 1440 / 1440 | 56 (97) / 55 (90) |
| 3 months | 110 | 1326 / 1323 | 43 (81) / 46 (81) |
| 6 months | 102 | 1440 / 1348 | 42 (82) / 45 (88) |
| 9 months | 98 | 1345 / 1321 | 41 (85) / 41 (82) |

Median wear was 1340 minutes on weekdays and 1440 on weekends (p<0.001, r=0.105). Wear was highest on days 2 to 6. Day-to-day coefficient of variation in wear ranged from 7.5% to 31.6% by arm and visit. 33 of 119 participants had a mean below 960 minutes at one or more visits.

Six participants reported device concerns across 8 participant-visits.
- One refused to wear it at the last three visits because it "looks like a prison tracker."
- Two devices were lost, one at baseline.
- One reported skin irritation and had the strap changed mid-wear.
- One reported a rash.
- One said the strap from a previous visit "became smelly when wet."

Hardware malfunction counts, data corruption, postal loss and firmware problems are not reported as separate figures. Whether either lost device went missing in the post is not stated.

## Feasibility Findings

The authors conclude that accelerometer integration "is feasible and can yield high-quality data" in middle-aged adults in a gerotherapeutic trial.

They name the mail-back step as the main data-loss risk, because data cannot be checked until the device returns. They suggest reminders, remotely syncing devices and immediate data retrieval. They recommend hypoallergenic straps and proactive strap replacement. They suggest that early wear compliance may flag later non-adherence, which would allow targeted support.

They read the sex effect as a hypothesis. Women may face more work, family and caregiving burden. The trial did not measure any of these.

## Relevance to Future Study Design

A 7-day mail-back protocol with no reminders produced median wear near 24 hours at every visit in this population. The population was healthy, motivated and enrolled in a supplement trial. It is not a clinical sample.

Wear time in the first monitoring week may be worth watching as an early dropout signal. The effect per minute is small, so its value as a practical screening tool is not established.

The device problems were social and dermatological, not electronic. Budget for spare straps and a cleaning step between visits.

Compensation is not reported. Neither is staff time per participant.

## Evidence Confidence

Verified for the device protocol, the valid-day and adherence definitions, every figure in Tables 2 to 5, the dropout reasons, the hazard ratios and the funding and competing-interest statements. All were read from the published PLOS PDF and the Europe PMC full-text XML (PMC13614584, CC BY 4.0) on 2026-10-22.

Reported for the screening funnel, which sits only in the CONSORT figure image and was not extracted.

The authors' link between wear and dropout is an association in an exploratory secondary analysis. They do not claim it is causal.

## Key Links

- Paper (OA, CC BY 4.0): https://doi.org/10.1371/journal.pdig.0001691
- Europe PMC: https://europepmc.org/article/PMC/PMC13614584
- Trial registration: https://clinicaltrials.gov/study/NCT05706389
- Local PDF: `../literature/2026-lu-plosdigithealth-accelerometer-implementation-gerotherapeutic-trial-able.pdf`

## Related profiles

- Device: [Ametris (ActiGraph)](../../module-01-wearables/profiles/ametris-actigraph.md)
- Other ActiGraph deployments in this module: [`actigraph-als-upper-limb-wear-time.md`](actigraph-als-upper-limb-wear-time.md), [`beiwe-actigraph-modus-als-progression.md`](beiwe-actigraph-modus-als-progression.md)
- Provisioned research-grade wrist device with periodic swaps: [`geneactiv-beiwe-college-year-deep-phenotyping.md`](geneactiv-beiwe-college-year-deep-phenotyping.md)
- Wear or engagement predicting retention: [`radar-mdd-longterm-engagement.md`](radar-mdd-longterm-engagement.md)

## Sources

1. Lu JK, Wang W, Chew YE, Guan L, Kennedy BK, Maier AB. *PLOS Digit Health* 2026;5(9):e0001691. DOI 10.1371/journal.pdig.0001691. PMC13614584. Full text, Tables 1 to 5 and the published peer-review history read from the PLOS PDF and Europe PMC XML, 2026-10-22. Establishes every figure in this profile.
