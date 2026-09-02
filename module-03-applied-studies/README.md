# Module 3 — Applied Wearables and Digital Phenotyping Studies

**Status:** **55 study profiles / 54 distinct deployments** (2026-09-02). Two profiles report one cohort. Baseline of 19 (2026-08-31) plus a 21-study
extension built in two parallel passes — a platform-coverage pass and an Onnela-tranche pass.

## What this module is

Modules 1 and 2 answer *what a technology can theoretically do*. Module 3 answers *what happened when
researchers actually deployed it*.

The unit of analysis is the **study**, not the device or platform. The questions are operational and
methodological — recruitment, retention, adherence, data completeness, technical failure modes — not
sensor accuracy or platform capability. Those belong to Modules 1 and 2 respectively, and this module
links to them rather than duplicating them.

**Central question:** when research teams have actually used these devices and platforms in real
studies, what worked, what didn't, and what does that reveal about feasibility that vendor
documentation and platform capability alone can't show?

## Start here

| File | What it's for |
|---|---|
| **[`feasibility-matrix.md`](feasibility-matrix.md)** | **The main resource.** Three tables — scale/duration/retention, completeness/wear time, and a one-line takeaway per study — plus cross-cutting patterns and an important warning about non-standardised definitions. |
| [`profiles/`](profiles/) | One deep profile per study (**55**). |
| [`_citation-graph-scan-2026-09.md`](_citation-graph-scan-2026-09.md) | OpenAlex citation-graph discovery — finds deployments that cite a platform's methods paper without naming it. Confirms the CARP null by a second, independent method. |
| [`_recency-scan-2026-09.md`](_recency-scan-2026-09.md) | Date-sorted discovery pass. Shows the citation-sorted baseline missed **62 of 64** recent candidates, and corrects two of its own conclusions. |
| [`_uncovered-platforms-report.md`](_uncovered-platforms-report.md) | The AWARE / Avicenna / MetricWire / m-Path / CARP coverage pass. |
| [`_onnela-tranche-report.md`](_onnela-tranche-report.md) | The Onnela-tranche build report. |
| [`_inventory-and-scope-decisions.md`](_inventory-and-scope-decisions.md) | How the study universe was searched, what was screened out and why, known biases in the discovery method. |
| [`_onnela-module3-candidates.md`](_onnela-module3-candidates.md) | 27 triaged candidates from the Onnela Lab publication sweep, ranked, not yet profiled. |
| [`sources.md`](sources.md) | Consolidated source list with retrieval status. |
| [`_scan-queue.md`](_scan-queue.md) | **Candidates awaiting a profile.** Fed by the weekly scan routine; also carries the unbuilt backlog from the manual discovery passes. |
| [`literature-index.json`](literature-index.json) | Dedup ledger for the weekly scan — 55 profiled studies plus recorded rejections. |
| [`literature/`](literature/) | Open-access PDFs. Five baseline studies are XML-extract only — see `sources.md`. |

## The ten findings that matter most

Drawn across the whole baseline. Each links to the profile that establishes it.

1. **Retention and completeness are different questions, and studies mostly report the flattering
   one.** RADAR-MDD achieved ~80% outcome retention and **17.7% cross-stream completeness** in the
   same cohort. → [Matcham 2022](profiles/radar-mdd-recruitment-retention.md)
2. **Passive data outlasts active data — but not automatically.** Reproduced in five studies across
   three platforms; adolescent Beiwe passive held **flat at ~94% over 18 months while surveys fell
   65%→30%**. One study found the reverse for smartphone passive data.
   → [Huang 2025](profiles/beiwe-adolescent-feasibility.md),
   [de Angel 2023](profiles/radar-base-treatment-engagement.md)
3. **Purely passive smartphone collection does not exist.** OS background limits mean the app must be
   periodically foregrounded. Beiwe's `heartbeat` push (2024) substitutes a server-triggered wake for
   a participant-initiated one — narrowing but not removing the dependency.
   → [Beukenhorst 2022](profiles/beiwe-als-adherence.md)
