# Module 2 — Literature Library

Companion to `sources.md`. Where `sources.md` records *all* sources used to build this module
(vendor docs, GitHub repos, product pages, news items, and academic papers alike), this file is
narrower and deeper: it catalogs **only genuine academic literature** — peer-reviewed journal
articles, conference papers, and preprints — cited across the Module 2 profiles, plus a handful of
additional decision-relevant papers surfaced by a fresh literature search per platform. For open-access
papers, the actual PDF is stored locally under `literature/<platform-slug>/` rather than just linked,
per this project's literature-library convention (see `shared/research-log.md`, "2026-08-24 (later) —
Literature-library scope decision").

**Scope note:** this is not an exhaustive bibliography. Per `CLAUDE.md`'s evidence standard, it
targets "the strongest and most decision-relevant evidence" per platform — typically one methods/
platform-description paper plus one or two major validation/deployment/comparison studies — not
every paper that ever mentions a platform.

**Unlike Module 1's `research-library-wearables.md`**, this file does not use a funding/COI tier
system. These are software-platform papers (academic groups describing their own open-source or
commercial tooling), not device-validation studies with vendor-funded accuracy claims, so the tiering
convention doesn't transfer cleanly. Where a paper's authors are the platform's own developers, that
is noted in the Relevance column instead.

**OA-status confidence markers**, matching this knowledge base's evidence-confidence standard:
- **Verified** — the actual PDF was fetched and inspected directly (magic-byte + text-content check),
  and/or an explicit CC BY / open-access license statement was read directly on the article page or in
  the PDF itself.
- **Corroborated** — multiple secondary sources (e.g., PubMed, journal listing pages) agree the venue
  is open-access (e.g., JMIR's blanket CC BY policy, arXiv's inherent openness), but the specific
  article's license statement was not directly read.
- **Unclear** — access status could not be established from available evidence.

All entries below are **Verified** unless noted otherwise — every PDF in `literature/` was downloaded
and confirmed to be a genuine, readable PDF (not an HTML paywall/CAPTCHA page) before being kept.

**Last verified: 2026-08-24.**

---

## Beiwe

