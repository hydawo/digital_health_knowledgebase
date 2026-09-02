# AWARE Framework build report — 2026-09-02

Pass over the ranked AWARE candidate list from the dedicated OpenAlex citation-graph run
(425 papers citing Ferreira, Kostakos & Dey 2015, W2078074240, since 2016).

**Result: 5 profiles built, 2 candidates rejected. AWARE goes from 3 profiles to 8 — the module's
second-best-served Module 2 platform after Beiwe (12).**

**Nothing was written from an abstract.** Every figure in every profile was read from full text
(Europe PMC `fullTextXML`, cross-checked against the publisher PDF for bylines). The one candidate
whose full text could not be obtained was rejected rather than written up.

---

## Platform verification — the headline result

The verification requirement was the point of this pass, and it produced a clean outcome:

**All five profiled studies genuinely deployed AWARE.** No candidate on the ranked list turned out
to be a background citation misattributed to AWARE. The Methods section of each names the AWARE
application or framework as the deployed sensing stack, not merely as a cited precedent.

**Two important qualifications, both recorded in the profiles:**

| Study | What was actually deployed |
|---|---|
| Aledavood 2024 (MoMo-Mood) | AWARE app **"modified and adapted"** by the authors, orchestrated by their own NIIMA/Niimpy platform. Not a stock build. |
| Bae 2023 | **"We developed our mobile data collection app based on the AWARE framework"** — an AWARE-*derived* custom app, not AWARE as distributed. |

Wu 2023, Balliu 2024 and Borelli 2025 describe installing and running the AWARE application itself.

The two rejected candidates are the ones where the platform question mattered, and neither is an
AWARE deployment — see Rejections below.

---

## Profiles built

| # | File | Study | N / duration | Why it qualified |
|---|---|---|---|---|
| 1 | [`aware-alcohol-liver-disease-craving.md`](profiles/aware-alcohol-liver-disease-craving.md) | **Wu et al. 2023**, *Hepatol Commun* | 163 screened → 24 enrolled → 12 completed; 30 days | Feasibility is a stated aim. Full screening funnel, itemised withdrawal reasons, OS-stratified passive yield, informative attrition. |
| 2 | [`aware-momo-mood-mood-disorders.md`](profiles/aware-momo-mood-mood-disorders.md) | **Aledavood et al. 2024** (MoMo-Mood), *JMIR Ment Health* | 164 → 151; up to 1 year | **Study adherence is research question 1.** Passive missingness stratified by psychiatric diagnosis; survival analysis; self-diagnosed support failure. |
| 3 | [`aware-stand-mood-prediction-adherence.md`](profiles/aware-stand-mood-prediction-adherence.md) | **Balliu et al. 2024** (STAND), *npj Digit Med* | 437 → 183; up to 40 weeks | Prediction paper, but carries a dedicated adherence Results section with formal tests, plus a 20× attrition contrast between care models. |
| 4 | [`aware-msavorus-passive-completeness-companion.md`](profiles/aware-msavorus-passive-completeness-companion.md) | **Borelli et al. 2025**, *JMIR Form Res* | 37 → 28; ≥19 weeks | **Same cohort as an existing profile** (see below). Supplies the passive-completeness figures that profile records as its biggest gap. |
| 5 | [`aware-binge-drinking-jitai-sensor-loss.md`](profiles/aware-binge-drinking-jitai-sensor-loss.md) | **Bae et al. 2023**, *JMIR Form Res* | 75; 14 weeks | **Thin — flagged as such in the profile.** Qualifies on one finding: a 35.4% person-day loss with a data-loss mechanism new to the module. |

PDFs downloaded to `literature/`:

```
2023-wu-hepatolcommun-aware-alcohol-craving-liver-disease.pdf
2024-aledavood-jmirmentalhealth-momo-mood-multimodal-digital-phenotyping.pdf
2024-balliu-npjdigitalmedicine-personalized-mood-prediction-smartphones.pdf
2025-borelli-jmirformres-multimodal-passive-sensing-college-depression.pdf
2023-bae-jmirformres-phone-sensors-explainable-ai-drinking.pdf
```

---

## Rejections

### `10.1145/3711043` — Zhang, Trujillo & Poellabauer 2025, *Proc. ACM HCI* (CSCW) — **rejected: full text unobtainable**

Ranked top priority, and on its abstract it is exactly Module 3's subject matter — data quality
across recruitment, device usability, data quantity, compliance, consistency, privacy concerns and
incentive mechanisms, from a college mental-wellness crowdsensing study running October 2022 –
August 2023.

