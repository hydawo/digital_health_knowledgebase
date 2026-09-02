# Borelli et al. 2025 — mSavorUs companion: passive-stream completeness for the AWARE + Oura + Samsung cohort, N=28

> **⚠ Same cohort as [`aware-msavorus-loneliness-multidevice.md`](aware-msavorus-loneliness-multidevice.md) (Nguyen et al. 2025).** These are two papers on one deployment, not two independent observations. Do not count them separately in any tally, and do not treat their figures as replication. This profile exists because it supplies the passive-stream completeness numbers the Nguyen profile explicitly records as its biggest gap.

## Quick Facts

| Field | Details |
|---|---|
| Citation | Borelli JL, Wang Y, Li FH, Russo LN, Tironi M, Yamashita K, Zhou E, Lai J, Nguyen B, Azimi I, Marcotullio C, Labbaf S, Jafarlou S, Dutt N, Rahmani A. "Detection of Depressive Symptoms in College Students Using Multimodal Passive Sensing Data and Light Gradient Boosting Machine: Longitudinal Pilot Study." *JMIR Formative Research* 2025;9:e67964. DOI [10.2196/67964](https://doi.org/10.2196/67964). PMID 40460426 / PMC12174877. |
| Study design | Machine-learning analysis (LightGBM + SHAP) of a longitudinal pilot that embedded a randomised relational-savoring intervention. **Secondary analysis of an already-profiled cohort.** |
| Sample size (enrolled / analyzed) | **37 enrolled → 10 withdrew → 28 analyzed** (Nguyen reports 29 for its own analytic sample from the same 37). |
| Population | Undergraduates aged 18–22 at a large West Coast US university (UC Irvine). Mean age 19.96 (SD 1.23); 54% women. **46% Latine, 36% Asian, 14% White, 4% other** — one of the module's few non-White-majority cohorts. Excluded: parents, married students, returners, non-fluent English speakers, and **anyone currently meeting criteria for depression**. |
| Duration | **≥19 weeks (4.5 months)** per participant: 6 weeks monitoring → 4 weeks randomised monitoring-only vs. intervention → ≥9 weeks monitoring-only. |
| Devices/platforms used | **[AWARE](../../module-02-digital-phenotyping/profiles/aware-framework.md)** (passive smartphone) + **[Oura](../../module-01-wearables/profiles/oura.md) Ring** + **[Samsung](../../module-01-wearables/profiles/samsung.md) Gear Sport smartwatch** + a separate survey app + the mSavorUs intervention app. Wearables provisioned; phone BYOD. |
| Funding/COI | Academic (UC Irvine). Co-author **Amir Rahmani is credited elsewhere in this cohort's reporting as the developer of both mSavorUs and the AWARE deployment** — see the Nguyen profile. This paper carries no explicit competing-interests statement addressing that relationship. |
| Last verified | 2026-09-02 |

## Why this profile exists

The Nguyen 2025 profile closes with an unusually blunt gap statement:

> "**Wearable wear time and Oura/Samsung data completeness are not reported.** This is the profile's biggest gap: a 22-week two-wearable deployment that does not publish wear-time or device-yield figures cannot be used as evidence about either device's adherence characteristics."

Borelli 2025 publishes those figures for the same deployment:

> **Smartphone-based passive sensing data: 16% average missing rate. Wearable-derived physiological data: 11% average missing rate.**

Three further things this paper adds that its companion does not: an **Android-only eligibility criterion**, an **itemised list of missingness mechanisms**, and the finding that **wearable non-wear time was among the five strongest predictors of depressive symptoms** — missingness behaving as signal rather than noise.

## Establishing that this is the same cohort

**Verified.** Same institution and author group; same 37 enrolled; same three-phase monitoring/intervention/monitoring structure; same relational-savoring intervention; same device stack (Oura Ring + Samsung Gear Sport + AWARE + a survey app); mean age 19.96 vs Nguyen's 19.93. Borelli's Methods refers the reader to "Nguyen et al [unpublished data, 2024]" for the intervention design — that manuscript is the paper published as Nguyen et al. 2025, *JMIR Form Res* 9:e70528 (PMC12518887).

**Two bibliographic discrepancies between the papers, unresolved:**

| Item | Nguyen 2025 | Borelli 2025 |
|---|---|---|
| Enrolment window | late Jan – early Feb **2021** | Jan – Feb **2022** |
| Duration | 22 weeks | **≥**19 weeks (4.5 months) |
| Analytic N | 29 | 28 |
| Race/ethnicity | 43.3% Latinx / 43.3% Asian American / 17.2% White | 46% Latine / 36% Asian / 14% White / 4% other |

The N and demographic differences are consistent with one participant differing between analytic samples. **The enrolment-year discrepancy is a genuine conflict and one of the two papers is wrong**; neither can be resolved from the published texts. It matters for interpretation — a Jan–Feb 2021 start places the whole monitoring period inside California's COVID-19 restrictions, which is how the Nguyen profile reads it, while a 2022 start does not. Recorded here rather than silently resolved, per this project's source-conflict rule.

## Instrumentation and Deployment Model

**Android-only eligibility.** Participants had to be "fluent in English and used an **Android smartphone with an operating system of 6.0 or higher**." This is the module's second Android-only platform requirement after [RADAR-MDD](radar-mdd-recruitment-retention.md), where the equivalent constraint **caused 11% of withdrawals**. Borelli reports no equivalent figure — the requirement here operated at screening, so anyone with an iPhone never entered the funnel and is invisible. In a US undergraduate population, where iPhone share among 18–24-year-olds is high, this is a substantial and unmeasured selection.

It also means **this cohort contributes nothing to the module's iOS/Android question** — it has no iOS arm by construction. That is worth stating plainly, because a five-month AWARE + two-wearable deployment looks like it should.

**Instrument load:** one ring, one smartwatch, two chargers, and four apps (AWARE, the daily/weekly survey app, mSavorUs, plus the Oura and Samsung companion apps — five if the vendor apps are counted separately). Research assistants asked participants to keep devices on "as much as possible unless charging or engaging in any intense activity (eg, sports) that might damage the devices" — an instruction that builds a non-wear window into the protocol.

**Sampling:** the Samsung Gear Sport collected **raw PPG for 12 minutes every 2 hours** via green LED; Oura supplied nightly sleep, HR, HRV and activity; watch features were extracted at **one value every 5 minutes** and reduced to daily slope, intercept, SD and mean. AWARE supplied calls, messages, notifications, screen activity and location, with location features computed over a **5-day window**.

**Compensation: US $30 to $660 depending on components completed.** The upper figure is among the largest per-participant payments in this module — comparable to [Soon 2025](oura-university-freshmen-sleep.md)'s ~USD 263 and well above the four movie tickets in [MoMo-Mood](aware-momo-mood-mood-disorders.md). It did not prevent 27% attrition.

## Recruitment and Retention

- **37 enrolled → 10 withdrew (27.0%) → 28 analysed.** No reasons for withdrawal are given in this paper; the companion attributes exactly one withdrawal to technical burden and leaves the rest unattributed.
- Recruitment was by **flyers and campus announcements**. No screening funnel is published — the number approached, screened out for not having an Android phone, or screened out for currently meeting depression criteria is not reported.
- **Active-survey completeness is very high**: after three months of monitoring there were **355 valid weekly PHQ-9 submissions and 4 missed** — a **98.9% completion rate** on the weekly outcome measure, monitored by the clinically-trained first author. Note this is the *weekly* instrument; the companion paper's *EMA* adherence over the same deployment falls from 79% to 69%. **Two active streams in one study, 30 points apart, because one is weekly and supervised and the other is high-frequency and automated.**

The retention framing in the Discussion is worth quoting for its selectivity: "participants in this study had **high rates of adherence** to study protocols—although some participants dropped out at the outset of the study, participants who continued with the study provided consistent data streams." That is a conditional-on-completion claim about a cohort that lost 27%, and it is exactly the retention-versus-completeness elision this module tracks.

## Data Completeness and Technical Issues

**Definitions used:**

- *Missing rate* — **"missing data percentages across participants"** for each data source, averaged. The paper does not state the denominator (expected samples? enrolled days? post-imputation rows?), which limits comparability. Treat these as order-of-magnitude figures.
- *PHQ-9 completion* — valid submissions vs missed, at the weekly level.
- Missing values were classified **missing completely at random**, on the argument that occurrence was independent of the depression scale. Given that non-wear time turned out to be one of the strongest predictors of depressive symptoms in the same paper, **this MCAR claim is in tension with the paper's own result** and should not be carried forward.

**Figures:**

| Stream | Average missing rate |
|---|---|
| Smartphone passive sensing (AWARE) | **16%** |
| Wearable-derived physiological data (Oura + Samsung) | **11%** |
| Weekly PHQ-9 | **1.1%** (4 missed of 359) |

**The wearables outperformed the phone.** An 11% wearable miss rate against 16% for smartphone passive sensing, on the same participants over the same months, is the reverse of the ordering most study designers assume (phones are always with you; rings and watches get taken off). It is consistent with [cross-cutting pattern 2](../feasibility-matrix.md) only if one treats the AWARE stack's background-execution and permission dependencies as the higher-demand component — which the authors' own failure list supports.

**Named missingness mechanisms**, split by the authors into two classes:

| Class | Mechanisms named |
|---|---|
| Human | forgetting to charge the devices; removing the wearables during daily activities |
| **Technical** | **interruption of data collection due to server congestion**; **permission allowance on the phone** |

**"Server congestion" is a research-infrastructure failure, not a participant or device failure**, and this module has recorded it explicitly only once before. It is the class of loss that a self-hosted deployment owns entirely and a managed SaaS deployment does not — a live consideration in any [Module 2 hosting decision](../../module-02-digital-phenotyping/profiles/aware-framework.md). "Permission allowance on the phone" is the familiar Android runtime-permission revocation problem, and is the mechanism the Nguyen companion observed as AWARE "not being received" on at least two occasions.

**PPG quality handling reveals a further, unquantified loss layer.** Raw PPG was passed through a signal-quality-assessment stage classifying segments clean or noisy; noisy segments under 15 seconds were **reconstructed with a generative adversarial network**, and longer unreliable segments were removed. **The proportion of PPG classified noisy, reconstructed, or discarded is not reported.** So the 11% wearable figure sits on top of an unmeasured within-signal quality loss, and some of the surviving data is synthetic. This is a distinct failure category from [Bladon 2026](connect-multi-wearable-psychosis.md)'s present-but-corrupt Samsung sleep records, but it lands in the same place: **presence is not quality**, and here quality was repaired rather than reported.

**Imputation:** nearest-previous-value carried forward for continuous physiological and smartphone data; **EMA responses deliberately not imputed** "to maintain the integrity of self-reported measures." That asymmetry is good practice and worth copying.

**Non-wear time as a predictor.** In the combined-group SHAP analysis, the five most influential features were average sleep breathing rate, missed call counts, resting minutes, **non-wear time of wearable devices**, and lifestyle-app notification counts. A missingness variable ranked fourth out of 1,000+ features for predicting depressive symptoms. This reproduces [Wang 2021](beiwe-inpatient-suicide-pilot.md)'s finding — survey non-completion outranking most content features for suicidal-ideation prediction — on a *passive* stream in a *non-clinical* cohort. **Two independent instantiations now; this is no longer a one-study curiosity.**

## Feasibility Findings

The paper's own feasibility claims are thin and partly self-contradictory (see the "high rates of adherence" quote above). The transferable findings are the ones the authors report as methods rather than conclusions:

1. A **19-week, three-device, four-app deployment in undergraduates is sustainable at roughly 73% retention and 84–89% passive completeness**, with payment up to $660 and weekly supervised outcome collection.
2. **The weekly supervised instrument achieved 98.9%; the automated high-frequency instruments did not.** Frequency and supervision, not the participants, explain the difference.
3. **Server-side capacity is a data-loss mechanism a study team can actually fix**, unlike participant charging behaviour.

## Relevance to Future Study Design

1. **Read this paper alongside Nguyen 2025, never instead of it.** One deployment, split across an intervention-outcomes paper and an ML paper, with the operational figures distributed between them. The module's practice of profiling a technology once per study needs an exception for split reporting, and this is that exception.
2. **Expect the wearable to beat the phone on completeness, not the other way round** — at least for a provisioned ring and watch against a BYOD Android AWARE build. 11% vs 16% here.
3. **Report noisy/discarded/reconstructed proportions for raw physiological signals.** An 11% missing rate on top of an unreported PPG-quality loss, some of it GAN-reconstructed, is not an 11% data-quality figure.
4. **Android-only eligibility silently rewrites your sample and your OS evidence.** Record how many people were screened out by it — RADAR-MDD's 11%-of-withdrawals figure exists only because that study looked.
5. **Do not assert MCAR when your own model finds missingness predictive.** The non-wear-time SHAP result and the MCAR classification cannot both be right.
6. **Large payments do not buy retention.** Up to $660 and 27% still withdrew, consistent with the module's incentive pattern.
7. **Weekly-and-supervised beats high-frequency-and-automated for outcome completeness** — 98.9% vs 69%. If the primary endpoint can be weekly, make it weekly.

## Evidence Confidence

**Verified** — the same-cohort identification (via Borelli's own citation of the Nguyen manuscript plus matching design, N, devices and demographics); the 37/10/28 flow; the Android 6.0+ eligibility criterion; the ≥19-week three-phase structure; the 16% smartphone and 11% wearable missing rates; the 355-valid / 4-missed PHQ-9 counts; the $30–$660 compensation range; the four named missingness mechanisms; the PPG SQA/GAN-reconstruction pipeline; the MCAR classification; the imputation asymmetry; and non-wear time's position in the combined-group top-five features. Read from the full text (Europe PMC PMC12174877), 2026-09-02.

**Unclear** — the denominator behind the 16% and 11% figures; the proportion of PPG classified noisy, reconstructed or discarded; reasons for the 10 withdrawals; the screening funnel, including how many were excluded for not owning an Android phone; and which of the two papers has the correct enrolment year.

**Conflicting sources** — enrolment year (2021 per Nguyen, 2022 per Borelli) and duration (22 weeks vs ≥19 weeks) for the same deployment. Both recorded; neither resolved. Per this project's standard, no silent choice has been made between them.

**Small-sample caution.** N=28 analysed, one university, one department's participant pool, Android users only, and people currently meeting depression criteria were **excluded** — so the depression-detection target is subclinical variation (mean PHQ-9 4.90, SD 4.25) dichotomised at >4. The completeness figures are pilot-scale and single-site.

**COI:** the sensing deployment and the intervention app are attributed in the companion paper to co-author Amir Rahmani. This paper contains no competing-interests statement addressing that. The completeness figures reported here are not flattering, which limits the exposure, but the "high rates of adherence" characterisation of a 27%-attrition cohort is the authors' own.

## Key Links

- Paper (OA, CC BY): https://doi.org/10.2196/67964
- Europe PMC: https://europepmc.org/article/PMC/PMC12174877
- Companion paper (same cohort): https://doi.org/10.2196/70528
- Local PDF: `../literature/2025-borelli-jmirformres-multimodal-passive-sensing-college-depression.pdf`

## Related profiles

- **Same cohort:** [`aware-msavorus-loneliness-multidevice.md`](aware-msavorus-loneliness-multidevice.md)
- Platform: [AWARE](../../module-02-digital-phenotyping/profiles/aware-framework.md)
- Devices: [Oura](../../module-01-wearables/profiles/oura.md), [Samsung](../../module-01-wearables/profiles/samsung.md)
- Missingness as signal: [`beiwe-inpatient-suicide-pilot.md`](beiwe-inpatient-suicide-pilot.md), [`aware-alcohol-liver-disease-craving.md`](aware-alcohol-liver-disease-craving.md)
- Android-only platform requirement causing loss: [`radar-mdd-recruitment-retention.md`](radar-mdd-recruitment-retention.md)
- Presence is not quality: [`connect-multi-wearable-psychosis.md`](connect-multi-wearable-psychosis.md), [`empatica-epilepsy-data-quality.md`](empatica-epilepsy-data-quality.md)
- Payment does not buy retention: [`beiwe-spinal-cord-injury-incentives.md`](beiwe-spinal-cord-injury-incentives.md), [`oura-university-freshmen-sleep.md`](oura-university-freshmen-sleep.md)

## Sources

1. Borelli JL, Wang Y, Li FH, Russo LN, Tironi M, Yamashita K, Zhou E, Lai J, Nguyen B, Azimi I, Marcotullio C, Labbaf S, Jafarlou S, Dutt N, Rahmani A. *JMIR Form Res* 2025;9:e67964. DOI 10.2196/67964. Full text read from Europe PMC (PMC12174877), 2026-09-02. Byline verified against the publisher PDF (PMC JATS lists the handling editor and peer reviewer in separate contrib-groups after the authors). Establishes every figure in this profile.
2. Nguyen B, et al. *JMIR Form Res* 2025;9:e70528. DOI 10.2196/70528. Used here only to establish cohort identity and the conflicting enrolment window; see [`aware-msavorus-loneliness-multidevice.md`](aware-msavorus-loneliness-multidevice.md).
