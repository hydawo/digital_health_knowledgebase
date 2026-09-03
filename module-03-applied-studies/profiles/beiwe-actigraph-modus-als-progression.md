# Johnson et al. 2023 — Beiwe + ActiGraph Insight Watch vs. Modus StepWatch in ALS: dual-form-factor wear compliance, N=40, 6 months

## Quick Facts

| Field | Details |
|---|---|
| Citation | **Johnson SA**, **Karas M** (co-first authors), Burke KM, Straczkiewicz M, Scheier ZA, Clark AP, Iwasaki S, Lahav A, Iyer AS, **Onnela JP**, Berry JD. "Wearable device and smartphone data quantify ALS progression and may provide novel outcome measures." *npj Digital Medicine* 2023;6:34. DOI [10.1038/s41746-023-00778-y](https://doi.org/10.1038/s41746-023-00778-y). PMC9987377. |
| Study design | Single-centre, non-interventional, **fully remote** prospective observational study. Participants self-selected their wearable; groups were not randomised. |
| Sample size (enrolled / analyzed) | **46 enrolled → 40 analysed** (20 ActiGraph, 20 Modus). One enrolled participant could not download the Beiwe app at all. Analysis sample required ≥2 fully completed ALSFRS-RSE *and* ROADS surveys. |
| Population | Ambulatory adults with ALS (El Escorial criteria), able to operate their smartphone unassisted. Mean age 61.8 (SD 12.0), range 34–98; 62.5% male; **87.5% White**, 87.5% non-Hispanic; median baseline staff-administered ALSFRS-R 33 (range 11–47); **82.5% iOS / 17.5% Android**. |
| Duration | 6 months per participant; enrolment January–December 2021. |
| Devices/platforms used | **[Beiwe](../../module-02-digital-phenotyping/profiles/beiwe.md)** (surveys, BYOD smartphone) + **one of two provisioned wearables**: wrist-worn **[ActiGraph](../../module-01-wearables/profiles/ametris-actigraph.md) Insight Watch** (triaxial accelerometer, raw at 32 Hz, cellular upload to CentrePoint) **or** ankle-worn **Modus Health StepWatch 4** (step-based; **not profiled in Module 1 — expansion candidate**). |
| Funding/COI | **Sponsored by Mitsubishi Tanabe Pharma Holdings America (MTPHA)**; two co-authors are an MTPHA employee and a paid MTPHA strategic advisor respectively. Senior author Berry reports research support from MTPHA and multiple other sponsors. **Onnela, Beiwe's originator, is a co-author** (declares no competing interests). MTPHA states it did not restrict publication; academic authors retained editorial control. Discussed under Evidence Confidence. |
| Last verified | 2026-09-01 |

## Summary

The rarest thing in this module: **two different wearable form factors, worn continuously by two
arms of the same cohort, with their compliance statistics printed side by side in one table, plus a
smartphone survey stream running across both.** Most multi-device studies report a single pooled
adherence figure or none at all.

And the study's most valuable operational contribution is not the compliance numbers themselves — it
is the authors' explicit warning **not to compare them**. ActiGraph participants recorded a median
158 valid days versus Modus's 136, and 21 versus 12 average valid hours per valid day. The authors
state directly that this difference "should not be interpreted as meaningfully different because the
devices collected data differently, thus methodologies used for valid hour determination differed."
A valid hour on the ActiGraph meant 60 consecutive minutes of non-missing data with the vendor's
wear-status flag set; a valid hour on the Modus meant **at least one step logged**. Those are not the
same measurement, and no amount of care in the study design makes them comparable.

That is Module 3's "definitions are not standardised" problem appearing *inside a single paper, in a
single table, in the same cohort* — which makes it the cleanest available demonstration that
cross-study wear-time comparisons are usually meaningless.

The second decision-relevant finding is a **sensitivity analysis on monitoring frequency**: for the
headline accelerometer measure, one week of data with eight-week gaps between collection windows
produced essentially the same baseline estimate as continuous six-month monitoring, and still
detected significant functional decline. Continuous wear may be buying much less than it costs.

## Instrumentation and Deployment Model

**Three simultaneous data collection channels:**

1. **Staff-administered ALSFRS-R** at baseline, 3 and 6 months — the reference standard.
2. **Beiwe on the participant's own smartphone (BYOD)**, administering the self-entry ALSFRS-RSE and
   the Rasch-built Overall ALS Disability Scale (ROADS) **at baseline and every 2–4 weeks**. Data
   encrypted on-device and transferred over Wi-Fi to HIPAA-compliant AWS. The app was removed at
   study completion.
3. **One provisioned wearable per participant, worn continuously.** Participants **chose** their
   device and split evenly (20/20); the authors note no preference emerged. Devices were returned in
   prepaid packaging.

**Device configurations and, critically, their incompatible wear definitions:**

| | ActiGraph Insight Watch | Modus StepWatch 4 |
|---|---|---|
| Wear site | Wrist (side not specified to participants) | Ankle |
| Raw sampling | Triaxial accelerometer, **32 Hz** | Second-level step counts |
| Upload path | Cellular → ActiGraph CentrePoint cloud | Vendor portal |
| Wear instruction | "As much as possible (preferably 24 h)" | Same, but **may be removed during sleep** |
| Epoch-level wear status | Yes — vendor algorithm on minute-level data | **No** — only a day-level wear indicator inferred from step timestamps |
| **"Valid hour" definition** | **60 consecutive minutes with no missing data and vendor wear-status = worn** | **≥1 step logged in the hour** |
| "Valid day" definition | ≥8 valid hours (not necessarily consecutive) | Same threshold, different underlying hour |
| Raw data access | Provided on request | Not available (no raw accelerometry) |

The Modus valid-hour rule is a **behavioural** criterion (did you take a step?) while the ActiGraph
rule is a **device-state** criterion (was the device on your body and recording?). A participant
sitting still for an hour wearing a StepWatch generates an invalid hour; the same participant
wearing an Insight Watch generates a valid one. In a population with progressive mobility loss, that
asymmetry is not a rounding error — it systematically penalises the more impaired participants on
one device and not the other.

**A second, independent measurement trap the authors document:** neither vendor's daily summary
measures (VDMs) explicitly account for missing data from non-wear, charging or upload interruptions.
The authors demonstrate this concretely — ActiGraph's sedentary and non-sedentary minutes sum to
1,440 in their own investigator-derived measures but **do not sum to 1,440 in the vendor-provided
measures** — and conclude that vendor summaries "may be biased downward." Their imputed
investigator-derived version raised baseline total activity counts from **1,292,056 to 1,362,438**
(a 5.4% difference) and produced "much stronger" and statistically significant associations with the
clinical scales. If you take vendor daily summaries at face value, you are analysing an unlabelled
mixture of behaviour and missingness.

**Compensation:** participants received **$50 at 3 months and $50 at 6 months if still contributing
data** — a retention-conditional incentive, structurally similar to the one in
[Mercier et al.](beiwe-spinal-cord-injury-incentives.md) though smaller in cadence.

**Support model:** contacting participants was permitted when they appeared to be having technical
difficulties or asked for help, but **these calls were not systematically logged** — so the amount
of human support behind these compliance figures is unquantified. That is a material gap: it means
the numbers cannot be cleanly labelled "supported" or "unsupported."

## Recruitment and Retention

Recruitment was **entirely remote**: ALS social media accounts, an institutional research
recruitment website, and the site's ALS multidisciplinary clinic. Study procedures were conducted
remotely with rare exception.

| Stage | N |
|---|---|
| Enrolled Jan–Dec 2021 | **46** |
| Met analysis sample criteria (≥2 complete ALSFRS-RSE and ROADS) | **40 (87%)** |
| Could not download the Beiwe app | **1** |
| ActiGraph arm / Modus arm | 20 / 20 |

The paper does not publish a formal dropout curve or a screened-to-enrolled funnel; the
enrolled-to-analysed step is the only attrition figure available. Six participants (13%) did not
reach two complete survey pairs, and the paper does not break down why beyond the one app-download
failure.

**Days in the observation period** — the closest available proxy for retention — was a median of
**179 (range 23–191)** overall, against a 6-month target. The lower end of that range (23 days)
indicates at least one participant contributing under a month while still meeting the two-survey
analysis criterion.

## Data Completeness and Technical Issues

**Table 2 of the paper, reproduced — median [min, max] per participant:**

| | ActiGraph (n=20) | Modus (n=20) | Combined (n=40) |
|---|---|---|---|
| ALSFRS-RSE submissions | 5 [2, 10] | 6 [2, 13] | **5 [2, 13]** |
| ROADS submissions | 4 [2, 10] | 5 [2, 13] | **5 [2, 13]** |
| Days in observation period | 178 [23, 191] | 180 [61, 189] | **179 [23, 191]** |
| Valid days in observation period\* | 158 [21, 191] | 136 [16, 183] | **146 [16, 191]** |
| Average valid hours on a valid day\* | 21 [15, 24] | 12 [10, 17] | **16 [10, 24]** |

\* **Not comparable between columns** — see the valid-hour definitions above. The authors say so
explicitly.

**What can legitimately be read off this table:**

- **Within the ActiGraph arm**, median valid days were **158 of 178 observed days (89%)**, at a
  median 21 valid hours per valid day. That is a genuinely high continuous-wear figure for a
  6-month deployment in a neurodegenerative population, and it is directly comparable to other
  device-state-based wear-time reporting.
- **Within the Modus arm**, median valid days were **136 of 180 (76%)**, at 12 valid hours per valid
  day — but under a "≥1 step per hour" rule, and with sleep removal explicitly permitted. Twelve
  active hours a day is close to what you would expect from a waking-hours-only, step-gated
  definition, so this is not evidence of worse wear.
- **The survey stream is the thin one.** A median of **5 ALSFRS-RSE and 5 ROADS submissions over 6
  months** against a 2–4 week schedule implies roughly 6–13 possible prompts; 5 completed is a
  median of somewhere around 40–80% depending on the actual prompt count, which the paper does not
  publish. The authors report survey compliance qualitatively as "robust" and "adequate" rather than
  as a percentage. **This is the paper's weakest reporting**, and the reason the survey side of the
  dual-modality comparison is less useful than the wearable side.
- The authors' own benchmark framing: "Compliance is often quite variable in many digital health
  studies, both within and between studies: levels range from **25–80%**." They place their result at
  the favourable end of that band without computing a comparable percentage.

**Yield gain from remote surveys:** the authors note the number of Beiwe survey submissions "was
much higher than the number of assessments typically obtained in traditional in-person clinical
trials" — 5 remote ALSFRS-RSE per participant over 6 months versus 3 staff-administered
ALSFRS-R visits (baseline, 3, 6 months). A modest ~1.7× on the schedule as configured, well short of
the ~8× reported in [Beukenhorst et al.](beiwe-als-adherence.md) with weekly surveys. **Sampling
cadence, not the platform, sets the yield multiple.**

**Documented technical failure modes and burdens, in the authors' words:**

1. **One participant could not download the Beiwe app** (reason not given) — an outright enrolment
   loss to app distribution.
2. **"Some participants experienced high battery drain, which they found bothersome."**
3. **Technical difficulties** — logging back in, resolving glitches — "all affect data collection
   and can require study coordinator support."
4. **Device feature design "is of paramount importance in a population that frequently loses hand
   strength and dexterity"**; the authors call out strap design specifically.
5. **Participants can change the side on which they wear the device**, which the study permitted and
   did not track.
6. **Managing high data volumes from passive monitoring "can be logistically difficult for the
   device, participant, and/or researchers."**

**Missing-data handling:** the ActiGraph arm used mean-imputation of minute-level activity counts
across a participant's wear-days before deriving investigator-derived measures; the Modus arm could
not do this (no raw accelerometry). No sensitivity analysis excluding imputed values is reported.

**Sensitivity analysis on monitoring frequency — the most transferable result in the paper.** Nine
data-collection schedules were modelled against continuous 6-month collection, using total activity
counts (ActiGraph IDM):

- All scenarios produced baseline estimates within **≤1.5%** of the continuous-collection estimate.
- Monthly-change estimates varied by **<4%** for any scenario with **2 weeks of data** per window
  (up to 8-week breaks).
- Slope estimates varied by up to **24.5%** in the sparsest scenarios (1 week on / 8 weeks off) —
  but **every schedule, including 1 week on / 8 weeks off, still detected significant functional
  decline.**

## Feasibility Findings

The authors' stated conclusion: "Despite the observational nature of the study, older age group, and
use of multiple technologies, device wear- and survey submission-compliance were robust in both
device groups," and remote digital data collection "affirm[s] the feasibility and utility of remote
monitoring with the use of apps and wearable devices."

Their explicit limitations: no healthy control arm; missing data from imperfect compliance ("though
not enough to substantively affect data integrity"); a **more slowly progressing population than
interventional trials** enrol, which they flag as limiting transfer to trial settings; and low
ethnoracial diversity — though they note it was "more inclusive than most US ALS studies" and
speculate that digital technology, properly applied, "can bridge the gap between underrepresented
populations in ALS research." That last claim is offered without supporting data.

Their design recommendation, stated directly: "digital interface design, beta testing, and robust
support for technical issues are critically important for ensuring data quality in digital studies."

## Relevance to Future Study Design

1. **Never compare wear-time figures across devices without reading both valid-hour definitions.**
   This paper is the reference case: 158 vs 136 valid days and 21 vs 12 valid hours/day in one
   cohort, and the authors say the difference is an artefact of definition, not behaviour. Extract
   the definition alongside every wear-time number you cite.
2. **Prefer a device-state wear criterion over a behavioural one in populations losing mobility.**
   A "≥1 step per hour" rule confounds non-wear with immobility, and does so worse the sicker the
   participant gets — exactly the wrong direction for a progression study.
3. **Do not analyse vendor daily summaries without checking whether they account for non-wear.**
   Neither vendor here did. The correction was 5.4% on baseline activity counts *and* the difference
   between weak and significant associations with the clinical scale.
4. **Insist on raw data access at procurement.** ActiGraph provided raw accelerometry on request,
   which is what made the imputed investigator-derived measures possible. Modus did not, which is
   why none of the 12 Modus measures could be corrected — and why **none of the Modus measures were
   significantly associated with both clinical scales** while eight ActiGraph measures were.
5. **Continuous wear may be over-specified.** One week of wear every nine weeks reproduced the
   baseline estimate to within 1.5% and still detected decline. For long studies in burdened
   populations, intermittent windows are worth modelling before defaulting to 24/7.
6. **Survey yield is set by your prompt cadence, not your platform.** A 2–4 week Beiwe cadence gave
   ~1.7× the staff-administered assessment count; a weekly cadence in
   [Beukenhorst et al.](beiwe-als-adherence.md) gave ~8×. Decide the cadence from the analytic need.
7. **Publish survey compliance as a percentage with a stated denominator.** This study did not, and
   as a result its dual-modality comparison is only half usable — the very thing that makes it
   valuable is weakened by one missing number.
8. **Letting participants choose their device cost nothing here and bought a natural comparison.**
   The 20/20 split with similar clinicodemographics is a cheap design feature worth copying — though
   note it is self-selection, not randomisation, so the arms are not formally exchangeable.

## Evidence Confidence

**Verified** for the Table 2 compliance statistics, the enrolment/analysis counts, the valid-hour and
valid-day definitions, the sensitivity-analysis results, the vendor-summary bias demonstration
(1,292,056 vs 1,362,438), the device configurations, and the $50/$50 compensation structure — all
read directly from the published open-access PDF including tables.

**Unclear for survey compliance as a rate.** The paper reports it only as "robust"/"adequate" and as
median submission counts. The denominator (number of prompts actually sent per participant) is not
published, so a percentage cannot be derived. Do not cite a survey compliance percentage from this
study.

**Verified but non-comparable** for the ActiGraph-vs-Modus wear figures — the numbers are correct
and the authors' warning against comparing them is explicit. Treat as two separate single-device
observations, not as a head-to-head.

**COI — two distinct exposures, worth separating.**

- **Industry sponsorship.** MTPHA sponsored the study; one co-author is an MTPHA employee and
  another a paid MTPHA strategic advisor; the senior author reports MTPHA research support and
  advisory-panel payment. MTPHA's commercial interest is in **ALS therapeutics**, and the paper's
  thesis — that digital measures could serve as trial outcome measures, potentially reducing
  required trial sample sizes — is directly aligned with a sponsor's interest in cheaper, faster
  trials. That is a real directional pressure on the *interpretive* claims (that these measures are
  ready for trial use), and essentially none on the *descriptive* compliance statistics. The paper
  states MTPHA did not restrict publication and academic authors held editorial control.
- **Platform-developer COI.** Onnela, Beiwe's originator, is a co-author and declares no competing
  interests. As with other Beiwe deployment papers, the exposure would be to comparative claims
  about Beiwe, and none are made — Beiwe appears here purely as a survey-delivery mechanism, with
  no passive smartphone sensing at all. Notably, the paper's most quotable platform-adjacent facts
  cut against the platform: a participant who could not download the app, and battery drain
  complaints. **Nothing in the wear-compliance findings is Beiwe-specific**; they are properties of
  the two wearables and their vendor pipelines.

**Not a Beiwe passive-sensing study.** Worth stating explicitly, because the study is sometimes
described as a Beiwe deployment: Beiwe was used **only for survey delivery** here. No smartphone
GPS, accelerometry, or log data was collected. The heartbeat/background-suspension question that
governs Beiwe passive completeness elsewhere in this module therefore does not apply, and this
study's numbers say nothing about it.

**Generalisability.** N=40, single centre, 87.5% White, 82.5% iOS, ambulatory at baseline, and — the
authors' own most important caveat — **more slowly progressing than a typical interventional trial
population**. Also note the 2021 collection window: this predates Beiwe's mid-2024 heartbeat, which
is irrelevant to the survey stream used here but would matter for any attempt to extend the design
to passive smartphone data.

## Addenda from related papers on the same programme

Two later-screened papers report on the same MGH remote ALS programme. Both overlap this cohort and both add figures this profile lacked, so they are recorded here rather than as a fourth and fifth ALS profile. Both were read in full on 2026-09-03.

Straczkiewicz et al. 2024 (*eBioMedicine* 101:105036, DOI 10.1016/j.ebiom.2024.105036, PMC10914560) is the ActiGraph arm of this cohort, 23 enrolled and 20 analysed. It applies a stricter valid-day rule than Johnson's, at least 21 hours (1,260 minutes) of wear by the Choi algorithm, and under that rule the median was 124 valid days (range 3 to 165) against Johnson's 158 under an 8-hour rule. Same people, same raw data, a fifth fewer valid days at the median. The arm was 15 iOS and 5 Android. Participants submitted a mean of 6.9 surveys (median 6, range 2 to 15) with a mean of 36.8 days between them (median 32, range 6 to 112). 15 of 20 were right-handed, and handedness had not been collected prospectively. The sponsor "was involved in protocol development."

Karas et al. 2024 (*Annals of Clinical and Translational Neurology* 11(6):1380-1392, DOI 10.1002/acn3.52050, PMC11187949) is the passive smartphone-sensing side of the programme, which this profile records as not collected in the wearable arm. 63 people with ALS enrolled between January 2021 and July 2022. 45 met all three analytic criteria (at least two ALSFRS-RSE surveys, at least 28 valid accelerometer days, at least 28 valid GPS days). The 18 excluded were older (mean 63.2 years) and more impaired (median baseline ALSFRS-RSE 32.5 against 37). The mean observation period was 292.3 days (median 291, range 53 to 398). Accelerometer data days in analysis averaged 113.7 (median 108, range 29 to 267), with 724.7 valid accelerometer minutes a day within analysed days, and GPS data days averaged 217.4. Support calls were possible but "were not systematically logged." Collection ran 2021 to 2022, before the platform's heartbeat feature.

## Key Links

- Paper (open access): https://doi.org/10.1038/s41746-023-00778-y
- Europe PMC: https://europepmc.org/article/PMC/PMC9987377
- Analysis code (authors'): https://github.com/onnela-lab/als-wearables
- ActiGraph Insight Watch / CentrePoint: https://theactigraph.com/
- Modus Health StepWatch: https://modushealth.com/
- **Local PDF (already in the knowledge base, not duplicated):**
  `../../module-01-wearables/literature/research-accelerometers/2023-johnson-npjdigitalmedicine-wearable-device-smartphone-data-quantify-als.pdf`

## Related profiles

- Platform: [Beiwe](../../module-02-digital-phenotyping/profiles/beiwe.md)
- Device: [ActiGraph](../../module-01-wearables/profiles/ametris-actigraph.md)
- **Module 1 expansion candidate surfaced here:** Modus Health **StepWatch 4** (ankle-worn step
  monitor) — used as a primary instrument, not profiled in Module 1.
- Same disease, same platform, weekly cadence, no engagement scaffolding:
  [`beiwe-als-adherence.md`](beiwe-als-adherence.md)
- Same disease, wrist accelerometers only, N=202, and the clearest wear-time-threshold result in the
  module: [`actigraph-als-upper-limb-wear-time.md`](actigraph-als-upper-limb-wear-time.md)
- Other Beiwe + wearable multi-device deployment:
  [`beiwe-fitbit-gynecologic-cancer-hope.md`](beiwe-fitbit-gynecologic-cancer-hope.md)
- Multi-device deployment at larger device count:
  [`radar-ad-feasibility-usability.md`](radar-ad-feasibility-usability.md)

## Sources

1. Johnson SA, Karas M, et al. *npj Digital Medicine* 2023;6:34. DOI 10.1038/s41746-023-00778-y.
   Full text, Tables 1–2 and Methods read from the published open-access PDF held locally at
   `module-01-wearables/literature/research-accelerometers/`, 2026-09-01, via `pdftotext -layout`.
   Establishes every figure in this profile.
