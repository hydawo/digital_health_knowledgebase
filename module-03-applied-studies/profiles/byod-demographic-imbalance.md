# Cho et al. 2022 — Demographic imbalances resulting from the BYOD study design, and the Demographic Improvement Guideline (CovIdentify case study)

## Quick Facts

| Field | Details |
|---|---|
| Citation | Cho PJ, Yi J, Ho E, Shandhi MMH, Dinh Y, Patil A, Martin L, Singh G, Bent B, Ginsburg G, Smuck M, Woods C, Shaw R, Dunn J. "Demographic Imbalances Resulting From the Bring-Your-Own-Device Study Design." *JMIR mHealth and uHealth* 2022;10(4):e29510. DOI [10.2196/29510](https://doi.org/10.2196/29510). PMC9034431. |
| Study design | **Viewpoint paper** — not a primary deployment study. Combines (a) a non-systematic review of demographics across 15 published BYOD studies, (b) a proposed guideline, and (c) a **retrospective implementation case study** in the authors' own CovIdentify cohort. See Evidence Confidence for why it is in Module 3 despite the format. |
| Sample size (enrolled / analyzed) | 15 BYOD studies reviewed; CovIdentify case study is the authors' own COVID-19 cohort (device counts below rather than a stated N) |
| Population | US adults. The paper's subject *is* the population composition problem. |
| Duration | CovIdentify enrolled from April 2020, 12 months of participant contribution; the guideline pilot ran June–October 2020 with results measured over 4 months |
| Devices/platforms used | Participant-owned **Fitbit, Garmin, Apple Watch** — BYOD, later hybrid. See [Fitbit/Google](../../module-01-wearables/profiles/fitbit-google.md), [Garmin](../../module-01-wearables/profiles/garmin.md), [Apple Watch/HealthKit](../../module-01-wearables/profiles/apple-watch-healthkit.md) |
| Funding/COI | Duke Bass Connections Fellowship; Duke-Margolis Center; MEDx; NCBiotech; Duke CTSI (NIH CTSA UL1TR002553). **Conflicts of interest: none declared.** Co-author Ginsburg was affiliated with the NIH All of Us Research Program, which is one of the studies critiqued. |
| Last verified | 2026-08-31 |

## Summary

The clearest statement in the literature that **BYOD is not a neutral cost-saving convenience — it
is a sampling decision that systematically excludes the people digital health most needs to reach.**
The recruitment pool for a BYOD study is, by construction, people who already own the device, and
that population is younger, healthier, wealthier and whiter than the population the resulting
technology will be deployed on.

Its most striking single finding is about **All of Us**, a program explicitly designed for
diversity: **more than 80% of participants in the overarching All of Us study are from historically
underrepresented groups, but 70% of participants in its Fitbit BYOD substudy identified as White
non-Hispanic — with only 4% Black and 3% Asian**, and over 90% non-Hispanic/non-Latino. The BYOD
design overwhelmed a deliberate, well-funded, national diversity mandate. If it can happen there, a
smaller study should assume it will happen to them.

The paper then does the thing most equity critiques do not: it proposes a concrete three-step
guideline, applies it to its own imbalanced study, and reports what changed.

## Instrumentation and Deployment Model

BYOD throughout: participants contributed data from wearables they already owned (Fitbit, Garmin,
Apple Watch) plus daily symptom reports via app, email, or text.

**The design migrated to hybrid under the guideline** — the research team began purchasing and
donating devices. The authors are careful to name the consequence: *"shifts in our study design,
such as donating commercial wearable devices to underrepresented groups, have resulted in a non-BYOD
(ie, hybrid) study."* Even then, **participants still had to own a smartphone** to pair the donated
wearable, so a BYOD floor remained.

## Recruitment and Retention

**Cross-study review (15 BYOD studies, PubMed + Web of Science, manual filtering — the authors
explicitly state this was not a systematic review):**

- **4 of 15 (27%) did not report any race or ethnicity demographics at all.**
- **0 of the remaining 11 (73%) achieved demographic proportions representative of the US
  population.** None. That is the paper's central empirical claim.

**All of Us Fitbit substudy (data 2008–2019):**

| | Overarching All of Us | Fitbit BYOD substudy |
|---|---|---|
| Historically underrepresented groups | **>80%** | — |
| White non-Hispanic | — | **70%** |
| Black | — | **4%** |
| Asian | — | **3%** |
| Non-Hispanic / non-Latino | — | **>90%** (6% Hispanic/Latino) |

**CovIdentify, before intervention:** the communities hardest hit by COVID-19 — Black/African
American and Hispanic/Latinx — had the *lowest* representation in a study whose entire purpose was
building a COVID-19 detection algorithm for resource-constrained settings.

**CovIdentify, after implementing the guideline (4 months):**

- **+250% representation of Black and African American participants**
- **+49% representation of Latinx and Hispanic participants**

## The Demographic Improvement Guideline

Three iterative steps, applicable at design time (though the authors applied them retrospectively):

1. **Identify** populations at risk of omission for whom the technology will ultimately be used, and
   decide whether BYOD is appropriate for the research question at all. A literature review of prior
   studies using similar devices and advertising strategies gives a baseline expectation.
2. **Modify** the study design using internal and external resources — institutional offices
   experienced in recruiting underrepresented groups; **choosing devices by prevalence in the target
   group rather than by sensor spec** (they note using smartphone sensors instead of consumer
   wearables as a legitimate option); community groups, NGOs, device donors, clinician referral, a
   community liaison, a community advisory board.
3. **Launch and monitor demographics in real time**, adjusting recruitment while the study is
   running, and restrategizing with community partners if the approach is not working. Continue
   engaging the population after study end to report findings back.

**What this actually cost in the case study — the most useful operational detail in the paper:**

- Applied to **nearly 30 funding opportunities**; won three (Duke Bass Connections, NC Biotech, Duke
  MEDx/CTSI), which funded **65 wearable devices**.
- Received a **donation of 300 additional devices** from a completed study.
- Attended **12 community events**, including food and medication distribution events, and
  distributed **250 free wearables** in a socially distanced manner.
- Recruited a **Latinx community liaison**, translated the study website into **four additional
  languages**, ran multilingual social-media advertising with diverse imagery, and presented to
  community groups — explaining the study's *current imbalance* as part of the pitch.
- Negotiated **reduced device pricing with wearable companies**, linked from the study's homepage.

That is the real price of a 250% shift: roughly 365 devices, three grants out of thirty
applications, a dedicated liaison, four translations, and twelve in-person events during a pandemic.

**When is a demographically imbalanced sample acceptable?** The authors set a deliberately high bar.
Only if **both** hold: (1) the disease as measured by the device does not differ across race,
ethnicity or age, **and** (2) the technology works the same for everyone. They then argue neither is
generally true, and that **the researcher is obligated to prove the null hypothesis** for both —
which they note "is often an even larger barrier than designing an equitably sampled study
population." Legitimately restricted populations (e.g. pregnancy studies) should be handled through
explicit inclusion/exclusion criteria, not through sampling drift.

## Data Completeness and Technical Issues

Not a completeness paper, but it documents a **hardware-level measurement bias** that matters for
every wearable study in Module 1:

- A 2020 *NEJM* study of ~50,000 paired measurements (>8,000 White and >1,000 Black patients) found
  **occult hypoxia was detected by pulse oximetry three times less often in Black patients**.
- The authors extend the concern: **the wrist-worn optical (PPG) sensors in Apple Watch, Fitbit and
  Garmin are of the same family**, and manufacturers do not systematically publish the demographic
  composition of their validation populations. Optical SpO2 sensing may also fail in people with
  more melanin and, separately, in people with sickle cell trait.
- Consequence: **models trained on demographically skewed wearable data may fail to generalise, and
  the sensor itself may be a source of the skew** — two compounding problems.

They also note that **device ownership itself varies**: use is lower among adults over 50 than
18–34, and young, healthy, more educated individuals are likelier to own wearables.

## Feasibility Findings

The guideline **worked** in the direction intended, substantially and within four months, but
required converting the study from BYOD to hybrid and mounting a funded, staffed community
engagement operation. The honest reading is that **BYOD's cost advantage is partly an accounting
illusion**: the money not spent on devices reappears as recruitment, engagement, and — if
unaddressed — as biased models.

The authors' own stated recommendations beyond the guideline:

- **Publication venues and funding agencies should require detailed demographic reporting of BYOD
  studies** — 27% of the reviewed studies reported none at all.
- **Funders should create funding opportunities specifically for equitable digital health study
  design**, including device purchase; they name the lack of such funding as a key barrier.
- Consider a **randomized withdrawal design** to reduce follow-up costs — while explicitly warning
  that it **may itself skew demographics** (a useful tension with
  [Beukenhorst et al.'s](beiwe-als-adherence.md) endorsement of run-in-and-withdrawal designs).
- Consider participant compensation amount **and timing**, plus wear tracking, at design time.

## Relevance to Future Study Design

1. **Treat "BYOD" as a stated limitation on generalisability from the outset, not a budget line.**
   0 of 11 reviewed studies that reported demographics achieved representativeness.
2. **A diversity mandate at the parent-study level does not survive a BYOD substudy.** The All of Us
   contrast (>80% underrepresented → 70% White non-Hispanic) is the single most quotable fact in
   this module for anyone proposing a BYOD design.
3. **Monitor recruitment demographics in real time**, like data completeness — both are correctable
   only while the study is running.
4. **Hybrid BYOD is the realistic compromise**, but budget it properly: ~365 devices, 3 of 30 grant
   applications, a liaison, translations, and 12 community events bought a 250%/49% shift here.
5. **Choose devices partly by ownership prevalence in the target population**, and consider
   smartphone-only designs where wearable ownership is the barrier — which is a direct argument for
   the Module 2 phenotyping platforms over Module 1 wearables in underserved populations.
6. **Interrogate sensor validation demographics**, especially for PPG and SpO2. Absence of published
   validation demographics is itself a finding to record — see
   [`../../module-01-wearables/validation-evidence.md`](../../module-01-wearables/validation-evidence.md).
7. **Report demographics even when they are bad.** A quarter of the reviewed literature is unusable
   for this question because it reported nothing.

## Evidence Confidence

**Verified** for the review counts (15 studies, 4 reporting nothing, 0 of 11 representative), the
All of Us substudy percentages, the CovIdentify intervention inputs (device counts, grants, events,
translations), and the +250% / +49% outcomes — all directly stated in the paper.

**Reported, not Verified, for the causal efficacy of the guideline.** This is the key caveat. The
CovIdentify implementation was **retrospective, uncontrolled, single-site, and concurrent with a
rapidly evolving pandemic**. There is no comparison arm, and the percentage increases are relative
to a very low base (4% Black participants in a comparable BYOD study means small absolute changes
produce large percentage swings). The authors state the limitation themselves and describe the
guideline as "one unique potential solution of the many possible solutions."

**Format caveat — recorded deliberately.** This is a **Viewpoint**, a category Module 3 generally
excludes in favour of primary deployments (see
[`../_inventory-and-scope-decisions.md`](../_inventory-and-scope-decisions.md)). It is included
because it is the only source found that reports *cross-study* deployment demographics alongside a
tested operational intervention, and because its subject — who ends up in the dataset — is a
first-order deployment-reality question that no single-cohort paper can answer. Read the review
component as **non-systematic by the authors' own statement**; they explicitly acknowledge possibly
overlooking studies that did recruit representatively.

**One structural conflict worth naming:** co-author Ginsburg was affiliated with the All of Us
Research Program while the paper's most prominent critique is of an All of Us substudy. The paper
declares no conflicts. The direction of the critique runs against that affiliation, which
strengthens rather than weakens it.

## Key Links

- Paper (OA): https://doi.org/10.2196/29510 · https://mhealth.jmir.org/2022/4/e29510
- Europe PMC: https://europepmc.org/article/PMC/PMC9034431
- Local PDF: `../literature/2022-cho-jmirmhealth-byod-demographic-imbalances.pdf`
- Supplementary appendices (race/ethnicity breakdowns by study; device ownership by race/ethnicity;
  iPhone ownership by race/ethnicity) are DOCX files on the JMIR article page — **not retrieved this
  pass**, and they contain the per-study demographic table underlying Figure 1.

## Related profiles

- The largest BYOD deployment, critiqued here: [`allofus-fitbit-step-counts.md`](allofus-fitbit-step-counts.md)
- Equity counterpart in smartphone sensing:
  [`beiwe-missing-data-sociodemographic.md`](beiwe-missing-data-sociodemographic.md)
- Who survives to analysis in a long study:
  [`radar-mdd-longterm-engagement.md`](radar-mdd-longterm-engagement.md)
- Devices: [Fitbit/Google](../../module-01-wearables/profiles/fitbit-google.md),
  [Garmin](../../module-01-wearables/profiles/garmin.md),
  [Apple Watch/HealthKit](../../module-01-wearables/profiles/apple-watch-healthkit.md)

## Sources

1. Cho PJ, et al. *JMIR mHealth uHealth* 2022;10(4):e29510. DOI 10.2196/29510. Full text read from
   the published PDF (via Europe PMC, PMC9034431), 2026-08-31. Establishes every figure in this
   profile.
2. Referenced within (1) for the pulse-oximetry disparity: Sjoding MW, et al. *NEJM* 2020 —
   racial bias in pulse oximetry measurement. Not independently retrieved this pass; the figures
   quoted here are as reported by Cho et al.
