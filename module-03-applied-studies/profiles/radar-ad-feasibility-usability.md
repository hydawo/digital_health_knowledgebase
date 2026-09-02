# Muurling et al. 2024 — RADAR-AD: feasibility and usability of a complex 8-device RMT protocol across all stages of Alzheimer's disease, N=229

## Quick Facts

| Field | Details |
|---|---|
| Citation | Muurling M, de Boer C, Hinds C, Atreya A, Doherty A, Alepopoulos V, Curcic J, Brem AK, Conde P, et al., and the RADAR-AD consortium. "Feasibility and usability of remote monitoring in Alzheimer's disease." *DIGITAL HEALTH* 2024;10:20552076241238133. DOI [10.1177/20552076241238133](https://doi.org/10.1177/20552076241238133). PMC11005503. |
| Study design | Cross-sectional observational feasibility/usability study nested in the RADAR-AD project; two tiers (tier 1 main study, tier 2 optional sub-study). Feasibility = compliance + drop-out; usability = problem rates from bi-weekly semi-structured interviews. |
| Sample size (enrolled / analyzed) | **229 (tier 1)**; **45 (tier 2 sub-study)**; 23 did both in parallel. Groups: healthy control 69, preclinical AD 39, prodromal AD 65, mild-to-moderate AD 56. Groups did not differ on age (p=0.09), sex (p=0.22), or education (p=0.15). |
| Population | Adults >50 across **all syndromic stages of AD** plus healthy controls, at up to 14 European sites. Required a smartphone (relaxed mid-study — see Limitations) **and an available study partner**. |
| Duration | 8 weeks (tier 1); 4 weeks (tier 2). Enrolment spanned COVID-19. |
| Devices/platforms used | **Axivity AX3** and **Fitbit Charge 3** (both wrist); Mezurio app (daily, 4–8 tasks/day); Altoida app (weekly); optional wearable camera; **tier 2:** Fibaro fixed at-home sensors, **Dreem EEG sleep headband**, CANedge car data logger. See [Axivity/GENEActiv](../../module-01-wearables/profiles/axivity-geneactiv.md) and [Fitbit/Google](../../module-01-wearables/profiles/fitbit-google.md). |
| Funding/COI | RADAR-AD, an IMI-funded consortium. **Note a real COI**: the developers of the Altoida and Mezurio apps and of the wearable camera were themselves part of the RADAR-AD consortium; other device developers were not. |
| Last verified | 2026-08-31 |

## Summary

The best available answer to "how many devices can you actually put on a participant at once, and
does cognitive impairment break it?" RADAR-AD ran an unusually maximalist protocol — two wrist
activity trackers simultaneously, two cognitive-task apps, an optional wearable camera, and for a
subset a home sensor network, an EEG sleep headband and a car data logger — across the full AD
severity spectrum, and reported compliance, drop-out and device-by-device problem rates.

The headline result is genuinely encouraging and genuinely qualified: **a highly complex RMT
protocol is feasible even in mild-to-moderate AD** (overall drop-out 7.5%), but compliance and
usability both degrade with disease severity, and — the finding with the widest transfer — **the
variation between individual devices was larger than the variation between "active" and "passive"
categories**. Altoida (a weekly app) produced far more problems than Mezurio (a daily app requiring
much more interaction). Device design, not interaction burden, was the dominant driver.

## Instrumentation and Deployment Model

Fully researcher-provisioned devices, participant-owned smartphone, with a baseline clinic visit for
setup, hand-out, and instruction, plus a printed study manual.

**Tier 1 (8 weeks, all participants):**

- **Axivity AX3** — raw accelerometry, wrist, no screen.
- **Fitbit Charge 3** — consumer tracker, worn concurrently with the Axivity.
- **Mezurio app** — daily schedule of 4–8 cognitive tasks per day, with a **parallel schedule for the
  study partner**.
- **Altoida app** — weekly cognitive assessment.
- **Wearable camera** — optional, 6 self-chosen days; only ethically approved at 9 of the sites.

**Tier 2 (4 weeks, optional, N=45):** Fibaro fixed in-home sensors, **Dreem** wearable EEG sleep
headband, **CANedge** in-car data logger.

**Operational model — this is why the numbers look good:**

- **Bi-weekly researcher phone calls** to every participant, to ask about usability and resolve
  technical issues.
- **Real-time data monitoring for Fitbit and Dreem**: participants were contacted if no data (or
  bad-quality data) arrived for more than two consecutive days.
- **A study partner was an inclusion requirement**, and partners actively helped with charging,
  turning devices on, and app use.

Note the asymmetry the authors call out: **Axivity, Fibaro and CANedge could not be monitored in
real time**, so technical failures and study-team errors on those devices were only discoverable
after data collection ended and could not be fixed.

## Recruitment and Retention

Recruitment targets were met for both tiers despite COVID-19 site closures (which explain uneven
per-site recruitment). **Tier 2 recruitment in the UK was unexpectedly poor (n=3)** even though all
tier 1 participants at London and Oxford were invited — and no data was collected on *why* people
declined, which the authors flag as a missed opportunity.

**Drop-out — tier 1: 17 / 229 (7.5%)**, by group:

| Group | Drop-outs | Mean days before dropping out |
|---|---|---|
| Healthy control | 3 (4%) | 15 (SD 5) |
| Preclinical AD | 4 (11%) | 17 (SD 11) |
| Prodromal AD | 4 (6%) | 13 (SD 8) |
| Mild-to-moderate AD | 6 (11%) | 27 (SD 12) |

**Reasons for drop-out (tier 1), by count:**

- **Discomfort from wearing one or both wristbands — 6** (HC 3, ProAD 1, MildAD 2). The single
  largest reason, and it is a *hardware ergonomics* problem, not a cognitive one — note that half of
  these were healthy controls.
- Frustration with the daily Mezurio tasks — 2
- Study partner wanted or needed to stop — 3 (ProAD 1, MildAD 2)
- Medical reason — 1
- Other — 5, comprising: data-privacy concerns (1), forgetting to wear the watches and use the apps
  (1), participation being too stressful (2), and **participation reminding them too much of their
  own cognitive decline (1)**.

**Tier 2: 2 / 45 (4.4%)** — one mild-to-moderate AD participant with discomfort from the Dreem
headband, and one preclinical AD participant who found it too stressful and **felt "under
surveillance" because of the Fibaro home sensors**.

## Data Completeness and Technical Issues

**Compliance by device and group** (median, Q1–Q3; 100% wear time = 24 h/day for 56 days):

| Device | Healthy control | Preclinical AD | Prodromal AD | Mild-to-moderate AD | p |
|---|---|---|---|---|---|
| **Fitbit** wear time % | 92 (84–97) | 94 (85–96) | 84 (67–96) | **83 (43–93)** | **0.01** |
| **Axivity** wear time % | 57 (49–98) | 95 (50–99) | 85 (50–99) | 52 (45–95) | 0.21 |
| Wearable camera, hours | 14 (10–15) | 15 (13–18) | 16 (14–22) | 14 (6–18) | 0.55 |
| **Mezurio** compliance % | 92 (81–96) | 94 (81–97) | 87 (78–94) | 83 (58–92) | N/A |
| Mezurio commitment % | 100 (92–100) | 100 (95–100) | 97 (92–100) | 97 (65–100) | N/A |
| **Altoida** compliance % | 75 (50–112) | 75 (50–100) | 63 (38–88) | **not used** | 0.09 |
| **Dreem** compliance % (of 28 nights) | 93 (88–93) | 93 (64–102) | 89 (83–93) | 84 (62–93) | 0.65 |

Device *uptake* also fell with severity — e.g. Fitbit data available for 100% of HC vs 95% of
MildAD; Mezurio 100% vs 84%; **Altoida 59% → 49% → 34% → not used at all in mild-to-moderate AD**.

Note the Fitbit compliance figures (median 83–94% wear time over 8 weeks) are far higher than the
62.5% RADAR-MDD achieved over ~18 months — a duration and support-intensity difference, not a
device difference. See [RADAR-MDD](radar-mdd-recruitment-retention.md).

**Documented technical failure modes:**

- **CANedge car logger — the worst performer, and instructive.** Not installed for 20 participants,
  of which **12 were purely technical**: incompatibility with car types, specifically **cars older
  than 2008 and electric vehicles**. For a further 4, it was installed but **produced no data at
  all**. Uptake ranged 36–58% across groups. A device whose compatibility depends on the
  participant's vehicle fleet is a scheduling and budgeting hazard.
- **Fibaro home sensors** not installed for 7 reasons: technical (2), participant/partner refusal
  (4), and someone else in the home having dementia (1).
- **No real-time monitoring on Axivity, Fibaro, CANedge** → failures undetectable until after
  collection.

**Usability problem rates** (0 = never any problem, 3 = always problems with everything; mean (SD)):

| RMT | All | HC | PreAD | ProAD | MildAD |
|---|---|---|---|---|---|
| CANedge | **0.01** (0.05) | 0.05 | 0.00 | 0.00 | 0.00 |
| Fibaro | 0.11 (0.25) | 0.07 | 0.20 | 0.06 | 0.09 |
| Fitbit | 0.19 (0.32) | 0.13 | 0.12 | 0.20 | **0.31** |
| Axivity | 0.21 (0.32) | 0.17 | 0.18 | 0.24 | 0.25 |
| Camera | 0.28 (0.41) | 0.24 | 0.32 | 0.30 | 0.29 |
| Mezurio | 0.31 (0.41) | 0.20 | 0.31 | 0.39 | 0.37 |
| **Dreem** | **0.49** (0.43) | 0.27 | 0.58 | 0.59 | 0.52 |
| **Altoida** | **0.60** (0.68) | 0.46 | 0.74 | 0.73 | N/A |

Category ordering held (passive sensors < wearables < active apps), **but within-category spread was
larger than between-category spread** — Altoida (weekly) scored 0.60 against Mezurio's (daily, 4–8
tasks) 0.31, despite demanding far less interaction. Mild-to-moderate AD participants had
significantly more Fitbit problems than HC and preclinical AD, driven by **discomfort wearing the
watch and difficulty understanding the watch instructions**.

