# Culhane et al. 2026 - GENEActiv sleep and activity reports on a 21-bed psychiatric inpatient unit, 155 admissions to 68 wearers

## Quick Facts

| Field | Details |
|---|---|
| Citation | Culhane BW, Patterson RD, Rahimi-Eichi H, Yip AG, Huesman K, Kostick-Quenet K, Salvi J, Beauchamp P, Ressler KJ, Baker JT. "Clinical Implementation of Wearable-Derived Sleep and Activity Reporting for Inpatient Psychiatric Monitoring." *JMIR Formative Research* 2026;10:e88466. DOI [10.2196/88466](https://doi.org/10.2196/88466). PMID 42766331 / PMC13592238. Published 2026-09-21. |
| Study design | Single-site, two-phase clinical implementation reported against the iCHECK-DH checklist. Uptake counts in phase 1, report turnaround in phase 2, then semistructured interviews coded by two researchers. The IRB classed it as an implementation initiative, not human subject research. |
| Sample size (enrolled / analyzed) | Phase 1 (August to December 2023). 155 admitted, 88 offered a device, 68 accepted, 42 had at least one report delivered. Phase 2 (January to June 2024). Uptake not tracked. 34 reports delivered. Interviews with 8 psychiatrists (only 1 had used the reports) plus the unit medical and nursing directors. Multimedia Appendix 1 also lists 5 mental health staff, 4 nurses and 2 social workers interviewed. |
| Population | Adults aged 18 to 65 on a 21-bed locked unit in a 238-bed psychiatric hospital in Massachusetts (McLean Hospital). Mean length of stay 17 days (SD 23). Common diagnoses major depressive disorder, schizophrenia spectrum, bipolar disorder and borderline personality disorder. Unit population 36.5% female and 80% White (n=181). |
| Duration | 11 months in total (August 2023 to June 2024). Per patient, the device was worn for the inpatient stay or until a report was requested. GENEActiv recorded at 20 Hz for up to 30 days. |
| Devices/platforms used | [GENEActiv Original](../../module-01-wearables/profiles/axivity-geneactiv.md) wrist actigraph, researcher-provisioned from 30 devices in an existing lab inventory. Data pulled by physically collecting the device. DPSleep pipeline for sleep and activity. Medication administration data from the hospital EMR. MATLAB graphical report plus a Python natural-language summary. No phenotyping platform. |
| Funding/COI | Discretionary institutional funds from the McLean Institute for Technology in Psychiatry. No external grant. Baker reports consulting fees and equity from Tetricus Labs. The unit medical director (Yip) was the main clinical user, the project champion and an author. The nursing director (Huesman) is also an author. Patient compensation is not reported. |
| Last verified | 2026-10-22 |

## Summary

This is the module's only study in which wearable data were fed back to treating clinicians as part of routine inpatient care. The unit of success is clinical use of a report, not a research dataset.

Patients mostly said yes. Of 88 patients offered a device in phase 1, 68 accepted (77.3%). Nurses recorded 20 refusal reasons. Five of those were privacy or surveillance concerns.

The bottleneck sat upstream and downstream of the patient. Nurses offered a device to only 88 of 155 admissions (56.8%). Clinicians requested a report for 42 of 68 wearers (61.8%). In phase 2, 32 of the 34 reports went to one psychiatrist, the unit medical director who co-led the project. The third psychiatrist on the unit requested none.

Turnaround was the main technical complaint. Full automation cut report generation from about 5 days to under 24 hours. That still meant collecting each watch by hand before any data existed.

## Instrumentation and Deployment Model

Provisioned and offline. Nurses offered the waterproof GENEActiv at admission. Consent to wear it was verbal, as part of routine workflow. The device has no wireless upload, so a research assistant had to swap or collect the watch and download it before any report could be built.

The collection rule changed four times in eleven months (Table 2).

| Period | Device collection | Report delivery |
|---|---|---|
| Aug to Sep 2023 | RA collects within 24 h of a REDCap or QR-code request | Emailed within 48 h |
| Oct 2023 | Weekly Thursday collection of every device worn 3 or more days | RA presents at Tuesday rounds, 5 d after collection |
| Nov to Dec 2023 | Same weekly collection | RA briefs nurses before Tuesday rounds |
| Jan to Jun 2024 | RA collects within 24 h of an email request | Email or secure file transfer within 48 h, sometimes within 3 h |

Under the first request model "only six report requests were completed," mostly from the medical director (Multimedia Appendix 1). Nurses and social workers sent none.

Report text was handwritten by lab staff on Sundays in phase 1. It became semiautomated, then fully automated in phase 2. No large language models were used in report generation. One research assistant handled device turnover and data processing, and that person's time was the main ongoing cost. Devices cost about US $275 each.

## Recruitment and Retention

| Stage (phase 1 only) | n |
|---|---|
| Admitted to the unit | 155 |
| Offered a device by nursing staff | 88 (56.8%) |
| Accepted | 68 (77.3% of offered) |
| Refusal reasons recorded | 20 |
| Refused for privacy or surveillance concerns | 5 (25% of recorded reasons) |
| At least one report delivered to the psychiatrist | 42 (61.8% of wearers) |

The rest were "general unwillingness to participate without particular reason." Why 67 admissions were never offered a device is not quantified. The authors attribute it to variable nursing buy-in. Nurses who saw device distribution and tracking as burdensome, with two of three psychiatrists uninterested, offered devices less consistently.

Patients were not followed for wear or removal during the stay. The paper says patients "demonstrated willingness to wear devices for the duration of inpatient stay." It gives no count of patients who removed the device early. A few patients reported discomfort, especially with the device worn beside a personal watch and the mandatory hospital bracelet.

Phase 2 did not track uptake at all. Project resources were moved from driving uptake to fixing report generation.

## Data Completeness and Technical Issues

Wear time, valid days and sleep-detection failure rates are not reported. The share of wearers whose data produced a usable report is not reported either. The 42 of 68 figure measures clinician requests, not data quality.

Documented failure modes are operational.

- Latency. With an offline device and in-house software, average generation took about 5 days in phase 1. Automation reduced this to under 24 hours in phase 2, with some same-day delivery.
- Reliability and clarity. The medical director named "the timeliness and reliability of the report as the greatest barriers to clinical use." The authors cite "reliance on software in-development and nonnetworked data collection."
- Device loss. One patient took a device home at discharge and mailed it back. No devices were destroyed. Nurses "reliably retrieved devices before discharge."
- Interpretability. Staff called the project "the sleep study." Percentile and fragmentation language did not match how nurses talk about sleep. That gap persisted into rounds.
- Staff turnover. One of the three unit psychiatrists left before phase 2 and was covered by rotating clinicians, who requested two reports.

No adverse events were reported.

## Feasibility Findings

The authors conclude that wearable-derived sleep and activity reporting is "technically feasible in inpatient psychiatry." They base that on patient participation and on automated report generation by the end. They are explicit that clinical utility was concentrated in one early adopter, so it "may not yet reflect routine uptake among average end users."

Their recommendations (Table 3) are to put reports in the EMR before morning rounds, to show "last-night" sleep metrics first, to use devices with wireless near-real-time upload, and to make processing accurate enough to skip human checking. On the organisational side they recommend project champions at every staff level and dedicated project staff. Interviewed psychiatrists said they would spend about 15 to 30 seconds per patient on a report.

## Relevance to Future Study Design

An offline research actigraph is a poor fit when the consumer of the data is a clinician who acts on last night's sleep. GENEActiv was chosen for raw 20 Hz data and a 30-day battery. The same property forced a physical collection step that set the floor on report latency.

On an inpatient unit, patient willingness is not the binding constraint. Here 77% of those offered accepted. Only 57% of admissions were ever offered, and that step depended on nursing buy-in. A future team should count and staff the offer step, not just the consent step.

Report use concentrated almost entirely in one co-author. A future team should expect clinical uptake of this kind to depend on a named champion. It should measure use by clinicians who are not on the project before calling the workflow adopted.

No wear-time or data-completeness figure exists for this deployment. A team planning an inpatient actigraphy study cannot use this paper to size expected valid nights.

## Evidence Confidence

Verified. The phase 1 funnel (155, 88, 68, 42), the refusal breakdown, the phase 2 report count and requester split, the turnaround change, the device specification and cost, the four collection models, the device-loss incident, the funding and the conflict statement were all read from the full text (Europe PMC JATS XML of PMC13592238, CC BY 4.0) and Multimedia Appendix 1, on 2026-10-22. The publisher PDF could not be retrieved without a browser check, so the byline was taken from the JATS author list and checked against the Authors' Contributions statement. Ivan Steenstra appears in the JATS contributor list but is not an author.

Reported. The claims that patients wore devices for their whole stay and that nurses reliably retrieved devices are narrative statements without counts.

Unclear. Whether the 20 recorded refusal reasons cover every refusal. Interview evidence on barriers comes mainly from the medical and nursing directors, both authors, which the authors flag as a bias.

Not assessed here. DPSleep's accuracy belongs with Module 1's [GENEActiv profile](../../module-01-wearables/profiles/axivity-geneactiv.md).

## Key Links

- Paper (OA, CC BY 4.0): https://doi.org/10.2196/88466
- Europe PMC: https://europepmc.org/article/PMC/PMC13592238
- Local PDF: not stored. The PMC and Europe PMC PDF endpoints returned a browser check on 2026-10-22. Full text read from the Europe PMC JATS XML.
- DPSleep pipeline paper: https://doi.org/10.2196/29849

## Related profiles

- Device: [Axivity and GENEActiv](../../module-01-wearables/profiles/axivity-geneactiv.md)
- Same lab, same device and DPSleep pipeline in a research cohort: [`geneactiv-beiwe-college-year-deep-phenotyping.md`](geneactiv-beiwe-college-year-deep-phenotyping.md)
- Other inpatient psychiatric deployment: [`beiwe-inpatient-suicide-pilot.md`](beiwe-inpatient-suicide-pilot.md)
- Clinician gatekeeping as the binding constraint: [`beiwe-fitbit-gynecologic-cancer-hope.md`](beiwe-fitbit-gynecologic-cancer-hope.md)
- Device chosen against patient preference in psychosis: [`sleepsight-schizophrenia-rest-activity.md`](sleepsight-schizophrenia-rest-activity.md)

## Sources

1. Culhane BW, Patterson RD, Rahimi-Eichi H, Yip AG, Huesman K, Kostick-Quenet K, Salvi J, Beauchamp P, Ressler KJ, Baker JT. *JMIR Formative Research* 2026;10:e88466. DOI 10.2196/88466. Full text, Tables 1 to 3 and the Methods read from the Europe PMC JATS XML, 2026-10-22. Establishes every figure in this profile.
2. Same paper, Multimedia Appendix 1, "Narrative descriptions of phase I and phase II," read from the Europe PMC supplementary files, 2026-10-22. Establishes the six completed requests under the first request model and the interview roster.
