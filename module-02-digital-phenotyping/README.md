# Module 2 — Mobile Digital Phenotyping Platforms

**Update, 2026-10-11:** the Beiwe and RADAR-base profiles and their matrix cells were corrected
against the committed vendor fact records in `../facts/` (batch 1).

**Status, 2026-10-10:** ten current platforms are profiled. On 2026-10-10 every profile was corrected
against an independent review (hosting and academic access, app-store availability, compliance
evidence tiers, the AWARE sensor counts) and `comparison-matrix.md` was rebuilt from the corrected
profiles. The history below describes the original 2026-08-24/25 passes.

**Original status: two research passes complete for the first eight platforms, 2026-08-24 through 2026-08-25.**
The initial research phase (2026-08-24, single session) is now followed by direct-source-fetch
second passes covering every platform in the module: AWARE Framework, mindLAMP, and MetricWire
(2026-08-24, same-day second session) and Beiwe, RADAR-base, Avicenna Research (Ethica), m-Path, and
CARP Mobile Sensing (2026-08-25). This mirrors Module 1's two-pass depth, though the passes here were
narrower re-verification sweeps targeting each profile's specific "not independently verified" and
"Unclear"/"Reported" flags rather than full re-research from scratch. Major second-pass resolutions:
Beiwe Service Center's actual pricing (previously methodology-only), RADAR-base's confirmed
managed-hosting offering and itemized Android sensor catalog, Avicenna Research's ISO 27001:2022
statement (rated Verified at the time; corrected to Corroborated, vendor-stated, on 2026-10-10),
m-Path's fully public tiered pricing, and CARP Mobile Sensing's expanded
wearable/HealthKit-integration catalog and `carp-portal` dashboard repository. See
`../shared/research-log.md`'s 2026-08-25 entry for the full account, and
`../shared/unresolved-questions.md` (questions raised in T13) for what the second passes could not close.

## Purpose

This module answers the practical question CLAUDE.md poses for it: **what can a research team
collect and do with each mobile digital-phenotyping platform, how configurable and accessible is
the resulting data, what infrastructure and operational model does it require, and what are the
practical tradeoffs compared with alternatives?**

## Platforms covered

Ten platforms received full profiles:

| Platform | Category | Profile |
|---|---|---|
| **Beiwe** | Academic open source + paid managed service (Beiwe Service Center, published rates) | `profiles/beiwe.md` |
| **RADAR-base** | Academic/consortium open source, Kafka-based; managed hosting from The Hyve | `profiles/radar-base.md` |
| **mindLAMP** | Academic, source-available (server and apps unlicensed), mental-health/clinical dual-use; hosted via the BIDMC mindLAMP Core | `profiles/mindlamp.md` |
| **AWARE Framework** | Academic open source, plugin-extensible, Android-first | `profiles/aware-framework.md` |
| **Avicenna Research (formerly Ethica)** | Commercial SaaS | `profiles/avicenna-research-ethica.md` |
| **MetricWire** | Commercial SaaS | `profiles/metricwire.md` |
| **LifeData (RealLife Exp)** | Commercial SaaS — **EMA/ePRO only, not passive sensing** | `profiles/lifedata.md` |

> **Scope note on LifeData (added 2026-09-02).** LifeData is included because Module 2's scope already
> admits commercial EMA-centric platforms (Avicenna/Ethica, MetricWire) and because it is the platform
> behind two substantial deployments this knowledge base needed to be able to cite. But it sits at the
> edge of this module's definition and should be read that way: **its only sensor stream is GPS captured
> alongside a survey response** — no accelerometer, screen or app usage, communication metadata,
> Bluetooth, audio, wearable, HealthKit or FHIR. A bare "GPS: Yes" cell in the comparison matrix would
> badly overstate it next to Beiwe, RADAR-base or AWARE, so the passive-streams row states the
> restriction explicitly. Treat LifeData as an **EMA/ePRO platform benchmarked against phenotyping
> platforms**, not as one of them.
| **m-Path** | Commercial/academic hybrid, EMA/EMI-first | `profiles/m-path.md` |
| **CARP Mobile Sensing** | Academic open-source framework/library, with a DTU-hosted service and web portal | `profiles/carp-mobile-sensing.md` |
| **Evidation** | Commercial participant network and real-world-data platform. **Wearable plus survey intake through connected consumer accounts, not phone sensing.** Edge of scope, included for its recruitment scale and its published engagement evidence | `profiles/evidation.md` |

