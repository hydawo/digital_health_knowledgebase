# Zawada et al. 2025 - Beiwe after ischemic stroke and TIA, Mayo Clinic Arizona, 54 enrolled, the first Beiwe window mostly after the 2024 heartbeat change

## Quick Facts

| Field | Details |
|---|---|
| Citation | Zawada S, Acosta J, Collins C, Dumitrascu O, Harahsheh E, Hagen C, Ganjizadeh A, Mahmoudi E, Erickson B, Demaerschalk B. "Real-World Smartphone Data Predicts Mood After Ischemic Stroke and Transient Ischemic Attack Symptoms and May Constitute Digital Endpoints: A Proof-of-Concept Study." *Mayo Clinic Proceedings: Digital Health* 2025;3(3):100240. DOI [10.1016/j.mcpdig.2025.100240](https://doi.org/10.1016/j.mcpdig.2025.100240). PMID 40881107 / PMC12381640. Preprint on medRxiv 2025-01-25. |
| Study design | Prospective cohort, single centre, proof of concept. Weekly in-app PHQ-8, monthly staff-administered MADRS by video, passive phone sensing. Repeated-measures correlation and linear mixed models predicting MADRS. |
| Sample size (enrolled / analyzed) | 67 recruited. 54 enrolled. 44 downloaded the app. 38 completed the first MADRS. 35 completed the study. 1 excluded from the correlation analysis for Forest quality-check failure. 15 excluded from the prediction models for one or more missing measures, "primarily due to GPS measures." |
| Population | Adults admitted to Mayo Clinic Hospital in Arizona with ischemic stroke or TIA symptoms, plus people in sequelae monitoring after a previous IS or TIA. Prior dementia excluded. Of the 44 downloaders, 59.1% male, mean age 57, 88.6% White, 77.3% iOS. |
| Duration | 8 weeks of study data per participant, with the platform capturing up to 90 days to absorb MADRS scheduling delays. Recruitment 1 March to 31 August 2024. Monitoring 1 March to 15 November 2024. |
| Devices/platforms used | [Beiwe](../../module-02-digital-phenotyping/profiles/beiwe.md) on participant-owned iOS and Android phones, with Forest for processing (Oak for accelerometer, Jasmine for GPS). Accelerometer 10 s on, 10 s off. GPS 1 min on, 10 min off. Screen touch used for PHQ-8 completion time. No wearable. |
| Funding/COI | Mayo Clinic (no grant number), a P.E.O. Scholar Award, a Kosciuszko Foundation Graduate Award, a PhRMA Foundation predoctoral fellowship and NCATS TL1 5TL1TR002380-05 (Zawada). Funders had no role. The only competing-interest statement is that Erickson and Demaerschalk, as editorial board members, were kept out of peer review. All ten authors list Mayo Clinic affiliations. None is from the Beiwe team. Participant compensation not reported. |
| Last verified | 2026-10-22 |

## Summary

This is a small clinical Beiwe deployment from a team outside the Onnela Lab. Its value to the module is its calendar. Monitoring ran from 1 March to 15 November 2024. Beiwe's server-side heartbeat push was globally enabled on 2024-05-29. That date falls about three months into a window of about eight and a half months. Every other Beiwe profile in the module collected data before it.

The paper does not say whether the heartbeat was active. It does not name the Beiwe server version, the host or any keepalive feature. Its only push notification is the weekly survey prompt. Heartbeat status here is not stated.

The funnel is the clearest operational result. 54 enrolled and 35 finished (64.8%). Ten of the 54 never downloaded the app. Three of those ten cited a download issue and one cited data privacy.

Survey adherence held up. 73% of participants completed eight or more weeks of PHQ-8.

Passive completeness is reported only as a per-participant table in Supplemental Table 2. The paper never states its denominator, and the table's own description contradicts its column headers. GPS loss was large enough to drop 15 participants from the prediction models.

## Instrumentation and Deployment Model

Bring your own device. Owning a smartphone was an inclusion criterion. Patients were screened from the electronic health record and recruited by email after discharge. Consent and registration were fully remote. Participants downloaded Beiwe themselves at baseline.

The app collected accelerometer, GPS and screen touch data and delivered the PHQ-8. A notification carried the survey at baseline and once a week. The authors chose the sampling cycles from earlier studies with the app to limit battery drain. Accelerometer ran 10 seconds on and 10 seconds off. GPS ran 1 minute on and 10 minutes off.

Staff ran a MADRS by video every 30 days. The app was uninstalled at study completion. Supplemental Figure 1 lists "Beiwe app removal" at the 90-day assessment.

Processing used the Forest library. Accelerometer data went through Oak. GPS went through Jasmine, whose quality filter drops participants with suboptimal data. Who hosted the Beiwe server is not reported. The paper calls the platform HIPAA-compliant without naming the deployment.

## Recruitment and Retention

The CONSORT diagram gives each step with reasons.

| Step | n | Losses and stated reasons |
|---|---|---|
| Recruited | 67 | 13 declined consent. Prior smartphone app hack 1, language barrier 1, unknown 11 |
| Enrolled | 54 | 10 did not download. Download issue 3, data privacy 1, medical emergency or diagnosis 2, unknown 4 |
| Downloaded the app | 44 | 6 did not complete the first MADRS. Unresponsiveness 5, drop out 1 |
| Completed first MADRS | 38 | 3 dropped out. Chemotherapy 1, hospitalisation 1, smartphone issue 1 |
| Completed the study | 35 | TIA 9, IS 10, other transient stroke-like symptoms 10, IS or TIA before 2023 6 |

The paper's retention figure is 35 of 54 enrolled (64.8%). Lost to follow-up was defined as a phone that "stopped streaming data" or a participant who was "no longer responsive."

Supplemental Table 3 uses different denominators. It gives a total of 41, with 3 completing 30 days, 38 completing 60 days and 38 completing 90 days. The paper does not reconcile these with the 35 in the CONSORT diagram.

Two participants were seen at hospital for stroke symptoms during the study. Supplemental Appendix 2 says no one with major aphasia took part, and that decliners were not interviewed.

Compensation is not reported. Reminder or check-in contact beyond the weekly notification and the monthly MADRS is not reported.

## Data Completeness and Technical Issues

Survey completion first. "73% of participants" completed eight or more weeks of PHQ-8. The denominator is not stated. Supplemental Figure 3 is a histogram of weeks with a completed survey. Read from the plot, about 32 participants sit in the 7 to 8 week bin and about 7 in the 1 to 2 week bin. These are approximate readings of a figure, not tabulated values.

Passive completeness comes from Supplemental Table 2, headed "Data Missingness for Sensors by Participant." Its columns are "GPS completeness (Daily)" and "Accelerometer completeness (Daily)." The accompanying text describes a different quantity, "the sum of daily minutes the GPS was turned off" and "the minutes of missing data per day." The table does not say which of these it shows, over what period it is averaged, or against what denominator.

The table has 43 participant rows. The GPS column has 34 numeric values and 9 entries written variously as NA, na or N/A. The accelerometer column has 41 numeric values and 2 missing. Some GPS cells carry a percent sign and some do not.

| Stream | Numeric entries | Range in the table | Median of the table's numeric entries |
|---|---|---|---|
| GPS | 34 of 43 | 2.9 to 42.4 | 4.77 (computed here, not reported by the paper) |
| Accelerometer | 41 of 43 | 13.3% to 94.3% | 46.5% (computed here, not reported by the paper) |

The paper reports no summary statistic for either column. The medians above were computed for this profile from the printed values, treating unmarked GPS numbers as percentages.

The values sit oddly against the stated sampling. A 1-minute-on, 10-minutes-off GPS cycle allows data in at most 1 minute of every 11, about 9.1% of wall-clock minutes. Four GPS values exceed that (42.4, 17, 15.5 and 14.6). A 10-seconds-on, 10-seconds-off accelerometer cycle allows at most half of wall-clock time. Fourteen accelerometer values exceed 50%, one of them 94.3%. These ceilings are this profile's arithmetic from the stated configuration, not the paper's. They suggest the metric is not a simple share of wall-clock minutes, or that some participants ran a different configuration. The paper does not say which.

No iOS versus Android completeness split is given. The only OS figure is the cohort split, 34 iOS and 10 Android. The authors write that "As most participants had an iOS smartphone, data may be biased in ways unnoticed."

GPS was the main source of analytic loss. Fifteen participants were excluded from the prediction models for missing measures, primarily GPS. GPS measures were also "the primary source of missing measures in the week before a MADRS assessment." The authors suggest this may have excluded "patients with older smartphones and unreliable cellular data networks."

The supplement lists the authors' reasons for GPS missingness. These are phones turned off, location streaming disabled, uncharged phones, installing updates, and "apps conflicting with Beiwe data collection." It adds that sampling rates "may automatically decrease when phones are in a low battery state." None of these is quantified.

Other technical failure modes are the three download issues and one dropout for a smartphone issue. The Discussion names rural wireless and cellular access in Arizona and participant travel as further sources of variation. No server, upload or app-crash incidents are reported.

Heartbeat status is not stated. The calendar window runs 260 days, from 1 March to 15 November 2024. Of those, 171 days fall on or after 2024-05-29, about 66% of the window. Per-participant enrolment dates are not reported, so the share of participant-time after that date cannot be calculated from the paper.

## Feasibility Findings

The authors conclude that smartphone sensors "captured objective behavior measures in patients with IS/TIA" over a minimum of eight weeks. They present this as the first smartphone GPS and accelerometer study in an IS or TIA population.

They are cautious about the passive data. They warn that average measures "may be biased when proportions of collected data are low," pointing to Supplemental Table 2. They also say that participants "most likely did not carry their phones constantly."

Their design recommendation is to "explore how to design study protocols that reduce data missingness." They suggest testing whether other GPS sources, such as the Apple Watch, capture more complete data in this population.

## Relevance to Future Study Design

Expect to lose about a fifth of an emailed, post-discharge BYOD cohort before the app is installed. Here it was 10 of 54. Three of those were download problems that onboarding support might have caught.

A 1-in-11 GPS duty cycle left GPS as the stream that removed participants from analysis. A study whose endpoint depends on weekly mobility features should budget for that loss or raise the GPS cycle and accept the battery cost.

Report the completeness denominator. This paper's per-participant table cannot be compared with other Beiwe deployments because it does not say what a value of 4.77 or 46.5% is a share of. The comparison it was most needed for, post-heartbeat completeness, is the one it cannot support.

If the heartbeat question matters to a design decision, ask the team for the Beiwe server version and the per-participant enrolment dates.

Comparison with other Beiwe profiles is limited to figures both papers report on the same definition. The closest match is [`beiwe-transdiagnostic-outpatient-completeness.md`](beiwe-transdiagnostic-outpatient-completeness.md) (Pellegrini 2022), whose modelling approach this study adapted. Both report the share of participants completing a PHQ-8 in eight or more weeks. Pellegrini reports 78% in a paid, clinic-visit design during 2015 to 2018. Zawada reports 73% in a remote design with compensation not reported. Both used the same 10-seconds-on, 10-seconds-off accelerometer cycle. Pellegrini's passive completeness is defined against expected minutes, so it cannot be set against Supplemental Table 2. The two studies' retention figures use different denominators. Pellegrini's 38 of 45 counts people whose app staff installed at baseline. Zawada's 35 of 54 includes 10 who never installed it.

On cohort OS mix, which several Beiwe profiles report, this cohort was 77.3% iOS. That compares with 82.5% in [`beiwe-actigraph-modus-als-progression.md`](beiwe-actigraph-modus-als-progression.md), 84.5% in [`beiwe-nurses-health-study-burst.md`](beiwe-nurses-health-study-burst.md) and 96% in [`beiwe-adolescent-feasibility.md`](beiwe-adolescent-feasibility.md).

## Evidence Confidence

Verified. The recruitment window, monitoring window, CONSORT counts and reasons, the 64.8% completion figure, the 73% PHQ-8 figure, the sampling configuration, the OS split, the 15 model exclusions, the lost-to-follow-up definition, the stated causes of GPS missingness, and the funding and competing-interest statements were read from the Europe PMC full-text XML (PMC12381640, CC BY-NC-ND) and the supplementary file mmc1.docx on 2026-10-22. The CONSORT figure was read from the article's figure image.

Unclear. The passive completeness metric in Supplemental Table 2. The values are verified as printed. What they measure is not, because the table and its text describe different quantities and several values exceed the duty-cycle ceiling.

Not stated. Whether Beiwe's heartbeat was active. The window placement is verified. Heartbeat status cannot be read from the paper.

Reported. The Supplemental Figure 3 bin counts are approximate readings of a histogram.

Not assessed here. The MADRS prediction results and the PHQ-8 correlations are the paper's subject, not deployment findings.

Conflict note. All authors list Mayo Clinic affiliations. No industry conflict is declared.

## Key Links

- Paper (OA, CC BY-NC-ND): https://doi.org/10.1016/j.mcpdig.2025.100240
- Europe PMC: https://europepmc.org/article/PMC/PMC12381640
- Preprint: https://www.medrxiv.org/content/10.1101/2025.01.23.25320624v1
- Local PDF: not stored. Europe PMC, PMC and the publisher PDF endpoints all served a browser check on 2026-10-22. Profile written from the Europe PMC XML and supplementary files.

## Related profiles

- Platform: [Beiwe](../../module-02-digital-phenotyping/profiles/beiwe.md)
- Same weekly PHQ-8 and MADRS design, pre-heartbeat: [`beiwe-transdiagnostic-outpatient-completeness.md`](beiwe-transdiagnostic-outpatient-completeness.md)
- Heartbeat development timeline: [`beiwe-als-adherence.md`](beiwe-als-adherence.md)
- Beiwe missingness by OS and sociodemographics, pre-heartbeat: [`beiwe-missing-data-sociodemographic.md`](beiwe-missing-data-sociodemographic.md)
- Another clinic-recruited Beiwe cohort with a GPS completeness figure: [`beiwe-spine-disease-mobility.md`](beiwe-spine-disease-mobility.md)

## Sources

1. Zawada S, Acosta J, Collins C, et al. *Mayo Clin Proc Digit Health* 2025;3(3):100240. DOI 10.1016/j.mcpdig.2025.100240. Full text, Tables 1 to 4 and the CONSORT figure read from the Europe PMC JATS XML (PMC12381640), and Supplemental Figures 1 and 3, Supplemental Tables 1 to 5 and Supplemental Appendices 1 to 3 read from mmc1.docx, 2026-10-22. Establishes every figure in this profile except the two medians and the duty-cycle ceilings, which are computed here and labelled as such.
