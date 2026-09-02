# Yi et al. 2025 — Beiwe 8-day intensive burst inside the Nurses' Health Study II, N=181, uncompensated

## Quick Facts

| Field | Details |
|---|---|
| Citation | Yi L, Trudel-Fitzgerald C, Hu CR, Wilt G, Chavarro J, **Onnela JP**, Grodstein F, Kubzansky LD, James P. "Measuring Psychological Well-Being and Behaviors Using Smartphone-Based Digital Phenotyping: An Intensive Longitudinal Observational mHealth Pilot Study Embedded in a Prospective Cohort of Women." *JMIR mHealth and uHealth* 2025;13:e71375. DOI [10.2196/71375](https://doi.org/10.2196/71375). PMC12407220. |
| Study design | Intensive longitudinal observational **pilot/feasibility** substudy embedded in an established prospective cohort (NHSII). Stated objective is adherence and completeness, not substantive findings. Includes an end-of-study participant feedback survey. |
| Sample size (enrolled / analyzed) | **600 invited → 333 screened → 326 eligible → 238 consented → 200 downloaded/registered → 181 transmitted data.** 174/181 contributed any passive data; **7 contributed none**. |
| Population | Active NHSII participants — US registered nurses, **all female**, mean age **67.8 (SD 3.9)**, **98.3% White** (178/181), 81.8% married, 58.6% never-smokers. **84.5% iOS** (153/181). Geographically skewed: 44.8% Midwest, 26.0% South, 17.7% West, 11.6% Northeast. |
| Duration | **8 days per participant** (day 1 baseline survey; days 2–8 intensive). Fielded 21 Jul – 21 Nov 2021. |
| Devices/platforms used | **[Beiwe](../../module-02-digital-phenotyping/profiles/beiwe.md)** on participants' own smartphones (BYOD, iOS + Android). Twice-daily EMA + minute-level accelerometer and GPS. |
| Funding/COI | NIH (R01 HL150119, U01 CA176726, U01 HL145386, R01 AG85375), Harvard Chan Dean's Fund, Thomas O. Pyle Fellowship. **Onnela, Beiwe's originator, is a co-author.** Authors declare no conflicts. **Participants were not compensated.** |
| Last verified | 2026-09-01 |

## Summary

The short-burst counterpart to [Yi et al. 2024](beiwe-chronic-disease-substudy.md)'s year-long
2,394-participant substudy, in a different and much older cohort — and the answer to "what does an
8-day Beiwe burst actually yield inside an established, highly-engaged epidemiological cohort?"

The answer is **modest and honestly reported**: 86.2% completed the one-off baseline survey, but
only **~55% of twice-daily EMA prompts** were answered across days 2–8, and **32 of 181 participants
(17.7%) submitted no EMA survey at all**. Passive completeness was better than active — 62.0%
accelerometer and 57.7% GPS valid days under a ≥10-valid-hours criterion — reproducing the
passive-outlasts-active pattern this module has now seen across three platforms.

Three features make it more useful than its size suggests. First, it publishes a **complete
CONSORT-style recruitment funnel** with the unusual final step of *consented but never transmitted*
made explicit (238 → 200 → 181), which isolates onboarding failure from consent refusal. Second, it
ran an **end-of-study feedback survey**, filling exactly the gap the 2024 substudy identified in
itself — and the feedback is discordant with the compliance numbers in an instructive way:
participants rated the app easy to use (median 85/100) and said they were likely to do it again
(median 85/100) while answering barely half the prompts. Third, it is **uncompensated**, in a cohort
whose defining characteristic is decades of voluntary survey compliance — making it close to a
ceiling estimate for goodwill-driven adherence, and a sobering one.

The authors' own diagnosis of the shortfall is **onboarding technical failure, not fatigue**:
compliance was flat across the seven days with no downward trend, and the 32 zero-response
participants clustered around installation and registration problems.

## Instrumentation and Deployment Model

**BYOD, both operating systems, no device provisioning, no compensation.** Participants downloaded
Beiwe from the iOS or Android app store and logged in with provided credentials. At study end they
were instructed to delete the app and their accounts were deactivated.

**Sampling configuration (duty-cycled explicitly to preserve battery):**

- **GPS: raw data every 15 minutes for 90 consecutive seconds.**
- **Accelerometer: 10 Hz, every 30 seconds for 10 consecutive seconds.**

Note this is a *denser* GPS cadence than the [2024 NHS3/GUTS substudy](beiwe-chronic-disease-substudy.md)
(90 s on / 810 s off) but a *sparser* accelerometer duty cycle (10 s in 30 s vs 30 s in 90 s — the
same 33% duty ratio, at a finer grain). The duty cycles are a deliberate battery trade and the
authors flag in the discussion that this non-continuous sampling is itself a source of the
completeness shortfall.

**Active protocol — twice daily, days 2–8:**

| Prompt | Contents | Median completion time |
|---|---|---|
| Early afternoon | 21 items (13 non-branching) — momentary PANAS-X affect, stress events, coping strategies | 0.8 min (mean 1.5, SD 8.3) |
| Evening (18:00) | 63 items (30 non-branching) — retrospective day affect, stressful/positive events, life satisfaction, previous night's sleep | 4.3 min (mean 5.2, SD 5.3) |
| Baseline (day 1) | Life Orientation Test–Revised (dispositional optimism) and others | — |

A survey was marked incomplete if not answered before the next prompt was sent.

**Participant instructions:** keep the smartphone on their person during waking hours, charge
regularly, and connect to Wi-Fi at least weekly to sync. Weekly Wi-Fi access, US contiguous
residence and smartphone ownership were eligibility criteria.

**Support model:** trained research assistants provided technical support by phone or email
throughout — but, as the results show, this was **not sufficient at the onboarding moment**, which
is where the losses concentrated.

**Privacy design:** raw data encrypted before transmission to AWS; GPS and survey data moved to a
separate analytical server; accelerometer data deleted from temporary analytic storage after
processing; 2FA and SSH keys on both servers; no personal or health information entered through
Beiwe.

## Recruitment and Retention

**The recruitment funnel, from a 116,429-member parent cohort:**

| Stage | N | % of invited | % of previous |
|---|---|---|---|
| Randomly selected and invited (from active, non-substudy NHSII members) | **600** | 100% | — |
| Completed eligibility screener | 333 | 55.5% | 55.5% |
| Determined eligible | 326 | 54.3% | 97.9% |
| Consented | 238 | 39.7% | 73.0% |
| **Downloaded and registered the app** | 200 | 33.3% | 84.0% |
| **Transmitted any data** | **181** | **30.2%** | 90.5% |

Two things stand out against the 2024 substudy's 7.4% end-to-end yield from 32,441 invitations.
First, **screener completion was 55.5% here versus 10.7% there** — a five-fold difference, and the
plausible explanation is that this study *individually invited 600 people by email* rather than
issuing a mass invitation, and drew from those "who have most frequently engaged with the larger
NHSII." Second, and more useful operationally: **19 people consented, installed, registered, and
still never transmitted a byte**, and a further 38 consented without ever registering. **57 of 238
consenters (24%) were lost between consent and first data.** That is a distinct, addressable failure
class that almost no deployment paper separates out.

The target was 200; 181 was achieved. The authors report **no major demographic differences among
invited, consented and enrolled participants**, and none between iOS and Android users — so the
funnel loss appears not to be demographically selective *within* this already extremely homogeneous
cohort.

**Retention within the 8 days:** participants contributed data on a mean of **7 of 8 possible days
(SD 2, median 8)**. Attrition inside the window was real but small — the authors identify app
deletion before day 8 (participant self-unenrolment) as the *primary* reason for non-collection days.

**A protocol-compliance detail worth noting:** some participants **did not delete the app at study
end and left it running for up to 150 days**, generating additional surveys and passive data that
were excluded from analysis. Uninstall-at-end is not a reliable off-switch.

## Data Completeness and Technical Issues

**Volume:** 40.0 GB total from 181 participants over 8 days — 19.2 GB accelerometer, 0.6 GB GPS,
0.01 GB survey.

**Survey compliance:**

| Stream | Rate |
|---|---|
| Baseline survey (day 1, one-off) | **156/181 = 86.2%** |
| Early afternoon EMA, days 2–8 | **705/1,267 = 55.6%** (SD 3.9% across days) |
| Evening EMA, days 2–8 | **693/1,267 = 54.7%** (SD 3.2% across days) |
| Within-survey item response (non-branching items) | 99% afternoon, 96% evening |
| **Participants submitting zero EMA surveys** | **32/181 = 17.7%** |

**Participant-level EMA compliance banding:**

| Threshold | Early afternoon | Evening |
|---|---|---|
| Completed >25% of prompts | 136 (75.1%) | 138 (76.2%) |
| Completed >50% | 118 (65.2%) | 116 (64.1%) |
| Completed >75% | **71 (39.2%)** | **69 (38.1%)** |

**Two observations the authors highlight, both counter-intuitive:**

1. **No fatigue effect.** Daily response rates fluctuated between 50% and 60% across days 2–8 with
   no downward trend, and there were no substantial differences in compliance between individual
   questions. This is despite "boring to answer every day" being the most common feedback-survey
   complaint, and despite the evening survey being three times longer than the afternoon one — **no
   compliance difference by survey length either.**
2. **The one-off baseline survey vastly outperformed the repeated ones** (86.2% vs ~55%) —
   reproducing the onboarding-moment effect the 2024 substudy found (82.7% registration survey vs
   36% ongoing mean).

**Passive completeness — participant-day level** (valid day = ≥600 valid minutes / 10 valid hours;
valid minute = ≥1 second of observation; denominator 1,267 potential participant-days, 181 × 7):

| | Accelerometer | GPS |
|---|---|---|
| Valid days | **786 (62.0%)** | **731 (57.7%)** |
| Invalid days | 293 (23.1%) | 142 (11.2%) |
| **Non-collection days (no data at all)** | **188 (14.8%)** | **394 (31.1%)** |

The **GPS non-collection rate is more than double the accelerometer's** (31.1% vs 14.8%) while its
invalid-day rate is half — i.e. GPS failed in an all-or-nothing way far more often. The authors
attribute non-collection primarily to app deletion, and secondarily to phones not being charged,
GPS being disabled, or **an operating-system update causing the Beiwe app to malfunction
temporarily**.

**Passive completeness — participant level** (proportion of the 7 days that were valid):

| | Accelerometer | GPS |
|---|---|---|
| ≥25% of days valid | 145 (80.1%) | 125 (69.1%) |
| ≥50% | 112 (61.9%) | 105 (58.0%) |
| ≥75% | 79 (43.6%) | **90 (49.7%)** |

Note the crossover: GPS is worse at the ≥25% and ≥50% bands but **better at ≥75%**. Consistent with
the all-or-nothing pattern — participants either got usable GPS or got none.

**Valid hours on days when any data was collected** (n=174): accelerometer mean 11.8 h (SD 5.6,
median 12.9); GPS mean 15.2 h (SD 7.0, median 18.0). A stricter 16-valid-hour sensitivity threshold
was applied but its results are not given in the main text.

**A bibliographic note for anyone re-deriving these numbers:** Table 3's header states **N=1,276**
total potential collection days while the results text and every row total state **1,267** (=181×7,
and 786+293+188 = 731+142+394 = 1,267). The 1,276 is a **transposition typo in the published paper**.
Table 3 also renders GPS invalid days as "142 (11,21)" — a comma for a decimal point. Neither
affects any conclusion.

**Participant feedback survey (n≈174–179 of 181), medians on 1–100 scales:**

| Question | Median |
|---|---|
| App easy to use (1 = difficult, 100 = easy) | **85.0** |
| Likelihood of participating again (1 = very unlikely, 100 = very likely) | **85.0** |
| Was it a positive experience (1 = hated it, 100 = loved it) | **64.0** |

Most-selected complaints: the EMA prompt was **"annoying to answer every day"** and the **"questions
were worded poorly."** Reported app problems: **"App was too hard to download and install"** and
**"The interface was confusing."** Open-ended additions: repetitive questions, unclear wording, a
need for better notifications (sound/visual alerts), and lengthy completion times.

**The single most operationally pointed finding:** 19 of 181 participants (10.5%) **completed the
feedback survey but not the baseline survey** — people who stayed engaged enough with the study to
give feedback while contributing no data. Their reported issues were **technical difficulties during
app installation and registration, inability to reach study staff for support, and lack of
reminders.** That is a direct, named, fixable cause of a chunk of the missing 45%.

## Feasibility Findings

The authors' stated conclusion: "modest compliance with smartphone EMA surveys and good completeness
of passive sensing data is possible," adherence "remained stable over the 1-week period," and the
approach is "promising" for embedding in large epidemiological cohorts.

They compare themselves unfavourably and explicitly against benchmark literature: a 2021 systematic
review of 53 smartphone EMA well-being studies (median duration 7 days) reported **average
compliance of 71.6%**, against their ~55%. Their stated reasons for the gap: those studies used
**convenience samples**, **provided compensation**, and enrolled much younger participants (mean
30.8 vs 67.8 years). They also cite a meta-analysis finding a negative association between items per
prompt and EMA compliance, and concede their 21- and 63-item surveys were long by EMA standards.

**Their explicit recommendations:**

1. **Guarantee timely technical support at installation and registration**, not just "throughout."
2. **Add reminders and notification enhancements** (sound/visual triggers), simplify the app layout.
3. **Alternate truncated and full EMA versions** across days to mitigate fatigue, or space week-long
   bursts across a year rather than running one continuous block.
4. **Move from fixed-frequency to movement-triggered passive sampling** — "turning sensors on and
   off based on the participants' movement status ... rather than a fixed frequency" — to conserve
   battery while improving geolocation and activity data quality.
5. Note that passive completeness exceeded active compliance, "indicat[ing] that passive sensing
   data collection may impose a lower burden ... and can be extended longer."

## Relevance to Future Study Design

1. **An 8-day burst in a highly-engaged, uncompensated cohort yields ~55% EMA and ~60% passive.**
   That is the planning figure. It is *lower* than convenience-sample benchmarks, not higher, and
   the cohort's decades of survey compliance did not transfer to intensive daily measurement.
2. **Budget for 17.7% zero-response participants and size N accordingly.** Nearly one in five
   enrolled participants contributed no active data at all. A mean compliance figure conceals this
   entirely.
3. **The consent-to-first-data gap is a distinct, large, addressable loss.** 238 consented → 181
   transmitted (24% lost), with installation and registration named as the cause by the affected
   participants themselves. Instrument that step and staff it.
4. **Front-load anything essential.** 86.2% at baseline vs ~55% repeating, reproducing the 2024
   substudy's 82.7% vs 36%. Two independent Beiwe cohorts now show the same onboarding-moment
   effect.
5. **Survey length did not predict compliance here; survey repetition did.** A 63-item evening
   survey matched a 21-item afternoon survey (54.7% vs 55.6%). If you need more items, adding them
   to an existing prompt appears cheaper than adding a prompt.
6. **Expect no fatigue curve over one week — and do not read that as headroom.** Compliance was flat
   at ~55% from day 2. The loss was front-loaded into onboarding, not accumulated over time.
   Extending the burst would likely extend the plateau, not degrade it.
7. **GPS fails all-or-nothing; accelerometer degrades gracefully.** 31.1% GPS non-collection vs
   14.8% accelerometer, but GPS had *more* participants at ≥75% valid days. Plan GPS analyses around
   a smaller, cleaner subsample rather than a partially-complete full sample.
8. **Positive user sentiment does not predict compliance.** Median 85/100 on ease of use and 85/100
   on willingness to repeat, alongside 45% of prompts unanswered. Post-hoc acceptability scores are
   not an adherence forecast.
9. **Uninstall-at-end is unreliable.** Some participants left the app collecting for up to 150 days
   past the protocol window. Build server-side deactivation into the protocol, not participant
   action.

## Evidence Confidence

**Verified** for the recruitment funnel, all EMA compliance rates and banding, participant-day and
participant-level passive completeness, valid-hour means, data volumes, duty-cycle configuration,
feedback-survey medians, and the 32-participant zero-response and 19-participant
feedback-without-baseline counts — all read directly from the published open-access PDF including
Tables 1–4.

**Verified** for the paper's two internal inconsistencies (Table 3 header N=1,276 vs 1,267; "11,21"
for 11.21%), identified by arithmetic against the row totals during this pass.

