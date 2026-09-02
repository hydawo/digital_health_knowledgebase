# Straczkiewicz et al. 2024 — Bilateral wrist accelerometers in the ALS Research Collaborative, N=202: the wear-time threshold that changed the analytic N by 52%

## Quick Facts

| Field | Details |
|---|---|
| Citation | Straczkiewicz M, Burke KM, Calcagno N, Premasiri A, Vieira FG, **Onnela JP**, Berry JD (Onnela and Berry share senior authorship). "Free-living monitoring of ALS progression in upper limbs using wearable accelerometers." *Journal of NeuroEngineering and Rehabilitation* 2024;21:223. DOI [10.1186/s12984-024-01514-7](https://doi.org/10.1186/s12984-024-01514-7). PMC11662782. |
| Study design | Secondary analysis of a large observational registry cohort — the **ALS Research Collaborative (ARC) Study** run by the ALS Therapy Development Institute (ALSTDI). Longitudinal linear mixed models, with pre-planned sensitivity analyses on wear-time threshold, movement-angle threshold, and sensor position. |
| Sample size (enrolled / analyzed) | **438 in the source cohort → 354 with handedness recorded → 310 with ALSFRS-RSE surveys → 108 excluded for insufficient wear-time → 202 analysed.** |
| Population | People with ALS. Analytic sample mean age 54.8 (SD 10.9), range 20–78; 62.9% male; **94.0% White**; 85.6% right-handed; mean baseline ALSFRS-RSE 40.8 (SD 5.2) of 48 — i.e. relatively **early-stage, mildly impaired**. ALS onset in the upper limbs in 38% (non-dominant 15.8%, dominant 14.4%, both 7.9%). |
| Duration | Participation September 2014 – January 2023. **Mean follow-up 895.0 days (SD 694.9) — roughly 29 months**, the longest in this tranche. Protocol: **one week of wear every two to four weeks.** |
| Devices/platforms used | **[ActiGraph](../../module-01-wearables/profiles/ametris-actigraph.md) GT3X+** worn on **both** wrists (dominant and non-dominant), continuous triaxial accelerometry at **30 Hz**. Self-entry ALSFRS-RSE surveys. No smartphone phenotyping platform. |
| Funding/COI | Data collected by ALSTDI (a non-profit ALS research organisation) as part of the ARC Study; analysis by Harvard Chan and Mass General. IRB: Advarra CIRBI. **Authors declare no competing interests.** **There was no participant compensation.** |
| Last verified | 2026-09-01 |

## Summary

The single most important operational number in this tranche, and possibly in the module, is in this
paper's Table 1: participants contributed a mean of **282.8 days of collected accelerometer data**,
of which a mean of **51.34 days (18.2%) were "valid"** under the study's 21-hours-per-day wear
criterion.

And then the discussion supplies the counterfactual that makes it load-bearing:

> "Comparison using a more liberal wear-time threshold of **16 or 8 h**, resulted in including
> **240 or 308 subjects**, respectively, instead of **202** included in our main evaluation."

**The analytic sample size varies by 52% — from 202 to 308 participants — as a function of nothing
but a definitional choice about what counts as a worn day.** Same devices, same cohort, same raw
data. This is the cleanest available demonstration that "wear time," "data availability" and
"retention" are not comparable across studies unless the definition travels with the number, and it
is a within-study demonstration, so it cannot be dismissed as a difference between cohorts.

The paper's second operational contribution is a **null on the analytic consequences of that
choice**: the wear-time threshold "did not play a major role in detecting trajectories of disease
progression over time, but it did in estimating of average outcome change associated with ALSFRS-RSE
responses." A stricter threshold bought precision in cross-sectional association estimates and
bought nothing for longitudinal slope detection — while costing a third of the sample.

Everything here is **device-side**: no smartphone platform, no Beiwe. It is a useful non-Beiwe
anchor point within an otherwise Beiwe-heavy tranche, and it comes from an **independently-collected
registry** (ALSTDI's ARC Study) rather than from a study the analysing lab designed.

## Instrumentation and Deployment Model

**Two provisioned ActiGraph GT3X+ devices per participant, one on each wrist**, recording continuous
triaxial accelerometry at 30 Hz.

**Wear protocol — intermittent by design, and the authors explain why:**

- **One week of wear every two to four weeks**, not continuous.
- **Night-time wear was optional.**
- Participants "could also take off the device for nighttime or at any given time of a day as
  needed."

The authors state the rationale explicitly, and it is a good statement of a real trade-off:

> "Although disadvantageous to data completeness, this approach was required to secure time for data
> downloading, device battery recharging, and importantly **minimizing participant burden and
> likelihood of drop-out**."

This is a deliberate exchange of completeness for retention over a **29-month mean follow-up** — and
the follow-up duration achieved is by far the longest in this tranche, so the trade appears to have
worked on its own terms.

**Wear-time determination and the valid-day rule:**

- Wear time determined by a previously published algorithm (not a self-report diary).
- **A participant-day was valid only if it accumulated ≥21 hours (1,260 minutes) of wear.** The
  authors state this was chosen "to ensure a more uniform wear-time across participants over their
  monitoring period."
- **Sensor wear compliance = valid days ÷ days with accelerometer data collection.**
- Follow-up duration = time between first and last day of accelerometer data collection.

**Note what the 21-hour rule does in combination with optional night-time removal.** The protocol
permits taking the device off at night; the validity criterion requires 21 of 24 hours of wear.
Those two rules are in direct tension, and the 18.2% valid-day rate is the arithmetic consequence.
The authors acknowledge this in limitations, attributing the discrepancy to "the study design,
participants' compliance to device wear, and a **conservative data inclusion criterion**."

**Outcome measure:** self-entry ALSFRS-RSE, at intervals matched to the wear windows. Analytic
sample required **≥2 complete ALSFRS-RSE surveys**.

## Recruitment and Retention

**The exclusion cascade — worth reading as an attrition funnel even though the paper frames it as
data availability:**

| Stage | N | Loss |
|---|---|---|
| ARC Study participants included for this analysis (Sep 2014 – Jan 2023) | **438** | — |
| Handedness information available | 354 | −84 (19.2%) |
| ALSFRS-RSE surveys available | 310 | −44 |
| **Excluded: insufficient sensor wear-time (<21 h/day)** | — | **−108 (35% of 310)** |
| **Analytic dataset** | **202** | 46% of 438 |

The 84 participants missing handedness data are a **metadata** loss, not a sensor loss — a reminder
that ancillary variables required by the analysis can silently remove a fifth of a cohort before any
device question arises.

**The ARC Study itself has enrolled over 600 people with ALS**; 438 is the subset relevant to this
analysis window.

**Analytic vs. source cohort comparison** (Table 1) shows the selection was mostly benign on
demographics — age 54.8 vs 54.5, 62.9% vs 64.2% male, 94.0% vs 93.2% White — but **not on the
outcome**: mean ALSFRS-RSE decline was **−0.570 points/month in the analytic sample vs −0.714 in the
full cohort**, and symptom duration at sign-up was longer (33.6 vs 28.2 months). **The analysable
participants were declining ~20% more slowly than the cohort as a whole.** That is a
progression-rate selection effect introduced by a wear-time criterion, and it is exactly the
direction you would predict: people who can and do wear a device 21 hours a day are less impaired.
The authors do not comment on it.

## Data Completeness and Technical Issues

**The headline completeness figures (analytic sample, n=202):**

| Metric | Mean (SD) |
|---|---|
| Follow-up (first to last day of accelerometer data) | **895.0 days (694.9)** |
| Days with accelerometer data collected | **282.8 (215.5)** |
| **Valid accelerometer days, non-dominant wrist (≥21 h wear)** | **48.40 (60.87)** |
| **Valid accelerometer days, dominant wrist (≥21 h wear)** | **51.34 (64.73)** |
| ALSFRS-RSE surveys per participant | 15.98 (14.65) |
| Mean interval between surveys | 65.97 days (34.09) |

Read that as a cascade:

- **895 days of follow-up → 282.8 days with any data (31.6%)** — mostly explained by the
  one-week-in-two-to-four-weeks protocol, i.e. missingness by design.
- **282.8 days with data → ~51 valid days (18.2%)** — explained by the 21-hour rule against optional
  night-time removal, i.e. missingness by definition.
- **Net: ~5.7% of follow-up days entered the primary analysis.**

Every SD here exceeds or approaches its mean (60.87 on 48.40; 215.5 on 282.8; 694.9 on 895.0),
which means the distributions are heavily right-skewed and **the means substantially overstate the
typical participant**. Medians are not published — a genuine reporting gap for a paper whose value
is largely in these numbers.

**The wear-time threshold sensitivity — the finding to carry forward:**

| Valid-day wear threshold | Participants entering analysis |
|---|---|
| **21 hours** (primary) | **202** |
| **16 hours** | **240** (+18.8%) |
| **8 hours** | **308** (+52.5%) |

And the authors' summary of what changed analytically: the threshold "did not play a major role in
detecting **trajectories of disease progression over time**, but it did in estimating of **average
outcome change associated with ALSFRS-RSE responses**." (Details are in supplementary material not
retrieved in this pass — the direction and magnitude of the difference in the association estimates
is therefore **Unclear** here.)

**Other documented limitations, in the authors' words:**

- A **single accelerometer per wrist** "only allows for an approximation of limb movements unaffected
  by significant linear acceleration"; they explicitly note the **GT3X+ has no gyroscope or
  magnetometer** and that sensor fusion would improve the method. That is a device-selection
  constraint with direct consequences for the biomarker.
- **No participant compensation** — recorded in the ethics statement, and worth noting given the
  29-month mean follow-up achieved without it. (This is registry participation in a rare disease,
  the same high-commitment population effect [Beukenhorst et al.](beiwe-als-adherence.md) invoke.)

**Their own forward recommendation on adherence, stated plainly:**

> "In future trials it will be essential to set **more transparent expectations for device wear-time**
> and to **provide regular contact and reminders** for study participants, as it has led to the
> improved adherence in previous studies."

## Feasibility Findings

The study's scientific conclusion is that wrist-worn accelerometers "worn unilaterally or
bilaterally, may serve as useful tools for quantifying upper limb ALS disease progression," and
that the digital biomarkers declined **more steeply than the survey scores** did — the standard
argument for digital outcome measures.

Its explicit feasibility purpose was **generalisation testing**: the paper exists to check whether a
prior 20-participant pilot reproduced at 202 participants over 29 months rather than 6. It did, with
smaller effect magnitudes for count metrics (e.g. Cf45: −2.71%/month here vs −4.86% in the pilot) and
larger for duration metrics (Df45: +2.88% vs +1.70%), while producing "similar estimates of the
association between daily measures and ALSFRS-RSE."

The authors also report that findings were unchanged when using the **dominant** rather than
non-dominant wrist, with dominant-limb count metrics only ~3% higher — leading them to conclude
either that the method does not distinguish fine dominant-hand activity such as handwriting, or that
this population does not use the dominant hand preferentially. **Sensor position did not matter
here**, which is a genuinely useful practical result: a single wrist sensor, either side, appears
sufficient for this biomarker.

## Relevance to Future Study Design

1. **State the valid-day wear-time threshold in the same breath as every wear-time or completeness
   figure you cite, and treat any figure without one as uninterpretable.** 202 / 240 / 308 analysable
   participants at 21 / 16 / 8 hours, in one cohort. This is the module's reference case for the
   non-standardised-definitions problem.
2. **A conservative wear threshold is not free — it selects on disease severity.** The analytic
   sample declined ~20% more slowly than the source cohort (−0.570 vs −0.714 ALSFRS-RSE
   points/month). In a progression study, a wear-time criterion is a covert severity filter.
3. **Do not set a valid-day threshold above what your protocol asks for.** A 21-hour rule alongside
   permission to remove the device at night guarantees mass invalidation. Either require night wear
   or lower the threshold.
4. **Intermittent wear appears to buy long-horizon retention.** One week in every 2–4 weeks, over 29
   months, uncompensated. Read against
   [Johnson et al.](beiwe-actigraph-modus-als-progression.md)'s sensitivity analysis showing one
   week of data with eight-week gaps reproduced continuous-monitoring estimates — **two independent
   ALS studies now suggest continuous wear is over-specified.**
5. **Report medians alongside means for wear-time distributions.** Every SD here approaches or
   exceeds its mean; the means describe a participant who may not exist.
6. **Ancillary metadata can be a larger loss than sensor failure.** 84 of 438 participants (19%)
   were lost to missing handedness, before any device criterion applied.
7. **A single wrist sensor, either side, was sufficient** for these upper-limb biomarkers — but the
   absence of a gyroscope and magnetometer on the GT3X+ constrains what can be derived. Check the
   sensor complement against the intended derivation before procurement.
8. **Set wear-time expectations explicitly with participants and provide reminders**, per the
   authors' own recommendation. This study did neither and reports 18.2% valid days.

## Evidence Confidence

**Verified** for the exclusion cascade (438 → 354 → 310 → 202, with 108 excluded on wear-time), the
Table 1 completeness statistics (282.8 collected days, 48.40 / 51.34 valid days, 895.0 days
follow-up, 15.98 surveys), the 21-hour valid-day definition, the wear-compliance definition, the
device configuration and wear protocol, the absence of compensation, and the **202 / 240 / 308
threshold-sensitivity counts** — all read directly from the published open-access PDF including
Table 1 and the discussion.

**Unclear** for the analytic consequence of the wear-time threshold. The authors state it mattered
for association estimates but not for progression trajectories; the magnitudes are in supplementary
material (Sect. 2.3) not retrieved in this pass. Do not quantify this claim from this profile.

**Inference, flagged as such:** the observation that the analytic sample declined more slowly than
the source cohort (−0.570 vs −0.714 points/month) is read off Table 1 by this pass; the authors do
not report or discuss it as a selection effect. The numbers are theirs; the interpretation is not.

**Not applicable — heartbeat.** This is a **wearable-only** study with no smartphone phenotyping
platform. Beiwe's mid-2024 heartbeat/keepalive is irrelevant here, and the pre-heartbeat caveat that
applies to the Beiwe profiles in this tranche does **not** apply to these figures. The completeness
shortfall here is a wear-protocol and definition artefact, not an OS background-suspension artefact.

**COI.** Authors declare no competing interests. Onnela (Beiwe's originator) is a senior author, but
**Beiwe is not used in this study at all**, so the platform-developer COI that attaches to the rest
of this tranche does not apply. Two co-authors are affiliated with ALSTDI, which collected the data
and holds it (data available on request "after review and approval by the owners of the data") — a
data-custodianship arrangement worth noting but not obviously a directional conflict. The paper's
findings are notably unflattering to its own data-collection protocol (18.2% valid days), which is
the relevant test.

**Generalisability.** 94.0% White, mean baseline ALSFRS-RSE 40.8 of 48 (mildly impaired), and — per
the point above — a wear-time-selected sample declining more slowly than the registry population.
Findings apply to relatively early-stage ALS in a US research registry. The paper's own framing is
that its value lies in **reproducing** a smaller pilot at scale, which it does.

## Key Links

- Paper (open access): https://doi.org/10.1186/s12984-024-01514-7
- Europe PMC: https://europepmc.org/article/PMC/PMC11662782
- ALS Research Collaborative (ARC) Study, ALS Therapy Development Institute:
  https://www.als.net/als-research-collaborative/
- **Local PDF (already in the knowledge base, not duplicated):**
  `../../module-01-wearables/literature/research-accelerometers/2024-straczkiewicz-jneuroengrehabil-free-living-monitoring-als-progression-upper-limbs.pdf`

## Related profiles

- Device: [ActiGraph](../../module-01-wearables/profiles/ametris-actigraph.md)
- Same disease, same senior author, wearable + smartphone survey, and the other half of the
  "continuous wear is over-specified" argument:
  [`beiwe-actigraph-modus-als-progression.md`](beiwe-actigraph-modus-als-progression.md)
- Same disease, smartphone-only, with the time-to-discontinuation analysis this study lacks:
  [`beiwe-als-adherence.md`](beiwe-als-adherence.md)
- Wear-time criteria as an inclusion filter at population scale:
  [`allofus-fitbit-step-counts.md`](allofus-fitbit-step-counts.md)
- Data completeness as the primary outcome, on a different device:
  [`empatica-epilepsy-data-quality.md`](empatica-epilepsy-data-quality.md)

## Sources

1. Straczkiewicz M, Burke KM, Calcagno N, Premasiri A, Vieira FG, Onnela JP, Berry JD.
   *J Neuroeng Rehabil* 2024;21:223. DOI 10.1186/s12984-024-01514-7. Full text, Table 1 and
   discussion read from the published open-access PDF held locally at
   `module-01-wearables/literature/research-accelerometers/`, 2026-09-01, via `pdftotext -layout`.
   Establishes every figure in this profile. Supplementary Section 2.3 (wear-threshold sensitivity
   detail) was **not** retrieved.
