# Ghazi et al. 2026 - Withings BPM Connect Pro with pharmacist telehealth after emergency department discharge, pilot RCT, N=24

## Quick Facts

| Field | Details |
|---|---|
| Citation | Ghazi L, Gonzalez-Flores P, Green Vance E, Short QH, Mehta T, Hearld LR, Mahmood S, Neyra JA, Mugavero MJ. "Feasibility and acceptability of a remote blood pressure monitoring pharmacist-led telehealth programme in an emergency department transition care clinic: a pilot randomised controlled trial." *BMJ Open* 2026;16(10):e121681. DOI [10.1136/bmjopen-2026-121681](https://doi.org/10.1136/bmjopen-2026-121681). PMID 42914550 / PMC13691778. Published 2026-10-22. |
| Study design | Two-arm parallel-group pilot RCT, 1:1, permuted blocks of 2 and 4 in REDCap. Open-label. Recruitment, retention and fidelity are the primary outcomes. Blood pressure change is exploratory. ClinicalTrials.gov NCT06247111. |
| Sample size (enrolled / analyzed) | 27 assessed. 24 randomised (12 per arm). 24 completed baseline. 16 completed the 12-week visit (8 per arm) and were analysed for blood pressure. |
| Population | Adults seen at the University of Alabama at Birmingham emergency department postdischarge clinic with elevated blood pressure and no primary care provider. Mean age 48.4 (SD 12.8). 38% female. 71% Black. 79% insured. 38% reported difficulty paying for medical care. |
| Duration | 12 weeks per participant. The enrolment window is given as July 2024 to January 2025 in Methods and as July 2024 to March 2025 in Results. |
| Devices/platforms used | [Withings](../../module-01-wearables/profiles/withings.md) BPM Connect Pro upper-arm cuff, provisioned to the intervention arm only. Readings flowed to the UAB electronic health record and then to REDCap. Weekly pharmacist video visits ran on Doximity on the participant's own smartphone. No Module 2 platform. |
| Funding/COI | NIH Forge AHEAD Center P50MD017338 and BIGDATA MHI Core P30AR072583. Competing interests "None declared." No Withings funding or Withings-affiliated author. Who supplied the cuffs is not reported. Usual care participants received US$75. Intervention participants received US$435, including US$30 per pharmacist visit. |
| Last verified | 2026-10-30, against the Europe PMC full-text XML (PMC13691778) |

## Summary

This pilot gave a connected blood pressure cuff to patients leaving an emergency department with no primary care. A pharmacist reviewed the transmitted readings in weekly video visits and adjusted medication with physician approval. The comparator was the clinic's usual follow-up and the same education handout.

The screening funnel was short. 24 of 27 patients assessed were randomised. The paper reports this as an 88.9% recruitment rate.

Retention was 67% in both arms. Most loss was at the single in-person 12-week visit, not active withdrawal. Three intervention participants completed most weekly visits and then did not come in.

The cuff figures are the device content. 11 of 12 intervention participants transmitted at least one reading. One transmitted none despite receiving the cuff. The 11 sent 2029 readings, a mean of 169 (SD 115) each.

## Instrumentation and Deployment Model

Provisioned, intervention arm only. Participants were told to measure twice in the morning and twice in the evening. The paper calls this "a total of four readings per day over 12 weeks."

The cuff sent readings to the UAB electronic health record. From there they were transferred to the study REDCap database. A Methods sentence says instead that the cuff "was programmed to transmit data directly to the study REDCap database." The paper does not reconcile the two routes.

The paper also disagrees with itself on connectivity. Methods say the cuff transmits "via Wi-Fi/Bluetooth." The Discussion calls it "a cellular-enabled RBPM device requiring no Wi-Fi." The Module 1 Withings profile lists cellular variants of the BPM range. The paper does not say whether a Withings app or account was involved.

Adherence support had two layers. Daily automated text messages prompted measurement. A study team member contacted any participant who missed three consecutive days. The number of such contacts is not reported.

UAB nursing staff reviewed incoming readings Monday to Friday under the hospital's existing remote monitoring programme. Yellow and red alert thresholds set the response. The usual care arm had no cuff and no study contact between baseline and 12 weeks.

Eligibility required a smartphone with video capability. Phone OS is not reported. Second-shift and overnight workers were excluded because the protocol needed daytime video visits and twice-daily readings.

## Recruitment and Retention

The research coordinator screened the electronic health record for clinic patients on prespecified recruitment days only. A screening log recorded ineligibility and refusals. The refusal count is not given in the text.

| Stage | n |
|---|---|
| Assessed for eligibility | 27 |
| Met inclusion and randomised | 24 |
| Intervention / usual care | 12 / 12 |
| Completed baseline | 24 |
| Completed the 12-week visit | 16 (8 per arm) |
| Analysed for blood pressure | 16 |

Methods define the recruitment rate over eligible patients. Results compute it as 24 of 27 assessed.

Retention was defined a priori as completing the 12-week visit with a clinic blood pressure. In the intervention arm, one participant was withdrawn at week 3 under the safety protocol for uncontrolled blood pressure. Three others "completed most weekly visits" but did not attend or give blood pressure at 12 weeks. In the usual care arm, four did not attend. Their reasons were not captured because that arm had no interim contact.

The intervention arm received US$435 in compensation against US$75 for usual care. Retention was still identical. The authors read this as evidence that the in-person visit, not money, drove attrition.

## Data Completeness and Technical Issues

| Measure | Intervention arm |
|---|---|
| Transmitted at least one cuff reading | 11 of 12 (92%) |
| Transmitted no readings | 1 of 12 |
| Total readings, among the 11 | 2029 |
| Readings per participant, mean (SD) | 169 (115) |
| Readings per week, mean (SD) | 15 (9) |
| Participants with readings, per week | 9 to 11 |
| Pharmacist visits completed, mean (SD) of 12 | 10.6 (3.3), range 3 to 12 |
| Visits with blood pressure reviewed | 96.9% (123/127) |
| Completed acceptability measures | 8 of 12 |

The reading-adherence arithmetic does not reconcile. Methods specify four readings a day. Results give the expected maximum as 168 readings "with twice-daily readings over 84 days." The reported mean of 169 is above that maximum. No per-participant completeness percentage is given against either protocol.

No technical failure modes are reported. There is nothing on sync failures, connectivity gaps, cuff faults or data lost between Withings, the health record and REDCap. The reason the one participant sent no readings is not given. Weekly adherence detail is in online supplemental table 1, which was not retrieved for this profile.

No OS breakdown is reported.

## Feasibility Findings

The authors conclude the programme "is feasible, highly acceptable" in a predominantly Black safety-net population. They describe it as technically and culturally feasible in this setting. Acceptability scores were AIM 4.69, IAM 4.75 and FIM 4.78 on a 1 to 5 scale, from 8 respondents.

They name three changes for the planned multisite trial. Outcomes should be collected remotely to cut attrition at the in-person visit. The usual care arm should get a home cuff without pharmacist support. Compensation should be tied to shared study milestones and applied equally across arms.

## Relevance to Future Study Design

A connected cuff reached almost everyone it was given to. 11 of 12 transmitted data in a population with no primary care and frequent cost barriers. That is a small sample, and the paper gives no completeness rate against its own protocol.

State the reading protocol once and compute adherence against it. This paper specifies four readings a day and then benchmarks against two. A future team cannot tell from it what share of expected readings arrived.

Routing device data through the hospital record has a cost. Here it let existing nursing staff review readings on weekdays. It also put two systems between the cuff and the research database, and the paper reports nothing on loss at either step.

The single in-person outcome visit was where participants were lost. Three intervention participants stayed engaged for weeks and then missed it. Remote collection of the final reading is the cheapest fix the paper points to.

Paying per pharmacist visit gave the intervention arm US$435 against US$75. A future trial that keeps this structure cannot separate engagement from payment.

## Evidence Confidence

Verified. The screening and randomisation counts, the per-arm retention and its reasons, the safety withdrawal, the 11 of 12 transmitting, the 2029 readings and the per-participant and per-week means, the pharmacist visit counts and fidelity percentages, the acceptability scores and respondent count, the compensation amounts, and the funding and competing-interests statements were read from the Europe PMC full-text XML of the published article (CC BY-NC 4.0) on 2026-10-30.

Unclear. The enrolment end month differs between Methods and Results. The cuff's connectivity is given as Wi-Fi/Bluetooth and as cellular. The data path is given as via the health record and as direct to REDCap. The expected-readings benchmark contradicts the stated four-a-day protocol, and the mean exceeds it. Supplemental table 1 was not read.

The device attribution in the scan queue (Withings BPM Connect Pro) was confirmed from the Methods. The first author was taken from the XML's author contributor records, not from a PDF byline.

## Key Links

- Paper (OA, CC BY-NC 4.0): https://doi.org/10.1136/bmjopen-2026-121681
- Europe PMC: https://europepmc.org/article/PMC/PMC13691778
- Trial registration: https://clinicaltrials.gov/study/NCT06247111
- Local PDF: none. Full text was read from the Europe PMC XML.

## Related profiles

- Device: [Withings](../../module-01-wearables/profiles/withings.md)
- The other Withings deployment, also with a connected blood pressure monitor: [`withings-postop-remote-monitoring.md`](withings-postop-remote-monitoring.md)
- Another emergency department deployment: [`oura-ed-admitted-older-adults-sleep.md`](oura-ed-admitted-older-adults-sleep.md)
- Another small pilot RCT with a provisioned device: [`apple-watch-pst-college-alcohol-use-pilot-rct.md`](apple-watch-pst-college-alcohol-use-pilot-rct.md)
- Cardiovascular deployments: [`fitbit-heart-study-afib.md`](fitbit-heart-study-afib.md), [`apple-heart-data-management-lessons.md`](apple-heart-data-management-lessons.md)

## Sources

1. Ghazi L, Gonzalez-Flores P, Green Vance E, Short QH, Mehta T, Hearld LR, Mahmood S, Neyra JA, Mugavero MJ. *BMJ Open* 2026;16(10):e121681. DOI 10.1136/bmjopen-2026-121681. PMID 42914550. PMC13691778. Full text including Tables 1 and 2, figure captions, ethics, compensation, funding and competing-interests statements read from the Europe PMC full-text XML, 2026-10-30. Establishes every figure in this profile.
