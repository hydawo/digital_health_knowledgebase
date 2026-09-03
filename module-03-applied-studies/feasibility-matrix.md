# Module 3 — Feasibility Matrix

**Last updated: 2026-09-03.** **65 profiles / 64 distinct deployments** (two profiles report one cohort, see Part D; Part E folds two multi-paper cohorts into single profiles). One row per study. This is the resource a future study team should read
first: who else tried this device/platform combination, at what scale, for how long, and did it hold
up.

**How to read this file.** Retention and completeness are *different questions* and studies answer
them very differently — a study can report 80% retention and 18% cross-stream completeness at the
same time. Both columns are given where the study reports both. Figures are as reported; definitions
are **not** standardised across studies (see the Definitions warning at the bottom, which is the
single most important caveat in this file).

---

# Part A — Baseline set (19 studies, 2026-08-31)

## Table 1 — Scale, duration, retention

| Study | Device / platform | Deployment model | N (enrolled → analyzed) | Duration | Retention |
|---|---|---|---|---|---|
| [Matcham 2022 (RADAR-MDD)](profiles/radar-mdd-recruitment-retention.md) | RADAR-base + Fitbit Charge 2/3 | Provisioned wearable, own phone, **Android only** | 623 enrolled | 11–24 mo (median 541 d) | **79.8%** stayed max available time; 20.2% withdrew; ~80% outcome completion at every timepoint |
| [Zhang 2023 (RADAR-MDD)](profiles/radar-mdd-longterm-engagement.md) | RADAR-base + Fitbit | Same cohort as above | 614 analyzed | 43 wk / 94 wk | At 43 wk: **Fitbit 67.6%, surveys 54.6%, phone passive 47.7%** |
| [Muurling 2024 (RADAR-AD)](profiles/radar-ad-feasibility-usability.md) | 8 device types incl. Axivity AX3, Fitbit Charge 3, Dreem, Fibaro, CANedge | Fully provisioned, own phone | 229 (+45 sub-study) | 8 wk (+4 wk) | **Drop-out 7.5%** (tier 1); 4.4% (tier 2) |
| [de Angel 2023](profiles/radar-base-treatment-engagement.md) | RADAR-base + Fitbit | Provisioned | 66 | 7 mo | **60%** |
| [Beukenhorst 2022 (ALS)](profiles/beiwe-als-adherence.md) | Beiwe | **BYOD, iOS + Android**; no engagement scaffolding | 94 across 3 studies | 12 / 52 / 20 wk | At 3 mo, active: **77% / 59% / 96%**; passive: 95% / 86% / 100% |
| [Yi 2024 (NHS3/GUTS)](profiles/beiwe-chronic-disease-substudy.md) | Beiwe | BYOD, both OSes, **uncompensated** | 32,441 invited → **2,394** | 1 yr (mean 214 d) | **57.3% at 6 mo** (Android 50.2%, iOS 59.8%) |
| [Huang 2025 (adolescents)](profiles/beiwe-adolescent-feasibility.md) | Beiwe | BYOD, **96% iPhone** | 48 analyzed | **18 mo** | **81%** completed full 18 mo |
| [Kiang 2021](profiles/beiwe-missing-data-sociodemographic.md) | Beiwe | BYOD, 77% Android | 211 (6 studies) | 2015–2018, varied | n/a — missingness meta-study |
| [Wang 2021 (inpatient)](profiles/beiwe-inpatient-suicide-pilot.md) | Beiwe (wave 2) + movisensXS (wave 1) | **Loaner phones provided** | 104 → 83 | Mean 6.9 d inpatient | 79.8% met ≥3-survey threshold; **only 65/83 completed follow-up** |
| [Cohen 2023 (SHARP)](profiles/mindlamp-relapse-3site.md) | mindLAMP | Hybrid — **phones + cellular provided** at Indian sites | 132 | Mean 156 d | Not framed as retention; 20 relapse events |
| [Meyer 2018 (Sleepsight)](profiles/sleepsight-schizophrenia-rest-activity.md) | Fitbit Charge HR + Purple Robot | **Fully provisioned incl. 4G data** | 15 → 14 | 8 wk | **93%** completed |
| [Raugh 2021](profiles/dp-schizophrenia-tolerability.md) | Ilumivu mEMA + Empatica smartband | Provisioned phones + band | 109 (54 SZ / 55 CN) | **6 d** | n/a (too short) |
| [Böttcher 2022](profiles/empatica-epilepsy-data-quality.md) | Empatica E4 | Provisioned, 4 centres | 632 inpatient + 39 outpatient | ~128,000 h total | Outpatient dropout: KCL 5/15, UKF 1/12 |
| [Jonker 2021](profiles/withings-postop-remote-monitoring.md) | Connecare + Fitbit Charge 2 + Withings Thermo/BPM | Fully provisioned | 102 screened → **47** → 37 completed | 3 mo | **56% participation**; 37/47 completed |
| [Helmer 2025 (Support)](profiles/movesense-palliative-support-trial.md) | Wrist monitor + chest-wall ECG (CE-marked) | Fully provisioned | **275 screened → 7** | ≤30 d | **Terminated early** — target of 25 unachievable |
| [Cho 2022 (BYOD)](profiles/byod-demographic-imbalance.md) | Fitbit/Garmin/Apple Watch | BYOD → hybrid | 15 studies reviewed + own cohort | — | n/a — viewpoint + case study |
| [Master 2022 (All of Us)](profiles/allofus-fitbit-step-counts.md) | Fitbit | **Pure BYOD, retrospective linkage** | 214,206 EHR-consented → **6,042** | **Median 4.0 yr** | n/a — cohort construction, not retention |
| [Garcia 2022 (Apple Heart)](profiles/apple-heart-data-management-lessons.md) | Apple Watch | Pure BYOD, **siteless** | **419,297** | 8 mo enrolment | 2,161 notified → **450 (20.8%)** returned primary-outcome data |
| [Lubitz 2022 (Fitbit Heart)](profiles/fitbit-heart-study-afib.md) | Fitbit (10 models) | Pure BYOD, siteless | **455,699** | Median 122 d at risk | 4,728 notified → 1,671 (35.3%) telehealth → **~22%** returned patch |

