# Jonker et al. 2021 — Remote home monitoring of older surgical oncology patients (Connecare: Fitbit + Withings), N=47

## Quick Facts

| Field | Details |
|---|---|
| Citation | Jonker LT, Plas M, de Bock GH, Buskens E, van Leeuwen BL, Lahr MMH. "Remote Home Monitoring of Older Surgical Cancer Patients: Perspective on Study Implementation and Feasibility." *Annals of Surgical Oncology* 2021;28:67–78. DOI [10.1245/s10434-020-08705-1](https://doi.org/10.1245/s10434-020-08705-1). PMC7752881. |
| Study design | Observational cohort with an explicit implementation-and-feasibility framing; **early cohort** (subset of the system) vs **late cohort** (full system) |
| Sample size (enrolled / analyzed) | 102 assessed → 89 eligible → 50 consented → **47 included** → 45 to surgery → 41 at discharge → **37 completed 3-month follow-up** |
| Population | Patients **aged ≥65** scheduled for oncologic surgery, University Medical Center Groningen (NL). Mean age 72.2 ± 5.0 (range 65–85); 66% male; 100% Dutch; **only 19% higher education**; 85.1% already owned a smartphone/tablet. Median Charlson comorbidity index 4. |
| Duration | Preoperatively to **3 months postoperatively**; intensive 14-day post-discharge window. Recruitment May 2018 – Jun 2019. |
| Devices/platforms used | **Connecare** remote home monitoring system (case-manager website + patient app) with **[Fitbit](../../module-01-wearables/profiles/fitbit-google.md) Charge 2**, **Nokia [Withings](../../module-01-wearables/profiles/withings.md) Thermo** thermometer and **Withings BPM** blood pressure monitor, plus a smart weight scale; ASUS ZenPad 10 / Samsung Galaxy Tab A study tablets where needed |
| Funding/COI | Connecare consortium (EU project). Academic authorship; no device-manufacturer authors. |
| Last verified | 2026-08-31 |

## Summary

Small, but the most operationally candid study in this module — it has a section titled **"Logistical
Problems Encountered and Their Solutions"** that reads like a deployment postmortem, and it is the
only profile here where **recruitment method was changed mid-study and the effect measured**.

Two findings transfer well beyond surgical oncology. First, **switching recruitment from telephone to
face-to-face at the outpatient clinic nearly doubled the participation rate — from 33% (6/18) to 63%
(44/70)**. Second, the study documents a long list of small, unglamorous usability failures — text
too small, excessive mobile data use, Wi-Fi data-transfer delays fixed by switching to Bluetooth,
passwords older patients could not remember, Fitbit syncing harder than expected — each with the fix
the team applied.

Its headline conclusion is genuinely positive and worth stating precisely: **once older patients
consented, they complied and completed.** The barrier was at the door, not after it. **39 of 89
eligible patients declined**, overwhelmingly because of *perceived mental burden at a stressful time*
— not because of the technology.

## Instrumentation and Deployment Model

**Connecare**, an EU-consortium-developed system with three components:

1. **Smart Adaptive Case Management System (SACM)** — a professional website used by a **case
   manager** to monitor physical activity, vital signs and questionnaires in real time, with an
   **alert system that alarms when a value falls outside a preset range**.
2. **Self-Management System (SMS)** — the patient-facing app, pre-installed on the patient's own
   smartphone or a study tablet, which also showed patients their own recovery progress.
3. **Connected commercial devices**, each with explicit alarm thresholds:

| Device | Alarm thresholds | From |
|---|---|---|
| **Fitbit Charge 2** | step count <1,000 (where the patient's average is normally >1,000) | May 2018 |
| **Nokia Withings Thermo** thermometer | temperature <36 °C or >38 °C | Oct 2018 |
| **Nokia Withings BPM** | BP <100/60 or >150/100 mmHg; heart rate <50 or >100/min | Oct 2018 |
| Smart weight scale | — | Oct 2018 |

The staged device rollout is what defines the **early cohort** (Fitbit only, May–Nov 2018) versus the
**late cohort** (n=24, full system, Jan–Jun 2019).

**Deployment practice worth copying:** preoperative assessment, instruction and Wi-Fi connection
**took place at patients' homes (n=43) rather than at the hospital**, because patients had trouble
reproducing hospital-given instructions in their own environment.

## Recruitment and Retention

**Full flowchart:**

| Stage | N | Losses and reasons |
|---|---|---|
| Assessed for eligibility | 102 | **Ineligible (13):** no internet (11), contact dermatitis from Fitbit (1), insufficient Dutch (1) |
| Eligible | 89 | **Declined (39):** high mental burden (30), **digital illiteracy (7)**, negative previous research experience (1), in another study (1) |
| Consented | 50 | Became ineligible (3): surgery cancelled |
| **Included** | **47** | Dropped out before surgery (2): contact dermatitis from Fitbit (1), too stressful (1) |
| Underwent surgery | 45 | Dropped out before discharge (4): died (1), withdrew due to metastatic disease or postoperative complications (3) |
| Assessed at discharge | 41 | Dropped out before study end (4): postoperative complications (2), **too time consuming (2)** |
| **Completed 3-month follow-up** | **37** | |

**Participation rate 56% (50/89 eligible).** The dominant decline reason — **perceived high mental
burden in a time of stress for surgery (30 of 39, 77%)** — is about study participation generally,
not about digital technology. Only 7 declined for digital illiteracy, and 11 were ineligible for
lacking internet.

**Who declined, and why it matters:** those who declined were **more often female (56% vs 32%,
p=0.018) and older (mean 76 ± 5.8 vs 73 ± 5.4 years, p=0.009)**. The resulting cohort is therefore
younger and more male than the eligible population — a selection effect in the same direction as the
BYOD problem, arising here from consent rather than device ownership.

**The recruitment-method experiment.** Inclusion was slow initially. Switching from telephone
approach to **mostly face-to-face contact at the outpatient clinic** raised participation from
**33% (6/18) in May–Sep 2018 to 63% (44/70) in Oct 2018–Jun 2019**. This is the only measured
recruitment-strategy effect in the module and is a strong argument for in-person recruitment in older
clinical populations.

## Data Completeness and Technical Issues

**Compliance was high once enrolled:**

- **Activity tracker worn a median of 87 days (IQR 70–90) out of 90 post-discharge days.**
- **Vital-signs measurement and health-questionnaire completion: median 10.5 days (IQR 4.5–14.0) to
  12 days (IQR 5–14) out of 14 days.**

**Acceptability and usability:**

- **System Usability Scale: mean 74.4 ± 19.3** (early cohort 73.1 ± 15.1) — above the conventional
  ~68 "acceptable" benchmark.
- **Net Promoter Score: +29.7%** on a −100 to +100 scale.

**Logistical problems and their documented solutions — the most reusable content in this paper:**

| Problem | Solution applied |
|---|---|
| Low initial recruitment | Face-to-face approach at outpatient clinic (33% → 63%) |
| Usability problems (text and icons too small); excessive mobile data usage | Preoperative assessment, instruction and Wi-Fi connection moved **to patients' homes** (n=43) |
| **Considerable delays transferring thermometer and weight-scale data over Wi-Fi** | **Switched the thermometer to Bluetooth** |
| Smart weight scale awkward | Patients found it **easier to enter weight manually** into the app |
| Logging in with own email and self-chosen passwords was time-consuming at install; **login details hard for patients to remember** | **Pre-installed all applications on tablets and created study usernames and passwords** |
| **Fitbit synchronisation harder than expected** | Added a **paper instruction pamphlet** from Oct 2018; found phone support was more effective when the patient was referred to the pamphlet simultaneously |
| Patients needing help | **34 (83%) synced Fitbit data unaided, but only 21 (72%) completed vital signs and questionnaires unaided** → team resolved to give post-discharge instructions **with a family member present** |

**Measurement variability observed** (inter-subject vs intra-subject): temperature was very stable
(median 36.5 °C, IQR 0.3 vs 36.6 °C, IQR 0.4); blood pressure and heart rate showed larger and
comparable inter/intra variability; **weight showed much higher inter- than intra-subject
variability** (IQR 8.3 kg vs 1.0 kg), as expected. **Preoperative step count varied widely**
(median 5,392 steps, IQR 5,446 between subjects vs 6,567, IQR 3,932 within). Self-reported activity
(SQUASH) correlated only **moderately** with measured step count (Spearman's ρ=0.42, p=0.016) — a
useful, if incidental, argument for objective measurement.

## Feasibility Findings

The authors' conclusion: older oncologic patients **considered postoperative home monitoring
acceptable and usable**; once consented, they were compliant and completion was high.

The implicit but important corollary: **the feasibility constraint in this population is enrolment,
not operation.** 44% of eligible patients declined, mostly on grounds of psychological burden during
a stressful period, and the decliners were older and more often female than the participants.

**Two contact dermatitis events from the Fitbit** (one causing ineligibility, one causing dropout
before surgery) are a small but concrete reminder that wrist-worn hardware has a skin-tolerance
failure mode — consistent with wristband discomfort being the leading dropout reason in
[RADAR-AD](radar-ad-feasibility-usability.md).

## Relevance to Future Study Design

1. **Recruit face-to-face in older clinical populations.** A near-doubling of participation from a
   change in approach method alone is the cheapest intervention documented in this module.
2. **Expect the barrier at consent, not in operation.** 87 of 90 days of tracker wear, and SUS 74.4,
   in a cohort with mean age 72 and only 19% higher education. Age is not the obstacle it is assumed
   to be.
3. **Do onboarding in the participant's home.** Instructions given at hospital did not survive the
   trip home.
4. **Prefer Bluetooth over Wi-Fi for peripheral device sync**, and be willing to let manual entry
   replace a smart device that adds friction without adding value.
5. **Do not make older participants create and remember credentials.** Pre-provision accounts and
   pre-install apps.
6. **Provide paper instructions alongside phone support** — the combination worked better than either
   alone.
7. **Plan for a family member at instruction.** Only 72% completed vital signs and questionnaires
   unaided, versus 83% for tracker syncing.
8. **Budget for skin reactions to wrist-worn devices** as a screening and attrition category.
9. **Set explicit alert thresholds per device** — Connecare's per-device alarm ranges are a good
   worked example of turning a monitoring stream into an actionable clinical signal.

## Evidence Confidence

**Verified** for the recruitment flowchart, decline reasons, participation-rate change, compliance
medians, SUS and NPS scores, and the logistical problems and solutions — all primary reported
results read from the published PDF.

**Small and single-centre.** N=47 included, 37 completing, at one Dutch academic hospital, **100%
Dutch nationality**. The compliance and usability figures should be treated as encouraging
single-site evidence, not as population estimates.

**Staged-rollout confound:** the early cohort used only the Fitbit; the full device set arrived in
October 2018, at the same time as the recruitment-method change and the instruction-pamphlet
change. The improvement from 33% to 63% participation is therefore **confounded with the other
changes made in the same period** — the authors attribute it to the face-to-face switch, which is
plausible but not isolated. Treat the recruitment finding as **Corroborated**, not Verified.

**Selection effect the study itself documents:** decliners were significantly older and more often
female, so the results describe a younger, more male subset of eligible older surgical patients.

**Platform note:** **Connecare is not profiled in Module 2.** It is a clinical remote-monitoring
platform rather than a research phenotyping platform, but it belongs on the expansion-candidate list
in [`../_inventory-and-scope-decisions.md`](../_inventory-and-scope-decisions.md).

## Key Links

- Paper (OA): https://doi.org/10.1245/s10434-020-08705-1
- Europe PMC: https://europepmc.org/article/PMC/PMC7752881
- Local PDF: `../literature/2021-annsurgoncol-remote-home-monitoring-older-surgical-cancer.pdf`
- Supplementary Textbox S3 (lessons learned from logistical problems) — on the publisher page, **not
  retrieved this pass**

## Related profiles

- Devices: [Withings](../../module-01-wearables/profiles/withings.md),
  [Fitbit / Google](../../module-01-wearables/profiles/fitbit-google.md)
- Multi-device protocols in older/impaired populations, and wristband discomfort as an attrition
  cause: [`radar-ad-feasibility-usability.md`](radar-ad-feasibility-usability.md)
- Another small clinical deployment with provisioned hardware:
  [`movesense-palliative-support-trial.md`](movesense-palliative-support-trial.md)

## Sources

1. Jonker LT, et al. *Ann Surg Oncol* 2021;28:67–78. DOI 10.1245/s10434-020-08705-1. Full text and
   tables read from the published PDF (via Europe PMC, PMC7752881), 2026-08-31. Establishes every
   figure in this profile.