One additional file covers platforms that were identified but deliberately not given full profiles:

| File | Covers |
|---|---|
| `profiles/legacy-and-adjacent-platforms.md` | **Purple Robot** (legacy, Android-only, archived: last code 2019, maintainer statement 2023), **StudentLife** (historical study + dataset, not a live platform), **Koa Health** (active research program, no confirmed externally-deployable platform), and a note on candidates searched for but not found (PhoneStudy) |

See `_inventory-and-scope-decisions.md` for the full reasoning behind what was included, deferred, or
excluded, mirroring the pattern used in Module 1.

## Literature library

`literature-library.md` indexes the academic papers (as opposed to vendor docs/repos/news) cited
across this module's profiles, plus a handful of additional decision-relevant papers found via a
fresh per-platform search. Where a cited paper is legitimately open-access, the actual PDF is stored
under `literature/<platform-slug>/` rather than just linked: 54 of 91 catalogued papers as of
2026-10-10 (MetricWire has none; see the literature library for why). This mirrors Module 1's
`research-library-wearables.md` convention, without that file's funding/COI tiering (not applicable —
these are software-platform papers, not vendor-funded device-validation studies).

## The Beiwe/Forest relationship — handled explicitly

Per CLAUDE.md's specific instruction, `profiles/beiwe.md` treats the Beiwe/Forest relationship
carefully: they are **separate open-source repositories with separate release cadences**, both
maintained by the Onnela Lab, designed to work together but not architecturally fused. Beiwe collects
and stores data; Forest analyzes it. A study can use either without the other. The Beiwe profile
applies the same "Reported unless independently corroborated" standard to every other platform in
this module — no promotional framing, and its Limitations and Open Questions sections are as direct
about Beiwe as any other profile is about its own subject.

## What this module found, in brief

Updated 2026-10-10 to agree with the corrected profiles and the rebuilt matrix. Updated 2026-10-21
from the batch-2 vendor fact records (mindLAMP, AWARE, Avicenna Research, MetricWire, m-Path, CARP,
LifeData, Evidation; facts checked 2026-10-11).

1. **Three deployment postures**, not a simple open-source/commercial binary: self-hosted platforms
   with public source (Beiwe, RADAR-base and AWARE under open licences; mindLAMP source-available,
   its server and apps unlicensed); fully managed commercial SaaS (Avicenna Research, MetricWire,
   m-Path, LifeData, Evidation; Avicenna also offers vendor-installed on-premises); and a
   build-your-own-app framework (CARP Mobile Sensing). See `comparison-matrix.md` Table 3.
2. **All five public-source platforms now have a hosted alternative to self-hosting**: Beiwe (Beiwe
   Service Center, published rates), RADAR-base (The Hyve, quote only, best for about 200
   participants or fewer), mindLAMP (BIDMC mindLAMP Core, priced by proposal), CARP (DTU-hosted,
   research-partner projects only, 2024 rates published) and AWARE (University of Melbourne hosting
   service, by contact, price not stated). (Corrected 2026-10-10; this item previously said only
   Beiwe offered managed hosting. Corrected 2026-10-21 for AWARE's paid hosting and CARP's terms.)
3. **iOS/Android parity should not be assumed anywhere.** Beiwe and AWARE document per-stream iOS
   coverage: Beiwe's calls, SMS (lab-distributed Android builds only), Wi-Fi and Bluetooth are Android only; AWARE's catalogue marks 19 of
   33 modules as iOS-available, and AWARE Client V3 (2026-06-28) adds Apple Watch, AirPods motion
   and own-keyboard streams. CARP's package table marks light, screen, Wi-Fi, app usage, calls and SMS as
   Android only. RADAR-base has no maintained iOS passive app (its iOS data come from HealthKit
   through the questionnaire app). Elsewhere the iOS question is Unclear or only partly documented.
4. **App-store availability differs from what the module said before.** AWARE's iOS client is on the
   App Store (only the Android client is sideloaded); mindLAMP's public iOS build dates from 2023,
   with newer builds on TestFlight for testers only; CARP Studies is on the App Store as an unlisted
   app; no Google Play listing could be confirmed for Beiwe2 (its Android app is sideloaded from each
   deployment). Both m-Path apps are on Google Play. See Table 2.
