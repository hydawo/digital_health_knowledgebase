# Helmer et al. 2025 — Support trial: continuous wearable monitoring in hospitalised palliative patients — terminated early for recruitment failure, N=7

## Quick Facts

| Field | Details |
|---|---|
| Citation | Helmer P, Glück J, Anastasiadis A, Rumpf F, Hottenrott S, Winkler BE, Meybohm P, Kranke P, Roch C, Sammeth M. "The use of wearable sensor technology to enhance supportive care in hospitalized palliative patients (Support trial): a prospective preliminary pilot study." *BMC Palliative Care* 2025;24:154. DOI [10.1186/s12904-025-01794-3](https://doi.org/10.1186/s12904-025-01794-3). PMC12126900. |
| Study design | Prospective pilot feasibility study. **Terminated prematurely** — the 25-patient target was judged unachievable. |
| Sample size (enrolled / analyzed) | **275 screened → 263 (95.6%) excluded → 9 consented → 2 withdrew → 7 analyzed.** Of the 7: 1 completed the maximum duration, 3 were discharged, **3 died during hospitalisation**. |
| Population | Adults on the six-bed Interdisciplinary Center for Palliative Medicine inpatient unit, University Hospital Würzburg — advanced, incurable disease |
| Duration | Oct 2023 – Nov 2024. Monitoring up to **30 days**, or until discharge or death. |
| Devices/platforms used | A **wrist-worn monitor** and a **single-lead chest-wall ECG sensor**, both **CE-marked certified medical devices**. See [Movesense](../../module-01-wearables/profiles/movesense.md) — note the device-identification caveat under Evidence Confidence. |
| Funding/COI | Academic (University Hospital Würzburg). No device-manufacturer authorship apparent. |
| Last verified | 2026-08-31 |

## Summary

The module's most important **negative case**. A well-designed, ethically approved, CE-marked-device
feasibility study in a hospital palliative care unit **could not recruit** and was stopped: 275
patients screened, **263 (95.6%) excluded**, 7 analysed against a target of 25.

The cause is specific, structural, and generalisable well beyond palliative care: **the responsible
ethics committee required patients to provide written informed consent personally, with no option
for proxy consent.** In a population where many patients are, by the nature of their condition,
unable to consent for themselves, that requirement removes most of the eligible pool by
construction. The authors note this bluntly, and add the second horn of the dilemma: patients who
*can* consent tend to be those with longer life expectancy receiving palliative care as part of
restorative treatment — i.e. **the consent requirement selects against exactly the population the
study was designed to help.**

They situate this in a known pattern: in palliative-care RCTs, **only 36.8% of studies meet their
a priori planned cohort size**.

The technical findings, though based on 7 patients, are also instructive — most notably that
**oxygen saturation from a wrist device was unusable (45.1%)** while heart rate and respiratory rate
were excellent (>99%), and that **the chest sensor's hardware was excellent while its software was
the failure point**.

## Instrumentation and Deployment Model

**Fully provisioned, clinician-applied.** On consent, each participant received a study ID, and
**both a wrist monitor and a chest sensor were applied**, with continuous vital-sign collection
started immediately. A **reference heart rate and blood pressure measurement by standard upper-arm
cuff** was taken to calibrate the wrist monitor.

**Baseline data collected included wrist circumference and Fitzpatrick skin type** alongside
Charlson Comorbidity Index, Karnofsky Performance Status and ECOG — a good practice worth noting,
since skin tone is directly relevant to optical sensor performance (see
[Cho et al.](byod-demographic-imbalance.md) on pulse-oximetry disparities).

**Both devices remained in place for the whole stay**, with **routine daily visits to replace or
charge batteries**. Participation ended on death, discharge, or at 30 days.

**Eligibility:** inpatients on the palliative unit, ≥18, able to give written informed consent
themselves. **Exclusions:** prior participation, **inability to provide informed consent
personally**, inadequate German, and suspected non-compliance.

## Recruitment and Retention

| Stage | N |
|---|---|
| Screened | 275 |
| **Excluded — did not meet inclusion criteria, especially written informed consent** | **263 (95.6%)** |
| Provided written informed consent | 9 |
| Withdrew consent before study interventions | 2 |
| **Analysed** | **7** |

Outcomes among the 7: **1 completed the maximum 30 days; 3 discharged to outpatient care; 3 died
during hospitalisation.**

The study was **terminated prematurely** because reaching the target of 25 was deemed unfeasible.

**The authors' analysis of why**, stated directly: the primary barrier was identifying eligible
patients **able to provide written informed consent by themselves**. Ethics-committee requirements
allowed **no proxy consent**. This "significantly limited the pool of potential participants, as many
patients at the end of life are either unable to provide written informed consent themselves or have
a longer life expectancy because they have only received supportive palliative care as a part of
restorative measures or care planning."

They observe that recruitment in palliative-care research is notoriously difficult, that only 36.8%
of RCTs in the field meet their planned cohort size, and that the reasons "remain poorly understood",
with ethical and methodological complexity as likely contributors.

## Data Completeness and Technical Issues

**Overall valid-data yield:**

| Device | Mean valid data | Median | Range |
|---|---|---|---|
| **Wrist-worn** | **61.5%** of monitored time | 57.6% | 20.1–78.3% |
| **Chest-wall** | **55.2%** | 62.3% | **3.6–100%** |

**By parameter:**

| Parameter | Availability |
|---|---|
| **Heart rate** | **>99%** |
| **Respiratory rate** | **>99%** |
| **Oxygen saturation** | **45.1%** |

**Two entirely different failure mechanisms, and this is the most useful technical content:**

1. **Wrist device — algorithmic rejection, not hardware failure.** The authors attribute the gaps to
   **the device's internal algorithm rejecting values of poor signal quality** under real-world
   conditions. They explicitly rule out device failure, since manufacturer guidelines (regular device
   checks and charging) were consistently followed, and consider transmission, processing or storage
   errors unlikely. They note wrist-worn **pulse oximetry is known to be prone to interference** —
   consistent with the 45.1% SpO2 figure.
2. **Chest sensor — excellent hardware, failed software.** Signal quality was **excellent despite
   being a single-lead system with minimal inter-electrode distance**, and the compact cable-free
   design did not restrict patient mobility. But **"the device's unapproved data storage software
   posed significant challenges, including frequent app crashes, unsaved data, and file
   corruption."** Those software failures caused the missing data, and produce the 3.6% floor in the
   chest device's range. The authors draw the obvious conclusion: **robust software development and
   validation matters as much as sensor quality in continuous monitoring systems.**

**End-of-life monitoring performance:** among the three patients who died, **the interval between the
last recorded device measurement and time of death ranged from 0 to 25 minutes** — i.e. the devices
were capturing data essentially up to the moment of death, which is the study's clearest positive
technical result.

## Feasibility Findings

Two separable conclusions, and it matters not to blur them:

- **Technically feasible.** Continuous monitoring worked in this setting, with excellent heart rate
  and respiratory rate capture right up to death, and a chest ECG sensor that did not impede
  mobility.
- **Operationally infeasible as designed.** The consent framework made recruitment impossible.

The authors' forward-looking recommendation is that **future studies should take these study-design
limitations into account** — i.e. negotiate the consent pathway (including proxy consent provisions)
with the ethics committee *before* designing the recruitment plan, not after.

## Relevance to Future Study Design

1. **Settle the consent mechanism before anything else in populations with impaired capacity.** A
   no-proxy-consent requirement excluded 95.6% of screened patients and killed the study. This
   applies equally to dementia, ICU, acute stroke, and severe psychiatric illness cohorts.
2. **Beware consent requirements that select against your target population.** Patients able to
   self-consent had systematically different prognoses from those who could not — so even a
   successfully recruited cohort would have been unrepresentative.
3. **Do not treat "wearable data completeness" as one number.** 61.5% overall concealed >99% for
   heart rate and 45.1% for SpO2 on the same device.
4. **Wrist-based SpO2 is not currently dependable for continuous clinical monitoring.** Under half of
   expected values, from a CE-marked medical device, under supervised inpatient conditions with daily
   charging.
5. **Distinguish algorithmic suppression from data loss.** The wrist device's gaps were the
   manufacturer's quality algorithm discarding poor signal — invisible unless you look for it, and it
   means "missing" data is partly a vendor policy decision.
6. **Vet the vendor's data-storage software as carefully as the sensor.** An excellent single-lead
   ECG was undermined by app crashes, unsaved data and file corruption.
7. **Chest-wall sensors are a credible alternative to wrist devices** where wrist optical sensing
   struggles — good signal quality, no mobility restriction, no cables.
8. **Publish failed feasibility studies.** This one is more useful than several successful ones,
   precisely because it names the barrier.

## Evidence Confidence

**Verified** for the screening and consent funnel, the exclusion rate and its stated cause, the
data-yield percentages by device and by parameter, the last-measurement-to-death intervals, and the
technical failure descriptions — all primary reported results read from the published PDF.

**Severely limited by sample size, as the authors state first among their limitations:** N=7
prevents "definitive conclusions regarding the primary and secondary endpoints," and the work
"should be regarded as a preliminary pilot trial." The **completeness percentages rest on seven
patients** and the ranges are correspondingly wide (chest device 3.6–100%). Treat every technical
figure here as **Reported** rather than established, with the important exception of the recruitment
finding, which is Verified and is the paper's real contribution.

**Device identification caveat — flagged rather than resolved.** This profile is filed under the
Movesense slug because that is how the study surfaced in discovery, and Movesense is named in the
paper. However, **the full text as read describes the devices generically ("wrist-worn monitor",
"chest-wall ECG sensor", both CE-marked) and this pass could not confirm from the extracted text
which specific commercial models were used for each role.** Do not cite this profile as evidence
about a named device's performance until the model identification is confirmed against the paper's
methods tables. Logged for follow-up.

## Key Links

- Paper (OA, CC BY): https://doi.org/10.1186/s12904-025-01794-3
- Europe PMC: https://europepmc.org/article/PMC/PMC12126900
- Local PDF: `../literature/2025-bmcpalliativecare-wearable-sensors-palliative-support-trial.pdf`

## Related profiles

- Device: [Movesense](../../module-01-wearables/profiles/movesense.md) (see caveat above)
- Another small provisioned-hardware clinical deployment with a detailed problem log:
  [`withings-postop-remote-monitoring.md`](withings-postop-remote-monitoring.md)
- Data completeness vs on-body time as distinct failure modes:
  [`empatica-epilepsy-data-quality.md`](empatica-epilepsy-data-quality.md)
- Consent and capacity as a selection filter:
  [`radar-ad-feasibility-usability.md`](radar-ad-feasibility-usability.md) (study-partner requirement)

## Sources

1. Helmer P, et al. *BMC Palliative Care* 2025;24:154. DOI 10.1186/s12904-025-01794-3. Full text read
   from the published PDF (via Europe PMC, PMC12126900), 2026-08-31. Establishes every figure in this
   profile.