---

## Table 2 — Data completeness and wear time

| Study | Wear time | Active data completeness | Passive data completeness | Cross-stream |
|---|---|---|---|---|
| [Matcham 2022](profiles/radar-mdd-recruitment-retention.md) | **62.5%** (15.1 h/day) over median 541 d | PHQ-8 95.3% *any data*; **THINC-it: ~60% of participants had <26%** | GPS + battery best, phone usage worst | **Only 17.7% had >50% across all streams** |
| [Zhang 2023](profiles/radar-mdd-longterm-engagement.md) | — | Most-engaged cluster 20 surveys vs least-engaged 4 | Fitbit 294 d vs 18 d (best vs worst cluster) | 44.6% of low-survey participants kept supplying Fitbit ~42 wk |
| [Muurling 2024](profiles/radar-ad-feasibility-usability.md) | **Fitbit 83–94%**; Axivity 52–95% | Mezurio 83–92%; **Altoida 63–75%, unusable in mild-mod AD** | Dreem 84–93% | — |
| [de Angel 2023](profiles/radar-base-treatment-engagement.md) | Fitbit ~80% → **45%** at 7 mo | **~90% → ~30%** at 7 mo (steepest decline) | **Smartphone stable at 20–40% throughout**; GPS worst > Bluetooth > accelerometry | — |
| [Beukenhorst 2022](profiles/beiwe-als-adherence.md) | — | Surveys median 90–100% while active | **GPS 90–100% of days** | Month-1 dropouts: 7.8–41%; long-term adherers ~75% |
| [Yi 2024](profiles/beiwe-chronic-disease-substudy.md) | 14.8 h/day GPS; 13.2 h/day accel | **Surveys 36% mean** (registration survey 82.7%) | **40.4% of potential days; 68.8% within follow-up** | **Bimodal: ~40% excellent (≥75%), ~34% poor (≤10%)** |
| [Huang 2025](profiles/beiwe-adolescent-feasibility.md) | — | **47%**, declining 65% → 30% | **89%, flat over 18 mo** (90→95→95→94%) | Clinical interviews 99% |
| [Kiang 2021](profiles/beiwe-missing-data-sociodemographic.md) | — | — | **Non-collection at baseline: accel 19.1%, GPS 26.9%; +0.5%/wk and +0.9%/wk** | iOS GPS non-collection RR 0.66 vs Android |
| [Wang 2021](profiles/beiwe-inpatient-suicide-pilot.md) | — | **52.2%** EMA compliance | — | Missingness was a **top-2 predictor** of the outcome |
| [Cohen 2023](profiles/mindlamp-relapse-3site.md) | — | **28.5%** | **57.4%** (Boston 59.6%, Bangalore 52.3%, Bhopal 63.5%) | — |
| [Meyer 2018](profiles/sleepsight-schizophrenia-rest-activity.md) | **21.8 h/day = 91%**, all participants ≥70% | Sleep diary 91%, symptom diary 88% | — | — |
| [Raugh 2021](profiles/dp-schizophrenia-tolerability.md) | — | SZ **63.8%** vs CN 75.3% (morning best, momentary worst) | **ACL 87/90% > GPS 73/78% > audio 40/50% > smartband 20/28%** | — |
| [Böttcher 2022](profiles/empatica-epilepsy-data-quality.md) | **On-body >80% every cohort** | — | **Onboard storage <10% loss vs streaming up to ~50%**; BCH 98.4% vs KCL 51.5% completeness | Signal quality: TEMP 92–100% > EDA 63–78% > **BVP 51–63%** |
| [Jonker 2021](profiles/withings-postop-remote-monitoring.md) | **87 of 90 days** (median) | Vitals + questionnaires 10.5–12 of 14 d | — | SUS 74.4; NPS +29.7% |
| [Helmer 2025](profiles/movesense-palliative-support-trial.md) | — | — | Wrist **61.5%**, chest **55.2%**; **HR and RR >99%, SpO2 45.1%** | Last measurement 0–25 min before death |
| [Master 2022](profiles/allofus-fitbit-step-counts.md) | Valid day = **≥10 h wear + ≥100 steps** | — | **0.02% of days excluded** for <100 steps | 15.4–16.0% of person-months excluded (<15 valid days) |
| [Lubitz 2022](profiles/fitbit-heart-study-afib.md) | **Median 23 h/day (IQR 22–24)**; 85% of days ≥18 h | — | — | ~4.5% of ECG patches returned unusable |

---

## Table 3 — One-line feasibility takeaway per study

