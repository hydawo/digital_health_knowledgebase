# Module 3 — Recency/citation-graph build report, 2026-09-02

**What this is.** The build pass that consumed the two 2026-09 discovery files
([`_recency-scan-2026-09.md`](_recency-scan-2026-09.md) and
[`_citation-graph-scan-2026-09.md`](_citation-graph-scan-2026-09.md)) and turned their highest-value
candidates into profiles. **10 new profiles, taking the module from 40 to 50.** Every figure in every
new profile was read from full text (PDF or PMC full-text XML); no profile was written from an
abstract.

---

## What was built

| # | Profile | Study | Technology | Why it was chosen |
|---|---|---|---|---|
| 1 | [`mindlamp-linc-passive-data-quality.md`](profiles/mindlamp-linc-passive-data-quality.md) | Calvert, Lane, Flathers & Torous 2026, *Sci Rep* | mindLAMP | Named as highest priority. Squarely the module's central subject; postdates every prior profile; surfaced independently by both scans. |
| 2 | [`vpn-network-traffic-phenotyping.md`](profiles/vpn-network-traffic-phenotyping.md) | Mahmood et al. 2026, *JMIR Form Res* | **None** — WireGuard VPN | Named priority. Genuinely novel passive modality; full funnel, coverage, SUS/NASA-TLX and interviews. |
| 3 | [`sensorkit-techsans-older-adults.md`](profiles/sensorkit-techsans-older-adults.md) | Shen et al. 2026, *Innov Aging* | **Apple SensorKit** (TechSANS) | Named priority. Fills the older-adult gap and is the module's first deployed SensorKit study. **Platform attribution in both scans was wrong — see below.** |
| 4 | [`beiwe-type-2-diabetes-feasibility.md`](profiles/beiwe-type-2-diabetes-feasibility.md) | McInerney et al. 2024, *BMC Digit Health* | Beiwe | Named priority. Retention, feasibility and completeness together — **and OS-stratified missingness that bears directly on Tier 15 Q111.** |
| 5 | [`connect-multi-wearable-psychosis.md`](profiles/connect-multi-wearable-psychosis.md) | Bladon et al. 2026, *JMIR Form Res* | Fitbit + Apple Watch + Samsung, on RADAR-base/CareLoop | Named priority. Multi-device priority area; thickens Apple Watch and Samsung coverage. |
| 6 | [`mpath-dementia-esm-feasibility.md`](profiles/mpath-dementia-esm-feasibility.md) | Dewitte et al. 2025, *npj Dementia* | m-Path | Chosen: away from Beiwe; high-intensity ESM in dementia; Australia; explicit platform-founder COI. |
| 7 | [`garmin-low-income-physical-activity.md`](profiles/garmin-low-income-physical-activity.md) | Carlson et al. 2026, *JMIR Mhealth Uhealth* | Garmin Vívofit 4 | Chosen: **first Garmin deployment in the module** (a named device-breadth gap), low-income/majority-Black US cohort. |
| 8 | [`whoop-mental-health-survey-engagement.md`](profiles/whoop-mental-health-survey-engagement.md) | Presby et al. 2025, *JMIR* | WHOOP | Chosen: **first WHOOP deployment**; largest cohort in the module; hardest vendor COI. |
| 9 | [`samsung-palliative-pain-ecuador.md`](profiles/samsung-palliative-pain-ecuador.md) | Domínguez et al. 2026, *JMIR Form Res* | Samsung Galaxy Watch 5/6 | Chosen: **first Latin American deployment** (named geography gap); second palliative study; per-participant wear and battery telemetry. |
| 10 | [`mindlamp-global-cognitive-multisite.md`](profiles/mindlamp-global-cognitive-multisite.md) | Castillo et al. 2025, *Schizophrenia* | mindLAMP | Chosen on geography (India + US concurrent). **Thinnest of the ten operationally — flagged as such in the profile.** |

