# Carlson et al. 2026 — Garmin Vívofit 4 + automated SMS (ActiveKC) in low-income Kansas City communities, N=114 over 7 weeks

## Quick Facts

| Field | Details |
|---|---|
| Citation | Carlson JA, Materia F, Moon M, Ryu S, Yeager C, Steel C, Shields K, Gill HS, Berkley-Patton J, Catley D. "Automated Physical Activity Support for Adults and Youth From Low-Income Communities: Single-Arm Pilot Study." *JMIR mHealth and uHealth* 2026;14:e76991. DOI [10.2196/76991](https://doi.org/10.2196/76991). PMID 42247677 / PMC13282599. Published 2026-06-05. |
| Study design | **Single-arm pre-post pilot** of a beta-version mHealth intervention, with **pre-specified feasibility/acceptability benchmarks** and an exploratory step-count outcome. Reported per TREND. |
| Sample size (enrolled / analyzed) | **Adults: 132 assessed → 84 enrolled (64%) → 83 analysed. Youth: 49 assessed → 31 enrolled (63%) → 31 analysed.** Total analytic sample **114**. |
| Population | Adults and youth ≥8 years from **6 Kansas City, Missouri zip codes** with the city's highest CDC Social Vulnerability Index scores (0.67–0.95) and 44%–88% Black residents. Adults: **88% female, 84% Black or African American**, mean age 50 (range 19–88), 63% without a college degree. Youth: 77% female, 77% Black, mean age 13 (range 8–17); 84% had a participating parent. |
| Duration | 7-day run-in + **7-week intervention** (54–56 days total). Enrolment September 2021 – February 2022. |
| Devices/platforms used | **[Garmin](../../module-01-wearables/profiles/garmin.md) Vívofit 4** step tracker (provisioned), synced to the **Garmin Connect** app on the participant's own phone, with study access via the **Garmin API**. Automated 2-way SMS via Microsoft Azure Communication Services and a custom real-time management application. |
| Funding/COI | Jackson County, Missouri (contract O.5506). **"Garmin Inc provided some of the monitors for this study"** — an in-kind vendor contribution; the funders had no role in design, conduct, interpretation or publication. **Conflicts of interest: none declared.** IRB: Children's Mercy Hospital STUDY00001939. Compensation up to **US $95** for completing assessments. |
| Last verified | 2026-09-02 |

## Summary

The module's first **Garmin** deployment, and one of the very few in any population selected
explicitly for socioeconomic disadvantage. It is also the study that most directly contradicts one of
the module's headline findings.

**Finding #14 says the enrolment funnel starts before consent and is usually unreported, citing
[Cote 2019](beiwe-spine-disease-mobility.md)'s 42% of approached patients excluded for not owning a
smartphone.** This study, in six of Kansas City's most socially vulnerable zip codes, reports:

> **"No individuals who were screened for eligibility were ineligible because of lack of access to a
> smartphone."**

Zero, out of 181 screened, in a cohort that is 84% Black, 63% without a college degree, and drawn
from the highest-SVI neighbourhoods in the city. The authors read this as evidence of "the growing
ubiquity in smartphone use among low-income populations."

**An important qualification, from the paper's own methods — the two studies do not measure the same
thing.** This study's criterion was that **"either the participant or parent was required to have
*access* to a smartphone"**, and **"youth without a smartphone were connected to another device in the
household (eg, tablet or parent's smartphone)."** Access is therefore **household-level**, and the
design deliberately routed around individual non-ownership rather than encountering it. Cote 2019's
42% figure, by contrast, is **individual ownership** in a clinic population of adults with spine
disease. So this is not a clean refutation.

What it does establish, and it is still substantial: **a study can be designed so that individual
smartphone non-ownership stops being an exclusion criterion at all** — by accepting household devices
and enrolling parent–child dyads. The transferable lesson is about *protocol design*, not about
device ownership having ceased to matter. Treat the "barrier has disappeared" reading as
**Unclear**; treat "the barrier is designable-around in family and community settings" as
**Verified**.

The rest of the numbers meet most pre-set benchmarks: **enrolment 63–64%** (benchmark ≥60%),
**retention 77–93%** (≥80%), **message-delivery fidelity 99%** (≥80%), **wear adherence 79–82%**
(≥70%), **acceptability 83–100%** (≥80%). **Engagement was the exception** — replies to two-way
messages averaged **2.6 of 7** for adults and 3.2 of 7 for youth, against a ≥70% benchmark, and was
**highly patterned by demographics in the opposite direction to the study's target population**.

## Instrumentation and Deployment Model

**Provisioned wearable, BYOD phone.** Study staff set up the Garmin monitor, Garmin Connect app and
Garmin account, configured auto-sync, and demonstrated both. Youth without a personal phone were
connected to another household device (tablet or parent's phone), and **for 48% (15/31) of youth,
messages went to the parent's phone.**

**Data access was through the Garmin API**, which the team used operationally rather than only
analytically: **staff reviewed data reports weekly and contacted anyone with no data in the previous
4 days** by text and phone call. This is the same "Notify" pattern LINC formalises on mindLAMP
([Calvert 2026](mindlamp-linc-passive-data-quality.md)) — a vendor-API-driven data-flow monitor with
a defined staleness threshold — arrived at independently on a consumer wearable platform.

**A run-in period doubled as an eligibility screen**, and its two exclusion criteria are worth
noting: participants were excluded if they averaged **≥7500 steps/day (adults)** or **≥12,000
steps/day (youth)** during 7 days of run-in, *or* if they **wore the Garmin on fewer than 3 days of
the run-in**. The second criterion is a **prospective adherence screen** — a design choice this
module has otherwise seen only retrospectively, as a wear-time threshold applied at analysis (see
[Straczkiewicz 2024](actigraph-als-upper-limb-wear-time.md)).

**Intervention:** 7 weeks of automated, Garmin-data-personalised SMS, 4 days/week: a Sunday past-week
review, a Wednesday midweek check-in with an activity tip, a Friday distance-milestone message, and a
Monday **two-way** message on a rotating contextual topic (knowledge, values, problem solving,
planning, built environment, social support, maintenance) with a 48-hour reply window. Daily step
goals were set by Garmin's own adaptive algorithm; the weekly goal was uniform (meet the daily goal on
≥4 days).

## Recruitment and Retention

Recruitment was **in-person and community-embedded**: COVID-19 vaccination and health-screening events
hosted by neighbourhood, youth, business, faith-based and health organisations, plus well-child visits
in a hospital-based paediatric primary-care system serving mainly uninsured and underinsured families
from the same neighbourhoods. Enrolment happened on-site.

**Enrolment: 84/132 adults (64%), 31/49 youth (63%).** **19% (25/132) of adults were excluded for
already meeting the step guideline in run-in; no youth were.** The authors call the latter "alarming".

**Retention, by assessment:**

| | Adults | Youth |
|---|---|---|
| Step-tracker midpoint (weeks 3–4) | **95% (79/83)** | 94% (29/31) |
| Step-tracker endpoint (weeks 6–7) | 84% (70/83) | **77% (24/31)** |
| Survey endpoint | 93% (77/83) | 87% (27/31) |

**Enrolled participants were not a neutral sample of those screened**, and the paper reports this
explicitly: **enrolled adults were significantly more likely to hold a college degree (37% vs 15%)**
and non-significantly more likely to be female (88% vs 75%). Enrolled youth were significantly more
likely to be female (77% vs 33%) and Black (77% vs 53%). So even within a deliberately low-income,
majority-Black recruitment frame, **the education gradient reappeared at the enrolment step** — a
finer-grained version of the representativeness problem
[Cho 2022](byod-demographic-imbalance.md) documents at the cohort level.

## Data Completeness and Technical Issues

**Definition, stated precisely, and it is one of the stricter ones in the module.** Non-wear = any
15-minute period with maximum motion intensity of 0. **A valid day requires ≥8 hours of wear time AND
≥100 total steps.** A participant's estimate for an assessment period was set to missing if they had
**<3 valid days** in that period.

**Adherence: adults a mean of 46 valid wear days (SD 13) and youth 44 (SD 13) over the 54–56-day
window — 82% and 79% respectively.** For a 7-week provisioned-wearable deployment this is at the high
end of the module, comparable to [Lubitz 2022](fitbit-heart-study-afib.md)'s BYOD wear compliance and
well above most provisioned studies.

**Fidelity: 45 of 3955 messages (1.1%) failed to deliver**, "largely because of mobile phone numbers
being inactive for a period of time" — the most concrete quantification of *phone-service* instability
as a data-loss mechanism anywhere in this module, and one specific to lower-income cohorts.

**Technical support: 10 participants contacted, all for a lack of recent Garmin data. 9 of the 10 were
documented as Garmin-monitor-to-Garmin-app synchronisation failures**; the tenth was believed to have
stopped wearing the device. The Discussion is unusually candid about the residue:

> anecdotal evidence "we were unable to quantify suggested that some problems were recurring and that
> some participants needed to regularly engage with their Garmin app to ensure proper synchronizing."

And that the fix "could vary somewhat across smartphone software type and version, requiring staff to
develop detailed guidance protocols to capture the different scenarios encountered."

**This is the consumer-wearable analogue of the phenotyping-app background-execution problem.** A
device advertised as passive required periodic participant interaction with a *second* app to keep
data flowing, the failure varied by handset and OS version, and it consumed staff time that the study
could not measure. It is finding #3 — purely passive collection does not exist — reproduced on a
wearable-plus-vendor-app pipeline rather than a research app.

**No adverse events.**

## Feasibility Findings

Against the pre-set benchmarks: **enrolment/eligibility met (63–64% vs ≥60%)**; **retention met for
adults (93%) and near-met for youth (77% vs ≥80%)**; **fidelity comfortably met (99% vs ≥80%)**;
**adherence met (79–82% vs ≥70%)**; **acceptability met (83–100% vs ≥80%)**; **engagement not met**.

**Acceptability was high and higher in youth than adults:**

| | Adults | Youth |
|---|---|---|
| Program somewhat/very easy to use | 88% (69/78) | 96% (27/28) |
| Message frequency "just right" | 83% (65/78) | 93% (26/28) |
| Program helped me be more active | 99% (77/78) | 100% (28/28) |
| Would recommend to family/friends | 97% (75/77) | 100% (28/28) |

**The step tracker was the highest-rated component** for both groups; the web resources were the
lowest-rated, and qualitative work in the same sample found some participants were **wary of clicking
links sent by text** — a security-hygiene behaviour that directly suppressed engagement with an
intervention component.

**Engagement is where the study's most important equity finding sits.** Adults replied to a mean of
**2.6 (SD 2.2) of 7** two-way messages, youth **3.2 (SD 2.7)**. And **adults who replied to more
messages were significantly more likely to be White non-Hispanic and to hold a college degree**, and
non-significantly more likely to be female and younger. Among youth there was no such patterning.

**Efficacy signals (exploratory, single-arm, all non-significant in the full sample):** adults +240
steps/day (d=0.13), youth +413 (d=0.15). Larger among the least active at baseline — adults
**<5000 steps/day: +609 steps/day (d=0.40, 18%)**; youth **<8000: +1406 (d=0.58, 26%)** — and among
the most engaged tertile (adults +584, youth +941). Youth whose **parent** received the messages showed
larger increases (+530) than those messaged directly. Awareness of one's own activity level rose
significantly in adults (2.7→3.1, p=0.01) and non-significantly in youth.

Regression on the highest-baseline youth subgroup showed a **large negative change** (−1825
steps/day at endpoint, p=0.002), which is what regression to the mean looks like in a single-arm
design and reinforces that these are exploratory.

## Relevance to Future Study Design

1. **Define smartphone access at the household level, not the individual level, where the population
   allows it.** Zero of 181 screened were excluded on access — but the criterion permitted a parent's
   phone or a household tablet, and the study enrolled parent–child dyads. This is a protocol choice
   that removed an exclusion criterion, not evidence that individual ownership no longer varies.
   Verify locally before either provisioning phones or assuming you need not.
2. **The barrier has moved to phone *service*, not phone ownership.** 1.1% of messages failed because
   numbers went inactive. Budget for churn in phone numbers, not for absence of phones.
3. **Consumer wearables need a data-flow monitor and a staleness threshold.** Weekly Garmin API review
   with 4-day no-data outreach, 10 participants contacted, 9 of 10 sync failures. This is the same
   mechanism LINC formalises for phenotyping apps, and it should be standard on any wearable study
   using a vendor API.
4. **Garmin-to-Garmin-Connect sync failure was the dominant technical problem, was handset- and
   OS-version-dependent, and recurred.** A vendor-app sync step in your pipeline is an ongoing staff
   cost, not a one-time setup cost.
5. **A run-in period is a cheap prospective adherence screen.** Excluding participants who wore the
   device <3 of 7 run-in days is more defensible than discovering the same participants as missing
   data at analysis.
6. **Engagement with interactive content stratified by race and education *within* a
   majority-Black, low-income sample.** Passive wear adherence did not (79–82% overall). If your
   outcome depends on active engagement, the digital divide reappears inside the population you
   recruited to address it.
7. **Wear adherence at 79–82% over 7–8 weeks on a provisioned entry-level tracker is achievable in a
   population usually described as hard to reach** — and the device was the participants' favourite
   component. The reach problem here was engagement with content, not with hardware.
8. **Do not send bare links by SMS.** Some participants would not click them.

## Evidence Confidence

**Verified** — the enrolment funnel for adults and youth; all retention percentages by assessment
type; the wear-time definition (≥8 h + ≥100 steps; ≥3 valid days) and non-wear rule; the 46/44 valid
wear days and 82%/79% adherence; the 45/3955 message-delivery failures; the 10 troubleshooting
contacts with the 9/10 sync attribution; all acceptability percentages; the mean message replies and
their demographic patterning; the pre-set benchmarks; every step-count estimate in Table 2 with its
CI and p-value; the explicit statement that no one was excluded for lack of smartphone access; the
Garmin in-kind monitor contribution. Read from the published PDF and PMC XML (PMC13282599), 2026-09-02.

**Exploratory, and the authors say so** — the step-count changes are from a **single-arm** design with
no control group; the full-sample changes were non-significant; the subgroup effects are post hoc,
non-significant and subject to regression to the mean (visible in the high-baseline youth subgroup's
large negative change). Read them as hypothesis-generating.

**Reported** — the recurring, unquantified sync problems and the requirement for some participants to
engage regularly with the Garmin app. Explicitly described as anecdotal by the authors.

**Vendor relationship** — Garmin provided some monitors in kind. No authors are Garmin-affiliated, no
Garmin role in design or publication is declared, and the paper reports the Garmin sync failure as the
dominant technical problem, which is not a flattering finding for the donor.

**Generalisability** — one US metropolitan area, one beta-version intervention, single arm,
predominantly female enrolment in both age groups (88%/77%), and a documented education gradient
between screened and enrolled adults. The authors explicitly identify **reach among men, boys, and
adults with lower education** as the study's main shortfall.

## Key Links

- Paper (OA, CC BY): https://doi.org/10.2196/76991
- Europe PMC: https://europepmc.org/article/PMC/PMC13282599
- Local PDF: `../literature/2026-carlson-jmirmhealth-garmin-physical-activity-low-income-communities.pdf`

## Related profiles

- Device: [Garmin](../../module-01-wearables/profiles/garmin.md)
- **Qualifies (does not cleanly contradict) the smartphone-ownership funnel finding:** [`beiwe-spine-disease-mobility.md`](beiwe-spine-disease-mobility.md),
  [`aware-light-smartsense-d-youth-depression.md`](aware-light-smartsense-d-youth-depression.md)
- Representativeness and the digital divide: [`byod-demographic-imbalance.md`](byod-demographic-imbalance.md),
  [`allofus-fitbit-step-counts.md`](allofus-fitbit-step-counts.md),
  [`connect-multi-wearable-psychosis.md`](connect-multi-wearable-psychosis.md)
- Data-flow monitoring with a staleness threshold: [`mindlamp-linc-passive-data-quality.md`](mindlamp-linc-passive-data-quality.md)
- Wear-time thresholds determining the analytic sample: [`actigraph-als-upper-limb-wear-time.md`](actigraph-als-upper-limb-wear-time.md),
  [`allofus-fitbit-step-counts.md`](allofus-fitbit-step-counts.md)
- Recruitment channel and in-person approach outperforming remote:
  [`beiwe-spinal-cord-injury-incentives.md`](beiwe-spinal-cord-injury-incentives.md),
  [`withings-postop-remote-monitoring.md`](withings-postop-remote-monitoring.md)

## Sources

1. Carlson JA, Materia F, Moon M, et al. *JMIR Mhealth Uhealth* 2026;14:e76991. DOI 10.2196/76991.
   Full text and tables read from the published PDF and PMC XML (PMC13282599), 2026-09-02. Establishes
   every figure in this profile.