**Wristband ergonomics as a first-class finding:** the **Axivity was singled out as made from a
stiff material that many found unpleasant**, and participants frequently volunteered that they would
be glad to take the watches off. Against that, **8 participants (2 per group) liked the Fitbit
enough to say they wanted to buy one after the study.**

**Camera-specific social friction:** **no Geneva participants agreed to wear the camera at all**, on
confidentiality/privacy grounds. It was the device most noticed by other people; participants had to
explain it, were asked to turn it off or cover the lens, and some would only wear it indoors or when
alone. Study partners in the mild-to-moderate group often had to remind participants to switch it
off for private activities (e.g. using the toilet) and back on afterwards. Participants and partners
were given the chance to review and delete photos at study end — a consent-management practice worth
copying.

## Feasibility Findings

The study's stated conclusion: a highly complex RMT protocol **is feasible even in a mild-to-moderate
AD population**, and the authors explicitly encourage other teams to use RMTs in AD study designs.
Compliance declined with disease severity but remained high; usability was broadly positive, with
more problems where more interaction was required.

The authors' three explicit recommendations for future RMT protocols:

1. **Evaluate each device's design individually rather than reasoning from active/passive
   categories.** This is their headline design lesson, and it is well supported by their own data.
   Where support during a trial will be limited, or the trial is long, prefer lower-interaction
   RMTs — but do not assume a low-interaction device is acceptable.
