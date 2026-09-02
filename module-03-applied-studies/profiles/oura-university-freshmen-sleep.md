# Soon et al. 2025 — Oura Ring 3 across a 20-week university semester, N=638, 64,642 nights, compensated up to USD 263

## Quick Facts

| Field | Details |
|---|---|
| Citation | Soon CS, Chua XY, Leong RLF, Ong JL, Massar SAA, Qin S, Chong KHM, **Onnela JP**, Chee MWL. "A longitudinal study of sleep in university freshmen: facilitating and impeding factors." *SLEEP* 2025;48(10):zsaf156. DOI [10.1093/sleep/zsaf156](https://doi.org/10.1093/sleep/zsaf156). PMC12515602. Advance access 9 June 2025. |
| Study design | Prospective longitudinal cohort, STROBE-reported. Multi-stream: continuous wearable sleep tracking + daily EMA + intermittent time-use diaries + institutional class timetables. |
| Sample size (enrolled / analyzed) | **638 enrolled; 69 withdrew (10.8%) over the semester.** 500 participants had ≥4 weeks of data in each instructional period and entered the primary mixed-model analysis. |
| Population | Freshmen entering the **National University of Singapore** in the 2023–24 academic year. Mean age 20.3 (SD 1.3); 51.7% female; **357 (56.0%) living on campus, 281 (44.0%) off campus**. |
| Duration | **20 weeks** — one full semester including instructional, reading, examination and vacation weeks. |
| Devices/platforms used | **[Oura Ring 3](../../module-01-wearables/profiles/oura.md)** (provisioned; purchased with grant funds) + the research group's **proprietary Z4IP smartphone app** for daily EMA and time-use diaries (**not profiled in Module 2 — expansion candidate**). |
| Funding/COI | Lee Foundation grant to MWLC; **rings were purchased with these funds, with no contribution from Oura**. Senior author **MWL Chee sits on the Medical Advisory Board of Oura Health**; the authors state the study was independently designed, funded and conducted, and report no financial conflicts. **Onnela is a co-author** but no Beiwe or other Onnela-lab platform was used. |
| Last verified | 2026-09-01 |

## Summary

The largest consumer-wearable longitudinal deployment in this tranche and one of very few
non-Beiwe, non-US studies in Module 3: **638 students, one provisioned smart ring each, 20 weeks,
64,642 nights of sleep data.**

It is included here for three operational reasons rather than its sleep findings.

First, it is a **generous-compensation benchmark**. Participants earned up to **SGD 355 (~USD 263)**,
scaled to the number of study components completed each day — an order of magnitude above the
per-participant incentives elsewhere in this module. What that bought: **72.4% of possible
person-nights of ring data, 10.8% withdrawal over 20 weeks**, and Oura data from more than 450
participants in every instructional week.

Second, it reproduces the **passive-outlasts-active gradient inside a single cohort with three
streams of graded burden**, and the gradient is steep: **72.4% (ring, zero daily effort) → 66.2%
(time-use diary, but only during three protocol fortnights) → 42.8% (daily EMA app)**. The wearable
returned nearly 1.7× the data of the daily self-report app, in the same people, over the same weeks.

Third — and this is the unusual part — the authors **tested whether the missingness biased their
conclusions** rather than merely acknowledging it. Sleep-timing trends were "similarly observed in
both high and low compliance participants," which is a specific, checkable claim of the kind almost
no study in this module makes. It is a supplementary-figure analysis, so its strength is limited,
but the practice is worth copying.

## Instrumentation and Deployment Model

**One provisioned wearable and three self-report channels:**

1. **Oura Ring 3**, worn continuously. Participants were **required to wear it at least 20 hours
   daily** for a night's sleep to be tracked. For each day, the **longest sleep period between
   18:00 the previous day and 17:59 the current day** was designated the main sleep episode; other
   sleep periods were counted as naps. Additional wear-time-based filtering was applied "to ensure
   accurate characterization of the broad range of sleep patterns under free-living conditions,
   particularly, nights with irregular, short sleep or absent sleep" (detail in supplementary
   material not retrieved this pass).