**Corroborated** for the causal attribution of low EMA compliance to onboarding technical failure.
The authors label it a speculation ("we therefore speculate"), and the supporting evidence — the
19 feedback-without-baseline participants' self-reported reasons plus the absence of a fatigue
curve — is suggestive rather than dispositive. It is the most plausible explanation available, and
it is not established.

**Corroborated** for "passive imposes lower burden than active." True in this cohort (62.0%/57.7% vs
~55%) and consistent with the module's other studies, but the margin here is narrow, and the two
quantities are not measured on the same scale (valid *days* vs answered *prompts*).

**Pre-heartbeat.** Data collection ran 21 Jul – 21 Nov 2021, nearly three years before Beiwe's
server-side heartbeat/keepalive push was globally enabled on 2024-05-29. The passive completeness
figures here are a **pre-heartbeat lower bound**. The mechanism is directly relevant: the authors
name "the tendency of phone operating systems to disable sensor access when the phone is inactive
for extended periods, such as during sleep" as a specific cause of their shortfall — precisely the
problem heartbeat was built to address. See [`beiwe-als-adherence.md`](beiwe-als-adherence.md) and
Tier 14 Q106 in `../../shared/unresolved-questions.md`. That said, app deletion (the authors' stated
*primary* cause of non-collection) would be unaffected by heartbeat.

