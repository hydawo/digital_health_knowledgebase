# Module 2 — Sources

All sources accessed **2026-08-24** unless otherwise noted. "Retrieval" records how the source was
consulted, because it determines the confidence label a claim can carry.

**Academic literature note:** for the subset of sources below that are peer-reviewed papers,
conference papers, or preprints (as opposed to vendor docs, GitHub repos, or news/blog posts), see
**`literature-library.md`** for a dedicated index — full citation, open-access status, and a locally
stored PDF where the paper is legitimately open-access. Several entries below that were Search-summary
retrieval here (e.g. the RADAR-base JMIR Mental Health 2024 paper, RADAR-IoT, mindLAMP's JMIR mHealth
uHealth paper, AWARE's Ferreira et al. paper, m-Path's Frontiers paper, CARP's Bardram et al. arXiv
paper, and the Purple Robot systematic review) now have a Verified-status full-text PDF via that file.

- **Direct** — page fetched and read in this session (supports **Verified**)
- **Search summary** — established via search-result summarization of the named source (supports
  **Corroborated** at best)
- **Secondary** — third-party reporting about a primary source (supports **Reported**)

**Note on this module's retrieval mix**: this was a single research session (contrast Module 1's two
deep passes). A larger proportion of sources here are Search summary rather than Direct fetch —
several primary documentation sites (LAMP docs, AWARE Framework's detailed pages, individual vendor
pricing pages) either returned errors on direct fetch or were not directly fetched due to session
scope. This is recorded plainly rather than smoothed over; see each profile's own Sources section for
per-claim retrieval detail.

**Second-pass update (2026-08-24):** a follow-up session direct-fetched primary sources for AWARE
Framework, mindLAMP, MetricWire, Koa Health, and attempted Purple Robot's lab site, specifically to
close Tier 10 unresolved-questions items #87–92. New Direct-retrieval sources are marked below with
"(2nd pass)". MetricWire's own site and Purple Robot's lab site remained unreachable even on this
second, deliberate attempt (HTTP 403 and domain-wide HTTP 500 respectively) — these are now recorded
as **repeated, confirmed access barriers** rather than single-session gaps.

---

## Beiwe

| ID | Title | Org | URL | Type | Retrieval | Establishes |
|---|---|---|---|---|---|---|
| S-BEI-01 | Digital Phenotyping and Beiwe Research Platform | Onnela Lab, Harvard T.H. Chan SPH | https://hsph.harvard.edu/research/onnela-lab/digital-phenotyping-and-beiwe-research-platform/ | Lab page | **Direct** | Data types, iOS/Android support, architecture, BSD-3 licence, self-host vs BSC |
| S-BEI-02 | beiwe-backend README | Onnela Lab (GitHub) | https://github.com/onnela-lab/beiwe-backend | Open-source repo | **Direct** | Django/AWS architecture, encryption design, identifier hashing, BSD-3, related repos |
| S-BEI-03 | forest repository | Onnela Lab (GitHub) | https://github.com/onnela-lab/forest | Open-source repo | **Direct** | Forest's purpose and relationship to Beiwe |
| S-BEI-04 | Beiwe Service Center overview | Onnela Lab | https://www.beiwe.org/beiwe-service-center-overview/ ; https://hsph.harvard.edu/research/onnela-lab/beiwe-service-center/ | Service page | Search summary | BSC service scope, pricing methodology |
| S-BEI-05 | onnela-lab GitHub organization | Onnela Lab | https://github.com/onnela-lab | Org listing | Search summary | Recent commit activity used for "Active" status |

## RADAR-base

