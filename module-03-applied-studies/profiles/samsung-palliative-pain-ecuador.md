# Domínguez et al. 2026 — Samsung Galaxy Watch pain monitoring in palliative cancer care, Ecuador, N=7 over 7 weeks

## Quick Facts

| Field | Details |
|---|---|
| Citation | Domínguez F, Heras J, Benjumea J, Vallejo M, Parra E, Fiallos W, Villao A, Pazmiño F, Stiens J, da Silva B. "Evaluating a Wearable-Based Pain Monitoring System in Palliative Cancer Care: Usability and Feasibility Study." *JMIR Formative Research* 2026;10:e78098. DOI [10.2196/78098](https://doi.org/10.2196/78098). PMID 41650128 / PMC12880589. |
| Study design | Observational **product-usability and feasibility** study embedded in a routine clinical workflow. Mixed methods: device telemetry, patient exit interviews, health-care staff survey, analysed against the **NASSS framework**. |
| Sample size (enrolled / analyzed) | **7 patients** met criteria and volunteered (4 recruited at outpatient consultations, 3 during home visits). **5 used the system >1 week; 4 completed ≥2 weeks.** Telemetry analysis covers **5**. Plus **5 palliative-care staff** (3 clinicians, 2 nurses) — **3 of whom are coauthors**. |
| Population | Adults with cancer in the **home-based palliative care programme at SOLCA, Guayaquil, Ecuador**. Inclusion: capacity to consent, **Karnofsky Performance Status >50**, current pain requiring monitoring, and ownership of an Android smartphone (loan available). Exclusions: cognitive impairment, physical limitation preventing smartwatch use (**oedema or cachexia**), **lack of family support**, residence outside the city. Age range 35–77 (median 47); 6 of 7 women; 2 low-income/high-school, 5 middle-income/higher education. |
| Duration | 1 week hospital-based + 1 week home-based per patient; study conducted over a **7-week period in Q3 2024** (screening/recruitment ended 2024-09-15). |
| Devices/platforms used | **[Samsung](../../module-01-wearables/profiles/samsung.md) Galaxy Watch 5 (SM-R910) and Watch 6 (SM-R940)**, 44 mm, provisioned with the **NEST** WearOS app preinstalled, paired to a NEST companion app on the patient's own Android phone. Data to a study server and a clinician-facing web dashboard. **Only processed vendor outputs collected — heart rate and wrist detection from Samsung's proprietary algorithms; no raw sensor data.** |
| Funding/COI | VLIR-UOS Short Initiative EC2022SIN341A105; VUB IOF-GEAR Tech4Health. **Conflicts of interest: none declared** — but note that 3 of the 5 staff participants are coauthors. **No participant compensation.** Ethics: Universidad Técnica de Manabí CEISH-UTM-EXT_24-06-21_FXDB. |
| Last verified | 2026-09-02 |

## Summary

The module's **first Latin American deployment** and its second palliative-care study. It is very
small — 7 patients — but it earns a place for three reasons: it is the only entry with
**per-participant wear rates and battery telemetry reported individually**, it reverses the outcome of
the module's other palliative study, and it produces a clean, unexpected result about **where
participants prefer to enter patient-reported outcomes**.

**[Helmer 2025](movesense-palliative-support-trial.md) terminated: a no-proxy-consent requirement
excluded 95.6% of screened palliative patients.** This study, in the same clinical setting, ran to
completion with 7 patients — because it structured recruitment differently. Recruitment ran **through
the existing home-based palliative care team during routine visits**, with a clinician performing a
**KPS assessment first** and only then introducing the study, and **consent taken in person with a
family member present**. Family support was an explicit inclusion criterion rather than an obstacle.
This is the clearest available demonstration that **the palliative-care consent problem is a design
problem, not a fixed property of the population** — though the price is a cohort of 7.

**The PRO-entry finding:** across 296 patient-reported outcomes, **246 (83%) were entered on the
smartwatch and only 50 (17%) on the phone app**, with no significant dependency on location or report
type. Patients in a palliative setting overwhelmingly preferred the wrist over the handset for
symptom reporting.

## Instrumentation and Deployment Model

**Fully provisioned wearable, BYOD Android phone** (with a loaner available). SOLCA staff installed
and paired the NEST mobile app at recruitment, with an ESPOL technician on hand during setup. **The
patient and a family member received training together.**

**Two-phase protocol:** 1 week in hospital with **daily in-person check-ins**, then 1 week at home
with **remote follow-up every 2 days**. The palliative team monitored incoming data through a
web dashboard.

**Telemetry as a wear measure.** The watch **pings the cloud every 5 minutes while worn**, each ping
carrying current heart rate and battery level. Wear time is reconstructed from ping presence. This is
a materially better wear proxy than most in this module — better than "any data on the day"
(see [Bladon 2026](connect-multi-wearable-psychosis.md)'s valid-day definition), comparable in spirit
to Empatica's on-body scoring in [Böttcher 2022](empatica-epilepsy-data-quality.md) — and it is
available because the team wrote its own WearOS app rather than relying on vendor exports.

**Only processed data.** Heart rate and wrist detection come from **Samsung's proprietary on-device
algorithms**; the IMU is used only to complement wrist detection. **No raw sensor data were
collected.** Anyone reading Module 1's [Samsung profile](../../module-01-wearables/profiles/samsung.md)
for raw-data access will recognise the constraint; this study did not attempt to work around it.

## Recruitment and Retention

**7 recruited; 5 with usable telemetry; 4 completed ≥2 weeks.** The reasons for the three shortfalls
are individually reported, which at this sample size is the only useful way to report them:

- **User 1** could not cooperate with the medical team at study end; no closing interview, and **the
  smartwatch was not returned.**
- **User 5** had an extended hospital stay; the team judged it best to remove the watch at the closing
  interview.
- **User 6 withdrew after 1 day due to rapidly deteriorating health.**
- **User 7 was ended by an unrecoverable technical failure of her own phone after 2 days**, preventing
  further participation.

So of four disruptions, **two were disease progression, one was clinical judgement, and one was BYOD
handset failure**. In a population with a KPS >50 inclusion floor, disease progression is the dominant
attrition mechanism and no protocol change addresses it — which is the honest read on why palliative
deployments are small.

No enrolment funnel above consent (approached, screened, ineligible) is reported. Given that the
comparable finding in [Helmer 2025](movesense-palliative-support-trial.md) was a 95.6% pre-consent
exclusion rate, **its absence here is the profile's biggest gap**: we cannot tell whether the
different outcome reflects a different consent design or a much narrower screening frame.

## Data Completeness and Technical Issues

**Definition, stated precisely:** wear rate = hours the watch was actively worn (reconstructed from
5-minute telemetry pings) ÷ total days the device was in the participant's possession.

| User | PROs (n) | Possession (days) | Wear time (h) | **Wear rate** |
|---|---|---|---|---|
| User 1 | 15 | 18.4 | 176 | **39.8%** |
| User 2 | **193** | 17.9 | 396 | **92.1%** |
| User 3 | 6 | 6.5 | 55.9 | **35.8%** |
| User 4 | 56 | 13.7 | 189.8 | **57.6%** |
| User 5 | 5 | 28.1 | 460 | **68.3%** |

**Wear rate ranged from 35.8% to 92.1% and PRO entries from 5 to 193 — a 39× spread on active
reporting against a 2.6× spread on wear, in the same five people.** The passive/active divergence
that this module documents at cohort level is visible here *within individuals*, and it is much wider
on the active side. User 5 wore the device for 460 hours over 28 days and submitted five reports.

**Time-of-day pattern:** except for User 3, **participants wore the watch mostly at night, during
sleeping hours** — the opposite of the daytime-wear assumption most step-based protocols make, and
consistent with the battery data below.

**Battery telemetry, reported per participant** — rare in this module and directly reusable:

| User | Charges (n) | Discharge duration (h), mean (SD) | Discharge rate/h (%), mean (SD) |
|---|---|---|---|
| User 1 | 6 | 43.1 (15.2) | 1.8 (0.2) |
| User 2 | 10 | 39.6 (17.8) | 1.7 (0.3) |
| User 3 | 5 | 22.2 (10.6) | 2.7 (0.6) |
| User 4 | 7 | 34.9 (10.5) | 2.7 (0.5) |
| User 5 | 14 | 33.2 (14) | 2.6 (1.0) |

Observed discharge was **consistent with Samsung's own specification (~40 h, ~2.5%/h)**, so the NEST
WearOS app and 5-minute telemetry did **not** materially increase battery drain. Read together with
the night-wear pattern, the authors infer participants **charged the watch in the evening before
wearing it to sleep** — an inversion of the usual assumption that smartwatch charging costs you the
night.

That matters against [Bladon 2026](connect-multi-wearable-psychosis.md), where the same device family
produced a **4.8% median valid-sleep-day rate**, and where the discussion attributes low sleep
availability partly to charging requirements. **Here, with a bespoke WearOS app and explicit training,
night wear was the dominant pattern.** The two findings are not contradictory — different apps,
different data pipelines, different cohorts, and this one has n=5 — but they do suggest that
"smartwatches lose the night to charging" is a behaviour that can be designed around rather than a
hardware fact.

**PRO input channel:** 143 pain reports and 153 rescue-medication reports, **246 (83%) via the watch
and 50 (17%) via the phone**, with no statistically significant dependency between input method,
location and report type.

## Feasibility Findings

The authors' conclusion is a qualified feasibility claim analysed through the **NASSS framework**
(condition, technology, value proposition, adopters, organisation, wider system, embedding over time)
— an unusual and useful framing for a wearable deployment, since it forces attention onto
organisational adoption rather than only participant adherence.

The design decisions that appear to have made the study run at all:

- **Recruitment inside an existing home-based care programme**, by the clinicians already visiting.
- **A clinical performance screen (KPS >50) before the study was even mentioned.**
- **Consent in person with a family member present**, and family support as an inclusion criterion.
- **Training the patient and a family member together.**
- **Physical exclusions specific to the population** — oedema and cachexia preventing smartwatch wear.
- **Daily in-person check-ins in the hospital week**, tapering to every 2 days at home.

Interviews were conducted by SOLCA staff at device return, and **deliberately not audio-recorded**
given patients' physical and emotional condition — the interviewer took written notes. Both patient
interviews and the staff survey were kept short for the same reason. This is a defensible ethical
adaptation that also weakens the qualitative evidence, and the authors say so.

## Relevance to Future Study Design

1. **Palliative deployments are feasible with the right consent architecture, and the constraint is
   clinical not technical.** Compare [Helmer 2025](movesense-palliative-support-trial.md)'s
   termination on a no-proxy-consent rule. Recruiting inside an existing care programme, screening on
   performance status first, and consenting with family present is the difference worth copying.
2. **Expect disease progression to be the dominant attrition mechanism**, not burden or technology.
   Two of four disruptions here; no protocol change addresses it. Power accordingly and report it
   separately from technology-related dropout.
3. **Patients entered 83% of their symptom reports on the watch, not the phone.** If you are building
   PRO capture for a wearable study, the wrist is not a fallback interface — it may be the primary
   one. This is the module's only direct measurement of that choice.
4. **A 5-minute telemetry ping is a cheap, honest wear-time measure** and it does not cost battery
   life. Any team writing its own WearOS/watchOS app should build this in rather than inferring wear
   from data presence.
5. **Report wear rate per participant when N is small.** 35.8%–92.1% across five people conveys far
   more than a median would.
6. **Night-time wear is achievable on a Samsung smartwatch** with a low-power app and explicit
   training. Verify locally rather than assuming the charging cycle will cost you sleep data.
7. **Exclude on physical wearability, explicitly.** Oedema and cachexia are named exclusions here and
   are the kind of criterion that only appears once a team has tried a wristband in an oncology
   population.
8. **A patient's own phone failing can end their participation.** One of seven. In a provisioned-watch
   / BYOD-phone hybrid, the phone is the weakest link.

## Evidence Confidence

**Verified** — the recruitment counts and the individually reported reasons for each of the four
disruptions; the full per-participant wear table (PROs, possession days, wear hours, wear rate); the
per-participant battery table and its consistency with Samsung's specification; the 246/50 (83%/17%)
PRO input split with its pain/rescue breakdown; the 5-minute telemetry mechanism; the inclusion and
exclusion criteria including oedema/cachexia and family support; the device models; the absence of
compensation and of raw sensor data; the night-wear pattern. Read from the full text and published PDF
(PMC12880589), 2026-09-02.

**N = 7 (5 with telemetry).** Every quantitative statement here is descriptive. No inference about
population wear rates, adherence or acceptability is supportable, and the profile does not attempt
one. The value is in the mechanisms and the per-participant detail, not in the levels.

**Reported** — the inference that participants charged the watch in the evening before sleeping. It
follows from the battery and time-of-day telemetry and is plausible, but was not directly observed or
asked.

**Selection.** Inclusion required KPS >50, capacity to consent, Android phone ownership, family
support, and city residence. 5 of 7 were middle-income with higher education, in a
service-of-last-resort oncology setting. This is a **relatively well-resourced, well-supported subset**
of palliative patients, and no pre-consent funnel is reported to size how selective that was.

**Qualitative evidence is weak by design.** Interviews were not recorded, were conducted by the
clinical staff who delivered the intervention (3 of whom are coauthors), and were kept short. Patient
feedback in this study should not be weighted like an independently facilitated interview study.

## Key Links

- Paper (OA, CC BY): https://doi.org/10.2196/78098
- Europe PMC: https://europepmc.org/article/PMC/PMC12880589
- Local PDF: `../literature/2026-dominguez-jmirformres-samsung-wearable-pain-monitoring-palliative.pdf`

## Related profiles

- Device: [Samsung](../../module-01-wearables/profiles/samsung.md)
- **The other palliative deployment, which terminated on consent design:**
  [`movesense-palliative-support-trial.md`](movesense-palliative-support-trial.md)
- Same device family, opposite sleep-data result:
  [`connect-multi-wearable-psychosis.md`](connect-multi-wearable-psychosis.md)
- Wear measured independently of data presence: [`empatica-epilepsy-data-quality.md`](empatica-epilepsy-data-quality.md)
- Remote post-operative monitoring in an oncology/surgical population:
  [`withings-postop-remote-monitoring.md`](withings-postop-remote-monitoring.md)
- Clinician gatekeeping and consent as the binding constraint:
  [`beiwe-fitbit-gynecologic-cancer-hope.md`](beiwe-fitbit-gynecologic-cancer-hope.md)

## Sources

1. Domínguez F, Heras J, Benjumea J, et al. *JMIR Form Res* 2026;10:e78098. DOI 10.2196/78098. Full
   text and Tables 1–4 read from the published PDF and PMC XML (PMC12880589), 2026-09-02. Establishes
   every figure in this profile.