| Study | Takeaway |
|---|---|
| [Matcham 2022](profiles/radar-mdd-recruitment-retention.md) | 80% retention and 17.7% cross-stream completeness came from the same study — size multimodal analyses off the second number. |
| [Zhang 2023](profiles/radar-mdd-longterm-engagement.md) | Retention is stream-specific; wearables outlast phones; **study-provided phones retained *worse* than BYOD** (HR≈1.66). |
| [Muurling 2024](profiles/radar-ad-feasibility-usability.md) | Eight concurrent devices are feasible even in mild-moderate AD; **within-device design variation exceeded active-vs-passive category differences**. |
| [de Angel 2023](profiles/radar-base-treatment-engagement.md) | More intensive treatment predicted *more* attrition; self-tracking without visible improvement made people remove the wearable. |
| [Beukenhorst 2022](profiles/beiwe-als-adherence.md) | The unsupported baseline: 59% active retention at 3 mo in a year-long study with **no reminders, no incentives**. Purely passive collection is impossible. |
| [Yi 2024](profiles/beiwe-chronic-disease-substudy.md) | 13 invitations per enrolment; compliance is **bimodal**, not central; app deletion — not technical failure — was the dominant loss mechanism. |
| [Huang 2025](profiles/beiwe-adolescent-feasibility.md) | Over 18 months, **passive held flat at ~94% while surveys halved**. Reminder intensity tracked completion almost exactly (99% / 89% / 47%). |
| [Kiang 2021](profiles/beiwe-missing-data-sociodemographic.md) | Plan for ~19%/27% baseline non-collection growing ~0.5–0.9%/week. Demographics mostly did **not** predict missingness; OS did. |
| [Wang 2021](profiles/beiwe-inpatient-suicide-pilot.md) | **Model missingness as a predictor, not just a nuisance** — it beat most content features (AUC 0.81→0.93). |
| [Cohen 2023](profiles/mindlamp-relapse-3site.md) | A platform ported across two countries and urban/rural sites with modest quality loss — and **the rural site had the best passive completeness**. |
| [Meyer 2018](profiles/sleepsight-schizophrenia-rest-activity.md) | Patients rejected research-grade wearables on stigma; the consumer device they chose got 91% wear. **Negative symptoms, not paranoia, predicted dropout.** |
| [Raugh 2021](profiles/dp-schizophrenia-tolerability.md) | Passive stream reliability tracks **computational and radio demand**. A Bluetooth-tethered band returned ~20–28%. Use 25% adherence cut-offs, not 50%. |
| [Böttcher 2022](profiles/empatica-epilepsy-data-quality.md) | **Recording mode dominates everything**: onboard <10% loss vs streaming ~50%. Participants wore the device; the system lost the data. |
| [Jonker 2021](profiles/withings-postop-remote-monitoring.md) | Switching recruitment from phone to face-to-face nearly doubled participation (33%→63%). Barrier was at consent, not operation. |
| [Helmer 2025](profiles/movesense-palliative-support-trial.md) | **A no-proxy-consent requirement excluded 95.6% of screened patients and killed the study.** Settle consent before designing recruitment. |
| [Cho 2022](profiles/byod-demographic-imbalance.md) | 0 of 11 BYOD studies reporting demographics were representative. All of Us: >80% underrepresented overall → **70% White in its Fitbit substudy**. |
| [Master 2022](profiles/allofus-fitbit-step-counts.md) | Self-generated data is far more complete than study-collected data (0.02% day exclusions), and buys 4-year horizons — at ~3% linkage yield. |
| [Garcia 2022](profiles/apple-heart-data-management-lessons.md) | 419,297 enrolled → 450 usable. **You cannot reliably count your own participants** in app-enrolled trials; consider sample size as *estimated*. |
| [Lubitz 2022](profiles/fitbit-heart-study-afib.md) | BYOD gives wear compliance no provisioned study matches (23 h/day) — and costs representativeness. **A $50 incentive did not fix the funnel.** |

---

# Part B — Extension set (21 studies, 2026-09-01)

Built in two parallel passes: a **platform-coverage pass** closing the AWARE / Avicenna / MetricWire /
m-Path / CARP gap, and an **Onnela-tranche pass**. Same scope rules, same full-text standard.

## Table 4 — Extension: scale, duration, retention

| Study | Platform / device | Deployment model | N | Duration | Retention / completion |
|---|---|---|---|---|---|
| [McClaine 2024](profiles/aware-chemotherapy-engagement.md) | **AWARE** + Fitbit | BYOD phone, provisioned Fitbit | 320 approached → 167 enrolled (52.2%) → **162** | 90 d | 90.1% completed; 9.9% withdrew |
| [Camargo 2025 (SmartSense-D)](profiles/aware-light-smartsense-d-youth-depression.md) | **AWARE-Light** + actigraphy | BYOD, **Android only** | 48 consented → **40 (83%)** | 8 wk | 7 of 8 non-completers withdrew over **app technical issues** |
| [Nguyen 2025 (mSavorUs)](profiles/aware-msavorus-loneliness-multidevice.md) | **AWARE** + **Oura** + **Samsung Watch** | Multi-device, provisioned wearables | 37 → **29** | **22 wk** | 8 withdrew; EMA adherence reported *by phase*, declining |
| [Achterberg 2026](profiles/avicenna-adolescent-esm-school-phone-bans.md) | **Avicenna** | BYOD | 211 signed up (70% of approached) → **195** | 17 d, 6/day | **Compliance 78%** (95% CI 74.7–80.6) under a national school phone ban |
| [Kivelä 2024](profiles/avicenna-ema-suicidal-ideation-iatrogenic.md) | **Ethica/Avicenna** | BYOD | 209 signed up → 90 intake → **82 enrolled, 81 completed** | 21 d, 4/day, ≤40 items | **Acceptability reported as both 39% and 98%** — see below |
| [Kochhar 2025](profiles/avicenna-smoking-youth-ema-compliance.md) | **Avicenna** | BYOD | **84** | 7 d, 5/day | **Compliance 76.89%** (SD 5.81); 27 of 35 EMAs |
| [Siebers 2025](profiles/metricwire-fraudulent-participation.md) | **MetricWire** (+ Fitbit) | Virtual/siteless, incentivised | **10 fraudulent enrolled**; later **37 blocked** | ~6 mo | n/a — adversarial failure mode |
| [Spangenberg 2026](profiles/metricwire-post-discharge-ema-reactivity.md) | **MetricWire Catalyst** | BYOD | **16 interviewed** from parent cohort | **~7 mo, ~300 prompts** | **63.3% → 47.4%** across phases (vs 14–21% in prior comparable studies) |
| [Clark 2025](profiles/metricwire-sgm-youth-ema-feasibility.md) | **MetricWire** | BYOD | **50** SGM youth | 28 d, 3/day | **80.21%** (SD 16.92) — highest mental-health compliance in the module |
| [Dennard 2025 (AVATAR2)](profiles/mpath-avatar2-esm-engagement.md) | **m-Path** | Provisioned equipment + support | 207 → **134 (64.7%) consented to ESM** | 10/day × 6 d × 3 timepoints | **39.1%** (SD 28.5) — lowest in module, definitional; **35.3% declined ESM outright** |
| [Bonnier 2025](profiles/mpath-nssi-ema-benefits-challenges.md) | **m-Path** | BYOD | 132 → **124** | 28 d, 6/day | **74.87%** (SD 18.78), declining linearly |
| [Niemeijer 2023 (m-Path Sense)](profiles/carp-mpath-sense-performance-study.md) | **CARP (CAMS)** + m-Path | BYOD, **52 iOS / 52 Android** | **104** | 3 wk | **Relative coverage ≈ 0.50**; 69.5 GB collected |
| [Mercier 2020](profiles/beiwe-spinal-cord-injury-incentives.md) | Beiwe | BYOD | 105 approached → **43** | 4 mo | **50% → 78%** after a $30/2-month incentive was introduced |
| [Johnson 2023](profiles/beiwe-actigraph-modus-als-progression.md) | Beiwe + **ActiGraph Insight** / **Modus StepWatch** | BYOD phone + provisioned wearable | 46 → **40** (20/20) | 6 mo | Dual-form-factor compliance printed side by side |
| [Yi 2025](profiles/beiwe-nurses-health-study-burst.md) | Beiwe | BYOD, **uncompensated** | 600 invited → 238 consented → **181 transmitted** | **8 d** | 86.2% baseline survey; **~55% of twice-daily EMA** |
| [Fu 2024 (Pain-IDR)](profiles/beiwe-pain-clinic-operational-report.md) | Beiwe | BYOD, embedded in a live clinic | **77** onboarded | 6 mo protocol, 18 mo report | **49.4% completed**; 84% mean among completers |
| [Wright 2018 (HOPE)](profiles/beiwe-fitbit-gynecologic-cancer-hope.md) | Beiwe + **2× Fitbit** | BYOD phone + provisioned Fitbits, **no incentive** | 18 eligible → **8 gatekept by oncologists** → 10 approached → **10** | 30 d | "100% approach-to-consent" — see below |
| [Soon 2025](profiles/oura-university-freshmen-sleep.md) | **Oura Ring 3** + Z4IP | Provisioned, **paid up to ~USD 263** | **638**; 69 withdrew (10.8%) | **20 wk**, 64,642 nights | Largest consumer-wearable study in the extension |
| [Liu 2019](profiles/lamp-schizophrenia-cognition-unpaid.md) | **LAMP** (mindLAMP predecessor) | BYOD, **explicitly unpaid** | **35** (18 SZ / 17 HC) | 12 wk | Patients engaged **3× more** than healthy controls |
| [Cote 2019](profiles/beiwe-spine-disease-mobility.md) | Beiwe | BYOD, clinic-recruited | 216 approached → **105** (all analysed) | Median 94.5 d | **42% of those approached excluded for not owning a smartphone** |
| [Straczkiewicz 2024](profiles/actigraph-als-upper-limb-wear-time.md) | **ActiGraph GT3X+**, bilateral wrists | Provisioned | 438 → **202** analysed | **Mean 895 d (~29 mo)** | **282.8 collected days → 51.34 valid (18.2%)** |