**Not written, because the full text could not be retrieved.** Routes attempted and their outcomes:

| Route | Outcome |
|---|---|
| ACM DL PDF (`dl.acm.org/doi/pdf/10.1145/3711043`) — the OA/bronze URL OpenAlex and Unpaywall both give | Returns an HTML challenge page, not a PDF |
| ACM DL full-HTML view | HTTP 403 |
| arXiv (title, author, topic queries) | No preprint |
| Europe PMC / PMC | Not indexed — ACM venues are not in PMC |
| Semantic Scholar Graph API | Abstract and metadata only; reference list returns empty |
| MOSAIC Lab publications page (FIU, Poellabauer's group) | Lists the paper; **no PDF link** |

**Platform unverified.** Nothing retrievable states which sensing stack the study used, and
Poellabauer's group has historically fielded its own app rather than AWARE. **Do not assume this is
an AWARE deployment.** It remains the single highest-value unbuilt AWARE-adjacent candidate; it needs
either institutional ACM DL access or an author request. Bibliographic note: OpenAlex dates it
2025-05-02 in *PACM HCI*; the MOSAIC Lab page describes it as CSCW 2025, Bergen, October 2025 — the
journal-then-conference pattern normal for PACM HCI.

### `10.2196/51689` — Sahandi Far et al. 2025 (JTrack-EMA+), *JMIR* — **rejected: out of scope, and not an AWARE study**

Full text read (PMC11815298). It is a **platform development-and-usability paper** for JTrack-EMA+,
a Jülich-developed cross-platform EMA system. It has no deployment cohort in Module 3's sense.

**AWARE appears only as a related-work citation** — specifically as an example of a platform that
"[has] two distinct apps for each platform", alongside RADAR-base and SEMA3. This is precisely the
background-citation pattern that produced the earlier misattributions. It is not an AWARE deployment
and never was.

Note for Module 2: **JTrack-EMA+ does not appear to be profiled in Module 2**, and on this paper it
is a real, actively-developed EMA platform (Forschungszentrum Jülich; Dukart group). Flagging it as a
**Module 2 expansion candidate**, per the scope rule that unprofiled technologies are flagged rather
than absorbed. Not acted on — Module 2 is not mine to touch.

---

## Most decision-relevant operational finding, one per profile

1. **Wu 2023** — **The sensing app itself was the leading named cause of withdrawal: 5 of 12
   non-completers cited AWARE technical problems**, including one outright installation failure, against
   only 2 who lost interest. This is the module's most explicit attribution of dropout to the app rather
   than to "burden".
2. **Aledavood 2024** — **Passive-data missingness ranged from 1.2% (controls) to 20.4% (borderline
   personality disorder) inside one study, one platform, one configuration** — a 17× spread. Any
   platform-level completeness figure quoted for a mixed-diagnosis cohort is meaningless.
3. **Balliu 2024** — **Two-week attrition was 1.7% in the in-person clinical-care arm versus 33.5–37.3%
   in the online-support arms, with the *sicker* arm retaining better.** The mechanism the authors give
   is that clinical participants were told to reconcile missed assessments during their regular
   in-person sessions.
4. **Borelli 2025** — **Wearables beat the phone on completeness: 11% missing for provisioned Oura +
   Samsung against 16% for BYOD AWARE smartphone sensing**, over the same participants and months. And
   **wearable non-wear time ranked fourth of 1,000+ features for predicting depressive symptoms.**
5. **Bae 2023** — **35.4% of person-days (414 of 1,168) were unusable**, attributed by the authors to
   participants disabling GPS through the phone's settings menu after being told the sensors were
   configurable. A data-loss class the module has not previously catalogued.

---

## OS-stratified data extracted (Tier 15 Q111 / Q111b)

Three of the five report something OS-relevant. **They do not point the same way, and the reason is
that they measure three different things.** This strengthens the module's current
*stream-specific-before-platform-specific* framing and adds a third category to it.

| Study | Measure | Direction | Category |
|---|---|---|---|
| **Wu 2023** | Mean **number of passive sensor types delivered** per participant: **Android 8.4 vs iOS 4.7** | **Android > iOS** (≈1.8×) | *Breadth of streams available* |
| **Balliu 2024** | **SMS-derived features could not be computed on iOS at all** — available for **only 15 of 183 participants (8.2%)** | **Android-exclusive stream** | ***Structural OS gate*** — new category |
| **McClaine 2024** (existing profile) | Passive **data yield** | **iOS > Android** | *Within-stream yield* |
| **McInerney 2024** (existing, Beiwe) | **EMA delivery**: iPhone missed 70.0%/70.6% vs Android 21.3%/26.8%; **no OS effect on accelerometer or GPS** | **Android > iOS on active; null on passive** | *Active-stream delivery* |

**The new contribution is Balliu's structural gate.** Wu's breadth measure and McClaine's yield
measure can be reconciled in principle — iOS exposes fewer sensors, but the ones it exposes may
deliver more densely. Balliu's finding is different in kind: the SMS stream **does not exist on iOS
by platform policy**, so it is not a completeness problem with a mitigation. The planning response is
binary — accept an 8% subsample, or drop the feature. Any Module 3 or study-design guidance on OS
asymmetry should now distinguish three cases:

1. **Structural** — the stream is OS-exclusive. No mitigation. (Balliu; SMS/call logs generally.)
2. **Yield** — the stream exists on both but arrives at different densities. Mitigable by
   configuration. (Wu, McClaine, Niemeijer.)
3. **Delivery** — active prompts reach one OS worse than the other. Mitigable by support and reminder
   design. (McInerney.)

**Two of the five profiled studies report no OS data at all**, and both are cases where it would have
been valuable: Aledavood's 151-participant year-long deployment does not state its iOS/Android split,
and Bae's dual-platform 14-week deployment never stratifies. **Borelli's cohort is Android-only by
eligibility criterion**, so it contributes nothing to the question by construction — which is itself
worth noting, since it is a five-month three-device AWARE deployment that looks like it should.

**The mechanism behind the McInerney EMA asymmetry remains unidentified.** Nothing in this tranche
addresses it.

---

## Head-to-head platform comparison

**None found.** No candidate compared Beiwe, mindLAMP and RADAR-base, or any two of them. **The
module's gap here is unchanged.** The nearest thing in this tranche is Aledavood 2024's Limitations
section, which *benchmarks* MoMo-Mood's own adherence against three published figures from other
platforms (65.3% completeness in a 334-patient 12-week MDD study; 99% in a 29-patient 1-year bipolar
study; 84.8%/66.8% patient/control adherence over 9 months) — a literature comparison, not a
head-to-head deployment, and useful only as context.

---

## Bibliographic errors and conflicts caught

**1. Borelli 2025 and Nguyen 2025 are the same cohort — Verified.** This is the most consequential
finding of the pass. `aware-msavorus-loneliness-multidevice.md` (Nguyen et al. 2025, *JMIR Form Res*
9:e70528) and the new Borelli profile describe **one deployment**: same institution, same 37 enrolled,
same three-phase design, same relational-savoring intervention, same Oura + Samsung Gear Sport + AWARE
+ mSavorUs stack, mean age 19.93 vs 19.96. Borelli's Methods cites "Nguyen et al [unpublished data,
2024]" for the intervention design — that manuscript is the published Nguyen 2025 paper.