| ID | Title | Org | URL | Type | Retrieval | Establishes |
|---|---|---|---|---|---|---|
| S-RAD-01 | About | RADAR-base | https://radar-base.org/about/ | Platform page | **Direct** | Purpose, architecture, hosting models, data sources, KCL/The Hyve maintainership, Apache 2.0 |
| S-RAD-02 | Publications | RADAR-base | https://radar-base.org/publications/ | Listing page | Search summary | Published-use record across disease domains |
| S-RAD-03 | 2026 RADAR-base Symposium announcement | RADAR-base | https://radar-base.org/2026/05/28/%F0%9F%9A%80-radar-base-symposium-2026-innovation-impact-the-future-of-mobile-health/ | Blog/news | Search summary | 2026 activity, named industry partners |
| S-RAD-04 | Digital Phenotyping of Mental and Physical Conditions: Remote Monitoring of Patients Through RADAR-Base Platform | *JMIR Mental Health* 2024 | https://mental.jmir.org/2024/1/e51259 | Peer-reviewed | Search summary | Platform-use description across clinical domains |
| S-RAD-05 | RADAR-IoT: An Open-Source, Interoperable, and Extensible IoT Gateway Framework for Health Research | PubMed | https://pubmed.ncbi.nlm.nih.gov/39066012/ | Peer-reviewed | Search summary | IoT gateway extension, open-source status |

## mindLAMP

| ID | Title | Org | URL | Type | Retrieval | Establishes |
|---|---|---|---|---|---|---|
| S-LAMP-01 | BIDMCDigitalPsychiatry GitHub organization | BIDMC Division of Digital Psychiatry | https://github.com/BIDMCDigitalPsychiatry | Org listing | **Direct** | Repository inventory incl. "[Deprecated]" labels on `LAMP-portal`/`LAMP-app`; current `LAMP-server` |
| S-LAMP-02 | Digital Psych — mindLAMP | Digital Psych (Torous lab) | https://www.digitalpsych.org/mindlamp1.html | Lab page | Search summary | Platform framing, research/clinical dual orientation |
| S-LAMP-03 | Enabling Research and Clinical Use of Patient-Generated Health Data (the mindLAMP Platform): Digital Phenotyping Study | Vaidyam, Halamka, Torous — *JMIR mHealth uHealth* 2022 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8783287/ | Peer-reviewed | Search summary | Platform-description paper |
| S-LAMP-04 | mindLAMP publications | docs.lamp.digital | https://docs.lamp.digital/about/publications/ | Docs site | **Attempted, HTTP 404 (both passes)** | Not retrieved — confirmed documentation-access gap |
| S-LAMP-05 | LAMP-portal repository | BIDMCDigitalPsychiatry (GitHub) | https://github.com/BIDMCDigitalPsychiatry/LAMP-portal | Repo | **Direct (2nd pass)** | Archived by owner 2020-11-17, read-only |
| S-LAMP-06 | LAMP-app repository | BIDMCDigitalPsychiatry (GitHub) | https://github.com/BIDMCDigitalPsychiatry/LAMP-app | Repo | **Direct (2nd pass)** | Archived by owner 2020-11-17, read-only |
| S-LAMP-07 | BIDMCDigitalPsychiatry current repository listing | BIDMC Division of Digital Psychiatry (GitHub) | https://github.com/BIDMCDigitalPsychiatry?tab=repositories | Org listing | **Direct (2nd pass)** | Current successor repos (`LAMP-dashboard`, `LAMP-server`, `LAMP-core-android`, `LAMP-core-ios`, `LAMP-activities`, `LAMP-app-gateway`, `LAMP-js`/`LAMP-py` BSD-3-Clause, `LAMP-toolkit` MIT) |
| S-LAMP-08 | docs.lamp.digital landing page | BIDMC Division of Digital Psychiatry | https://docs.lamp.digital/ | Docs site | **Direct (2nd pass), landing content only** | Passive-sensor list, "flexible hosting" framing, `/api` nav reference |

## AWARE Framework

