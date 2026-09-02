# Fu et al. 2024 — Beiwe embedded in a running outpatient pain clinic: the Pain-IDR operational report, N=77, 18 months

## Quick Facts

| Field | Details |
|---|---|
| Citation | Fu M, Shen J, Gu C, Oliveira E, Shinchuk E, Isaac H, Isaac Z, Sarno DL, Kurz JL, Silbersweig DA, **Onnela JP**, Barron DS. "The Pain Intervention & Digital Research Program: an operational report on combining digital research with outpatient chronic disease management." *Frontiers in Pain Research* 2024;5:1327859. DOI [10.3389/fpain.2024.1327859](https://doi.org/10.3389/fpain.2024.1327859). PMC10869590. |
| Study design | Self-described **operational report** on an ongoing clinical-research programme launched 2022, covering its first 18 months across two sites. Narrative (workflow evolution) plus quantitative (recruitment, participant experience, data characteristics). Not a hypothesis-testing study. |
| Sample size (enrolled / analyzed) | **77 consented and onboarded → 38 (49.4%) completed the 6-month protocol**; 39 withdrew or were dismissed. 54 recorded reasons for declining consent or withdrawal. |
| Population | Outpatients with chronic pain at two Mass General Brigham sites (Weymouth, then Charlestown/Spaulding). Mean age **55.5 (SD 15.8)**, range 20–85; 51 female / 26 male; **79% White** (61/77). Screening required age **≥50**, English, and personal smartphone ownership. |
| Duration | 6-month protocol per participant; programme running since 2022, report covers first 18 months. |
| Devices/platforms used | **[Beiwe](../../module-02-digital-phenotyping/profiles/beiwe.md)** on participants' own smartphones (BYOD). Passive: GPS, accelerometer, smartphone usage statistics. Active: daily 5-question micro-surveys (PROMIS-29 split across days) + daily audio journals up to 3 min. REDCap used for consent and out-of-app instruments. |
| Funding/COI | Brigham & Women's / Spaulding / Harvard Chan. **Onnela, Beiwe's originator, is a co-author.** |
| Last verified | 2026-09-01 |

## Summary

Almost every study in Module 3 reports operational facts as a by-product of a scientific question.
This one is the reverse: the operational design *is* the paper. It documents how a research protocol
was folded into a live outpatient clinic, what broke, and what the team changed in response —
including two mid-course IRB amendments — over 18 months and two sites.

Its headline numbers are **49.4% six-month completion**, and among completers a mean **84% overall
data completeness, split as 51% active and 78% passive**. Those three figures need to be read
together and carefully: the 84/51/78 split is computed **only over the 38 participants who completed
six months** — i.e. over the better half of the cohort by construction. Applied across all 77
onboarded participants the picture is much weaker, and the paper does not compute that version.

The most transferable content is not the numbers but the **operational apparatus**: a three-layer
screening cascade running through the clinic's own scheduling system, a formal
minimum-completion-and-dismissal rule adopted after the fact, twice-weekly data checks by phone or
email, a compensation model tied to monthly data volume, and a virtual REDCap consent flow built in
response to COVID-era patient reluctance. Teams planning to run digital phenotyping inside routine
care can lift this structure more or less directly.

Its most counter-intuitive finding is that **age did not predict completion** in a cohort screened
to be ≥50 and running to age 85 — and that among those who withdrew, days-on-study was *negatively*
correlated with age (younger withdrawers left sooner). The authors explicitly frame this against the
prior expectation that older patients would be less able to participate: "We observed the opposite."

## Instrumentation and Deployment Model

**BYOD Beiwe, both streams, plus REDCap for anything outside the app:**

- **Passive:** GPS location, accelerometer, smartphone usage statistics — collectively branded by
  the team as the **HERMES phenotype** (High-frequency Ecological Recordings of Mobility, Emotion
  and Sociability). Exact duty cycles are not published in this paper (deferred to a subsequent
  publication).
- **Active:** daily **micro-surveys of five questions**, constructed by splitting the PROMIS-29
  across days, one of which is a repeated daily pain score; plus a **daily audio journal of up to 3
  minutes**. Note the micro-survey design choice — the same burden-reduction strategy tested
  head-to-head by van den Berg et al. 2022 (assessed but not profiled; see the tranche report).
- **Instruments delivered outside Beiwe via REDCap:** PROMIS-10 at the initial visit, the User
  Engagement Scale–Short Form, and the end-of-study feedback survey.

**Enrolment and consent workflow — three screening layers, all inside clinic operations:**

1. **Telephone screening by call-centre staff** against research eligibility (English-speaking, ≥50
   years old, owns a smartphone). Eligible interested patients trigger an **Epic message to the
   research assistant**.
2. **Weekly research-team meeting** reviewing that week's scheduled patients, screening for
   eligibility, and **flagging recruitment candidates in the Epic scheduling system**.
3. **Screening during the clinical visit** by a Pain-IDR clinician, who refers interested patients to
   the research assistant.

At Charlestown/Spaulding the RA had a dedicated clinic room, and research visits were held
separately after the clinical visit — which the authors credit for "establishing rapport which we
feel was important in promoting longitudinal participation." That is an unquantified but explicit
claim about physical co-location as a retention mechanism.

**Consent evolved mid-programme.** The team began with in-person intakes and paper consents, then
built a **REDCap video-plus-survey virtual consent flow** in response to COVID-19 concerns and to
patients' varying comprehension needs. Onboarding time per patient varied "in large part on a
patient's technological literacy," which the authors define operationally as being able to fill
fields, view phone notifications, and set permissions.

**Compensation:** monthly, **scaled to how much data was uploaded**, "as a way to promote patient
engagement and monitor progress." Programme totals:

| | Total paid | Mean per participant |
|---|---|---|
| All 77 onboarded | **$8,379.15** | $109.84 |
| 38 completers | $6,708.97 | **$177.09** |
| 39 non-completers | $1,218.25 | **$44.32** |

**Engagement monitoring and the dismissal rule — adopted mid-study by IRB amendment.** The original
protocol had **no minimum completion requirement**. After observing that some participants stopped
responding to micro-surveys within weeks of onboarding, the team amended the IRB protocol so that:

- a participant with **one month below 20% active-data completion** is notified and asked to
  troubleshoot;
- a participant with **more than two consecutive months below 20%** is **dismissed from the study**.

This was backed by a "closed-loop learning system": check-ins at monthly follow-up visits **and
biweekly (the paper says "twice a week") data checks by phone or email** from the research
assistant, specifically to keep everyone above the 20% floor.

That is a materially different support intensity from any other Beiwe study in this module —
[Beukenhorst et al.](beiwe-als-adherence.md) had no engagement contact at all,
[Yi et al.](beiwe-chronic-disease-substudy.md) had none and no exit survey, and
[Mercier et al.](beiwe-spinal-cord-injury-incentives.md) contacted after two missing weeks. Read
the Pain-IDR completeness figures as an **actively-managed upper bound**, and note that the
dismissal rule mechanically removes the worst contributors from the completer denominator.

## Recruitment and Retention

| Stage | N |
|---|---|
| Consented and onboarded | **77** |
| Completed the 6-month protocol | **38 (49.4%)** |
| Withdrew or were dismissed | **39 (50.6%)** |

The paper does not publish an approached-to-consented funnel — a real gap for an operational report,
and the main thing missing from an otherwise unusually candid account.

**Days on study:**

| Group | Mean days |
|---|---|
| All 77 onboarded | 130.6 |
| 38 completers | **189.9** |
| 39 non-completers | **72.8** |

**Reasons for declining consent or withdrawing (n=54 recorded):**

| Reason | Share |
|---|---|
| Inability to participate due to **health or life events** | **76%** |
| **Technological difficulties with the smartphone app** | **15%** |
| **Privacy concerns** | **7%** |
| Language barrier | 2% (one patient) |

Three-quarters of loss was **situational, not technological** — health events and life circumstances
in a chronic-pain population. That is a useful corrective to the assumption that app friction is the
dominant failure mode in older cohorts; here it accounted for 15%. The single language-barrier case
led the team to add "ability to read and complete surveys in English" to the formal screening
criteria — a small, concrete example of eligibility criteria being written by field experience
rather than protocol design, and one that narrows the population.

**Predictors of completion — all null:**

| Variable | Completers | Non-completers | Test |
|---|---|---|---|
| Age (mean) | 58.8 (SD 13.3) | 52.3 (SD 17.5) | **p=0.10**, two-sided t-test |
| Gender | — | — | **p=0.86**, chi-square |
| Compensation amount | — | — | not related to completion |

Among those who withdrew, days-on-study was **negatively correlated with age (r = −0.06)** — i.e.
younger withdrawers left sooner, though at r = −0.06 this is a numerically negligible association
that the authors nonetheless report and interpret. **Treat that specific correlation as noise**;
the defensible version of the finding is the null on age and completion.

Racial composition differs notably between groups — completers 26/38 (68%) White vs non-completers
35/39 (90%) White — but the paper does not test this and the "Other/Unknown" category is 7 in
completers and 0 in non-completers, which suggests a data-recording difference rather than a real
one. Not interpretable as published.

## Data Completeness and Technical Issues

**Completion rates — among the 38 six-month completers only:**

| Measure | Definition used | Rate |
|---|---|---|
| Mean days with **either** active or passive data | days with any data / 6-month window | **190 days, 84%** |
| **Active** data completion | days with **any** active data | **51%** |
| **Passive** data completion | days with **any** passive data | **78%** |

Three cautions on these numbers, in order of importance:

1. **The denominator is completers only.** Non-completers averaged 72.8 days on study and are
   excluded. Any comparison against studies that report completeness over all enrolled participants
   is invalid in this direction.
2. **The bar is "any data on the day," not a valid-hours threshold.** This is one of the most
   permissive completeness definitions in the module — compare
   [Yi et al. 2025](beiwe-nurses-health-study-burst.md)'s ≥10 valid hours or
   [Straczkiewicz et al.](actigraph-als-upper-limb-wear-time.md)'s ≥21 hours. A day with a single
   GPS fix counts as complete here.
3. **The dismissal rule truncates the low end by design.** Participants persistently below 20%
   active completion were removed, so the surviving distribution is censored.

With those caveats stated, the **51% active / 78% passive split reproduces the passive-outlasts-active
pattern** seen across every Beiwe deployment in this module, at a similar magnitude to
[Yi et al. 2025](beiwe-nurses-health-study-burst.md) (~55% active / ~60% passive) despite very
different populations, durations, and support intensity.

**Technical problems in participants' own words** (freeform feedback):

> "I liked the app when it worked. However, for most of the time the app did not display the surveys
> to fill out which resulted in my use being very inconsistent."

> "The daily surveys were way too frequent. It made me disengage from the whole thing. Maybe if the
> questions changed or I could use my data in real time to make change it would be fine but it was
> way too repetitive."

The first quote describes **surveys failing to render** — an app-level delivery failure that would
be indistinguishable from participant non-response in any completeness statistic. It is a reminder
that "active data completion 51%" bundles non-response with non-delivery, and nothing in the
published data separates them.

**Other documented friction:**

- **Permission-granting at onboarding** — participants must enable location settings for GPS and
  accelerometer collection, and "may be worried about privacy and data security." The team's
  response was supplementary education materials explicitly addressing privacy and time commitment.
- **A conceptual objection the team took seriously:** participants questioned "whether the data
  collected reflected their day-to-day reality; that is, how much of a person's experience could a
  GPS and/or accelerometer tracing capture?" The team **modified its onboarding materials** to state
  that each stream captures only a facet of lived experience. This is an unusual and worthwhile
  operational note — participant scepticism about construct validity as an engagement risk.
- **A dedicated research assistant as a continuous support channel** was the team's stated remedy
  for participants who were willing but needed technical help.

**Participant experience, quantified:** mean **3.88 on a 0–5 Likert scale** (n=17) for "I enjoyed
using the Beiwe app and being a part of the study." Note n=17 of 38 completers — the experience
measure covers under half the completers and under a quarter of those onboarded.

## Feasibility Findings

The authors' stated conclusion is deliberately modest: in both rural and urban clinical settings,
"our preliminary findings are optimistic: participants engaged the digital research over the space
of 6 months," and the programme "has successfully engaged older patients with chronic pain."

Their explicit, transferable operational lessons:

1. **Build the dismissal/minimum-completion rule into the original protocol**, not by amendment.
   The team learned this the expensive way.
2. **Instrument regular check-ins** (they used monthly visits plus twice-weekly data checks) rather
   than relying on app notifications.
3. **Build virtual consent early**, and make education materials address privacy and time commitment
   explicitly.
4. **Give the research assistant a private room in the clinic** if possible; they credit rapport
   from separate research visits with sustaining participation.
5. **Explain the epistemic limits of the data to participants**, because scepticism about whether
   sensors capture their reality is itself an engagement risk.
6. **Do not assume older patients are the problem.** Age did not predict completion in a 20–85
   cohort screened to ≥50.

## Relevance to Future Study Design

1. **Half of onboarded patients will not finish a 6-month clinic-embedded protocol**, even with
   monthly visits, twice-weekly data checks, and volume-scaled compensation. 49.4% completion is
   the realistic planning figure for this setting.
2. **Read every completeness figure's denominator before using it.** 84%/51%/78% here are
   completer-only, any-data-that-day rates from an actively-managed, censored cohort. They are not
   comparable to valid-hours-based, all-enrolled figures elsewhere in this module.
3. **Situational loss dominates technological loss 5:1.** 76% health/life events vs 15% app
   difficulty. In chronic-disease populations, budget attrition around clinical course, not around
   usability.
4. **A minimum-completion floor with a notify-then-dismiss ladder is a workable engagement lever** —
   and it changes what your completeness statistics mean. If you adopt one, report completeness both
   with and without dismissed participants.
5. **Compensation scaled to data volume did not predict completion.** Completers earned more
   ($177 vs $44) because they stayed longer, not the reverse; the authors explicitly report
   compensation amount as unrelated to completion. Contrast with
   [Mercier et al.](beiwe-spinal-cord-injury-incentives.md), where a *threshold* incentive did track
   retention.
6. **Distinguish survey non-delivery from survey non-response.** A participant reported surveys
   simply not displaying "most of the time." No completeness metric in this paper — or in most
   papers — can tell those apart.
7. **Recruit through the clinic's own systems.** Call-centre screening → Epic flagging → weekly team
   review → in-visit clinician referral is a reusable four-step cascade that costs the research team
   little incremental effort per patient.
8. **Publish the approached-to-consented funnel.** This report's main omission; without it the 77
   cannot be placed against the clinic's patient volume.

## Evidence Confidence

**Verified** for all recruitment, completion, days-on-study, compensation, reason-for-withdrawal and
data-completion figures, the screening cascade, the dismissal rule, and the participant quotations —
all read directly from the published open-access PDF including Table 1 and Figure 2's caption.

**Unclear** for the racial composition difference between completers and non-completers — untested
by the authors and confounded by a suspicious "Other/Unknown" asymmetry (7 vs 0).

**Reported, and probably noise, for "days on study negatively correlated with age among
withdrawers."** The authors state r = −0.06, which is negligible; they nonetheless build an
interpretive claim on it. The robust version of this result is the **null** on age and completion
(p=0.10), which is well supported.

**Not comparable without adjustment:** the 51%/78% active/passive completion rates. See the three
cautions above. The paper is transparent about the completer-only denominator; it is easy to lose in
citation.

**Pre-heartbeat, mostly.** Data collection began in 2022 and the report covers the first 18 months
(through roughly mid-to-late 2023, published February 2024). Beiwe's server-side heartbeat/keepalive
push was globally enabled **2024-05-29** — after this reporting window. The 78% passive figure is
therefore a **pre-heartbeat lower bound**. See [`beiwe-als-adherence.md`](beiwe-als-adherence.md) and
Tier 14 Q106 in `../../shared/unresolved-questions.md`. Because the programme is ongoing, a future
Pain-IDR publication would be one of the few available opportunities to observe pre/post-heartbeat
passive completeness in the same protocol.

**COI.** Onnela, Beiwe's originator, is a co-author. The report is about the platform's use in
practice, and the exposure would be to claims flattering Beiwe. It reports instead: 49.4%
completion, 51% active-data completion, participants describing surveys that did not display, an app
that had to be backstopped by twice-weekly human check-ins and a formal dismissal rule, and 15% of
loss attributed directly to technological difficulty with the app. The framing does not protect the
platform. **The findings that generalise here are about clinical-research operations, not about
Beiwe** — the screening cascade, consent flow, dismissal ladder and support model would transfer
unchanged to any Module 2 platform.

**Generalisability.** N=77, two sites in one US health system, screened to age ≥50 and
English-speaking, 79% White, smartphone ownership required. The programme's own screening criteria
(≥50, English, owns a smartphone) exclude precisely the "access-limited" population the introduction
motivates the work by. The report is a description of one programme's first 18 months, not a
controlled evaluation of anything.

## Key Links

- Paper (open access): https://doi.org/10.3389/fpain.2024.1327859
- Europe PMC: https://europepmc.org/article/PMC/PMC10869590
- **Local PDF (already in the knowledge base, not duplicated):**
  `../../module-02-digital-phenotyping/literature/onnela-lab/2024-fu-frontierspainresearchlau-pain-intervention-digital-research-operational-report.pdf`

## Related profiles

- Platform: [Beiwe](../../module-02-digital-phenotyping/profiles/beiwe.md)
- **Most contact-intensive Beiwe deployment in the module** — read against the least
  ([`beiwe-als-adherence.md`](beiwe-als-adherence.md), no engagement contact of any kind) and the
  uncompensated large-cohort case ([`beiwe-chronic-disease-substudy.md`](beiwe-chronic-disease-substudy.md)).
- Threshold-conditional incentive, contrasting with this study's volume-scaled model:
  [`beiwe-spinal-cord-injury-incentives.md`](beiwe-spinal-cord-injury-incentives.md)
- Older-adult cohort, short burst, same active/passive gap:
  [`beiwe-nurses-health-study-burst.md`](beiwe-nurses-health-study-burst.md)
- Clinic-recruited Beiwe in a surgical/pain population:
  [`beiwe-spine-disease-mobility.md`](beiwe-spine-disease-mobility.md)
- Remote-monitoring implementation lessons in older patients:
  [`withings-postop-remote-monitoring.md`](withings-postop-remote-monitoring.md)

## Sources

1. Fu M, Shen J, et al. *Front Pain Res* 2024;5:1327859. DOI 10.3389/fpain.2024.1327859. Full text,
   Table 1 and figure captions read from the published open-access PDF held locally at
   `module-02-digital-phenotyping/literature/onnela-lab/`, 2026-09-01, via `pdftotext` in both
   `-layout` and reflow modes (the latter needed to recover the reasons-for-withdrawal percentages,
   which `-layout` interleaved across columns). Establishes every figure in this profile.