**Platform balance.** Only **1 of 10 is a Beiwe study**, deliberately, against the citation-graph
pass's 47-of-71 Beiwe yield. The module's Beiwe share falls from 11/40 (28%) to 12/50 (24%).

---

## What was assessed and rejected

| Candidate | DOI | Why not |
|---|---|---|
| Van der Donckt et al. 2024, "Mitigating data quality challenges in ambulatory wrist-worn wearable monitoring" | `10.1038/s41598-024-67767-3` | **Listed as RADAR-base in the citation-graph scan; it is an Empatica E4 paper.** Rejected on scope: it is a **tooling/methods paper applied retrospectively to two existing datasets**, with only **4 of 30 mBrain21 participants** publicly available for consent reasons, plus the public ETRI lifeLog 2020 set. No deployment cohort of its own. Its content overlaps [`profiles/empatica-epilepsy-data-quality.md`](profiles/empatica-epilepsy-data-quality.md) without adding new deployment data. **Worth revisiting** as a source of reusable countermeasures (non-wear detection, artifact handling, windows-of-interest with missing data), and its mBrain21 parent study (30 chronic-headache patients, 90 days, streaming E4) would qualify on its own. |
| Ball et al. 2025, EMA of suicidal thoughts and behaviours | `10.1016/j.beth.2025.05.007` | Already corrected in the recency scan: 90% of participants used **Realtime EXP by LifeData**, not MetricWire. Not re-litigated here. LifeData was flagged as a Module 2 expansion candidate; a parallel pass appears to be building it out. |
| Various JMIR Research Protocols entries (e.g. `10.2196/87201`) | — | Protocol papers with no results. Out of scope per Phase 1 screening. |
| `10.2196/77033` (Withings contactless sleep monitor), `10.3390/bios16050250` (unobtrusive sensing review), `10.1136/bmjopen-2025-115440` (FEXO protocol) | — | Validation study, review, and protocol respectively. All out of scope. |

**Not reached this pass**, and still the best remaining candidates: the m-Path social-support JITAI
(`10.2196/74103`), the RADAR-base autism/CNS digital-endpoints study (`10.2196/71145`), the Oura
frontline-nurses cohort (`10.2196/77818`), and the seven AWARE citation-graph candidates. **AWARE
remains the least-served of the covered platforms** and is the obvious target for the next pass.

---

## Platform attributions that turned out to be wrong

Three of the candidates carried incorrect platform attributions in the scan files. All three were
caught only by reading the full text, which is exactly the failure mode the citation-graph scan's own
caveats warned about.

1. **Shen et al. 2026** — listed in both scans as **beiwe/mindlamp/radar-base**, and described in the
   recency scan as "a rare cross-platform guide." **It is none of those.** The deployed platform is
   **TechSANS**, a bespoke iOS app built on **Apple SensorKit**. Beiwe and mindLAMP appear in one
   sentence: an Android build was *later* made on Beiwe and is **not analysed**, and Avicenna and
   mindLAMP are named as publicly available SensorKit-enabled alternatives. **RADAR-base does not
   appear in the paper at all.** Consequence: **the module still has no study comparing Beiwe,
   mindLAMP and RADAR-base**, and the "rare cross-platform guide" line in the recency scan should be
   struck.
2. **Mahmood et al. 2026** — listed under **Beiwe** in both scans. Beiwe appears **once**, as a
   background citation in Prior Work. **No phenotyping platform was deployed**; the instrument is a
   WireGuard VPN capturing network metadata.
3. **Van der Donckt et al. 2024** — listed under **RADAR-base** in the citation-graph scan. It is an
   **Empatica E4** paper (mBrain21 and ETRI lifeLog 2020 datasets). RADAR-base is not used.

**First authors** were verified from the full text in all ten cases. One discrepancy worth recording
for anyone reusing the extraction pipeline: **PMC's JATS `contrib-group` for JMIR articles lists the
handling editors before the authors** — for Carlson et al. it returns "Alicia Stone, Lorraine Buis,
Andrea Graham…", none of whom are authors. **The PDF byline is authoritative; the XML contrib-group
is not.**

