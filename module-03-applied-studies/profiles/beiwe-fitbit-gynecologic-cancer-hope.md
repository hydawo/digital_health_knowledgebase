# Wright et al. 2018 — HOPE pilot: Beiwe + two Fitbits in gynecologic cancer, N=10, 30 days, no financial incentive

## Quick Facts

| Field | Details |
|---|---|
| Citation | Wright AA, Raman N, Staples P, Schonholz S, Cronin A, Carlson K, Keating NL, **Onnela JP**. "The HOPE Pilot Study: Harnessing Patient-Reported Outcomes and Biometric Data to Enhance Cancer Care." *JCO Clinical Cancer Informatics* 2018;2:1–12. DOI [10.1200/CCI.17.00149](https://doi.org/10.1200/CCI.17.00149). PMC6556148. |
| Study design | Single-arm, single-site **pilot intervention** (not observational) with pre-specified feasibility thresholds, plus qualitative exit interviews with both patients and clinicians. No control arm. |
| Sample size (enrolled / analyzed) | **18 potentially eligible → 8 gatekept out by treating oncologists → 10 approached → 10 consented and enrolled (100%).** 8 of 10 used the Beiwe app; 9 of 10 produced passive data; 9 of 10 wore both Fitbits. |
| Population | Women with advanced gynecologic cancer receiving palliative chemotherapy, age >20. Mean age 60 (SD 11); 8 married; **4 of 10 identified as Black or other non-White race**; high health literacy and numeracy; 80% reported being somewhat or very comfortable with smartphone apps; mean 3 symptoms at baseline; mean ECOG performance status 1 (SD 0.66). |
| Duration | **30 days.** |
| Devices/platforms used | **[Beiwe](../../module-02-digital-phenotyping/profiles/beiwe.md)** on participants' own smartphones (BYOD, iOS + Android) + **two provisioned [Fitbits](../../module-01-wearables/profiles/fitbit-google.md)**: **Fitbit Zip** worn at the waist and **Fitbit Charge 2** worn on the non-dominant wrist, both during all waking hours, both synced daily via the **Fitabase** analytics platform. |
| Funding/COI | Dana-Farber/Harvard Cancer Center and Harvard Chan. **Onnela, Beiwe's originator, is senior author; Staples and Carlson are Onnela-lab affiliates.** ASCO conflict-of-interest disclosures accompany the paper. |
| Last verified | 2026-09-01 |

## Summary

Ten participants, thirty days — trivially small, and included in this module for one reason: it
reports **an enrolment funnel, an adherence funnel, and an acceptability funnel, all three, at the
individual-participant level**, and its headline "approach-to-consent rate was 100%" turns out to be
a much more interesting number than it looks.

The 100% is real: all ten patients who were approached consented. But **eighteen patients were
potentially eligible, and their treating oncologists removed eight of them before anyone was
approached** — for "bad timing for the patient" (4), "too distressed" (3), and "ineligible as a
result of language barriers" (1). **The real yield from the eligible pool is 10/18 = 56%, and the
binding constraint was clinician gatekeeping, not patient refusal.** A study reporting only the
approach-to-consent rate would present a 100% recruitment success that concealed a 44% pre-approach
loss.

The adherence numbers — **90% to the wearables, 70% to the smartphone surveys** — are among the
highest in this module, and they were achieved with **no financial incentive at all**. Participants
kept the Fitbits and an external battery charger after the study; that was the entire compensation.
Against [Mercier et al.](beiwe-spinal-cord-injury-incentives.md)'s 50%-without-incentive and
[Yi et al.](beiwe-nurses-health-study-burst.md)'s ~55% EMA response, that demands explanation, and
the most likely one is not the technology: this was a **30-day intervention with daily monitoring by
research staff and a real-time clinical safety loop** — participants had a concrete reason to
believe someone was reading their answers.

Its most decision-relevant technical finding is a single sentence: **one participant was excluded
from the app entirely because her Android device ran version 4.3 (2012), which was incompatible with
Beiwe.** In a ten-person study, an OS-version floor cost 10% of the active-data sample.

## Instrumentation and Deployment Model

**Three instruments, one participant-facing loop:**

1. **Beiwe (BYOD)** delivering daily PRO-CTCAE symptom items, with **branching logic** used to
   stratify responses by risk and deliver **tailored symptom-management advice on-screen**. Passive
   Beiwe streams — GPS, accelerometry, screen on/off logs, call logs, Wi-Fi — were also collected but
   **not analysed until the end of the study**.
2. **Fitbit Zip at the waist** and **Fitbit Charge 2 on the non-dominant wrist**, worn during all
   waking hours, synced daily, both linked to **Fitabase** so investigators could remotely monitor
   physical activity in near-real time.
3. **A real-time clinical response loop.** Active Beiwe data was **monitored daily**. High-risk
   symptom reports triggered in-app advice to call the clinician, plus a staff phone call to the
   participant and an email to the clinical team. The app home screen included a call button that
   dialled staff nurses for triage.

**Data quality monitoring using device disagreement — worth copying.** The team hypothesised that
**an active heart rate on the Charge 2 combined with a low step count** meant either genuine
inactivity (a health signal) or non-adherence (a data signal), and used that combination as a
trigger to contact participants. It fired twice: one participant was preparing to go to the
emergency department for severe nausea and vomiting (her clinical team resolved it by phone), and
one had been hospitalised for a procedure. **Both were true positives for the health interpretation,
not the non-adherence interpretation** — a small but genuine demonstration that cross-sensor
disagreement can be operationalised as a monitoring rule rather than left as noise.

**Compensation: none.** Participants kept the two accelerometers and an external battery charger
after study completion; "no additional financial incentives were offered." The battery charger is a
small detail that matters — it is a direct acknowledgement that running Beiwe plus two synced
Fitbits imposes a real power burden.

**Pre-specified feasibility thresholds** (declared in Methods, which is good practice and rare):

| Criterion | Threshold | Achieved |
|---|---|---|
| Enrolment rate among eligible patients approached | ≥60% | **100%** (10/10) |
| Adherence to daily smartphone surveys ≥4 days/week | ≥70% | **70%** (7/10) |
| Adherence to the Fitbits ≥4 days/week | ≥80% | **90%** (9/10) |

Note the definitions: **adherence here is a count of participants meeting a ≥4-days-per-week bar,
not a percentage of prompts answered or days worn.** Ten participants, so each one is worth ten
percentage points. "70% adherent to smartphone surveys" means *seven people* cleared the bar — it
does not mean 70% of surveys were answered, and the paper does not report the latter.

## Recruitment and Retention

**The full funnel, with the gatekeeping step made explicit:**

| Stage | N | Note |
|---|---|---|
| Identified as potentially eligible | **18** | |
| **Removed by treating oncologist before approach** | **8 (44%)** | "bad timing for the patient" (4), "too distressed" (3), "language barriers" (1) |
| Approached to participate | **10** | |
| Consented and enrolled | **10 (100%)** | The paper's headline "approach-to-consent rate was 100%" |
| **Effective yield from the eligible pool** | **10/18 = 56%** | Not reported as such by the authors |

All oncology providers agreed to approach, recruit and obtain consent — so the gatekeeping was
case-by-case clinical judgement, not provider refusal to participate.

**Retention:** no participant is reported as withdrawing during the 30 days. All ten completed the
end-of-study acceptability questions. The relevant losses are all **participation-quality** losses
rather than dropout, and they are itemised below.

## Data Completeness and Technical Issues

**Participant-level participation, itemised (n=10):**

| Stream | Participants contributing | Named exceptions |
|---|---|---|
| Daily smartphone surveys ≥4 days/week | **7** | 1 answered **no questions at all**; 1 had **Android 4.3 (2012), incompatible with Beiwe**; 1 answered **only three surveys, in the final week** |
| Wore **both** Fitbits daily throughout | **9** | 1 wore neither |
| Used the Beiwe app (received in-app advice) | **8** | mean 10 symptoms addressed (SD 9) over the 30 days |
| Produced Beiwe passive data | **9** | |

**The Android version floor is the most transferable technical fact here.** A 2012 OS release made a
2018 study's app unusable for that participant. In a BYOD design the device population is whatever
the cohort happens to own, and in older or lower-income cohorts that tail is long. **Screen for OS
version at eligibility, not at onboarding** — this participant consented, enrolled, and then could
not participate.

Note also the asymmetry: **9 of 10 produced passive Beiwe data but only 8 of 10 used the app**, and
only 7 met the survey bar. Passive contribution again exceeded active contribution, consistent with
every other Beiwe deployment in this module.

**Device agreement, reported directly:** when participants wore both Fitbits, **the Charge 2
recorded more steps than the Zip, by a mean of 445 steps (SD 1,296)**. The very large SD relative to
the mean means the two devices disagreed substantially and inconsistently on individual days. Mean
daily step count on the Charge 2 was **3,973 (SD 2,305)**, rising from 3,520 (SD 1,937) in week 1 to
4,136 (SD 1,578) in week 3. Two consumer wrist/waist devices in the same cohort, on the same days,
producing step counts that differ by a wide and unstable margin is a useful caution against treating
consumer step counts as interchangeable across form factors. (Accuracy against a reference standard
is Module 1's territory — see [Fitbit](../../module-01-wearables/profiles/fitbit-google.md).)

**No data-completeness percentages are published** — no valid-day rate, no valid-hour threshold, no
survey response rate as a proportion of prompts. This is the paper's principal reporting gap and it
is what keeps it from being more useful than it is.

## Feasibility Findings

The study met all three of its pre-specified feasibility thresholds and the authors conclude the
intervention "is feasible, acceptable, and was perceived to be effective in improving symptom
management."

**Acceptability, at the individual level (n=10):**

| Statement | Response |
|---|---|
| "Participating in this study placed a substantial burden on me" | **9 disagreed or strongly disagreed** |
| "I wish I had not agreed to participate in this study" | **1 agreed** — and she attributed it to regret about **her own nonadherence**, not to burden |
| "Would recommend the application to a friend going through treatment" | **9 agreed** |

The single dissenting participant's stated reason is worth recording: regret about not adhering,
rather than resentment of the demands. That is a distinct psychological failure mode — participants
who fall behind may disengage from *guilt* rather than *burden*, which implies different remedies
(low-stakes re-entry, forgiveness of missed days) than burden reduction would.

**Clinical utility signals, from a 10-person pilot and therefore anecdotal:** two participants were
identified via step-count anomalies, and two more via survey-triggered high-risk symptom alerts.
Both patients and clinicians reported in exit interviews that the intervention increased physical
activity, communication with the care team, and symptom management.

**Authors' stated limitations:** single site, short duration (30 days), well-educated cohort with
high health literacy despite racial diversity, and **no control arm** — "this pilot does not
establish efficacy." Their stated next step was a multisite study through NCI Community Oncology
Research Program sites over a longer duration.

## Relevance to Future Study Design

1. **Report the eligible-to-approached step, not just approach-to-consent.** 100% vs 56% in the same
   study. **Clinician gatekeeping removed 44% of the eligible pool** on grounds ("bad timing," "too
   distressed") that are legitimate clinically and invisible in any funnel that starts at "approached."
   In oncology and palliative settings this is likely the largest single recruitment filter.
2. **Screen for smartphone OS version at eligibility.** One participant in ten was lost to a
   six-year-old Android release after consenting. Publish your minimum OS as an inclusion criterion.
3. **A daily-monitored intervention with a clinical response loop achieves adherence that
   observational protocols do not** — 90% wearable and 70% survey, with no money changing hands.
   The mechanism is plausibly that responses visibly *did something*. Where a study can offer that
   honestly, it may be worth more than an incentive.
4. **Cross-sensor disagreement is an operational monitoring rule, not just noise.** Active heart
   rate plus low step count, used as a contact trigger, produced two true clinical positives in 30
   days across 10 participants.
5. **Do not read "N% adherent" as "N% of prompts answered."** This study's adherence figures are
   counts of participants clearing a ≥4-days-per-week bar. Extract the definition before comparing
   against any other study.
6. **Two consumer accelerometers on the same person disagree by a wide, unstable margin** (445 steps
   mean difference, SD 1,296 between waist Zip and wrist Charge 2). Do not mix form factors within
   one analysis without an explicit reconciliation strategy.
7. **Budget for the power burden of multi-device protocols.** This study issued an external battery
   charger as part of the kit — a cheap, concrete mitigation that also functioned as the only
   participant compensation.
8. **Nonadherence can produce participant regret independent of burden.** Design a graceful re-entry
   path for participants who fall behind.

## Evidence Confidence

**Verified** for the enrolment funnel (18/8/10/10), the three pre-specified feasibility thresholds
and the results against them, the participant-level stream breakdown (7 survey-adherent, 9 wearing
both Fitbits, 8 app users, 9 passive contributors), the Android 4.3 incompatibility, the step-count
figures and inter-device difference, the acceptability responses, and the compensation model — all
read directly from the published PDF.

**Reported, and weak by construction, for all adherence percentages.** N=10 means every figure moves
in 10-point increments, and the adherence definition is a participant count against a
≥4-days-per-week bar rather than a proportion of prompts or days. **90% and 70% here are not
commensurable with the percentage-of-prompts figures reported elsewhere in this module.** Cite as
"9 of 10 participants" and "7 of 10 participants."

**Unclear** for data completeness in any conventional sense. No valid-day rate, no valid-hour
criterion, no proportion of prompts answered, no passive-stream yield. The paper's operational value
is entirely in its funnels, not its completeness.

**Reported** for the clinical-utility anecdotes (two step-anomaly detections, two survey-triggered
alerts). Four events in a single-arm ten-person pilot with no control arm; the authors say so.

**Pre-heartbeat.** Conducted and published in 2018, six years before Beiwe's server-side
heartbeat/keepalive push was globally enabled on 2024-05-29. The passive-stream observations (9 of
10 producing data) are a **pre-heartbeat lower bound**. See
[`beiwe-als-adherence.md`](beiwe-als-adherence.md) and Tier 14 Q106 in
`../../shared/unresolved-questions.md`. Given the 30-day duration and daily staff monitoring, the
background-suspension problem had limited time and opportunity to manifest here.

**COI.** Onnela, Beiwe's originator, is senior author, and two further co-authors are Onnela-lab
affiliates. The exposure is to claims that Beiwe worked well — and the paper does conclude the
intervention is feasible and acceptable. Against that: the paper reports, in a ten-person sample,
one participant who could not run the app at all on her device, one who answered nothing, and one
who answered three surveys in the final week. Those are 30% of the sample and they are named
individually. The **wearable** figures (90%) involve Fitbit, not Beiwe, and carry no
platform-developer exposure; the **funnel** figures are counts of clinic conduct. What the COI could
plausibly colour is the interpretive framing that a 30-day, 10-person, single-arm pilot demonstrates
feasibility of the *approach* — a framing the authors themselves hedge with an explicit "this pilot
does not establish efficacy."

**Nothing here is Beiwe-specific.** The gatekeeping finding, the OS-version floor, the cross-sensor
monitoring rule, and the adherence achieved under a clinical response loop would all transfer
unchanged to any Module 2 platform capable of branching surveys and daily data review.

**Generalisability.** N=10, single site (Dana-Farber), 30 days, advanced gynecologic cancer on
palliative chemotherapy, all female, high health literacy, 80% comfortable with smartphone apps. The
authors flag every one of these. Any figure from this study is a case-series observation, not an
estimate.

## Key Links

- Paper (open access): https://doi.org/10.1200/CCI.17.00149
- Europe PMC: https://europepmc.org/article/PMC/PMC6556148
- Fitabase (the Fitbit research data platform used):
  https://www.fitabase.com/
- **Local PDF (already in the knowledge base, not duplicated):**
  `../../module-02-digital-phenotyping/literature/onnela-lab/2018-wright-jcoccinformatics-hope-pilot-study-harnessing-patient-reported-outcomes.pdf`

## Related profiles

- Platform: [Beiwe](../../module-02-digital-phenotyping/profiles/beiwe.md)
- Device: [Fitbit / Google](../../module-01-wearables/profiles/fitbit-google.md)
- Other Beiwe + wearable multi-device deployment, with side-by-side wear compliance:
  [`beiwe-actigraph-modus-als-progression.md`](beiwe-actigraph-modus-als-progression.md)
- Unincentivised Beiwe baselines for comparison:
  [`beiwe-als-adherence.md`](beiwe-als-adherence.md),
  [`beiwe-chronic-disease-substudy.md`](beiwe-chronic-disease-substudy.md)
- Incentive comparison: [`beiwe-spinal-cord-injury-incentives.md`](beiwe-spinal-cord-injury-incentives.md)
- Consent/eligibility gatekeeping as the binding constraint, at much larger scale:
  [`movesense-palliative-support-trial.md`](movesense-palliative-support-trial.md)
- Fitbit-based remote monitoring in cancer/chronic disease cohorts:
  [`allofus-fitbit-step-counts.md`](allofus-fitbit-step-counts.md)

## Sources

1. Wright AA, Raman N, Staples P, Schonholz S, Cronin A, Carlson K, Keating NL, Onnela JP.
   *JCO Clin Cancer Inform* 2018;2:1–12. DOI 10.1200/CCI.17.00149. Full text, Table 1 and figure
   captions read from the published open-access PDF held locally at
   `module-02-digital-phenotyping/literature/onnela-lab/`, 2026-09-01, via `pdftotext` in both
   `-layout` and reflow modes. Establishes every figure in this profile.