2. **Daily EMA via the Z4IP app**, delivered between **20:00 and 23:59** — a questionnaire with
   daily-repeating and weekly-repeating items, plus an audio diary component.
3. **Time-use diaries via Z4IP**, during **three protocol fortnights** (start, middle and end of
   semester). Participants selected activities from a list, tagging group activities; entries were
   **editable for up to 3 days**. Only days with **≥75% completion and ≥3 activity types** were
   analysed.
4. **Official institutional class timetables**, used to stratify wake times against each
   participant's first class of the day — a zero-burden contextual data source that produced one of
   the study's central results.

**Compensation: up to SGD 355 (~USD 263) per participant, scaled to the number of study components
completed each day.** This is a volume-scaled model like [Fu et al.](beiwe-pain-clinic-operational-report.md)'s
rather than a threshold model like [Mercier et al.](beiwe-spinal-cord-injury-incentives.md)'s, and
it is by an order of magnitude the largest per-participant incentive in this tranche.

**Missing-data handling — stated and strict:** "**No imputation was performed for missing data.**"
Days with overseas travel were excluded from all analyses. Weekly averages required a **minimum of
one weekday and one weekend day** for a given week to be included.

**Recruitment:** flyers, posters, emails and orientation-camp announcements before the first
semester, with eligibility assessed by an online demographic survey before consent. NUS IRB
approved; STROBE followed.

## Recruitment and Retention

| Stage | N |
|---|---|
| Enrolled | **638** |
| **Withdrew over the 20 weeks** | **69 (10.8%)** |
| Entered the primary mixed-model analysis (≥4 weeks of data in each instructional period) | **500 (78.4%)** |
| Provided ≥100 days of Oura data | **433 (67.9%)** |

**10.8% withdrawal over a 20-week continuous-wear protocol is low** by this module's standards, and
the population is favourable in every direction: young, digitally fluent, institutionally
co-located, and paid well. Weekly participation declined gradually across the semester, but **every
instructional week retained Oura data from more than 450 participants** (>70% of enrolled).

The gap between 638 enrolled and 500 analysable (21.6% loss) is the analytic-eligibility filter —
the ≥4-weeks-in-each-period requirement — not withdrawal. As in
[Straczkiewicz et al.](actigraph-als-upper-limb-wear-time.md), the analytic criterion removes about
twice as many participants as dropout does.

## Data Completeness and Technical Issues

**Yield by stream — the burden gradient, in one cohort:**

| Stream | Participant-days | Completeness | Daily participant effort |
|---|---|---|---|
| **Oura Ring 3 sleep** | **64,642** | **72.4%** | Wear the ring (≥20 h/day) |
| Time-use diary (three protocol fortnights) | 17,726 | **66.2%** | Categorise the day's activities, editable for 3 days |
| **Z4IP daily EMA** | **38,209** | **42.8%** | Complete a nightly questionnaire in a 4-hour window |

A further **8,005 days of time-use diary were recorded outside the required fortnights** —
volunteered data, at roughly 45% of the in-protocol volume. Some participants kept diarising when
not asked to.

**The 72.4% ring figure is a person-night completeness rate** (64,642 nights against 638
participants × ~140 days), computed **without imputation** and after a **≥20-hour daily wear
requirement**. That combination — a strict wear criterion, no imputation, and 72.4% yield — makes it
one of the more trustworthy completeness figures in this module, and a useful contrast with
[Straczkiewicz et al.](actigraph-als-upper-limb-wear-time.md), whose 21-hour criterion produced
18.2% valid days on an intermittent wear protocol. **The difference is the protocol, not the
threshold**: continuous wear with a 20-hour rule vastly outperforms intermittent wear with a 21-hour
rule.

**Distribution of participant-level yield:** 433 of 638 (67.9%) provided **≥100 days** of Oura data
out of ~140 possible. The remaining third is not further characterised.

**Bias check — the practice worth copying.** The authors note that "lower completion rates were
observed on the more time-consuming, self-report channels (e.g. EMA, time-use diaries) that were
delivered later in the semester," acknowledge that "the reduced numbers contributing to these data
could bias the results," and then **test it**: "the overall trends in sleep timing were similarly
observed in both high and low compliance participants (Supplementary Figure S1), i.e. not likely to
have been affected by missing data." That is a missingness sensitivity analysis presented as a
routine obligation rather than a special contribution.

