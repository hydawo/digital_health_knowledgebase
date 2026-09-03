# Shiba et al. 2023 - Oura Ring Gen 2 adherence in South Florida healthcare workers, TemPredict substudy, N=91

## Quick Facts

| Field | Details |
|---|---|
| Citation | Shiba SK, Temple CA, Krasnoff J, Dilchert S, Smarr BL, Robishaw J, Mason AE. "Assessing Adherence to Multi-Modal Oura Ring Wearables From COVID-19 Detection Among Healthcare Workers." *Cureus* 2023;15(9):e45362. DOI [10.7759/cureus.45362](https://doi.org/10.7759/cureus.45362). PMID 37849583 / PMC10578453. Published 2023-09-16. |
| Study design | Observational substudy of the UCSF TemPredict Study. Adherence is the primary outcome, not a footnote. Descriptive statistics, t-tests and Welch's ANOVA. The authors call it mixed methods, but no qualitative component is reported. |
| Sample size (enrolled / analyzed) | 100 enrolled. 91 in the per-protocol wearable analysis after 8 withdrew and 1 lost the ring. Survey data could not be retrieved for a further 8, so survey adherence rests on 83. |
| Population | Florida Atlantic University affiliated clinicians and trainees at multiple South Florida clinical sites during the early pandemic. 35 healthcare professionals, 39 residents, 17 medical students. 59% female, mean age 36 (SD 13). |
| Duration | Minimum eight weeks per participant, in two enrolment phases. Phase I had 39 participants (hospital-based staff and residents only). Phase II had 71, of whom 19 continued from Phase I, and added medical students. |
| Devices/platforms used | [Oura Ring Gen 2](../../module-01-wearables/profiles/oura.md), provisioned and sized in person. Data flowed through the standard consumer Oura app to Oura's cloud. Study staff read it through an Oura Teams account. The daily symptom survey was a Qualtrics link opened from inside the Oura app. Data were then transferred to REDCap at FAU. No phenotyping platform. |
| Funding/COI | US Department of Defense (MTEC and USAMRDC), AFOSR via MIT Lincoln Laboratory, the #StartSmall foundation, Florida Blue Foundation, and Oura Health Oy. Oura provided a portion of the rings. Two authors (Mason, Smarr) hold Oura patents and have received Oura consulting fees, and Smarr holds Oura stock. Both state they were not being paid by Oura at the time of data collection. Participant compensation is not reported. |
| Last verified | 2026-09-03 |

## Summary

This is the only study in the module where adherence to a consumer ring is the stated primary outcome. The population is also unusual for a wearable study. These were clinicians and trainees working hospital shifts in the first year of COVID-19, a group the authors describe as working long, irregular schedules with procedures incompatible with wearing a device.

The headline is a gap between two streams in the same people over the same nights. Participants recorded ring sleep on 87.8% of study nights (SD 11.6) and submitted the daily symptom survey on 63.8% of days (SD 27.4). The difference held in every subgroup the authors cut, including both sexes and all three occupational groups. Cohen's d for the overall comparison was 1.16.

The second finding is that the survey stream, not the ring, is where the population differences appeared. Residents wore the ring on 82.8% of nights against 92.4% for attending-level professionals. Their survey adherence was 49.8% against 71.9%. The ring gap was ten points. The survey gap was 22 points. Medical students were as adherent as the professionals on both streams.

The third is a phase effect the authors cannot fully explain. Survey adherence rose from 43.1% in Phase I to 74.7% in Phase II (d=1.35) while ring adherence barely moved (85.9% to 89.7%, not significant). The authors offer two candidate explanations, pandemic concern increasing over time and the changed occupational mix, and do not choose between them.

## Instrumentation and Deployment Model

Provisioned. Consented participants met study staff in person to be fitted for ring size and trained on the app. Everything before that point was remote to limit COVID exposure. Participants were told to wear the ring every night while sleeping and were encouraged to wear it around the clock. Staff monitored adherence continuously through the Oura Teams cloud view and "sent frequent reminders about the protocol" for the whole study. The reminder cadence and channel are not reported.

The ring's own firmware shaped the adherence measure. At the time of the study the Oura Ring Gen 2 only recorded a sleep episode if it detected at least four hours of consecutive sleep. A night worn but with under four hours of sleep counts as non-adherent under the study's definition. The paper does not quantify how often that happened. For a cohort that includes residents on overnight call it is a plausible contributor to the resident gap, but the paper does not test it.

Survey delivery ran through a second vendor stack. The Qualtrics survey was reached through the Oura app, hosted by UCSF, and transferred to FAU by an encrypted process into REDCap. Survey data for eight participants "could not be retrieved." The paper does not say where in that chain the loss occurred.

### The parent study

The 100 participants here are a subset of the TemPredict Study, whose algorithm paper (Mason et al. 2022, *Scientific Reports* 12:3463, DOI [10.1038/s41598-022-07314-0](https://doi.org/10.1038/s41598-022-07314-0), PMC8891385) supplies the deployment model at scale. That paper is an algorithm paper and reports no adherence or wear time, so it is folded in here rather than profiled separately.

The parent cohort had two arms. Existing Oura owners were invited inside the Oura app and 73,399 responded, of whom 62,139 met all inclusion criteria. Healthcare workers at 20 US sites, Florida Atlantic University among them, were enrolled separately and provided with rings. That arm reached 3,180 against a target of 3,400. Sites were mailed flyers and plastic sizing kits so staff could find their ring size before a ring was shipped.

Of the 65,319 in the initial pool, 242 withdrew and 1,924 "did not engage sufficiently with study activities to be included in analyses," meaning they completed the baseline survey but no daily or monthly follow-up survey. That left 63,153. Nobody was compensated in either arm.

The parent study's completeness filter is severe and is the only completeness figure it reports. Of 704 participants who self-reported possible COVID-19, 306 had a reliable laboratory-confirmed diagnosis. Of those 306, 73 met the data thresholds for algorithm training, which required Oura data on at least 20 usable baseline days, at least 7 days before diagnosis and 14 after, with complete heart rate, respiratory rate and temperature. Non-wear was inferred rather than measured, by treating minutes with a MET value below 0.5 as non-wear and discarding both the MET and temperature readings for those minutes. Elevated temperature readings saved while a ring was charging were a named artefact.

Oura's role in the parent study was larger than in this substudy. The company "provided 1400 pieces of hardware and financial support in the form of a sponsored research contract," and its data-use policy does not permit the authors to share the data with third parties without approval.

## Recruitment and Retention

Recruitment was "by multiple modalities" across FAU-affiliated sites. The number approached and the number screened are not reported. Eligibility required English, adult age, a smartphone, and willingness to co-enrol in the parent TemPredict study.

| Stage | n |
|---|---|
| Enrolled | 100 |
| Withdrew consent or participation | 8 |
| Lost the provided ring | 1 |
| Per-protocol wearable analysis | 91 |
| Survey data unretrievable | 8 |
| Survey adherence analysis | 83 |

Nine percent attrition is low for this module, and it happened over a minimum of eight weeks with no reported compensation. Reasons for the eight withdrawals and their timing are not reported.

## Data Completeness and Technical Issues

Adherence definitions are explicit and worth copying. Wearable adherence is the percentage of enrolled nights on which a sleep record exists. Survey adherence is the percentage of enrolled days on which a survey response was received. Neither uses minutes of wear, and daytime wear was never measured.

| Group | n (ring / survey) | Ring nights recorded | Survey days submitted |
|---|---|---|---|
| All | 91 / 83 | 87.8% (SD 11.6) | 63.8% (SD 27.4) |
| Phase I | 39 / 35 | 85.9% (SD 12.1) | 43.1% (SD 27.1) |
| Phase II | 71 / 67 | 89.7% (SD 10.5) | 74.7% (SD 21.3) |
| Healthcare professionals | 35 / 32 | 92.4% (SD 8.2) | 71.9% (SD 23.8) |
| Residents | 39 / 35 | 82.8% (SD 12.9) | 49.8% (SD 28.7) |
| Medical students | 17 / 16 | 89.6% (SD 9.9) | 78.1% (SD 13.4) |
| Female | 54 / 49 | 88.9% (SD 10.8) | 67.9% (SD 26.8) |
| Male | 37 / 34 | 86.0% (SD 12.5) | 57.9% (SD 27.1) |

Professionals versus residents differed on both streams (ring p<0.001, d=0.88; survey p<0.005, d=0.83). Residents versus students differed only on surveys (p<0.001, d=-1.14). Sex differences were not significant on either stream.

Technical failure modes are almost absent from the paper. One ring was lost. Eight survey datasets were unretrievable. There is no mention of sync failures, battery, charging, ring damage, or app problems, and no per-night wear-minute data. The Discussion notes that the three parent TemPredict papers all excluded participants for missing data "which could be due to adherence issues or, at the time, issues with ensuring data capture," which is as close as the paper comes to naming a capture problem.

No iOS versus Android breakdown is given.

## Feasibility Findings

The authors conclude that healthcare workers were highly adherent to a nightly ring protocol in a pandemic, that a daily survey was substantially less adherent, and that residents were the least adherent group on both measures. They attribute the ring result to emphasising the study's importance, an atmosphere of collaboration with participants, frequent feedback, and the device's ease of use. They attribute the lower survey rate to the time a survey takes. They attribute the resident result to stress and disrupted schedules during the surge in admissions. None of these attributions is tested in the data.

Their stated design implication is that wearables are "likely a more efficacious tool" than daily surveys for early infection detection in this workforce.

## Relevance to Future Study Design

A future team deploying a ring in a clinical workforce can take four things from this paper.

Nightly ring adherence near 88% is achievable in shift-working clinicians with in-person fitting, continuous cloud monitoring and frequent reminders, and without any reported payment. The support model is described only in outline, so the cost of replicating it is unknown.

The active stream is where occupational differences show up. If a study needs symptom surveys from residents, budget for roughly half of days rather than the three quarters attending staff will give.

State the sleep-detection threshold. A ring that discards nights under four hours of sleep will under-report adherence in exactly the population that sleeps least, and this paper cannot separate non-wear from short sleep.

The two-vendor survey chain lost data for 8 of 91 participants before analysis. That is a larger loss than the ring stream suffered, and it came from the research data pipeline rather than the device.

## Evidence Confidence

Verified. The enrolment and exclusion counts, the two adherence definitions, every percentage and SD in the table above, the test statistics and effect sizes, the two-phase structure, the four-hour sleep-detection rule, the reminder practice, and the funding and conflict statements were all read from the published PDF (Cureus, CC BY 4.0) on 2026-09-03.

Not assessed here. Whether Oura Gen 2 metrics predicted infection is the parent TemPredict study's question and belongs with Module 1's [Oura profile](../../module-01-wearables/profiles/oura.md).

Conflict note. Oura funded part of the work, supplied part of the hardware, and two senior authors have patents, consulting income and, in one case, equity tied to the company. The adherence figures are unflattering to the survey stream rather than to the ring, so the conflict runs in the direction of the paper's conclusion. The figures themselves are simple counts and are reported with SDs and test statistics.

## Key Links

- Paper (OA, CC BY 4.0): https://doi.org/10.7759/cureus.45362
- Europe PMC: https://europepmc.org/article/PMC/PMC10578453
- Local PDF: `../../module-01-wearables/literature/oura/2023-shiba-cureus-adherence-oura-covid-healthcare-workers.pdf` (already held by Module 1; not duplicated)

## Related profiles

- Device: [Oura](../../module-01-wearables/profiles/oura.md)
- Other Oura deployments in this module: [`oura-university-freshmen-sleep.md`](oura-university-freshmen-sleep.md), [`aware-msavorus-loneliness-multidevice.md`](aware-msavorus-loneliness-multidevice.md)
- Passive stream outlasting active stream: [`whoop-mental-health-survey-engagement.md`](whoop-mental-health-survey-engagement.md), [`beiwe-adolescent-feasibility.md`](beiwe-adolescent-feasibility.md)
- Occupational or clinical-role effects on adherence: [`aware-stand-mood-prediction-adherence.md`](aware-stand-mood-prediction-adherence.md)
- Research-pipeline data loss as its own class: [`aware-msavorus-passive-completeness-companion.md`](aware-msavorus-passive-completeness-companion.md)

## Sources

1. Shiba SK, Temple CA, Krasnoff J, Dilchert S, Smarr BL, Robishaw J, Mason AE. *Cureus* 2023;15(9):e45362. DOI 10.7759/cureus.45362. Full text, Table 1 and Figures 1 to 3 captions read from the published PDF, 2026-09-03. Establishes every figure in this profile.