| ID | Title | Org | URL | Type | Retrieval | Establishes |
|---|---|---|---|---|---|---|
| S-AWR-01 | AWARE Framework official site | AWARE Framework | https://awareframework.com/ | Project site | **Direct (both passes)** | Platform framing, Android-primary/iOS-port distinction, app-store distribution constraint, Configurator/RAPIDS references |
| S-AWR-02 | AWARE Framework GitHub organization | AWARE Framework | https://github.com/awareframework | Org listing | **Direct (2nd pass)** | 97-repo inventory, Apache-2.0 licence confirmed on `aware-client` and named plugin repos, commit activity through Aug 2026 |
| S-AWR-03 | AWARE Framework — Open Collective | AWARE Framework | https://opencollective.com/aware-framework | Funding page | Search summary | Community-funding model |
| S-AWR-04 | AWARE: Mobile Context Instrumentation Framework | Ferreira et al. | https://www.researchgate.net/publication/275349654_AWARE_Mobile_Context_Instrumentation_Framework | Foundational paper | Search summary | Historical/architectural origin |
| S-AWR-05 | AWARE Sensors documentation | AWARE Framework | https://awareframework.com/sensors/ | Docs page | **Direct (2nd pass)** | **Primary/Verified.** Full per-sensor Android-vs-iOS availability table (~33 modules); resolves unresolved-question #88 |

## Avicenna Research (Ethica)

| ID | Title | Org | URL | Type | Retrieval | Establishes |
|---|---|---|---|---|---|---|
| S-AVI-01 | Avicenna Research official site | Avicenna Research | https://avicennaresearch.com/ | Vendor site | Search summary | Current company identity, rebrand from Ethica Data |
| S-AVI-02 | Avicenna Research (Ethica Data) product docs | Avicenna Research | https://avicennaresearch.dev/ | Vendor docs | Search summary | Named feature areas |
| S-AVI-03 | Data Access & Analytics | Avicenna Research | https://avicennaresearch.dev/features/data-access-and-analytics/ | Vendor docs | Search summary | Export formats (CSV, JSON, GEXF, KML), latency claim |
| S-AVI-04 | App Store listing — Avicenna (Ethica) | Apple | https://apps.apple.com/us/app/ethica-avicenna/id1137173052 | App listing | Search summary | Naming continuity |
| S-AVI-05 | Google Play listing — Avicenna Research | Google | https://play.google.com/store/apps/details?id=com.ethica.logger | App listing | Search summary | Package name continuity (`com.ethica.logger`) |
| S-AVI-06 | Ethica/iEpi academic project page | Univ. of Saskatchewan | https://www.cs.usask.ca/~osgood/iEpi/iEpi.html | Academic page | Search summary | Academic origin as epidemiological sensing/EMA system |
| S-AVI-07 | Avicenna Research company profile | CB Insights | https://www.cbinsights.com/company/ethica-data | Directory | Search summary | Corroborates Ethica-to-Avicenna continuity |
| S-AVI-08 | Third-party pricing/trial listings | Capterra, SoftwareAdvice, SoftwareWorld | various | Directory | Search summary | Free-trial characterization — **Reported, not vendor-verified** |

## MetricWire

