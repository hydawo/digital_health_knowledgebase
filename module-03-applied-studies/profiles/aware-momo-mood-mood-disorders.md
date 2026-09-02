# Aledavood et al. 2024 — MoMo-Mood: AWARE + actigraph + bed sensor in mood disorders, N=151 for up to 1 year

## Quick Facts

| Field | Details |
|---|---|
| Citation | Aledavood T, Luong N, Baryshnikov I, Darst R, Heikkilä R, Holmén J, Ikäheimonen A, Martikkala A, Riihimäki K, Saleva O, Triana AM, Isometsä E. "Multimodal Digital Phenotyping Study in Patients With Major Depressive Episodes and Healthy Controls (Mobile Monitoring of Mood): Observational Longitudinal Study." *JMIR Mental Health* 2024;11:e63622. DOI [10.2196/63622](https://doi.org/10.2196/63622). PMID 39984168 / PMC11890149. |
| Study design | Observational longitudinal cohort with **four subcohorts** (MDD, bipolar disorder, borderline personality disorder, healthy controls), preceded by a separately-recruited pilot. **Study adherence is research question 1**, not a footnote. Two-phase design: a 2-week *active* phase, then a *passive* phase of up to 1 year. |
| Sample size (enrolled / analyzed) | **Main study: 164 recruited → 13 (7.9%) supplied no passive data at all → 151 analyzed** (30 controls; 121 patients — 76 MDD, 24 BPD, 21 BD). **Pilot: 37 recruited (23 controls + 14 MDD), 1 control excluded on baseline PHQ-9.** |
| Population | Finnish psychiatric **outpatients** already diagnosed by structured interview (MINI; SCID-II for BPD), recruited from Helsinki University Hospital Mood Disorder Division, Turku University Central Hospital and City of Espoo Mental Health Services, plus healthy controls. Patients mean age 34.7 (SD 12.71), 71.1% female; controls mean 42 (SD 14.07), 77% female. Excluded: psychotic features, concurrent substance use disorder, imminent suicide risk. |
| Duration | **Up to 1 year** (pilot: 6 months for patients, 1 year for controls). Active phase 2 weeks; passive phase the remainder. |
| Devices/platforms used | **[AWARE](../../module-02-digital-phenotyping/profiles/aware-framework.md)** — "modified and adapted" by the authors — orchestrated by the **Niimpy / Non-Intrusive Individual Monitoring Architecture (NIIMA)** platform; **Philips Actiwatch 2** actigraph; **Murata SCA11H** ballistocardiographic bed sensor with a preconfigured Wi-Fi router. Smartphone BYOD; actigraph, bed sensor and router provisioned. |
| Funding/COI | Academic (Aalto University, University of Helsinki). James S. McDonnell Foundation (TA); Aalto Science-IT. **"Conflicts of Interest: None declared."** Acknowledgements thank Denzil Ferreira — an AWARE author — for discussions, but no AWARE developer is on the byline. |
| Last verified | 2026-09-02 |

## Summary

The **largest and longest AWARE deployment in this module**, and the only one designed with study adherence as a primary research question rather than a reported byproduct. It contributes three things the module did not previously have.

**First, a passive-data completeness figure stratified by psychiatric diagnosis, using an unusually honest proxy.** The authors treat a day with **no smartphone battery data** as a missing day and report average per-participant passive missingness of **10.5% overall — but 1.2% for controls, 4.5% for BD, 14.1% for MDD and 20.4% for BPD**. That is a **17-fold spread across diagnostic groups within one study, one platform and one configuration.** The module has never had this comparison before, and it undermines the practice of quoting a single platform-level completeness number.

**Second, a clean demonstration that adherence and completeness diverge in opposite directions across the same subcohorts.** Measured by PHQ-9 response, BD patients were the *most* adherent group (83% still responding at week 8) and controls among the least (52%). Measured by passive missingness, controls were the *best* (1.2%) and BPD the worst (20.4%). **Ranking platforms or populations by "adherence" gives a different answer depending on which stream you pick** — the module's central methodological warning, instantiated inside a single study.

**Third, a quantified cost of not engaging participants after onboarding.** Contact ceased after the 2-week active phase. **By week 8 only 65.7% (99/151) were still returning the biweekly PHQ-9**, and the authors name the absence of follow-up or feedback as the likely cause. This is the module's cleanest natural experiment on support intensity, because the design change is explicit and the authors say so.

Notably, **the log-rank test found no significant difference in adherence between patients and healthy controls**, and no significant difference between patient subcohorts — despite the descriptive spread above. The study is a caution against over-reading subgroup adherence percentages that survival analysis does not support.

## Instrumentation and Deployment Model

**Two-phase design, deliberately front-loaded to limit burden.**

| Phase | Length | Streams |
|---|---|---|
| **Active** | 2 weeks | AWARE passive smartphone sensing; **EMA 5×/day** (morning, evening, 3 random afternoon prompts); Actiwatch 2 actigraphy; Murata bed sensor |
| **Passive** | up to 1 year | AWARE passive smartphone sensing only; **PHQ-9 every 2 weeks** |

The authors state the split was implemented "to minimize the risk of study fatigue and burden on participants." The 2-week active window was chosen to match both the PHQ-9 recall period and the **14-day battery life of the Actiwatch 2** — so participants never had to charge the actigraph, and researchers never had to re-provision it. That is a device-selection decision made for operational reasons, and it is the kind of choice this module rarely sees made explicit.

**Smartphone streams collected:** accelerometer (x/y/z + accuracy), app foreground use / notifications / crashes, battery (level, status, health), call type and duration, SMS type, location (lat/long/speed/accuracy), screen state (on/off/lock/unlock). **No message content and no contact identities left the device**; contacts were reduced to anonymous identifiers.

**The bed sensor required provisioned network infrastructure** — participants received the Murata node *and a preconfigured Wi-Fi router* so data could go straight to the study server. Any team costing a bed-sensor arm should budget the router, its configuration, and the home-network support call that follows.

**Incentive: four movie tickets total** — two at enrolment, two after completing the active phase. Nothing for the passive year. The authors state explicitly this was the only compensation, and no feedback was returned to participants. For a study asking for up to 12 months of continuous smartphone sensing, this is at the extreme low end of what this module has recorded.

## Recruitment and Retention

- **164 recruited into the main study.** **13 (7.9%) provided no passive data whatsoever** "due to technical challenges or other issues" and were excluded from all analyses. The paper does not disaggregate technical failure from non-participation, so the true zero-yield technical rate is a subset of 7.9%.
- **151 analysed:** 30 controls, 76 MDD, 24 BPD, 21 BD.
- **Employment asymmetry is severe and matters for interpretation:** 83% (25/30) of controls were employed full time versus **9.9% (12/121) of patients**. The authors re-ran the rhythm analyses restricted to full-time-employed participants precisely because of this, and some findings reversed — a reminder that "patient vs control" in this cohort is partly confounded with daily structure.
- **Baseline PHQ-9:** controls 1.7 (SD 1.49); MDD 14.6 (SD 5.41); BPD 14.57 (SD 5.62); BD 13.53 (SD 4.73) — i.e. mild-to-moderate outpatient depression, not severe or inpatient.

**Adherence over time (definition: returned the biweekly PHQ-9):**

| Group | Still active at week 8 |
|---|---|
| **Overall** | **65.7% (99/151)** |
| Bipolar disorder | 83% (17/21) |
| MDD | 74% (56/76) |
| **Healthy controls** | **52% (16/30)** |
| Borderline personality disorder | 50% (12/24) |

**Kaplan-Meier survival analysis with a log-rank test found no statistically significant difference between any of these groups.** Treat the ordering as descriptive. What is robust is the *overall* level: a third of the cohort had stopped returning questionnaires within two months, in a study with no post-onboarding contact.

## Data Completeness and Technical Issues

**Definitions used (they differ from every other study in this module):**

- *Participation adherence* — **availability of the biweekly PHQ-9 response**. This is an active-stream definition being used as the study's headline adherence metric.
- *Passive data missingness* — per participant, **days with no battery data ÷ days enrolled**, then averaged across participants within a group. Battery data are used as a proxy for "the app was running and transmitting at all". This is a **presence-of-any-data** definition, the most permissive family in the module (compare [Beukenhorst 2022](beiwe-als-adherence.md)); it will not detect partial-day loss, duty-cycle shortfalls, or [structurally corrupt records](connect-multi-wearable-psychosis.md).
- *Analytic inclusion for rhythm analyses* — **≥8 weeks of communication and smartphone-use data**, with the first and last day of each participant's record excluded as incomplete.

**Average passive-data missingness, by group:**

| Group | Mean missingness |
|---|---|
| Healthy controls | **1.2%** |
| Bipolar disorder | 4.5% |
| MDD | 14.1% |
| **Borderline personality disorder** | **20.4%** |
| **All participants** | **10.5%** |

**Other completeness and cleaning figures:**

- **46,788 calls collected; 39,491 (84.4%) longer than 0 seconds** — i.e. **15.6% of call records were zero-duration** and had to be treated separately. Anyone deriving "number of calls" from a phone-log stream without this filter is counting missed and failed connections as social contact.
- **132 app-use sessions exceeding 10 hours were removed as probable system error.** A small number, but it establishes that app-foreground duration on this stack can produce impossible values.
- Actigraph and bed-sensor nights were dropped if <3 h or >13 h of sleep, and first/last nights were always excluded. Final yield: **862 actigraph days and 841 bed-sensor nights** from the 2-week active phase.
- Bed-sensor and actigraph outputs were **manufacturer-preprocessed**; the authors flag this as a limitation that "can potentially introduce unknown errors and biases." The module has the same concern logged for vendor-derived wearable metrics generally.

**No OS-stratified data is reported.** The paper does not state the iOS/Android split of the cohort, does not report yield by OS, and does not discuss iOS background-execution constraints — a notable omission in a study using a modified AWARE build for up to a year. This limits its contribution to Tier 15 Q111/Q111b.

**No app-crash counts are published**, despite `app crashes` being one of the collected AWARE streams — the same absence [McClaine 2024](aware-chemotherapy-engagement.md) exhibits.

## Feasibility Findings

The authors' stated conclusion is that the design is feasible: the pilot "had no significant issues", which justified scaling to the main study "with minimal changes overall", and the main study demonstrates "the feasibility of harnessing data from a cohort of patients with different types of clinically diagnosed depressive syndromes."

Their own caveats are the useful part:

1. **"The overall adherence rates for all groups were low."** They say so directly in the Principal Findings, and again in the Limitations: incomplete data and rising dropout "may decrease the study's analytical power, introduce bias, and obscure longitudinal patterns."
2. **They name the cause they can act on:** "Our participants were not followed up on or engaged with after they completed the active phase... The lack of further follow-up or feedback to the participants has likely played an essential role in our dropout rates." This is a self-diagnosed, correctable design fault, stated plainly.
3. **They benchmark against the literature rather than claiming a good result** — citing 65.3% smartphone completeness in a 334-patient 12-week MDD study, 99% in a 29-patient 1-year bipolar study, and 84.8%/66.8% patient/control daily self-assessment adherence over 9 months elsewhere. Their own figures sit at the low end and they say so.
4. **Substantive scientific yield was modest**: no group differences in sleep duration, active hours, accelerometer-derived activity intensity, call/SMS volume or total screen time. Only **weekday location variance (P=.004) and weekday normalized entropy (P=.05)** separated patients from controls, and the entropy effect did not survive restriction to employed participants. Their reading: passive sensors "may more readily detect gross observable behavioral abnormalities, which may emerge only in the epidemiologically rarer severe range of depression or in mania."

That last point is a feasibility finding in the strict sense: **a year of multimodal passive collection in mild-to-moderate outpatient depression produced few group-level signals**, which is decision-relevant for anyone sizing a similar study.

## Relevance to Future Study Design

1. **Do not quote a platform-level completeness number for a mixed-diagnosis cohort.** 1.2% versus 20.4% within one study, one app build and one configuration. If your cohort includes BPD or comparable populations, plan against the subgroup figure, not the pooled 10.5%.
2. **Choose your adherence metric before you see the data, and name the stream.** The BD group is best on PHQ-9 return and second-best on passive missingness; controls are worst on PHQ-9 return and best on passive missingness. A study reporting either alone would tell a different story.
3. **Post-onboarding contact is the lever, and its absence is measurable.** 65.7% at week 8 with zero contact after week 2 and four movie tickets total. Compare [Calvert 2026](mindlamp-linc-passive-data-quality.md), where 1.3 troubleshooting contacts per participant and ~9 interventions/week bought median GPS quality of 0.92. The cost of support is now quantified at both ends of the range.
4. **Match device battery life to phase length.** The 14-day active phase exists partly because the Actiwatch 2 runs 14 days. Zero charging burden, zero re-provisioning, zero charge-related missingness — obtained by fitting the protocol to the hardware rather than the reverse.
5. **Filter zero-duration calls.** 15.6% of this cohort's call records. A social-contact feature built without that filter is measuring something else.
6. **Budget network infrastructure for home sensors.** The bed sensor required shipping a preconfigured router to every participant.
7. **Report the iOS/Android split even when you do not analyse it.** Its absence here means a 151-participant, year-long AWARE deployment cannot contribute to the module's highest-value open question.

## Evidence Confidence

**Verified** — the 164/13/151 flow and subcohort sizes; the pilot's 23+14 recruitment and single exclusion; the two-phase design and its rationale; the 65.7% week-8 adherence and all four subgroup figures; the null log-rank result; all five passive-missingness percentages and the battery-proxy definition behind them; the 46,788/39,491 call figures; the 132 removed app sessions; the 862 actigraph days and 841 bed-sensor nights; the device inventory; the four-movie-ticket compensation; and the authors' attribution of dropout to absent follow-up. Read from the full text (Europe PMC PMC11890149), 2026-09-02.

**Reported** — that the 13 zero-yield participants failed for technical reasons. The paper says "technical challenges or other issues" without disaggregating.

**Unclear** — the iOS/Android composition of the cohort and any OS effect (not reported); the number of participants behind each subgroup missingness average beyond the group sizes; the extent of AWARE modification ("modified and adapted... to cater to the needs of our studies") and therefore how transferable these figures are to a stock AWARE build; and the passive-phase EMA burden, since EMA ran only in the 2-week active phase and its results are published elsewhere.

**Generalisability caution.** Finnish public-sector psychiatric outpatients with mild-to-moderate symptoms, excluding psychosis, active substance use disorder and imminent suicide risk. The authors note that including inpatients, severe or psychotic depression, or mania "might have revealed more marked deviations" — and that patients were on treatment, so observed sleep is partly pharmacological. The 83%-vs-9.9% employment gap between controls and patients confounds any daily-rhythm comparison.

**Same-study note:** MoMo-Mood also exists as a medRxiv preprint (`10.1101/2024.06.27.24309600`) and a JMIR preprint. **This is one study, profiled once**; the *JMIR Mental Health* version is cited. The pilot (MoMo-Mood Pilot) is described within this paper and is not a separate Module 3 entry.

**COI:** none declared, and none apparent. No AWARE developer is an author; Denzil Ferreira is thanked in acknowledgements only. The paper's own adherence figures are unflattering and are presented as such.

## Key Links

- Paper (OA, CC BY): https://doi.org/10.2196/63622
- Europe PMC: https://europepmc.org/article/PMC/PMC11890149
- medRxiv preprint (same study): https://doi.org/10.1101/2024.06.27.24309600
- Niimpy behavioural data analysis toolbox (open source, authors' own): https://github.com/digitraceslab/niimpy
- Local PDF: `../literature/2024-aledavood-jmirmentalhealth-momo-mood-multimodal-digital-phenotyping.pdf`

## Related profiles

- Platform: [AWARE](../../module-02-digital-phenotyping/profiles/aware-framework.md)
- Other AWARE deployments: [`aware-chemotherapy-engagement.md`](aware-chemotherapy-engagement.md), [`aware-msavorus-loneliness-multidevice.md`](aware-msavorus-loneliness-multidevice.md), [`aware-light-smartsense-d-youth-depression.md`](aware-light-smartsense-d-youth-depression.md)
- Support intensity as the retention lever: [`mindlamp-linc-passive-data-quality.md`](mindlamp-linc-passive-data-quality.md), [`radar-mdd-recruitment-retention.md`](radar-mdd-recruitment-retention.md)
- Retention vs completeness divergence: [`radar-mdd-recruitment-retention.md`](radar-mdd-recruitment-retention.md), [`radar-mdd-longterm-engagement.md`](radar-mdd-longterm-engagement.md)
- Permissive presence-of-any-data completeness definitions: [`beiwe-als-adherence.md`](beiwe-als-adherence.md)
- Present-but-wrong data: [`connect-multi-wearable-psychosis.md`](connect-multi-wearable-psychosis.md)

## Sources

1. Aledavood T, Luong N, Baryshnikov I, Darst R, Heikkilä R, Holmén J, Ikäheimonen A, Martikkala A, Riihimäki K, Saleva O, Triana AM, Isometsä E. *JMIR Ment Health* 2024;11:e63622. DOI 10.2196/63622. Full text read from Europe PMC (PMC11890149), 2026-09-02. Byline verified against the publisher PDF (PMC JATS lists the handling editor and peer reviewers in separate contrib-groups after the authors). Establishes every figure in this profile.