2. **Prefer RMTs that can be monitored in real time**, so technical failures and study-team errors
   are fixable during collection rather than discovered afterwards. They note Fitbit's real-time
   feedback loop may itself have raised adherence.
3. **Involve — and consider mandating — a study partner**, especially for cognitively impaired
   participants, to help with apps, switching devices on, and charging. They attribute drop-outs in
   the prodromal and mild-to-moderate groups partly to the absence of an engaged partner.

They also note that older age was associated with *better* adherence here, consistent with a large
meta-analysis, and are explicit that **the bi-weekly researcher calls, the study-partner
involvement, and real-time monitoring are why engagement was this high** — the numbers are
conditional on that support model.

## Relevance to Future Study Design

1. **Multi-device protocols are viable in cognitively impaired populations** — 7.5% drop-out over 8
   weeks across eight device types is a strong result and a useful counterweight to blanket
   scepticism about deploying technology in dementia cohorts.
2. **Wristband material and comfort deserve as much protocol attention as sensor specification.**
   The most common drop-out reason was wristband discomfort, and it hit healthy controls too. Two
   trackers on one wrist compounds this.
3. **Prefer devices with a real-time data channel.** The Axivity/Fibaro/CANedge blind spot is the
   clearest illustration in this module of why "we'll check the data at the end" is a failure mode
   rather than a workflow.
