# Module 2 — Mobile Digital Phenotyping Platforms

**Status: two research passes complete for all eight platforms, 2026-08-24 through 2026-08-25.**
The initial research phase (2026-08-24, single session) is now followed by direct-source-fetch
second passes covering every platform in the module: AWARE Framework, mindLAMP, and MetricWire
(2026-08-24, same-day second session) and Beiwe, RADAR-base, Avicenna Research (Ethica), m-Path, and
CARP Mobile Sensing (2026-08-25). This mirrors Module 1's two-pass depth, though the passes here were
narrower re-verification sweeps targeting each profile's specific "not independently verified" and
"Unclear"/"Reported" flags rather than full re-research from scratch. Major second-pass resolutions:
Beiwe Service Center's actual pricing (previously methodology-only), RADAR-base's confirmed
managed-hosting offering and itemized Android sensor catalog, Avicenna Research's ISO 27001:2022
certification, m-Path's fully public tiered pricing, and CARP Mobile Sensing's expanded
wearable/HealthKit-integration catalog and `carp-portal` dashboard repository. See
`../shared/research-log.md`'s 2026-08-25 entry for the full account, and
`../shared/unresolved-questions.md` Tier 13 for what the second passes could not close.

## Purpose

This module answers the practical question CLAUDE.md poses for it: **what can a research team
collect and do with each mobile digital-phenotyping platform, how configurable and accessible is
the resulting data, what infrastructure and operational model does it require, and what are the
practical tradeoffs compared with alternatives?**

## Platforms covered

Eight platforms received full profiles:

| Platform | Category | Profile |
|---|---|---|
| **Beiwe** | Academic open source + optional managed service | `profiles/beiwe.md` |
| **RADAR-base** | Academic/consortium open source, Kafka-based | `profiles/radar-base.md` |
| **mindLAMP** | Academic open source, mental-health/clinical dual-use | `profiles/mindlamp.md` |
| **AWARE Framework** | Academic open source, plugin-extensible, Android-first | `profiles/aware-framework.md` |
| **Avicenna Research (formerly Ethica)** | Commercial SaaS | `profiles/avicenna-research-ethica.md` |
| **MetricWire** | Commercial SaaS | `profiles/metricwire.md` |
| **m-Path** | Commercial/academic hybrid, EMA/EMI-first | `profiles/m-path.md` |
| **CARP Mobile Sensing** | Academic open-source framework/library (not a hosted product) | `profiles/carp-mobile-sensing.md` |

One additional file covers platforms that were identified but deliberately not given full profiles:

| File | Covers |
|---|---|
| `profiles/legacy-and-adjacent-platforms.md` | **Purple Robot** (legacy, Android-only, maintenance status Unclear), **StudentLife** (historical study + dataset, not a live platform), **Koa Health** (active research program, no confirmed externally-deployable platform), and a note on candidates searched for but not found (PhoneStudy) |

See `_inventory-and-scope-decisions.md` for the full reasoning behind what was included, deferred, or
excluded, mirroring the pattern used in Module 1.

## Literature library

`literature-library.md` indexes the academic papers (as opposed to vendor docs/repos/news) cited
across this module's profiles, plus a handful of additional decision-relevant papers found via a
fresh per-platform search. Where a cited paper is legitimately open-access, the actual PDF is stored
under `literature/<platform-slug>/` rather than just linked — 13 papers across 8 platforms as of
2026-08-24 (MetricWire has none; see the literature library for why). This mirrors Module 1's
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

1. **The module splits into three deployment postures**, not a simple open-source/commercial binary:
   self-hosted academic open source requiring real infrastructure capacity (Beiwe, RADAR-base,
   mindLAMP, AWARE); fully managed commercial SaaS requiring none (Avicenna Research, MetricWire,
   m-Path); and a build-your-own-app framework requiring mobile-development rather than backend
   capacity (CARP Mobile Sensing). See comparison-matrix.md Table 3.
2. **Only Beiwe offers both a free self-hosted path and a documented paid managed-hosting
   alternative** run by the same organization that builds the software (the Beiwe Service Center).
   No comparable managed-hosting option was confirmed for RADAR-base, mindLAMP, or AWARE.
3. **iOS/Android parity should not be assumed anywhere in this module**, per CLAUDE.md's explicit
   instruction — and AWARE Framework is the one platform that says so about itself: its own
   materials describe the iOS port as different/lesser in coverage than the Android client. Every
   other platform's parity question was left as "not independently verified" rather than assumed.
4. **Updated 2026-08-25 — commercial pricing is no longer almost-universally non-public.** After the
   second pass, only **Avicenna Research and MetricWire** still require vendor contact for real
   pricing. **Beiwe** now publishes actual Beiwe Service Center rates ($1,937/month + $6/Active
   Participant Month), and **m-Path** now publishes a fully itemized tier-plus-add-on pricing
   structure — the most granular in the module. RADAR-base has a confirmed managed-hosting option
   (The Hyve) but its rates remain non-public.
5. **Updated 2026-08-25 — compliance documentation is no longer undocumented for every platform.**
   **Avicenna Research** has an independently audited, dated ISO 27001:2022 certification (the
   strongest compliance evidence in the module), and **m-Path** has a vendor self-declared
   "compliant with GDPR and HIPAA" statement. This is real progress but not closure: mindLAMP,
   MetricWire, RADAR-base, Beiwe, CARP Mobile Sensing, and AWARE Framework still have no documented
   compliance certification, and SOC 2/21 CFR Part 11 status remains unconfirmed even for Avicenna
   Research and m-Path. This remains the module's largest residual cross-platform gap.
6. **mindLAMP has explicitly deprecated components** in its own public GitHub organization
   (`LAMP-portal`, `LAMP-app`), which a prospective adopter needs to map against the current
   architecture before building on any specific repository.
7. **CARP Mobile Sensing is architecturally distinct from every other platform in this module** — it
   is a Flutter library/framework a team builds its own app on top of, not a pre-built,
   dashboard-configured product. This changes both its adoption cost (mobile-dev capacity, not
   backend/DevOps capacity) and its comparison basis against the others.
8. **Purple Robot and StudentLife are historically important but were deliberately not given full
   profiles** — Purple Robot's live maintenance status could not be established (and it is
   Android-only regardless), and StudentLife's lasting value to new researchers is its dataset, not
   a reusable data-collection tool.

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
  sensing — Samsung's Health Research Stack has digital-phenotyping-adjacent characteristics but is
  profiled there, not duplicated here.

## Known gaps for a future pass

- No platform in this module received the kind of full-text primary-documentation read that Module
  1's second pass gave several wearable ecosystems; most claims here rest on search-summary
  retrieval rather than direct fetch (see `sources.md`'s retrieval-method notes).
- Sensor-level detail (exact passive-stream catalogs, sampling configurability, iOS/Android parity)
  is the single most common "not independently verified" gap across every profile.
- No systematic published-use/citation-count survey was attempted for any platform (contrast
  CLAUDE.md's "Evidence of use" ask) — this would be a natural focus for a second pass.
- Compliance documentation (HIPAA/GDPR/SOC2/Part 11) is undocumented across the entire module and is
  the highest-value item to close before recommending any platform for a regulated study.