The new profile carries a prominent warning header saying so. **These are not two independent
observations and must not be counted as two studies in any tally, matrix row, or platform count.** I
have written it as an explicitly-labelled companion rather than declining to build it, because it
supplies exactly the passive-completeness figures the Nguyen profile names as its own biggest gap.
**Whether the `feasibility-matrix.md` gets one row or two for this cohort is your call to make** — I
have not touched the matrix.

**2. An unresolved conflict between those two papers on enrolment year.** Nguyen says late Jan – early
Feb **2021**; Borelli says Jan – Feb **2022**. Also 22 weeks vs ≥19 weeks, and N=29 vs N=28. The N and
demographic differences are consistent with one participant differing between analytic samples; **the
year is a genuine conflict and one paper is wrong.** It matters: a 2021 start puts the entire
monitoring period inside California's COVID-19 restrictions, which is how the existing Nguyen profile
reads it. Recorded in both places, resolved in neither, per the project's source-conflict rule.

**3. A typographical error in Bae 2023.** The retained non-drinking events are given as "489/756,
64.9%" while the retained total is 754 in the same sentence, and 122 + 143 + 489 = 754. Recorded in
the profile rather than silently corrected.

**4. The JMIR byline hazard reproduced, and in both orientations.** As warned:

- **Aledavood 2024** (PMC11890149): authors first, then a contrib-group containing **John Torous**
  (handling editor), then one containing Babak Najand, Tobias Kockler and Ulrich Ebner-Priemer
  (reviewers). Naive parsing appends non-authors.