---

## Findings that confirm, contradict or sharpen the module's headline findings

### Sharpened — the iOS/Android contradiction (Tier 15 Q111), and it now has a shape

[McInerney 2024](profiles/beiwe-type-2-diabetes-feasibility.md) supplies the single most useful data
point yet, because it is **Beiwe** — the platform whose three prior studies favoured iOS — and it
**stratifies by stream**:

| Stream | iPhone | Android | Test |
|---|---|---|---|
| Morning EMA missing | **70.0%** | **21.3%** | t(66)=8.623, p<0.001 |
| Evening EMA missing | **70.6%** | **26.8%** | t(66)=7.965, p<0.001 |
| Accelerometer missing | *no significant OS association* | | |
| GPS missing | *no significant OS association* | | |

**A ~49-point iOS penalty on active data and no detectable OS effect on passive data, in one cohort,
on one platform, at one time (Feb–Aug 2021, 62% Android / 38% iOS, stable between completers and
dropouts).**

**The proposed sharpening:** the module currently records the OS asymmetry as *platform- and
configuration-specific with no settled direction*. This study suggests it is **stream-specific before
it is platform-specific** — the direction can differ between the active and passive streams of the
*same* deployment. On that reading the existing evidence stops being flatly contradictory: Kiang's
GPS non-collection and Yi's GPS compliance are **passive** findings; Niemeijer's 6×-longer iOS gaps
are **passive**; McClaine's lower Android yield is **active**; McInerney's is **active**. It does not
fully resolve the contradiction (Niemeijer and Kiang are both passive and disagree), but it means
**any statement of the form "iOS is better/worse on platform X" that does not name the stream is
under-specified**, and Q111 should be rewritten to require the stream.

The **mechanism here is unidentified** and the profile says so — it could be notification delivery,
survey rendering (participants reported notifications leading to a black screen), or the fixed
3-hour response window interacting with iOS notification handling. Identifying it would be high value.

**Two other OS-relevant observations, both negative:**

- [Calvert 2026 (LINC)](profiles/mindlamp-linc-passive-data-quality.md) is **90.3% iOS** and its
  Limitations section names that as a possible driver of its 0.92 headline — **but reports no
  OS-stratified completeness.** The most frustrating omission in the batch.
- [Shen 2026](profiles/sensorkit-techsans-older-adults.md) is **iOS-only**, so no comparison is
  possible — but it independently documents the **iOS-side** background constraint in plain terms:
  participants had to keep the app out of the app switcher and **reopen it after every phone
  restart**.

### Contradicted — finding #14, the pre-consent smartphone-ownership funnel

Finding #14 cites [Cote 2019](profiles/beiwe-spine-disease-mobility.md): **42% of those approached
excluded for not owning a smartphone.** [Carlson 2026](profiles/garmin-low-income-physical-activity.md),
screening 181 adults and youth across the **six highest-Social-Vulnerability-Index zip codes in
Kansas City** (44–88% Black residents; enrolled cohort 84% Black, 63% no college degree), reports:

> **"No individuals who were screened for eligibility were ineligible because of lack of access to a
> smartphone."**

**Zero.** The barrier appears to have moved from **phone ownership** to **phone service**: 1.1% of
3,955 intervention SMS failed to deliver, "largely because of mobile phone numbers being inactive for
a period of time." Finding #14's other three legs (oncologist gatekeeping, handset incompatibility,
consent design) are untouched; the **smartphone-ownership leg is 2019 evidence and should be dated
as such.**

### Sharpened — finding #6, BYOD trades representativeness for compliance

[Bladon 2026](profiles/connect-multi-wearable-psychosis.md) shows the same trade-off appearing
**inside a provisioned study, through device choice**. The Samsung Galaxy Watch was chosen
disproportionately by **Black and Black British participants (29.8% vs 12.8% Apple), the most deprived
IMD quintile (55.3% vs 28.6%), and the least employed group (10.6% employed)** — and Samsung was the
device discontinued on data quality. The authors state the tension themselves. **A data-driven device
decision is not demographically neutral**, and this is a mechanism finding #6 does not currently
cover.