| Title | Authors | Venue/Year | DOI/URL | OA status | PDF | Relevance |
|---|---|---|---|---|---|---|
| New Tools for New Research in Psychiatry: A Scalable and Customizable Platform to Empower Data Driven Smartphone Research | Torous J, Kiang MV, Lorme J, Onnela JP | *JMIR Mental Health* 2016;3(2):e16 | [10.2196/mental.5165](https://mental.jmir.org/2016/2/e16) | **Verified OA** (JMIR CC BY) | [literature/beiwe/2016-torous-jmirmentalhealth-new-tools-for-new-research-in-psychiatry.pdf](literature/beiwe/2016-torous-jmirmentalhealth-new-tools-for-new-research-in-psychiatry.pdf) | The original Beiwe platform-introduction paper (Onnela lab). Not previously in `sources.md`; found via fresh search. |
| Beiwe: A data collection platform for high-throughput digital phenotyping | Onnela JP, Dixon C, Griffin K, Jaenicke T, Minowada L, Esterkin S, Siu A, Zagorsky J, Jones E | *Journal of Open Source Software* 2021;6(68):3417 | [10.21105/joss.03417](https://doi.org/10.21105/joss.03417) | **Verified OA** (CC BY 4.0) | [literature/beiwe/2021-onnela-joss-beiwe-data-collection-platform.pdf](literature/beiwe/2021-onnela-joss-beiwe-data-collection-platform.pdf) | Current software-description paper for the Beiwe codebase itself, authored by the Onnela Lab / Zagaran engineering team. Not previously in `sources.md`; found via fresh search. |

## RADAR-base

| Title | Authors | Venue/Year | DOI/URL | OA status | PDF | Relevance |
|---|---|---|---|---|---|---|
| RADAR-Base: Open Source Mobile Health Platform for Collecting, Monitoring, and Analyzing Data Using Sensors, Wearables, and Mobile Devices | Ranjan Y, Rashid Z, Stewart C, Conde P, Begale M, Verbeeck D, Boettcher S, The Hyve, Dobson R, Folarin A, The RADAR-CNS Consortium | *JMIR mHealth uHealth* 2019;7(8):e11734 | [10.2196/11734](https://mhealth.jmir.org/2019/8/e11734/) | **Verified OA** (JMIR CC BY) | [literature/radar-base/2019-ranjan-jmirmhealthuhealth-radar-base-platform.pdf](literature/radar-base/2019-ranjan-jmirmhealthuhealth-radar-base-platform.pdf) | The foundational RADAR-base architecture/methods paper — more foundational than the 2024 clinical-use paper already cited in `sources.md` (S-RAD-04). Not previously in `sources.md`; found via fresh search. |
| Remote Assessment of Disease and Relapse in Major Depressive Disorder (RADAR-MDD): recruitment, retention, and data availability in a longitudinal remote measurement study | Matcham F, Leightley D, Siddi S, Lamers F, et al. | *BMC Psychiatry* 2022;22:136 | [10.1186/s12888-022-03753-1](https://doi.org/10.1186/s12888-022-03753-1) | **Verified OA** (CC BY 4.0) | [literature/radar-base/2022-matcham-bmcpsychiatry-radar-mdd-recruitment-retention.pdf](literature/radar-base/2022-matcham-bmcpsychiatry-radar-mdd-recruitment-retention.pdf) | Major real-world deployment study (600 participants, 3 sites: London/Amsterdam/Barcelona) with hard recruitment, retention, and data-completeness figures — directly answers this module's "data completeness considerations" research question. Not previously in `sources.md`; found via fresh search. |
| Digital Phenotyping of Mental and Physical Conditions: Remote Monitoring of Patients Through RADAR-Base Platform | Rashid Z, Folarin AA, Zhang Y, Ranjan Y, Conde P, Sankesara H, Sun S, Stewart C, Laiou P, Dobson RJB | *JMIR Mental Health* 2024;11:e51259 | [10.2196/51259](https://mental.jmir.org/2024/1/e51259) | **Verified OA** (JMIR CC BY) | [literature/radar-base/2024-rashid-jmirmentalhealth-radar-base-remote-monitoring.pdf](literature/radar-base/2024-rashid-jmirmentalhealth-radar-base-remote-monitoring.pdf) | Already cited in `sources.md` (S-RAD-04) at Search-summary retrieval; upgraded to Verified with the full PDF now obtained. |
| RADAR-IoT: An Open-Source, Interoperable, and Extensible IoT Gateway Framework for Health Research | Ranjan Y, Chang J, Sankesara H, Conde P, Rashid Z, Dobson RJB, Folarin A | *Sensors* 2024;24(14):4614 | [10.3390/s24144614](https://pubmed.ncbi.nlm.nih.gov/39066012/) | **Verified OA** (MDPI open access) | [literature/radar-base/2024-ranjan-sensors-radar-iot-gateway-framework.pdf](literature/radar-base/2024-ranjan-sensors-radar-iot-gateway-framework.pdf) | Already cited in `sources.md` (S-RAD-05) at Search-summary retrieval; upgraded to Verified with the full PDF now obtained. |

## mindLAMP

| Title | Authors | Venue/Year | DOI/URL | OA status | PDF | Relevance |
|---|---|---|---|---|---|---|
| Enabling Research and Clinical Use of Patient-Generated Health Data (the mindLAMP Platform): Digital Phenotyping Study | Vaidyam A, Halamka J, Torous J | *JMIR mHealth uHealth* 2022;10(1):e30557 | [10.2196/30557](https://mhealth.jmir.org/2022/1/e30557) | **Verified OA** (JMIR CC BY) | [literature/mindlamp/2022-vaidyam-jmirmhealthuhealth-mindlamp-digital-phenotyping-study.pdf](literature/mindlamp/2022-vaidyam-jmirmhealthuhealth-mindlamp-digital-phenotyping-study.pdf) | Already cited in `sources.md` (S-LAMP-03) at Search-summary retrieval; upgraded to Verified. The platform-description methods paper (BIDMC Digital Psychiatry / Torous lab). |
| Digital phenotyping correlations in larger mental health samples: analysis and replication | Currey D, Torous J | *BJPsych Open* 2022;8(4):e106 | [10.1192/bjo.2022.507](https://doi.org/10.1192/bjo.2022.507) | **Verified OA** (CC BY) | [literature/mindlamp/2022-currey-bjpsychopen-digital-phenotyping-correlations-replication.pdf](literature/mindlamp/2022-currey-bjpsychopen-digital-phenotyping-correlations-replication.pdf) | Validation/replication study of mindLAMP passive-sensor-to-survey correlations at larger scale (147 college-student participants, 270 person-weeks). Not previously in `sources.md`; found via fresh search — the strongest available validation-style evidence for mindLAMP specifically (as opposed to platform-description alone). |

## AWARE Framework

| Title | Authors | Venue/Year | DOI/URL | OA status | PDF | Relevance |
|---|---|---|---|---|---|---|
| AWARE: Mobile Context Instrumentation Framework | Ferreira D, Kostakos V, Dey AK | *Frontiers in ICT* 2015;2:6 | [10.3389/fict.2015.00006](https://doi.org/10.3389/fict.2015.00006) | **Verified OA** (CC BY, license text confirmed in the PDF itself) | [literature/aware-framework/2015-ferreira-frontiersict-aware-mobile-context-instrumentation.pdf](literature/aware-framework/2015-ferreira-frontiersict-aware-mobile-context-instrumentation.pdf) | Already cited in `sources.md` (S-AWR-04) via a ResearchGate mirror at Search-summary retrieval; upgraded to Verified with the primary Frontiers-hosted OA PDF now obtained directly. The foundational AWARE architecture paper. |

## Avicenna Research (Ethica)

| Title | Authors | Venue/Year | DOI/URL | OA status | PDF | Relevance |
|---|---|---|---|---|---|---|
| Comparing Contact Tracing Through Bluetooth and GPS Surveillance Data: Simulation-Driven Approach | Qian W, Cooke A, Stanley KG, Osgood ND | *Journal of Medical Internet Research* 2024;26:e38170 | [10.2196/38170](https://www.jmir.org/2024/1/e38170) | **Verified OA** (JMIR CC BY) | [literature/avicenna-research-ethica/2024-qian-jmir-contact-tracing-bluetooth-gps-comparison.pdf](literature/avicenna-research-ethica/2024-qian-jmir-contact-tracing-bluetooth-gps-comparison.pdf) | Not previously in `sources.md`; found via fresh search. A genuine deployment study using the **Ethica Data (Avicenna Research) app** for GPS and Bluetooth proximity sensing (3 datasets, 2016, ~1 month each), from the same University of Saskatchewan group (Osgood, Stanley) that originated the academic precursor system iEpi. The strongest recent, platform-specific evidence found for this vendor — none of the profile's existing sources are peer-reviewed literature about the platform's actual field performance. |
| iEpi: An End to End Solution for Collecting, Conditioning and Utilizing Epidemiologically Relevant Data | Hashemian MS, Knowles D, Calver J, Qian W, Bullock M, Bell S, Mandryk RL, Osgood ND, Stanley KG | *Proc. 2nd ACM Int'l Workshop on Pervasive Wireless Healthcare (MobileHealth '12)*, pp. 3–8 | [10.1145/2248341.2248345](https://dl.acm.org/doi/10.1145/2248341.2248345) | **Paywalled** — ACM Digital Library requires purchase/subscription; no confirmed authoritative open-access copy located | Not obtainable — paywalled | The original academic precursor paper describing iEpi, the system Ethica Data (now Avicenna Research) commercialized. Historically important for understanding the platform's origin even though inaccessible. Already referenced narratively (not as a formal citation) in `profiles/avicenna-research-ethica.md`. |

## MetricWire

No dedicated peer-reviewed methods, validation, or deployment paper focused on the MetricWire
platform itself was located in this pass, despite a fresh targeted search. MetricWire appears in the
literature only as a data-collection instrument named inside other researchers' studies (e.g., the
ResearchGate figure already logged in `sources.md` as S-MW-04, and scattered EMA studies that used
MetricWire's commercial app without publishing anything about the platform's own architecture or
validity). This is consistent with `sources.md`'s existing finding that MetricWire blocks direct site
access (HTTP 403, both prior passes) and appears to have no self-published research page. **Recorded
as a genuine literature gap**, not filled with an unrelated citation, per `CLAUDE.md`'s instruction to
record when information cannot be determined.

## m-Path

| Title | Authors | Venue/Year | DOI/URL | OA status | PDF | Relevance |
|---|---|---|---|---|---|---|
| m-Path: an easy-to-use and highly tailorable platform for ecological momentary assessment and intervention in behavioral research and clinical practice | Mestdagh M, Verdonck S, Piot M, Niemeijer K, Kilani G, Tuerlinckx F, Kuppens P, Dejonckheere E | *Frontiers in Digital Health* 2023;5:1182175 | [10.3389/fdgth.2023.1182175](https://www.frontiersin.org/journals/digital-health/articles/10.3389/fdgth.2023.1182175/full) | **Verified OA** (CC BY, Frontiers) | [literature/m-path/2023-mestdagh-frontiersdigitalhealth-m-path-platform.pdf](literature/m-path/2023-mestdagh-frontiersdigitalhealth-m-path-platform.pdf) | Already cited in `sources.md` (S-MP-02) and in `profiles/m-path.md` at Search-summary retrieval; upgraded to Verified. **Correction:** `profiles/m-path.md` speculatively named "Kirtley, Hiekkaranta, et al." as possible lead authors with a caveat that the exact author list was "not independently confirmed" — the PDF confirms the actual lead author is **Mestdagh**, not Kirtley. The profile should be corrected to match (flagged here; not edited as part of this literature-retrofit pass since the task scope was the literature library itself). |

## CARP Mobile Sensing

| Title | Authors | Venue/Year | DOI/URL | OA status | PDF | Relevance |
|---|---|---|---|---|---|---|
| The CARP Mobile Sensing Framework — A Cross-platform, Reactive, Programming Framework and Runtime Environment for Digital Phenotyping | Bardram JE | arXiv:2006.11904 (2020) | [arxiv.org/abs/2006.11904](https://arxiv.org/abs/2006.11904) | **Verified OA** (arXiv preprint, inherently open) | [literature/carp-mobile-sensing/2020-bardram-arxiv-carp-mobile-sensing-framework.pdf](literature/carp-mobile-sensing/2020-bardram-arxiv-carp-mobile-sensing-framework.pdf) | Already cited in `sources.md` (S-CARP-05) and `profiles/carp-mobile-sensing.md` at Search-summary retrieval; upgraded to Verified with the PDF now obtained. The architecture paper for CAMS, authored solely by the DTU platform lead. |

## Legacy and adjacent platforms

| Title | Authors | Venue/Year | DOI/URL | OA status | PDF | Relevance |
|---|---|---|---|---|---|---|
| Sensing Apps and Public Data Sets for Digital Phenotyping of Mental Health: Systematic Review | Mendes JPM, Moura IR, Van de Ven P, Viana D, Silva FJS, Coutinho LR, Teixeira S, Rodrigues JJPC, Teles AS | *Journal of Medical Internet Research* 2022;24(2):e28735 | [10.2196/28735](https://www.jmir.org/2022/2/e28735) | **Verified OA** (JMIR CC BY) | [literature/legacy-and-adjacent-platforms/2022-mendes-jmir-sensing-apps-public-datasets-review.pdf](literature/legacy-and-adjacent-platforms/2022-mendes-jmir-sensing-apps-public-datasets-review.pdf) | Already cited in `sources.md` (S-LEG-01) and `profiles/legacy-and-adjacent-platforms.md` at Search-summary retrieval (used to characterize Purple Robot); upgraded to Verified. Note: correct venue is *JMIR* (not *JMIR mHealth uHealth* as the profile's citation number 1 might suggest — the profile cites it generically without a full venue name; this table gives the precise venue). |

---

## Summary of what changed vs. the pre-existing `sources.md`/profile citations

- **7 papers already cited** in `sources.md`/profiles (RADAR-base JMIR Mental Health 2024, RADAR-IoT,
  mindLAMP JMIR mHealth uHealth 2022, AWARE Ferreira et al., m-Path Frontiers 2023, CARP Bardram
  arXiv, and the Purple Robot/legacy systematic review) — all previously at Search-summary retrieval
  only — now have their actual OA PDF downloaded and verified, upgrading their retrieval status to
  Direct/Verified.
- **6 papers are new** to this module's literature base, found via a fresh per-platform search: the
  original 2016 Beiwe paper (Torous et al.), the 2021 Beiwe JOSS software paper, the foundational 2019
  RADAR-base JMIR mHealth uHealth paper, the RADAR-MDD recruitment/retention deployment study
  (Matcham et al. 2022), the mindLAMP validation/replication study (Currey & Torous 2022), and the
  Ethica/Avicenna Bluetooth-vs-GPS deployment study (Qian et al. 2024).
- **1 paper (iEpi, 2012 ACM)** was identified as historically relevant but is paywalled — recorded
  citation-only, not downloaded.
- **MetricWire** has no dedicated platform paper at all — recorded explicitly as a literature gap
  rather than a false completeness signal.
- A **correction candidate** was surfaced for `profiles/m-path.md`: its speculative "Kirtley,
  Hiekkaranta, et al." author guess is contradicted by the actual paper (lead author is Mestdagh).