4. **Vet hardware compatibility against the participant population's actual equipment before
   committing** — CANedge's incompatibility with pre-2008 and electric vehicles wasted a large share
   of that device's sample.
5. **Wearable cameras carry social and site-level costs that other sensors do not** — a whole site
   declined. Budget for the possibility that a camera sub-study simply does not run at some sites.
6. **A required study partner is a real eligibility filter.** It improved adherence, but the authors
   note people were excluded for lacking one, particularly in the cognitively normal groups.
7. **8 weeks is short.** Do not extrapolate these compliance rates to a multi-month protocol; compare
   against the RADAR-MDD figures over ~18 months.

## Evidence Confidence

**Verified** for all compliance rates, drop-out counts and reasons, problem rates, and device-level
technical failures — these are the paper's primary tabulated results, read from the published PDF.

**Corroborated** for the causal claim that intensive support (bi-weekly calls, study partner,
real-time monitoring) produced the high compliance: plausible, stated by the authors, consistent
with RADAR-MDD, but not experimentally isolated.

**A real COI to weigh:** the **Altoida and Mezurio app developers and the wearable-camera developer
were members of the RADAR-AD consortium**. In this instance the direction of the finding runs
*against* the interested parties — Altoida scored the worst problem rate of any device and was
abandoned entirely in the mild-to-moderate group — which makes the negative findings about those
apps more credible rather than less, not something to discount.

**Limitations the authors state:**

- **Selection bias from requiring a smartphone** — likely more tech-savvy and higher-educated
  participants. Partially mitigated mid-study: some sites struggled to find cognitively impaired
  smartphone owners, so participants were allowed to join using only the activity trackers and
  at-home sensors.
- **Selection bias from requiring a study partner** — people without one could not participate,
  especially in cognitively normal groups.
- **The study-partner perspective was never assessed**, despite partners installing the Mezurio app
  and completing twice-daily questionnaires — a notable gap given how central partners were.
- **Short duration** relative to real clinical trials.
- Problem-rate data in Figure 2 was **not analysed statistically**.

## Key Links

- Paper (OA, CC BY-NC): https://doi.org/10.1177/20552076241238133
- Europe PMC: https://europepmc.org/article/PMC/PMC11005503
- RADAR-AD project: https://www.radar-ad.org/
- Local PDF: `../literature/2024-muurling-digitalhealth-radar-ad-feasibility-usability.pdf`

## Related profiles

- Platform: [RADAR-base](../../module-02-digital-phenotyping/profiles/radar-base.md)
- Devices: [Axivity / GENEActiv](../../module-01-wearables/profiles/axivity-geneactiv.md),
  [Fitbit / Google](../../module-01-wearables/profiles/fitbit-google.md)
- Same platform family, different disease area and much longer horizon:
  [`radar-mdd-recruitment-retention.md`](radar-mdd-recruitment-retention.md),
  [`radar-mdd-longterm-engagement.md`](radar-mdd-longterm-engagement.md)

## Sources

1. Muurling M, et al. *DIGITAL HEALTH* 2024;10:20552076241238133. DOI 10.1177/20552076241238133.
   Full text and tables read from the published PDF (via Europe PMC, PMC11005503), 2026-08-31.
   Establishes every figure in this profile.
