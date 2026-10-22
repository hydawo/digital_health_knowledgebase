# Haimovich et al. 2026 - Oura Ring Gen 3 in older adults admitted from the emergency department, N=15

## Quick Facts

| Field | Details |
|---|---|
| Citation | Haimovich AD, Lacourciere A, Palihnich K, Mulqueen S, Jansen N, Bertisch SM, Schonberg MA, Naik AD, Berry SD, Marcantonio ER, Shapiro NI, Mullington JM. "Feasibility and Acceptability of Oura Ring Sleep Monitoring in Older Adults Admitted From the Emergency Department: Prospective Cohort Study." *JMIR Form Res* 2026;10:e92359. DOI [10.2196/92359](https://doi.org/10.2196/92359). PMID 42814730 / PMC13626187. Published 2026-09-30. The PDF byline marks Haimovich, Lacourciere and Bertisch with an asterisk. |
| Study design | Single-site prospective cohort pilot. Feasibility and acceptability are the primary outcomes. No formal sample size calculation. Not registered as a trial. |
| Sample size (enrolled / analyzed) | 29 approached, 15 enrolled (2 through a legally authorised representative), 1 withdrew immediately, 14 in the feasibility analysis. 13 met the wear criterion. 11 completed the exit survey. 10 had complete paired device and survey data. |
| Population | Adults aged 65 or over in the Beth Israel Deaconess Medical Center ED, Boston, with an inpatient medical bed request placed between 1 PM and 10 PM. Median age 78 (IQR 75 to 82, range 65 to 92). 7 of 14 female. 13 White non-Hispanic, 1 Black non-Hispanic. 3 with documented dementia or cognitive impairment. 2 delirious at enrolment and 2 more developed delirium. |
| Duration | Up to 4 hospital days or until discharge, whichever came first. Recruitment February to March 2025. Median 2 monitored nights (IQR 1 to 3). |
| Devices/platforms used | [Oura Ring Gen 3](../../module-01-wearables/profiles/oura.md), provisioned. Each ring synced to a study-provided Apple iPhone SE. Data exported as CSV from Oura Teams. REDCap held survey and chart data. No phenotyping platform. |
| Funding/COI | NIA awards 1K23AG090744 and R33AG058926 (through GEAR), K24AG070106 and R01AG030618. The paper states Oura Health Ltd was not involved in funding, design, data collection, analysis, interpretation or writing. Unrelated author disclosures (MBO Partners advising, UpToDate royalties, Apnimed and Aethermind consulting). Participant compensation is not reported. |
| Last verified | 2026-10-22 |

## Summary

This is an acute-care deployment of a consumer ring. Patients were enrolled while boarding in the ED and kept the ring on through transfer to an inpatient unit. The window was days, not weeks.

The headline is that the ring stayed on. Of 14 participants who completed study procedures, 13 wore it for more than 75% of the analysed period (92.9%, 95% CI 66.1% to 99.8%). The median participant-level wear percentage was 93.4% (IQR 91.0% to 96.2%).

Delirium is where it broke. The single participant who failed the wear criterion was delirious at enrolment and wore the ring for about 8% of the period. All three participants who missed the exit survey were delirious at the planned assessment. One of those was moved to intensive care and the ring was removed.

Recruitment was the weaker link. 15 of 29 approached patients enrolled (51.7%, 95% CI 32.5% to 70.6%). Five of the 14 non-enrolments were capacity related.

## Instrumentation and Deployment Model

Fully provisioned. Research staff fitted the ring in the ED and asked patients to wear it continuously. Rings were returned at the end of study procedures. Each ring was paired to a study iPhone SE rather than the patient's own phone. No protected health information was entered at ring registration.

Wear time was not read from a vendor wear flag. The authors derived it from one-minute MET values exported from Oura Teams. A minute counted as worn when MET was 0.9 or greater. Device cessation was the first minute after which all remaining MET values fell below 0.9. Wear percentage was computed within complete 9 PM to 9 PM intervals and averaged per participant.

ED time and inpatient-unit time were pooled. Unit-location timestamps were not available, so the study cannot separate boarding from ward time.

Active collection ran alongside the ring. Staff gave the 3D-CAM delirium assessment daily, the MoCA after the first night in those not delirious, and a daily sleep-quality rating with the PROMIS Sleep Disturbance short form. Delirious participants stayed on the ring but were not asked to complete daily surveys.

## Recruitment and Retention

Recruitment ran on weekdays from 1 PM to 10 PM only, when research staff were available. Staff screened the EHR for inpatient medical bed requests and approached eligible patients when clinical care allowed. The number screened before approach is not reported.

| Stage | n |
|---|---|
| Approached | 29 |
| Declined | 9 |
| Lacked capacity, representative declined | 2 |
| Lacked capacity, no representative available | 3 |
| Enrolled | 15 |
| Withdrew immediately after enrolment | 1 |
| Completed study procedures (feasibility analysis) | 14 |
| Met the more-than-75% wear criterion | 13 |
| Completed exit survey | 11 |
| Complete paired device and survey data | 10 |

The reason for the immediate withdrawal is not reported. The paper does not report how many participants were discharged before day 4.

## Data Completeness and Technical Issues

| Measure | Result |
|---|---|
| Wear criterion met (more than 75% of analysed period) | 13 of 14 (92.9%, 95% CI 66.1% to 99.8%) |
| Median participant wear percentage | 93.4% (IQR 91.0% to 96.2%) |
| Wear in the one non-adherent participant | About 8%, delirious at enrolment |
| Acceptability (disagreed the ring bothered them) | 9 of 11 (81.8%, 95% CI 48.2% to 97.7%) |
| Daily sleep surveys completed | 19 surveyed nights in total |

Acceptability answers split 5 strongly disagree, 4 disagree, 1 neutral and 1 strongly agree.

One ring was removed on transfer to intensive care. No ring loss, sync failure, battery or charging problem is reported. Ring battery life over the window and any charging protocol are not reported.

The device's sleep output was not checked against polysomnography or research actigraphy. Median device-estimated sleep among the 13 adherent participants was 4.3 hours per 24 hours (IQR 2.6 to 7.0). Patient-rated sleep quality correlated with device sleep duration in the 10 with paired data (Kendall tau 0.54, P=.04).

## Feasibility Findings

The authors conclude that Oura Ring Gen 3 monitoring was feasible for most older adults admitted from the ED who completed study procedures. They also conclude it was not bothersome to most exit-survey respondents. They state that delirium "may complicate device and study retention."

They recommend larger multisite studies with location-aware monitoring. They also recommend concurrent polysomnography or research-grade actigraphy in a validation subset. Their third recommendation is retention strategies for patients with delirium or cognitive impairment.

## Relevance to Future Study Design

A provisioned ring paired to a study phone can survive ED boarding and a ward transfer in patients with a median age of 78. Median wear was 93.4%, and only one of 14 missed the 75% criterion.

Delirium is the failure mode to plan for. It accounted for the one wear failure, all three missing exit surveys and the one ICU removal. The acceptability figure excludes exactly those patients.

Budget for capacity. Five of 29 approached patients could not consent and had no representative who agreed. Staffing windows also limit who is reached, because recruitment ran only on weekday afternoons and evenings.

If the analysis needs ED and ward time separately, capture location timestamps. This study could not.

## Evidence Confidence

Verified. The recruitment funnel, the MET-based wear definition, the wear and acceptability proportions with CIs, the delirium attribution of each loss, the ICU removal, and the funding and conflict statements were read from the publisher PDF (PMC13626187, CC BY 4.0) and the Europe PMC JATS full text on 2026-10-22.

The feasibility claims rest on 14 participants. The authors call their own estimates imprecise. The acceptability denominator excludes the three delirious participants, so it is biased upward by construction.

Not assessed here. Whether Oura sleep estimates are valid in hospitalised older adults is a Module 1 question and was not tested in this study.

## Key Links

- Paper (OA, CC BY 4.0): https://doi.org/10.2196/92359
- Europe PMC: https://europepmc.org/article/PMC/PMC13626187
- Local PDF: `../literature/2026-haimovich-jmirformres-oura-ring-sleep-older-adults-ed-admission.pdf`

## Related profiles

- Device: [Oura](../../module-01-wearables/profiles/oura.md)
- Other Oura deployments: [`oura-tempredict-healthcare-worker-adherence.md`](oura-tempredict-healthcare-worker-adherence.md), [`oura-university-freshmen-sleep.md`](oura-university-freshmen-sleep.md)
- Inpatient deployment with provisioned hardware: [`beiwe-inpatient-suicide-pilot.md`](beiwe-inpatient-suicide-pilot.md)
- Cognitive impairment and consent by proxy: [`mpath-dementia-esm-feasibility.md`](mpath-dementia-esm-feasibility.md), [`radar-ad-feasibility-usability.md`](radar-ad-feasibility-usability.md)

## Sources

1. Haimovich AD, Lacourciere A, Palihnich K, et al. *JMIR Form Res* 2026;10:e92359. DOI 10.2196/92359. Publisher PDF and Europe PMC JATS full text (PMC13626187) read 2026-10-22. Establishes every figure in this profile.
