# Garcia et al. 2022 — Apple Heart Study: data-management lessons from a site-less digital trial, N=419,297

## Quick Facts

| Field | Details |
|---|---|
| Citation | Garcia A, Balasubramanian V, Lee J, Gardner R, Gummidipundi S, Hung G, Ferris T, Cheung L, Granger C, Kowey P, et al. "Lessons learned in the Apple Heart Study and implications for the data management of future digital clinical trials." *Journal of Biopharmaceutical Statistics* 2022. DOI [10.1080/10543406.2022.2080698](https://doi.org/10.1080/10543406.2022.2080698). PMC9378511 (author manuscript). |
| Study design | Methodological retrospective on the Apple Heart Study — a **pragmatic, single-arm, prospective, site-less digital trial**. Not a new cohort; a data-management post-mortem framed against the Clinical Trials Transformation Initiative (CTTI) guidelines. |
| Sample size (enrolled / analyzed) | **419,297 enrolled across all 50 states in 8 months.** 2,161 (0.52%) notified of possible AF. The engagement funnel below is the point of the paper. |
| Population | US Apple Watch owners, self-enrolled through an app. Described as having "broad diversity and inclusion." |
| Duration | 8-month enrolment period |
| Devices/platforms used | **[Apple Watch](../../module-01-wearables/profiles/apple-watch-healthkit.md)** (irregular-pulse algorithm), study app, **AmericanWell** telehealth, **BioTelemetry** single-lead ECG patch (now Philips), participant surveys |
| Funding/COI | **Academic–industry partnership between Stanford University and Apple Inc.** — Apple is both the device manufacturer and a study partner. |
| Last verified | 2026-08-31 |

## Summary

The only study in this module operating at six-figure scale, and the only one written specifically
about **data management as the binding constraint**. Its value here is not the AF-detection result
(that is Module 1's territory) but three concrete operational problems that only appear at scale,
each with a documented solution:

1. **A catastrophic engagement funnel.** 419,297 enrolled → 2,161 notified → **450 (20.8% of those
   notified) returned data relevant to the primary objective.** Enrolment at scale bought almost
   nothing without a way to hold onto the small subgroup that mattered.
2. **You cannot count your own participants.** App-based enrolment generated duplicate participant
   records through pathways nobody anticipated, requiring a **Levenshtein-distance deduplication
   algorithm over ~96 billion candidate comparisons**, reduced to ~3 billion by blocking. Positive
   predictive value: 96%.
3. **Timestamps are a first-class data-integrity problem.** Device clocks drift, participants change
   them, and cross-device concordance analysis depends entirely on alignment.

The paper's most striking proposal follows from (2): in app-enrolled trials, **treat sample size as
a quantity estimated with uncertainty** rather than a known integer. That is a genuinely novel idea
for clinical trials and it falls directly out of the deduplication problem.

## Instrumentation and Deployment Model

**Fully site-less and BYOD** — participants used their own Apple Watch and iPhone, downloaded the
study app, and screened, consented and enrolled entirely within it.

**The Apple Watch detection pathway** (documented here more precisely than in most secondary
sources): the optical sensor measures pulse waveform to generate **one-minute tachograms** during
opportunistic periods — roughly every couple of hours when the participant appears at rest. On
detecting pulse irregularity, sampling increases to **approximately every 15 minutes**. If the
irregularity is not seen in the next tachogram, sampling reverts. **If irregularities appear in 5 of
6 consecutive tachograms, the participant is notified.**

**The post-notification protocol** — a multi-vendor chain, each link a place to lose people:

1. Notified → prompted to contact an **AmericanWell telehealth doctor** (first study visit).
2. If not needing urgent care → mailed a **BioTelemetry single-lead ECG patch**.
3. Wear patch + Watch simultaneously for **one week**, return the patch.
4. BioTelemetry generates arrhythmia reports → discussed at a second telehealth visit.
5. **90-Day Follow-up Survey** to notified participants; **End of Study Survey** to everyone.

Six distinct data sources per participant: study app, AmericanWell visits, raw ECG patch data,
BioTelemetry's derived summary report, cardiologist adjudication of the patch data, and
participant-reported questionnaires.

## Recruitment and Retention

**Enrolment was the easy part** — 419,297 in 8 months across all 50 states, "a number not likely
possible without the use of a digital tool."

**The engagement funnel, which is the paper's central cautionary table:**

| Stage | N | % of previous | % of notified |
|---|---|---|---|
| Enrolled | 419,297 | — | — |
| **Notified of possible AF** | **2,161** | **0.52%** | 100% |
| Contacted the telehealth doctor | **945** | **44%** | 43.7% |
| Eligible to receive an ECG patch | 658 | 70% | 30.4% |
| **Returned the patch for analysis** | **450** | **68%** | **20.8%** |

**Roughly four in five notified participants never produced the data the trial's primary and
secondary objectives depended on**, despite email and phone outreach. The authors are explicit that
this "resulted in a missing data issue that potentially compromised the generalizability of our
findings," and that uncertainty in the estimates was **higher than expected, reflected in wider
confidence intervals than originally anticipated**.

**Survey completion — a counter-intuitive and important result:**

| Survey | Group | Completion |
|---|---|---|
| 90-Day Follow-up | Notified (n=2,161) | 1,376 (**63.7%**) |
| End of Study | **Notified** (n=2,161) | 929 (**43%**) |
| End of Study | **All enrolled** (n=419,297) | 293,015 (**70.2%**) |

**Participants who were *not* notified completed the End of Study Survey at a substantially higher
rate than those who were** (70.2% vs 43%). The authors flag this as "interesting" without resolving
it. It is worth taking seriously: it suggests that receiving a worrying health alert may *reduce*
subsequent research engagement — the opposite of the intuition that alerted participants are more
invested. The authors do note missingness may be "related to underlying health (e.g., concern about
cardiovascular health in the wake of an alert)."

**Why site-less trials lose people, in the authors' own analysis:** in a traditional trial,
adherence "may come naturally as coordinators directly contact participants to schedule in-person
clinic visits. The phone calls and emails to schedule visits as well as the in-person visits
themselves often create personal relationships that may increase adherence." A site-less design
removes that relationship-building by construction.

**Their solution was a hybrid:** email and phone outreach to notified participants, plus in-app
reminders for surveys. They also suggest modest incentives on data return, in-app gamification, and
returning results to participants — citing the Metastatic Breast Cancer Project's **95% survey
adherence** achieved through social media and bidirectional communication.

## Data Completeness and Technical Issues

### Duplicate participant identification

Two IDs were issued per enrolment: a **Device ID (DID)** and a **Participant ID (PID)**. The design
anticipated app deletion and re-enrolment (new PID, same DID). It did **not** anticipate:

- A participant **buying a new watch**, reinstalling and re-enrolling → **new PID and new DID**, with
  no way for the system to recognise the existing enrolment.
- Participants **sharing a watch** with others.

**The deduplication algorithm**, built and validated *during* the study after routine data-quality
monitoring surfaced duplicate PIDs:

- Pairwise matching on **last name, email, first name, consent date, state of residence, date of
  birth, phone number**, scored by **Levenshtein string distance**.
- Naive comparison across ~half a million records would have been **~96 billion comparisons**.
  Blocking into four subsets — same DID, same last name, same first name, same date of birth —
  reduced this to **~3 billion**.
- Match threshold set by **cross-validation**. **Positive predictive value 96%.**

**Four stated lessons:**

1. Build a **uniqueness verification step into app onboarding**, comparing each new enrollee against
   those already enrolled and asking flagged individuals to confirm.
2. Expect any initial deduplication algorithm to **need refinement and accuracy characterisation** —
   ideally via a **pilot study before launch**, especially where consent and onboarding are
   electronic.
3. **Carry both PID and DID on every piece of data** wherever possible.
4. **Treat sample size as estimated with uncertainty**, with a variance accounting for algorithm
   accuracy. The authors call this novel for clinical trials and appropriate for large, low-risk,
   app-recruited trials; they leave the variance estimator as future work.

### Timestamp integrity

**Clock drift, measured:** BioTelemetry computed drift across a set of devices over 26 days of data
and found it **ranged from 7 to 39 seconds, mean 20.3 seconds**. Drift is worsened by, among other
things, **recording while the battery is near depletion**.

**Mitigations applied:**

- Recorded the date and time the ECG patch was **shipped, received, worn and returned**, to validate
  timing.
- Data treated as high-integrity only if the patch recording occurred **within a certain number of
  days from shipment**.
- **BioTelemetry synchronised each patch to UTC immediately before shipping.**
- For concordance analysis, a **±60-second window** was appended around each sampled ECG-patch
  interval, so an Apple Watch one-minute tachogram was compared against a 3-minute patch window.
  Misalignment would bias toward falsely concluding discordance.

**Two timestamp types were recorded on every datum: device-generated and server-generated** (the
latter at upload), so a faulty device clock can be detected and worked around.

**A real integrity failure they caught:** one participant's event sequence showed them being
**notified *after* their study visit and after receiving an ECG patch** — chronologically impossible.
Causes may include participants altering the device clock themselves or faulty clocks. The lesson
they draw: timestamp evaluation "should not simply be limited to the examination of the range and
distribution of single variables, but rather should be done in conjunction with the other data
elements" — i.e. **validate event sequences, not just value ranges**, and put this in the data
quality monitoring plan.

## Feasibility Findings

The authors' framing is that digital trials deliver enrolment scale and passive collection, but
introduce data problems that traditional trials do not have: data "not necessarily intended for
research," noisier, needing integration across heterogeneous sources, with non-obvious incompleteness
and opportunistic rather than fixed measurement timing.

They build on CTTI's seven-area framework, arguing its data-management recommendations ("collect the
minimum data set necessary," "proactively address and map data flow," "minimize missing data") are
sound but lack the operational detail needed for adoption. Their two proposed additions:

- **Extend CTTI's emphasis on feasibility studies to data management** — run a pre-launch feasibility
  study on the data pipeline, not just on the technology.
- **An increased role for collaborative data scientists in the design and conduct** of digital
  trials, not only in analysis.

**Their generalizability defence, which is a reusable template:** (1) anticipate reasons for
non-adherence *at design time* and pre-specify them in the analysis plan; (2) **comprehensively
compare those analysed against those excluded for missing data** — in AHS the two groups were
comparable on sociodemographics and AF burden, suggesting limited bias; (3) run **pre-planned
sensitivity analyses** on plausible missingness mechanisms (here, AF burden and ECG patch wear
time), which showed the primary results robust.

They further recommend **explicitly collecting reasons for non-adherence** (e.g. prompting
participants to say why they never contacted the telehealth provider) so those variables can feed
sensitivity analyses and multiple imputation.

**On trial selection:** they advise that digital designs suit trials with **short follow-up, a
fast-acting intervention, or a highly motivated target population** (e.g. rare or severe disease) —
precisely because those rely less on sophisticated retention machinery.

## Relevance to Future Study Design

1. **Enrolment scale does not survive contact with a multi-step protocol.** 419,297 → 450. Size the
   study on the *last* step of the funnel, not the first.
2. **Every vendor handoff is an attrition point.** Telehealth contact (44%), patch eligibility (70%),
   patch return (68%) compound to 20.8%.
3. **Alerted participants may disengage more, not less** (43% vs 70.2% End of Study Survey
   completion). Do not assume the clinically interesting subgroup is the motivated one.
4. **Design participant-uniqueness verification into onboarding**, and pilot the deduplication
   algorithm before launch. Carry device and participant IDs on every record.
5. **Consider reporting sample size with uncertainty** in app-recruited trials.
6. **Record device *and* server timestamps on everything**, measure clock drift empirically, and
   validate longitudinal event ordering as part of routine data-quality monitoring.
7. **Pre-specify missingness reasons and comparison-of-excluded analyses at design time** — this is
   what allowed AHS to defend generalisability despite losing 79% of its notified cohort.
8. **A site-less design removes the coordinator relationship that quietly drives adherence.** Budget
   an explicit replacement for it.

## Evidence Confidence

**Verified** for the enrolment and engagement funnel figures, survey completion rates, deduplication
algorithm design and 96% PPV, comparison counts, and the measured clock drift range — all directly
reported in the full text.

**Reported** for the characterisation of the cohort as having "broad diversity and inclusion" — this
is asserted without demographic tables in this paper, and it sits uneasily against
[Cho et al.'s](byod-demographic-imbalance.md) documented finding that BYOD consumer-wearable studies
systematically fail to achieve representativeness. Anyone relying on AHS diversity claims should go
to the primary trial reports rather than this methodological paper.

**COI — substantial and worth stating.** The Apple Heart Study was an **academic–industry partnership
between Stanford and Apple Inc.**, i.e. the device manufacturer was a study partner. This paper's
subject matter (data management failures and engagement shortfalls) runs against commercial interest,
which lends it credibility on those specific points. It is not a source to use for claims about the
Apple Watch's detection performance.

**Availability caveat:** *Journal of Biopharmaceutical Statistics* is paywalled and the PMC
author-manuscript PDF route returned HTML rather than a PDF. **No PDF was obtained**; full text was
read from the NCBI PMC XML deposit. Logged as Tier 14 Q110 in
`../../shared/unresolved-questions.md`.

## Key Links

- Paper: https://doi.org/10.1080/10543406.2022.2080698
- Europe PMC (author manuscript): https://europepmc.org/article/PMC/PMC9378511
- CTTI digital health trials recommendations: https://ctti-clinicaltrials.org/our-work/digital-health-trials/
- Primary trial reports (Turakhia et al. 2019 design; Perez et al. 2019 *NEJM* results): see
  `../../module-01-wearables/literature-library.md` — note the *NEJM* paper is confirmed genuinely
  paywalled (Tier 12 item 98 in `../../shared/unresolved-questions.md`).

## Related profiles

- Device: [Apple Watch / HealthKit](../../module-01-wearables/profiles/apple-watch-healthkit.md)
- The directly comparable large consumer deployment:
  [`fitbit-heart-study-afib.md`](fitbit-heart-study-afib.md)
- BYOD representativeness: [`byod-demographic-imbalance.md`](byod-demographic-imbalance.md)
- The other very large BYOD wearable cohort:
  [`allofus-fitbit-step-counts.md`](allofus-fitbit-step-counts.md)

## Sources

1. Garcia A, et al. *J Biopharm Stat* 2022. DOI 10.1080/10543406.2022.2080698. Full text read from
   the NCBI PMC author-manuscript XML deposit (PMC9378511), 2026-08-31. Establishes every figure in
   this profile.
