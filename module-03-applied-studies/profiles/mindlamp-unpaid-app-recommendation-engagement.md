# Dwyer et al. 2024 - mindLAMP phenotyping to guide app recommendation, unpaid and fully remote, 5 weeks, N=82

## Quick Facts

| Field | Details |
|---|---|
| Citation | Dwyer B, Flathers M, Burns J, Mikkelson J, Perlmutter E, Chen K, Ram N, Torous J. "Assessing Digital Phenotyping for App Recommendations and Sustained Engagement: Cohort Study." *JMIR Formative Research* 2024;8:e62725. DOI [10.2196/62725](https://doi.org/10.2196/62725). PMID 39560976 / PMC11615540. Published 2024-11-19. |
| Study design | Two-arm pilot. After 1 week of mindLAMP data collection, participants were randomly assigned to a digital navigator recommendation based on their phenotyping data or to unguided choice among the same 4 apps. Engagement with the chosen app is the outcome. |
| Sample size (enrolled / analyzed) | 82 enrolled. 22 dropped after the first meeting (11 per arm). 13 dropped after the second meeting (7 control, 6 treatment). 47 remained. Only the How We Feel and UCLA Mindful groups were large enough to analyse. 39 of 47 used a depression or anxiety app. |
| Population | US adults recruited through ResearchMatch with GAD-7 above 5, a primary care physician or psychiatrist, and an Apple or Android phone. Among the 47 remaining, mean age 43.0 (SD 16), 79% female, 89% White. 43% were 4-year college graduates and 30% had a master's degree or higher. |
| Duration | 5 weeks. Week 1 was observational. Weeks 2 to 5 were use of the chosen intervention app. Calendar dates are not reported. |
| Devices/platforms used | [mindLAMP](../../module-02-digital-phenotyping/profiles/mindlamp.md) on participants' own phones (BYOD), used only for data collection. Passive GPS, accelerometer, screen and phone on or off, and step count. Active surveys in mindLAMP and REDCap. Intervention app use was measured from participant screenshots of the phone's Screen Time page. No wearable. |
| Funding/COI | No funding statement in the full text. Torous, the senior author, is editor-in-chief of *JMIR Mental Health*. The study is from the BIDMC Division of Digital Psychiatry, which the paper states developed mindLAMP. Participants received no compensation. BIDMC IRB protocol 2022P001143. |
| Last verified | 2026-10-31, from the Europe PMC full-text XML |

## Summary

This study ran a remote mindLAMP protocol with no payment at all. Its operational value is the attrition it produced and the reasons recorded for it.

43% (35/82) dropped out within 5 weeks. Most of the loss came early. 27% (22/82) left after the first meeting, before any intervention app was chosen.

Reasons were mostly unknown. 9 of the 22 early leavers and 11 of the 13 later leavers gave no reason. Three early and 2 later leavers left for "data quality reasons," which the paper does not define.

The authors attribute the attrition to the lack of payment and the remote format. They judged that paying participants would have confounded the engagement outcome.

## Instrumentation and Deployment Model

BYOD on Apple or Android. OS split is not reported.

mindLAMP was configured for data collection only (Materials, mindLAMP App). It ran custom surveys and passive GPS, accelerometer, screen-use and step-count sensors throughout the 5 weeks.

A 6-item daily survey ran twice a day in week 1. It dropped to 3 times a week from the second visit to the end (Active Data). System Usability Scale and Digital Working Alliance Inventory were given at each of 3 web-based visits.

In the experimental arm a digital navigator reviewed a radar plot and a correlation matrix of the participant's week-1 mindLAMP data. The navigator then recommended an app targeting the symptom most correlated with impaired functioning.

Intervention app screen time could not be captured automatically across Apple and Android. Participants submitted screenshots of their Screen Time page at the final visit instead.

## Recruitment and Retention

All participants came from ResearchMatch (Participants). Consent was web-based. Screening counts are not reported.

47 of 82 remained to the end. The paper reports the complement, 35 (43%) dropouts. The definition is remaining in the study through the third visit.

Attrition after the first meeting was 22. Of these, 9 gave unknown reasons, 6 lost interest, 3 cited the time commitment, 3 left for data quality reasons and 1 had a family emergency (Results, Demographics and Groups).

Attrition after the second meeting was 13. Of these, 2 left for data quality reasons and 11 for unknown reasons.

The Limitations section adds that some participants "finished the study but were excluded for data quality issues." Whether these are the same 5 counted as dropouts is not stated.

Dropout was balanced by arm. The abstract gives 17 (21%) in the phenotyping arm and 18 (22%) in the control arm.

## Data Completeness and Technical Issues

No mindLAMP completeness figure is reported for any passive stream. The daily survey response rate is not reported.

The definition of "data quality reasons" is not given. The paper calls the problem "ubiquitous in digital phenotyping research."

Screen time for the intervention apps was self-reported by screenshot. The authors found no correlation between self-reported engagement and scaled screen time (R2=0.0188, P=.39).

Two of the four intervention apps had too few users to analyse. The navigator algorithm consistently pointed to depression and anxiety targets. Control participants mostly chose the same two apps.

Not reported. OS split. GPS or accelerometer coverage. Technical failures in mindLAMP. The calendar period of enrolment.

## Feasibility Findings

The authors conclude that phenotyping-guided app recommendation "is feasible and may increase engagement." The screen-time difference for How We Feel was not significant (P=.36).

They attribute the small sample and high dropout to the absence of compensation and the remote format. They state that paying for visits would likely have raised engagement but confounded the results. They also state that in-person visits might have cut dropout but narrowed recruitment.

They recommend a four-arm design for future work. The arms would be clinical recommendation, phenotyping-based recommendation, participant choice and no app.

## Relevance to Future Study Design

An unpaid, fully remote mindLAMP study recruited through a national registry lost 43% of participants in 5 weeks. Most of that loss happened before the second visit.

Ask for and record a reason at every withdrawal. 11 of the 13 later leavers here gave none.

Define "data quality" exclusions before the study starts. This paper lost participants to it at both dropout points without saying what failed.

Screen Time screenshots were the workaround for measuring third-party app use across both OSs. They did not agree with self-report.

## Evidence Confidence

Reported. The attrition counts and reasons, the arm balance and the deployment details were read from the Europe PMC full-text XML (PMC11615540, CC BY 4.0) on 2026-10-31. They are simple counts. The paper gives no passive-data completeness, so the platform-side feasibility of mindLAMP in this cohort cannot be graded beyond attrition.

Unclear. Whether participants excluded for data quality after finishing are included in the 35 dropouts.

Not assessed here. Whether recommendation improved engagement or symptoms is the study's research question.

## Key Links

- Paper (OA, CC BY 4.0): https://doi.org/10.2196/62725
- Europe PMC: https://europepmc.org/article/PMC/PMC11615540
- Local PDF: not held. The paper is not in `module-02-digital-phenotyping/literature/mindlamp/`.

## Related profiles

- Platform: [mindLAMP](../../module-02-digital-phenotyping/profiles/mindlamp.md)
- Other mindLAMP deployments in this module: [`mindlamp-digital-clinic-blended-care-open-trial.md`](mindlamp-digital-clinic-blended-care-open-trial.md), [`mindlamp-older-adults-gps-cognition-feasibility.md`](mindlamp-older-adults-gps-cognition-feasibility.md), [`mindlamp-linc-passive-data-quality.md`](mindlamp-linc-passive-data-quality.md)
- Unpaid deployments: [`lamp-schizophrenia-cognition-unpaid.md`](lamp-schizophrenia-cognition-unpaid.md)
- Remote recruitment and data quality: [`metricwire-fraudulent-participation.md`](metricwire-fraudulent-participation.md)

## Sources

1. Dwyer B, Flathers M, Burns J, Mikkelson J, Perlmutter E, Chen K, Ram N, Torous J. *JMIR Formative Research* 2024;8:e62725. DOI 10.2196/62725. PMC11615540. Full text read from the Europe PMC XML, 2026-10-31. Establishes every figure in this profile.
