# Beukenhorst et al. 2022 — Beiwe in ALS: adherence and data completeness across two observational studies and one clinical trial, N=94

## Quick Facts

| Field | Details |
|---|---|
| Citation | Beukenhorst AL, Burke KM, Scheier Z, Miller TM, Paganoni S, Keegan M, Collins E, Connaghan KP, Tay A, Chan J, Berry JD, **Onnela JP**. "Using Smartphones to Reduce Research Burden in a Neurodegenerative Population and Assessing Participant Adherence: A Randomized Clinical Trial and Two Observational Studies." *JMIR mHealth and uHealth* 2022;10(2):e31877. DOI [10.2196/31877](https://doi.org/10.2196/31877). PMC8857693. Trial registration NCT03168711. |
| Study design | Secondary analysis of **three** studies sharing one platform: two observational cohorts + one randomized placebo-controlled trial (SURE-ALS2, inosine). Kaplan–Meier time-to-discontinuation + Cox PH predictors + per-28-day data completeness. |
| Sample size (enrolled / analyzed) | **94 total** — study 1 N=22 (12 weeks), study 2 N=49 (52 weeks), study 3 N=23 (20-week trial). One participant died before study end in *each* of the three studies. |
| Population | People with ALS (El Escorial criteria), ≥moderate smartphone use, no other neurological disorder. Mean age 56–58; **91–100% White**; baseline ALSFRS-R 34–36. Sites: Mass General, Washington University St Louis, Twin Cities ALS Clinic, Holy Cross ALS Clinic. |
| Duration | 12, 52 and 20 weeks respectively; data spanning Jul 2016 – Mar 2021 |
| Devices/platforms used | **[Beiwe](../../module-02-digital-phenotyping/profiles/beiwe.md)** only — participants' own smartphones (BYOD), **both iOS and Android** (60% iOS overall) |
| Funding/COI | Academic (Harvard Chan Biostatistics / Mass General Neurological Clinical Research Institute). Onnela is Beiwe's originator and is senior author — a platform-developer-reports-on-own-platform COI, discussed under Evidence Confidence. |
| Last verified | 2026-08-31 |

## Summary

The best-documented Beiwe deployment record available, and unusually valuable because it reports
**three studies with the same platform, the same disease, and deliberately different designs** —
letting design effects be separated from platform effects. It is also, importantly, a study **with
no engagement scaffolding at all**: no routine contact to encourage engagement, no reimbursement for
engagement, and no reminders beyond the app's own notifications. That makes it the cleanest
available lower bound on what a smartphone phenotyping platform achieves unassisted, and a direct
contrast with the heavily-supported RADAR studies.

Three findings carry beyond ALS. **Adherence in this population was better than published smartphone
studies generally**, not worse, despite progressive physical and cognitive decline. **Passive data
outlasted active data everywhere** — phones kept returning GPS after participants stopped doing
surveys. And **early data completeness predicts later adherence**: participants who dropped out in
month 1 or 2 had visibly poor completeness while still nominally enrolled, which the authors turn
into a concrete design recommendation (run-in-and-withdrawal).

## Instrumentation and Deployment Model

**BYOD, participants' own phones, both OSes.** The Beiwe app was installed and activated by a study
coordinator at the baseline clinic visit, and uninstalled at the final visit.

| | Study 1 | Study 2 | Study 3 (trial) |
|---|---|---|---|
| N | 22 | 49 | 23 |
| Duration | 12 weeks | 52 weeks | 20 weeks |
| Clinic visits | 3 | 2 | 3 (+ phone calls every 3 weeks) |
| Smartphone survey | Weekly | Weekly | Weekly |
| GPS duty cycle | **on 1 min / off 10 min** | same | same |

Data streams: weekly self-administered ALSFRS-R; weekly speech recordings (reciting displayed text)
and cough recordings; survey metadata (presentation time, per-answer submission time, completion
time); and passive sensor/log data including GPS at the ~6-samples-per-hour duty cycle above.

**Deployment volume:** 185 clinic-administered ALSFRS-R scores versus **1,465 smartphone-administered
ALSFRS-R scores** — an ~8× increase in outcome measurements for the same cohort, which is the paper's
core argument for the approach. Plus 3,748 audio recordings and **10.4 GB of GPS data**.

**Critical design contrast with the RADAR studies:** *"None of the studies included routine contact
with participants to encourage engagement; there was no reimbursement for engagement; and outside of
reminders from the smartphone app itself, no reminders were sent."* Study 3 (the trial) did have
3-weekly phone calls as part of trial conduct.

## Recruitment and Retention

**Time-to-discontinuation (Kaplan–Meier), proportion still contributing at 3 months:**

| Study | Active data (surveys + audio) | Passive data (GPS) |
|---|---|---|
| Study 1 (12-wk observational) | 77% (17/22) | 95% (21/22) |
| Study 2 (52-wk observational) | **59% (29/49)** | 86% (42/49) |
| Study 3 (20-wk trial) | **96% (22/23)** | **100% (23/23)** |

The ordering is consistent and interpretable: **the clinical trial retained best, the year-long
observational study retained worst.** Trial participants are more selected, more monitored, and
have a shorter horizon.

**Predictors of discontinuation: none found.** Cox proportional hazards models (separate for survey,
audio, and GPS data) tested age, sex, smartphone OS, and baseline disease severity across all four
ALSFRS-R subdomains. **No variable was significantly associated with discontinuation risk.** The
authors are appropriately honest that this analysis was **underpowered** — ALS is rare and the total
N is 94 — so this is an absence of evidence, not evidence of absence. It is nonetheless a useful
negative result: baseline disease severity did not visibly drive attrition, echoing RADAR-MDD's
finding that baseline depression severity did not predict data availability.

## Data Completeness and Technical Issues

**Completeness among participants while still active** (100% GPS = any data that day; 100% survey/
audio = one submission per scheduled week):

- **GPS was the most complete stream in all three studies — 90–100% of days.**
- Surveys: median **100%** (study 1), **90%** (study 2).
- Audio (cough): median **92%** (study 3).
- **Study 3 (trial) had the highest completeness overall; study 2 (52 weeks) the lowest.**

**The early-dropout signal — the most transferable finding:**

| Participant group | Mean data completeness while active |
|---|---|
| Dropped out in month 1 | **7.8% (audio) to 41% (surveys)** |
| Dropped out in month 2 | 41% (cough audio) to 59% (GPS) |
| Adhered long-term (>2 months) | **~75%, fluctuating, across all data types** |

Participants who were going to drop out were **already contributing very little while nominally
enrolled**. Completeness also generally declined over time, and was typically lowest in a
participant's final month — with the notable exception of study 2, where those who lasted to the
final month completed everything.

**Documented technical constraint — the single most important platform fact in this profile:**

> Both major mobile operating systems implement power-saving measures for background apps. **No app
> can run in background mode indefinitely; the app must be brought to the foreground at least
> occasionally for background collection to persist.** The authors conclude explicitly that
> **"longitudinal passive data collection without active data collection is not possible."**

This is an OS-level architectural fact, not a Beiwe limitation, and it inverts a common study-design
assumption. A "passive-only, zero-burden" smartphone protocol does not exist: something must return
the app to the foreground periodically to keep the passive stream alive. It also explains why passive
completeness tracks active engagement rather than being independent of it.

> **Platform development since publication — read the claim above as describing pre-2024 Beiwe.**
> Beiwe subsequently added a **heartbeat** (also called *keepalive*) mechanism: a server-side push
> notification, dispatched on a schedule, whose purpose is to wake the app so background collection
> resumes. It was developed on the `push-notification-heartbeat` and `finish-heartbeat` branches
> between January and May 2024, with the message and interval made **configurable per study**
> (2024-04-08), Android push support added (2024-05-14), the latest heartbeat surfaced as a datapoint
> on the participant page (2024-05-15), and the feature flag removed so that **heartbeat became
> globally enabled on 2024-05-29**. A heartbeat API endpoint followed on 2024-06-06.
> (**Verified** — `onnela-lab/beiwe-backend` public commit history.)
>
> This **narrows but does not eliminate** the constraint. The underlying OS behaviour is unchanged;
> heartbeat substitutes a server-triggered wake for a participant-initiated one, so the app still
> depends on being periodically foregrounded — the trigger is simply no longer required to be an
> active research task the participant must complete. For study design this matters: a
> low-active-burden protocol became more viable after mid-2024 than Beukenhorst et al.'s data
> (collected 2016–2021) could reflect, but a genuinely zero-touch passive protocol still does not
> exist.
>
> **Open question:** the quantified effect of heartbeat on data completeness is not, as far as this
> pass could establish, published in the peer-reviewed literature or in public Beiwe documentation —
> only the implementation itself is publicly evidenced. Logged in
> `../../shared/unresolved-questions.md`. Any completeness figures in this module that predate
> mid-2024 (including all of Beukenhorst et al. and [Kiang et al.](beiwe-missing-data-sociodemographic.md))
> should be treated as **lower bounds** for current Beiwe deployments, not as current performance.

Other stated sources of passive incompleteness: participant behaviour (e.g. disabling GPS) and
device/OS/hardware variation, which the authors note is hard to modify and **changes over time**.

## Feasibility Findings

The study's stated conclusion: three studies **successfully collected smartphone data longitudinally
from a neurodegenerative population**, and time-to-discontinuation was **higher than in typical
smartphone studies**, which commonly show exponential dropout. The authors offer this as a
**benchmark for participant engagement**, and it is a well-earned framing given the absence of any
engagement scaffolding.

They attribute the better-than-expected adherence to the **high research commitment of people with
ALS**, citing a comparison study where MS participants dropped out significantly later than healthy
controls (who remained active for only 1 day), and where clinic-referred participants discontinued
far sooner than self-referred ones (7 vs 25.5 days).

**Explicit design recommendations:**

1. **Collect passive data**, which is more complete and outlasts active engagement.
2. **Identify likely adherers during the study's initial phase.** For trials, the authors endorse a
   **run-in-and-withdrawal design**: a weed-out period after enrolment, randomising only participants
   still using the app afterwards. Their own month-1/month-2 completeness data is the evidence for
   why this would work.
3. Monitor active-data completeness early as the screening signal.

They also flag, as a caution on active data, that repeated self-report may **influence participant
responses through the Hawthorne effect and related reporting bias** — a measurement-validity concern
distinct from completeness.

## Relevance to Future Study Design

1. **This is the unsupported-baseline number.** Compare 59% active-data retention at 3 months in a
   52-week unsupported observational study against RADAR-MDD's ~80% outcome completion with
   bi-weekly researcher contact, incentives, and a kept device. The gap is roughly the value of the
   support model, and it should be budgeted as such.
2. **Trial context buys adherence.** 96% active / 100% passive at 3 months in the trial versus 59% /
   86% in the year-long cohort, same platform, same disease. Design and horizon dominate.
3. **Do not plan a genuinely zero-touch passive smartphone protocol.** The OS background-execution
   constraint means the app must be periodically foregrounded. On Beiwe since mid-2024 a
   **server-side heartbeat push can supply that wake** instead of an active research task, so the
   *participant-burden* cost of keeping passive collection alive is now much lower than this paper's
   data implies — but the dependency itself remains. Confirm the equivalent mechanism (and whether
   it is enabled) on any platform under consideration.
4. **Instrument and act on month-1 completeness.** Early completeness separates eventual dropouts
   from adherers cleanly enough to support run-in designs or targeted outreach.
5. **Progressive disease is not automatically an adherence barrier.** Neither baseline severity nor
   any demographic predicted dropout here (underpowered, but directionally consistent with
   RADAR-MDD).
6. **BYOD across both OSes worked** — 60% iOS, no OS effect detected. Contrast with RADAR-base's
   Android-only requirement, which cost that study 11% of its withdrawals.
7. **The ~8× gain in outcome measurements** (1,465 smartphone vs 185 clinic ALSFRS-R scores) is the
   quantitative case for smartphone outcomes in a rare, hard-to-visit population.

## Evidence Confidence

**Verified** for all retention, discontinuation, completeness, and data-volume figures — primary
reported results read from the published PDF.

**Unclear** for predictors of attrition: the Cox models found nothing, but the authors state the
analysis was underpowered. Do not cite this as evidence that disease severity is unrelated to
adherence.

**COI worth naming plainly:** **Jukka-Pekka Onnela, Beiwe's originator, is the senior author**, and
the analysis is of Beiwe's own performance. That said, the paper's framing works against
self-interest in the places it matters — it reports 59% three-month active retention in the
year-long study without minimising it, and its most quotable technical finding (that purely passive
smartphone collection is impossible) is a limitation of the whole approach, Beiwe included. The
figures are descriptive statistics of the platform's own logs rather than a comparison against a
competitor, so there is no comparative claim for the COI to distort. Treat as **Verified** for the
numbers and **Corroborated** for the interpretive claim that adherence exceeded typical smartphone
studies (that comparison is against a small, heterogeneous set of cited studies, not a systematic
benchmark).

**Generalisability limits the authors state:** ALS is rare, so all three studies are small; results
may not generalise to other neurodegenerative diseases; and the cohorts are **91–100% White**,
which is a serious external-validity limit given that
[Kiang et al.](beiwe-missing-data-sociodemographic.md) found sociodemographic structure in
digital-phenotyping missingness.

## Key Links

- Paper (OA): https://doi.org/10.2196/31877 · https://mhealth.jmir.org/2022/2/e31877
- Europe PMC: https://europepmc.org/article/PMC/PMC8857693
- Trial registration: https://clinicaltrials.gov/ct2/show/NCT03168711
- Local PDF: `../literature/2022-beukenhorst-jmirmhealth-smartphones-als-adherence-completeness.pdf`

## Related profiles

- Platform: [Beiwe](../../module-02-digital-phenotyping/profiles/beiwe.md)
- Other Beiwe deployments: [`beiwe-missing-data-sociodemographic.md`](beiwe-missing-data-sociodemographic.md),
  [`beiwe-adolescent-feasibility.md`](beiwe-adolescent-feasibility.md),
  [`beiwe-chronic-disease-substudy.md`](beiwe-chronic-disease-substudy.md)
- Supported-model contrast: [`radar-mdd-recruitment-retention.md`](radar-mdd-recruitment-retention.md)

## Sources

1. Beukenhorst AL, et al. *JMIR mHealth uHealth* 2022;10(2):e31877. DOI 10.2196/31877. Full text and
   tables read from the published PDF (via Europe PMC, PMC8857693), 2026-08-31. Establishes every
   figure in this profile.
