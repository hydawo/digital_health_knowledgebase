# McClaine et al. 2024 — Engagement with three concurrent data streams during chemotherapy (AWARE + Fitbit), N=162

## Quick Facts

| Field | Details |
|---|---|
| Citation | McClaine S, Fedor J, Bartel C, Chen L, Durica KC, Low CA. "Engagement With Daily Symptom Reporting, Passive Smartphone Sensing, and Wearable Device Data Collection During Chemotherapy: Longitudinal Observational Study." *JMIR Cancer* 2024;10:e57347. DOI [10.2196/57347](https://doi.org/10.2196/57347). PMID 39656513 / PMC11668979. |
| Study design | Prospective observational cohort with engagement as the **primary** outcome. Day-level binary adherence outcomes modelled with logistic generalized estimating equations (GEE), univariable then a priori multivariable. |
| Sample size (enrolled / analyzed) | **320 approached → 167 enrolled (52.2%) → 162 analyzed** (146/162 completed, 90.1%; 16/162 withdrew, 9.9%). Cohort collection was ongoing at the time of writing. |
| Population | Adults receiving outpatient chemotherapy for a solid tumour at a large US academic cancer centre (plus 7 from a community registry). Mean age **59.5 (SD 11.8, range 28–92)**; 62.3% female; **83.3% White**; 63.6% **stage 4**; 60.5% iOS. |
| Duration | **90 days** per participant, enrolled March 2020 – June 2023. |
| Devices/platforms used | **[AWARE](../../module-02-digital-phenotyping/profiles/aware-framework.md)** (passive smartphone sensing) + **MoSHI Surveys** (in-house notification/survey app) + **[Fitbit](../../module-01-wearables/profiles/fitbit-google.md) Inspire** (provisioned). Feature extraction via **RAPIDS**. |
| Funding/COI | Academic — Henry L. Hillman Foundation, NCI R37CA242545, CTSI UL1TR001857, NCI P30CA047904. **The survey app (MoSHI Surveys) was developed by the senior author's team, and AWARE by "our research collaborators"** — a partial developer relationship, disclosed in-text rather than as a formal COI. |
| Last verified | 2026-09-01 |

## Summary

The clearest side-by-side measurement in this module of **active vs. two different passive streams in one cohort, over 90 days, in an acutely ill population** — and the first study this module has found that examines predictors of engagement with *passive smartphone sensing* during cancer treatment.

The headline triple: **daily symptom surveys 61% (SD 27%) of days; smartphone passive data 73% (SD 35%); Fitbit 70% (SD 33%)**. Passive again beat active, but only by ~10 points, not the roughly 2× seen in [mindLAMP's three-site study](mindlamp-relapse-3site.md) or [Beiwe/ALS](beiwe-als-adherence.md). The narrower gap is best read as an artefact of the definitions used — a "completed" survey was only 50% complete, whereas passive days required ≥8 valid sensing hours.

The findings a study designer should carry away are about *who* disengages. **Non-White participants had roughly half the odds of completing symptom surveys (OR 0.49) and about a third of the odds of yielding wearable data (OR 0.35)** relative to White participants — in a cohort that was already 83.3% White. And, cutting hard against the standard assumption, **older age predicted *better* Fitbit engagement (OR 1.03 per year)**.

## Instrumentation and Deployment Model

**Mixed BYOD/provisioned.** Participants used **their own smartphone** (owning one was an eligibility criterion), but the **Fitbit Inspire was provided** and could be kept at study end.

Three streams:

| Stream | App | Participant burden |
|---|---|---|
| Daily symptom survey (NCI PRO-CTCAE-based, 15 symptoms) | MoSHI Surveys | Active; one notification/day at a participant-chosen time |
| Passive smartphone sensing | AWARE (Android + iOS) | Keep app running in background |
| Activity, HR, sleep | Fitbit Inspire | Wear continuously; charge ~every 10 days; sync via Fitbit app |

**The operational apparatus is as important as the technology, and the authors say so.** A secure web dashboard carried one column per data source and **raised a flag after 3 consecutive days without data**. It was reviewed **at least three times a week**; flagged participants were contacted by their preferred channel, escalated to a phone call or an in-person visit at their next treatment if the flag persisted a week, then re-contacted every 1–2 weeks. All contacts were logged. The authors explicitly warn that **"it is likely that we would have lower rates of engagement without these interactions with research staff"** — meaning every number below is an *actively-managed* figure, not a hands-off one.

## Recruitment and Retention

- **320 approached, 167 enrolled (52.2%).** Stated reasons for declining: *concerns about technology*, feeling overwhelmed, being too busy, not feeling well, not interested. Technology concern being named first in a chemotherapy population is itself a recruitment-design fact.
- **90.1% completed the 90-day protocol; 9.9% withdrew.**
- Completers and withdrawers **did not differ on any measured characteristic except insurance plan type (P=.02)**; all others P>.08. This reproduces the null found across four other studies in this module — baseline severity generally does not predict who drops out.

## Data Completeness and Technical Issues

**Definitions used (they are not interchangeable with any other study in this module):**

- *Survey adherence* — a response **started on that day and ≥50% complete**.
- *Phone adherence* — **≥8 valid hours** of data from **any** of 14 AWARE sensors (activity recognition, app crashes, apps foreground, app notifications, battery, Bluetooth, calls, keyboard, light, locations, SMS, screen, Wi-Fi connected, Wi-Fi visible). A "valid hour" = a 60-minute window with ≥1 row of data in ≥30 of those minutes.
- *Fitbit adherence* — **≥8 valid hours of intraday heart-rate data**.

**Mean per-participant adherence over enrolled days:**

| Stream | Mean | SD |
|---|---|---|
| Daily symptom survey | **61%** | 27% |
| Smartphone (AWARE) | **73%** | 35% |
| Fitbit | **70%** | 33% |

**Predictors (multivariable GEE):**

| Factor | Surveys | Phone | Fitbit |
|---|---|---|---|
| Non-White vs White | **OR 0.49** (0.29–0.81), P=.006 | — | **OR 0.35** (0.17–0.73), P=.005 |
| Stage 4 cancer | **OR 0.69** (0.48–1.00), P=.048 | — | — |
| Weekend | **OR 0.90** (0.83–0.97), P=.008 | — | — |
| Age (per year) | — | — | **OR 1.03** (1.01–1.06), P=.01 |
| Better baseline cognitive function | — | — | **OR 1.18** (1.03–1.34), P=.02 |
| Greater baseline depressive symptoms | — | **OR 1.18** (1.03–1.36), P=.02 (fewer symptoms → more engagement) | — |
| Days since last chemotherapy | — | fewer days → more engagement | fewer days → more engagement |

**A named technical asymmetry.** Phone data yield was **systematically lower on Android than iOS "due to differences in sensor data sampling frequencies across platforms"**, and every phone-yield model had to be adjusted for phone type as a result. Note the direction: this is the **opposite** of the usual expectation that Android's more permissive background access yields more data — here the *sampling schedule the framework applies per OS* dominated. Compare [Niemeijer et al.](carp-mpath-sense-performance-study.md), who found iOS gaps far *longer* than Android gaps on a different framework. **These two findings are not reconcilable from the published text and should be treated as platform- and configuration-specific, not as a general rule.**

The authors offer no counts of app crashes, device failures, or sync failures — an absence worth noting given that AWARE itself logs app crashes as a sensor.

## Feasibility Findings

The authors' own conclusion: engagement with all three streams over 90 days was **feasible**, "even among older patients and patients with advanced cancer receiving active treatment."

Their two framed lessons:

1. **The digital divide may widen existing health disparities** — non-White participants engaged less with both the survey and the wearable, in a cohort recruited at a single academic centre.
2. **The age assumption is wrong, at least for wearables** — older participants engaged *more*. The authors speculate about fewer competing demands (work, childcare), and separately note that better self-reported cognition also predicted Fitbit engagement, so "older" and "cognitively impaired" should not be collapsed.

Recommendations they make: experiment with reminder formats and schedules, onboarding and training, and levels of integration with the clinical care team; and study engagement **without** research-staff monitoring, which their own design cannot.

## Relevance to Future Study Design

1. **Budget for a monitoring apparatus, or discount the numbers.** A three-times-weekly dashboard review with a 3-day no-data flag and an escalating contact ladder produced 61/73/70%. A study without that staffing should not plan against these figures.
2. **Race predicted disengagement more strongly than illness severity did.** OR 0.35 for wearable data is a large effect. Any study whose analytic sample is defined by adherence thresholds will therefore be *more* White than its enrolled sample — the same mechanism [Cho et al.](byod-demographic-imbalance.md) document for BYOD designs, arriving here through adherence rather than device ownership.
3. **Stop treating older adults as the adherence risk.** Two studies in this module now find the opposite direction for wearables.
4. **Weekends and time-since-treatment are schedulable variables.** Engagement rose the closer a day was to a chemotherapy visit — partly because coordinators could troubleshoot in person. Anchoring support contacts to treatment days is nearly free.
5. **Report the definition beside the number.** "61% survey adherence" here means *≥50% of one survey started that day*; [Dennard et al.](mpath-avatar2-esm-engagement.md) counted only **100%-complete** questionnaires and got 39.1%. The two figures are not comparable.

## Evidence Confidence

**Verified** — the enrolment funnel (320/167/162), completion and withdrawal counts, all three adherence means and SDs, every odds ratio and confidence interval quoted, and all three adherence definitions. Read from the full text (Europe PMC PMC11668979), 2026-09-01.

**Reported** — the claim that Android/iOS yield differences are due to sampling-frequency differences. Stated by the authors as an explanation for a modelling decision, with no supporting measurement in the paper.

**Unclear** — how much of the engagement figures is attributable to the staff-monitoring apparatus. The authors flag this as a limitation but cannot quantify it, and it is the single largest source of uncertainty in transferring these numbers.

**Stated limitations:** smartphone ownership and English literacy were eligibility criteria, skewing the sample toward higher technology literacy; selection bias, since people unlikely to engage were likelier to decline; day-to-day symptom burden may itself drive survey response, unmeasured; and the ≥50%/≥8-hour thresholds are conventions, with results potentially sensitive to them.

**COI:** the survey app is the senior author's team's own product and AWARE is described as built by "our research collaborators." No competing-interests statement addressing this appears in the extracted text. The engagement figures are unflattering rather than promotional and no comparator platform is evaluated, which limits the exposure — but the framing of the system as feasible is the authors' own.

## Key Links

- Paper (OA, CC BY): https://doi.org/10.2196/57347
- Europe PMC: https://europepmc.org/article/PMC/PMC11668979
- Analysis code (per paper): GitHub, cited as reference 34
- RAPIDS pipeline: https://www.rapids.science/
- Local PDF: `../literature/2024-mcclaine-jmircancer-aware-fitbit-chemotherapy-engagement.pdf`

## Related profiles

- Platform: [AWARE](../../module-02-digital-phenotyping/profiles/aware-framework.md)
- Device: [Fitbit / Google](../../module-01-wearables/profiles/fitbit-google.md)
- Same passive > active ordering: [`mindlamp-relapse-3site.md`](mindlamp-relapse-3site.md), [`beiwe-als-adherence.md`](beiwe-als-adherence.md)
- Demographic skew in who supplies data: [`byod-demographic-imbalance.md`](byod-demographic-imbalance.md), [`beiwe-missing-data-sociodemographic.md`](beiwe-missing-data-sociodemographic.md)
- Contradictory OS-platform finding: [`carp-mpath-sense-performance-study.md`](carp-mpath-sense-performance-study.md)

## Sources

1. McClaine S, et al. *JMIR Cancer* 2024;10:e57347. DOI 10.2196/57347. Full text read from Europe PMC (PMC11668979), 2026-09-01. Establishes every figure in this profile.
