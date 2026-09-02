# Bae et al. 2023 — AWARE-based app for binge-drinking prediction in young adults, N=75 over 14 weeks

> **Thin-operational-content profile.** This is primarily an algorithm-development paper and it reports no retention rate, no withdrawal count and no recruitment funnel. It is included for one substantive deployment finding — **35.4% of participant-days were unusable, largely because the sensing app let participants switch sensors off** — plus its incentive structure and its platform-developer authorship. Everything else here is context. See *Scope note* under Evidence Confidence.

## Quick Facts

| Field | Details |
|---|---|
| Citation | Bae SW, Suffoletto B, Zhang T, Chung T, Ozolcer M, Islam MR, Dey AK. "Leveraging Mobile Phone Sensors, Machine Learning, and Explainable Artificial Intelligence to Predict Imminent Same-Day Binge-drinking Events to Support Just-in-time Adaptive Interventions: Algorithm Development and Validation Study." *JMIR Formative Research* 2023;7:e39862. DOI [10.2196/39862](https://doi.org/10.2196/39862). PMID 36809294 / PMC10196900. |
| Study design | **Secondary analysis** of sensor and SMS data collected within a 5-arm randomized trial (ClinicalTrials.gov **NCT02918565**), granted IRB exemption as secondary analysis. Algorithm development and validation; XAI (SHAP-style) feature attribution. |
| Sample size (enrolled / analyzed) | **75 participants** — the same 75 throughout; no attrition is reported. Analytic unit is the **person-day**: **1,168 reported events → 754 retained (64.6%)**, after excluding **414 (35.4%)**. |
| Population | Young adults **aged 21–25** with ≥1 past-month binge-drinking event, recruited from **emergency departments** in the greater Pittsburgh area. Mean age 22.4 (SD 1.9); **71% women; 53% White, 31% Black, 16% other race; 11% Hispanic; 45% college-enrolled.** A more socioeconomically and racially varied cohort than most in this module. |
| Duration | **14 weeks.** |
| Devices/platforms used | A **custom app built on the [AWARE](../../module-02-digital-phenotyping/profiles/aware-framework.md) framework** — not a stock AWARE deployment. iOS and Android. Ground truth by **twice-weekly SMS** self-report, not in-app EMA. BYOD; no wearable. |
| Funding/COI | NIH/NIAAA **1R21AA030153-01**. IRB: Stevens Institute of Technology 2023-018(N); University of Washington STUDY00016480. **COI: senior author Anind K. Dey is a co-author of the AWARE framework paper (Ferreira, Kostakos & Dey 2015)** that this app is built on. No competing-interests statement addressing this appears in the extracted text. |
| Last verified | 2026-09-02 |

## Summary

The module's first AWARE-derived deployment in a **non-clinical, ED-recruited young-adult substance-use cohort**, and its first covering a just-in-time adaptive intervention (JITAI) *target* rather than a delivered JITAI.

Its one genuinely decision-relevant operational finding is a data-loss figure with a named mechanism:

> **414 of 1,168 reported drinking/non-drinking days (35.4%, mean 5.52 per person) were excluded because they lacked GPS location data and had more than half of their key features missing.** The authors' stated explanation: **"the AWARE app allowed users to disable GPS collection."**

That is a **configurability-as-data-loss** finding, and it is a different failure class from everything else the module has catalogued. This module's existing loss mechanisms are OS background restrictions, permission revocation, radio/battery demand, vendor policy change, server capacity and participant non-wear. Here the *framework's own participant-facing settings menu* is the loss mechanism: participants "recognized that the AWARE app and certain sensors are configurable, which means that, for example, GPS can be disabled manually by accessing the setting menu on their smartphones." Being told they could do it, they did.

The paper is otherwise light on deployment reality and should be cited narrowly.

## Instrumentation and Deployment Model

**A derivative app, not stock AWARE.** "We developed our mobile data collection app based on the AWARE framework." Any figure here applies to the authors' build, not to AWARE as distributed, and the sensor set and duty cycles reflect their configuration choices — the authors note they "used the default sampling rates specified in the AWARE data collection framework."

**Streams:** GPS/location, app usage (unique apps used, duration, app switches, apps in foreground), screen status (on/off counts, total screen duration), battery (time fully charged, total charging duration, battery percentage), and Wi-Fi (count of unique hotspots as an environmental feature).

**Store-and-forward upload, gated on Wi-Fi.** Data were stored on the device and synced to the study server, encrypted, only when the phone reached Wi-Fi; the app **checked for Wi-Fi availability every 30 minutes**. That is a deliberate design for battery and data-plan economy, and it also means a participant without regular Wi-Fi access accumulates upload latency — a real consideration in an ED-recruited, mixed-income cohort, and one the paper does not examine.

**Ground truth came by SMS, not in-app.** Participants were texted twice weekly, on the two days each had reported drinking most at baseline, asking how many standard drinks they consumed "yesterday", with the NIAAA standard-drink definition supplied, plus start and end times. Decoupling the outcome measure from the sensing app is a design choice worth noting: it means active-stream failure and passive-stream failure are independent here, unlike [Wu 2023](aware-alcohol-liver-disease-craving.md), where one app carried both and they failed together.

**Incentives:** **US $20** for installing the app and completing baseline surveys, then **US $10 per week of data collection, up to US $140** — roughly $160 maximum over 14 weeks, paid at the end. Note the structure: payment was for *weeks of data collection*, i.e. conditioned on the passive stream, not on survey responses. This module has no other example of an incentive tied to passive-data supply, and the paper does not evaluate whether it worked.

## Recruitment and Retention

**Not reported.** The paper gives the final cohort composition and nothing about how it was arrived at: no number approached or screened in the emergency departments, no consent rate, no withdrawals, no retention figure over the 14 weeks. Participants "were told that they could drop out of the study at any time"; whether any did is not stated. The parent trial (NCT02918565) is cited for "methods of screening, enrollment, and clinical trial procedures", so those figures exist elsewhere and are **not** carried into this profile — they were not read.

**The one inclusion rule stated** is analytic: participants were included if they reported ≥1 non-drinking day and ≥1 low-risk or binge day, and had **≥3 days with the minimum sensor data needed for analysis**. All 75 met it.

## Data Completeness and Technical Issues

**Definitions used:**

- *Excluded event* — a reported day with **no GPS-based location data and more than half of its key features missing**. This is a two-condition, feature-level definition and it has no counterpart anywhere else in this module; it is not comparable to any "wear time", "valid hour" or "data availability" figure in the [feasibility matrix](../feasibility-matrix.md).
- *Also excluded* — "days that were missing a few hours of sensor data (eg, owing to smartphone running out of battery)". The threshold for "a few hours" is not given.
- *Retained-day gap handling* — gaps of a few minutes (5–10 min) were filled by **linear interpolation between adjacent sensor readings**.

**Figures:**

| Metric | Value |
|---|---|
| Reported events (person-days) collected | **1,168** |
| Events excluded for missing sensor data | **414 (35.4%)** |
| Mean events excluded per participant | **5.52** |
| Events retained for analysis | **754 (64.6%)** |
| — binge-drinking events | 122 (16.2%) |
| — low-risk drinking events | 143 (19.0%) |
| — non-drinking events | 489 (64.9%) |

**Named loss mechanisms:** participant-initiated GPS disabling via the phone's settings menu (the mechanism the authors name first and most specifically); and phone battery exhaustion. No app-crash, sync-failure or device-loss counts are given, and there is **no OS-stratified reporting** despite the app running on both iOS and Android — the paper states the dual-platform support and never revisits it.

**A visible drift in the class counts.** The retained non-drinking events are reported as "489/756, 64.9%" in one sentence while the retained total is 754 in the same sentence and 122+143+489 = 754. The 756 appears to be a typographical error in the published text. Recorded rather than silently corrected.

**The authors' own operational recommendations** are the closest the paper comes to a feasibility discussion, and they are all about the missing 35.4%:

- "More frequent reminder systems or a more effective incentive mechanism could improve compliance with sustainable data collection using phone sensors and phone surveys over a long period."
- "**The development of a 'dashboard' could help a researcher to monitor participant compliance.**" — i.e. this study had none, which is the apparatus [McClaine 2024](aware-chemotherapy-engagement.md) credits for its 61/73/70% figures and [Calvert 2026](mindlamp-linc-passive-data-quality.md) costs at 1.3 contacts per participant.
- Future work should "explore different sampling rates to optimize both the performance of the predictive models and the battery life", since they used framework defaults.

## Feasibility Findings

The authors "position our work as a feasibility study" for sensor-driven JITAI targeting. Their transferable conclusions:

1. **Same-day binge-drinking events are predictable from phone sensors** at practically useful lead times — the modelling result, out of Module 3's scope, catalogued in Module 2's literature library.
2. **The deployment as run lost a third of its person-days**, and the fixes they name are *operational* (reminders, incentives, a monitoring dashboard) and *configurational* (sampling rates), not technical.
3. **Battery drain is treated as a live constraint on sensor selection** — they suggest that identifying an optimal sensor subset could allow lower overall sampling rates, trading model performance against battery life. This is the module's clearest statement that sensor-set design is a battery-budget decision, though it is proposed rather than measured.

## Relevance to Future Study Design

1. **Check what your sensing app lets participants turn off, and whether you are obliged to tell them.** Informing participants that sensors are configurable is ethically right and operationally expensive — 35.4% of person-days here. Budget for it, or design the analysis so a single disabled stream does not invalidate the day.
2. **Do not make one stream load-bearing for the whole day's record.** The exclusion rule was *no GPS* **and** *>half of key features missing*. GPS disabling was the pivot. A feature set with a viable non-GPS fallback would have retained more of these days.
3. **A compliance dashboard is not optional at this scale.** The authors ask for one in their own future-work section. Studies in this module that had one report materially better completeness.
4. **Wi-Fi-gated upload is a socioeconomic variable.** A 30-minute Wi-Fi polling loop in an ED-recruited cohort will not treat all participants equally, and no study here has measured the effect.
5. **Report retention even in a secondary analysis.** A 14-week deployment in 75 people that publishes no withdrawal count cannot be used for retention planning, which is most of what a future team wants from it.
6. **State the OS split.** A dual-platform AWARE-derived build over 14 weeks contributes nothing to the module's highest-value open question because the paper never stratifies.

## Evidence Confidence

**Verified** — the 75-participant cohort and its demographics; the 14-week duration; the ED recruitment setting and parent-trial registration; the $20 + $10/week (max $140) incentive structure; the 1,168 → 754 event flow with the 414 exclusion and 5.52-per-person mean; the three retained class counts; the two-condition exclusion definition; the linear-interpolation gap handling; the 30-minute Wi-Fi polling and store-and-forward upload; the twice-weekly SMS ground-truth protocol; and the authors' statement that participants could disable GPS from the settings menu. Read from the full text (Europe PMC PMC10196900), 2026-09-02.

**Reported** — that GPS disabling is the cause of the missing key features. The authors offer it as an example ("might have occurred, for example, because...") rather than a measurement. **The 35.4% loss is Verified; its attribution to participant-initiated GPS disabling is Reported and should be cited as such.**

**Unclear** — retention and withdrawals over 14 weeks (not reported); the recruitment funnel (deferred to the parent trial and not read here); the iOS/Android composition and any OS effect; the threshold behind excluding days "missing a few hours" of data; whether the incentive was actually paid per week of data supplied or per week enrolled; and whether the "489/756" figure is a typographical error (the arithmetic says yes).

**Scope note.** Module 3 excludes algorithm-development papers whose only operational content is a cohort size and a duration. This one clears that bar narrowly and on a single finding — a quantified, mechanism-attributed 35.4% person-day loss from a data-loss pathway not otherwise represented in the module — plus a novel incentive structure and a platform-developer COI worth recording. **It is not a feasibility study and should not be cited as evidence about AWARE's retention characteristics.** Its modelling results belong in [Module 2's literature library](../../module-02-digital-phenotyping/literature-library.md), not here.