| ID | Title | Org | URL | Type | Retrieval | Establishes |
|---|---|---|---|---|---|---|
| S-MW-01 | MetricWire platform characterization | MetricWire (via search aggregation) | https://metricwire.com/ | Vendor site | **Search-summary only — direct fetch blocked HTTP 403 in both passes (homepage, /pricing, /site-licence/, /contact-us/)** | Platform features (consent, diaries, passive sensing, trigger-based surveys, dashboards) |
| S-MW-02 | MetricWire company profile | PitchBook | https://pitchbook.com/profiles/company/89864-11 | Directory | Search summary | Founding year (2013), HQ |
| S-MW-03 | Third-party software directories | Capterra, SoftwareWorld, SoftwareSuggest, TechnologyCounter, SourceForge, Visualping | various | Directory | Search summary | Trial/demo availability; no pricing figures found (both passes) |
| S-MW-04 | EMA study figure referencing MetricWire | ResearchGate | https://www.researchgate.net/figure/Select-screenshots-from-the-EMA-study-smartphone-platform-MetricWire-EMA-ecological_fig2_354098947 | Peer-reviewed (figure) | Search summary | Evidence of research use |
| S-MW-05 | MetricWire GitHub organization | MetricWire | https://github.com/MetricWire | Org listing | **Direct (2nd pass)** | **Primary/Verified.** Exactly one public repo (unrelated forked ADR template); no public SDK/API client — corroborates closed-source characterization |
| S-MW-06 | m2c2kit integration guide — MetricWire | m2c2-project (GitHub) | https://github.com/m2c2-project/m2c2kit-integration-guides/blob/main/docs/metricwire.md | Integration guide | Search summary (2nd pass) | URL-based identifier-injection integration pattern with MetricWire |
| S-MW-07 | `zeolite` — unofficial Python client for MetricWire's "Catalyst" system | Univ. of Wisconsin–Madison Center for Healthy Minds (GitHub) | https://github.com/uwmadison-chm/zeolite | Repo | Search summary (2nd pass) | Evidence an internal/partner API ("Catalyst") exists, though no official public API docs located |

## m-Path

| ID | Title | Org | URL | Type | Retrieval | Establishes |
|---|---|---|---|---|---|---|
| S-MP-01 | m-Path official site | m-Path | https://m-path.io/ | Vendor site | Search summary | Platform framing, m-Path sense, JITAI/EMI support |
| S-MP-02 | m-Path: an easy-to-use and highly tailorable platform for ecological momentary assessment and intervention in behavioral research and clinical practice | *Frontiers in Digital Health* 2023 | https://www.frontiersin.org/journals/digital-health/articles/10.3389/fdgth.2023.1182175/full ; PMC: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10619650/ | Peer-reviewed | Search summary | Platform-description methods paper |
| S-MP-03 | m-Path — Research page | m-Path | https://m-path.io/landing/research/ | Vendor page | Search summary | "250+ Universities" claim — Reported |

## CARP Mobile Sensing

| ID | Title | Org | URL | Type | Retrieval | Establishes |
|---|---|---|---|---|---|---|
| S-CARP-01 | Copenhagen Research Platform | DTU | https://carp.dk/ | Project site | Search summary | Platform family overview |
| S-CARP-02 | CARP Mobile Sensing (CAMS) | DTU | https://carp.dk/cams/ | Project page | Search summary | Framework architecture, data-transformer features, ECG integration |
| S-CARP-03 | About — CARP | DTU | https://carp.cachet.dk/about/ | Project page | Search summary | MIT licence, DTU copyright, application domains |
| S-CARP-04 | carp_mobile_sensing Flutter package | DTU (pub.dev) | https://pub.dev/packages/carp_mobile_sensing | Package registry | Search summary | Active distribution confirmation |
| S-CARP-05 | The CARP Mobile Sensing Framework — A Cross-platform, Reactive, Programming Framework and Runtime Environment for Digital Phenotyping | Bardram et al. | https://arxiv.org/pdf/2006.11904 | Peer-reviewed / preprint | Search summary | Architecture paper |

## Legacy and adjacent platforms