## Table 5 — Extension: the numbers worth carrying

| Study | The number |
|---|---|
| [McClaine 2024](profiles/aware-chemotherapy-engagement.md) | Three streams, one cohort: **surveys 61%, smartphone passive 73%, Fitbit 70%**. **Non-White participants had ~half the odds of completing symptom surveys.** |
| [Camargo 2025](profiles/aware-light-smartsense-d-youth-depression.md) | **29% of consented participants could not run the app on their own Android handset.** Acceptability was high (83.1%) among those who could. |
| [Achterberg 2026](profiles/avicenna-adolescent-esm-school-phone-bans.md) | 78% compliance **with 88% reporting school phone restrictions** — but the protocol was redesigned around the ban, so the compliance was *bought*, not observed. |
| [Kivelä 2024](profiles/avicenna-ema-suicidal-ideation-iatrogenic.md) | **39% vs 98% acceptability for the same study, 59 points apart**, both defensible. Also: **no systematic ideation reactivity** over 21 days × 4/day. |
| [Kochhar 2025](profiles/avicenna-smoking-youth-ema-compliance.md) | **28.8% objected to the 1.5-hour response window** — a configurable platform setting, and the single biggest complaint. |
| [Siebers 2025](profiles/metricwire-fraudulent-participation.md) | **MetricWire's carrier-country field unmasked 10 fraudulent participants** (VPNs, Nigerian carriers) in a $480 virtual trial; a manual checklist later blocked 37. |
| [Spangenberg 2026](profiles/metricwire-post-discharge-ema-reactivity.md) | 63.3% → 47.4% over ~7 months, against prior comparable studies at **14–21%**. Prompts occasionally **intensified distress**. |
| [Clark 2025](profiles/metricwire-sgm-youth-ema-feasibility.md) | **80.21% compliance** — and the participants themselves chose 3 prompts/day, reasoning about school phone policies. Co-design as an adherence intervention. |
| [Dennard 2025](profiles/mpath-avatar2-esm-engagement.md) | 39.1% is an artefact: completion had to be defined as **100%-complete** because m-Path's partial-save export was unreliable. **Age, gender, ethnicity and severity did not predict completion (P=.74).** |
| [Bonnier 2025](profiles/mpath-nssi-ema-benefits-challenges.md) | **78.57% reported at least one benefit** (64.58% increased self-insight); **7.29% found it overwhelming**. Emotional discomfort correlated with lower compliance (r=−0.29). |
| [Niemeijer 2023](profiles/carp-mpath-sense-performance-study.md) | **~50% relative coverage** despite 69.5 GB collected — and **iOS gaps ~6× longer than Android's.** |
| [Mercier 2020](profiles/beiwe-spinal-cord-injury-incentives.md) | Retention **50% → 78%** — but **survey completion rate did not rise at all**, and recruitment stream mattered more (53% vs 21%). |
| [Yi 2025](profiles/beiwe-nurses-health-study-burst.md) | An 8-day burst in a highly-engaged cohort still yields only **~55% EMA response**. |
| [Fu 2024](profiles/beiwe-pain-clinic-operational-report.md) | **49.4% six-month completion** in a live clinic, with two mid-course IRB amendments documented. |
| [Wright 2018](profiles/beiwe-fitbit-gynecologic-cancer-hope.md) | "100% approach-to-consent" — after **treating oncologists gatekept out 8 of 18 eligible patients**. Clinician gatekeeping is invisible in most funnels. |
| [Soon 2025](profiles/oura-university-freshmen-sleep.md) | 10.8% withdrawal over 20 weeks at **~USD 263** compensation — a generous-payment benchmark. |
| [Liu 2019](profiles/lamp-schizophrenia-cognition-unpaid.md) | Unpaid, 12 weeks: **patients engaged 3× more than healthy controls.** Deliberately uncompensated for generalisability. |
| [Cote 2019](profiles/beiwe-spine-disease-mobility.md) | **42% of everyone approached excluded on the spot for not owning a smartphone** — the starkest BYOD exclusion figure in the module. |
| [Straczkiewicz 2024](profiles/actigraph-als-upper-limb-wear-time.md) | Same raw data, three thresholds: **analytic N = 202 / 240 / 308 at 21 / 16 / 8 hours** required daily wear. |