[Carlson 2026](profiles/garmin-low-income-physical-activity.md) adds a second layer: within a
deliberately low-income, majority-Black frame, **enrolled adults were significantly more likely to
hold a college degree than those screened (37% vs 15%)**, and **adults who engaged more with two-way
messages were significantly more likely to be White non-Hispanic and college-educated** — while
**passive wear adherence showed no such gradient** (79–82% overall). The digital divide reappears
**inside** the population recruited to address it, and it appears in the **active** stream only.

### Confirmed and extended — finding #7, scale not surviving a protocol

[Presby 2025](profiles/whoop-mental-health-survey-engagement.md) reaches the same outcome without any
of the usual causes. No recruitment, no provisioning, no clinic visit, no second vendor — just a
**monthly two-item survey inside an app paying subscribers already open daily**. Result: **mean 1.84
responses per person across 13 invitations (~14%)**, and **170,320 eligible → 3,196 (1.9%)** surviving
an ≥8-response + wear filter. Meanwhile the passive stream produced **7,942,176 device-days** with
**13.2 of 14 days present** conditional on responding. **The passive/active gap is a property of the
modality, not of research burden.**

### Confirmed on a fourth and fifth architecture — finding #3, purely passive collection does not exist

- **Apple SensorKit / iOS** ([Shen 2026](profiles/sensorkit-techsans-older-adults.md)): keep the app
  out of the app switcher; reopen after every restart. Two participants withdrew over technical
  frustration; a third was excluded for unrecoverable data loss.
- **Network layer** ([Mahmood 2026](profiles/vpn-network-traffic-phenotyping.md)): the VPN silently
  stops on reboot or battery death, with **no indicator on most handsets**. One participant lost
  **304 hours (~12.5 days)**. The authors' stated next step is **automated reactivation** — the third
  independent arrival at a keepalive in this module.
- **Consumer wearable + vendor app** ([Carlson 2026](profiles/garmin-low-income-physical-activity.md)):
  **9 of 10 support contacts were Garmin-watch-to-Garmin-Connect sync failures**, recurring,
  handset- and OS-version-dependent, with some participants needing to "regularly engage with their
  Garmin app to ensure proper synchronizing."

And LINC is the counterpoint that proves the rule: mindLAMP's answer to the same OS constraint is a
**daily EMA whose purpose is to keep the app foregrounded** — the *opposite* design from Beiwe's
server-side `heartbeat`, aimed at the identical problem.

### Sharpened — finding #15, definitions decide the answer

Four new instances, three of them **within a single paper**:

- **[Calvert 2026](profiles/mindlamp-linc-passive-data-quality.md): 0.92 vs 0.78** passive and
  **0.95 vs 0.76** active, for the **same cohort**, differing only in which days enter the
  denominator. The paper reports both — the companion analysis's figures are named in its own text.
- **[Mahmood 2026](profiles/vpn-network-traffic-phenotyping.md): 93% vs 66% retention.** 93% =
  ≥5 days of traffic among those contributing any traffic; 66% = consent to exit interview. **27
  points apart, both in the abstract-adjacent text, both defensible.**
- **[Bladon 2026](profiles/connect-multi-wearable-psychosis.md): Fitbit heart-rate completeness is
  80.1% or 53.0%** depending only on whether the denominator is **valid days** or **valid hours**.
  A "valid day" metric roughly doubled apparent completeness across all three device groups.
- **[Presby 2025](profiles/whoop-mental-health-survey-engagement.md)** applies a **>1000 min/day**
  wear criterion — the strictest in the module — and it is a major driver of the 1.9% survival rate.

### Confirmed — finding #16, remote incentivised studies attract fraud