4. **A single configuration choice dominated data loss**: onboard recording lost <10%, live streaming
   lost up to ~50%, on the same device across four centres. Participants wore the device; the system
   lost the data. → [Böttcher 2022](profiles/empatica-epilepsy-data-quality.md)
5. **Provisioning a phone made retention worse, not better** (HR≈1.66 for ceasing to contribute), and
   an Android-only platform requirement caused 11% of one study's withdrawals.
   → [Zhang 2023](profiles/radar-mdd-longterm-engagement.md),
   [Matcham 2022](profiles/radar-mdd-recruitment-retention.md)
6. **BYOD buys wear compliance no provisioned study matches, and costs representativeness.** 23 h/day
   median wear; and All of Us is >80% historically underrepresented overall but **70% White in its
   Fitbit substudy**. → [Lubitz 2022](profiles/fitbit-heart-study-afib.md),
   [Cho 2022](profiles/byod-demographic-imbalance.md)
7. **Enrolment scale does not survive a multi-step protocol.** 419,297 → 450 usable; 455,699 → 1,057.
   A $50 incentive did not fix it. → [Garcia 2022](profiles/apple-heart-data-management-lessons.md),
   [Lubitz 2022](profiles/fitbit-heart-study-afib.md)
8. **Consent design can be the binding constraint.** A no-proxy-consent requirement excluded 95.6% of
   screened palliative patients and terminated the study.
   → [Helmer 2025](profiles/movesense-palliative-support-trial.md)
9. **Missingness can be signal, not noise.** Adding survey non-completion as a predictor raised AUC
   from 0.81 to 0.93 — it outranked most content features.
   → [Wang 2021](profiles/beiwe-inpatient-suicide-pilot.md)
10. **Baseline disease severity mostly does not predict attrition** — null across four studies. But
    *anxiety*, *negative symptoms*, younger age, and slow notification response all do.
    → see the cross-cutting patterns in [`feasibility-matrix.md`](feasibility-matrix.md)

## What's covered

**Module 2 platforms — all eight covered:** Beiwe (12), **AWARE (8 profiles / 7 deployments)**, mindLAMP/LAMP (5), RADAR-base (4),
**Avicenna/Ethica (3)**, **MetricWire (3)**, **m-Path (3)**, **CARP (1)**. Plus movisensXS, Ilumivu mEMA,
Purple Robot and now **LifeData** in mixed designs.

**Beyond Module 1/2 technologies:** the recency set added this module's first **Apple SensorKit** and
first **VPN network-traffic** deployments. Both carry explicit scope notes — neither deploys a
profiled Module 1/2 technology, and both are legitimate to reject on a stricter reading of the scope
rule.

**Module 1 devices:** Fitbit (10), Apple Watch (3), **Samsung (3)**, ActiGraph (2), Empatica (2), **Oura (2)**,
Axivity/GENEActiv (1), Withings (1), Modus StepWatch (1), **Garmin (1, new)**, **WHOOP (1, new)**, plus a
chest-wall ECG sensor. Garmin and WHOOP were previously absent.

**Priority areas covered:** longitudinal deployments (8 weeks to 4 years); multi-device and
multi-modal studies (RADAR-AD's eight device types; Jonker's Fitbit + Withings + Connecare);
large-cohort and multi-site (455,699; 419,297; three sites across two countries); and studies
reporting feasibility as an outcome rather than a footnote (the majority here).

## What's missing

Recorded honestly, because the gaps shape what conclusions this module can support:

- ~~**Recency.**~~ **Addressed 2026-09-01** by a date-sorted re-run —
  [`_recency-scan-2026-09.md`](_recency-scan-2026-09.md). The gap was large (**62 of 64** recent
  candidates were invisible to the citation-sorted pass), so treat the 19-study baseline as
  *well-established* practice rather than current practice until the recency candidates are built out.
- **Device breadth.** Garmin, Polar, Samsung, ActiGraph and Oura deployments are thin or absent — the
  discovery vocabulary favoured phenotyping platforms.
