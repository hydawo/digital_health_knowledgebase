# Wang et al. 2021 — Inpatient EMA of suicidal thinking to predict post-discharge suicide attempts, N=83

## Quick Facts

| Field | Details |
|---|---|
| Citation | Wang SB, Coppersmith DDL, Kleiman EM, Bentley KH, Millner AJ, Fortgang R, Mair P, Dempsey W, Huffman JC, Nock MK. "A Pilot Study Using Frequent Inpatient Assessments of Suicidal Thinking to Predict Short-Term Postdischarge Suicidal Behavior." *JAMA Network Open* 2021;4(3):e210591. DOI [10.1001/jamanetworkopen.2021.0591](https://doi.org/10.1001/jamanetworkopen.2021.0591). PMC7944382. |
| Study design | Prognostic study, TRIPOD-reported; elastic-net prediction models with 5-fold cross-validation, 3 repetitions. Two recruitment waves pooled. |
| Sample size (enrolled / analyzed) | **104 enrolled → 83 (79.8%) completed ≥3 EMA surveys and were analyzed.** Only **65 of 83** completed a follow-up survey. **9 (10.8%) made a suicide attempt** in the month after discharge. |
| Population | Adults admitted to the **inpatient psychiatric unit at Massachusetts General Hospital** for suicidal thoughts and/or risk. Mean age 38.4 (SD 13.6); 51.8% male; **83.1% White**. |
| Duration | EMA for the hospital stay — **mean 6.9 days (SD 5.4), range 2–46**; follow-up at 2 and 4 weeks post-discharge. Data collected Jan 2016 – Dec 2018. |
| Devices/platforms used | **Wave 1: movisensXS** (4 prompts/day). **Wave 2: [Beiwe](../../module-02-digital-phenotyping/profiles/beiwe.md)** (6 prompts/day, for greater temporal granularity). **Loaner phones provided** where needed. |
| Funding/COI | Academic (Harvard, Rutgers, MGH, Michigan, Franciscan Children's). Kleiman reports NIMH grants outside this work; Huffman reports salary support from Elsevier outside this work. |
| Last verified | 2026-08-31 |

## Summary

Included here for one finding that inverts how this entire module treats missing data: **survey
non-completion was itself among the strongest predictors of post-discharge suicide attempts.**

Adding **percentage missingness as a predictor** raised cross-validated AUC from 0.81 to **0.93** for
the mean model and from 0.89 to **0.93** for the dynamic-features model. Missingness was the **most
important predictor in the mean model** and the **second most important in the dynamic-features
model**.

Every other profile in Module 3 treats missing data as a nuisance to be minimised, imputed, or
apologised for. This study treats it as signal — and it turns out to carry more information than
most of the content being measured. The mechanism the authors propose is mundane and plausible:
participants likely did not respond when meeting their care team **or when highly distressed**.

The operational context matters: **overall EMA compliance was only 52.2%**, in a supervised inpatient
setting, with $10/day compensation, over a mean stay of under 7 days. That is the lowest active-data
compliance of any study in this module, and it produced the best prediction.

## Instrumentation and Deployment Model

**Provisioned where needed** — having a compatible smartphone was explicitly **not** an inclusion
criterion; **loaner phones were provided**. In a population defined by acute psychiatric
hospitalisation, this removes the BYOD selection filter that shapes most of the other profiles here.

**Two waves, different software** (protocols otherwise identical, data pooled):

| Wave | Dates | N | Platform | Prompts/day |
|---|---|---|---|---|
| 1 | Jan 2016 – Jan 2017 | 45 | **movisensXS** | 4 semirandom |
| 2 | May 2017 – Dec 2018 | 59 | **Beiwe** | 6 semirandom |

**EMA content** — three items, each 0 (none) to 9 (very much), delivered during waking hours:

1. Desire to die by suicide ("How intense is your desire to kill yourself right now?")
2. Intent to die by suicide
3. Ability to resist the urge to die by suicide

**Compensation: $10 per day.**

**Inclusion:** admission for suicidal thoughts and/or risk, English fluency. **Exclusion:** anything
impairing capacity to consent or participate (e.g. cognitive impairment).

## Recruitment and Retention

| Stage | N |
|---|---|
| Enrolled | 104 |
| **Analyzed (≥3 EMA surveys completed)** | **83 (79.8%)** |
| Completed a post-discharge follow-up survey | **65 of 83** |
| Made a suicide attempt in the month after discharge | 9 (10.8%) |

The **≥3-survey inclusion threshold excluded 21 enrolled participants (20.2%)** — a filter worth
noting, since it removes precisely the lowest-engagement participants from a study whose headline
finding is that low engagement predicts risk.

**Follow-up attrition is the more serious gap: 18 of 83 (21.7%) never completed a follow-up survey**,
and the authors flag this explicitly as a limitation.

## Data Completeness and Technical Issues

**Overall EMA compliance: mean 52.2%.** Median **18.5 EMA responses** per participant (range 3–120),
across **more than 1,300 individual observations** in total.

The wide range reflects the **intentionally naturalistic design** — participants completed prompts
only for the duration of their hospital stay, which varied from 2 to 46 days.

**The authors are explicit that missingness was very likely not at random**, proposing that
participants did not respond **when meeting members of their care team** or **when highly
distressed**. That second mechanism is what makes missingness predictive.

**Missingness as a predictor — the core result:**

| Model | AUC (first–third quartile) | With missingness added |
|---|---|---|
| Baseline (20 SITBI characteristics) | 0.71 (0.55–0.88) | — |
| Mean of real-time suicidal thoughts | 0.81 (0.67–0.91) | **0.93 (0.90–1.00)** |
| **Dynamic changes in real-time suicidal thoughts** | **0.89 (0.81–0.97)** | **0.93 (0.88–1.00)** |

Features capturing **rapid fluctuations in suicidal thinking** were the strongest content predictors;
**missingness ranked first (mean model) and second (dynamic model)** overall.

## Feasibility Findings

The study's stated conclusion concerns prediction, not logistics: real-time data collection during
hospitalisation **significantly improved short-term prediction** of post-hospitalisation suicide
attempts, with dynamic-change features performing best — and **"survey noncompletion also emerged as
an important predictor."**

For Module 3's purposes the transferable findings are:

- **52.2% compliance is workable for a prediction model** if the sampling is dense enough. Density
  and duration can substitute for per-prompt compliance.
- **Providing loaner phones removes a selection filter** that would otherwise be severe in an acute
  psychiatric population.
- **Missingness should be modelled, not just minimised**, in populations where non-response
  plausibly correlates with the state being measured.

## Relevance to Future Study Design

1. **Retain and analyse compliance metadata as a predictor, not just a quality metric.** This is the
   single most actionable idea in this profile and it generalises anywhere non-response may covary
   with the outcome — pain, mood, fatigue, relapse, acute deterioration.
2. **State whether missingness is plausibly MNAR, and say why.** Contrast
   [de Angel et al.](radar-base-treatment-engagement.md), who note that missing data may equally
   reflect software error, and call for mapping technical failures to missingness. Both are true, and
   distinguishing them determines whether missingness is signal or noise.
3. **Provide loaner devices in acute clinical populations.** It cost this study its BYOD selection
   bias and made the cohort more representative of the ward.
4. **Beware inclusion thresholds that delete your lowest-engagement participants** when engagement is
   itself informative. The ≥3-survey rule removed 20% of those enrolled.
5. **Dense short-burst EMA works where long protocols would not.** 4–6 prompts/day for a mean of
   6.9 days produced 1,300+ observations.
6. **Follow-up is the weak link in inpatient-to-community studies** — 21.7% never completed any
   post-discharge survey, in a population where the outcome occurs after discharge.

## Evidence Confidence

**Verified** for the enrolment and analysis counts, compliance rate, response distributions, AUC
figures and predictor rankings — primary reported results read from the full text.

**Pilot-scale, and the authors lead their limitations with it:** **83 participants, 9 outcome events,
83.1% White.** Suicide attempts are a low-base-rate outcome, and AUCs estimated from nine events
carry wide uncertainty — visible in the quartile ranges (e.g. 0.81–0.97 for the dynamic model). The
authors call for larger, more diverse samples and longer follow-up. **Do not treat the 0.93 AUC as a
validated performance estimate**; it is a promising pilot result requiring external validation.

**Limitations the authors state:** small and predominantly White sample; **only self-reported
measures of suicidal thoughts and urges** (they suggest adding psychophysiological and passive
smartphone data — accelerometer, heart monitor — in future work); relatively few observations for
some participants (median 18.5, range 3–120); **overall compliance relatively low at 52.2%** with
many responses likely not missing at random; and only 65 of 83 completing follow-up.

**Platform heterogeneity to note:** wave 1 used **movisensXS** and wave 2 used **Beiwe**, at
different prompt frequencies (4 vs 6/day), and the waves were **pooled**. Compliance and response
figures are therefore a blend of two platforms and two sampling schedules, and **this study cannot
speak to either platform's performance individually.** My discovery pass initially tagged this study
as Beiwe + Empatica; that was incorrect — **no Empatica device was used** — and the record has been
corrected here. movisensXS is not profiled in Module 2; flagged as an expansion candidate in
[`../_inventory-and-scope-decisions.md`](../_inventory-and-scope-decisions.md).

## Key Links

- Paper (OA, CC-BY): https://doi.org/10.1001/jamanetworkopen.2021.0591
- Europe PMC: https://europepmc.org/article/PMC/PMC7944382
- **PDF not obtained** — the JAMA-family PMC route served HTML rather than a PDF. Full text was read
  from the NCBI PMC XML deposit. Logged as Tier 14 Q110 in
  `../../shared/unresolved-questions.md`.

## Related profiles

- Platform: [Beiwe](../../module-02-digital-phenotyping/profiles/beiwe.md)
- Missingness as nuisance vs missingness as signal:
  [`beiwe-missing-data-sociodemographic.md`](beiwe-missing-data-sociodemographic.md),
  [`radar-base-treatment-engagement.md`](radar-base-treatment-engagement.md)
- Early completeness predicting later adherence:
  [`beiwe-als-adherence.md`](beiwe-als-adherence.md)

## Sources

1. Wang SB, et al. *JAMA Netw Open* 2021;4(3):e210591. DOI 10.1001/jamanetworkopen.2021.0591. Full
   text read from the NCBI PMC XML deposit (PMC7944382), 2026-08-31. Establishes every figure in this
   profile.
