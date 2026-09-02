# Cohen et al. 2023 — SHARP: mindLAMP relapse prediction across three sites in two countries, N=132

## Quick Facts

| Field | Details |
|---|---|
| Citation | Cohen A, Naslund JA, Chang S, Nagendra S, Bhan A, Rozatkar A, Thirthalli J, Bondre A, Tugnawat D, Reddy PV, Dutt S, Choudhary S, Chand PK, Patel V, Keshavan M, Joshi D, Mehta UM, **Torous J**. "Relapse prediction in schizophrenia with smartphone digital phenotyping during COVID-19: a prospective, three-site, two-country, longitudinal study." *Schizophrenia* 2023;9:6. DOI [10.1038/s41537-023-00332-5](https://doi.org/10.1038/s41537-023-00332-5). PMC9880926. |
| Study design | Prospective longitudinal cohort (SHARP — Smartphone Health Assessment for Relapse Prevention); **interim report on the first half of an ongoing collection**. Multivariate anomaly detection + changepoint detection, benchmarked against a naive logistic regression. |
| Sample size (enrolled / analyzed) | **132 analyzed** — 76 with schizophrenia (20 of whom relapsed, 56 did not) and 56 healthy controls. By site: **Boston 33, Bangalore 49, Bhopal 50.** |
| Population | Adults with schizophrenia plus age-, sex- and education-matched controls. Mean age 32.3 (SD 8.1). **74.2% Asian overall** — a genuinely non-Western-majority digital phenotyping cohort, which is rare. Sites differed significantly on age (p=0.001), sex (p=0.004), race, ethnicity and education (all p<0.001). |
| Duration | Enrolled for a mean of **156 days (SD 65)** overall; Boston 145 (SD 80), Bangalore 195 (SD 66), Bhopal 126 (SD 18). Intended up to 1 year. Ran during COVID-19. |
| Devices/platforms used | **[mindLAMP](../../module-02-digital-phenotyping/profiles/mindlamp.md)** — open-source smartphone app. Passive: geolocation, accelerometer, screen state. Active: surveys. Plus REDCap for clinical scales. |
| Funding/COI | Academic — Beth Israel Deaconess/Harvard Medical School, NIMHANS Bengaluru, Sangath and AIIMS Bhopal. **Torous, mindLAMP's lead developer, is senior and corresponding author.** |
| Last verified | 2026-08-31 |

## Summary

The only study in this module that deploys a digital phenotyping platform across **markedly
different cultures, languages, and healthcare contexts** — an urban US site, an urban Indian site,
and a more rural Indian site — and asks whether the same system works in all three. It is included
here not for its relapse-prediction result but for what it documents about **running one platform
across sites with very different infrastructure**, and for a data-quality number that should
recalibrate expectations across this whole module.

That number: **average active data quality of 28.5% and passive data quality of 57.4%.** These are
completeness ratios against everything the protocol expected. Roughly seven in ten expected survey
responses never arrived, and over four in ten expected passive datapoints never arrived — and the
authors state, credibly, that this was **"comparable to or even exceeded"** several other published
studies. Anyone budgeting a phenotyping study off headline retention figures rather than
completeness ratios should read this table first.

The study also documents a deployment practice worth copying: a **one-week trial period** that
screened out participants whose phones did not actually produce data.

## Instrumentation and Deployment Model

**Hybrid BYOD.** Participants used their own smartphone if it was mindLAMP-compatible and could
collect adequately. **If a participant at either Indian site lacked a compatible phone, they were
provided a Samsung Galaxy M31 with cellular service** — device *and* connectivity, which is a
materially larger provisioning commitment than most studies make and a prerequisite for the sites
being comparable at all.

**The one-week trial period — the most transferable operational detail here.** Before full
enrolment, data collection was measured for a week. **If a participant had multiple days of no
passive data collection, they did not pass.** This is a run-in screen implemented in practice, and
it is the same mechanism [Beukenhorst et al.](beiwe-als-adherence.md) recommend from their
completeness data. Note the consequence for interpreting the numbers below: **the 57.4% passive data
quality is measured on a cohort already filtered for phones that demonstrably worked.**

**Data streams:** passive — geolocation, accelerometer, screen state. Active — in-app surveys.
Monthly, a research assistant administered PANSS in person (NIMHANS, Sangath-AIIMS) or virtually
(BIDMC, over StarLeaf, a HIPAA-compliant video platform), after which participants completed PHQ-9,
GAD-7, SF-36, SFS, PSQI, WSS and BASIS-24 within 24 hours via REDCap. BACS was administered at
intake, 6 months and 12 months.

The app was **co-designed with patients, family members and clinicians across all three sites** —
not adapted centrally and shipped outward.

## Recruitment and Retention

Enrolment duration varied substantially and informatively by site: **Bangalore 195 days (SD 66),
Boston 145 (SD 80), Bhopal 126 (SD 18)**. Bhopal's very low standard deviation alongside its low
mean suggests a tightly bounded participation window rather than individually varying dropout.

**20 participants experienced a clinical relapse** before the 1 Aug 2022 cutoff (17 had one, 3 had
two). Relapse distribution across sites was **not significantly different** (χ²=3.98, df=2, p=0.14):
Boston 9, Bangalore 8, Bhopal 3.

Relapse ascertainment: 5 tied to hospitalisation reports, 2 to suicide attempts or significant
suicidal ideation, 4 detected via ≥25% increases in monthly PANSS, and 9 from sudden significant
symptom increases requiring clinical intervention. All identified through monthly self-report at
in-person or virtual consultations, or by monthly medical-record review.

## Data Completeness and Technical Issues

**Data quality — defined as actual datapoints collected ÷ datapoints expected if every survey were
completed and every phone transmitted all passive data.**

| | **Active data quality** | | | | **Passive data quality** | | | |
|---|---|---|---|---|---|---|---|---|
| | Boston | Bangalore | Bhopal | **Total** | Boston | Bangalore | Bhopal | **Total** |
| Relapsed (n=20) | 0.321 | 0.360 | **0.118** | 0.326 | 0.555 | 0.611 | 0.660 | 0.591 |
| Not relapsed (n=56) | 0.277 | 0.238 | 0.311 | 0.271 | 0.533 | 0.519 | 0.623 | 0.555 |
| Controls (n=56) | 0.303 | 0.225 | 0.339 | 0.280 | **0.840** | 0.482 | 0.642 | 0.585 |
| **Total** | 0.298 | 0.258 | 0.316 | **0.285** | 0.596 | 0.523 | 0.635 | **0.574** |

Observations that matter for design:

- **Passive completeness roughly doubles active completeness** (57.4% vs 28.5%) — the same ordering
  seen in [Beukenhorst](beiwe-als-adherence.md) and [Zhang](radar-mdd-longterm-engagement.md), now
  reproduced on a third platform in a third clinical population across two countries.
- **Site differences in passive quality are modest** (52.3%–63.5%), which is the study's strongest
  implicit argument that the platform ported successfully. **Bhopal — the more rural site — had the
  *highest* passive data quality (63.5%)**, cutting against an assumption that lower-resource
  settings yield worse data.
- **Boston controls are a conspicuous outlier at 84.0% passive quality**, roughly 25 points above
  every other cell. The paper does not explain this; it is unexplained variance worth noting before
  anyone treats a single site's control group as a benchmark.
- **Bhopal's relapsed participants had the lowest active quality in the table (11.8%)**, on only 3
  relapse events — a small cell, but it points at the concern that the participants whose data
  matters most may be the ones supplying least.

**Documented causes of incompleteness**, stated by the authors:

- *Active:* participants ignored reminders; saw reminders but forgot; or **turned off app
  notifications** entirely.
- *Passive:* forgetting to charge the phone; **turning on low power mode, which disrupts mindLAMP's
  collection**; and turning off GPS despite instructions not to.

**A field-level constraint the authors name explicitly:** the widely-used CrossCheck dataset
"represents information that is older and **no longer feasible to obtain due to changes around data
availability rules from smartphone manufacturers**." This is the same OS/vendor policy erosion that
cost RADAR-MDD its call and SMS logs — here it has rendered a whole historical benchmark dataset
unreproducible.

## Feasibility Findings

The study's own conclusion is about prediction rather than logistics: anomalies were **2.12× more
frequent in the month preceding a relapse** and **2.78× more frequent in the month preceding and
following**, versus **1.5×** for a naive logistic regression on demographics, self-reported
medication adherence and symptoms — making the anomaly-detection model **1.41× more effective**.
188 significant anomalies at p=0.005, of which **13 (6.9%) were true positives**.

The deployment-relevant findings:

- **Permutation testing failed to reject the null that anomaly detection performed equally well at
  all three sites (p=0.165)** — supporting the claim that the approach ports across cultures and
  languages. The authors are careful: p=0.165 means "likely minor differences", not identity.
- **Adding passive data and data-quality metrics improved prediction over active data alone** by a
  measurable 1.41×. Notably, **data quality itself was used as an input stream** to anomaly
  detection — an unusual and clever move that treats missingness as signal rather than nuisance.
- **No single passive stream was most predictive across individuals**, which the authors read as
  reflecting the personalised nature of relapse. Practical consequence: a study cannot pre-select
  one stream and expect it to generalise.
- Changepoints in passive data correlated with self-reported symptom change on PANSS, PHQ-9, GAD-7,
  SF-36, SFS, PSQI, WSS and BASIS-24.

## Relevance to Future Study Design

1. **Report completeness ratios, not just retention.** 28.5% active / 57.4% passive being described
   as at-or-above the published norm is the single most calibrating fact in this profile. Retention
   and completeness are different questions and this module's studies answer them very differently.
2. **A digital phenotyping platform can port across countries, languages and urban/rural settings**
   with only modest degradation in passive data quality — but only with real provisioning support
   (phones *and* cellular service at the Indian sites) and local co-design.
3. **Implement a data-collection trial period before full enrolment.** A one-week screen that
   excludes phones producing multiple days of no passive data is cheap and directly protects the
   analytic sample. Remember its cost: it makes the reported quality figures conditional on a
   pre-filtered cohort, and — as [Cho et al.](byod-demographic-imbalance.md) warn about withdrawal
   designs — it may skew demographics.
4. **Low power mode is a specific, nameable failure mode.** Add it to participant instructions and
   to troubleshooting scripts alongside charging and GPS permissions.
5. **Treat data quality as an analysable stream, not just a diagnostic.** Feeding it into the
   anomaly detector was part of what made the model work.
6. **Rural ≠ worse data.** Bhopal outperformed both urban sites on passive completeness.
7. **Historical benchmark datasets are decaying.** If a design leans on CrossCheck-era comparisons,
   verify the streams involved are still collectable under current OS and vendor rules.

## Evidence Confidence

**Verified** for enrolment figures, per-site durations, relapse counts and ascertainment, the full
data-quality table, and the anomaly/logistic-regression comparison — all primary reported results
read from the published PDF.

**Reported** for the interpretive claim that this data quality is "comparable to or even exceeded"
other studies — the comparison is to three cited studies, not a systematic benchmark, and the
authors themselves open that paragraph with "It is challenging to compare our results to prior
studies."

**Unclear** for cross-site equivalence of the algorithm. p=0.165 is a failure to reject, on a small
number of relapse events (20 total, 3 at Bhopal). This is not evidence of equivalence, and the
authors say so.

**Major confounder the authors state plainly: COVID-19.** The study ran under mobility restrictions
that differed in timing and severity between the US and India, and even between US counties and
states. Since passive data *is* behavioural data, the authors concede that "smartphone behavior and
overall data quality may not reflect regular usage outside of this time frame, affecting
generalizability of our passive data results." They plan a later-pandemic comparison once the study
concludes. Additionally, **this is an interim report on the first half of an ongoing collection**,
chosen deliberately because relapse triggers were expected to change as restrictions lifted.

**Other stated limitations:** relapses came from monthly clinical interviews and medical records, so
unreported inter-visit relapses are possible; and cultural and environmental factors not captured by
the smartphone likely contribute to residual site differences.

**COI:** John Torous, mindLAMP's lead developer, is senior and corresponding author, and the paper
evaluates mindLAMP. As with the Beiwe papers in this module, the reported operational figures are
unflattering in absolute terms (28.5% active completeness) and no competitor comparison is drawn,
which limits what the COI could distort. The *predictive-model* claims are more exposed to it than
the completeness figures.

## Key Links

- Paper (OA): https://doi.org/10.1038/s41537-023-00332-5
- Europe PMC: https://europepmc.org/article/PMC/PMC9880926
- Published protocol (ref 17 in the paper): see `../sources.md`
- Local PDF: `../literature/2023-schizophrenia-mindlamp-relapse-prediction-three-site.pdf`

## Related profiles

- Platform: [mindLAMP](../../module-02-digital-phenotyping/profiles/mindlamp.md)
- Same passive > active completeness ordering on other platforms:
  [`beiwe-als-adherence.md`](beiwe-als-adherence.md),
  [`radar-mdd-longterm-engagement.md`](radar-mdd-longterm-engagement.md)
- Run-in/withdrawal screening, and its demographic risk:
  [`beiwe-als-adherence.md`](beiwe-als-adherence.md),
  [`byod-demographic-imbalance.md`](byod-demographic-imbalance.md)

## Sources

1. Cohen A, et al. *Schizophrenia* 2023;9:6. DOI 10.1038/s41537-023-00332-5. Full text and tables
   read from the published PDF (via Europe PMC, PMC9880926), 2026-08-31. Establishes every figure in
   this profile.
