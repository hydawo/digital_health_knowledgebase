# Cote et al. 2019 — Beiwe in clinic-recruited spine disease: the smartphone-ownership exclusion and a 43% daily survey rate, N=105

## Quick Facts

| Field | Details |
|---|---|
| Citation | **Cote DJ**, **Barnett I** (co-first authors), **Onnela JP**, Smith TR (co-senior authors). "Digital Phenotyping in Patients with Spine Disease: A Novel Approach to Quantifying Mobility and Quality of Life." *World Neurosurgery* 2019;126:e241–e249. DOI [10.1016/j.wneu.2019.01.297](https://doi.org/10.1016/j.wneu.2019.01.297). PMC6706326 (NIHPA author manuscript). |
| Study design | Prospective observational cohort, single general neurosurgical clinic. Linear mixed models relating daily self-reported pain to 30 passively-derived mobility and sociability summaries, with Generalized Higher Criticism multiple-testing correction. |
| Sample size (enrolled / analyzed) | **216 approached → 105 enrolled (all 105 analysed).** See the correction note below — **55 is the number who had surgery, not the analysed sample.** |
| Population | Adults (≥18) with clinically diagnosed spine disease seen as neurosurgical candidates. Mean age 52.0 (SD 14.0); 45.7% male; disease site 60.1% lumbar, 33.3% cervical, 5.7% thoracic. **52.4% (55/105) underwent neurosurgical intervention during follow-up.** |
| Duration | Enrolment June 2016 – May 2017. **Median follow-up 94.5 days (3.15 months).** |
| Devices/platforms used | **[Beiwe](../../module-02-digital-phenotyping/profiles/beiwe.md)** only — participants' own smartphones (BYOD, Android + iOS). |
| Funding/COI | Brigham & Women's / Harvard Chan. **Onnela, Beiwe's originator, is co-senior author; Barnett, a Beiwe/Forest methods developer, is co-first author.** The paper states plainly that Beiwe was "developed by a subset of the authors." |
| Last verified | 2026-09-01 |

## Summary

An early, large clinic-recruited Beiwe deployment whose operational value is concentrated in two
places: **the recruitment funnel, which quantifies the BYOD smartphone-ownership exclusion more
starkly than almost any other study in this module**, and **a full 30-feature daily summary table
with a published per-day missing-GPS figure**, which is rare.

**42% of everyone approached was excluded on the spot for not owning a smartphone.** That is the
single most important number in the paper for study-design purposes, and it comes from a general
neurosurgical clinic in Boston in 2016–17. It puts a hard, empirical figure on the selection problem
that [Cho et al.](byod-demographic-imbalance.md) treats structurally: in this population, BYOD
digital phenotyping was simply unavailable to two out of five patients.

The active-data yield is also worth recording plainly: **participants completed 43.4% of daily
surveys**, and only **70.7% of the responses that were submitted arrived on the day they were
prompted**. The study's weekly-response framing (73.2%) is the number that gets quoted; the daily
one is the number that governs any analysis needing same-day pairing.

### A correction to the Module 3 candidate list

The staged candidate file recorded this study as "105 patients enrolled (55 analyzed)" and called
the enrolled-versus-analysed gap "one of the clearest attrition signals in the set." **That is
wrong.** The full text is unambiguous: 105 patients were enrolled and all 105 appear in Table 1 and
in the analysis; **55 (52.4%) is the number who underwent a surgical intervention during follow-up.**
There is no 105→55 attrition. The abstract's phrasing ("105 patients were enrolled with a median
follow-up time of 94.5 days; 55 patients underwent a surgical intervention during follow up") is
easy to misread from an abstract alone, which is exactly why the candidate file labelled its
rankings **Reported** pending full-text extraction.

## Instrumentation and Deployment Model

**BYOD, both operating systems, installed in clinic by a research assistant** who created each
participant's account and gave uniform instructions — including **"keeping it running as a
background application"**, which is an explicit acknowledgement of the OS background-suspension
problem later formalised by [Beukenhorst et al.](beiwe-als-adherence.md).

**Sampling configuration — dense by this module's standards:**

- **GPS: 1 minute on, every 5 minutes** (a 20% duty cycle, ~288 designed on-minutes/day).
- **Accelerometer: 10 seconds on, every 10 seconds** (a 50% duty cycle).
- Anonymised **phone call and text logs** — timing, hashed communication-partner identifiers, and
  message length. **No content was recorded.** Note that call and text logs are **Android-only** on
  Beiwe (the paper states the app collects "phone and call logs (Android only)"), so the sociability
  stream covers only part of this BYOD cohort — and the paper does **not** report the OS split,
  which makes the null sociability result harder to interpret than it appears.
- Bluetooth, Wi-Fi and screen on/off time also enumerated as collected.
- Data encrypted on-device, stored temporarily, uploaded periodically over Wi-Fi.

**Active protocol — one prompt per day, at a fixed time:** at 17:00 EST, "Please rate your pain over
the last 24 hours on a scale from 0 to 10," on a sliding 0–10 scale. **Responses submitted after
midnight (more than 7 hours after prompting) were excluded from analysis** — a deliberate
data-quality rule that costs yield and buys interpretability.

**No compensation, no engagement contact, and no adherence-monitoring apparatus are described.**
This is an unsupported deployment in the same sense as [Beukenhorst et al.](beiwe-als-adherence.md).

## Recruitment and Retention

**The enrolment funnel — the most reusable content in this paper:**

| Stage | N | % of previous | % of approached |
|---|---|---|---|
| Approached for enrolment | **216** | — | 100% |
| **Excluded immediately: no smartphone ownership** | **90** | **42%** | 42% |
| Remaining eligible | 126 | 58% | 58% |
| Could not recall phone password for enrolment | 15 | 12% of 126 | 7% |
| Phone not accessible on the day of the visit | 4 | 3% of 126 | 2% |
| Declined consent over data-security concerns | 2 | 1% of 126 | 1% |
| **Enrolled** | **105** | **83% of 126** | **49%** |

Three separate lessons sit in that table:

1. **Smartphone ownership removed 42% of the clinic population.** Not willingness, not capability —
   ownership. In 2016–17, in a US academic neurosurgical clinic.
2. **A further 15 patients (12% of otherwise-eligible) were lost because they could not remember
   their app-store password**, and 4 more because their phone was not with them. **19 of 126 (15%)
   of eligible patients were lost to purely logistical onboarding friction** — a category almost
   never reported, and one that is trivially addressable with pre-visit instructions or a
   follow-up onboarding call.
3. **Only 2 of 126 (1.6%) declined over data security.** Privacy refusal was the *smallest* loss
   category, an order of magnitude below device-ownership and forgotten passwords.

**Retention.** The paper reports no dropout curve and no formal withdrawal count. What it reports
instead: **median follow-up 94.5 days**, and a mean of **82.5 GPS days per participant (SD 68.4)**.
The very large SD relative to the mean indicates a wide spread of contribution lengths — some
participants contributing for a few days, others for many months — but the distribution is not
published. Figure 5's caption notes that **"some patients stopped taking their smartphone surveys
after recovery despite continuing to collect smartphone GPS location and mobility data passively"** —
the passive-outlasts-active pattern, observed narratively here rather than quantified.

## Data Completeness and Technical Issues

**Survey response — the two rates diverge sharply, and the flattering one is the one usually quoted:**

| Metric | Mean | (25%, 75%) quantiles |
|---|---|---|
| **Daily** survey response rate | **43.4%** | (23.2, 69.8) |
| **Weekly** survey response rate (≥1 survey in the week) | **73.2%** | (50.6, 100.0) |
| Responses submitted on the day prompted | **70.7%** | — |

The interquartile range on the daily rate — **23% to 70%** — is the more honest summary than either
mean: a quarter of participants answered fewer than one day in four.

The gap between 43.4% daily and 73.2% weekly is itself a methodological warning. Both are true; they
answer different questions; and a study whose analysis needs **same-day** pairing of pain score with
mobility (as this one's does) is governed by the 43.4% figure, further reduced by the 29.3% of
responses excluded for arriving after midnight. Effective same-day yield is therefore on the order
of **~31%** of prompted days. The paper does not compute that figure.

**GPS completeness — published, and stark.** Table 1 reports **median missing GPS data of 1,349.7
minutes per day (IQR 1,323.7–1,379.2)**.

- Against a 1,440-minute day, that leaves a median of **~90 minutes of GPS data per day**.
- The configured duty cycle (1 minute in every 5) designs for **~288 minutes/day**.
- **Inference, not a stated result:** roughly **31% of the designed sampling was actually realised**,
  and about 94% of wall-clock time has no GPS observation — most of it missing by design, the
  remainder from behaviour and OS behaviour. The authors do not present this decomposition; it
  follows arithmetically from their own published figures and the stated duty cycle, and is flagged
  here as an inference so it can be checked.

This is why the analysis pipeline depends on imputation: raw GPS was converted to flights and
pauses, "missing portions of data were imputed," and daily mobility summaries derived from the
imputed series (the Barnett–Onnela method, itself a Module 2 methods contribution). **The mobility
results in this paper are results about an imputed trajectory, not an observed one.**

**Stated sources of missingness, in the authors' own limitations:**

1. **Missingness by design:** "the collection of high-frequency sensor data causes some battery
   drainage, [so] sensors need to be sampled according to a sampling scheme that unavoidably
   introduces some missingness by design."
2. **Human behavioural factors**, "such as individuals deactivating smartphone GPS."
3. **The smartphone-ownership exclusion**, which they explicitly link to "underrepresentation of
   patients of lower socioeconomic status and the elderly."

**Analytic handling of missingness:** days with no GPS data or no pain-survey response were simply
**dropped** from the mixed models ("we ignored days that either had no GPS data or had no response to
the pain survey"). No sensitivity analysis on that exclusion is reported.

**Published daily summary distributions** (median, IQR — useful as reference values for anyone
configuring a comparable Beiwe study):

| Feature | Median | IQR |
|---|---|---|
| Time spent at home (min) | 927.1 | 623.9–1,242.8 |
| Distance travelled (m) | 51,989 | 18,692–97,833 |
| Radius of gyration (m) | 3,218.8 | 846.8–9,881.9 |
| Maximum diameter (m) | 13,828 | 4,868–29,382 |
| Significant locations visited | **2** | 1–3 |
| Average flight length (m) | 236.0 | 160.1–334.9 |
| Fraction of day not moving | **0.88** | 0.79–0.94 |
| Significant location entropy | **0** | 0–0.28 |
| Circadian routine (0 low – 1 high) | 0.59 | 0.42–0.71 |
| Outgoing texts/day | 4 | 0–14 |

Note the median **significant location entropy of 0** and **two significant locations visited per
day**: this cohort's mobility was highly concentrated, which constrains how much variance any
mobility feature could carry.

## Feasibility Findings

The paper's stated conclusion is about the science, not the operations: patients reporting higher
pain showed reduced mobility on three GPS summaries (average flight length, maximum diameter
travelled, total distance travelled), and smartphone digital phenotyping "appears to be a promising
and scalable approach." **No association was found between pain and any sociability measure** — a
null that should be read alongside the Android-only limitation on call/text logs noted above.

The authors' feasibility argument is largely a *comparative* one against alternatives rather than an
empirical one about their own yield: they note that wearable-based mobility studies "typically
require participants to wear an additional device, increasing the likelihood of patient
non-compliance and subsequent missing data," and that electronic survey response has higher response
rates than postal or telephone modes. Neither claim is tested here.

They offer no explicit study-design recommendations — an omission relative to the later Onnela-lab
papers in this tranche, which almost all close with an operational recommendation list.

## Relevance to Future Study Design

1. **Budget the smartphone-ownership exclusion explicitly, and measure it.** 42% of an approached
   US neurosurgical clinic population in 2016–17. Ownership has risen since, but the exclusion is
   still the first and largest filter in any BYOD design, and it is **not random with respect to age
   or socioeconomic status** — the authors say so.
2. **Add an onboarding-friction line to the funnel.** 15% of otherwise-eligible patients were lost
   to a forgotten app-store password or an absent phone. Pre-visit instructions ("bring your phone,
   know your password") would have recovered most of them for free.
3. **Privacy refusal was 1.6%.** Consistently across this module, stated privacy concern is a much
   smaller loss category than teams anticipate — 7% in
   [Fu et al.](beiwe-pain-clinic-operational-report.md), 1.6% here.
4. **Report daily and weekly response rates separately, and state which one your analysis depends
   on.** 43.4% vs 73.2% in the same cohort, from the same prompts.
5. **A same-day pairing requirement compounds with the response rate.** 43.4% responded, 70.7% of
   those on the same day. Design the late-response exclusion rule *before* powering the study.
6. **Publish missing-sensor-minutes per day.** This paper does, and it is far more interpretable
   than a "days with any data" completeness rate. Pair it with the configured duty cycle so readers
   can separate missingness-by-design from missingness-by-failure.
7. **If your analysis rests on imputed GPS, say so in the abstract.** Every mobility result here
   depends on flight-and-pause imputation over a series with ~94% of wall-clock minutes unobserved.
8. **Check OS coverage before relying on call/text logs.** Beiwe's communication logs are
   Android-only; a null sociability finding in a BYOD cohort with an unreported OS split is close to
   uninterpretable.

## Evidence Confidence

**Verified** for the enrolment funnel (216/90/15/4/2/105), the survey response rates (43.4% daily,
73.2% weekly, 70.7% same-day), the GPS duty cycle and accelerometer configuration, median follow-up,
mean GPS days, the surgical proportion (55/105), and every value in the Table 1 daily-summary
distributions — all read directly from the full text and tables.

**Verified as a correction:** the "105 enrolled / 55 analysed" reading in the staged candidate file
is incorrect. All 105 were analysed; 55 is the surgical subgroup.

**Inference, explicitly flagged, not a stated result:** the ~31%-of-designed-sampling GPS
realisation rate. It follows from the published median missing-minutes figure and the stated duty
cycle, but the authors neither compute nor endorse it.

**Unclear** for retention. No dropout count, no withdrawal reasons, no time-to-discontinuation
analysis. The mean 82.5 GPS days (SD 68.4) against a 94.5-day median follow-up is the only signal,
and the SD implies a distribution that is not summarised anywhere in the paper.

**Unclear** for the sociability null. Call and text logs are Android-only on Beiwe; the OS split of
this BYOD cohort is not reported; therefore the effective N for the sociability analyses is unknown.

**Pre-heartbeat.** Data collection ran June 2016 – May 2017, seven years before Beiwe's server-side
heartbeat/keepalive push was globally enabled on 2024-05-29. Every completeness figure here is a
**pre-heartbeat lower bound**, and this is one of the earliest deployments in the module, so it
should be treated as a floor even among pre-heartbeat studies. See
[`beiwe-als-adherence.md`](beiwe-als-adherence.md) and Tier 14 Q106 in
`../../shared/unresolved-questions.md`.

**COI — the strongest in this tranche, and it is disclosed in the text.** Beiwe was, in the paper's
own words, "developed by a subset of the authors": **Onnela (originator) is co-senior author and
Barnett (developer of the GPS imputation method the analysis relies on) is co-first author.** The
exposure here is broader than in the other Beiwe papers, because the paper's scientific result
depends on *the authors' own imputation method applied to the authors' own platform's data*, and the
paper contains a general endorsement of the approach ("digital phenotyping has the potential to
revolutionize the surgical care of patients with spine disease") that is not derived from any
measurement.

What the COI **cannot** distort: the enrolment funnel and the survey response rates, which are
counts of study conduct and which are unflattering (42% device exclusion, 43.4% daily response).
Those are the figures this profile relies on. What it **could** distort: the framing that this
approach is "promising and scalable" on the strength of a cohort with ~94% of GPS wall-clock time
unobserved, and the comparative claim that smartphone collection avoids the non-compliance of
wearable studies — which is asserted, not measured, and which this module's evidence does not
support in general.

**Generalisability.** Single Boston academic neurosurgical clinic, 2016–17, N=105, no reported
race/ethnicity or socioeconomic data at all — an unusual omission, and one that sits awkwardly
against the authors' own concern about socioeconomic underrepresentation from the ownership
exclusion.

## Key Links

- Paper (subscription; author manuscript free in PMC): https://doi.org/10.1016/j.wneu.2019.01.297
- Europe PMC: https://europepmc.org/article/PMC/PMC6706326
- **Local PDF: none.** NIHPA author manuscript outside the PMC open-access subset
  (`isOpenAccess: N`); Europe PMC's `?pdf=render` returns HTTP 500 and PMC's PDF endpoint is behind a
  proof-of-work bot challenge. **Full text obtained via NCBI efetch XML**
  (`db=pmc&id=6706326&retmode=xml`), which carries the complete body and all tables.

## Related profiles

- Platform: [Beiwe](../../module-02-digital-phenotyping/profiles/beiwe.md)
- BYOD selection effects, the structural treatment of this profile's 42% finding:
  [`byod-demographic-imbalance.md`](byod-demographic-imbalance.md)
- Sociodemographic structure in Beiwe missingness:
  [`beiwe-missing-data-sociodemographic.md`](beiwe-missing-data-sociodemographic.md)
- Same clinical setting and same team's later, operations-first programme:
  [`beiwe-pain-clinic-operational-report.md`](beiwe-pain-clinic-operational-report.md)
- Unsupported Beiwe baseline with a formal time-to-discontinuation analysis, which this study lacks:
  [`beiwe-als-adherence.md`](beiwe-als-adherence.md)
- Postoperative remote monitoring: [`withings-postop-remote-monitoring.md`](withings-postop-remote-monitoring.md)

## Sources

1. Cote DJ, Barnett I, Onnela JP, Smith TR. *World Neurosurg* 2019;126:e241–e249.
   DOI 10.1016/j.wneu.2019.01.297. Full text and Tables 1–2 read from the NCBI efetch PMC XML render
   of PMC6706326, 2026-09-01. Establishes every figure in this profile except the explicitly-flagged
   duty-cycle realisation inference.