---

# Part C — Recency and citation-graph set (10 studies, 2026-09-02)

Built from the date-sorted and OpenAlex citation-graph discovery passes
([`_recency-scan-2026-09.md`](_recency-scan-2026-09.md),
[`_citation-graph-scan-2026-09.md`](_citation-graph-scan-2026-09.md)). Deliberately weighted **away**
from Beiwe — only 1 of 10 — because the citation-graph yield was Beiwe-heavy for reasons of anchor
citation counts, not deployment frequency.

## Table 7 — Recency set

| Study | Platform / device | N | Duration | Headline operational number |
|---|---|---|---|---|
| [Calvert 2026 — LINC](profiles/mindlamp-linc-passive-data-quality.md) | mindLAMP | 373 | 2–3 wk | **Median GPS quality 0.92** vs 0.12–0.80 across six prior mindLAMP studies — and the cost: **1.3 troubleshooting contacts/participant, ~9 interventions/week, two RAs** |
| [Mahmood 2026](profiles/vpn-network-traffic-phenotyping.md) | **VPN network-traffic sensing** (no Module 1/2 platform) | 29 contributing | 2 wk | **74.1% coverage, uniform across time of day, <1% battery/24 h** — but one **304-hour gap** after a reboot nobody noticed |
| [Shen 2026 — TechSANS](profiles/sensorkit-techsans-older-adults.md) | **Apple SensorKit** (first in module) | 21 | ~6 mo | 141 days/participant = **74.4%** under a ≥14 h/day rule; uncompensated, and the authors conclude compensation matters even for low-burden passive work |
| [McInerney 2024](profiles/beiwe-type-2-diabetes-feasibility.md) | Beiwe | 85 | — | **iPhone missed 70.0%/70.6% of morning/evening EMA vs Android 21.3%/26.8%** (p<0.001) — while accelerometer and GPS showed **no** OS association in the same cohort |
| [Bladon 2026 — CONNECT](profiles/connect-multi-wearable-psychosis.md) | Fitbit vs Apple Watch vs **Samsung** | 105 | 20 wk | Satisfaction flat across devices; **completeness differed ~3×**. The most-chosen device was the worst-performing. **98% of Samsung sleep records present but corrupt** |
| [Dewitte 2025](profiles/mpath-dementia-esm-feasibility.md) | m-Path | 12 | 10 d | **80% compliance at 7 prompts/day in dementia, zero dropouts, unpaid** |
| [Carlson 2026 — ActiveKC](profiles/garmin-low-income-physical-activity.md) | **Garmin** (first in module) | 114 | 7 wk | **Zero of 181 screened excluded for smartphone access** — but access was defined at *household* level (see profile) |
| [Presby 2025](profiles/whoop-mental-health-survey-engagement.md) | **WHOOP** (first in module) | 181,574 members | 13 mo | **170,320 → 3,196 (1.9%)** and **1.84 survey responses per person in 13 months** — with no recruitment, provisioning or clinic step at all |
| [Domínguez 2026](profiles/samsung-palliative-pain-ecuador.md) | Samsung Galaxy Watch | 7 | 7 wk | **First Latin American deployment in the module.** Completed a palliative protocol by recruiting inside an existing care programme with family-present consent |
| [Castillo 2025](profiles/mindlamp-global-cognitive-multisite.md) | mindLAMP | 56 | 30 d | India + US remote cognitive assessment. **Thinnest of the ten — flagged as such in-profile** |


---

# Part D — AWARE coverage set (5 profiles, 2026-09-02)

Built from a dedicated OpenAlex pass over the **425 papers citing the AWARE anchor** (Ferreira,
Kostakos & Dey 2015) since 2016. **All five verified from full text as genuine AWARE deployments** —
none was a background-citation misattribution — though two used modified builds (see notes).

## Table 8 — AWARE set

| Study | N | Duration | Headline operational number |
|---|---|---|---|
| [Wu 2023 — alcohol-associated liver disease](profiles/aware-alcohol-liver-disease-craving.md) | 163 → 24 → **12** | 30 d | **5 of 12 non-completers withdrew citing AWARE technical problems** (incl. one installation failure) vs 2 losing interest — the most explicit app-attributed dropout in the module |
| [Aledavood 2024 — MoMo-Mood](profiles/aware-momo-mood-mood-disorders.md) | 164 → **151** | up to 1 yr | **Passive missingness 1.2% (controls) → 20.4% (BPD)** inside one study, one platform, one config. A **17× spread** — platform-level completeness figures for mixed cohorts are close to meaningless. AWARE **modified by the authors** (NIIMA/Niimpy) |
| [Balliu 2024 — STAND](profiles/aware-stand-mood-prediction-adherence.md) | 437 → **183** | up to 40 wk | **1.7% vs 33.5–37.3% two-week attrition** — in-person clinical care vs online support, with the *sicker* arm retaining **better**. Mechanism: missed assessments reconciled during routine visits |
| [Borelli 2025 — mSavorUs completeness](profiles/aware-msavorus-passive-completeness-companion.md) | 37 → **28** | ≥19 wk | **Provisioned wearables beat the BYOD phone: 11% missing (Oura + Samsung) vs 16% (AWARE smartphone)** — same people, same months. ⚠️ **Same cohort as the mSavorUs row in Part B** — one deployment, two reports |
| [Bae 2023 — binge-drinking JITAI](profiles/aware-binge-drinking-jitai-sensor-loss.md) | **75** | 14 wk | **35.4% of person-days unusable (414/1,168)** — participants disabled GPS via the settings menu after being told sensors were configurable. A **new data-loss class: participant-exercised configurability** |