**Documented technical issues: essentially none.** The paper reports no device failures, sync
problems, app crashes, or battery complaints — a notable silence given 638 devices over 20 weeks. It
is not clear whether none occurred or whether none were recorded; **treat the absence as
unreported, not as zero.**

**A measurement-reactivity caveat the authors raise themselves:** "Although we did not prompt any
behavioral change, we cannot exclude the possibility that participation heightened valuation of
sleep through creating awareness of unhealthy sleep habits **as students viewed their sleep data**
and reflected on their use of time." The Oura Ring is a **consumer** device with a consumer feedback
app — participants saw their own scores. That is a structural difference from research-grade
accelerometers (blinded by default) and a genuine threat to using consumer wearables in
observational designs.

## Feasibility Findings

The authors' explicit feasibility claim: "**Broad and sustained adoption of the digital phenotyping
tools used in this study (>70 per cent of participants providing Oura data over 20 weeks)
underscores their acceptance by today's digitally savvy students.**"

They also note a design advantage specific to a single-semester cohort: "the lack of seasonal effects
eliminates a common confound in extended longitudinal studies that focus on sleep duration and
timing" — Singapore's equatorial location removes photoperiod variation, which is an unusual and
genuine methodological asset for a longitudinal sleep study.

Their stated limitations relevant to deployment: reactivity from participants viewing their own
sleep data; lower completion on self-report channels; and the absence of light and meal-timing data
that would have enriched the design.

## Relevance to Future Study Design

1. **A continuous-wear consumer ring, well compensated, in a young co-located cohort, yields ~72% of
   person-nights over 20 weeks with 10.8% withdrawal.** That is the planning figure, and it is close
   to a best case — every population and design factor here is favourable.
2. **The burden gradient is steep and reproducible: 72.4% wearable / 66.2% intermittent diary /
   42.8% daily EMA, same people, same semester.** A nightly self-report app returns roughly 60% of
   what a passively-worn device does. Budget active and passive streams separately; never assume a
   shared completeness rate.
3. **Continuous wear beats intermittent wear on valid-day yield even at a similar threshold.**
   20 h/day continuous → 72.4% here; 21 h/day on a one-week-in-three protocol → 18.2% in
   [Straczkiewicz et al.](actigraph-als-upper-limb-wear-time.md) The protocol dominates the
   threshold.
4. **Run a compliance-stratified sensitivity analysis and publish it.** This study compared sleep
   trends in high- vs low-compliance participants. It is cheap, and it converts an acknowledged
   limitation into a checkable claim.
5. **Free contextual data can carry a study's main result.** Institutional class timetables cost
   nothing in participant burden and produced the central finding (52.4% of post-midterm wake times
   occurring after an 08:00 class had started). Look for administrative data that can be joined to
   sensor data.
6. **Consumer wearables show participants their own data, and that is a design decision you are
   making whether or not you notice.** In observational sleep research this is a reactivity risk the
   authors flag explicitly. Research-grade devices can be blinded; consumer rings largely cannot.
7. **State the imputation policy.** "No imputation was performed" is a one-line disclosure that makes
   the 72.4% directly interpretable. Compare with
   [Cote et al.](beiwe-spine-disease-mobility.md), where every mobility result rests on imputed GPS.
8. **Report device failures explicitly, including a count of zero.** Silence at 638 devices × 20
   weeks is not evidence of reliability.

## Evidence Confidence

**Verified** for enrolment (638), withdrawals (69), the analytic subsample (500), the per-stream
day counts and completeness rates (64,642 / 72.4%; 38,209 / 42.8%; 17,726 / 66.2%; 8,005
out-of-protocol), the ≥100-days figure (433, 67.9%), the ≥20-hour wear requirement, the
no-imputation policy, the compensation ceiling (SGD 355), and the residence split — all read
directly from the published open-access PDF.

**Corroborated** for the claim that missingness did not bias the sleep-timing conclusions. The
authors performed the check and report it, but the evidence lives in a supplementary figure not
retrieved in this pass, and "similar trends in high- and low-compliance participants" is a visual
rather than statistical criterion as described.

