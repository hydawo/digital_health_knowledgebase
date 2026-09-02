# Wu et al. 2023 — AWARE in alcohol-associated liver disease with alcohol use disorder, N=24 over 30 days

## Quick Facts

| Field | Details |
|---|---|
| Citation | Wu T, Sherman G, Giorgi S, Thanneeru P, Ungar LH, Kamath PS, Simonetto DA, Curtis BL, Shah VH. "Smartphone sensor data estimate alcohol craving in a cohort of patients with alcohol-associated liver disease and alcohol use disorder." *Hepatology Communications* 2023;7(12):e0329. DOI [10.1097/HC9.0000000000000329](https://doi.org/10.1097/HC9.0000000000000329). PMID 38055637 / PMC10984664. |
| Study design | Prospective observational **pilot** with feasibility as an explicit stated aim alongside craving-correlate discovery and effect-size estimation for future power analysis. STROBE-reported. |
| Sample size (enrolled / analyzed) | **163 screened → 24 enrolled (14.7%) → 12 completed all study components (50% retention).** Analytic sub-samples are smaller still: 17 had sensor data linkable to 90-day outcomes; 8 had ≥2 days of craving-score change. |
| Population | Adults with alcohol-associated liver disease (ALD) **and** alcohol use disorder (AUD), Mayo Clinic Rochester, inpatient and outpatient. Median age **49 (IQR 39.8–57.3)**; 70.8% male; **83.3% White**; **62.5% decompensated cirrhosis**; 54.2% history of alcohol-associated hepatitis; median MELD 10.5; median AUDIT 25; median 97 days of abstinence before enrolment. |
| Duration | **30 days** of collection per participant, plus 90-day clinical-outcome follow-up after last contact. Recruited September 2021 – July 2022. |
| Devices/platforms used | **[AWARE](../../module-02-digital-phenotyping/profiles/aware-framework.md)** only — passive sensing (11 sensor streams) plus AWARE-delivered daily EMA. Feature extraction via **RAPIDS**. Keystroke de-identification via spaCy. BYOD smartphone. |
| Funding/COI | NIH/NIDA Intramural Research Program; Mayo Clinic Division of Gastroenterology and Hepatology Innovation Award; T32 DK07198 (TW). **No AWARE-developer authorship** — unusually for this module's AWARE set, the platform was used at arm's length. Simonetto consults for Mallinckrodt and BioVie (unrelated). |
| Last verified | 2026-09-02 |

## Summary

The module's **first AWARE deployment in a physically ill, non-psychiatric clinical population**, and one of its most useful small studies because it is unusually candid about a bad result: **a 14.7% enrolment rate and a 50% retention rate**, with the failure modes itemised participant by participant.

Two findings should change how a study team plans an ALD/AUD or comparable clinical digital-phenotyping deployment.

**First, the platform itself was the leading named cause of withdrawal.** Of the 12 non-completers, **5 withdrew citing technical problems with the AWARE application** — three said it interfered with other phone functions and was burdensome, one lost cellular service, one could not complete installation after repeated attempts. Only 2 withdrew from loss of interest. This is the most explicit attribution of dropout to the sensing app in this module; most studies report withdrawal reasons as "participant burden" without separating app defects from study burden.

**Second, attrition was informative with respect to the clinical outcome even though baseline characteristics predicted nothing.** No baseline demographic, disease, behavioural or psychological variable distinguished completers from non-completers — the same null this module has now reproduced across five studies. But **90-day alcohol relapse ran 16.7% among those completing 20 days of EMAs versus 57.1% among those completing none** (4 of 7), and ED admission/hospitalisation 33.3% versus 57.1%. The people who stopped supplying data were the people who got worse. Any analysis of this cohort that conditions on completeness is conditioning on the outcome.

There is also a clean **OS-stratified passive-yield figure**: participants on Android supplied a mean of **8.4 sensor types**, participants on iOS **4.7** — Android roughly 1.8× iOS on *breadth of passive streams delivered*.

## Instrumentation and Deployment Model

**Pure BYOD.** Owning a smartphone with cellular data and Wi-Fi was an eligibility criterion; no devices were provided. Participants installed AWARE at an in-person or video initial visit, were asked to keep it running in the background for 30 days, and were told to uninstall it at the follow-up visit.

**One app carried both streams.** Unlike [McClaine et al. 2024](aware-chemotherapy-engagement.md), which split passive sensing (AWARE) from surveys (MoSHI Surveys), here AWARE delivered the EMA as well. Daily EMAs were pushed at **18:00 with a 3-hour response window** — a single fixed prompt, not a participant-chosen time. Content: the 3-item Brief Alcohol Craving Scale, standard drinks and other substance use in the past 24 hours, and 11 mood items on a 5-point scale.

**Eleven passive sensor streams** were collected. The three most commonly available across participants were **accelerometer, screen and Wi-Fi network**. Keystroke data were captured and automatically de-identified server-side with spaCy — an unusual inclusion for a clinical study and a design point worth noting for IRB planning.

**Monitoring apparatus.** Staff were alerted if a participant missed EMAs for **≥3 consecutive days** and then contacted them by text or phone. Participants could call staff for help. Anyone who stopped transmitting AWARE data or answering EMAs was classed as lost to follow-up. This is a lighter-touch version of McClaine's three-times-weekly dashboard review, and it produced substantially worse retention in a sicker population.

**Incentives:** $30 per visit (initial and follow-up), **$1 per daily EMA**, plus a **$10 bonus at 80% EMA completion** — roughly $100 maximum over 30 days. The per-EMA-plus-threshold-bonus structure did not prevent a 50% retention rate, consistent with this module's [pattern 8](../feasibility-matrix.md): incentives buy persistence, not engagement.

## Recruitment and Retention

**The funnel:**

| Stage | n | % |
|---|---|---|
| Approached/screened | 163 | — |
| Enrolled | **24** | **14.7%** |
| Not enrolled | 139 | 85.3% |
| — not interested | 98 | 70.5% of decliners |
| — **incompatible technology** | **22** | **15.8% of decliners** |
| — stopped responding before enrolment | 19 | 13.7% of decliners |
| Completed all study components | **12** | **50% of enrolled** |

**14.7% is the lowest enrolment rate in this module for a study without a multi-vendor confirmatory protocol.** It is not a funnel-attrition artefact of the kind [Apple Heart](apple-heart-data-management-lessons.md) and [Fitbit Heart](fitbit-heart-study-afib.md) document — it is straightforward refusal at first approach, in a stigmatised condition.

**Device incompatibility removed 22 of 163 people (13.5% of everyone approached) before consent.** That is the same pre-consent gate [Camargo 2025](aware-light-smartsense-d-youth-depression.md) measured at 29% and [Cote 2019](beiwe-spine-disease-mobility.md) at 42%, arriving here through app compatibility rather than device ownership. The authors expect this barrier to shrink as app coverage improves — an expectation, not a finding.

**Withdrawal reasons for the 12 non-completers, as itemised:**

| Reason | n |
|---|---|
| Technical issues with the AWARE application | **5** |
| — interfered with other phone functions / burdensome | 3 |
| — lost cellular service after enrolment | 1 |
| — could not install despite repeated attempts | 1 |
| Lost contact despite staff follow-up | 4 |
| Lost interest | 2 |
| Died (decompensated cirrhosis, before any EMA) | 1 |

(Totals to 12.)

**Completers versus non-completers: no significant difference on any measured baseline characteristic** — demographics, disease stage, MELD, AUDIT, insight, readiness to change, depression, anxiety, stress, resilience, social support or self-efficacy. The authors draw the conclusion that dropout risk "may not be attributed to such factors."

## Data Completeness and Technical Issues

**Definitions used (state them beside the numbers; they are not comparable to other studies here):**

- *Retention / completion* — **"adequate AWARE and EMA data"** plus attendance at the follow-up visit. The paper does not publish the threshold behind "adequate", which is the weakest point in its reporting.
- *Sensor data availability* — **≥30 days of AWARE sensor data** for the per-participant availability figure.
- *EMA completion tiers* — ≥20 days, <20 days, or 0 days, used as the grouping variable for clinical outcomes.

**Figures:**

| Metric | Value |
|---|---|
| Participants with ≥30 days of AWARE sensor data | **12 / 24 (50.0%)** |
| Participants supplying **no** AWARE data after enrolment | **3 / 24 (12.5%)** |
| Median days AWARE data transmitted | **34.5 (IQR 28.8)** |
| Participants completing ≥20 days of EMAs | 12 (50.0%) |
| Participants completing <20 days of EMAs | 5 (20.8%) |
| Participants completing **0** EMAs | **7 (29.2%)** |
| Mean sensor types delivered — **Android** | **8.4** |
| Mean sensor types delivered — **iOS** | **4.7** |

**Passive and active data were locked together, not decoupled.** "All participants supplied AWARE data every day that they responded to EMAs." This is the opposite of the module's most-replicated pattern ([pattern 1](../feasibility-matrix.md): passive outlasts active) — here the passive stream did not survive independently of the participant's engagement with the survey. It is consistent with the finding that 29.2% supplied zero EMAs while 12.5% supplied zero sensor data at all: for a substantial group, disengagement was total rather than stream-specific.

**A counter-signal worth recording:** some participants **kept supplying AWARE data for a mean of 14.6 additional days after the EMA period ended**, despite being asked to uninstall the app. Passive collection outlived the study protocol in exactly the people it did not outlive the EMAs in. This has a governance implication — a study that instructs uninstallation must verify it, not assume it.

**Named technical failure modes:** app interference with other phone functions (3 participants); installation failure despite repeated attempts (1); loss of cellular service (1); and, in the authors' own limitations, "temporary interruptions (eg, if the phone is turned off or the operating system halts data collection)". The OS-halts-collection mechanism is the same background-execution dependency documented for [Beiwe](beiwe-als-adherence.md) and [CARP](carp-mpath-sense-performance-study.md).

**The OS asymmetry, and what it does and does not say.** Android delivered 8.4 sensor types on average against iOS's 4.7. This is a **breadth-of-stream** measure, not a within-stream completeness measure, and the direction (Android > iOS) is the *opposite* of the direction [McClaine 2024](aware-chemotherapy-engagement.md) reports for the same framework on a *yield* measure. Both are AWARE. The two are not necessarily in conflict — iOS restricts which sensors AWARE can access at all, while McClaine's figure concerns how much data arrives from the sensors that do work — but neither paper measures the other's quantity, so the reconciliation is inference. The authors themselves note that model-level variance beyond OS "could not be captured."

## Feasibility Findings

The authors' own conclusion is that digital phenotyping is **"a feasible method for disease monitoring and prognostication in this population"**, while simultaneously reporting a 14.7% enrolment rate, a 50% retention rate, and app-attributed withdrawals. That gap between the framing and the numbers is itself worth reading: this module has repeatedly found "feasible" used to mean "not impossible" rather than "operationally sound".

Their explicit lessons for future study design:

1. Enrolment was limited by **lack of interest** and by **smartphone incompatibility with the study app**; they expect the latter to shrink with better cross-model support.
2. Retention was 50% with **no baseline predictor of who dropped out** — so pre-screening on severity, insight or readiness will not select a retainable cohort.
3. Data transmission was inconsistent across individuals despite standardised installation procedures, with **Android/iOS differences plus unmeasured model-level variance**.
4. **"Data sparsity must be accounted for in both study recruitment and data analysis"** — i.e. inflate the target N at design time, and handle missingness explicitly rather than by listwise deletion.

## Relevance to Future Study Design

1. **Plan for roughly 7× the analytic N at approach.** 163 approached produced 12 usable participants. In a stigmatised, physically ill population with a 30-day protocol and light-touch support, that is the realistic conversion.
2. **Report withdrawal reasons at the level of the app, not "burden".** The finding that 5 of 12 withdrawals were app-attributable — including one outright installation failure — is only visible because the authors itemised it. Most studies here do not, and the module cannot separate app defects from protocol burden as a result.
3. **Check whether your missingness correlates with your outcome, not just with your baseline covariates.** The relapse rate among zero-EMA participants was 3.4× that of completers while baseline characteristics were identical. Testing only baseline balance would have given false reassurance. This extends [Wang 2021](beiwe-inpatient-suicide-pilot.md)'s "missingness is signal" finding from a predictor to a confounder.
4. **Do not assume passive collection will carry you when EMA engagement fails.** In this cohort it did not: sensor data arrived only on days the participant also answered the survey. The passive-outlasts-active assumption is not safe in every deployment.
5. **Verify uninstallation.** Data kept arriving for a mean of 14.6 days after participants were instructed to remove the app.
6. **Budget the screening burden of technology eligibility.** 13.5% of everyone approached was excluded by app incompatibility, before any consent conversation.

## Evidence Confidence

**Verified** — the 163/24/12 funnel and all decliner sub-counts; the itemised withdrawal reasons; the 50.0% ≥30-day sensor availability, 12.5% zero-data and 34.5-day median; the EMA completion tiers; the Android 8.4 vs iOS 4.7 sensor-type means; the 90-day clinical outcomes by completion tier; the null on completer-vs-non-completer baseline comparison; the incentive schedule and the 3-consecutive-day escalation rule. Read from the full text (Europe PMC PMC10984664), 2026-09-02.

**Reported** — the interpretation that the Android/iOS difference reflects platform sensor availability. The measurement is real; the mechanism is the authors' explanation, unmeasured.

**Unclear** — the threshold behind "adequate AWARE and EMA data" that defines the 50% retention rate. This is the study's headline feasibility figure and its denominator is not published. Also unclear: how many participants or days the "OS halts data collection" interruptions affected.

**Small-sample caution.** N=24 enrolled, 12 completing, single US academic centre, 83.3% White, median 97 days of abstinence before enrolment and low baseline craving scores. The authors flag likely self-selection on insight and readiness to change. The association between non-completion and 90-day relapse rests on 7 participants in the zero-EMA group and should be read as a signal to test, not an effect size.

**Pre-heartbeat / configuration note.** This is an AWARE deployment, so the Beiwe `heartbeat` caveat does not apply — but the collection window (Sep 2021 – Jul 2022) predates several iOS and Android background-execution changes, and the framework build is not specified.

**COI:** none relating to the platform. No author is an AWARE developer, and the study is not promotional about the framework — it is one of the few papers here that names the sensing app as a cause of dropout.

## Key Links

- Paper (OA, CC BY-NC-ND): https://doi.org/10.1097/HC9.0000000000000329
- Europe PMC: https://europepmc.org/article/PMC/PMC10984664
- Supplemental material (recruitment/retention flow diagram, per-participant sensor availability): http://links.lww.com/HC9/A669
- RAPIDS pipeline: https://www.rapids.science/
- Local PDF: `../literature/2023-wu-hepatolcommun-aware-alcohol-craving-liver-disease.pdf`

## Related profiles

- Platform: [AWARE](../../module-02-digital-phenotyping/profiles/aware-framework.md)
- Same framework, opposite OS-yield direction: [`aware-chemotherapy-engagement.md`](aware-chemotherapy-engagement.md)
- Pre-consent technology exclusion: [`aware-light-smartsense-d-youth-depression.md`](aware-light-smartsense-d-youth-depression.md), [`beiwe-spine-disease-mobility.md`](beiwe-spine-disease-mobility.md)
- Missingness as signal / informative attrition: [`beiwe-inpatient-suicide-pilot.md`](beiwe-inpatient-suicide-pilot.md), [`beiwe-missing-data-sociodemographic.md`](beiwe-missing-data-sociodemographic.md)
- Baseline severity does not predict attrition: [`radar-mdd-recruitment-retention.md`](radar-mdd-recruitment-retention.md), [`beiwe-als-adherence.md`](beiwe-als-adherence.md)
- Incentives do not fix engagement: [`beiwe-spinal-cord-injury-incentives.md`](beiwe-spinal-cord-injury-incentives.md)

## Sources

1. Wu T, Sherman G, Giorgi S, Thanneeru P, Ungar LH, Kamath PS, Simonetto DA, Curtis BL, Shah VH. *Hepatol Commun* 2023;7(12):e0329. DOI 10.1097/HC9.0000000000000329. Full text read from Europe PMC (PMC10984664), 2026-09-02. Byline verified against the publisher PDF. Establishes every figure in this profile.