- **Borelli 2025** (PMC12174877): authors first, then **Amaryllis Mavragani** (editor), then Salvador
  Ruiz-Correa (reviewer).
- **Bae 2023** (PMC10196900): **the editor and reviewer contrib-groups come FIRST**, before the author
  group. Naive first-group parsing would put **Amaryllis Mavragani** as first author and **Olga
  Perski** as second. This is the opposite ordering from the other two JMIR articles in the same
  tranche — **the ordering is not stable within the publisher**, so position cannot be relied on. Use
  the `contrib-type="author"` attribute where present, and verify against the PDF byline regardless.

All five bylines were verified against the publisher PDF via `pdftotext -layout`.

---

## Engagement with the README's headline findings

Explicit confirmations, sharpenings and one contradiction.

**Confirmed:**

- **#5 (provisioning/platform requirements cost retention)** — Borelli's Android-only eligibility is
  the module's second such requirement after RADAR-MDD. Unlike RADAR-MDD it operated at *screening*,
  so its cost is entirely invisible; nobody with an iPhone entered the funnel.
- **#7 (funnels destroy enrolment)** — Wu: 163 approached → 12 usable, a 14.7% enrolment rate driven
  by plain refusal (70.5% of decliners "not interested") rather than protocol complexity. Balliu:
  437 → 183, 58% lost, and the largest single cut is an *adherence* threshold, not a technical one.
- **#9 (missingness is signal)** — **two new instantiations, and this finding should be upgraded from
  one-study to replicated.** Borelli: wearable non-wear time ranked 4th of 1,000+ features for
  predicting depressive symptoms, on a *passive* stream in a *non-clinical* cohort — the first
  extension of Wang 2021's active-stream, clinical-cohort result. Wu: 90-day relapse was 57.1% among
  zero-EMA participants against 16.7% among completers, while *no baseline characteristic*
  distinguished them.
- **#10 (baseline severity does not predict attrition)** — Wu reproduces the null across the full
  battery: demographics, disease stage, MELD, AUDIT, insight, readiness to change, depression,
  anxiety, stress, resilience, social support, self-efficacy. All null.
- **#14 (the funnel starts before consent)** — Wu: 22 of 163 approached (13.5%) excluded for
  incompatible technology, before any consent conversation. Balliu: eligible participants who
  **refused to install AWARE were excluded from the study** — a sensing-consent gate whose size is
  never measured. Borelli: Android-only screening, size never measured.
- **#15 (definitions decide the answer)** — Borelli reports **98.9% completion on the weekly PHQ-9**
  while the same deployment's EMA adherence (from the companion paper) falls to 69%. Two active
  streams, one study, 30 points apart, differing only in frequency and supervision.
- **#22 (support raises completion, payment raises persistence)** — Balliu is now the strongest
  evidence for the first clause; Borelli for the negative half of the second (up to $660 per
  participant, 27% attrition anyway).

**Sharpened:**

- **#17 (OS asymmetry is stream-specific)** — **correct, and incomplete.** Balliu adds a third
  category the current framing does not cover: streams that are **OS-exclusive by platform policy**
  (SMS on iOS), where the response is not mitigation but accepting an 8% subsample or dropping the
  feature. Suggested restatement of #17: *stream-specific first, and within that, distinguish
  structural gates from yield differences from delivery differences.*
- **#11 (OS asymmetry has no settled direction)** — superseded by #17 already, but Wu adds a fourth
  data point (Android 8.4 vs iOS 4.7 sensor types) whose direction is opposite to McClaine's on the
  **same framework**. They are reconcilable only if breadth and yield are separated, which neither
  paper does. Do not cite AWARE as favouring either OS.
- **#18 (support intensity has a quantified cost)** — Balliu supplies the other end of the range that
  Calvert 2026 anchors. Calvert: 1.3 troubleshooting contacts per participant buys 0.92 median GPS
  quality. Balliu: incidental reconciliation during routine clinical visits buys **1.7% vs ~35%
  two-week attrition**. Aledavood: **zero contact after week 2 and four movie tickets buys 65.7% at
  week 8**, and the authors name that absence as the cause themselves.

**Contradicted:**