**Platform-attribution note.** This is an **AWARE-derived custom build**, not stock AWARE, and the paper says so. The configurability finding may reflect the authors' build rather than the framework as distributed — although the ability of participants to revoke location permission through the OS is universal, and the finding likely generalises to any BYOD deployment that discloses it.

**COI:** senior author **Anind K. Dey co-authored the AWARE framework paper** on which this app is built. The paper contains no competing-interests statement addressing that relationship in the extracted text. The relevant exposure is limited — the study's headline operational finding is a criticism of the framework's configurability, which runs against interest — but the developer relationship is real and undisclosed here.

## Key Links

- Paper (OA, CC BY): https://doi.org/10.2196/39862
- Europe PMC: https://europepmc.org/article/PMC/PMC10196900
- Parent trial registration: https://clinicaltrials.gov/study/NCT02918565
- Local PDF: `../literature/2023-bae-jmirformres-phone-sensors-explainable-ai-drinking.pdf`

## Related profiles

- Platform: [AWARE](../../module-02-digital-phenotyping/profiles/aware-framework.md)
- Other AWARE deployments: [`aware-chemotherapy-engagement.md`](aware-chemotherapy-engagement.md), [`aware-alcohol-liver-disease-craving.md`](aware-alcohol-liver-disease-craving.md), [`aware-momo-mood-mood-disorders.md`](aware-momo-mood-mood-disorders.md), [`aware-stand-mood-prediction-adherence.md`](aware-stand-mood-prediction-adherence.md)
- The monitoring apparatus this study lacked: [`aware-chemotherapy-engagement.md`](aware-chemotherapy-engagement.md), [`mindlamp-linc-passive-data-quality.md`](mindlamp-linc-passive-data-quality.md)
- Configuration choice dominating data loss: [`empatica-epilepsy-data-quality.md`](empatica-epilepsy-data-quality.md)
- Analytic-threshold-driven denominators: [`actigraph-als-upper-limb-wear-time.md`](actigraph-als-upper-limb-wear-time.md)

## Sources

1. Bae SW, Suffoletto B, Zhang T, Chung T, Ozolcer M, Islam MR, Dey AK. *JMIR Form Res* 2023;7:e39862. DOI 10.2196/39862. Full text read from Europe PMC (PMC10196900), 2026-09-02. Byline verified against the publisher PDF (PMC JATS lists the handling editor and peer reviewer in contrib-groups **before** the author group for this article — naive parsing would put Amaryllis Mavragani and Olga Perski on the byline). Establishes every figure in this profile.
