# Master et al. 2022 — All of Us BYOD Fitbit cohort linked to EHR, N=6,042, median 4 years, 5.9 million person-days

## Quick Facts

| Field | Details |
|---|---|
| Citation | Master H, Annis J, Huang S, Beckman JA, Ratsimbazafy F, Marginean K, Carroll R, Natarajan K, Harrell FE, Roden DM, Harris P, Brittain EL. "Association of step counts over time with the risk of chronic disease in the All of Us Research Program." *Nature Medicine* 2022;28:2301–2308. DOI [10.1038/s41591-022-02012-w](https://doi.org/10.1038/s41591-022-02012-w). PMC9671804. |
| Study design | Retrospective observational cohort; **phenome-wide association study** linking participant-owned Fitbit data to electronic health records; time-varying Cox models |
| Sample size (enrolled / analyzed) | **6,042 analyzed** out of 214,206 All of Us participants consenting to EHR sharing (**2.8%**), from 329,070 participants total at the time of analysis (**1.8%**) |
| Population | US adults ≥18. Median age **56.7** (IQR 41.5–67.6); median BMI 28.1 (24.3–32.9). **73% female, 84% White, 71% college-educated.** |
| Duration | **Median monitoring 4.0 years (IQR 2.2–5.6)** — by far the longest observation period in this module. **5.9 million person-days.** |
| Devices/platforms used | **[Fitbit](../../module-01-wearables/profiles/fitbit-google.md)**, entirely participant-owned (BYOD), linked to EHR through the All of Us Research Program |
| Funding/COI | NIH All of Us Research Program; academic (Vanderbilt, Columbia). No device-manufacturer authorship. |
| Last verified | 2026-08-31 |

## Summary

The largest and longest participant-owned-wearable research deployment identified, and the paper
that most clearly demonstrates what BYOD buys and what it costs.

**What it buys is remarkable:** a median of **four years** of continuous, real-world activity data
per participant — 5.9 million person-days — at essentially zero device cost to the study, linked to
clinical outcomes in the EHR. No provisioned-device study can approach this duration. The authors
also point out a subtle methodological benefit: because **activity data date back to when the
participant created their Fitbit account, much of it was collected before they consented to All of
Us**, so the **risk of an observer/Hawthorne effect is negligible** — a genuine advantage of
retrospective consumer data that purpose-built research collection cannot replicate.

**What it costs is the recurring Module 3 lesson, at its starkest.** Of 214,206 All of Us
participants who had consented to share EHR data, **6,042 (2.8%) had linkable Fitbit data meeting
the inclusion criteria.** And the resulting cohort is **73% female, 84% White, 71% college-educated**
— the very imbalance [Cho et al.](byod-demographic-imbalance.md) use this same substudy to
illustrate, against a parent program that is >80% from historically underrepresented groups.

## Instrumentation and Deployment Model

**Pure BYOD, retrospective linkage.** There was no deployment in the usual sense — no recruitment
into a monitoring protocol, no device provisioning, no instructions. Participants who already owned
Fitbits and were already enrolled in All of Us linked their existing accounts, and their historical
data came with them.

**Inclusion criteria for the analytical cohort:**

1. Consented to share EHR data.
2. Linked their own Fitbit device.
3. Had valid Fitbit data over **at least 6 months** of total monitoring.
4. Aged ≥18 at any time during monitoring.

**A "valid day" was defined as ≥10 hours of Fitbit wear and ≥100 steps** — the 10-hour threshold
being a standard drawn from the actigraphy literature as sufficient to estimate waking-day physical
activity.

## Recruitment and Retention

There is no retention curve here in the conventional sense; the equivalent question is **who makes
it into the analytical cohort**, and the funnel is severe:

| Stage | N | % of previous |
|---|---|---|
| All of Us participants at time of analysis | 329,070 | — |
| Consented to share EHR data | 214,206 | 65.1% |
| **Linked a Fitbit + ≥6 months valid data + age ≥18** | **6,042** | **2.8%** |

**Included vs excluded participants differed systematically** (all p<0.001 unless noted): the
included cohort had **less coronary artery disease (2.8% vs 7.1%)**, less cancer (23.7% vs 27.9%),
less smoking (32.0% vs 40.6% with >100 cigarettes), **more alcohol use (96.8% vs 85.4%)**, lower BMI
(28.1 vs 28.8), and far higher education — **only 5.9% had no college versus 32.2% of those
excluded.** Age did not differ (p=0.373).

That education gap is the sharpest single number: **the excluded group was more than five times as
likely to have no college education.** Fitbit ownership is the filter, and it is filtering on
socioeconomic status.

## Data Completeness and Technical Issues

**Data loss was strikingly low once inside the cohort** — the consequence of using data people were
already generating for their own reasons:

- **Only 0.02% of total days excluded for having fewer than 100 steps.**
- **Only 0.44% excluded for the <6-month monitoring requirement.**
- Median **7,731 steps/day (IQR 5,867–9,827)**.
- In the time-varying Cox models, **15.4–16.0% of person-months (4.7–4.9% of days) were excluded for
  having fewer than 15 valid days** in that month.

Compare this to the ~40% of potential observation days with data in
[Yi et al.'s](beiwe-chronic-disease-substudy.md) provisioned-protocol Beiwe substudy, or
[Kiang et al.'s](beiwe-missing-data-sociodemographic.md) 19–27% baseline non-collection. **Data that
people generate for themselves is far more complete than data collected for a study** — which is the
central operational argument for BYOD and the counterweight to its representativeness problem.

**Technical limitations the authors state:**

- **Could not account for differences between Fitbit models**, which are known to vary in step
  accuracy.
- **Could not account for seasonal variation** or the COVID-19 pandemic, because device data were not
  available at the time of analysis and **dates were shifted to protect participant privacy** — a
  privacy-protection measure that directly destroys the ability to do time-period analysis. This is a
  genuine and underappreciated tradeoff for any study using a de-identified national cohort.
- **No non-stepping activity** (swimming, cycling) — captured only via waveform or raw accelerometry,
  which Fitbit does not expose.

## Feasibility Findings

The authors' explicit feasibility claim: *"this study provides important new evidence that
integration of these data sources is feasible"* — commercial wearable data linked to individual EHRs
producing actionable clinical information. They frame this as the first study they could identify
associating wearable physical-activity data with EHR-defined health outcomes.

Their stated tradeoff on data quality is measured and worth quoting in substance: **some fidelity is
lost between research-grade and commercial devices, but commercial data are "highly generalizable to
a large portion of the public who own such devices."** Note the careful hedge — generalizable to
device owners, which is precisely the population the funnel above shows is not representative of the
public at large.

## Relevance to Future Study Design

1. **BYOD retrospective linkage yields observation periods no funded study can buy.** Median 4 years,
   5.9 million person-days, at zero device cost. For questions needing long horizons, this is the
   only realistic route.
2. **Expect ~3% linkage yield from an EHR-consented cohort.** 214,206 → 6,042. Size accordingly.
3. **Self-generated data is dramatically more complete than study-collected data** (0.02% day-level
   exclusions vs 40–60% in protocol-driven phenotyping studies). The participant's own motivation is
   doing work no protocol can.
4. **Retrospective consumer data eliminates the observer effect** — a methodological advantage
   specific to this design.
5. **The selection filter is education and health status, not age.** The excluded group was 5×
   likelier to lack college education and had 2.5× the coronary artery disease prevalence. Any
   analysis of a BYOD wearable cohort is conditioning on a healthier, wealthier sample.
6. **Date-shifting for privacy forecloses temporal analysis.** If seasonality or a specific period
   (e.g. a pandemic) matters to the research question, confirm the cohort's de-identification scheme
   before committing.
7. **Device-model heterogeneity is uncontrolled** in any multi-year BYOD design, since participants
   upgrade. Treat step counts as approximately comparable, not identical, over time.

## Evidence Confidence

**Verified** for the cohort funnel, demographics, included-versus-excluded comparisons, monitoring
duration, valid-day definition and data-exclusion percentages — primary reported results read from
the published PDF.

**Scope caveat — recorded deliberately.** This is fundamentally an **epidemiological** paper, not a
feasibility paper, and it was flagged as an ambiguous inclusion in
[`../_inventory-and-scope-decisions.md`](../_inventory-and-scope-decisions.md). It earns its Module 3
entry because the cohort-construction funnel, the valid-day definition, the completeness figures and
the included/excluded comparison are all first-order deployment-reality facts about the largest BYOD
wearable dataset in existence. **A reader wanting a feasibility-first treatment of BYOD should start
with [`byod-demographic-imbalance.md`](byod-demographic-imbalance.md)**, which uses this same cohort
as its central example.

**Generalisability — stated plainly by the authors:** the cohort was "relatively young, female, white
and college-educated, and only included participants who owned Fitbit devices." They further note
the cohort **walked more than US adults over 60 on average**, i.e. it is an unusually active sample,
and argue this makes their effect estimates conservative. They call explicitly for studies including
participants "historically under-represented in biomedical research."

**Causal caution the authors state:** observational design, with acknowledged potential for reverse
causation (a condition causing fewer steps rather than the reverse), mitigated by restricting to
incident conditions.

The clinical findings themselves (step thresholds ~8,000–9,000/day, hazard ratios by condition) are
outside Module 3's scope and are not reproduced here beyond what is needed for context.

## Key Links

- Paper (OA): https://doi.org/10.1038/s41591-022-02012-w
- Europe PMC: https://europepmc.org/article/PMC/PMC9671804
- All of Us Research Program: https://allofus.nih.gov/
- Local PDF: `../literature/2022-master-naturemedicine-allofus-fitbit-step-counts-chronic-disease.pdf`

## Related profiles

- Device: [Fitbit / Google](../../module-01-wearables/profiles/fitbit-google.md)
- The critique of this exact substudy's representativeness:
  [`byod-demographic-imbalance.md`](byod-demographic-imbalance.md)
- Other very large consumer-wearable deployments:
  [`fitbit-heart-study-afib.md`](fitbit-heart-study-afib.md),
  [`apple-heart-data-management-lessons.md`](apple-heart-data-management-lessons.md)
- Protocol-driven completeness for contrast:
  [`beiwe-chronic-disease-substudy.md`](beiwe-chronic-disease-substudy.md)

## Sources

1. Master H, et al. *Nature Medicine* 2022;28:2301–2308. DOI 10.1038/s41591-022-02012-w. Full text
   and tables read from the published PDF (via Europe PMC, PMC9671804), 2026-08-31. Establishes
   every figure in this profile.