**COI.** Onnela, Beiwe's originator, is a co-author; the paper declares no conflicts of interest.
The exposure would be to claims flattering Beiwe, and the paper makes none — it reports ~55%
compliance, benchmarks itself explicitly *below* a 71.6% literature average, names the Beiwe app as
"too hard to download and install" in participants' own words, records a confusing interface, and
documents an OS update causing the app to malfunction. The interpretive claims run against
self-interest, which is the relevant test.

**Generalisability — severe, and stated by the authors.** All female, mean age 67.8, **98.3% White**,
all registered nurses with 30+ years of cohort engagement, all with smartphones and weekly Wi-Fi,
84.5% iOS. The authors concede this "may limit the generalizability of our findings regarding device
compliance," while arguing the results still inform other cohorts seeking to embed smartphone
collection. Two directions of bias pull opposite ways: the cohort's engagement history should
*inflate* compliance, while their age should *depress* it — and the observed ~55% presumably nets
both.

## Key Links

- Paper (open access): https://doi.org/10.2196/71375 · https://mhealth.jmir.org/2025/1/e71375
- Europe PMC: https://europepmc.org/article/PMC/PMC12407220
- Nurses' Health Study II: https://nurseshealthstudy.org/
- **Local PDF (already in the knowledge base, not duplicated):**
  `../../module-02-digital-phenotyping/literature/onnela-lab/2025-yi-jmirmhealthuhealth-measuring-psychological-well-being-behaviors-smartphone-based-digital.pdf`

