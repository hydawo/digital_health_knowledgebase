# Matcham et al. 2022 - RADAR-MDD, perceived usability and symptom severity as predictors of Fitbit wear and app questionnaire completion, N=547

## Quick Facts

| Field | Details |
|---|---|
| Citation | Matcham F, Carr E, White KM, Leightley D, Lamers F, Siddi S, Annas P, de Girolamo G, Haro JM, Horsfall M, Ivan A, Lavelle G, Li Q, Lombardini F, Mohr DC, Narayan VA, Penninx BWJH, Oetzmann C, Coromina M, Simblett SK, Weyer J, Wykes T, Zorbas S, Brasen JC, Myin-Germeys I, Conde P, Dobson RJB, Folarin AA, Ranjan Y, Rashid Z, Cummins N, Dineley J, Vairavan S, Hotopf M, on behalf of the RADAR-CNS consortium. "Predictors of engagement with remote sensing technologies for symptom measurement in Major Depressive Disorder." *Journal of Affective Disorders* 2022;310:106-115. DOI [10.1016/j.jad.2022.05.005](https://doi.org/10.1016/j.jad.2022.05.005). PMID 35525507. No PMCID. Matcham and Carr are joint first authors. |
| Study design | Secondary analysis of the RADAR-MDD observational cohort. Bayesian multivariable random-effects models linking symptoms, perceived usability and engagement at 3 and 12 months. |
| Sample size (enrolled / analyzed) | 623 enrolled in RADAR-MDD. 547 (87.8%) analysed after excluding 7 without clinical data, 65 without usability data and 4 without covariates. 535 at the 12-month timepoint. |
| Population | Adults with recurrent MDD at King's College London, VUmc Amsterdam and CIBER Barcelona. Median age 48 (IQR 32 to 58). 24% male. 41% in paid work. |
| Duration | Usage measured over the 3 months after the 3-month and 12-month assessments (months 3 to 6 and 12 to 15). |
| Devices/platforms used | [RADAR-base](../../module-02-digital-phenotyping/profiles/radar-base.md) active app (fortnightly PHQ-8). [Fitbit](../../module-01-wearables/profiles/fitbit-google.md) wrist tracker. Android phones. REDCap for 3-monthly outcomes and the usability questionnaires. |
| Funding/COI | RADAR-CNS is an IMI2 programme. Co-authors list affiliations with H. Lundbeck A/S and Janssen Research and Development. The funding and competing-interest statements were not in the accepted manuscript read. Participants were paid for enrolment, interviews and 3-monthly outcome data, but not for app questionnaires or Fitbit wear. |
| Last verified | 2026-10-31 |

## Summary

This paper overlaps the existing RADAR-MDD profiles ([Matcham 2022 BMC Psychiatry](radar-mdd-recruitment-retention.md), [Zhang 2023](radar-mdd-longterm-engagement.md)). It is profiled separately because it adds operational figures they do not carry. It gives Fitbit wear and PHQ-8 completion at two fixed three-month windows. It measures system usability and acceptability directly. It tests whether either predicts use.

The answer is that neither symptoms nor perceived usability predicted engagement to any practical degree. A one-SD rise in perceived ease of use was linked to 0.33 more PHQ-8 questionnaires over three months. It was linked to a two-point rise in the share of time wearing the Fitbit. Depression severity was not associated with any usability or usage measure.

Engagement decayed between the two windows. Median Fitbit wear fell from 0.90 of the time in months 3 to 6 to 0.74 in months 12 to 15. The share of windows with no PHQ-8 at all rose from 16% to 23%.

## Instrumentation and Deployment Model

The deployment is the RADAR-MDD protocol already described in [`radar-mdd-recruitment-retention.md`](radar-mdd-recruitment-retention.md). Participants used an existing Android phone or swapped to one for the study. PHQ-8 was pushed fortnightly through the RADAR-base active app.

Fitbit wear was the share of 15-minute periods per day containing heart rate data. It was averaged by month and rescaled over each three-month window to run from 0 (never worn) to 1 (always worn).

Perceived usability used the Post-Study System Usability Questionnaire (PSSUQ). Acceptability used the Technology Acceptance Model Fast Form (TAM-FF). Both were emailed through REDCap at 3, 12 and 24 months. Both asked about the whole system rather than the Fitbit and the app separately.

## Recruitment and Retention

Recruitment is reported in the parent paper. Here the analytic exclusions are the funnel.

| Stage | n |
|---|---|
| Enrolled in RADAR-MDD | 623 |
| Excluded, no clinical data | 7 |
| Excluded, no usability or acceptability data | 65 |
| Excluded, no covariates | 4 |
| Analysed | 547 (87.8%) |
| At the 12-month timepoint | 535 |

Excluded participants resembled the analysed sample on age, gender, education and comorbidity. Participants who withdrew partway through a three-month window were dropped from that window's usage measure.

## Data Completeness and Technical Issues

| Measure | Months 3 to 6 | Months 12 to 15 |
|---|---|---|
| Fitbit wear, median share of time (IQR) | 0.90 (0.56 to 0.97) | 0.74 (0.17 to 0.94) |
| Windows with no PHQ-8 completed | 86 (16%) | 100 (23%) |
| PSSUQ, reversed, median (IQR) | 94 (75 to 106) | 93 (73 to 107) |
| TAM-FF, reversed, median (IQR) | 86 (71 to 101) | 87 (68 to 103) |

Pooled across both windows, 19% of Fitbit observations (202 of 1082) showed zero wear. 19% of PHQ-8 observations (186 of 975) showed no questionnaire returned.

Usability scores barely moved between 3 and 12 months while Fitbit wear dropped sharply. Perceived usability does not track the decay.

Anxiety, not depression, carried the small clinical effects. A one-SD rise in GAD-7 was linked to 0.13 fewer PHQ-8 completions. A one-SD rise in functional disability (WSAS) was linked to a 3-point drop in the share of time wearing the Fitbit.

The paper names one measurement failure. Google Analytics logs showed more questionnaires completed than notifications received. A questionnaire could only be opened from a notification. The authors stopped trusting the analytics and used completion counts instead.

The PHQ-8 completion table runs from 0 to 6 per window, while the Methods describe a 0 to 9 count. The paper does not reconcile the two.

No iOS breakdown applies. The study was Android-only.

## Feasibility Findings

The authors conclude that perceived usability and actual use of remote measurement in MDD are robust across depression severity. Their reassurance to researchers is direct. People with more severe depressive symptoms were still able to participate effectively.

They suggest active tasks are more sensitive to anxiety and passive wear more sensitive to physical function. They caution that close contact with a supportive research team may have masked usability effects that would appear in real-world use.

## Relevance to Future Study Design

Do not screen out people with severe depression to protect data yield. Severity did not predict wear or questionnaire completion in 547 participants.

Do not expect a usability questionnaire to forecast attrition. Scores stayed flat while median wear fell from 0.90 to 0.74.

Plan for about a fifth of three-month windows to contain no data from a given stream, even in a well-supported cohort.

Validate notification analytics against task completions before using them as an engagement measure. Here the two disagreed in an impossible direction.

## Evidence Confidence

Verified. The exclusion counts, Table 1 demographics, the usage and usability medians at both windows, the zero-wear and zero-PHQ-8 counts, the Table 2 and Table 3 effect estimates, the wear-time definition, the compensation description and the Google Analytics discrepancy were read from the author accepted manuscript (figshare, CC BY) on 2026-10-31.

Unclear. The funding and competing-interests sections were not in the accepted manuscript. Industry ties are taken from the affiliation list only. The 0 to 9 versus 0 to 6 PHQ-8 range is unresolved.

Not assessed here. The version of record on ScienceDirect was not read. Figures may differ from the accepted manuscript in minor ways.

## Key Links

- Paper: https://doi.org/10.1016/j.jad.2022.05.005
- Accepted manuscript (figshare, CC BY): https://figshare.com/articles/journal_contribution/Predictors_of_engagement_with_remote_sensing_technologies_for_symptom_measurement_in_Major_Depressive_Disorder/24118110
- Preprint: https://doi.org/10.31234/osf.io/t2k5d
- Local PDF: none held

## Related profiles

- Platform: [RADAR-base](../../module-02-digital-phenotyping/profiles/radar-base.md)
- Device: [Fitbit / Google](../../module-01-wearables/profiles/fitbit-google.md)
- Same cohort: [`radar-mdd-recruitment-retention.md`](radar-mdd-recruitment-retention.md), [`radar-mdd-longterm-engagement.md`](radar-mdd-longterm-engagement.md)
- Follow-on trial in the same London participants: [`radar-base-fitbit-mdd-inapp-engagement-rct.md`](radar-base-fitbit-mdd-inapp-engagement-rct.md)
- Anxiety rather than depression predicting disengagement: [`radar-base-treatment-engagement.md`](radar-base-treatment-engagement.md)

## Sources

1. Matcham F, Carr E, White KM, et al., RADAR-CNS consortium. *J Affect Disord* 2022;310:106-115. DOI 10.1016/j.jad.2022.05.005. Author accepted manuscript, Tables 1 to 3 and supplementary figures read from the figshare deposit, 2026-10-31. First authors taken from the manuscript byline. Establishes every figure in this profile.