5. **Pricing:** Beiwe (BSC, FY26 card), m-Path and CARP's DTU-hosted service (2024 rate table) publish
   prices. Avicenna Research, MetricWire, LifeData (VA contract amounts are on USAspending, Reported),
   Evidation, The Hyve, AWARE's paid service and the mindLAMP Core do not. Academic routes exist but
   are mostly unpriced: MetricWire's Academic Site Licence (plus a Penn State sub-licence, Reported),
   LifeData's academic pricing and student discount, and
   Evidation-collected ALiR data through USC's Understanding America Study Data Use Agreement.
   Avicenna's free trial is test-only (data wiped monthly).
6. **Compliance:** no Module 2 platform has an independently confirmed certification. Avicenna
   Research (ISO 27001:2022), MetricWire (ISO 27001, SOC 2 Type II, 21 CFR Part 11, HIPAA, GDPR) and
   m-Path (GDPR, HIPAA; it publishes a DPA but no BAA) make vendor statements, all Corroborated at
   most; mindLAMP's documentation describes HIPAA Security Rule safeguards (Corroborated). The Hyve
   states ISO 27001 for itself, with a scope that does not name RADAR-base (Corroborated, added
   2026-10-11); LifeData's Data Privacy Framework certification is confirmed on the Commerce registry
   (self-assessed, re-certification under review); CARP documents GDPR controller roles; Beiwe
   documents its encryption design. (Corrected 2026-10-10: the module previously called Avicenna's statement an
   independently audited certificate and said MetricWire had no compliance documentation.)
7. **mindLAMP's licensing matters for self-hosters**: the server, apps, activities and worker carry
   no licence file, while the vendor's privacy page claims "no licensing restrictions" and a public
   request for written terms (issue 943) is unanswered; the supported route is the mindLAMP Core.
8. **CARP Mobile Sensing is architecturally distinct**: a Flutter library a team builds its own app
   on, now with a DTU-hosted service and an actively developed web portal.
9. **Purple Robot and StudentLife are historically important but not live platforms**: Purple Robot
   is archived (development ended in January 2019; the maintainer declared it archived in December
   2023) and is Android-only; StudentLife survives as a dataset.

## How to use this module

- Start with `comparison-matrix.md` for the cross-platform tables, then read the individual profile
  for any platform under real consideration — the matrix cells are deliberately terse and the
  profiles carry the caveats and evidence.
- Check `_inventory-and-scope-decisions.md` before assuming a platform not listed here was
  overlooked; several near-miss candidates (Koa Health, PhoneStudy) are recorded there with the
  reasoning for their exclusion or deferral.
- Check `../shared/unresolved-questions.md` (Module 2 section) before relying on any pricing or
  compliance claim for an actual study design — this module surfaced an unusually large number of
  "requires direct vendor/maintainer contact" items relative to Module 1.
- Cross-reference Module 1's `samsung.md` if a study design pairs Samsung wearables with phone-based
  sensing. Samsung's Health Research Stack has digital-phenotyping-adjacent characteristics but is
  profiled there, not duplicated here.

## Known gaps for a future pass

- Sensor-level detail (exact passive-stream catalogs, sampling configurability, iOS/Android parity)
  is now documented in part (batch-2 fact records, 2026-10-11): m-Path's and CARP's stream tables and
  OS splits; mindLAMP's sensor list and sampling, with an OS split only for telephony and SensorKit;
  Avicenna's stream catalogue, with iOS parity still Unclear; MetricWire's API stream types, with
  per-OS parity and sampling still Unclear.
- No compliance certificate or audit report has been read for any platform; the vendor statements
  in Table 7 need checking against a certificate (Avicenna's UKAS CertCheck entry sits behind a
  CAPTCHA) or direct vendor confirmation before a regulated study relies on them.
- Hosted-service prices are unpublished for The Hyve, the mindLAMP Core and AWARE's University of
  Melbourne service. CARP's DTU service publishes 2024 rates and is open only to research-partner
  projects (Q131).
- No systematic published-use/citation-count survey was attempted for any platform (contrast
  CLAUDE.md's "Evidence of use" ask).
