# Kiang et al. 2021 — Sociodemographic characteristics of missing data in digital phenotyping: a six-study Beiwe meta-study, N=211, 29,500 person-days

## Quick Facts

| Field | Details |
|---|---|
| Citation | Kiang MV, Chen JT, Krieger N, Buckee CO, Alexander MJ, Baker JT, Buckner RL, Coombs G III, Rich-Edwards JW, Carlson KW, **Onnela JP**. "Sociodemographic characteristics of missing data in digital phenotyping." *Scientific Reports* 2021;11:15408. DOI [10.1038/s41598-021-94516-7](https://doi.org/10.1038/s41598-021-94516-7). PMC8322366. |
| Study design | **Meta-study** pooling individual-level sensor *metadata* from six independent Beiwe studies; Bayesian hierarchical negative binomial regression with study- and participant-level random intercepts, plus sensitivity and stratified analyses |
| Sample size (enrolled / analyzed) | **211 participants** across 6 studies; **29,500+ person-days**; **8.3 billion sensor measurements** (8.1bn accelerometer, 113m GPS) in 81m measurement groupings. Regression N = 28,218 (accelerometer) / 28,053 (GPS) participant-days. |
| Population | Pooled and deliberately heterogeneous: **Studies A, C, E, F** = healthy Harvard College undergraduates; **Study B** = McLean Hospital patients at risk for mania and psychosis; **Study D** = healthy female nurses from Nurses' Health Study 3. Mean age 25.4 (SD 10.8); 66% female; 67% high-school education or less; 55% non-Hispanic White, 18% Asian, 15% non-Hispanic Black. **77% Android / 23% iOS.** |
| Duration | Studies conducted 2015–2018; per-participant follow-up varied by study protocol (time-based, not data-volume-based), spanning up to ~900 days on the pooled timeline |
| Devices/platforms used | **[Beiwe](../../module-02-digital-phenotyping/profiles/beiwe.md)** — participants' own smartphones (BYOD), Android and iOS. Accelerometer and GPS only. |
| Funding/COI | Academic (Harvard Chan, Stanford, McLean, Toronto). Onnela — Beiwe's originator — is corresponding author. |
| Last verified | 2026-08-31 |

## Summary

The reference paper on **how much smartphone sensor data you should actually expect to get, and from
whom**. Rather than reporting one study's completeness, it pools six Beiwe studies spanning healthy
undergraduates, psychiatric patients, and mid-career nurses, and models sensor non-collection as an
outcome in its own right.

Its central numbers are the planning figures every smartphone-phenotyping study design should start
from: **at study start, ~19% of expected accelerometer data and ~27% of expected GPS data are simply
not collected**, and non-collection then **grows by roughly 0.5%/week (accelerometer) and 0.9%/week
(GPS)** for the study's duration. That decay is close to linear and remarkably consistent, which
makes it usable for prospective power calculations.

The equity findings are more reassuring than the field's anxieties would predict, with one exception.
**GPS non-collection did not differ by race/ethnicity, education, age, or gender.** Accelerometer
non-collection did not differ by sex, education, or age — but **Black participants had ~64% higher
accelerometer non-collection than White participants**, with wide uncertainty. And **iOS users had
substantially lower GPS non-collection than Android users**, which is a device-market effect that
maps onto socioeconomic status even where the demographic coefficients themselves are null.

## Instrumentation and Deployment Model

Fully BYOD across both operating systems. All six studies used Beiwe with an alternating duty cycle
(the paper's worked example: GPS on 1 minute in every 10, giving a designed 10% sampling coverage —
2.4 hours of data per 24-hour period).

**The methodological move that makes the paper work:** because a duty-cycled sensor has a *known
expected data volume at design time*, actual-versus-expected is directly computable, and
non-collection can be diagnosed rather than inferred. The authors formalise the distinction:

- **Missingness by design** — the intended consequence of the sampling schedule the investigator
  configured (e.g. GPS off 9 minutes in 10 to save battery). Not a problem; it is the design.
- **Missingness due to sensor non-collection** — everything else: the participant forgets to charge
  the phone, disables GPS, or uninstalls the app; or the OS restricts sensor access for performance
  reasons. **The technological causes are proprietary and therefore unknown to the investigator**,
  which is precisely why it must be measured empirically.

**Privacy-preserving analysis worth noting as a practice:** only **timestamps** were analysed. GPS
coordinates and accelerometer values were stripped before analysis, because the research question
needed only metadata. This is a reusable pattern for methods work on sensitive sensor corpora.

Accelerometer and GPS were recorded **independently on the same phones** — disabling GPS did not stop
accelerometer collection — which is why the two sensors can show different demographic patterns.

## Data Completeness and Technical Issues

**The headline planning figures** (conditional average rate of sensor non-collection at study start):

| Sensor | Non-collection at baseline | Weekly increase |
|---|---|---|
| **Accelerometer** | **19.1%** (95% CI 8.9–45.8) | **+0.5%/week** (95% CI 0.4–0.7) |
| **GPS** | **26.9%** (95% CI 16.8–45.9) | **+0.9%/week** (95% CI 0.7–1.0) |

Note the credible intervals are wide — the upper bounds approach 46% for both sensors. Plan against
the interval, not the point estimate.

**Operating system — the largest single effect found:**

- **iOS users had ~34% lower GPS non-collection than Android users** (RR 0.66, 95% CI 0.45–0.95).
- The direction **reverses for accelerometer**: iOS users had *higher* accelerometer non-collection
  (RR 1.30), though the interval crosses 1 (0.80–2.11).

The authors read this as evidence of **systematic differences between the two operating systems in
how sensor access is handled** — not a participant-behaviour effect. Since sensor-by-OS behaviour is
proprietary and changes with OS releases, this is a moving target.

**Sociodemographic results** (relative rate; reference groups: non-Hispanic White, less than a
4-year degree):

| Covariate | Accelerometer RR (95% CI) | GPS RR (95% CI) |
|---|---|---|
| Time (per week) | **1.005 (1.004–1.007)** | **1.009 (1.007–1.010)** |
| iOS user | 1.301 (0.803–2.114) | **0.660 (0.453–0.948)** |
| Male | 0.821 (0.576–1.171) | 0.822 (0.607–1.106) |
| 4-year degree or higher | 0.786 (0.332–1.839) | 0.688 (0.339–1.416) |
| **Non-Hispanic Black** | **1.638 (1.059–2.517)** | 1.329 (0.907–1.953) |
| Asian | 0.724 (0.486–1.100) | 0.898 (0.630–1.295) |
| American Indian | 1.137 (0.637–2.047) | 1.241 (0.758–2.044) |
| Other/Multiple | 0.978 (0.232–4.074) | 0.926 (0.257–3.240) |
| Age (per 10 years) | 1.010 (0.973–1.048) | 1.011 (0.982–1.042) |

**The one positive equity finding: Black participants had ~64% higher accelerometer non-collection
than White participants** (95% CI 5.9%–252%). The authors flag the substantial uncertainty
themselves. **No corresponding GPS difference was found**, and no education, age or gender
differences were found for either sensor.

**Variance decomposition — the practical takeaway for study design:** **individual-level variation
exceeded study-level variation** for both sensors (accelerometer σγ 1.012 vs σδ 0.721; GPS σγ 0.888
vs σδ 0.295). Who the participant is matters more than which study they are in. Models explained 38%
(accelerometer) and 42% (GPS) of variance in non-collection by Bayes R².

## Feasibility Findings

The authors' stated conclusion is a feasibility endorsement: the results **"demonstrate the
feasibility of using smartphone-based digital phenotyping across diverse populations, for extended
periods of time, and within diverse cohorts."** The demographic null results are the basis for
that — with the accelerometer/Black participants exception noted.

**Their design-level recommendation, stated as a principle:** *design-based* mitigation of missing
data is preferable to statistical fixes after the fact. They are explicitly critical of the two
common alternatives — setting arbitrary data-"quality" thresholds and discarding high-missingness
blocks, or statistical modelling that relies on strong and unverifiable assumptions about the
missingness mechanism — and note that **statistically principled imputation for digital phenotyping
data barely exists**. The corollary: budget the ~19%/27% baseline and the weekly decay into the
sampling design and sample size up front, rather than planning to repair it in analysis.

They also note that non-collection missingness subdivides into MCAR/MAR/MNAR, that distinguishing
these matters at analysis, and that doing so is out of this paper's scope — an honest and important
open problem.

## Relevance to Future Study Design

1. **Use 19% (accelerometer) and 27% (GPS) baseline non-collection, plus 0.5%/0.9% per week, as
   *conservative* planning assumptions for a duty-cycled Beiwe-style deployment.** Over a 52-week
   study that implies GPS non-collection rising from ~27% to roughly ~74% — a very large effective
   loss of person-time that a naive power calculation would miss entirely. Caveat: these are
   **pre-heartbeat** figures (see Evidence Confidence); a current Beiwe deployment with heartbeat
   enabled should do better, by an amount not yet publicly quantified.
2. **Duty-cycle your sensors so that expected volume is known at design time.** Without a known
   denominator you cannot distinguish designed missingness from failure, and the paper's whole
   analysis becomes impossible. This is a concrete argument for configurable-sampling platforms.
3. **Do not assume equal data yield across operating systems.** The iOS/Android GPS gap is
   substantial and sensor-specific, and it interacts with the socioeconomic composition of the
   sample even though the demographic coefficients are individually null.
4. **The demographic nulls are genuinely reassuring but should not be over-read** — this is 211
   people, heavily weighted to undergraduates and nurses, and the one significant finding runs
   against Black participants on accelerometer.
5. **Recruit and model at the individual level.** Individual variation dominated study-level
   variation, so per-participant monitoring beats cohort-level dashboards for catching data loss.
6. **Analyse timestamps, not payloads, when studying data quality** — a cheap privacy win.

## Evidence Confidence

**Verified** for the non-collection rates, weekly trends, regression estimates and variance
components — primary reported results with full credible intervals, read from the published PDF, in
a paper whose sole purpose is this measurement.

**Corroborated → Unclear** for the Black-participant accelerometer finding specifically: the 95% CI
is 1.06–2.52 (i.e. 5.9% to 252% higher), which excludes 1 but is extremely wide, and there is **no
corresponding GPS effect**. The authors describe it as carrying "substantial uncertainty". Treat as
a signal warranting replication, not an established quantity.

**Confounding to weigh in the pooled design:** OS is not randomly assigned. The cohorts are
77% Android overall, and Android/iOS ownership correlates with socioeconomic status in the US, so the
OS effect and the demographic effects are entangled in ways this design cannot separate. The authors
do not claim otherwise.

**Generalisability limits:** four of six studies are Harvard undergraduates, giving a young
(mean age 25.4), highly-selected pooled sample in which "high school education" mostly means
"currently an undergraduate" rather than terminal educational attainment. Data are from **2015–2018**
— several Android and iOS generations ago, and the paper itself argues OS sensor policies are the
main driver of the largest effect it found, so **the absolute rates are the most likely part of this
paper to have drifted** and should be re-verified against a recent deployment before being used as
planning figures.

**Specifically superseded in one respect:** these rates predate Beiwe's **heartbeat/keepalive**
mechanism — a scheduled server-side push notification that wakes the app so background collection
resumes, globally enabled 2024-05-29 (**Verified**, `onnela-lab/beiwe-backend` commit history; see
[`beiwe-als-adherence.md`](beiwe-als-adherence.md) for the development timeline). Heartbeat targets
exactly the failure mode this paper measures — the app falling out of the foreground and the OS
suspending its sensor access — so the 19%/27% baselines and the 0.5%/0.9%-per-week decay should be
read as **pre-heartbeat lower bounds on data yield**, not as current Beiwe performance. The magnitude
of the improvement is not publicly published; logged in `../../shared/unresolved-questions.md`.

**COI:** Onnela, Beiwe's originator, is corresponding author. As with
[Beukenhorst et al.](beiwe-als-adherence.md), the findings are unflattering to the platform in the
sense that matters (a quarter of GPS data is missing from the outset and degrades weekly), and no
competitor comparison is made, so the COI has little to distort here.

## Key Links

- Paper (OA): https://doi.org/10.1038/s41598-021-94516-7
- Europe PMC: https://europepmc.org/article/PMC/PMC8322366
- Local PDF: `../literature/2021-kiang-scientificreports-sociodemographic-missing-data-digital-phenotyping.pdf`

## Related profiles

- Platform: [Beiwe](../../module-02-digital-phenotyping/profiles/beiwe.md)
- Companion — same platform, why passive collection needs active engagement:
  [`beiwe-als-adherence.md`](beiwe-als-adherence.md)
- Equity counterpart in a consumer-wearable BYOD design:
  [`byod-demographic-imbalance.md`](byod-demographic-imbalance.md)
- Contrast — per-stream retention on a different platform:
  [`radar-mdd-longterm-engagement.md`](radar-mdd-longterm-engagement.md)

## Sources

1. Kiang MV, et al. *Scientific Reports* 2021;11:15408. DOI 10.1038/s41598-021-94516-7. Full text and
   tables read from the published PDF (via Europe PMC, PMC8322366), 2026-08-31. Establishes every
   figure in this profile.