| ID | Title | Org | URL | Type | Retrieval | Establishes |
|---|---|---|---|---|---|---|
| S-LEG-01 | Sensing Apps and Public Data Sets for Digital Phenotyping of Mental Health: Systematic Review | PMC | https://pmc.ncbi.nlm.nih.gov/articles/PMC8895287/ | Peer-reviewed | Search summary | Purple Robot Android-only coverage claim; platform-comparison context |
| S-LEG-02 | Purple Robot Android Apps | Precision Health Informatics Data Lab, Northwestern | https://phidatalab.org/software__trashed/purple-robot-android-apps/ | Lab page | **Direct in 1st pass; 2nd-pass re-attempt (this page + `/software/` + domain root) returned HTTP 500 across the whole domain** | Page existed in 1st pass; URL slug still an unconfirmed retirement signal; 2nd pass adds a domain-wide server-error signal, itself inconclusive |
| S-LEG-03 | studentlife R package | Zenodo | https://zenodo.org/records/3371922 | Data package | Search summary | Continuing secondary use of the StudentLife dataset |
| S-LEG-04 | Koa Health — Research | Koa Health | https://www.koahealth.com/research ; https://koahealth.com/legal/complete-research-papers/ | Company page | Search summary (1st pass); **Direct (2nd pass)** for the `/research` URL | **Primary/Corroborated (2nd pass).** Confirms internal-only digital-phenotyping framing; page contains no platform-availability, SDK, or API language for outside teams |

---

## Sources sought but not obtained

| Target | URL | Outcome |
|---|---|---|
| mindLAMP publications listing | https://docs.lamp.digital/about/publications/ | **404 (confirmed again, 2nd pass)** |
| AWARE Framework detailed sensor documentation | https://awareframework.com/sensors/ | **Resolved 2nd pass — direct fetch succeeded**, full sensor table obtained |
| MetricWire official site (homepage, /pricing, /site-licence/, /contact-us/) | https://metricwire.com/ | **HTTP 403 on every path tried, both passes** — bot-protection, not a retrieval-effort gap |
| MetricWire GitHub organization | https://github.com/MetricWire | **Resolved 2nd pass — direct fetch succeeded** |
| Koa Health research page | https://www.koahealth.com/research | **Resolved 2nd pass — direct fetch succeeded** |
| Purple Robot lab page / phidatalab.org (all paths) | https://phidatalab.org/... | **HTTP 500 domain-wide, 2nd pass** — still not obtained; new signal (server error, not 404) |
| mindLAMP core-server/dashboard/app licence text | github.com/BIDMCDigitalPsychiatry (individual repo licence files) | Not directly opened this session; org-level listing didn't surface it. `LAMP-js`/`LAMP-py`/`LAMP-toolkit` licences ARE confirmed |
| Vendor pricing pages (Avicenna Research, m-Path) | various | Non-public / not located (unchanged, out of this pass's scope — Avicenna and m-Path were not targeted this pass) |

---

## Link check — 2026-08-24 (1st pass) / 2026-08-24 second pass

- **Direct fetch succeeded (1st pass):** Onnela Lab platform page, `beiwe-backend` README, `forest`
  repo, RADAR-base "About," BIDMCDigitalPsychiatry GitHub org, AWARE Framework site (partial
  content), Purple Robot lab page.
- **Direct fetch succeeded (2nd pass, new):** AWARE Framework sensors documentation
  (`awareframework.com/sensors/`), AWARE Framework GitHub org, BIDMCDigitalPsychiatry current
  repository listing, `LAMP-portal` and `LAMP-app` repos (confirming 2020-11-17 archival),
  `docs.lamp.digital` landing page, MetricWire GitHub org, Koa Health `/research` page.
- **404 (genuinely unavailable, confirmed in both passes):** `docs.lamp.digital/about/publications/`.
- **403 bot-protection (confirmed in both passes, MetricWire specifically):**
  `metricwire.com/`, `metricwire.com/pricing`, `metricwire.com/site-licence/`,
  `metricwire.com/contact-us/`.
- **500 server error, domain-wide (new signal, 2nd pass):** `phidatalab.org` and every path tested
  under it (`/`, `/software/`, `/software__trashed/purple-robot-android-apps/`) — the domain that
  succeeded on a single-page direct fetch in the first pass could not be reached at all in the
  second pass.
- **Not directly fetched even after two passes (search-summary only):** Avicenna Research, m-Path
  (out of this second pass's scope — see task framing), and RADAR-base/CARP sub-pages (also out of
  scope this pass). This remains a priority for any future third pass on those specific platforms.