## Related profiles

- Platform: [Beiwe](../../module-02-digital-phenotyping/profiles/beiwe.md)
- **Same first author, same design pattern, different cohort and 45× the scale:**
  [`beiwe-chronic-disease-substudy.md`](beiwe-chronic-disease-substudy.md) — read the two together;
  the 2024 paper supplies the long-horizon retention curve this one cannot, and this one supplies
  the participant feedback the 2024 paper explicitly regretted not collecting.
- Uncompensated, unsupported Beiwe baseline in clinical populations:
  [`beiwe-als-adherence.md`](beiwe-als-adherence.md)
- Incentive comparison: [`beiwe-spinal-cord-injury-incentives.md`](beiwe-spinal-cord-injury-incentives.md)
- BYOD selection effects: [`byod-demographic-imbalance.md`](byod-demographic-imbalance.md)
- Missingness with sociodemographic structure:
  [`beiwe-missing-data-sociodemographic.md`](beiwe-missing-data-sociodemographic.md)

## Sources

1. Yi L, Trudel-Fitzgerald C, et al. *JMIR mHealth uHealth* 2025;13:e71375. DOI 10.2196/71375. Full
   text and Tables 1–4 read from the published open-access PDF held locally at
   `module-02-digital-phenotyping/literature/onnela-lab/`, 2026-09-01, via `pdftotext` (both
   `-layout` and reflow modes, the latter needed to recover text broken across the two-column
   page boundary). Establishes every figure in this profile.
