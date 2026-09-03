# Panda et al. 2021 - Beiwe surveys around cancer surgery, 101 consented, 24% still answering at six months, no Android user answered at month one

## Quick Facts

| Field | Details |
|---|---|
| Citation | Panda N, Solsky I, Neal BJ, Hawrusik B, Lipsitz S, Lubitz CC, Gibbons C, Brindle M, Sinyard RD, Onnela JP, Cauley CE, Haynes AB. "Expected Versus Experienced Health-Related Quality of Life Among Patients Recovering From Cancer Surgery: A Prospective Cohort Study." *Annals of Surgery Open* 2021;2(2):e060. DOI [10.1097/AS9.0000000000000060](https://doi.org/10.1097/AS9.0000000000000060). PMID 34179891 / PMC8221715. Panda and Solsky are joint first authors. |
| Study design | Prospective cohort at a single academic cancer centre, July 2017 to July 2019. Smartphone surveys before surgery and at 1, 3 and 6 months after. |
| Sample size (enrolled / analyzed) | 101 consented. 74 completed both preoperative surveys and form the analysed sample (73%). 42, 33 and 24 completed the SF-36 at 1, 3 and 6 months. |
| Population | Adults scheduled for breast, skin and soft-tissue, head and neck, or abdominal tumour surgery at Massachusetts General Hospital. Of the 74, mean age 53.9 (SD 13.9), 66.2% female, 86.5% non-Hispanic White. 61 iPhone and 13 Android. |
| Duration | 6 months after surgery per participant. |
| Devices/platforms used | [Beiwe](../../module-02-digital-phenotyping/profiles/beiwe.md) on participant-owned phones, used in this analysis for surveys only. A study-designed expectations survey and the SF-36. The parent cohort collected GPS and accelerometer data that this paper does not analyse. Clinical covariates were abstracted from the health record into REDCap. |
| Funding/COI | NIH T32 DK007754-18 (Panda), an Ariadne Labs Spark Grant from the Paul G. Allen Family Foundation, and NIH/NIMH 1DP2MH103909 (Onnela). Onnela reports funding from Otsuka and an unrestricted gift from Mindstrong Health. Panda reports a contract with a DARPA contractor. Compensation is not reported. |
| Last verified | 2026-09-03 |

## Summary

A thin deployment paper that carries one number the module needs. Of 13 Android users who completed the preoperative surveys, none completed the one-month SF-36. One completed it at three months and one at six. Every iPhone user who answered at month one was among 42 iPhone completers out of 61. The authors do not comment on this. It is in Table 3 and nowhere else.

The paper is a surgical outcomes study, and its deployment content is a survey funnel with an explicit completion rule, a completer-versus-non-completer comparison, and a sensitivity analysis. It reports no attrition reasons, no technical problems, no reminder schedule and no compensation. That is why it is thin. It is included because a zero-of-thirteen operating-system result in a Beiwe deployment from 2017 to 2019 bears directly on the module's stream-specific OS finding, and because the cancer-surgery population is otherwise absent from the Beiwe entries here.

Retention itself was low. 73% completed the two preoperative surveys, then 42%, 33% and 24% of the consented cohort completed the postoperative SF-36 at one, three and six months under a rule that only counted surveys started within a week of the assigned date and at least 75% answered.

## Instrumentation and Deployment Model

Bring your own device. Patients were approached after their surgical consultation, about a week before surgery. Those who consented "were instructed to download the Beiwe smartphone application," which the team had used in earlier surgical studies. Patients without a smartphone or without fluent English were excluded. How many that removed is not reported.

Surveys were sent electronically through the app. Before surgery, a study-designed expectations survey asking patients to estimate their health at 1 week and 1, 3 and 6 months on the eight SF-36 domains, plus a baseline SF-36. Afterwards, the SF-36 at 1, 3 and 6 months. Disease-specific instruments were left out "to minimize survey burden and maximize feasibility."

Survey responses were encrypted and stored under HIPAA-compliant conditions. Clinical data were reviewed periodically from the health record and stored in REDCap. No reminder, support or contact procedure is described.

## Recruitment and Retention

The number approached is not reported. The funnel starts at consent.

| Stage | n | Share of 101 |
|---|---|---|
| Consented | 101 | |
| Completed both preoperative surveys (analysed) | 74 | 73% |
| Excluded for not completing preoperative surveys | 27 | |
| Completed SF-36 at 1 month | 42 | 42% |
| Completed SF-36 at 3 months | 33 | 33% |
| Completed SF-36 at 6 months | 24 | 24% |

Completion followed the American Association for Public Opinion Research definitions. "Only surveys initiated within 1 week of the assigned date and those with ≥75% completion were included in the final analyses."

Preoperative completers and non-completers did not differ on age (53.9 against 48.9, p=0.092), sex, race, BMI, phone operating system (82.4% against 81.5% iPhone, p=0.771), tumour site or neoadjuvant treatment.

Reasons for non-completion at any stage are not reported.

| Timepoint | iPhone | Android |
|---|---|---|
| Preoperative (74) | 61 | 13 |
| Month 1 (42) | 42 | 0 |
| Month 3 (33) | 32 | 1 |
| Month 6 (24) | 23 | 1 |

Month-six responders were older (mean 59.7) and 95.8% non-Hispanic White, against 53.9 and 86.5% in the analysed sample.

## Data Completeness and Technical Issues

Survey completion is the only completeness measure. Passive-stream completeness is not reported because the passive data are not analysed in this paper.

No technical failure modes are reported. Whether the Android result reflects notification delivery, an app problem, a rendering issue, or chance with 13 people cannot be examined from the paper, and the authors offer no explanation. The collection window (2017 to 2019) predates Beiwe's 2024 heartbeat feature.

Missing data were handled with a repeated-measures linear mixed model with multiple imputation as a sensitivity analysis. Observed and predicted SF-36 domain scores did not differ at any timepoint.

## Feasibility Findings

The authors' only feasibility statement is in the Limitations. "Despite the relatively high completion rate of the preoperative surveys, there was loss to follow up when assessing experienced HRQL at 1, 3, and 6 months postoperatively." They take reassurance from the absence of baseline differences and from the sensitivity analysis. They also assert that "the wide ownership and usage of smartphones across social determinants of health underscores the possibility of performing studies with similar methods in a more generalizable patient population," which is not measured in the paper.

## Relevance to Future Study Design

A surgical cohort surveyed through a phone app with no reported reminders lost three quarters of its consented participants by six months. Under a strict one-week window and 75% completion rule, that is the ceiling this design reached.

Zero of 13 Android users answered at month one, and one of 13 at three and six months. This runs the opposite way to [McInerney 2024](beiwe-type-2-diabetes-feasibility.md), where iPhones missed far more surveys than Android on the same platform three years later. The module's position is that OS effects are stream-specific and cannot be predicted from the OS alone. This paper adds that they cannot be predicted from the platform and the stream alone either. Something about this deployment, this period or these 13 people produced a complete Android failure on survey delivery, and the paper cannot say what.

Report the operating-system breakdown at every timepoint. This paper did, in a demographics table, without comment. It is the only reason the result survives.

State the completion rule with the rate. 42% under a one-week window with 75% completion is not comparable to a 42% under any-time, any-completion rules.

## Evidence Confidence

Verified. The consent and completion counts at each timepoint, the completion rule, the completer-versus-non-completer comparison, the operating-system counts by timepoint from Table 3, the demographics, the exclusion criteria, the funding and disclosure statements, and the sensitivity-analysis result were read from the published PDF (Annals of Surgery Open, CC BY 4.0) on 2026-09-03.

Not assessed here. The correlation between expected and experienced quality of life is the paper's subject.

Scope note. This profile rests on one table and one funnel. The parent deployment's primary papers (Panda et al. 2020, *JAMA Surgery* 155:123-129, and Panda et al. 2021, *Annals of Surgical Oncology* 28:985-994) report the passive GPS and accelerometer streams and are not yet profiled. They are the right source for the cohort's passive completeness, and this profile should be read as the survey-retention entry for that deployment.

## Key Links

- Paper (OA, CC BY 4.0): https://doi.org/10.1097/AS9.0000000000000060
- Europe PMC: https://europepmc.org/article/PMC/PMC8221715
- Local PDF: `../../module-02-digital-phenotyping/literature/onnela-lab/2021-panda-annalssurgeryopenperspec-expected-versus-experienced-health-related-quality-life.pdf` (already held by Module 2; not duplicated)

## Related profiles

- Platform: [Beiwe](../../module-02-digital-phenotyping/profiles/beiwe.md)
- OS effects on survey delivery, the opposite direction: [`beiwe-type-2-diabetes-feasibility.md`](beiwe-type-2-diabetes-feasibility.md)
- Other Beiwe surgical and clinic cohorts: [`beiwe-spine-disease-mobility.md`](beiwe-spine-disease-mobility.md), [`beiwe-fitbit-gynecologic-cancer-hope.md`](beiwe-fitbit-gynecologic-cancer-hope.md)
- Post-operative remote monitoring on another device: [`withings-postop-remote-monitoring.md`](withings-postop-remote-monitoring.md)
- Survey-completion rules and their effect on rates: [`whoop-mental-health-survey-engagement.md`](whoop-mental-health-survey-engagement.md)

## Sources

1. Panda N, Solsky I, Neal BJ, et al. *Ann Surg Open* 2021;2(2):e060. DOI 10.1097/AS9.0000000000000060. Full text, Figure 1 and Tables 1 to 5 read from the published PDF, 2026-09-03. Establishes every figure in this profile.
