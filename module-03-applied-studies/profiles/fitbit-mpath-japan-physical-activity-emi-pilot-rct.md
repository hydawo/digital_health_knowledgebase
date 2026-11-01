# Oba et al. 2025 - Provisioned Fitbit Sense plus m-Path EMA for a physical-activity EMI, Japanese inactive adults pilot RCT, N=40 over 4 weeks

## Quick Facts

| Field | Details |
|---|---|
| Citation | Oba T, Moriishi C, Takano K, Katahira K, Kimura K. "Mobile-Based Ecological Momentary Intervention for Improving Physical Activity in Adults Without Regular Physical Activity: Pilot Randomized Controlled Trial." *JMIR Formative Research* 2025;9:e79360. DOI [10.2196/79360](https://doi.org/10.2196/79360). PMC12677381. |
| Study design | Two-arm pilot RCT, 1:1 block randomisation, single-blind. EMI arm received tailored activity messages after each EMA. Control arm did the same EMA with no messages. |
| Sample size (enrolled / analyzed) | 232 assessed. 40 enrolled and randomised 1:1 (EMI arm n=20). 40 analysed. No dropouts. |
| Population | Adults aged 18 to 64 in and around Tsukuba City, Japan, not exercising regularly, in good health and on no medication. Mean age 45.40 (SD 10.50). Mostly employed and university-educated. |
| Duration | 4 weeks. Week 1 baseline. Weeks 2 to 4 intervention. Data collected November 2024 to March 2025. |
| Devices/platforms used | [Fitbit](../../module-01-wearables/profiles/fitbit-google.md) Sense or Sense 2 on the nondominant wrist, worn 24 hours a day. [m-Path](../../module-02-digital-phenotyping/profiles/m-path.md) for EMA and EMI. Both on a provisioned lab smartphone. |
| Funding/COI | JSPS KAKENHI 23H01051. No conflicts declared. No vendor funding or vendor-affiliated author. Compensation was JPY 15,000 to 20,000 (US $100 to 140). |
| Last verified | 2026-10-31 |

## Summary

This is a fully provisioned deployment. Each participant got a lab smartphone and a Fitbit Sense. The phone was preprogrammed in m-Path with the prompt schedule and messages for the participant's arm.

Retention and wear were near ceiling. All 40 randomised participants finished. Valid Fitbit heart-rate signal covered 90.3% (SD 10) of the study duration. EMA compliance was 79.5% (SD 23.5%) for the three daytime prompts and 87.2% (SD 18.81%) for the evening prompt.

The cost appeared in the skin. Fourteen of 40 participants reported a light skin rash, which the authors attribute to wearing the Fitbit. It is reported as no adverse event.

Acceptability was weak. Only 5 of 20 EMI-arm participants (25%) rated the fixed prompt times as appropriate.

## Instrumentation and Deployment Model

Provisioned. The paper states that "each participant received a smartphone and a Fitbit device at the beginning of the study." The Fitbit was linked to the phone through the Fitbit app. Participants could see their steps and heart rate at any time.

m-Path sent EMA prompts at 8 AM, 12 PM and 5 PM, each open until the next prompt. Each asked location, weather and social context. An evening prompt asked for self-reported daily steps and motivation. In the EMI arm, a message assembled from tagged phrases followed each completed EMA, from week 2.

Experimenters handed out the lab phones and so knew each participant's arm. Messages were delivered automatically. A researcher gave technical support as needed, for example with app login and online questionnaires.

Valid wear time was the count of minutes with a valid heart-rate value over 4 weeks. Activity intensity was minutes above 40% heart-rate reserve, using Fitbit's resting heart rate and the Tanaka equation. This heart-rate outcome was not preregistered.

The authors chose not to use passive phone sensing such as GPS or audio. They could not clear data-protection issues for it.

## Recruitment and Retention

| Stage | n |
|---|---|
| Assessed for eligibility | 232 |
| Enrolled and randomised | 40 |
| Completed the post-intervention assessment | 40 |

Recruitment used online adverts and emails to a local participant database. It was combined with recruitment for a sibling trial that needed pairs. People not eligible for, or unable to schedule, the paired trial were offered this one. Reasons for non-enrolment are in the CONSORT figure and were not extracted.

All participants were paid volunteers. The authors name payment as a likely reason for full retention.

## Data Completeness and Technical Issues

| Measure | Value |
|---|---|
| EMA compliance, daytime prompts, mean (SD) | 79.5% (23.5%), 66.78 valid responses out of 3 prompts x 28 days |
| Evening prompt compliance, mean (SD) | 87.2% (18.81%) |
| Valid Fitbit heart-rate signal, share of study duration, mean (SD) | 90.3% (10) |
| Skin rash attributed to the Fitbit | 14 of 40 |

Compliance did not correlate with any baseline characteristic. No device failure, sync problem or data loss is reported.

## Feasibility Findings

The authors call compliance excellent. They call the EMI's acceptability low. About half of EMI participants endorsed it as satisfactory (10 of 20), useful (9 of 20) or practical (10 of 20). For roughly one-third of prompts, participants said they would do a recommended activity.

They recommend better-timed and better-tailored messages, possibly by machine learning. They expect real-time passive sensing to remove the need for fixed prompt times.

## Relevance to Future Study Design

Fully provisioned phone plus Fitbit, in paid healthy adults, gave 90% heart-rate coverage and zero dropout over 4 weeks. That is close to a best case for this device.

Plan for skin reactions with 24-hour wrist wear. Fourteen of 40 reported a rash in 4 weeks.

Fixed prompt times are cheap to run and were judged poorly timed. Only a quarter of the EMI arm rated them appropriate.

## Evidence Confidence

Verified for the funnel, the compliance and wear figures, the rash count and the acceptability counts. These were read from the Europe PMC full-text XML (PMC12677381) on 2026-10-31.

Not assessed here. Whether Fitbit step and heart-rate outputs are accurate belongs with Module 1's [Fitbit profile](../../module-01-wearables/profiles/fitbit-google.md).

## Key Links

- Paper (OA): https://doi.org/10.2196/79360
- Europe PMC: https://europepmc.org/article/PMC/PMC12677381
- Local PDF: none held

## Related profiles

- Devices and platform: [Fitbit](../../module-01-wearables/profiles/fitbit-google.md), [m-Path](../../module-02-digital-phenotyping/profiles/m-path.md)
- Other provisioned Fitbit deployments: [`fitbit-ai-sleep-feedback-adolescent-soccer.md`](fitbit-ai-sleep-feedback-adolescent-soccer.md), [`fitbit-actigraph-proudme-summer-camp-adolescents.md`](fitbit-actigraph-proudme-summer-camp-adolescents.md)
- Fitbit plus a phenotyping platform: [`beiwe-fitbit-gynecologic-cancer-hope.md`](beiwe-fitbit-gynecologic-cancer-hope.md)

## Sources

1. Oba T, Moriishi C, Takano K, Katahira K, Kimura K. *JMIR Formative Research* 2025;9:e79360. DOI 10.2196/79360. PMC12677381. Full text read from Europe PMC XML, 2026-10-31. Establishes every figure in this profile.