[Calvert 2026](profiles/mindlamp-linc-passive-data-quality.md) **disqualified 19 of 417 enrolments
(4.6%) as fraudulent or non-US address.** This reproduces
[Siebers 2025](profiles/metricwire-fraudulent-participation.md) on a different platform, in a
different country, with a different detection route — moving fraud screening from "one study noticed
this" toward a routine expectation for remote recruitment.

### New — completeness and *correctness* are different, and only one is reported

[Bladon 2026](profiles/connect-multi-wearable-psychosis.md): **98% of Samsung Galaxy Watch sleep data
had duplicated start timestamps across sleep stages and missing end timestamps**, making sleep
duration underivable. Sleep data were nominally *present* for 80% of Samsung users. **A completeness
dashboard would have shown green.** Nothing currently in the module's cross-cutting patterns covers
silent data corruption, and it deserves its own line.

### New — vendor policy change as a live study risk, now quantified

Same study: **of 30 escalations to the software team, 20 were Samsung, and 17 of those 20 were traced
to a newly enforced Samsung privacy policy that blocked data transmission mid-study.** This is the
same class as the Google Play call/SMS restriction
([Niemeijer 2023](profiles/carp-mpath-sense-performance-study.md)) and the RADAR-MDD call/SMS
removal, but it is the first instance where a **mid-study vendor policy change directly caused the
majority of a study's technical burden** and contributed to a device being dropped.

### Sharpened — findings #8, #12 and #13, on what actually buys engagement

Three new studies pull in different directions and together suggest a cleaner statement:

- **[Dewitte 2025](profiles/mpath-dementia-esm-feasibility.md): 80% compliance (799/1004), zero
  dropouts, no payment at all**, in **dementia**, at **7 prompts/day for 10 days with a 20-minute
  response window**. Bought with a screening call that mapped each participant's daily schedule, a
  video tutorial, a supervised trial-run video call, a day-2-to-4 check-in, per-participant schedule
  modification, and in one case **carer-synchronised notifications**.
- **[Shen 2026](profiles/sensorkit-techsans-older-adults.md)**: an uncompensated **passive** study
  lost a participant to *"lack of perceived benefit"* at 4 months, and the authors conclude
  explicitly that **"even with low-burden data collection, compensation may play an important role in
  reducing attrition."**
- **[Carlson 2026](profiles/garmin-low-income-physical-activity.md)**: paid up to **US $95** for
  assessments; wear adherence 79–82%, but **replies to two-way messages averaged 2.6 of 7** and
  stratified by race and education.

**Proposed synthesis for the cross-cutting patterns:** *structured human support raises completion;
payment raises persistence; neither raises engagement with interactive content, and engagement is the
component that stratifies demographically.* That reconciles Mercier's retention-up/completion-flat
result, Liu's unpaid high engagement, Clark's co-designed 80.21%, Dewitte's unpaid 80% and Shen's
uncompensated withdrawal without discarding any of them.

### New — the palliative consent constraint is a design problem, not a population property

Finding #8 currently rests on [Helmer 2025](profiles/movesense-palliative-support-trial.md), where a
no-proxy-consent requirement **excluded 95.6% of screened patients and terminated the study**.
[Domínguez 2026](profiles/samsung-palliative-pain-ecuador.md) ran a palliative deployment to
completion by recruiting **inside an existing home-based care programme**, screening on **KPS >50
before mentioning the study**, consenting **in person with a family member present**, and making
**family support an inclusion criterion** rather than an obstacle. The cohort is 7, and no pre-consent
funnel is reported — so this **weakens the generality of #8 rather than overturning it**, and the
missing funnel is the reason it cannot do more.

### New — where participants enter patient-reported outcomes

Same study: **246 of 296 PROs (83%) were entered on the smartwatch, only 50 (17%) on the phone app**,
with no dependency on location or report type. The module has no other direct measurement of this
choice, and it inverts the usual assumption that the watch is a fallback interface.

---

## Cross-cutting observations for whoever integrates this

