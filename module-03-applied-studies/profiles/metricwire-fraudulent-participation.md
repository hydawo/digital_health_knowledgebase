# Siebers et al. 2025 — Detecting and controlling fraudulent participation in two virtual trials (MetricWire), 10 enrolled + 37 blocked

## Quick Facts

| Field | Details |
|---|---|
| Citation | Siebers R, Magane KM, Slayton H, Karzhevsky S, Palfai TP, Abrantes AM, Quintiliani LM, Stein MD. "Lessons Learned Identifying and Controlling Fraudulent Participation in Online Randomized Trials." *Journal of Medical Internet Research* 2025;27:e77512. DOI [10.2196/77512](https://doi.org/10.2196/77512). PMID 41160082 / PMC12612639. |
| Study design | Descriptive "lessons learned" report on fraud detection and prevention across **two linked, fully virtual RCTs**, with a 6-month evaluation of the prevention measures introduced. |
| Sample size (enrolled / analyzed) | **10 fraudulent participants successfully enrolled** before detection (all disenrolled from the Pain trial). After new measures: **37 individuals identified as fraudulent at screening (9 PA trial, 28 Pain trial) and none enrolled** between Nov 2023 and Nov 2024. |
| Population | Adults living with HIV, recruited **virtually from US metropolitan areas** into two trials addressing chronic pain and physical inactivity. |
| Duration | ~6-month participation per person; fraud first uncovered October 2023, prevention evaluated through November 2024. |
| Devices/platforms used | **[MetricWire](../../module-02-digital-phenotyping/profiles/metricwire.md)** for EMA; the PA trial also mailed participants a **[Fitbit](../../module-01-wearables/profiles/fitbit-google.md)**. Compensation up to **US $480** per participant, paid in gift certificates on completion of each study activity. |
| Funding/COI | Academic — Boston University School of Public Health, BU Psychological and Brain Sciences, Brown/Alpert Medical School, Tufts. **No platform relationship stated.** |
| Last verified | 2026-09-01 |

## Summary

The only study in this module where the failure mode is **adversarial rather than accidental**, and the only one that documents a research platform's own telemetry being repurposed as a forensic tool.

The mechanism is worth stating precisely, because it is directly reusable: **MetricWire records the carrier country of the phone completing each survey.** When the team audited the activity logs of every participant who had completed or was actively engaged in EMA, they found **10 participants connecting through a VPN in a UTC+1 timezone — and all 10 had a phone carrier country of Nigeria**, against every other participant showing a US timezone and a US carrier country. That single metadata field converted a suspicion into a disenrolment decision.

The second half is a prevention result: a **manual screening checklist**, applied to every candidate regardless of suspicion, blocked **37 fraudulent individuals over 12 months with zero further fraudulent enrolments**.

For a module about deployment reality, this is a category of risk that none of the other 30-odd profiles addresses: **a remote, incentivised, siteless study is a target**, and the data integrity threat is not missingness but fabrication.

## Instrumentation and Deployment Model

**Fully virtual, siteless, BYOD, incentivised.** Digital advertising, internet-based prescreening, remote screening and enrolment, videoconferenced assessment and behavioural intervention. EMA through MetricWire on the participant's own phone; a Fitbit mailed to PA-trial participants. **Up to US $480 in gift certificates**, released per completed activity.

Every one of those design choices — the ones that make decentralised trials attractive for access and geographic diversity — is also part of the attack surface. The authors are explicit that virtual approaches "improve access to research for marginalized and underrepresented communities" *and* "open new avenues for fraudulent participation."

## Recruitment and the Fraud Funnel

**Detection (October 2023).** The team noticed anomalies at the **prescreen** stage:

- **Volume shift**: prescreen submissions jumped from **2–3 per day to 10–12 per day** — the first indicator.
- Submissions at unconventional hours (**3 AM – 5 AM**), or many within a short window.
- Respondents giving **two first names as a full name** (e.g. "John Mark").
- **Gmail addresses following a predictable pattern** (first name, last name, digit string).
- **ZIP codes and area codes that did not correspond to the same location.**
- Ages clustered **20–35**.
- A higher-than-expected share indicating **male sex**.
- Implausible self-reported physical activity (**hundreds of minutes per day**).
- Maximum interest ratings (5/5) for **both** studies.

**Confirmation.** Auditing MetricWire activity logs for everyone who had completed or was engaged in EMA surfaced the **VPN + Nigeria carrier-country** signature on exactly 10 participants. All 10 were disenrolled from the Pain trial.

**Prevention and its result.** The team built a **manual checklist of fraud-associated characteristics**, used at prescreen and phone screen. Critically, **all potentially eligible candidates were phone-screened regardless of whether their prescreen looked suspicious** — the checklist was a scoring aid, not a triage gate. Between **November 2023 and November 2024**, PIs reviewing staff checklists and notes deemed **9 PA-trial and 28 Pain-trial candidates fraudulent** (37 total, separate from the original 10). **None were consented or enrolled.**

An important honesty note from the authors: those 37 were judged **"without MetricWire confirmation, which was unavailable as EMA was not performed during these screening stages."** The confirmatory telemetry only exists *after* enrolment — so the prevention layer necessarily rests on human judgement, with the false-positive risk that implies.

## Data Completeness and Technical Issues

Not a completeness study. The relevant data-integrity finding is the inverse: **10 participants generated apparently complete EMA data that was entirely fraudulent.** A study reporting adherence, retention or completeness without a fraud audit may be reporting figures partly manufactured by actors optimising for the incentive.

Two limitations of automated approaches, stated by the authors:

- **They did not originally capture time-on-form for the prescreen**, and judged that even if they had, the form was short enough that response-time analysis would have been of limited value.
- **IP-address checks have a "major drawback"** as a fraud signal — which is precisely why the platform's carrier-country field mattered: it is harder to spoof than an IP and was collected as a by-product of normal operation.

## Feasibility Findings

The authors' conclusion: for online clinical studies, **manual fraud-prevention methods used *alongside* automated ones** equip teams to detect evolving patterns of fraudulent enrolment. Neither layer alone was sufficient here — automation missed the initial breach, and manual review could not confirm it without the platform metadata.

## Relevance to Future Study Design

1. **Check what identity-adjacent metadata your EMA platform already records, before you need it.** Carrier country was decisive and was not collected for this purpose. Ask the same question of Beiwe, RADAR-base, mindLAMP, m-Path, Avicenna and AWARE deployments — most of which record device, network or timezone context.
2. **Instrument the prescreen for rate, not just for content.** A jump from 2–3 to 10–12 submissions/day was the earliest signal available and requires no new tooling.
3. **Treat high per-participant compensation as a risk multiplier.** US $480 paid incrementally on activity completion is a rational target. Incentives that improve retention (see [Kivelä et al.](avicenna-ema-suicidal-ideation-iatrogenic.md)'s feedback-report alternative and [Achterberg 2026](avicenna-adolescent-esm-school-phone-bans.md)'s €50 + lottery) also raise this exposure.
4. **Phone-screen everyone, and score with a checklist.** Selectively screening only suspicious candidates trains the adversary and is unfair to genuine participants who happen to look unusual.
5. **Budget for the false-positive cost.** 37 people were excluded on human judgement without confirmatory data. In a study recruiting from marginalised communities — the population decentralised design exists to reach — misclassification is a real harm, and this paper does not report an appeals process or a false-positive estimate.
6. **Report fraud audits in feasibility papers.** No other study in this module states whether one was conducted.

## Evidence Confidence

**Verified** — the two-trial design, MetricWire and Fitbit as instruments, the US $480 compensation, the 10 enrolled fraudulent participants, the VPN/UTC+1/Nigeria carrier-country signature, the prescreen volume shift from 2–3 to 10–12 per day, the full list of suspicious indicators, the checklist intervention, and the 9 + 28 = 37 blocked candidates with zero subsequent fraudulent enrolments over 12 months. Read from the full text (Europe PMC PMC12612639), 2026-09-01.

**Reported** — that all 37 later-blocked individuals were in fact fraudulent. The authors state plainly that this determination was made **without platform confirmation**, by PI review of staff checklists and notes. Their honesty about this is a strength of the paper; the classification remains unvalidated.

**Unclear** — the false-positive rate of the checklist; whether any genuine candidate was wrongly excluded; and whether the 10 confirmed fraudulent participants' EMA data was distinguishable from genuine data on any content-based measure. The paper does not report the last, which would have been the most generalisable finding of all.

**Scope note.** This is a methods/lessons-learned report rather than a full deployment study, and it reports no cohort-level retention or adherence figures. It is included under Module 3 because it documents an operational failure mode of real deployments, with counted outcomes, that no other profile covers.

**COI:** none identified. No stated relationship to MetricWire; the platform is described as an instrument, and its metadata is credited without endorsement.

## Key Links

- Paper (OA, CC BY): https://doi.org/10.2196/77512
- Europe PMC: https://europepmc.org/article/PMC/PMC12612639
- Platform: https://metricwire.com/
- Local PDF: `../literature/2025-siebers-jmir-fraudulent-participation-online-trials.pdf`

## Related profiles

- Platform: [MetricWire](../../module-02-digital-phenotyping/profiles/metricwire.md)
- Device: [Fitbit / Google](../../module-01-wearables/profiles/fitbit-google.md)
- Siteless recruitment at scale: [`fitbit-heart-study-afib.md`](fitbit-heart-study-afib.md), [`apple-heart-data-management-lessons.md`](apple-heart-data-management-lessons.md)
- Incentive design and its effects: [`avicenna-ema-suicidal-ideation-iatrogenic.md`](avicenna-ema-suicidal-ideation-iatrogenic.md), [`avicenna-adolescent-esm-school-phone-bans.md`](avicenna-adolescent-esm-school-phone-bans.md)

## Sources

1. Siebers R, et al. *J Med Internet Res* 2025;27:e77512. DOI 10.2196/77512. Full text read from Europe PMC (PMC12612639), 2026-09-01. Establishes every figure in this profile.