- **Geography.** Almost entirely North American and Western European. mindLAMP's India sites are the
  only substantial exception; no low-income-country deployments.
- **Platform balance — partly addressed, but Beiwe still dominates.** All five previously uncovered
  platforms now have entries. However **Beiwe is 11 of 40 profiles (28%)**, nine of them sharing an
  author, so they are not eleven independent observations — and **every Beiwe figure in the module
  predates the platform's `heartbeat` feature** (newest collection window closes 2023). The module's
  Beiwe evidence is simultaneously its largest and its most systematically dated. Each affected
  profile carries a pre-heartbeat lower-bound label.
- **Discovery method has three structural blind spots**, all found the hard way. **(c) Venue-shaped
  invisibility:** a platform's deployment-reality literature can sit outside the biomedical indexes
  this module searches. AWARE's operational papers live in CSCW/IMWUT/UbiComp — and the single
  best-matched AWARE candidate found (`10.1145/3711043`, "Participant Engagement and Data Quality")
  **could not be obtained in full text at all**: ACM DL serves a challenge page, no preprint exists,
  and it is not in PMC. It was left unprofiled rather than written from its abstract.
- The first two blind spots:
  **(a)** platform-name search cannot filter platforms whose name is an ordinary English word
  (Europe PMC ignores phrase quoting for "AWARE", so date-sorted results were pure noise);
  **(b)** it cannot find *framework-shaped* platforms at all — CARP is a library embedded in other
  people's apps and publishes under their names (m-Path Sense, DiaFocus, mCardia). Only an OpenAlex
  citation-graph pass found it. **Treat any future null from a name-based query as unproven.**
- **Grey literature.** Consortium reports, trial-registry posted results and vendor case studies were
  not searched.
- **Standardised definitions.** No study in this baseline uses the same definition of "wear time" or
  "data availability" as any other. This is a field-level problem, not a gap in the search.

## Scope rules (from `CLAUDE.md`)

**In scope:** real research deployments using a device or platform already profiled in Module 1 or 2,
reporting enough about *how the deployment went* to inform future study design.

