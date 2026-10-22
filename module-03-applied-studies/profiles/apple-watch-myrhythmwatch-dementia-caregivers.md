# Stahl et al. 2026 - Apple Watch rest-activity rhythm monitoring in dementia caregivers and people with dementia, N=21

## Quick Facts

| Field | Details |
|---|---|
| Citation | Stahl ST, Rodakowski J, Patira R, Smagula SF. "Enhancing a Behavioral Intervention Using Rest-Activity Rhythm Monitoring via a Consumer Wearable in Older Dementia Caregivers and People With Dementia: Feasibility and Acceptability Study." *JMIR Formative Research* 2026;10:e88773. DOI [10.2196/88773](https://doi.org/10.2196/88773). PMC13626640. ClinicalTrials.gov NCT05309577. |
| Study design | Single-arm pilot trial. Feasibility and acceptability are the primary outcomes. Pre-post mood and sleep change in caregivers is secondary. |
| Sample size (enrolled / analyzed) | 25 caregivers screened. 3 ineligible and 7 not interested left 15 caregivers. Of those 15, 7 declined to involve their care recipient and 2 care recipients were ineligible, leaving 6 people with dementia. 21 enrolled and 21 in the feasibility analysis. 11 of 15 caregivers in the pre-post health analysis. |
| Population | Older family caregivers of people with Alzheimer disease or a related dementia, living with the care recipient, in Pittsburgh, United States. Caregivers mean age 61.78 (SD 8.4). People with dementia mean age 81.45 (SD 8.46). |
| Duration | 6-week intervention per participant. Enrolment March 2023 to April 2024. People with dementia were later cut to 1 month of use. |
| Devices/platforms used | [Apple Watch](../../module-01-wearables/profiles/apple-watch-healthkit.md) Series 8, provisioned by post. Raw accelerometry processed by myRhythmWatch, a third-party app with a phone display and a clinician dashboard. No phenotyping platform. |
| Funding/COI | NIH R41AG069596 and P30AG024978. The last author owns and is CEO of Activity Rhythm Solutions, the former university start-up that developed myRhythmWatch with support from R41AG069596. Participants were paid US $125 for completing study procedures. |
| Last verified | 2026-10-22 |

## Summary

This is a small single-arm pilot that used an Apple Watch as a continuous rest-activity rhythm monitor. Therapists read the watch data each week to tailor a behavioural activation programme. The deployment question is whether a consumer watch can carry six weeks of near-24-hour wear in two groups that usually struggle with wearables, older caregivers and people with dementia.

The caregiver answer was yes. All 15 met the minimum data rule of 3 consecutive valid days. They averaged 35.5 valid days (SD 2.7) in a 42-day trial. All 15 were still collecting data in the last week.

The people with dementia did worse. They averaged 30.0 valid days (SD 3.2). Daily hours were lower and more variable across the trial. The team changed the protocol mid-study to ask caregivers to use the app with their care recipient for only 1 month.

The bigger loss was before enrolment. Of 15 caregivers asked to bring their care recipient, 7 declined or thought the study inappropriate for them. Only 6 of a possible 15 dyads formed.

## Instrumentation and Deployment Model

Provisioned. Each participant received an Apple Watch Series 8 through the United States Postal Service. Each had a one-to-one orientation. 18 of 21 (86%) chose a virtual orientation and 3 (14%) asked for one in person. Staff followed up 2 days after orientation "as needed" to troubleshoot.

Participants were asked to wear the watch for the whole 6 weeks. They were told to take it off only to bathe or shower and to charge it then. The charging routine is the only battery-management instruction reported.

myRhythmWatch reads raw triaxial accelerometry from the watch. The data are bandpass filtered, aggregated across axes and cut into 30-second epochs. Standard rest-activity rhythm measures are then shown as standardised scores on the participant's phone. Therapists saw the same metrics and raw accelerometer plots on a clinician dashboard the authors describe as HIPAA-compliant. The paper does not say whether the phone was the participant's own or supplied. iPhone model and iOS version are not reported.

Therapists used the dashboard in 6 weekly sessions of about 30 to 45 minutes. Sessions that included a care recipient ran about 60 minutes. Caregivers ran the sessions for themselves and for their care recipients.

## Recruitment and Retention

Recruitment was by targeted email to members of Pitt+Me, a University of Pittsburgh research registry of more than 400,000 people. Interested members were screened and consented on the same first phone call. Consent was electronic in REDCap.

Proxy consent was allowed for people with dementia who lacked capacity, with verbal assent. 3 of 6 signed their own e-consent. 3 were consented by proxy.

The caregiver eligibility rule changed after the study began. A PHQ-9 score of at least 5 was added on stakeholder advice. 3 caregivers were enrolled after the change.

All 21 enrolled participants completed the intervention. The paper reports no withdrawals. Caregiver therapy attendance was 5 of 6 sessions for 27% and 6 of 6 for 73%. The abstract gives this as a mean of 5.7 (SD 0.46).

The health assessments lost more people than the watch did. 4 of 15 caregivers (27%) did not complete pre and post measures. The authors attribute this to scheduling conflicts and low caregiver availability.

## Data Completeness and Technical Issues

A valid day was defined as at least 20 hours of accelerometer data. The feasibility threshold was at least 3 consecutive valid days.

- Caregivers. 15 of 15 met the threshold. Mean 35.5 valid days (SD 2.7). A few fell under the daily minimum in week 1. In later weeks the average caregiver collected sufficient daily data.
- People with dementia. 6 of 6 met the threshold. Mean 30.0 valid days (SD 3.2). Collection was lower and more variable throughout.

Per-participant daily hours are shown only in Figures 4 and 5. No per-week percentages are given in the text.

The paper names "increasing data collection issues among people with dementia" but does not say what they were. Device failures, sync problems, battery problems and app crashes are not reported. The number of valid days lost to charging is not reported. No adverse events were reported.

The abstract contradicts the Results on one point. It says "of the 6 people with dementia, only 6 were active users at the end of the trial." That sentence cannot be correct as written, and the Results text gives no end-of-trial count for this group.

Other internal inconsistencies, recorded so nobody re-derives them.
- Caregiver sex is 12 of 15 women (80%) in the Results text and 13 (87%) in Table 1.
- Black caregivers are "24% (4/15)" in the text and 4 (26.7) in Table 1.
- The PHQ-9 test statistic is t10=2.417 in the abstract and 2.477 in Table 2.
- The Discussion says 9 of 15 caregivers (60%) thought the study inappropriate for their care recipient. The Methods split that 9 into 7 who declined and 2 whose care recipient was ineligible.

## Feasibility Findings

The authors conclude that personalising a behavioural intervention with consumer-watch rest-activity monitoring is feasible and acceptable in older dementia caregivers. They base this on sustained caregiver engagement over 6 weeks.

They call monitoring in people with dementia feasible "albeit with significant caveats." Most caregivers did not think it suitable for their care recipient. Engagement among the 6 who joined was lower and shorter. Their summary is that the watch works for people with dementia "but not in all patients and typically not over longer periods."

They recommend that future studies in people with dementia try less obtrusive sensors, such as a pin or pendant. Satisfaction was rated 4.8 of 5 (SD 0.44).

## Relevance to Future Study Design

A 20-hour valid-day rule is strict for a watch that has to come off to charge. Caregivers still met it on about 35 of 42 days when told to charge during bathing.

Plan the dyad funnel, not just the caregiver funnel. Less than half of eligible caregivers brought a care recipient in.

Budget for shorter monitoring in people with dementia. This team shortened it mid-study, and the paper does not report what drove the data problems.

The figures come from 21 people at one site, recruited from a research registry, all of them willing to use digital technology. The authors expect lower feasibility among people with less digital literacy.

## Evidence Confidence

Verified for the funnel, the valid-day definition, the valid-day means, the orientation split, the session attendance and the funding and conflict statements. All were read from the Europe PMC full-text XML (PMC13626640, CC BY 4.0) on 2026-10-22. The publisher PDF could not be retrieved by script, so the byline and figures were taken from the JATS full text.

Unclear for the end-of-trial status of people with dementia, because the abstract sentence is self-contradictory. Also unclear for what the "data collection issues" were.

Conflict note. The last author owns the company that developed myRhythmWatch. The feasibility figures are simple counts, but the study evaluates that company's product.

## Key Links

- Paper (OA, CC BY 4.0): https://doi.org/10.2196/88773
- Europe PMC: https://europepmc.org/article/PMC/PMC13626640
- Trial registration: https://clinicaltrials.gov/study/NCT05309577
- Local PDF: none. The PMC and JMIR PDF endpoints returned challenge pages to a script on 2026-10-22, so no PDF is stored.

## Related profiles

- Device: [Apple Watch and HealthKit](../../module-01-wearables/profiles/apple-watch-healthkit.md)
- Other Apple Watch deployments in this module: [`apple-heart-movement-study-retention.md`](apple-heart-movement-study-retention.md), [`apple-womens-health-study-retention.md`](apple-womens-health-study-retention.md)
- Dementia and older-adult deployments: [`mpath-dementia-esm-feasibility.md`](mpath-dementia-esm-feasibility.md), [`radar-ad-feasibility-usability.md`](radar-ad-feasibility-usability.md), [`sensorkit-techsans-older-adults.md`](sensorkit-techsans-older-adults.md)
- Wear-time definitions changing the result: [`actigraph-als-upper-limb-wear-time.md`](actigraph-als-upper-limb-wear-time.md)

## Sources

1. Stahl ST, Rodakowski J, Patira R, Smagula SF. *JMIR Form Res* 2026;10:e88773. DOI 10.2196/88773. PMC13626640. Full text, Tables 1 and 2 and figure captions read from the Europe PMC full-text XML, 2026-10-22. Establishes every figure in this profile.