- **#2 (passive data outlasts active data)** — **Wu 2023 is a clean exception and should be added
  alongside de Angel 2023.** "All participants supplied AWARE data every day that they responded to
  EMAs." Passive and active did not decouple: 29.2% supplied zero EMAs, 12.5% supplied zero sensor
  data. In this deployment the passive stream did not survive independently of the participant's
  engagement with the survey. The cross-cutting-pattern entry currently reads "the direction never
  reverses" with one noted exception — that is now two, both AWARE-or-adjacent.

**New candidate cross-cutting pattern (three or more studies, so it meets the module's own bar):**

> **Research-infrastructure failure is a distinct and under-reported data-loss class.** Borelli names
> **server congestion**; Bae's design makes **Wi-Fi-gated store-and-forward upload** a socioeconomic
> variable in an ED-recruited cohort; Aledavood needed a **provisioned Wi-Fi router per participant**
> for the bed sensor. None of these is a device, OS or participant failure — they are the study team's
> own infrastructure, and they are the losses a self-hosted deployment owns entirely and a managed
> SaaS deployment does not. This is a live input to any Module 2 hosting-model decision.

---

## Honest assessment: does AWARE's deployment literature support more Module 3 entries?

**Partly. It is not exhausted, but the high-value seam is thinner than the 425-citation pool suggests,
and the remaining candidates are lower quality than these five.**

**What this pass consumed.** Five of the seven ranked candidates were built; one is unobtainable; one
was out of scope. The two "lower confidence" candidates behaved exactly as predicted — 51689 was a
platform paper citing AWARE in related work, and 39862 was a modelling paper that qualified only
narrowly. **The ranked list was well-calibrated**, which is itself useful information about the
citation-graph triage method.

**Why the remaining pool is weaker.** AWARE's citation profile differs structurally from Beiwe's or
RADAR-base's. Beiwe has an identifiable lab producing feasibility papers as a deliberate output;
RADAR-base has a consortium that publishes recruitment and retention as standalone papers. **AWARE is
a toolkit that hundreds of unrelated groups build one-off apps on**, and those groups publish
*findings*, not *deployments*. Two of the five built here (Balliu, Bae) are prediction papers that
qualified on a single section, and one (Borelli) is a companion analysis of a cohort already profiled.
Only two — Wu and Aledavood — are studies where operational reality is a primary output. That ratio
is the realistic yield.

**Three specific reasons to expect diminishing returns:**

1. **The derivative-build problem.** Two of five deployments were modified or AWARE-derived builds.
   The more of these accumulate, the less any figure generalises to "AWARE", and the more the module
   is really cataloguing *n* bespoke apps that share a lineage. At some point the platform-level
   aggregation stops meaning anything — a caveat worth carrying into the comparison matrix.
2. **Reporting norms in AWARE's typical venues.** The HCI/ubicomp venues where AWARE deployments most
   often appear (CSCW, IMWUT, UbiComp) are exactly where full text is hardest to obtain — the one
   candidate I could not read is the one from that literature. Any future AWARE pass will hit this
   wall repeatedly without institutional ACM DL access.
3. **Age.** AWARE's most-cited deployments cluster in 2016–2020, predating the Android background-
   execution restrictions and iOS changes that dominate current feasibility reality. Their
   completeness figures would need a dated-evidence label of the same kind the module already applies
   to pre-`heartbeat` Beiwe.

**What is worth doing next, in order:**

1. **Get `10.1145/3711043`.** It is the single highest-value unbuilt candidate and its abstract is
   pure Module 3. Institutional ACM DL access or an author request. **Verify its platform first** —
   there is no evidence it is AWARE.
2. **Re-run the citation-graph pass filtered to CSCW / IMWUT / UbiComp / CHI venues specifically**,
   accepting that retrieval will be the bottleneck. That is where AWARE deployment-reality papers
   live, and the Europe-PMC-shaped discovery route this module uses cannot see them. This is a
   **structural blind spot of the same family as the two already recorded in the README** — name-based
   search failing on ordinary-English platform names, and framework-shaped platforms publishing under
   other names. Add a third: **venue-shaped invisibility**, where the platform's home literature is
   outside the biomedical indexes entirely.
3. **Do not chase AWARE volume for its own sake.** Eight profiles is proportionate. The module's
   sharper gaps are now the Beiwe/mindLAMP/RADAR-base head-to-head (still zero), and the geographic
   concentration — all five studies here are US or Finnish, adding nothing to that.

**One caveat on the count.** AWARE now has **8 profiles, but 7 independent deployments**, because
Borelli and Nguyen share a cohort. Please do not let the headline number drift from the underlying
observations.