**Out of scope:** pure device-accuracy/validation studies (Module 1's literature library);
platform-architecture and methods papers with no deployment cohort (Module 2's); and feasibility
studies for technologies not yet profiled in Modules 1 or 2 — those are flagged as Module 1/2
expansion candidates rather than absorbed here.

**Cross-referencing:** profiles link back to the relevant Module 1/2 profiles. Content is linked,
never duplicated. Papers are catalogued once (in the module owning the *technology*) and profiled
here only if they carry operational substance.

## Additions from the 2026-09-01 extension

Findings from the 21 new profiles that change what the module says:

11. **OS asymmetry has no settled direction.** Three Beiwe studies favour iOS; **CARP found iOS gaps
    ~6× longer than Android's** and AWARE found Android yield lower than iOS. All Verified, pointing
    opposite ways. Stop planning around "iOS is better".
    → [Niemeijer 2023](profiles/carp-mpath-sense-performance-study.md),
    [McClaine 2024](profiles/aware-chemotherapy-engagement.md)
12. **Incentives buy enrolment persistence, not engagement.** Retention rose 50%→78% on a $30/2-month
    conditional payment — **but survey completion rate did not move**, and recruitment channel
    produced a bigger spread (53% vs 21%). → [Mercier 2020](profiles/beiwe-spinal-cord-injury-incentives.md)
13. **Co-design beats payment.** The module's highest mental-health compliance (**80.21%**) came from
    letting participants choose the prompt frequency themselves.
    → [Clark 2025](profiles/metricwire-sgm-youth-ema-feasibility.md)
14. **The funnel starts before consent, and is usually unreported.** 42% excluded for not owning a
    smartphone; 8 of 18 eligible patients gatekept out by their own oncologists behind a "100%
    approach-to-consent" headline; 29% unable to run the app on their own Android handset.
    → [Cote 2019](profiles/beiwe-spine-disease-mobility.md),
    [Wright 2018](profiles/beiwe-fitbit-gynecologic-cancer-hope.md),
    [Camargo 2025](profiles/aware-light-smartsense-d-youth-depression.md)
15. **Definitions decide the answer.** One study publishes **two defensible acceptability rates 59
    points apart** (39% and 98%) for the same cohort; another's "lowest-in-module" 39.1% is an
    artefact of a platform export limitation; a third yields **N = 202 / 240 / 308** from identical
    raw data at three wear-time thresholds.
    → [Kivelä 2024](profiles/avicenna-ema-suicidal-ideation-iatrogenic.md),
    [Dennard 2025](profiles/mpath-avatar2-esm-engagement.md),
    [Straczkiewicz 2024](profiles/actigraph-als-upper-limb-wear-time.md)
16. **Remote incentivised studies attract fraud, and platform metadata can catch it.** Carrier-country
    data unmasked 10 fraudulent participants; a screening checklist later blocked 37.
    → [Siebers 2025](profiles/metricwire-fraudulent-participation.md)

## Additions from the 2026-09-02 recency and citation-graph build

17. **The OS asymmetry is stream-specific before it is platform-specific** — this supersedes both
    earlier framings. In one Beiwe cohort, **iPhones missed 70.0%/70.6% of morning/evening EMA vs
    Android's 21.3%/26.8% (p<0.001), while accelerometer and GPS showed no OS association at all.**
    Never state an OS effect without naming the stream.
    → [McInerney 2024](profiles/beiwe-type-2-diabetes-feasibility.md)
18. **Data quality can be operationalised — and the operational cost is now quantified.** LINC raised
    median GPS quality to **0.92** against 0.12–0.80 across six prior studies on the same platform, at
    a cost of **1.3 troubleshooting contacts per participant, ~9 interventions/week, two RAs**. Below
    0.50 quality, home-time estimates are wrong by 2–4 hours.
    → [Calvert 2026](profiles/mindlamp-linc-passive-data-quality.md)
19. **Data can be present and wrong.** **98% of Samsung sleep records were present but corrupt.** No
    completeness metric in this module would have caught it — validate structure, not just presence.
    → [Bladon 2026](profiles/connect-multi-wearable-psychosis.md)
20. **Vendor policy changes are a quantified study risk.** 17 of 20 Samsung escalations in that study
    traced to a **mid-study Samsung privacy-policy change**.
21. **Zero-friction scale has a floor.** WHOOP's in-app surveys reached 181,574 members with no
    recruitment, provisioning or clinic step — and got **1.9% response and 1.84 responses per person
    in 13 months**. → [Presby 2025](profiles/whoop-mental-health-survey-engagement.md)
22. **Support raises completion; payment raises persistence; neither raises engagement with
    interactive content** — and interactive content is the component that stratifies demographically.

## Additions from the 2026-09-02 AWARE pass

23. **There are three kinds of OS effect, not one** — this refines #17. **Structural gates** (iOS does
    not expose SMS at all: features computable for **15 of 183 participants, 8.2%**), **yield
    differences** (70% vs 21% EMA miss), and **breadth differences** (Android delivered **8.4 vs iOS
    4.7 mean sensor types** — the opposite direction to the yield finding, on the same framework).
    → [Balliu 2024](profiles/aware-stand-mood-prediction-adherence.md),
    [Wu 2023](profiles/aware-alcohol-liver-disease-craving.md)
24. **A single platform's completeness figure is close to meaningless for a mixed cohort.** Within one
    study, one platform and one configuration, passive missingness ranged **1.2% (controls) to 20.4%
    (borderline personality disorder)** — a **17× spread by diagnosis**.
    → [Aledavood 2024](profiles/aware-momo-mood-mood-disorders.md)
25. **Care setting beats clinical severity for retention.** **1.7% vs 33.5–37.3% two-week attrition**
    between in-person clinical care and online support — with the *sicker* arm retaining better,
    because missed assessments were reconciled during routine visits.
    → [Balliu 2024](profiles/aware-stand-mood-prediction-adherence.md)
26. **Research-infrastructure failure is a distinct data-loss class, and self-hosting owns it.** Server
    congestion, Wi-Fi-gated upload, and one study provisioning **a router per participant**. Three
    independent studies. A direct input to the self-host-vs-SaaS decision in Module 2.
27. **Participant-exercised configurability costs data.** **35.4% of person-days unusable** because
    participants, told the sensors were configurable, switched GPS off.
    → [Bae 2023](profiles/aware-binge-drinking-jitai-sensor-loss.md)
28. **A second clean exception to #2 (passive outlasts active).** In one cohort *"all participants
    supplied AWARE data every day that they responded to EMAs"* — 29.2% supplied zero EMAs and 12.5%
    zero sensor data. **Passive and active did not decouple at all.**
    → [Wu 2023](profiles/aware-alcohol-liver-disease-craving.md)

## Recommended next steps

1. ~~Re-run discovery sorted by **date**.~~ **Done** — [`_recency-scan-2026-09.md`](_recency-scan-2026-09.md).
   ~30 high-value recent candidates are listed there and remain unprofiled, including
   **Calvert/Torous 2026 "LINC: a framework for maintaining high-quality passive data"**, which is
   squarely this module's subject and postdates every profile here.
2. ~~Build entries for **AWARE, Avicenna, MetricWire, m-Path and CARP**.~~ **Done** — 12 profiles.
3. ~~Promote the Onnela candidates that fill genuine gaps.~~ **Done** — 9 profiles, including
   **Mercier 2020** on incentives.
4. ~~**Run a citation-graph discovery pass** (OpenAlex).~~ **Done** —
   [`_citation-graph-scan-2026-09.md`](_citation-graph-scan-2026-09.md). 71 candidates; confirmed the
   CARP null by a second independent method; **3 of the first ~12 candidates were mis-attributed to
   the wrong platform**, so treat its attributions as Reported until full-text-checked.
7. ~~**AWARE is the least-served covered platform.**~~ **Addressed** — 5 profiles added, and the
   "7 unbuilt candidates" figure did not survive inspection (most were reviews or platform papers).
   A dedicated pass over all **425 AWARE-citing papers** found the seam is genuinely thin: **215 had
   zero deployment signals, 106 had one, 31 had two, only 2 had three or more.** AWARE is widely used
   and almost never written about operationally.
8. **Module 3 still has no head-to-head comparison of Beiwe, mindLAMP and RADAR-base.** The candidate
   that appeared to be one (Shen 2026) turned out to use none of them.
5. **Resolve whether DiaFocus is CARP-based** — its 2025 *JMIR Diabetes* 6-month pilot is a real
   deployment with Bardram as an author, but the full text never names CARP. Its design paper would
   settle it, and it would double CARP's evidence base.
6. **Re-verify the Beiwe completeness figures against a post-heartbeat deployment.** Every Beiwe
   number in this module is pre-2024.
4. Decide on Module 1/2 expansion for the technologies surfaced here but unprofiled: **Dreem, Fibaro,
   CANedge, Connecare, movisensXS, Ilumivu mEMA**.
5. ~~Wire this module into the weekly literature-scan routine.~~ **Repo side done 2026-09-02** —
   ledger seeded with all 55 profiled studies, queue created, and the routine specification recorded
   in [`../shared/weekly-literature-scan.md`](../shared/weekly-literature-scan.md).
   **One manual step remains and only the account owner can do it:** paste the Module 3 section from
   that file into the routine's prompt in the claude.ai Routines UI. The routine is a cloud Routine,
   not a local task, so its prompt cannot be edited from a repo session.

   Note the deliberate asymmetry: **the routine triages Module 3, it does not write it.** Modules 1
   and 2 catalogue papers *about* a technology, which is safely automatable from abstracts. Module 3
   asserts *what happened in a deployment*, which is not — every figure in its 55 profiles came from
   full text.
