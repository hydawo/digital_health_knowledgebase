# Liu et al. 2019 — LAMP app cognitive assessments in schizophrenia, unpaid, 12 weeks: patients engaged 3× more than healthy controls

## Quick Facts

| Field | Details |
|---|---|
| Citation | Liu G, Henson P, Keshavan M, **Onnela JP**, **Torous J**. "Assessing the potential of longitudinal smartphone based cognitive assessment in schizophrenia: A naturalistic pilot study." *Schizophrenia Research: Cognition* 2019;17:100144. DOI [10.1016/j.scog.2019.100144](https://doi.org/10.1016/j.scog.2019.100144). PMC6476810. |
| Study design | Naturalistic pilot, two-group (clinical vs. healthy control), 12 weeks. Novel analytic method (survival-analysis treatment of touch-event sequences with a modified Cox proportional-hazards model). |
| Sample size (enrolled / analyzed) | **35 total: 18 with schizophrenia, 17 healthy controls.** All analysed; no dropout figures reported. |
| Population | **Clinical group:** adults in active treatment at a Boston outpatient state mental-health clinic, diagnosis confirmed by treating psychiatrists; comorbidity not excluded. Mean age 26.1 (SD 5.3); 66.7% male; 68.8% White, 25.0% Black; **38.9% college graduates**. **Controls:** recruited from local colleges, screened with the MINI for absence of mental illness. Mean age 23.7 (SD 1.3); 64.7% male; **82.4% Asian**; **94.1% college graduates**. Groups differed significantly on race (p<0.001) and education (p=0.002). |
| Duration | **12 weeks.** |
| Devices/platforms used | The Beth Israel Deaconess **LAMP app** on participants' own smartphones (BYOD) — the direct predecessor of **[mindLAMP](../../module-02-digital-phenotyping/profiles/mindlamp.md)**, from the same Division of Digital Psychiatry. Cognitive games ("Jewels A" and "Jewels B"), symptom surveys, and step count. |
| Funding/COI | NIMH K23 career development award and a Brain & Behavior Research Foundation Young Investigator grant, both to **John Torous**, who is senior author and leads the LAMP/mindLAMP platform. **Onnela is a co-author.** Platform-developer COI discussed under Evidence Confidence. |
| Last verified | 2026-09-01 |

## Summary

Two reasons this small pilot earns a Module 3 entry, and neither is its cognitive-science result.

**First, it is the module's cleanest zero-incentive deployment.** Stated twice in the paper, and
once as an explicit design rationale: *"No payment or compensation was offered for engagement with
the app,"* and later, *"we did not compensate any participants to engage with the app **in order to
ensure our results are more generalizable**."* That is an unusually deliberate methodological choice
— most uncompensated studies are uncompensated by budget, not by design — and it makes this the
direct counterpart to [Mercier et al.](beiwe-spinal-cord-injury-incentives.md), where the same
research group network introduced a $30 incentive mid-study and watched retention rise from 50% to
78%.

**Second, the engagement result runs the opposite way to almost every prior assumption in this
field.** Over 12 weeks, with no compensation and full freedom to ignore prompts:

| | Mean assessments completed, Jewels A | Jewels B |
|---|---|---|
| **Participants with schizophrenia (n=18)** | **24** | **22** |
| Healthy controls (n=17) | **8** | **8** |

**The clinical group completed roughly three times as many voluntary assessments as the healthy
controls.** The authors are careful about what this can mean — "our results leave open the question
if lack of interest from controls or more motivation from those with schizophrenia contributed to
differing rates of engagement" — but either reading has the same design implication: **healthy
control arms may be the adherence risk in digital mental-health studies, not the clinical arm.**

Set against this module's other clinical-population findings — ALS participants out-adhering typical
smartphone cohorts in [Beukenhorst et al.](beiwe-als-adherence.md), and the same paper's cited
comparison in which healthy controls remained active for a single day — a consistent pattern is
accumulating: **people with a stake in the illness under study engage; convenience-sampled healthy
controls do not.**

**Note also that this is not a Beiwe study.** The instrument is the LAMP app, from Torous's Division
of Digital Psychiatry at BIDMC — the lineage that became
[mindLAMP](../../module-02-digital-phenotyping/profiles/mindlamp.md). The staged candidate list
described the technologies only as "smartphone cognitive assessments + sensors," which is
ambiguous; the full text names the app and links its repository.

## Instrumentation and Deployment Model

**BYOD, participants' own devices, open-source app.** Inclusion required "owning a smartphone able
to run the study app" — for both groups. Source code is public at
[BIDMCDigitalPsychiatry/LAMP-app](https://github.com/BIDMCDigitalPsychiatry/LAMP-app).

**Active protocol — voluntary throughout, which is the key design feature:**

| Instrument | Prompted cadence | Compulsion |
|---|---|---|
| **Jewels A** — tap numbered jewels in order, as fast and accurately as possible (a smartphone-adapted Trails A) | up to **2 cognitive assessments/week** | **"free to ignore these"** |
| **Jewels B** — same, alternating number → letter → number (Trails B, adding task switching) | (same allowance) | free to ignore |
| Clinical symptom surveys | up to **3 survey assessments/week** | free to ignore |
| Step count | passive | — |

The games were "adapted using several iterations of patient feedback to improve engagement" — a
co-design step the authors credit and one worth noting alongside the engagement result.

**Instrumentation detail relevant to analysis:** during each assessment the app records the
subject's ID, game level, and **the timestamp and item of every touch event on the screen**. That
touch-level granularity is what makes the survival-analysis approach possible, and it is a
capability worth checking for in any platform intended for cognitive tasks — most EMA platforms
record only the answer, not the interaction trace.

**Compensation: none, deliberately.**

**Ceiling on possible assessments:** up to 2 per week over 12 weeks ≈ **24 possible per game**. The
schizophrenia group's mean of 24 (Jewels A) and 22 (Jewels B) therefore sits **at or near the
protocol ceiling**, and the control group's 8 at roughly a third of it. That framing is not in the
paper — it follows from the stated cadence and duration and is flagged here as an inference — but it
converts a raw count into something like a compliance rate: **~100% vs ~33%.**

## Recruitment and Retention

**Recruitment sources were structurally different for the two groups**, and this is the study's main
internal weakness:

| | Clinical group | Controls |
|---|---|---|
| Source | Outpatient **state mental health clinic**, Boston | **Local colleges** |
| N | 18 | 17 |
| Mean age | 26.1 (SD 5.3) | 23.7 (SD 1.3) |
| 4-year college graduate or higher | **38.9%** | **94.1%** |
| Predominant race | 68.8% White, 25.0% Black | **82.4% Asian** |

The groups are matched on age (p=0.082) and sex (p=1.0) and unmatched on race (p<0.001) and
education (p=0.002). The authors acknowledge this directly: "while our control sample was balanced
in terms of age, it was not balanced in terms of education and this may have influenced results. As
a feasibility study, college students were a practical control group."

**Crucially, the clinical group came from an ongoing treatment relationship while the controls did
not.** That difference alone could produce the 3× engagement gap without any illness-related
motivation being involved — and it is the same mechanism
[Mercier et al.](beiwe-spinal-cord-injury-incentives.md) observed between their exercise-programme
and community-reintegration streams (53% vs 21% completion), and that
[Beukenhorst et al.](beiwe-als-adherence.md) cite from prior work (clinic-referred participants
discontinuing at 7 days vs self-referred at 25.5 days). **Recruitment channel is a plausible
confounder for every engagement comparison in this literature, and it is almost never controlled.**

**No retention, dropout, or attrition data are reported.** No time-to-discontinuation, no
per-participant distribution, no withdrawal count, no reasons. This is the profile's principal
limitation as a Module 3 entry: the paper establishes an engagement *level* but nothing at all about
engagement *over time*.

## Data Completeness and Technical Issues

**What is reported:**

| Metric | Schizophrenia (n=18) | Controls (n=17) |
|---|---|---|
| Mean Jewels A assessments over 12 weeks | **24** | **8** |
| Mean Jewels B assessments over 12 weeks | **22** | **8** |
| Approx. protocol ceiling (2/week × 12 weeks) | ~24 | ~24 |
| **Implied completion rate (inference, not stated)** | **~100% / ~92%** | **~33%** |

**What is not reported, and should have been:**

- Survey completion rates (up to 3/week were offered; no figure is given).
- Step-count completeness or passive-data yield of any kind, despite the paper stating that
  "collecting other forms of data such as surveys and steps was also feasible using the same
  smartphone platform" — that feasibility claim is made **without a supporting number**.
- Per-participant distributions. Means only, with no SDs, medians, or ranges. With n=18 and n=17,
  a handful of high-engagement participants could account for the entire group difference and it
  would be invisible.
- Any dropout, withdrawal, or discontinuation data.
- Any technical failure mode — no app crashes, sync failures, device incompatibilities, or battery
  complaints are mentioned. As in [Soon et al.](oura-university-freshmen-sleep.md), treat this as
  **unreported rather than absent**.

**A computational note the authors do flag as an operational constraint:** their analytic method "can
be computationally intensive if several weeks of data are aggregated," and they recommend a
weekly/monthly update cadence for faster runtime. A small point, but a real one for anyone planning
near-real-time cognitive scoring from touch-event streams.

## Feasibility Findings

The paper's stated conclusion is narrow and appropriately so: "It is feasible for those with
schizophrenia to use their own smartphones to complete cognitive assessments and other measures
related to their mental health."

Its cognitive result: on the simpler pattern task (Jewels A) both groups scored similarly; on the
task-switching version (Jewels B) the schizophrenia group scored significantly lower (mean β −3.88
vs −3.08, p=0.0080). Notably the authors chose college students as controls precisely so that the
groups would **not** separate on the easy task — an intentional design choice that they state
worked.

**Stated limitations, in the authors' order:** no independent validation sample; **no comparison
against gold-standard cognitive tests** (deliberately, given the stated use case of tracking
*intrapersonal change* rather than absolute cognition); the method cannot distinguish games with
identical Kaplan–Meier curves but different error counts; computational cost; and the unmatched
control group on education.

**Their forward inference on engagement**, which is the transferable one: "our result that those with
schizophrenia completed more cognitive assessments than healthy controls also suggests **engagement
rates will differ based on the populations studied**, so further collaborative design work with
patients could help ensure these smartphone assessments remain engaging."

## Relevance to Future Study Design

1. **Do not assume the healthy control arm is the easy arm.** 24 vs 8 assessments over 12 weeks,
   unpaid. If your design needs matched data density across arms, budget separate retention support
   — or compensation — for controls specifically.
2. **Voluntary, ignorable prompts in a clinical population reached the protocol ceiling with no
   payment.** This is a real data point against the assumption that serious mental illness implies
   low digital engagement, and it is consistent with the ALS findings elsewhere in this module.
3. **Recruitment channel confounds every engagement comparison here.** Clinic-recruited patients in
   active treatment vs. college-recruited controls is not a clean contrast. Where an engagement
   difference matters to your design, match on recruitment route, not just demographics.
4. **Read this together with the incentive evidence.** [Mercier et al.](beiwe-spinal-cord-injury-incentives.md)
   found retention rising 50% → 78% with a threshold incentive but **no change in survey completion
   rate**. Liu et al. found ceiling-level completion with **no incentive at all** in a clinical
   population. Together they suggest incentives buy *presence*, and the population's stake in the
   research buys *effort*.
5. **Choose a platform that records the interaction trace, not just the answer.** Touch-event-level
   timestamps are what made this analysis possible, and most survey-oriented platforms discard them.
6. **Co-design the instrument with the target population.** The games were revised over several
   iterations of patient feedback. Whether that caused the engagement gap cannot be established
   here, but it is the cheapest available candidate explanation.
7. **Publish per-participant distributions, not group means, at N<40.** This study's central
   engagement finding is reported as two pairs of means with no dispersion, which is the main reason
   it can only be cited as suggestive.

## Evidence Confidence

**Verified** for the sample composition and demographics (Table 1), the mean assessment counts
(24/22 vs 8/8), the prompted cadence (≤2 cognitive and ≤3 survey assessments per week, ignorable),
the 12-week duration, the explicit absence of compensation, the app identity and its public
repository, and the cognitive-performance results — all read directly from the published open-access
PDF.

**Inference, flagged as such:** the ~100% vs ~33% implied completion rates. These follow from the
stated cadence (2/week) and duration (12 weeks) against the reported means; the authors report only
raw counts and do not compute a rate.

**Reported, not established, for the engagement finding's interpretation.** The 3× difference is a
solid observation on its face, but with n=18 and n=17, **means published without any measure of
dispersion**, unmatched education and race between groups, and radically different recruitment
channels, the *causal* reading (that people with schizophrenia are more motivated to engage) is one
of at least three plausible explanations — the others being control disinterest (which the authors
raise themselves) and the clinic-relationship confound (which they do not).

**Unclear** for retention, data completeness, passive-data yield, survey completion, and technical
failure modes. None are reported. The paper's claim that collecting surveys and steps "was also
feasible" is **unsupported by any published figure**.

**Not applicable — heartbeat.** No Beiwe involvement; the pre-heartbeat caveat attaching to the
Beiwe profiles in this tranche does not apply. The LAMP app of 2019 will have faced the same
OS background-execution constraints described in [Beukenhorst et al.](beiwe-als-adherence.md), but
this study's active-assessment design does not depend on background collection, and no passive
completeness figure is published against which it could matter.

**COI.** **John Torous, senior author, leads the Division of Digital Psychiatry that built the LAMP
app, and both funding awards supporting this work are career-development grants to him.** Onnela,
Beiwe's originator, is a co-author (Beiwe is not used). This is a platform-developer-reports-on-own-
platform arrangement of the same shape as the Beiwe papers in this tranche.

What the COI could distort: the feasibility framing, and specifically the unsupported claim that
survey and step collection "was also feasible" — an assertion about the platform's capability with
no number behind it. What it is less likely to distort: the engagement *comparison*, which is
internal to the study and which cuts in a direction no platform developer would have predicted or
preferred (their healthy controls barely used the app). The authors also make the platform's source
code public and explicitly invite independent replication, which is the behaviour of a group
expecting to be checked.

**Generalisability.** N=35, single Boston clinic plus local colleges, 12 weeks, a control group that
is 82.4% Asian and 94.1% college-educated against a clinical group that is 68.8% White and 38.9%
college-educated. The authors note the large Asian representation among controls as notable given
that demographic's lower mental-health service use. Nothing here supports a population estimate; it
supports a hypothesis worth testing at scale.

## Key Links

- Paper (open access): https://doi.org/10.1016/j.scog.2019.100144
- Europe PMC: https://europepmc.org/article/PMC/PMC6476810
- LAMP app source (predecessor of mindLAMP):
  https://github.com/BIDMCDigitalPsychiatry/LAMP-app
- **Local PDF (already in the knowledge base, not duplicated):**
  `../../module-02-digital-phenotyping/literature/mindlamp/2019-liu-schizophrresconn-assessing-potential-longitudinal-smartphone-based-cognitive-assessment.pdf`

## Related profiles

- Platform lineage: [mindLAMP](../../module-02-digital-phenotyping/profiles/mindlamp.md) — this is
  the LAMP app that became mindLAMP.
- **Direct counterpart on incentives** — same institutional network, opposite design choice:
  [`beiwe-spinal-cord-injury-incentives.md`](beiwe-spinal-cord-injury-incentives.md)
- Clinical populations out-adhering expectations, with a formal retention analysis:
  [`beiwe-als-adherence.md`](beiwe-als-adherence.md)
- Later mindLAMP deployment at three sites across two countries:
  [`mindlamp-relapse-3site.md`](mindlamp-relapse-3site.md)
- Adherence, feasibility and tolerability in schizophrenia:
  [`dp-schizophrenia-tolerability.md`](dp-schizophrenia-tolerability.md),
  [`sleepsight-schizophrenia-rest-activity.md`](sleepsight-schizophrenia-rest-activity.md)

## Sources

1. Liu G, Henson P, Keshavan M, Onnela JP, Torous J. *Schizophr Res Cogn* 2019;17:100144.
   DOI 10.1016/j.scog.2019.100144. Full text and Table 1 read from the published open-access PDF
   held locally at `module-02-digital-phenotyping/literature/onnela-lab/`, 2026-09-01, via
   `pdftotext -layout`. Establishes every figure in this profile except the explicitly-flagged
   completion-rate inference.
