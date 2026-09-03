# Nock et al. 2026 - LifeData EMA after psychiatric emergency or inpatient presentation, 6 prompts a day for 84 days, N=619

## Quick Facts

| Field | Details |
|---|---|
| Citation | Nock MK, Kleiman EM, Bentley KH, Fortgang RG, Millner AJ, Zuromski KL, Bear A, Christie A, Daniel M, DeMarco D, Follet L, Kelly F, Neveux H, Obi-Obasi O, Ricard JR, Ramlal N, Tambedou T, Yacoby Y, Bird SA, Buonapane R, Donovan A, Mair P, Onnela JP, Picard R, Smoller JW. "Using Smartphone Surveys to Predict Next-Week Suicide Attempts." *Journal of Psychopathology and Clinical Science* 2026. DOI [10.1037/abn0001117](https://doi.org/10.1037/abn0001117). PMID 42149475 / PMC13308188. The local copy is the HHS author manuscript, "available in PMC 2026 June 26." The DOI, PMID and PMCID are not printed in that manuscript and are taken from the Module 2 LifeData profile and the Module 3 ledger. |
| Study design | Prospective three-month EMA cohort at two sites, with machine-learning prediction of next-week suicide attempt (SA) and suicide-related event (SRE). 188 model architectures screened, then lasso and BiLSTM compared under Monte Carlo cross-validation. Harvard IRB18-1749 and Mass General Brigham 2019P001241. |
| Sample size (enrolled / analyzed) | 619 consented. 502 (81.1%) submitted at least one survey. 498 (80.5%) answered the affect items on at least one survey and form the most inclusive analysed sample (246 adults, 252 adolescents). 117 consented participants never submitted a survey. |
| Population | 313 adults (18 and over) presenting to a psychiatric emergency service and 306 adolescents (12 to 19) presenting to a psychiatric inpatient unit, at two Boston-area hospitals. All presented with suicidal thoughts and/or recent suicidal behaviour. Of the 498 analysed, mean age 23.1 (SD 18.0, range 12 to 69), 72.1% female at birth, 74.5% White, 29.1% with a past-month suicide attempt. 24.1% of the sample reported household income under $21,000 (income was not asked of adolescents, 50.6%). |
| Duration | 84 days of EMA at six prompts a day (12 weeks), followed by three months of one daily survey that this paper does not analyse. |
| Devices/platforms used | [LifeData](../../module-02-digital-phenotyping/profiles/lifedata.md) participant app on participant-owned iOS or Android phones. Surveys only. No phone sensors, no wearable. The "passively collected survey meta-data" in the abstract are response-timing features from the survey platform. First LifeData deployment in this module. |
| Funding/COI | NIMH U01MH116928, the Will & Chet Griswold Fund and the Fuss Family Research Fund. Nock reports publication royalties, paid consulting (Cambridge Health Alliance, OpenAI, legal cases concerning a death by suicide), stock options in Cerebral Inc., and unpaid advisory roles at Empatica, Koko, TalkLife and the JED Foundation. Picard is an Empatica shareholder. Smoller has options at Sensorium Therapeutics, consulting fees from Data Driven and Tempus, and grant support from Biogen. Donovan and spouse hold Artisan Industries stock and a Mirah investment. No author declares a relationship with LifeData. Compensation was $10 for the baseline survey and $1 per completed EMA survey. |
| Last verified | 2026-09-03 |

## Summary

The largest EMA-only cohort in this module and the first on LifeData. It is included for a funnel that most prediction papers leave out. Of 619 people who consented in a psychiatric emergency service or on an inpatient unit, 117 never submitted a single survey. The 502 who did started 79,448 surveys over 84 days. The authors then state that rolling survey initiation ran below 50% for the whole three months and fell over time. Adults contributed survey data on a mean of 43 of the 84 days (SD 33.2). Adolescents contributed on a mean of 40 days (SD 25.7). The standard deviations are as wide as the means, so the cohort held a large group who stopped early alongside a group who kept going.

This happened with payment per survey. The authors say so directly in the Limitations, and then call the approach feasible on the strength of the volume that remained. Both readings are fair. Nearly 80,000 surveys is enough to train a BiLSTM to an AUC of .94 for SREs and .90 for SAs when a participant's own earlier surveys are in the training set. Held-out participants drop to .80 and .75 for adults, and to .72 and .67 for adolescents.

The design choice that sets this apart from the earlier Nock-lab inpatient cohort, [Wang 2021](beiwe-inpatient-suicide-pilot.md), is where the surveys happen. Wang collected only during the hospital stay, on Beiwe and movisensXS, with loaner phones. Here the collection is after presentation, in the community, for 12 weeks, on participants' own phones, and the survey metadata that Wang found predictive is built into the feature set from the start.

## Instrumentation and Deployment Model

Bring your own device. Owning an Android or iOS smartphone was an inclusion criterion. No loaner phones are mentioned. Consent, a baseline survey and app installation happened at presentation. The paper does not say which LifeData product generation was used or name the researcher console.

Each survey had 20 items on a 0 to 10 slider, three on suicidal thinking (urge, intent, ability to resist) and 17 on affective states. Each item was prefaced with "Right now, how much do you feel..." and a brief definition. Six surveys a day. The first and last prompt of the day were at fixed times agreed with each participant at enrolment, for example 9am and 9pm. The middle four were randomised between them at least two hours apart. Participants could also open a user-initiated survey at any time to report a suicide attempt, non-suicidal self-injury or anything else they thought the team should know. The survey open window and expiry rule are not reported.

Notifications started as soon as a participant could reach their phone. For adults from the emergency service that was typically immediate. For adolescents it was after discharge from the inpatient unit. The paper does not give the mean delay for adolescents.

Compensation was $10 for the baseline survey and $1 per completed EMA survey. No bonus structure or payment cap is mentioned.

The team ran "detailed risk monitoring procedures to respond in real-time to surveys indicating high suicidal intent." The thresholds, staffing and response pathway are "available upon request" and not in the paper. Outcome events were coded from three sources, self-report in an EMA survey, documentation in an electronic health record clinical note (consensus coded by two BA-level reviewers under doctoral supervision), or a risk-monitoring interaction. Any reminder practice, technical support line or participant contact schedule beyond risk monitoring is not reported.

The eleven metadata features were prompt-to-start lag in minutes, start-to-submit time in minutes, whether a survey was completed but not submitted until the next prompt, days since the last survey on file, the count of extreme (0 or 10) responses, and six start-time features (daytime, weekend, holiday, day before holiday, minutes of daylight, and an inverted-cosine daylight curve). Three within-study SRE features were added, hospitalisation on the survey date, count of SREs since enrolment, and days since the last documented SRE.

## Recruitment and Retention

Recruitment was in hospital at presentation. The paper reports no approached, screened, eligible or declined counts. It states as a limitation that "there were differences in how adults and adolescents were recruited," without describing them. Exclusions were inability to consent or assent, inability to speak or write English fluently, gross cognitive impairment from florid psychosis, intellectual disability, dementia or acute intoxication, and extremely agitated or violent behaviour. No exclusion count is given.

| Stage | n |
|---|---|
| Approached or screened | not reported |
| Consented | 619 (313 adults, 306 adolescents) |
| Submitted at least one survey | 502 (81.1%) |
| Never submitted a survey | 117 (18.9%) |
| Answered the affect items on at least one survey (analysed) | 498 (80.5%), 246 adults and 252 adolescents |
| Formal withdrawals | not reported |

The 117 who consented and never started a survey are the clearest attrition figure. The paper does not say whether they withdrew, never installed the app, or installed it and ignored every prompt. It does not compare them clinically or demographically with the 502.

There is no retention definition and no completion-rate table. The two figures that stand in are the mean days with survey data, 43 (SD 33.2) for adults and 40 (SD 25.7) for adolescents out of 84, and the statement that rolling median and mean survey initiation rates were "<50% over the three-month study period and decreased over time (see Figure S1 in the Supplement)." Figure S1 is not included in the author manuscript, so the shape and endpoints of that decline cannot be read here. Attrition reasons are not reported.

## Data Completeness and Technical Issues

Completeness is counted in surveys, not participants. The 502 responders started 79,448 surveys. Between 1,856 and 5,710 started surveys were "discontinued such that they became unusable," depending on which items a given model required. The most inclusive analysed set is 77,592 surveys from 498 people. By site, 41,450 adult surveys and 37,998 adolescent surveys carried a prediction window.

Missingness was not imputed. It was modelled. BiLSTM was chosen as a "missing-enabled" sequence model that treats missingness as a predictor, and the authors offer that as one reason it outperformed lasso. Two metadata features carry the non-response signal into the lasso models as well. In the adult independent lasso for SAs (Table 2), a survey completed but not submitted until the next prompt had OR 1.05 (95% CI 0.99 to 1.52) and days since the last EMA had OR 1.00. Prompt lag and survey duration were also OR 1.00. Weekend submission was OR 0.87 (0.81 to 0.92) and daytime submission OR 1.10 (1.05 to 1.16). Extreme responses were OR 1.08 (1.02 to 1.11). Being in hospital on the survey date was OR 0.91 (0.41 to 1.06).

Outcome events also thinned in the funnel. 459 SAs or SREs were recorded among 193 participants over the study. Restricting to participants with any survey data left 372 events in 162 people. An event could only be matched to a prediction if a survey existed in the prior seven days, which left 170 matched events (85 SAs, 85 non-SA SREs) across 92 participants. Subtracting the paper's own counts, 87 of the 459 events occurred in people who never submitted a survey, and 202 of the 372 events among responders had no survey in the preceding week. The paper does not draw out these two figures itself.

No technical failure mode is reported. There is no mention of notification delivery, app crashes, OS updates, upload or sync problems, or vendor-side incidents. No iOS versus Android breakdown is given. Data collection dates are not stated. Battery and data-use impact are not discussed. The Module 2 [LifeData profile](../../module-02-digital-phenotyping/profiles/lifedata.md) records a Play Store complaint about notifications appearing to time out, which this paper neither confirms nor rules out.

## Feasibility Findings

The authors' own statement, from the Limitations, reads in full. "Second, there was a significant amount of missing data, even in the context of our paying participants for completing surveys, limiting the ecological validity of our findings and highlighting that the intensive longitudinal monitoring methods used will not be equally engaging to all participants. On balance, despite this level of missingness, we still had nearly 80,000 EMA datapoints. With those data, we were able to sufficiently engage most of this high-risk sample and to sustain their engagement long enough to build prediction models for this high-risk post-hospital period, supporting the feasibility of this approach."

They add that these participation rates came from a 20-item protocol and that "much of our predictive power came from a smaller set of features," so a briefer survey may raise engagement, citing Smyth 2021 and Eisele 2022. They also point to metadata as cheap added signal, since model accuracy generally improved when it was included. For the future they want passive physiological and behavioural streams (heart rate, accelerometry), call and text logs, and environmental events, none of which this deployment collected.

On the prediction side they note that models trained with a participant's own data included did much better than models applied to new participants, and that adolescent independent models were weak enough to suggest adolescents cannot be predicted well without their own data in training.

## Relevance to Future Study Design

Budget for a fifth of consented patients to produce nothing. Here 117 of 619 never submitted a survey, in a design with per-survey payment and in-person enrolment at the point of care. The paper cannot say why. A study that needs those people, for instance one whose outcome is concentrated among non-responders, should plan a contact step between consent and first prompt and record what happens at it.

Report initiation rate over time, not just total surveys. The 79,448 figure and the "<50% and declining" figure describe the same data and give opposite impressions. This paper puts the curve in a supplement that did not travel with the manuscript, and the mean-days figures (43 and 40 of 84) are the only numbers left.

Six prompts a day for 12 weeks at $1 each is a heavier and longer schedule than the other suicide-risk EMA deployments in this module. [Wang 2021](beiwe-inpatient-suicide-pilot.md) ran six a day for a mean of 6.9 inpatient days at $10 a day and reached 52.2% compliance. [Kivelä 2024](avicenna-ema-suicidal-ideation-iatrogenic.md) and [Spangenberg 2026](metricwire-post-discharge-ema-reactivity.md) are the comparison points for acceptability and reactivity questions this paper does not ask.

Treat survey metadata as a data stream and keep it. Prompt lag, submit lag, deferred submission and days since last survey cost nothing to collect on any EMA platform. Here the timing features were weak in the lasso (OR 1.00 to 1.05) but the missingness-aware BiLSTM was the best model, which is the same direction as [Wang 2021](beiwe-inpatient-suicide-pilot.md). Whether LifeData exports these fields is documented in the Module 2 profile.

Adolescents recruited on an inpatient unit start EMA only at discharge. The paper counts their 84 days from an unstated start and gives no discharge-to-first-prompt lag. A design that mixes emergency-service adults and inpatient adolescents has two different day-zero definitions.

Real-time risk monitoring was part of the deployment and part of the outcome ascertainment. Its cost and staffing are not in the paper. A team replicating this needs that protocol from the authors before it can price the study.

## Evidence Confidence

Verified. The consent count, the 502 and 498 counts and their percentages, the 117 non-responders by subtraction, the survey counts (79,448 and 77,592, 1,856 to 5,710 discontinued), the per-site survey and event counts, the mean days with data and SDs, the prompt schedule, the compensation amounts, the 20-item content, the eleven metadata features, the outcome funnel (459, 372, 170), the model performance figures, the Table 2 odds ratios, Table 1 demographics, the funding and disclosure statements, and the verbatim feasibility statement were all read from the HHS author manuscript PDF on 2026-09-03.

Reported. The initiation-rate claim ("<50%" and "decreased over time") rests on Figure S1 in the supplement, which is not part of the author manuscript. Only the authors' text description is available here.

Not in the manuscript. DOI, PMID and PMCID are carried from the ledger and the Module 2 profile, not read from the PDF. The published version may differ from the author manuscript.

Not assessed here. The prediction results are reported for context only. Whether LifeData captures the metadata fields the models used is a Module 2 question and the [LifeData profile](../../module-02-digital-phenotyping/profiles/lifedata.md) covers it.

Conflict note. No author declares any relationship with LifeData, and the platform is not evaluated or praised in the text. The declared interests concern Empatica, Cerebral, OpenAI, Sensorium, Tempus, Data Driven and Biogen, none of which supplied anything to this study. The missingness figures are unflattering and are reported anyway.

Scope note. Q113 in `shared/unresolved-questions.md` recorded this study as excluded from Module 3 only because LifeData had no Module 2 profile. That profile exists as of 2026-09-02, so the scope reason is closed and this profile resolves it.

## Key Links

- Paper: https://doi.org/10.1037/abn0001117
- Europe PMC: https://europepmc.org/article/PMC/PMC13308188
- Local PDF (HHS author manuscript): `../../module-02-digital-phenotyping/literature/lifedata/2026-nock-jpsychopatholclinsci-smartphone-surveys-predict-next-week-suicide-attempts.pdf` (held by Module 2; not duplicated)
- Supplement (Figure S1, Tables S1 to S5): on PubMed Central with the published article, not in the local manuscript

## Related profiles

- Platform: [LifeData](../../module-02-digital-phenotyping/profiles/lifedata.md)
- Earlier Nock-lab cohort, inpatient-only EMA on Beiwe and movisensXS with loaner phones: [`beiwe-inpatient-suicide-pilot.md`](beiwe-inpatient-suicide-pilot.md)
- Other suicide-risk EMA deployments: [`avicenna-ema-suicidal-ideation-iatrogenic.md`](avicenna-ema-suicidal-ideation-iatrogenic.md), [`metricwire-post-discharge-ema-reactivity.md`](metricwire-post-discharge-ema-reactivity.md), [`metricwire-sgm-youth-ema-feasibility.md`](metricwire-sgm-youth-ema-feasibility.md), [`mpath-nssi-ema-benefits-challenges.md`](mpath-nssi-ema-benefits-challenges.md)
- Missingness as signal rather than nuisance: [`beiwe-inpatient-suicide-pilot.md`](beiwe-inpatient-suicide-pilot.md), [`beiwe-missing-data-sociodemographic.md`](beiwe-missing-data-sociodemographic.md)
- Financial incentives and survey engagement: [`beiwe-spinal-cord-injury-incentives.md`](beiwe-spinal-cord-injury-incentives.md)
- Adolescent EMA engagement: [`beiwe-adolescent-feasibility.md`](beiwe-adolescent-feasibility.md), [`avicenna-smoking-youth-ema-compliance.md`](avicenna-smoking-youth-ema-compliance.md)

## Sources

1. Nock MK, Kleiman EM, Bentley KH, et al. *Journal of Psychopathology and Clinical Science* 2026. DOI 10.1037/abn0001117. HHS author manuscript (PMC13308188) read in full, including Tables 1 and 2 and the figure captions, from the local PDF on 2026-09-03. Establishes every figure in this profile. Supplement not read.
2. Module 3 screening extraction, `../_screening-reports/2026-09-03-batchE.md`, paper 7. Used only for cross-checking; every number was re-read from the manuscript.