---

# Part E - Coverage set from the stored Module 1 and 2 PDFs (10 profiles, 2026-09-03)

Built by screening, from full text, the 51 PDFs already stored in the Module 1 and Module 2 literature
folders that carried three or more deployment-reality signals. 39 were unprofiled. 14 papers screened
in and became these 10 profiles (two cohorts are reported by more than one paper), 25 were rejected
with reasons in the ledger. Build report in
[`_coverage-build-report-2026-09.md`](_coverage-build-report-2026-09.md). Three of the ten are Beiwe
as the primary instrument, chosen because each adds something the twelve earlier Beiwe profiles lack.

## Table 9 - Coverage set

| Study | Platform / device | N | Duration | Headline operational number |
|---|---|---|---|---|
| [Shiba 2023, healthcare workers](profiles/oura-tempredict-healthcare-worker-adherence.md) | Oura Ring Gen 2, provisioned | 100 to 91 | 8+ weeks | Ring worn on 87.8% of nights against surveys on 63.8% of days. Residents were the low group on both, 82.8% and 49.8%. Parent TemPredict funnel 65,319 to 63,153 folded in |
| [Truslow 2024, Apple Heart and Movement Study](profiles/apple-heart-movement-study-retention.md) | Apple Watch, BYOD | 82,809 | 1 year | Three retention numbers from one cohort. 3.24% withdrew, 38% quiet on day 365, 28% permanently inactive. Half of withdrawals inside 111 days |
| [Mahalingaiah 2022, Apple Women's Health Study](profiles/apple-womens-health-study-retention.md) | Apple Watch and iPhone, BYOD | 10,000 | 6 months | Monthly survey 62.2% to 34.5% in six months while passive HealthKit cycle logging held at 72.4%. Month-six responders whiter and better educated than enrollees |
| [Moshe 2021, AWARE on iOS plus Oura](profiles/aware-oura-delphi-covid-lockdown.md) | AWARE (custom iOS app) plus participant-owned Oura | 60 to 55 | 30 days | Bring your own ring and iPhone. No hardware cost, five drop-outs, 9.1% sensing missingness, and a cohort 93% White and 80% degree-holding by construction |
| [Pellegrini 2022, four diagnostic groups](profiles/beiwe-transdiagnostic-outpatient-completeness.md) | Beiwe, BYOD | 45 to 38 | 8 weeks | Paid and visit-supported, 84% completed, yet only 39% of participants reached half the expected GPS. Retention and completeness diverge in the same people |
| [Torous, Barnett and Staples 2017 to 2018, schizophrenia pilot](profiles/beiwe-schizophrenia-state-clinic-pilot.md) | Beiwe, BYOD, no payment for app use | 17 to 15 | up to 90 days | The unsupported floor. Coverage 50.2% GPS and 46.9% accelerometer in month one, about half of surveys, one of 17 lost to Wi-Fi-only upload, two of five relapsers uninstalled before hospitalisation |
| [Panda 2021, cancer surgery](profiles/beiwe-cancer-surgery-survey-retention.md) | Beiwe surveys, BYOD | 101 to 74 to 24 | 6 months | 42%, 33% and 24% of consented at 1, 3 and 6 months. Zero of 13 Android users answered at month one, the opposite direction to McInerney 2024 |
| [Vidal Bustamante 2022, a full academic year](profiles/geneactiv-beiwe-college-year-deep-phenotyping.md) | GENEActiv, provisioned, plus Beiwe surveys | 68 to 49 | 256 days | Wristband swaps every 3 to 4 weeks and a 30 Hz to 10 Hz drop over winter break gave 220 usable actigraphy days a person. 88% re-enrolled two years later |
| [Nock 2026, after a psychiatric emergency](profiles/lifedata-post-hospital-suicide-ema.md) | LifeData, BYOD | 619 to 498 | 84 days | First LifeData deployment here. 117 of 619 never answered a survey, initiation ran under 50% and fell, at a dollar a survey. Adults averaged 43 of 84 days |
| [Weingarden 2025, body dysmorphic disorder](profiles/metricwire-beiwe-bdd-remote-ema-passive.md) | MetricWire EMA plus Beiwe passive, BYOD, fully remote | 87 to 83 | 3 months | 72% of 84 prompts answered and 85.9% of days with both streams. Three of 87 produced no passive data. Passive summaries went missing whole days at a time |

Addenda were also written into two existing ALS profiles from four related papers (Berry 2019,
Beukenhorst 2021, Straczkiewicz 2024, Karas 2024) rather than adding a fourth and fifth ALS row.

---

# Cross-cutting patterns

Findings that replicate across **three or more independent studies** are the most trustworthy content
in this module.

1. **Passive data outlasts active data.** Every study reporting both found it: Beiwe/ALS,
   Beiwe/adolescents, RADAR-MDD, mindLAMP, Raugh. Magnitude varies enormously (89% vs 47% in
   adolescents; 57% vs 29% in SHARP), but the direction never reverses. **Exception worth noting:**
   [de Angel 2023](profiles/radar-base-treatment-engagement.md) found smartphone passive data *lower*
   than active data throughout — passive durability is platform- and configuration-dependent, not
   automatic.
2. **Within passive streams, reliability tracks computational and radio demand.**
   Accelerometry > GPS > audio > Bluetooth-tethered wearable. Independently reproduced by
   [Raugh 2021](profiles/dp-schizophrenia-tolerability.md) and
   [de Angel 2023](profiles/radar-base-treatment-engagement.md) on different platforms.
3. **Baseline disease severity generally does *not* predict attrition** — null in RADAR-MDD
   (depression), Beukenhorst (ALS), Huang (bipolar), de Angel (depression). **But symptom dimension
   matters**: baseline *anxiety* did predict attrition (de Angel), as did *negative* symptoms
   (Meyer, Raugh) and time-varying depression severity (Zhang).
4. **OS asymmetry is STREAM-SPECIFIC before it is platform-specific.** This supersedes the earlier "direction not settled" framing. [McInerney 2024](profiles/beiwe-type-2-diabetes-feasibility.md) — a **Beiwe** study, the platform whose prior work favoured iOS — stratified by stream within one cohort and found **iPhones missing 70.0%/70.6% of morning/evening EMA vs Android's 21.3%/26.8% (p<0.001), while accelerometer and GPS showed no significant OS association in the same participants.** That reconciles the apparent contradiction: the earlier iOS-favouring results (Kiang, Yi) measured *passive* streams; the Android-favouring ones measured *active survey delivery*. **Never state an OS effect without naming the stream.** Mechanism unidentified — see Tier 15 Q111/Q111b.

    **Refined 2026-09-02 — there are three distinct kinds of OS effect, not one:**
    (a) **Structural gates** — the stream is unavailable on one OS at all. [Balliu 2024](profiles/aware-stand-mood-prediction-adherence.md) could compute SMS features for only **15 of 183 participants (8.2%)** because iOS does not expose them. There is no mitigation; the choice is binary.
    (b) **Yield differences** — same stream, different completeness. [McInerney 2024](profiles/beiwe-type-2-diabetes-feasibility.md)'s 70% vs 21% EMA miss rate.
    (c) **Breadth differences** — how many stream *types* arrive. [Wu 2023](profiles/aware-alcohol-liver-disease-craving.md) found Android delivering **8.4 vs iOS 4.7 mean sensor types** — Android ahead on breadth, the opposite direction to McInerney's yield finding, **on the same framework**.
    Note also that several dual-platform studies here report **no** OS breakdown at all, which is now a visible reporting gap.

    **Added 2026-09-03.** [Panda 2021](profiles/beiwe-cancer-surgery-survey-retention.md) supplies a contradicting data point on the active stream. On Beiwe in 2017 to 2019, zero of 13 Android users completed the month-one survey and one of 13 at three and six months, while 42 of 61 iPhone users completed month one. That is the opposite direction to McInerney's iOS penalty on the same platform and the same stream. The direction of an OS effect on survey delivery cannot be predicted even from platform and stream together. Logged as Tier 17 Q121. [Torous 2018](profiles/beiwe-schizophrenia-state-clinic-pilot.md) had already found GPS and accelerometer coverage running opposite ways by OS on the same phones in 2018.

4b. **Superseded framing, retained for provenance:** this matrix previously asserted "iOS outperforms Android", then "direction not settled".
   Three Beiwe studies favour iOS: Kiang (GPS non-collection RR 0.66), Yi 2024 (57.3% vs 50.2%
   retention at 6 months; 44.1% vs 26.7% "excellent" GPS compliance). Beukenhorst found no OS effect
   but was underpowered. **Against that**, [Niemeijer 2023](profiles/carp-mpath-sense-performance-study.md)
   — on CARP, with a clean 52/52 iOS/Android split — found **iOS data gaps roughly 6× longer than
   Android's**, and [McClaine 2024](profiles/aware-chemotherapy-engagement.md) on AWARE found Android
   yield *lower* than iOS. Both are Verified and they point opposite ways.
   **The honest reading: OS effects are large, platform- and stream-specific, and cannot be predicted
   from the OS alone.** Anyone planning around an OS assumption must check it for their specific
   platform, sensor and OS version. Logged as Tier 14 Q108.

5. **Support intensity, not participant capability, drives the numbers.** Compare Beukenhorst's
   unsupported 59% against RADAR-MDD's heavily-supported ~80%, and Huang's 99%/89%/47% ordering by
   reminder regime.
6. **Multi-step confirmatory protocols destroy large enrolments.** Apple Heart 419,297→450;
   Fitbit Heart 455,699→1,057. Each vendor handoff is an attrition point.
7. **BYOD trades representativeness for wear compliance.** Cho, Master and Lubitz together make this
   the module's clearest tradeoff.

8. **Incentives buy enrolment persistence, not engagement — and are not the biggest lever.**
   [Mercier 2020](profiles/beiwe-spinal-cord-injury-incentives.md) raised retention 50%→78% with a
   $30/2-month conditional payment, **but survey completion rate did not increase at all**; in the
   same study, *recruitment channel* produced a larger spread (53% vs 21%). At the other extreme,
   [Lubitz 2022](profiles/fitbit-heart-study-afib.md)'s $50-per-visit incentive did not fix its
   funnel, while [Liu 2019](profiles/lamp-schizophrenia-cognition-unpaid.md) achieved 3×-higher
   engagement in *patients than controls* with **no payment at all**, and
   [Soon 2025](profiles/oura-university-freshmen-sleep.md) still lost 10.8% at ~USD 263 per
   participant.

9. **Co-design and recruitment channel outperform payment.**
   [Clark 2025](profiles/metricwire-sgm-youth-ema-feasibility.md) reached **80.21%** — the module's
   highest mental-health compliance — after letting participants set the prompt frequency themselves;
   [Meyer 2018](profiles/sleepsight-schizophrenia-rest-activity.md) reached 91% wear after the user
   group chose the device. Compare Mercier's recruitment-stream spread and
   [Jonker 2021](profiles/withings-postop-remote-monitoring.md)'s 33%→63% from switching to
   face-to-face approach.

10. **The funnel starts before consent, and most studies never report that part.**
    [Cote 2019](profiles/beiwe-spine-disease-mobility.md): **42% of those approached excluded for not
    owning a smartphone.** [Wright 2018](profiles/beiwe-fitbit-gynecologic-cancer-hope.md): treating
    oncologists **gatekept out 8 of 18 eligible patients** before a "100% approach-to-consent" rate.
    [Camargo 2025](profiles/aware-light-smartsense-d-youth-depression.md): **29% could not run the app
    on their own handset.** [Helmer 2025](profiles/movesense-palliative-support-trial.md): 95.6%
    excluded at consent.

11. **Data can be present and wrong — completeness dashboards show green.** [Bladon 2026](profiles/connect-multi-wearable-psychosis.md) found **98% of Samsung sleep records were present but corrupt** (duplicated start timestamps, missing end times). No completeness metric in this module would have caught it. **Validate structure, not just presence.**

12. **Vendor policy changes are a quantified study risk.** In the same study, **17 of 20 Samsung escalations traced to a mid-study Samsung privacy-policy change.** Compare RADAR-MDD losing call/SMS logs to a Google Play permissions change. Budget for it.

13. **Support raises completion; payment raises persistence; neither raises engagement with interactive content — and interactive content is the component that stratifies demographically.** Reconciles [Dewitte's](profiles/mpath-dementia-esm-feasibility.md) unpaid 80% in dementia, [Shen's](profiles/sensorkit-techsans-older-adults.md) uncompensated withdrawal, and [Carlson's](profiles/garmin-low-income-physical-activity.md) paid-but-demographically-stratified reply rates.

14. **Research-infrastructure failure is a distinct data-loss class — and it is the one self-hosting owns.** Not device failure, not OS restriction, not participant behaviour: the *study's own* servers and network. [Borelli 2025](profiles/aware-msavorus-passive-completeness-companion.md) lost data to server congestion; [Bae 2023](profiles/aware-binge-drinking-jitai-sensor-loss.md) to Wi-Fi-gated upload; [Aledavood 2024](profiles/aware-momo-mood-mood-disorders.md) provisioned a **router per participant** to avoid it. Three independent studies clear the bar for a pattern. **This is a direct input to the self-host-vs-SaaS decision in Module 2** — a cost that moves to the vendor under SaaS and stays with the team under self-hosting.

15. **Participant-exercised configurability is its own data-loss class.** [Bae 2023](profiles/aware-binge-drinking-jitai-sensor-loss.md) lost **35.4% of person-days** because participants, having been told the sensors were configurable, turned GPS off in the settings menu. Telling participants they are in control is ethically right and operationally expensive; budget for it rather than being surprised.

17. **Withdrawal, daily non-participation and permanent inactivity are three different retention numbers, and a cohort paper should report all three.** [Truslow 2024](profiles/apple-heart-movement-study-retention.md) gives 3.2%, 38% and 28% at one year for the same 82,809 people. Any one alone would give a different impression. [Mahalingaiah 2022](profiles/apple-womens-health-study-retention.md) reaches the same conclusion in the sibling cohort by setting survey response (34.5% at month six) against passive HealthKit logging (72.4%).

18. **The unsupported floor and the supported ceiling on one platform.** [The Beiwe schizophrenia pilot](profiles/beiwe-schizophrenia-state-clinic-pilot.md), with no payment for app use and no reminders, returned about half the scheduled passive data and half the surveys and lost one of 17 entirely to Wi-Fi-only upload. [Pellegrini 2022](profiles/beiwe-transdiagnostic-outpatient-completeness.md), paid and visit-supported on the same platform, kept 84% of people but still had only 39% reach half the expected GPS. Support buys retention. It does not buy passive completeness, which sharpens both finding 1 and finding 5.

19. **A bring-your-own-everything inclusion rule is the cheapest deployment and the least representative.** [Moshe 2021](profiles/aware-oura-delphi-covid-lockdown.md) required an iPhone and an Oura Ring already owned. Hardware cost was zero and five of 60 left in a month. The cohort was 93% White, 80% degree-holding and iOS by construction. Same mechanism as finding 7, applied at the inclusion criterion rather than the recruitment channel.

16. **Remote incentivised studies attract fraud, and platform metadata can catch it.**
    [Siebers 2025](profiles/metricwire-fraudulent-participation.md) is the only study here addressing
    an adversarial failure mode — MetricWire's carrier-country field unmasked 10 fraudulent
    participants; a manual checklist later blocked 37.

---

## ⚠️ Definitions are not standardised — read before comparing cells

**The numbers in this file are not directly comparable across rows.** Studies define their
denominators differently, and few state the definition prominently:

- **"Wear time"** may mean any heart-rate sample in a 15-minute window (Matcham), the manufacturer's
  own wear algorithm (Muurling, Lubitz), or ≥10 hours plus ≥100 steps (Master).
- **"Data availability" / "completeness"** ranges from *any* data on a given day (Beukenhorst) to a
  single data point per hour (Matcham) to ≥8 hours of passive data plus one active task
  (de Angel) to actual-over-expected samples against a known duty cycle (Kiang, Cohen, Böttcher).
  **[de Angel et al.](profiles/radar-base-treatment-engagement.md) state explicitly that no standard
  threshold exists** and that their definition differs from Matcham's.
- **"Retention"** may mean completing outcome assessments (Matcham), still contributing any data to a
  given stream (Zhang), or not formally withdrawing (Muurling).
- Duty-cycled sampling means several "completeness" figures are computed against a *designed* partial
  denominator; others are against wall-clock time.

**The extension set makes this worse, not better, and supplies the definitive illustration.**
[Kivelä 2024](profiles/avicenna-ema-suicidal-ideation-iatrogenic.md) publishes **two defensible
acceptability rates for the same study, 59 percentage points apart** — 39% (of everyone who signed
up) and 98% (of eligible people who completed intake). Both are honest; the denominator is the whole
story. [Dennard 2025](profiles/mpath-avatar2-esm-engagement.md)'s 39.1% — the lowest figure in this
matrix — is an artefact of having to define completion as *100%-complete* because the platform's
partial-save export was unreliable. And [Straczkiewicz 2024](profiles/actigraph-als-upper-limb-wear-time.md)
shows the same raw accelerometer data yielding an analytic **N of 202, 240 or 308** depending only on
whether the wear-time threshold is set at 21, 16 or 8 hours per day.

**Use this matrix to compare patterns and orders of magnitude, not to rank platforms.** Where a
decision turns on a specific number, read the profile and then the paper — and check the
denominator.

A second caveat: **all Beiwe figures here predate the platform's `heartbeat`/keepalive feature**
(globally enabled 2024-05-29) and should be treated as **pre-heartbeat lower bounds** — see
[`profiles/beiwe-als-adherence.md`](profiles/beiwe-als-adherence.md) and Tier 14 Q106 in
[`../shared/unresolved-questions.md`](../shared/unresolved-questions.md).