**Unclear** for technical failure modes. None are reported; whether that reflects none occurring or
none being recorded cannot be determined from the paper.

**Unclear** for the supplementary wear-time filtering beyond the ≥20-hour rule (Supplementary
Methods and Table S1, not retrieved). The headline 72.4% therefore rests on a filter that is only
partly specified in the main text.

**Not applicable — heartbeat.** No Beiwe or smartphone passive-sensing platform was used; the EMA
app is the group's own Z4IP. The pre-heartbeat caveat attaching to the Beiwe profiles in this
tranche does not apply.

**COI — Oura-adjacent, and disclosed.** Senior author MWL Chee **sits on the Medical Advisory Board
of Oura Health**. The authors state the study was independently designed, funded and conducted, and
that the rings were purchased with Lee Foundation funds "with no contribution from Oura." The
exposure is to claims flattering the device — and the paper does make one: that >70% Oura provision
over 20 weeks "underscores [the tools'] acceptance." That is a favourable framing of the study's own
completeness statistic by an author with a vendor advisory relationship, and it should be read as
such. Against that: the paper makes **no accuracy or validity claim** about Oura's sleep staging or
duration measurement (which would be Module 1's territory and the more commercially sensitive
question), reports the EMA app's 42.8% without softening it, and volunteers the reactivity concern
that arises specifically from Oura being a consumer device with participant-visible feedback.
**Onnela is a co-author but no Onnela-lab platform is used**, so the Beiwe-developer COI that
dominates the rest of this tranche is absent here.

**Generalisability.** Single institution, single national context (Singapore), first-year
undergraduates aged ~20, provisioned devices, and generous compensation. Every one of those pushes
completeness upward. The equatorial location that removes the seasonal confound also means
photoperiod-driven sleep findings will not transfer to temperate cohorts.

## Key Links

- Paper (open access, CC BY): https://doi.org/10.1093/sleep/zsaf156
- Europe PMC: https://europepmc.org/article/PMC/PMC12515602
- NUS Centre for Sleep and Cognition: https://medicine.nus.edu.sg/csc/
- **Local PDF (already in the knowledge base, not duplicated):**
  `../../module-01-wearables/literature/oura/2025-soon-sleep-longitudinal-study-sleep-university-freshmen-facilitating.pdf`

## Related profiles

- Device: [Oura](../../module-01-wearables/profiles/oura.md)
- **Module 2 expansion candidate surfaced here:** the **Z4IP** EMA/time-use app (NUS Centre for
  Sleep and Cognition) — used as the study's sole active-data instrument, not profiled in Module 2.
- Wear-time definition and intermittent-vs-continuous protocol contrast:
  [`actigraph-als-upper-limb-wear-time.md`](actigraph-als-upper-limb-wear-time.md)
- Consumer-wearable adherence under BYOD at very large scale:
  [`fitbit-heart-study-afib.md`](fitbit-heart-study-afib.md),
  [`allofus-fitbit-step-counts.md`](allofus-fitbit-step-counts.md)
- Rest-activity monitoring with a consumer wearable in a clinical population:
  [`sleepsight-schizophrenia-rest-activity.md`](sleepsight-schizophrenia-rest-activity.md)
- Compensation models for comparison:
  [`beiwe-spinal-cord-injury-incentives.md`](beiwe-spinal-cord-injury-incentives.md) (threshold),
  [`beiwe-pain-clinic-operational-report.md`](beiwe-pain-clinic-operational-report.md) (volume-scaled)

## Sources

1. Soon CS, Chua XY, Leong RLF, Ong JL, Massar SAA, Qin S, Chong KHM, Onnela JP, Chee MWL.
   *SLEEP* 2025;48(10):zsaf156. DOI 10.1093/sleep/zsaf156. Full text, Table 1 and Figure 2 caption
   read from the published open-access PDF held locally at `module-01-wearables/literature/oura/`,
   2026-09-01, via `pdftotext -layout`. Supplementary Methods, Table S1 and Figure S1 were **not**
   retrieved.