1. **Two new "priority-area" boxes are now ticked.** Device breadth: **Garmin and WHOOP have their
   first entries**, and Samsung and Apple Watch each gain a second. Geography: **Ecuador is the
   module's first Latin American deployment** and Castillo adds concurrent India + US sites.
2. **The module's scope boundary was tested twice and both cases are flagged in-profile.**
   [Mahmood 2026](profiles/vpn-network-traffic-phenotyping.md) deploys **no** Module 1/2 technology
   (VPN network-layer sensing is flagged as a Module 2 expansion candidate), and
   [Presby 2025](profiles/whoop-mental-health-survey-engagement.md) is not a research deployment at
   all (no recruitment, provisioning or researcher contact) — included because its engagement funnel
   is a **hard empirical ceiling** for anyone proposing to piggyback on a consumer user base. Both
   carry explicit scope notes; both are legitimate to reject on integration if you prefer a stricter
   line. [Shen 2026](profiles/sensorkit-techsans-older-adults.md) is scoped as an **Apple SensorKit**
   deployment, which Module 1's `apple-watch-healthkit.md` does cover.
3. **Three papers contain internal reporting errors or inconsistencies**, all documented in-profile:
   McInerney's Attrition subsection inverts retention (says 18.8% completed; abstract, discussion and
   counts all give 18.8% *attrition* / 81.2% retention); Calvert's Discussion quotes 77.3% contacted
   once-or-twice against a Results figure of 52.9% (different denominators — of contacted vs of
   cohort); and Castillo's Boston PANSS scores sit at the instrument floor with SD 0, which the
   authors handle by excluding Boston from the totals.
4. **Module 1/2 expansion candidates surfaced:** **VPN/network-layer passive sensing** (Mahmood);
   **LifeData / Realtime EXP** (flagged by the recency scan, apparently in progress elsewhere); **CareLoop Health Ltd**, which
   with RADAR-base underpins the CONNECT platform and has a direct founder-COI relationship to
   Bladon et al.; and **neuroUX**, cited by Castillo as a digital cognitive-assessment comparator.
5. **Two PDFs could not be stored.** Mahmood (PMC13118141) and Bladon (PMC13340901): the Europe PMC
   `?pdf=render` route returns a 3-page truncation or a JSON error, and the JMIR PDF endpoints refuse
   automated retrieval. **Both were read in full from PMC full-text XML**, and both profiles say so
   in Key Links. `sources.md` will need the same "XML-extract only" treatment the five baseline
   studies get. The other **eight PDFs are stored** in `literature/` under the standard convention.
6. **All 10 profiles' relative links were checked against the filesystem.** Zero broken links.
7. **Platform-developer or vendor COI is present in 6 of the 10** and is stated explicitly in each:
   Torous (LINC; Castillo), Dejonckheere as m-Path co-founder and shareholder (Dewitte), Bucci and
   Ainsworth as CareLoop cofounders (Bladon), **all seven authors salaried by WHOOP** (Presby), and
   Garmin's in-kind monitor contribution (Carlson). Only McInerney, Mahmood, Shen and Domínguez are
   free of a platform/vendor relationship.

## Suggested next pass

1. **AWARE.** Seven citation-graph candidates, none built. It is now the least-served covered platform.
2. **The remaining named recency finds:** m-Path social-support JITAI (`10.2196/74103`), RADAR-base
   autism/CNS endpoints (`10.2196/71145`), Oura frontline nurses (`10.2196/77818`).
3. **The mBrain21 parent study** (30 chronic-headache patients, 90 days, streaming Empatica E4) rather
   than the Van der Donckt tooling paper that uses four of its participants.
4. **Rewrite Tier 15 Q111 to require the stream.** The question as posed ("which OS is better") is not
   answerable; "which OS is better *for which stream, on which platform*" is.
5. **Still no post-`heartbeat` Beiwe completeness figure.** McInerney's data are Feb–Aug 2021, so the
   module's newest Beiwe evidence remains pre-2024. Q106 is unmoved.
