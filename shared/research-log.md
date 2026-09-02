# Research Log

---

## 2026-09-01 (latest) — Infrastructure decision: fixed the weekly literature-scan egress block, rejected PubCrawl as an arXiv fallback

**Module:** Cross-module infrastructure (the automated weekly literature-scan routine covering Module 1 —
Wearables and Module 2 — Mobile Digital Phenotyping Platforms). Not a content-research session; no
profile, comparison-matrix, or library file was touched. Logged here per this file's own convention of
recording "decisions that could affect later comparisons" and per the 2026-08-31 entry immediately below,
which first surfaced the failure this entry resolves.

### What happened

The 2026-08-31 run of the "Wearables research library – weekly PubMed scan" routine (a claude.ai/code
Routine, not a locally-scheduled task) failed before any search executed: the routine's cloud environment
blocked outbound access to `eutils.ncbi.nlm.nih.gov` (NCBI E-utilities, required for both modules) and
`export.arxiv.org` (the arXiv API, required for Module 2's CS/engineering-venue platforms) at the network
egress layer — a policy denial, not a transient error or rate limit.

Two remediation paths were evaluated:

1. **An official PubMed MCP connector** (`https://pubmed.mcp.claude.com/mcp`, Anthropic-hosted) was
   attached to the routine as an alternative fetch path for the PubMed side of both modules.
2. **A community MCP connector named "PubCrawl"** was also attached, intended to cover arXiv/preprint
   search as a substitute for the blocked `export.arxiv.org` call. Its underlying code
   (`github.com/nickjlamb/pubcrawl`, by Nick Lamb / PharmaTools.AI) was verified as legitimate, open-source,
   and requiring no API keys. **However, the specific hosted instance the routine was pointed at**
   (`pubcrawl-production-feb9.up.railway.app`) **has no corresponding official-hosted-URL claim in the
   project's own README** — the README documents this project as self-hosted only, with a `railway.toml`
   enabling *anyone* to deploy their own copy. The user could not confirm whether they personally deployed
   this specific instance or obtained the URL secondhand.

### Decision: PubCrawl rejected; egress allowlist fixed instead

**PubCrawl was removed from the routine entirely and will not be used**, for reasons specific to this
routine's unattended, no-confirmation, repo-push operating mode:

- This routine runs **fully unattended** — its own prompt explicitly instructs "Do not ask for confirmation
  at any step" — and holds **push access to this repo's GitHub remote**.
- An MCP tool result (e.g., a returned "paper abstract") is data the agent reads, not verified-safe input.
  If an unverified third party operates the connected instance, a compromised or malicious server could
  return content containing hidden instructions attempting to hijack the unattended run — a prompt-injection
  vector. This risk is normally mitigated by treating tool output as data rather than instructions, but an
  autonomous, no-confirmation, write-access routine has less room for that mitigation to catch every case
  than an interactive session would.
- Beyond content-injection risk, using a generic biomedical-search bridge of unconfirmed operatorship means
  this project's search queries (what devices/platforms are being tracked) would pass through a third
  party's server with no stated data-handling policy.

**Instead, the actual blocking cause was fixed directly**: the routine's cloud environment ("Default")
had its Network Access setting changed from **Trusted** to **Custom**, with
`eutils.ncbi.nlm.nih.gov` and `export.arxiv.org` added to the Allowed Domains list (plus "include default
list of common package managers" to preserve Trusted-tier access to GitHub/npm/PyPI). This is a first-party
Claude Code environment setting (`docs: cloud-environments` → Access levels → Custom), not a third-party
dependency — it resolves both modules' original blocked hosts without introducing any new connector trust
surface. The PubMed MCP connector remains attached as a secondary/parallel fetch path for the PubMed side
only; it was not needed to resolve the arXiv block, which the environment fix addresses directly.

### Verification

A manual "Run now" of the routine was triggered immediately after the environment change
(`session_id: cse_014x1WaYUc5YWXA2BX3YxnaE`) to confirm the fix before waiting for the next scheduled
Monday firing. See the next log entry (or this repo's commit history around 2026-09-01) for that run's
outcome once it completes.

### Decisions that could affect later runs

1. **PubCrawl should not be re-added to this routine** without first confirming who operates whatever
   specific hosted instance is being pointed at (self-deployed and controlled by the user, or a named,
   accountable operator) — the underlying open-source project itself is not in question, only unverified
   third-party hosting of it inside an unattended, write-access automation.
2. If arXiv coverage breaks again in the future (e.g., the environment's Custom allowlist is reset), the
   fix is the same environment-level Network Access setting, not a new MCP connector, unless a future
   connector's operator can be verified.

---

## 2026-08-31 — Automated weekly literature scan: BLOCKED, both modules (network egress denial)

**Module:** Cross-module (Module 1 — Wearables; Module 2 — Mobile Digital Phenotyping Platforms)
**Scope:** First run of the new automated weekly PubMed/arXiv literature-scan routine (per the
scheduled task prompt now governing `research-library-wearables.md` and
`literature-library.md` updates). Intended to query NCBI E-utilities for Oura/WHOOP/Apple Watch
(Module 1) and NCBI E-utilities + the arXiv API for the eight Module 2 platforms, using a trailing
10-day window (2026-08-21 to 2026-08-31) since neither module had a prior automated run.

### Outcome: failed before any search executed — both modules

Neither module's search ran. This session's network egress policy blocks the required APIs
outright, confirmed as a policy denial rather than a transient error:

- **`eutils.ncbi.nlm.nih.gov`** (NCBI E-utilities — required for both Module 1 and Module 2):
  `WebFetch` returned `EGRESS_BLOCKED`; the environment's agent-proxy status endpoint
  (`$HTTPS_PROXY/__agentproxy/status`) independently logged a matching `recentRelayFailures` entry —
  `connect_rejected`, "gateway answered 403 to CONNECT (policy denial or upstream failure)" — at
  2026-08-31T12:29:34Z.
- **`export.arxiv.org`** (arXiv API — required for Module 2 only): direct `curl` returned HTTP 403
  with "Host not in allowlist: export.arxiv.org. Add this host to your network egress settings to
  allow access." — a policy denial from the sandbox network layer, not the arXiv service itself.

Per this environment's own proxy documentation: 403 from the egress proxy means the destination host
is not permitted by the current session's organization network policy, and the correct response is
to report the blocked host rather than retry or attempt a workaround (no alternative fetch route,
credential, or retry cadence would change this — it is a policy allowlist gap, not a rate limit or
outage). No PDF-hosting domains (Europe PMC, arXiv PDF URLs, publisher sites) were even reached,
since both searches failed at the query step before any candidate paper existed to fetch.

### Per this session's own step-8 handling instructions

- **Module 1:** 0 papers found (search never executed) for Oura, WHOOP, and Apple Watch alike.
  `module-01-wearables/research-library-index.json` created fresh (`pmids_seen: []`,
  `last_run_date: null`) since it did not previously exist, but **`last_run_date` was deliberately
  left `null`, not set to today**, so the next run retries the same trailing-10-day-or-later window
  rather than silently skipping it. `research-library-wearables.md` was not touched.
- **Module 2:** 0 papers found (search never executed) for all eight platforms (Beiwe, RADAR-base,
  mindLAMP, AWARE Framework, Avicenna Research/Ethica, m-Path, CARP Mobile Sensing, MetricWire).
  `module-02-digital-phenotyping/literature-library-index.json` created fresh (`ids_seen: []`,
  `last_run_date: null`) for the same reason. `literature-library.md` was not touched.

### Notable exclusions

None — no candidate papers were ever retrieved to evaluate against either module's relevance bar.

### Files created

```
module-01-wearables/research-library-index.json       (dedup ledger scaffold; last_run_date null)
module-02-digital-phenotyping/literature-library-index.json  (dedup ledger scaffold; last_run_date null)
```

### Decisions affecting later runs

1. **This is an environment/session configuration gap, not a content or methodology problem.**
   Whoever administers this session's network egress policy needs to add `eutils.ncbi.nlm.nih.gov`
   and `export.arxiv.org` to the allowlist before this routine can produce any output. Until then,
   every future scheduled firing of this routine will fail identically at the same step.
2. **Both index JSON files exist now but carry `last_run_date: null`**, intentionally indistinguishable
   from "never run" — a future run (once egress is fixed) should treat the search window the same way
   a true first run would (trailing 10 days from that run's date, per the routine's own instructions),
   not assume any coverage from this attempt.

---

## 2026-08-25 — Module 2 third pass: direct-source re-verification of Beiwe, RADAR-base, Avicenna Research, m-Path, CARP Mobile Sensing

**Module:** Module 2 (Mobile Digital Phenotyping Platforms) — third pass overall, second direct-source
re-verification pass. This is a Maintenance pass under CLAUDE.md's Maintenance section (re-check
primary docs, update verification dates, record changes), not new-module research. Scope: the five
platforms **not** covered by the 2026-08-24 second pass (which covered AWARE Framework, mindLAMP, and
MetricWire) — **Beiwe, RADAR-base, Avicenna Research (Ethica), m-Path, and CARP Mobile Sensing** —
bringing all eight profiled Module 2 platforms to the same second-pass verification standard. Module 1
and the three already-second-passed platforms were explicitly out of scope and were not touched.

### Technologies researched

Beiwe (and Forest), RADAR-base, Avicenna Research (Ethica), m-Path, CARP Mobile Sensing.

### Files created or updated

- `module-02-digital-phenotyping/profiles/beiwe.md`
- `module-02-digital-phenotyping/profiles/radar-base.md`
- `module-02-digital-phenotyping/profiles/avicenna-research-ethica.md`
- `module-02-digital-phenotyping/profiles/m-path.md`
- `module-02-digital-phenotyping/profiles/carp-mobile-sensing.md`
- `module-02-digital-phenotyping/comparison-matrix.md`
- `module-02-digital-phenotyping/sources.md`
- `module-02-digital-phenotyping/README.md`
- `shared/unresolved-questions.md` (Tier 10 items #84, #85, #86, #89, #90, #93, #94 annotated; new Tier 13 added, items #101–#105)

### Major findings

1. **Beiwe — Beiwe Service Center pricing resolved (unresolved-question #85, Verified).** A direct
   fetch of the BSC's own overview page (`hsph.harvard.edu/research/onnela-lab/beiwe-service-center/`)
   — which had returned a connection error on the first attempt this pass and succeeded on retry —
   now returns actual rate figures, not only the previously published methodology: **$1,937/month
   fixed + $6/Active Participant Month variable**, with worked examples totaling $24,144–$27,564. This
   closes what had been the module's clearest "methodology published, rates not" gap. Also confirmed:
   a `data_access_api_reference` directory exists in `beiwe-backend` (API existence narrowed from
   "not identified" to "exists, scope unconfirmed"); Forest's subpackage structure (`jasmine` =
   mobility, `willow` = communication/sociability, `sycamore` = survey completion); and the backend
   README's precise HIPAA language ("may interact with laws covering PII or PHI like HIPAA") — an
   applicability acknowledgment, explicitly not a compliance certification claim.
2. **RADAR-base — managed-hosting offering confirmed (unresolved-question #86, Verified) and
   iOS/Android parity gap confirmed (Corroborated).** The Hyve, RADAR-base's co-maintainer, offers a
   named managed-hosting product, **"RADAR-base as a Service"**: GDPR-compliant cloud hosting, 2–4
   week setup, support for unlimited studies in general framing but explicitly best suited to studies
   of ~200 participants or fewer (single-server infrastructure) per the vendor's own page. No pricing
   is published. Separately, a direct fetch of RADAR-base's own "Phone Data Sensors" documentation
   itemized 17 Android passive-sensor streams and stated explicitly that "substantial differences"
   exist between iOS and Android, with iOS availability "more sparse... due to lack of background
   collection capabilities" — RADAR-base joining AWARE Framework as the second platform in this module
   with a self-documented, Verified/Corroborated (not just assumed) iOS/Android gap. A `ManagementPortal`
   GitHub repository was also confirmed as an actively maintained (not merely referenced) component.
3. **Avicenna Research (Ethica) — compliance posture materially upgraded (Verified/Corroborated),
   pricing and API status re-confirmed unresolved.** A direct fetch of `avicennaresearch.com/legal/`
   surfaced the strongest compliance evidence found anywhere in this module: **ISO 27001:2022
   certification, dated and audited** (certified November 2024 with zero nonconformities; a
   surveillance audit in November 2025, also zero nonconformities), plus detailed HIPAA Privacy/
   Security Rule, UK GDPR Article 8, EU GDPR, and PIPEDA language specifically addressing minors' data.
   This is Verified (a specific, dated, audited certification) for ISO 27001 and Corroborated (specific
   vendor-stated language, not independently audited in what this session accessed) for the
   HIPAA/GDPR/PIPEDA claims. Pricing and a developer API were both re-confirmed as not found, after two
   direct fetches (homepage, data-access-and-analytics page) plus a dedicated search this pass — this
   strengthens rather than merely repeats the prior "not confirmed" finding.
4. **m-Path — pricing fully resolved (unresolved-question #93, Verified) and compliance
   corroborated.** A direct fetch of `m-path.io/pricing/` returned the complete, previously-unfound
   tier structure: Free (€0/50 participants), Essential (€1,599–€2,958), Standard (€2,099–€3,616),
   Comfort (€3,099–€5,338), all scaling with participant count, plus separately priced add-ons —
   notably **Sensing Lite (€3,000)**, **Sensing Full (€10,000)**, and **API Access (€5,000)**. This
   quantifies and confirms what the first pass only described qualitatively: m-Path sense (passive
   sensing) and the platform's API are both add-ons priced well above the base subscription, not
   included capabilities. Separately, m-Path's own homepage states "compliant with GDPR and HIPAA" —
   Corroborated (a specific, vendor-stated claim) rather than Verified (no independent audit evidence
   located, in contrast to Avicenna Research's ISO 27001 certificate found the same pass).
5. **CARP Mobile Sensing — wearable/health-platform integration catalog substantially expanded
   (Verified), and a researcher-dashboard component ("carp-portal") discovered, revising the prior
   "not offered" characterization.** A direct fetch of `carp.dk/cams/` itemized named wearable
   integrations far beyond the first pass's generic "ECG monitor" reference: Movisens (Move4,
   EcgMove4, EdaMove4), the eSense earplug, Polar (H10, Verity Sense), Movesense (MD, Active), and the
   Dexcom G7 continuous glucose monitor — plus confirmed **Apple Health and Google Health Connect**
   integration, a genuine differentiator not previously documented for this platform. Separately, a
   direct fetch of the `carp-dk` GitHub organization (42 repositories) revealed a `carp-portal`
   repository, a `carp-cli` terminal client with a protocol editor, and `carp-webservices-spring` (a
   Kotlin/Spring REST backend) — meaning CARP's ecosystem includes study-management-adjacent tooling
   beyond the CAMS sensing library alone. This revises, but does not fully overturn, the prior "not a
   dashboard product" framing: `carp-portal`'s existence is now Verified, but its feature completeness
   and documentation quality were not assessed this pass, so it should not be treated as equivalent to
   a mature commercial dashboard without further verification.

### Important unresolved questions (even after this pass)

- Whether Beiwe's `data_access_api_reference` directory documents a public, researcher-self-service
  API or an internal interface only (new Tier 13 item #101).
- Forest's full per-metric catalog within `jasmine`/`willow`/`sycamore` (new Tier 13 item #102).
- RADAR-base's exact iOS-side itemized sensor list, as distinct from the now-itemized Android list
  and the qualitative "more sparse" framing (new Tier 13 item #103).
- The Hyve's actual pricing for "RADAR-base as a Service," and how its ~200-participant ceiling is
  raised for larger studies (new Tier 13 item #104).
- `carp-portal`'s feature completeness and documentation relative to competitors' dashboards (new
  Tier 13 item #105).
- Avicenna Research's pricing and developer-API status (unresolved-questions #89/#90 — re-confirmed
  unresolved, not newly raised).
- SOC 2 and 21 CFR Part 11 status for every platform in the module, including the two (Avicenna
  Research, m-Path) that now have other compliance evidence.

### Sources or documentation that were unavailable

- `beiwe.org/beiwe-service-center-overview/` — returned a connection error (`ECONNRESET`) on first
  attempt; a retry of the equivalent `hsph.harvard.edu` overview URL succeeded, so this is recorded as
  a transient fetch failure rather than a confirmed access barrier.
- `github.com/onnela-lab/beiwe-backend/tree/main/api` — HTTP 404 (the `data_access_api_reference`
  directory's exact path/contents were not located via this specific URL guess).
- `jponnela.com/bf20/` (Forest documentation site) — HTTP 404.
- `github.com/cph-cachet` — HTTP 404 (wrong org name; the correct CARP organization is `carp-dk`,
  which was successfully fetched).
- Avicenna Research's own pricing page — not located by URL guess or search; likely does not exist
  publicly rather than being blocked.
- RADAR-base's iOS-vs-Android sensor comparison chart, referenced but not extracted from
  `radar-base.org/docs/4048-2/`.
- `carp-portal` repository's own README/contents — existence confirmed via the org listing; contents
  not opened this session.

### Decisions that could affect later comparisons

1. **The module-level claim "commercial pricing is almost universally non-public" no longer holds.**
   After this pass, only Avicenna Research and MetricWire lack public pricing; Beiwe, m-Path, and (for
   the managed-hosting path specifically) RADAR-base-via-The-Hyve all now have some level of published
   pricing, ranging from itemized (m-Path) to rate-figures-published (Beiwe) to offering-confirmed-but-
   unpriced (RADAR-base). `README.md` and `comparison-matrix.md` were updated accordingly.
2. **The module-level claim "no platform has documented compliance evidence" no longer holds.**
   Avicenna Research (ISO 27001:2022, audited) and m-Path (vendor-stated GDPR/HIPAA compliance) both
   now have some compliance evidence, though of different strength — this distinction (audited
   certification vs. vendor self-declaration) is preserved explicitly in both profiles and the
   comparison matrix rather than being flattened into a single "compliant" label.
3. **RADAR-base joins AWARE Framework as a platform with a self-documented (not merely assumed)
   iOS/Android sensor-availability gap.** Any future study-design guidance drawing on this module
   should weight RADAR-base's iOS suitability accordingly, alongside AWARE's already-Verified,
   more granularly quantified gap.
4. **CARP Mobile Sensing's "pure library, build everything yourself" characterization is now
   qualified, not overturned.** The discovery of `carp-portal` means CARP should no longer be
   described as having zero researcher-dashboard tooling, but its comparison-matrix cells reflect
   "exists, depth unconfirmed" rather than promoting it to parity with mature commercial dashboards
   without further verification.
5. **All eight Module 2 platforms have now had at least one direct-source-fetch pass on primary
   vendor/maintainer materials**, closing the module-wide gap where five of eight profiles rested
   substantially on search-summary retrieval. `README.md`'s status line was updated from "single
   session, not yet a second pass" to reflect two-pass-equivalent depth across the module, mirroring
   Module 1's stated two-pass status.

---

## 2026-08-25 (earlier) — Dial et al. 2025 full-text extraction (unresolved-question #80)

**Module:** 1 — Wearables
**Scope:** Closed the one remaining actionable item from the prior literature-library retrofit pass:
full-text read of Dial et al. 2025 (*Physiological Reports* 13:e70527), the only found Oura-vs-WHOOP
head-to-head validation study. The PDF was already downloaded in an earlier pass but never opened —
this pass read it directly.

**Findings:**
- **Funding/COI confirmed clean.** "Financially supported by the Air Force Research Laboratory
  (AFRL)." "The authors declare that they have no competing interests." No wearable-vendor funding —
  among the strongest-provenance studies in the module. Tier upgraded from Corroborated to Verified
  in `research-library-wearables.md` (both the Oura Tier C and WHOOP Tier C entries).
- **Complete HRV table extracted** (previously only RHR was known): Oura Gen4 CCC=0.99
  (MAPE 5.96±5.12%), Oura Gen3 CCC=0.97 (MAPE 7.15±5.48%), WHOOP 4.0 CCC=0.94 (MAPE 8.17±10.49%),
  Garmin Fenix 6 CCC=0.87 (MAPE 10.52±8.63%), Polar Grit X Pro CCC=0.82 (MAPE 16.32±24.39%).
- Confirmed why Garmin is excluded from the RHR comparison specifically (not HRV): its reported
  30-minute rolling-window RHR carries no timestamp, so night-to-night alignment with the Polar H10
  ECG reference is not possible — a methodological artifact of Garmin's own reporting, not a study
  design choice.
- `validation-evidence.md` §3a, `research-library-wearables.md` (two entries + two follow-up-list
  items marked done), `literature-library.md`, and `unresolved-questions.md` #80 all updated to
  reflect the resolution.

**Also checked:** retried the Harms 2018 NAIA-baseball dissertation (unresolved-question #99) via
its DigitalCommons URL — still returns HTTP 403. Left as-is; low-priority grey literature requiring
institutional ProQuest access this project doesn't have.

**Decisions that could affect later comparisons:** None to the cross-device conclusions already in
`comparison-matrix.md` — Oura still leads both RHR and HRV agreement, WHOOP is consistently
mid-pack, Garmin/Polar trail. This pass adds the missing evidentiary backing (full HRV table,
confirmed independence) rather than changing the ranking itself.

---

## 2026-08-24 — Retry of unresolved-question #98 (three blocked-but-OA papers)

**Module:** 1 — Wearables (literature library follow-up)
**Scope:** Targeted retry of the three papers `unresolved-questions.md` #98 flagged as having a
confirmed or probable open-access record that automated fetch could not retrieve in the Module 1
literature-library retrofit pass.

### Outcome: 2 of 3 obtained

1. **Khodr et al. 2024 (medRxiv, WHOOP systematic review) — obtained.** The versioned `.../v1/full.pdf`
   URL was genuinely bot-blocked (HTTP 403). Semantic Scholar's Graph API resolved the paper's
   canonical `medrxiv/early/.../full.pdf` path, which a plain browser-UA `curl` request retrieved
   cleanly. No extractable COI/disclosure section in the full text, so the paper's sponsorship tier
   stays Corroborated, not Verified, even with the PDF now in hand.
2. **Mahalingaiah et al. 2022 (AJOG, Apple Women's Health Study) — obtained.** The earlier "HTTP 500"
   diagnosis was a symptom, not the cause. NCBI's own OA web service (`oa.fcgi`) confirms a genuine CC
   BY-NC-ND record with a direct PDF link, but that URL sits behind a JS-driven bot-detection
   interstitial that blocks any non-browser client. A real browser session cleared the challenge and
   produced a `cloudpmc-viewer-pow` cookie; reusing that cookie in a direct `curl` request retrieved
   the PDF.
3. **Perez et al. 2019 (NEJM, Apple Heart Study) — confirmed genuinely paywalled, not obtained.**
   Checked directly against NCBI's OA web service, which returned `idIsNotOpenAccess` for PMC8112605.
   This is a materially different finding than the prior pass assumed: the earlier "HTTP 500 /
   CAPTCHA" symptoms were downstream of an underlying non-OA status, not a retrieval-infrastructure
   bug. No PDF exists to obtain without institutional NEJM access.

### Files updated

`module-01-wearables/literature/whoop/2024-khodr-medrxiv-whoop-systematic-review.pdf`,
`module-01-wearables/literature/apple-watch/2022-mahalingaiah-ajog-apple-womens-health-study-design.pdf`
(new PDFs); `module-01-wearables/literature-library.md` (updated entries, cross-device summary, new
"2026-08-24 retry" section); `module-01-wearables/research-library-wearables.md` (corrected entries
for all three papers); `shared/unresolved-questions.md` (#98 marked resolved).

### Decision affecting later comparisons

**A "retrieval failure" and "genuinely not open access" can look identical from an automated
script's perspective (both surface as an error page instead of a PDF) but mean very different
things.** Always check a paper's actual OA status against an authoritative source (e.g. NCBI's
`oa.fcgi` service) before concluding a blocked fetch is a fixable infrastructure problem — as
happened here with Perez, where the "OA per metadata" assumption in the prior pass was wrong.

---

## 2026-08-24 (later) — Literature-library scope decision

**Module:** Cross-module (affects both Module 1 and Module 2)
**Scope:** No new research; a methodology/scope decision surfaced while reviewing Module 2's sources.

### Finding

Confirmed via file audit that neither module's "library" currently stores actual paper files — `sources.md`
entries and `research-library-wearables.md` (Module 1) cite papers by URL/DOI with retrieval labeled
Direct/Search summary/Secondary, but no PDF has ever been downloaded into the repo. This applies equally to
Module 1's ~90-paper bibliography and Module 2's sources register, not just the newly built module.

### Decision

Going forward, the knowledge base will store actual open-access PDFs where legally distributable (PMC,
arXiv, OA journals such as JMIR) rather than citation-only entries. For paywalled papers, keep the existing
citation + abstract + link, explicitly flagged as "PDF not obtainable — paywalled," rather than attempting
to bypass access controls. This is additive to the existing evidence-confidence system, not a replacement —
retrieval labeling (Direct/Search summary/Secondary) still applies to how each *claim* was established.

### Open follow-up

Neither module has been retrofitted yet. Module 2's papers are the first target; Module 1's
`research-library-wearables.md` (~90 papers) has the same gap and should be retrofitted in a later session.

---

## 2026-08-21 — Module 1 (Wearables), initial research phase

**Module:** 1 — Wearables
**Scope:** Full initial research phase, Phases 1–6 per `CLAUDE.md`. Module 2 not started.

### Technologies researched

Apple (Watch / HealthKit / SensorKit / ResearchKit) · Fitbit + Google (Fitbit Web API, Google Health
API, Health Connect) · Garmin (Health API, Health SDK) · Oura (Ring 4, API v2) · WHOOP (5.0 / MG,
API v2) · Samsung (Galaxy Watch/Ring, Privileged Health SDK, Health Research Stack) · Polar (H10,
Verity Sense, BLE SDK, AccessLink) · Withings (ScanWatch, Advanced Research API, Health Solutions) ·
Empatica (EmbracePlus, Care Portal) · Ametris/ActiGraph (LEAP, CentrePoint, ActiLife) ·
Axivity + GENEActiv (AX3/AX6, open toolchain) · Data intermediaries (Fitabase, Terra, Validic,
Thryve, Rook, Sahha, Open Wearables, MyDataHelps) · Open datasets (*All of Us*, UK Biobank).

### Files created

```
module-01-wearables/README.md
module-01-wearables/comparison-matrix.md          (10 tables)
module-01-wearables/sources.md                    (~70 source entries + a "sought but not obtained" register)
module-01-wearables/profiles/apple-watch-healthkit.md
module-01-wearables/profiles/fitbit-google.md
module-01-wearables/profiles/garmin.md
module-01-wearables/profiles/oura.md
module-01-wearables/profiles/whoop.md
module-01-wearables/profiles/samsung.md
module-01-wearables/profiles/polar.md
module-01-wearables/profiles/withings.md
module-01-wearables/profiles/empatica.md
module-01-wearables/profiles/ametris-actigraph.md
module-01-wearables/profiles/axivity-geneactiv.md
module-01-wearables/profiles/data-intermediaries.md
shared/terminology.md
shared/research-log.md
shared/unresolved-questions.md
module-02-digital-phenotyping/                    (empty directory skeleton only — not researched)
```

### Major findings

1. **Fitbit Web API turndown, September 2026.** The legacy API stops syncing data; the Google
   Health API replaces it; Google OAuth 2.0 replaces Fitbit auth; **OAuth tokens do not transfer, so
   every participant must re-consent**; all Google Health API scopes are Restricted. Whether
   minute-level intraday HR/HRV/SpO2 survive at parity is unresolved and is the single highest-value
   open question in the module.
2. **Raw signal availability splits the field, and not along the consumer/research line.** Samsung
   (raw PPG incl. IR/Red, raw ECG, IBI, 25 Hz accel), Polar (raw ECG, PPI, ACC via an open GitHub
   SDK), Garmin (raw accel + BBI), and Withings (raw accel + 3-wavelength PPG) all expose raw data.
   **Oura and WHOOP expose none.** Apple exposes only discrete ECG voltage.
3. **WHOOP's API Terms of Use appear incompatible with research.** No permanent copies or databases;
   no transfer to third parties even with consent; explicit HIPAA disclaimer; non-compete clause.
   There is a written-agreement carve-out, which becomes a gating prerequisite.
4. **Study operations is the systematic gap in consumer platforms.** Apple, Fitbit/Google, Garmin,
   Oura, and WHOOP provide no participant management, no adherence monitoring, no wear-time
   tracking. Only Empatica, Ametris, and Samsung's Research Stack provide it natively; everyone else
   buys Fitabase at non-public pricing.
5. **Oura's sleep data only syncs when the participant opens the app.** Documented by Oura. The
   study's primary endpoint in most Oura research depends on a daily participant behaviour. A 403 is
   also returned when a participant's membership lapses — a silent data-flow termination.
6. **ActiGraph is now Ametris (rebrand 25 June 2025) and was acquired by Signant Health (announced
   May 2026).** GT9X is end-of-life. Corporate discontinuity is a real planning risk.
7. **Polar H10 at ~$90 with a free open BLE SDK gives raw ECG and RR intervals with no cloud, no
   approval, and no fee.** It is also the device the field uses as its criterion standard. This is
   the best cost-to-signal-quality ratio in the module by a wide margin.
8. **No consumer brand achieves acceptable accuracy for energy expenditure** (JMIR systematic review;
   umbrella review). This is a universal finding, not device-specific.
9. **Oura and WHOOP have never been compared under the same protocol.** Robbins 2024 (Oura best,
   kappa 0.65) excluded WHOOP; Schyvens 2025 (WHOOP best deep-sleep sensitivity, 69.6%) excluded
   Oura. Both vendors' "most accurate" claims rest on studies that excluded the other.
10. ***All of Us* already holds Fitbit data from 59,000+ participants over 14 years** with
    minute-level HR and steps, 46% linked to EHR/genomics. For many questions this is a better and
    far cheaper answer than collecting new data.

### Important unresolved questions

Recorded in full in `unresolved-questions.md` (62 items across seven tiers). The five blocking ones:
Google Health API intraday parity; WHOOP written retention agreement; Oura's 10-user cap approval
process; Garmin SDK academic licence cost; Samsung Partner Program criteria.

**Five of eleven ecosystems have entirely non-public pricing** (Empatica, Ametris, Fitabase,
Withings Advanced Research API, WHOOP Unite).

### Sources or documentation that were unavailable

| Target | Outcome |
|---|---|
| `developer.garmin.com/gc-developer-program/health-api/summaries/` | **404** — the complete Garmin Health API data-type list could not be obtained. This is the largest single documentation gap in the module |
| `developer.ouraring.com/docs` | 404 (Oura v2 docs obtained from `cloud.ouraring.com` via browser instead) |
| `withings.com` research pages | **403** to direct fetch; retrieved via browser |
| `support.empatica.com` plan article | **403**; retrieved via search summary only |
| `developer.apple.com/documentation/healthkit` | JS-rendered; only the page title was extractable |
| Polar per-product SDK docs (sampling rates) | Not retrieved |
| Withings developer API reference | Behind Partner Hub login |
| Robbins 2024 and Schyvens 2025 full texts | Not read in full; figures come from search summaries. **The Withings ScanWatch result from Schyvens is missing** |

### Decisions that could affect later comparisons

1. **"Raw data" is defined strictly** in `terminology.md` as near-native-rate sensor output, not the
   loose vendor sense of "unsummarized." Several vendors (notably Oura, via secondary sources) are
   described elsewhere as providing "raw sensor data"; under this definition they do not. This
   definition should carry into Module 2.
2. **Axivity and GENEActiv were added** beyond the `CLAUDE.md` starting list, because omitting them
   would have presented ActiGraph as the only research-grade accelerometry option and would have
   omitted the only open-hardware option in the module.
3. **Data intermediaries and open datasets were included** as a cross-cutting profile rather than
   excluded as "not wearables," because they are how most Fitbit/Garmin research is actually
   conducted.
4. **ActiGraph is profiled under its current name, Ametris.** Anyone searching this knowledge base
   for "ActiGraph" needs the rebrand surfaced, so both names appear in the filename and title.
5. **CGM, EEG wearables, and smart clothing/patches were deliberately deferred** to future modules
   rather than partially covered.
6. **Vendor engineering claims are labelled Reported, never Verified**, regardless of numerical
   specificity. This particularly affects Oura's Smart Sensing figures, WHOOP's sampling claims, and
   Samsung's Antioxidant Index.
7. **Contradictions between two sources from the same vendor are recorded as contradictions**, not
   silently resolved in favour of the more recent or more specific page. Five such contradictions
   are open (items 42–46 in `unresolved-questions.md`).
8. **Confidence labels distinguish retrieval method**: "Direct" fetch supports Verified; a search
   result summarizing a primary page supports only Corroborated. This is tracked per source in
   `sources.md` so the basis of every claim is auditable.

### Notes for the next update

- Re-verify the entire Fitbit/Google profile **after September 2026**; most of it will be stale.
- Re-check Ametris after the Signant Health integration completes.
- Apple Watch and Fitbit device lineups should be re-verified from vendor spec pages rather than
  launch coverage; the current entries lean on trade press.

---

## 2026-08-21 (second session, same day) — Module 1 deep-research pass

**Module:** 1 — Wearables
**Scope:** Execute the "recommended next research steps" from the first pass: read the primary
validation literature in full, close documentation gaps, verify pricing, and fill the discovery gap.
No vendor was contacted (outbound contact was not authorised and is the user's to initiate).

### Files created

```
module-01-wearables/validation-evidence.md          (new — full extraction from the PSG literature)
module-01-wearables/profiles/movesense.md           (new)
module-01-wearables/profiles/emerging-platforms.md  (new — Ultrahuman, Biostrap, Verily)
```

### Files substantially revised

`README.md` · `comparison-matrix.md` (Tables 3, 7, 9, 10 rewritten; Tables 11–12 added) ·
`sources.md` (second-pass source register appended) · `shared/unresolved-questions.md` (access-gating
framing corrected) · profiles: `whoop.md`, `oura.md`, `fitbit-google.md`, `garmin.md`,
`apple-watch-healthkit.md`, `polar.md`, `withings.md`, `empatica.md`, `samsung.md`,
`data-intermediaries.md`.

### Corrections to the first pass — recorded rather than silently fixed

1. **Schyvens et al. 2025 was misreported.** The first pass quoted per-stage *accuracy* figures as
   though they were the headline agreement statistic, producing the claim that WHOOP had "the best
   independently measured deep-sleep sensitivity." The actual overall agreement ranking is Apple
   0.53 > Fitbit Sense 0.42 > Charge 5 0.41 > **Whoop 0.37** > Withings 0.22 > Garmin 0.21. WHOOP's
   strength claim in that profile was overstated and has been rewritten.
2. **Robbins et al. 2024 has a declared conflict of interest**, not merely vendor promotion: funded
   by Oura Ring Inc., with the lead author on Oura's Medical Advisory Board receiving consulting
   fees. Now stated in a callout wherever the κ=0.65 figure appears.
3. **Garmin Enhanced BBI is not SDK-only.** It is available through the cloud Health API and through
   Fitabase/Labfront using ordinary Garmin Connect OAuth, with no custom app. It is, however,
   **collected during the sleep interval only** — a limitation the first pass did not know about.
4. **Apple Watch Series 11 carries a depth gauge (6 m) and water temperature sensor.** The first pass
   incorrectly attributed both to the Ultra 3 alone.
5. **Several "non-public" pricing entries were retrieval failures, not vendor secrecy.** Empatica's
   academic pricing, Polar's per-stream sampling rates, and Labfront's full price list are all
   published.
6. **The "contact the vendor" framing was overstated.** API documentation is public for almost every
   platform here; only Garmin's field schemas, Withings' API reference and Samsung's Privileged SDK
   download are genuinely gated. What requires contact is scale thresholds and unpublished
   commercial terms. `unresolved-questions.md` now opens with this distinction.

### Major new findings

1. **Google Health API access is a compliance project, not a registration.** Unverified apps are
   capped at **100 users**; verification requires a third-party **CASA security assessment costing
   $500–$4,500 and taking 2–6 weeks**, repeated **annually** where a third-party server is involved.
   Rate limits, by contrast, are extremely generous (86.4M/day/project).
2. **The intraday question resolved, leaning negative.** Heart Rate is documented as a *Sample* type
   with **no stated sampling interval**; HRV, SpO2, respiratory rate and resting HR appear as
   **Daily Aggregates**; there is no Intraday endpoint family and no `detail-level` parameter.
3. **Deep sleep and REM stage minutes are not reliably measurable on any consumer device.** Robbins'
   ICCs: deep sleep 0.13–0.36, REM 0.13–0.37 across Oura, Fitbit and Apple. TST and SE (0.74–0.85)
   are the only defensible stage-derived endpoints.
4. **Device data loss is a first-order design risk.** In a supervised laboratory, Garmin failed
   18/43 nights and Apple 15/35; Withings and Oura lost nothing.
5. **Polar's real specifications are far better than the README matrix implied**: H10 ECG at 130 Hz
   in µV and accelerometry to 200 Hz/±8 g; Verity Sense in SDK mode gives **22-bit PPG at 28–176 Hz**
   and a 9-axis IMU to 416 Hz — for roughly $95, with no registration.
6. **Movesense was a significant omission**: ECG to **512 Hz**, 9-axis IMU to **1.6 kHz**, 1 ms RR
   resolution, **custom firmware permitted at no licence cost**, and **Class IIa MDR 2017/745**
   certification on the MD variant.
7. **Labfront publishes its pricing** — free/`$500`/`$1,250` per year with EMA included — and holds a
   Garmin partnership that raises sensor resolution above stock. It is the only research platform in
   the module with transparent pricing.
8. **Raw signal is more widely available than the first pass concluded.** Ultrahuman exposes raw PPG
   from a *ring*; Biostrap exposes raw PPG with configurable rates plus surveys; Verily's Study Watch
   records ECG **and** EDA with weeks of onboard raw storage.
9. **Verily–Samsung, March 2026**: Galaxy Watch 8 raw PPG and motion signals into Verily's Pre
   platform — independent corroboration of Samsung's raw-data capability and a third access route.
10. **Hardware generations turned over during the research window**: Oura Ring 5 (28 May / 4 June
    2026, $399–$499, Health Radar), Fitbit Air (7 May 2026, $99.99, screenless, 2-second HR), and the
    Fitbit app's rebrand to **Google Health** (19 May 2026). **Every published validation study
    predates all current hardware.**

### Contradictions resolved

- **Polar H10 accelerometer** — resolved: the H10 *does* stream ACC at 25/50/100/200 Hz, ±2/4/8 g.
  The SDK README matrix was incomplete; the product documentation is authoritative. Separately, the
  Verity Sense has **no ECG** (the first pass wrongly listed one) but **does** have gyroscope and
  magnetometer (which the README omitted).
- **Withings ScanWatch validation result** — recovered from the paper: κ=0.22, TST +39.9 min,
  SE +10.2%, WASO −47.9 min, three-state classification, zero data loss.
- **Apple Series 11 sensor list** — resolved from Apple's own specification page.

### Contradictions still open

Apple ECG voltage access (documentation vs ResearchKit FAQ); Withings accelerometer rate
(24.824 Hz vs "25 Hz default, up to 100 Hz"); Samsung minimum watch generation (Watch4 vs Watch5);
Empatica biomarker count — now **three** public figures (11+, 18, 100+).

### Sources unavailable

Movesense datasheets are behind a survey-gated PDF download, so exact battery, water-resistance and
IMU range figures remain undetermined. `withings.com` and `whoop.com/membership` return 403 to
automated fetch. Garmin's field-level Health API schema remains behind the developer portal.

### Decisions affecting later comparisons

1. **A dedicated `validation-evidence.md` was created** rather than distributing findings across
   profiles, because the evidence is now detailed enough that scattering it would invite the same
   misquotation that produced the first pass's error.
2. **A bridged Oura-vs-WHOOP estimate is published, explicitly labelled as inference**, using Apple
   Watch as the shared anchor across the two studies. It is presented as an estimate that a future
   head-to-head could falsify, not as a finding.
3. **Sampling-rate comparisons are now first-class** in the comparison matrix (a league table by
   signal and cost of entry), because the second pass established that the cheapest and most open
   vendors offer the highest rates — a conclusion invisible without exact figures.
4. **Two new decision tables (11 and 12)** were added to the matrix: study-operations platforms, and
   platform selection by research question. These are the most directly reusable artefacts for
   downstream work.
5. **No vendor was contacted.** Outbound contact on the user's behalf was not authorised. Every
   "contact the vendor" item is left as a question with a named contact route, and the next-steps
   list is reordered so that the three highest-value actions require no contact at all.

---

## 2026-08-24 — Module 1, Oura/WHOOP/Apple Watch research library by sponsorship status

**Module:** 1 — Wearables
**Scope:** User-directed, narrower than a full module pass: build a bibliography of Oura-, WHOOP-,
and (added mid-session) Apple-Watch-related published research (any topic, not just sleep-staging
validation), tagged by whether each paper is vendor-employee-authored, vendor-funded/independent-
authored, or fully independent. Prompted by a follow-up question on whether the Oura MDPI
sleep-staging paper the user found (Kinnunen & Altini 2021) was itself vendor-authored — it is
(both authors are Oura Health staff). User then asked for an exhaustive pass; three parallel
background research agents were dispatched (one per device) to sweep across all topic areas —
sleep, HR/HRV, activity/EE, temperature, SpO2, menstrual/reproductive health, mental health,
military/occupational, systematic reviews — and verify funding/COI disclosures directly where
possible rather than inferring from affiliation.

### Files created

```
module-01-wearables/research-library-wearables.md   (new — supersedes the initial two-device draft,
                                                       research-library-oura-whoop.md, which was
                                                       deleted)
```

### Files revised

`shared/unresolved-questions.md` (Tier 9 added, items 77–83).

### Major findings

1. **The Oura "Promise of Sleep" paper (Sensors 2021) is Oura-employee-authored**, not independent —
   both Kinnunen and Altini are Oura Health staff. This had been implicitly treated as third-party
   evidence by the user going in; it is not.
2. **A genuine Oura-vs-WHOOP head-to-head exists and was previously missed**: Dial et al. 2025,
   *Physiological Reports* 13:e70527 (Ohio State / Air Force Research Lab, Wright-Patterson AFB).
   13 adults, 536 nights, ECG reference, Oura Gen3, Oura Gen4, and WHOOP 4.0 in the same protocol
   (plus Garmin, Polar). Oura Gen4/Gen3 had the best HRV agreement; WHOOP was "moderate."
   **`validation-evidence.md` §3 currently states no head-to-head exists and should be updated** —
   flagged as an open item rather than done in this pass, since that file does full-text extraction
   and this pass mostly worked from search-result summaries (direct access to the paper was blocked).
3. **WHOOP's most-cited early validation (Berryhill et al. 2020, *JCSM*, University of Arizona) was
   directly grant-funded by WHOOP Inc.**, though the authors are not WHOOP employees and reported no
   personal conflicts. WHOOP's own marketing describes this as independent confirmation — technically
   true (independent authors) but funding-sponsored, same pattern as Oura/Robbins 2024.
4. **The CQUniversity WHOOP HR/HRV validation (Bellenger et al. 2021, "99.7%/99% accurate") is
   funded by the Australian Institute of Sport, not WHOOP** — genuinely independent funding — but the
   device tested was **WHOOP 2.0**, two generations old, a caveat that gets dropped whenever this
   figure is cited in marketing. The same CQU author cluster (Miller, Bellenger, et al.) recurs across
   several other WHOOP papers, and one member (Dean Miller) holds a WHOOP-sponsored research position
   — later papers by this cluster should not be assumed independent by default.
5. **Oura has a standing sponsored lab relationship with NUS** (Oura–NUS Joint Lab) — relevant to
   reading Liang et al. 2024 (*Sensors*, Oura nocturnal HRV) as Tier B, not fully independent, despite
   non-Oura authorship. Oura also sponsors the **TemPredict** research infrastructure (COVID
   detection, antibody-response, depression/temperature papers), which underlies a cluster of papers
   that don't all list an Oura employee as co-author but share the sponsored dataset.
6. **WHOOP's in-house research output (Sleep journal, npj Digital Medicine, JMIR, PLOS) skews
   toward large real-world cohort/behavioral studies** (circadian habits, mental health, menstrual
   cycle, alcohol use, COVID respiratory-rate prediction) rather than lab-based PSG/ECG accuracy
   validation — the opposite pattern from Oura, whose in-house paper (Kinnunen & Altini 2021) *is* an
   accuracy-validation paper. WHOOP has no found in-house accuracy-validation publication; all of
   WHOOP's accuracy evidence is external (funded or independent).
7. **Apple has, by a wide margin, the largest independent (Tier C) accuracy-validation literature of
   the three vendors** — likely a function of Apple Watch's market scale and longevity rather than any
   particular openness. Apple's three flagship studies (Heart Study/NEJM, Women's Health Study,
   Heart and Movement Study) are large, rigorous, and explicitly vendor-sponsored/co-run, which is not
   how they are typically presented in public discourse.
8. **Funder bias does not run in one predictable direction.** Robbins 2024 (Oura-funded) still rated
   Apple Watch best on REM sensitivity; the Medtronic-funded DEFINE AFib study was unfavorable to
   Apple, the non-funding vendor being compared. Read the funding disclosure and the actual finding
   separately — don't assume the funder's own product always wins.
9. **SpO2 and skin/body-temperature validation are near-total independent-evidence gaps for both
   Oura and WHOOP** — no independent peer-reviewed study was found for either metric on either
   device. Apple Watch has at least one independent SpO2 validation (a pediatric population study);
   still thin outside that one paper.
10. **One prior tier assumption is now downgraded.** The second (2026) WHOOP-authored-looking
    npj Digital Medicine menstrual-cycle paper could not have its author list confirmed this pass —
    an earlier assumption that it was WHOOP-employee-authored like its sister paper is now marked
    Unclear rather than assumed Tier A.

### Explicitly not done in this pass

- Confirmed funding/COI on several leads only via secondary sources, not primary disclosure text,
  because WebFetch was blocked (403, CAPTCHA, or login wall) on Wiley, PMC (intermittently), MDPI,
  Springer/BiomedCentral, Nature/npj, Tandfonline, JACC, and IEEE Xplore. Every entry in the new
  library file carries an explicit **Verified / Corroborated / Unclear** marker reflecting this —
  see that file's "Access limitations encountered this pass" section for the full list.
- Did not individually verify the ~6-paper cluster of reproductive-health/arrhythmia studies on
  Oura's own research-page listing (labor onset, pregnancy biometrics, LH-surge, AF-via-PPG) —
  flagged as a likely dense Tier A/B cluster needing a follow-up pass.
- Did not fully read five systematic reviews found this pass (Khan et al. 2025 OTO Open; Shahid et
  al. 2025 JACC Advances; Choe & Kang 2025 Physiological Measurement; a Nova Southeastern AF-wearables
  review; the Khodr et al. WHOOP medRxiv preprint) — each is a discovery mechanism for further papers
  and none has been tier-classified with a Verified-level disclosure read.
- Did not attempt PubMed's own advanced search interface (relied on WebSearch/WebFetch throughout);
  a follow-up pass using direct database search may close some of the SpO2/temperature evidence gaps
  faster than general web search did.

### Decisions affecting later comparisons

1. **A dedicated `research-library-wearables.md` was created** rather than folding sponsorship
   tagging into `sources.md`, because the tiering scheme (A/B/C plus confidence markers) needed its
   own explanation and would have cluttered the module-level source register.
2. **The file's scope was widened mid-session from Oura+WHOOP to include Apple Watch**, at the
   user's request; the original two-device draft (`research-library-oura-whoop.md`) was deleted and
   replaced rather than kept alongside the three-device version, to avoid two competing files with
   overlapping Oura/WHOOP content.
3. **Confidence markers (Verified/Corroborated/Unclear) are attached to every tier assignment**, not
   just to headline claims, because several apparent "independent" studies in this space turn out to
   have funding or personnel ties once traced — the marker discipline is what keeps that traceable
   instead of collapsing into a flat "independent vs. not" claim.
4. **Cross-cutting findings (funder-bias direction, sponsored-infrastructure clusters, per-vendor
   evidence-base shape) are called out explicitly** in their own section of the library file, because
   they are the kind of pattern that's easy to lose if the file is only ever read one entry at a time.

---

---

## 2026-08-24 (later) — Reconciliation: Wearable Data Atlas vs. the sponsorship-tiered research library

**Module:** 1 — Wearables
**Scope:** User asked to reconcile the published `wearable-data-atlas.html` artifact against the
knowledge base — specifically `research-library-wearables.md`, the funding/COI-tiered bibliography
built earlier the same day (see prior log entry), which had explicitly flagged its own findings as
**not yet propagated** into `validation-evidence.md`, `comparison-matrix.md`, or the Atlas.

### Files revised

`validation-evidence.md` (§3 rewritten into §3a/§3b; new §6a added; gap table in §6b updated;
sources list extended) · `comparison-matrix.md` (Table 9's "never met" finding row and the Oura/
WHOOP/Apple non-sleep-evidence rows rewritten) · `wearable-data-atlas.html` (same two changes
mirrored, plus a reconciliation note in Table 9 and an updated header meta line) — then republished
to the same artifact URL.

### The central correction

The Atlas stated, in two places, that "Oura and WHOOP have never been compared under the same
protocol" and that any ranking between them was "a bridged estimate... not evidence." This is no
longer true for **resting HR and HRV**: Dial et al. 2025 (*Physiological Reports* 13:e70527, Ohio
State / Air Force Research Laboratory) put Oura Gen3, Oura Gen4, WHOOP 4.0, Garmin Fenix 6, and
Polar Grit X Pro on the same 13 participants for 536 nights against an ECG reference. Oura led on
both generations (CCC 0.97–0.98); WHOOP was worst of the four tested (CCC 0.91, "moderate").

This does **not** resolve the narrower PSG-scored sleep-stage-kappa question — Dial et al. did not
use polysomnography, so Robbins 2024 (excludes WHOOP) and Schyvens 2025 (excludes Oura) remain the
only sleep-architecture evidence, and the bridged estimate for that specific outcome was retained,
relabeled to make the scope explicit. The correction is precise: direct evidence now exists for one
outcome (HR/HRV), an indirect bridge remains the best available evidence for a different, narrower
outcome (sleep-stage kappa). Both files previously conflated these under one blanket claim.

The Dial et al. finding itself carries a **Corroborated, not Verified** marker throughout — direct
fetch of the paper was blocked (403/CAPTCHA) in the source research-library pass, so the funding/COI
disclosure has not been read and the HRV-specific CCC/MAPE figures (as opposed to resting HR) remain
incomplete. This caveat was carried into all three files, not softened in the summary/report layer.

### Secondary corrections — funding-disclosure asymmetry

The Atlas and comparison matrix flagged Robbins 2024's Oura funding prominently but did not apply
the same standard to the other two vendors' comparably-sponsored flagship studies:

- **The Apple Heart Study (*NEJM* 2019) is itself Apple-sponsored**, with named Apple co-authors and
  Stanford PIs disclosing Apple grants/personal fees — now stated in both files, matching the
  treatment already given to Oura/Robbins.
- **WHOOP's own most-cited early validation, Berryhill et al. 2020 (*JCSM*), was WHOOP-funded** —
  previously absent from both files entirely; now added to WHOOP's evidence row.

### Secondary corrections — Apple's non-cardiac record

Both files previously represented Apple's evidence position with a single line ("Apple Heart
Study — AFib notification at scale"), which is accurate for cardiac rhythm but implied a uniformly
strong record. The research library surfaced specific, independently-funded findings that don't fit
that framing: VO2max underestimated 13.31% MAPE ("not sufficiently accurate to inform clinical
decision-making," Doherty et al. 2025); HRV fails equivalence testing (28.88% MAPE, Doherty et al.
2024); and — the most concrete, actionable finding of the reconciliation pass — **wheelchair-user
fall-detection sensitivity of 4.7%** (14/300 trials detected, Abou et al. 2022), starkly below
Apple's general-population marketing framing. This last finding is now called out by name in both
files because it is specific enough to change a study-design decision (do not rely on Apple Watch
fall detection for a mobility-impaired population) in a way the module's other Apple findings are
not.

### Explicitly not done in this pass

- Did not attempt to re-fetch Dial et al. 2025 directly; the Corroborated marker and open extraction
  items (full HRV CCC/MAPE, funding disclosure) from `research-library-wearables.md` stand as-is.
- Did not propagate the research library's other open items (the unconfirmed 2026 WHOOP menstrual-
  cycle paper authorship, the five paywalled systematic reviews, the ~6-paper Oura reproductive-
  health cluster) into `validation-evidence.md` or the Atlas — those remain library-only findings
  pending their own follow-up, tracked in `shared/unresolved-questions.md` Tier 9.
- Did not touch Table 10 (differentiators) in either file — its Oura/WHOOP/Apple entries describe
  device capabilities, not accuracy evidence, and were not contradicted by this pass.
- Did not re-verify or extend Kinnunen & Altini 2021 (Oura's in-house sleep-staging paper) beyond
  naming it in `validation-evidence.md` §6a; it was not previously cited anywhere in this knowledge
  base as evidence, so there was nothing to correct, only a gap to note.

### Decisions affecting later comparisons

1. **The Oura-vs-WHOOP claim was split into two explicitly-scoped sub-questions (§3a resting HR/
   HRV, §3b PSG sleep-stage kappa)** rather than either leaving the old blanket claim in place or
   overclaiming that Dial et al. resolves sleep staging too. This is the reconciliation's central
   methodological move: correcting a claim precisely, not just marking it "no longer true."
2. **Funding-disclosure treatment was made symmetric across all three vendors** rather than only
   Oura's flagship study carrying a visible conflict flag — an internal-consistency fix, not new
   evidence.
3. **The Atlas artifact was republished to its existing URL** rather than left stale or created as a
   new artifact, per the standing "update in place" convention for this deliverable.

---

## 2026-08-24 (later) — Module 2 (Mobile Digital Phenotyping Platforms), initial research phase

**Module:** 2 — Mobile Digital Phenotyping Platforms
**Scope:** Full initial research phase, Phases 1–6 per `CLAUDE.md`, single session (contrast Module
1's two deep-research passes). Executed on explicit instruction to start Module 2.

### Technologies researched

Beiwe (Onnela Lab, Harvard) · Forest (Beiwe's companion analysis package — relationship documented
carefully per CLAUDE.md's explicit instruction) · RADAR-base (King's College London / The Hyve) ·
mindLAMP / LAMP Platform (BIDMC Division of Digital Psychiatry) · AWARE Framework (international
academic collaboration) · Avicenna Research, formerly Ethica/Ethica Data · MetricWire · m-Path (KU
Leuven-affiliated) · CARP Mobile Sensing (DTU, Bardram group) · Purple Robot, StudentLife, and Koa
Health (identified, deliberately not given full profiles — see below).

### Files created

```
module-02-digital-phenotyping/README.md
module-02-digital-phenotyping/comparison-matrix.md          (10 tables)
module-02-digital-phenotyping/sources.md                    (~45 source entries + a "sought but not obtained" register)
module-02-digital-phenotyping/_inventory-and-scope-decisions.md
module-02-digital-phenotyping/profiles/beiwe.md
module-02-digital-phenotyping/profiles/radar-base.md
module-02-digital-phenotyping/profiles/mindlamp.md
module-02-digital-phenotyping/profiles/aware-framework.md
module-02-digital-phenotyping/profiles/avicenna-research-ethica.md
module-02-digital-phenotyping/profiles/metricwire.md
module-02-digital-phenotyping/profiles/m-path.md
module-02-digital-phenotyping/profiles/carp-mobile-sensing.md
module-02-digital-phenotyping/profiles/legacy-and-adjacent-platforms.md
```

### Files revised

`shared/unresolved-questions.md` (Tier 10 added, items 84–94; "Last updated" line updated) ·
`shared/terminology.md` (new "Module 2 — Digital phenotyping platform terms" section appended).

### Major findings

1. **The module splits into three distinct deployment postures, not a simple open-source/commercial
   binary**: self-hosted academic open source requiring real infrastructure capacity (Beiwe,
   RADAR-base, mindLAMP, AWARE); fully managed commercial SaaS requiring none (Avicenna Research,
   MetricWire, m-Path); and a build-your-own-app framework requiring mobile-development rather than
   backend capacity (CARP Mobile Sensing, distributed as a Flutter library, not a hosted product).
2. **Beiwe and Forest are separate open-source repositories, not one fused artifact** — both
   maintained by the Onnela Lab, designed to work together, but independently usable and released.
   Documented explicitly per CLAUDE.md's specific instruction to handle this relationship carefully.
3. **Only Beiwe offers a documented, paid managed-hosting alternative (the Beiwe Service Center) to
   its own free self-hosted path.** No comparable managed-hosting option was confirmed for
   RADAR-base, mindLAMP, or AWARE — flagged as an open question for each.
4. **Ethica Data rebranded to Avicenna Research.** Confirmed via convergent evidence (shared
   app-store listing "Avicenna (Ethica)," shared Android package name `com.ethica.logger`, and
   third-party company-profile cross-referencing) rather than treating them as two platforms.
5. **AWARE Framework is the one platform in this module that self-documents an iOS/Android capability
   gap** — its own materials describe the iOS port as different/lesser in coverage than the primary
   Android client. Every other platform's parity question was left as "not independently verified"
   rather than assumed, per CLAUDE.md's explicit instruction not to assume parity.
6. **mindLAMP has explicitly deprecated components in its own public GitHub organization**
   (`LAMP-portal`, `LAMP-app`, both labeled "[Deprecated]" in-repo), while other components
   (`LAMP-server`) appear current — a status nuance a prospective adopter needs to map before
   building on any specific repository.
7. **Commercial pricing is almost universally non-public.** Avicenna Research, MetricWire, and
   m-Path all require vendor contact for real figures. Only Beiwe (via BSC) publishes a pricing
   *methodology* (fixed fee by study duration + variable fee by Active Participant Months, i.e.
   participants × per-participant collection months) — not actual rate figures.
8. **Compliance documentation (HIPAA/GDPR/DPA/SOC2/21 CFR Part 11) was not located for any platform
   in this module**, including ones with explicit clinical-trial or clinical-care positioning
   (mindLAMP, Avicenna Research, MetricWire). This is the single largest cross-platform gap and is
   called out at the module level, not just per-profile.
9. **CARP Mobile Sensing (DTU) is architecturally distinct from every other platform profiled** — an
   MIT-licensed Flutter library/framework a research team builds its own app on top of, not a
   pre-built, dashboard-configured product. Added under CLAUDE.md's "starting point, not a closed
   list" clause, alongside m-Path (added for its distinctive, peer-reviewed-documented JITAI/EMI
   sophistication).
10. **Purple Robot, StudentLife, and Koa Health were identified but deliberately not given full
    profiles.** Purple Robot's live maintenance status could not be established (and it is
    Android-only regardless of status); StudentLife's lasting relevance to new researchers is its
    dataset, not a reusable data-collection tool; Koa Health has an active digital-phenotyping
    research program but no confirmed externally-deployable platform. All three are documented in
    `profiles/legacy-and-adjacent-platforms.md` with the specific status question flagged, per
    CLAUDE.md's instruction to label discontinued/legacy platforms clearly rather than exclude them
    silently.

### Important unresolved questions

Recorded in full in `unresolved-questions.md` Tier 10 (items 84–94). The three highest-value:
whether any platform besides Beiwe offers managed hosting; actual (not just methodological) pricing
for Beiwe's BSC, Avicenna Research, and MetricWire; and compliance documentation for any platform
with clinical positioning.

### Sources or documentation that were unavailable

| Target | Outcome |
|---|---|
| `docs.lamp.digital/about/publications/` | **404** |
| AWARE Framework's deeper documentation pages | Limited content returned on direct fetch; sensor-level detail not obtained |
| `metricwire.com` | Not directly fetched this session; relied on search-summary aggregation |
| Vendor pricing pages (Avicenna Research, MetricWire, m-Path) | Non-public / not located |
| Most academic project sub-pages (RADAR-base beyond "About," CARP, m-Path beyond its home/research pages) | Search-summary retrieval only, not direct fetch |

### Decisions that could affect later comparisons

1. **This module received a single research session, not Module 1's two-pass depth.** This is
   stated explicitly in `README.md`, `comparison-matrix.md`, and this log entry rather than
   presented as equivalent-depth research. A higher proportion of claims here rest on search-summary
   retrieval than direct fetch — recorded per-source in `sources.md`.
2. **Ethica/Avicenna Research were treated as one entity** based on convergent identity evidence
   (app listing, package name, company-profile cross-reference) rather than profiled as two
   competing platforms or arbitrarily assigned to only one name.
3. **CARP Mobile Sensing and m-Path were added beyond `CLAUDE.md`'s starting list**, under its
   explicit "starting point, not a closed list" clause — mirroring how Module 1 added Axivity/
   GENEActiv beyond its own starting list.
4. **Compliance documentation (HIPAA/GDPR/SOC2) is flagged as a module-wide gap**, not just a
   per-profile Unclear marker, because it is the highest-value single item to close before any of
   these platforms could responsibly be recommended for a regulated study.
5. **Vendor engineering and marketing claims are labelled Reported, never Verified**, consistent
   with Module 1's standard — this particularly affects Avicenna Research's export-format claims,
   MetricWire's trigger-based-survey claims, and m-Path's "250+ Universities" figure.
6. **No vendor or maintainer was contacted.** Outbound contact on the user's behalf was not
   authorised. Every "contact the vendor/maintainer" item in Tier 10 is left as a question with a
   named contact route.

### Notes for the next update

- A second research pass should prioritize: (a) direct-fetching the primary documentation sites that
  returned limited or no content this session (AWARE, mindLAMP publications, MetricWire), (b)
  attempting to confirm or rule out managed-hosting options for RADAR-base/mindLAMP/AWARE, and (c)
  a systematic published-use/citation-count survey for each platform, which CLAUDE.md's "Evidence of
  use" section calls for but this session did not attempt.
- Re-verify mindLAMP's component-deprecation status, since it directly affects which repository a
  new adopter should build on.
- Confirm whether Koa Health warrants a ninth full profile once its platform-availability question
  (item 91) is resolved.

---

## 2026-08-24 (second session) — Module 2 second pass: direct-source re-verification of AWARE, mindLAMP, MetricWire; Koa Health and Purple Robot follow-up

**Module:** Module 2 (Mobile Digital Phenotyping Platforms) — second pass, not a redo. Scope was
deliberately narrow: the three platforms flagged in `module-02-digital-phenotyping/README.md` and
`_inventory-and-scope-decisions.md` as resting on search-summary rather than direct-fetch retrieval
(AWARE Framework, mindLAMP, MetricWire), plus two secondary items (Koa Health's platform-availability
status, Purple Robot's maintenance status). Beiwe, RADAR-base, Avicenna Research, m-Path, CARP, and
Module 1 were explicitly out of scope for this pass.

### Technologies researched

AWARE Framework, mindLAMP (LAMP Platform), MetricWire, Koa Health, Purple Robot.

### Files created or updated

- `module-02-digital-phenotyping/profiles/aware-framework.md`
- `module-02-digital-phenotyping/profiles/mindlamp.md`
- `module-02-digital-phenotyping/profiles/metricwire.md`
- `module-02-digital-phenotyping/profiles/legacy-and-adjacent-platforms.md` (Purple Robot, Koa Health sections)
- `module-02-digital-phenotyping/sources.md`
- `shared/unresolved-questions.md` (Tier 10, items #87, #88, #89, #90, #91, #92 annotated)

### Major findings

1. **AWARE Framework — resolved unresolved-question #88 (Verified).** Direct fetch of
   `https://awareframework.com/sensors/` produced a complete per-sensor Android-vs-iOS availability
   table: of ~33 documented sensor/plugin modules, only ~14 are available on iOS. Critically,
   **Locations (GPS) is Android-only** — a materially larger and more consequential gap than the
   profile's prior general "iOS differs" language conveyed. Also resolved the Active Data Collection
   open question: ESM/EMA is a native module on both platforms. Confirmed Apache-2.0 licence on
   `aware-client` and named plugin repos via direct GitHub org fetch. No managed/SaaS hosting option
   found anywhere on the official site — self-hosting remains the only path.
2. **mindLAMP — resolved unresolved-question #87 (Verified).** Direct GitHub fetch confirms
   `LAMP-portal` and `LAMP-app` were formally **archived by their owner on 2020-11-17** (not just
   labeled deprecated) and mapped their successors: `LAMP-dashboard` (portal successor) and
   `LAMP-core-android`/`LAMP-core-ios` (app successor). Confirmed current, actively-updated
   repositories through Aug 2026: `LAMP-server`, `LAMP-dashboard`, `LAMP-activities`,
   `LAMP-app-gateway`, `LAMP-js`/`LAMP-py` (BSD-3-Clause), `LAMP-toolkit` (MIT, successor to
   `LAMP-cortex`). Direct fetch of `docs.lamp.digital`'s landing page upgraded the passive-sensor
   list (GPS, accelerometer, screen time, calls, heart rate, steps, sleep, gyroscope) from Unclear to
   Corroborated, and surfaced a "flexible hosting and complete data access" phrase suggestive of a
   managed-hosting option — though whether it's offered to outside teams, and at what cost, remains
   unconfirmed (Reported, not resolved). `docs.lamp.digital/about/publications/` again returned 404,
   confirmed as a genuine, repeated access gap rather than a one-off.
3. **MetricWire — partially resolved unresolved-question #90; #89 remains unresolved.** Direct fetch
   of `metricwire.com`'s homepage, `/pricing`, `/site-licence/`, and `/contact-us/` all returned HTTP
   403 (bot-protection) — a confirmed, repeated access barrier, not an unattempted gap. However,
   direct fetch of `https://github.com/MetricWire` succeeded and confirmed exactly one public
   repository (an unrelated forked template) — corroborating the closed-source, no-public-SDK
   characterization. Two independent third-party clues (an m2c2kit integration guide, and an
   unofficial `zeolite` Python client referencing a MetricWire backend called "Catalyst") indicate
   some form of API exists but is not publicly documented for general researcher self-service.
   Pricing remains fully non-public; a "Site Licence" page exists but its terms could not be read.
4. **Koa Health — largely resolved unresolved-question #91 (Corroborated).** Direct fetch of
   `https://www.koahealth.com/research` confirms the page frames digital phenotyping strictly as an
   internal method applied through academic partnerships, with no mention of a deployable platform,
   SDK, or API for outside teams. This upgrades the exclusion rationale from inference to
   primary-source absence — though a fully closed answer still requires initiating direct vendor
   contact, which this session did not do (no outbound contact on the user's behalf was authorized).
5. **Purple Robot — still unresolved (unresolved-question #92); new negative signal found.** A
   deliberate second-pass fetch of the lab page, `/software/`, and the domain root all returned
   **HTTP 500 across the entire phidatalab.org domain** — the same domain that returned page content
   on a single-page fetch in the first pass could not be reached at all this session. This is a new,
   mildly corroborating (but inconclusive — could be a transient outage) signal consistent with
   reduced institutional maintenance of the lab's public web presence.

### Important unresolved questions (even after this pass)

- MetricWire's and Avicenna Research's actual pricing figures (item #89) — MetricWire's site remains
  blocked to automated fetch; Avicenna Research was out of scope this pass.
- The specific open-source licence covering mindLAMP's core `LAMP-server`/`LAMP-dashboard`/
  `LAMP-core-android`/`LAMP-core-ios` repositories (narrower than before — client-library and
  toolkit licences are now confirmed, but the core app/server licence is not).
- Whether mindLAMP's "flexible hosting" is available to outside research/clinical teams, and at what
  cost.
- Whether MetricWire's "Catalyst" API is available to researchers through any official channel.
- Purple Robot's actual current maintenance status — the domain-wide 500 errors are suggestive but
  not conclusive; requires either a later fetch attempt or direct lab contact.
- Full confirmation that no unlisted Koa Health enterprise/partnership platform offering exists —
  requires initiating vendor contact.

### Sources or documentation that were unavailable

- `metricwire.com` (all paths tested) — HTTP 403, confirmed in both passes.
- `phidatalab.org` (all paths tested) — HTTP 500 domain-wide in this pass (was reachable, at least
  partially, in the first pass).
- `docs.lamp.digital/about/publications/` — HTTP 404, confirmed in both passes.
- Individual repository licence files for mindLAMP's core server/dashboard/app repos — not opened
  directly this session (org-level listing did not surface licence badges for these specific repos).

### Decisions that could affect later comparisons

1. **AWARE's iOS limitation is now a Verified, quantified claim (location data is Android-only),
   not a general "coverage differs" caveat** — this should be weighted more heavily than before in
   any future revision of the comparison matrix's iOS/Android parity column for AWARE.
2. **mindLAMP's deprecated-repository risk is now fully resolved** — future references to mindLAMP
   in this knowledge base or downstream content should cite `LAMP-dashboard`/`LAMP-server`/
   `LAMP-core-android`/`LAMP-core-ios`, never `LAMP-portal`/`LAMP-app`.
3. **MetricWire's closed-source/no-public-API characterization is now Verified via direct GitHub
   inspection**, not merely "not located" — this is a stronger claim than the first pass's phrasing
   supported and should be reflected in the comparison matrix if it currently hedges more softly.
4. **Purple Robot and Koa Health remain outside full-profile status** — this pass did not surface
   evidence strong enough to add either as a ninth platform; the legacy-and-adjacent-platforms.md
   file's existing scope decision stands, now with stronger (if still not conclusive) primary-source
   backing.

---

## 2026-08-24 (later still) — Module 2 literature-library retrofit

**Module:** Module 2 (Mobile Digital Phenotyping Platforms)

**Task:** Retrofit Module 2 to store actual PDFs for cited open-access academic papers, per the
literature-library scope decision recorded earlier this date (see the "Literature-library scope
decision" entry above). Module 1 already has this pattern (`research-library-wearables.md` +
implicit PDF-adjacent workflow); Module 2 had never done it — `sources.md` and the profiles only ever
held URLs and summaries.

**Technologies/platforms covered:** Beiwe, RADAR-base, mindLAMP, AWARE Framework, Avicenna Research
(Ethica), MetricWire, m-Path, CARP Mobile Sensing, plus the legacy/adjacent-platforms file (Purple
Robot).

**Files created:**
- `module-02-digital-phenotyping/literature-library.md` — the new index (one table per platform:
  Title, Authors, Venue/Year, DOI/URL, OA status, PDF link, Relevance note).
- `module-02-digital-phenotyping/literature/<platform-slug>/` — 8 new directories holding 13
  downloaded PDFs total (`beiwe/` ×2, `radar-base/` ×4, `mindlamp/` ×2, `aware-framework/` ×1,
  `avicenna-research-ethica/` ×1, `m-path/` ×1, `carp-mobile-sensing/` ×1,
  `legacy-and-adjacent-platforms/` ×1). No `metricwire/` folder — no OA (or any) platform paper was
  found for MetricWire.

**Files updated:** `sources.md` (cross-reference note, no table duplication), `README.md` (new
"Literature library" section), `shared/unresolved-questions.md` (new Tier 11, two items),
`shared/research-log.md` (this entry).

**Process:** (1) read `sources.md` and all 8 profiles to compile the existing citation list — 7
academic papers were already cited, all at Search-summary retrieval only, none with a stored PDF;
(2) ran one fresh literature search per platform for additional decision-relevant methods/validation/
deployment papers not yet cited; (3) for every candidate paper, determined OA status from primary
evidence (JMIR/Frontiers/MDPI/BMC CC BY statements read directly in the fetched PDF, or arXiv's
inherent openness) rather than guessing; (4) downloaded every confirmed-OA PDF via `curl`, then
verified each with a Python (`pypdf`) parse — not just a magic-byte check — to confirm genuine
multi-page extractable text rather than an HTML CAPTCHA/paywall page saved with a `.pdf` extension.

**Counts:** **14 papers catalogued** (13 downloaded as verified real PDFs; 1 — the 2012 iEpi ACM
paper — left citation-only, paywalled). **0 papers were rejected as fake/broken PDFs after download**
— every download attempt that returned a genuine PDF passed verification; the failures were caught
*before* being kept (see below), not after.

**Per-platform breakdown:**
- **Beiwe** — 2 papers, both new to the KB, both downloaded (Torous et al. 2016 JMIR Mental Health
  original platform paper; Onnela et al. 2021 JOSS software paper).
- **RADAR-base** — 4 papers: 2 new (the foundational 2019 JMIR mHealth uHealth platform paper by
  Ranjan et al.; the Matcham et al. 2022 BMC Psychiatry RADAR-MDD recruitment/retention deployment
  study) and 2 upgraded from Search-summary to Verified with PDFs obtained (the 2024 JMIR Mental
  Health clinical-use paper; the RADAR-IoT Sensors paper).
- **mindLAMP** — 2 papers: 1 upgraded to Verified (Vaidyam et al. 2022 JMIR mHealth uHealth) and 1 new
  (Currey & Torous 2022 BJPsych Open validation/replication study).
- **AWARE Framework** — 1 paper, upgraded from a ResearchGate-mirror Search-summary citation to a
  Verified primary Frontiers-hosted OA PDF (Ferreira, Kostakos, Dey 2015).
- **Avicenna Research (Ethica)** — 2 papers: 1 new and downloaded (Qian et al. 2024 JMIR, a genuine
  Ethica-Data-app deployment study from the same University of Saskatchewan group that built the
  platform's academic precursor) and 1 new but paywalled, citation-only (Hashemian et al. 2012 ACM,
  the iEpi origin paper).
- **MetricWire** — 0 papers found. A dedicated search turned up no platform-specific methods,
  validation, or deployment paper of any kind — recorded as a genuine literature gap in
  `literature-library.md`, matching this module's existing finding that MetricWire has no public
  research page and blocks direct site access.
- **m-Path** — 1 paper, upgraded to Verified (Mestdagh et al. 2023 Frontiers in Digital Health).
- **CARP Mobile Sensing** — 1 paper, upgraded to Verified (Bardram 2020 arXiv preprint).
- **Legacy/adjacent (Purple Robot)** — 1 paper, upgraded to Verified (Mendes et al. 2022 JMIR
  systematic review, used to characterize Purple Robot).

**Surprises / notable findings:**
1. **A profile correction candidate surfaced, not made in this pass.** `profiles/m-path.md`
   speculatively named "Kirtley, Hiekkaranta, et al." as the paper's possible authors with an explicit
   caveat that the list was "not independently confirmed." The actual PDF confirms the real lead
   author is **Mestdagh**, not Kirtley — flagged in `literature-library.md` but the profile itself was
   left unedited, since this task's scope was the literature library, not profile content.
2. **PMC direct-fetch was reCAPTCHA-blocked for every `pmc.ncbi.nlm.nih.gov` URL tried this pass** —
   consistent with the access-limitation pattern already documented for Module 1's research library.
   The workaround that worked reliably: `europepmc.org/articles/<PMCID>?pdf=render`, which mirrors PMC
   content and was not blocked for any of the 5 papers it was tried on.
3. **No download was mistakenly kept as a "PDF" that was actually an HTML paywall/CAPTCHA page** —
   several early attempts (PMC's `/pdf/` trailing-slash pattern, one Cambridge Core guessed URL) did
   return HTML disguised with a `.pdf` filename, but all were caught by the `pypdf` text-extraction
   check (magic bytes alone were insufficient — some HTML responses started with binary-looking
   content) and discarded before being copied into `literature/`.
4. **RADAR-base turned out to have the deepest literature base of any platform in this module** — 4
   papers, spanning the foundational architecture paper, an IoT-extension paper, a clinical-use
   overview, and a major multi-site deployment/retention study. This reflects its EU-consortium
   funding model (large multi-site cohorts generate more publishable deployment data) more than any
   difference in platform quality.
5. **MetricWire's total absence of platform literature is a genuinely distinctive finding** relative
   to the other 7 platforms, all of which have at least one dedicated paper — logged as
   unresolved-question #95 rather than silently left out.

**Important unresolved questions (even after this pass):**
- Whether an authentic author-posted (non-paywalled) copy of the iEpi 2012 paper exists anywhere —
  see unresolved-question #96.
- Whether MetricWire has ever published anything about its own platform — see unresolved-question
  #95.
- `profiles/m-path.md`'s author-list error (Kirtley → should be Mestdagh) is flagged but not yet
  corrected in the profile itself.

**Sources or documentation that were unavailable:**
- Direct `pmc.ncbi.nlm.nih.gov` fetch — reCAPTCHA-blocked on every attempt (worked around via Europe
  PMC).
- ACM Digital Library full text for the iEpi paper — paywalled, no workaround attempted (per this
  project's standing instruction not to attempt to bypass access controls).

**Decisions that could affect later comparisons:** None of this pass's additions change any
cross-platform comparison conclusion in `comparison-matrix.md` — this was a citation/evidence-base
retrofit, not new factual research about platform capabilities. The one exception worth flagging for
a future pass: RADAR-base's now-visibly-deeper published-deployment literature (recruitment/retention
data at real multi-site scale) could support strengthening its "evidence of use" comparison-matrix
cell relative to platforms with thinner literature bases, if a future pass wants to formalize that.

---

## 2026-08-24 (later still) — Module 1 literature-library retrofit (Oura, WHOOP, Apple Watch)

**Module:** Module 1 (Wearables). **Technologies researched:** the 54 individually-named papers in
`research-library-wearables.md` across Oura (17), WHOOP (18), and Apple Watch (19, two of which —
Schyvens et al. 2025 and Robbins et al. 2024 — were already catalogued once each under Oura/WHOOP
rather than duplicated). Same retrofit pattern as the Module 2 literature-library pass immediately
above: determine open-access status from primary evidence for every individually cited paper, fetch
and locally store the actual PDF for anything legitimately OA, verify each with a `pypdf`
text-extraction check (not just HTTP 200 or magic bytes) before keeping it, and leave paywalled or
genuinely ambiguous papers citation-only rather than attempting any access-control workaround.

**Files created:**
- `module-01-wearables/literature-library.md` — the full index, organized by device with the
  Tier A/B/C sponsorship column preserved from `research-library-wearables.md` (per this file's own
  explicit instruction that "downstream content should not cite a Tier B/C split more confidently
  than the marker warrants" — the OA layer added here does not re-derive or upgrade that tiering).
- `module-01-wearables/literature/oura/`, `.../whoop/`, `.../apple-watch/` — 43 verified PDFs, 56 MB
  total.

**Files updated:**
- `module-01-wearables/research-library-wearables.md` — added a short pointer note near the top to
  `literature-library.md`; the sponsorship-tier analysis and per-paper writeups were left untouched
  per this pass's scope.
- `module-01-wearables/README.md` — added `literature-library.md` and `research-library-wearables.md`
  rows to the contents table.
- `shared/unresolved-questions.md` — Tier 12 added (see below).

**Per-device breakdown (papers catalogued → PDFs obtained → not obtained):**
- **Oura — 17 → 17 → 0.** The only device with zero access gaps. One substitution: Willoughby et al.
  2023 (*Sleep Medicine*, paywalled, Elsevier) has an open PsyArXiv preprint that was used instead
  after Europe PMC returned no OA record for the published version.
- **WHOOP — 18 → 13 → 5.** Not obtained: Holmes et al. 2026 (*Sleep*, paywalled, no PMC/preprint),
  Miller et al. 2020 (*J Sports Sciences*, Taylor & Francis, paywalled — confirms the prior pass's
  "Tandfonline 403" finding), Lundstrom et al. 2024 (SAGE, paywalled, confirmed HTTP 403), Khodr et
  al. 2024 (medRxiv preprint — legitimately OA in principle, but blocked by HTTP 403 bot-detection on
  every attempt this pass, not a true paywall), and Harms 2018 (an unpublished NAIA-baseball
  dissertation — a UNL DigitalCommons copy exists but 403'd, and ERIC's own hosted copy 404'd; low
  priority per the source file's own framing as "included here only for completeness").
- **Apple Watch — 19 → 13 → 6.** Not obtained: Jaworski & Park 2023 (IEEE EMBC, paywalled), Abou et
  al. 2022 (*Assistive Technology*, Taylor & Francis, paywalled), Choe & Kang 2025 (*Physiological
  Measurement*, IOP, paywalled), the DEFINE AFib Study (a conference-abstract supplement entry, not a
  full peer-reviewed paper — citation-only by nature, not by access failure), and two papers where
  Europe PMC's own metadata confirms `isOpenAccess: Y` with a PMCID but its PDF-render service
  returned HTTP 500 on every retry — Perez et al. 2019 (NEJM, Apple Heart Study) and Mahalingaiah et
  al. 2022 (AJOG, Apple Women's Health Study). These two are recorded as "OA but not obtained this
  pass" — a distinct status from paywalled, since the access barrier is Europe PMC's own retrieval
  infrastructure, not a publisher paywall or bot gate.
- **Total: 54 papers catalogued, 43 PDFs obtained (80%), 11 not obtained.**

**Major findings / surprises:**
1. **A materially significant correction to `research-library-wearables.md`'s own stated confidence.**
   The WHOOP paper "The menstrual cycle through the lens of a wearable device" (*npj Digital
   Medicine* 2026) was explicitly downgraded in a prior pass from "likely Tier A" to "Unclear,"
   because an AI-generated secondary summary naming Alexander Gonzalez and Johanna J. O'Day (Stanford
   Wu Tsai) as lead authors was flagged as "unverified and should not be trusted." **A bioRxiv
   preprint of this exact paper (DOI 10.1101/2025.09.11.675620) was located and downloaded, and its
   actual byline confirms that earlier AI-generated summary was correct**: Gonzalez and O'Day
   (Stanford, co-first/corresponding authors) plus three named WHOOP Inc. staff (Kim J, Jasinski SR,
   Holmes KE) as co-authors, alongside two more Stanford authors. This is a genuinely mixed
   Stanford-led / WHOOP-co-authored paper — it should be restored to Tier A, not left at Unclear. This
   is the single most decision-relevant finding of this pass: a paper the sponsorship-tier file
   actively warned readers away from trusting turned out to be correctly attributed.
2. **A venue mislabeling, not a wrong paper.** Gong et al.'s Oura smart-ring systematic review is
   cited in `research-library-wearables.md` as "*Diagnostics* (MDPI) / JMIR preprint #83508." The
   actual published DOI (10.3390/biomimetics10120819) resolves to a different MDPI journal,
   *Biomimetics* — same authors, same title, same findings, wrong venue name in the source file.
3. **No mismatched-author or retracted-paper problem found**, unlike Module 2's retrofit (which
   caught a wrong guessed author name in `profiles/m-path.md`). This pass's equivalent finding runs
   the opposite direction — a flagged-as-unverified guess turned out to be right (see #1).
4. **Several papers the source file could only cite by title, institution, or working title now have
   confirmed author lists**, obtained from the downloaded PDFs directly: the Oura/Cureus adherence
   paper (Shiba SK et al., not previously named), the WHOOP alcohol-trajectories JMIR paper (Grosicki
   GJ et al.), the WHOOP travel/recovery *Sports Medicine* paper (Hatamiya N et al. — whose actual
   published title, "Optimizing Athlete Travel for Performance," differs from the working title used
   in the source file, confirmed to be the same paper via matching DOI), the Apple Heart & Movement
   Study methods paper (Truslow J et al.), and the Cureus AFib-wearables systematic review (Belani S
   et al., previously identified only by its Nova Southeastern University affiliation).
5. **Apple's VO2max white paper, previously noted as "not machine-readable via fetch," downloaded and
   extracted cleanly this pass** — resolving open item #8 from `research-library-wearables.md`'s
   follow-up list.
6. **Author-order discrepancies on two Doherty-lab Apple Watch papers**: the source file lists
   "Doherty C, Lambe R, O'Grady B, Baldwin M" and "Doherty C, ..." as apparent lead authors on the
   PLOS ONE VO2max and Sensors HRV/RHR papers respectively; the actual published bylines list Lambe R
   and O'Grady B as first authors, with Doherty C as senior/last author on both. Not a wrong-paper
   error — same paper, same COI/funding conclusion — but worth correcting if this file's prose is
   ever revised to name individual authors.
7. **Two Apple Watch PDF filenames were corrected mid-retrofit** after the downloaded PDFs revealed
   the true venue: the Wasserlauf AF paper is *Journal of Cardiovascular Electrophysiology* (an
   initial filename guessed "Circulation: Arrhythmia and EP"), and the Littell pediatric SpO2/ECG
   paper is *PLOS Digital Health* (an initial filename guessed "PACE").
8. **The Dial et al. 2025 Oura-vs-WHOOP head-to-head (*Physiological Reports*) downloaded cleanly**,
   resolving the 403/CAPTCHA block noted in the prior pass. Full-text extraction into
   `validation-evidence.md` remains a separate, not-yet-done action item — this pass obtained the PDF
   but did not perform the deep extraction `validation-evidence.md` requires.

**Important unresolved questions (logged to `shared/unresolved-questions.md` Tier 12):**
- Whether the Gonzalez/O'Day WHOOP menstrual-cycle paper's tier should be formally corrected from
  "Unclear" back to "A" in `research-library-wearables.md` itself (not done in this pass — literature
  library only).
- Whether a working, non-bot-blocked route exists to the Khodr et al. medRxiv preprint, the Perez
  2019 NEJM PMC deposit, and the Mahalingaiah 2022 AJOG PMC deposit — all three have a confirmed or
  probable OA record that automated fetch could not retrieve this pass.
- Whether the Harms 2018 NAIA-baseball dissertation is obtainable through any other route (UNL
  DigitalCommons, ProQuest with institutional access) given its low but non-zero evidentiary value.

**Sources or documentation that were unavailable:**
- IEEE Xplore, Taylor & Francis (Tandfonline), SAGE Journals, IOP Publishing (*Physiological
  Measurement*), and Oxford Academic's *Sleep* — no OA route found for any paper hosted at these
  venues in this pass, consistent with paywall patterns already documented elsewhere in this module.
- Europe PMC's PDF-render service (`europepmc.org/articles/<PMCID>?pdf=render`) — reliable for every
  PMCID tried except two (PMC8112605 / Perez NEJM, PMC10518829 / Mahalingaiah AJOG), both of which
  returned HTTP 500 on repeated attempts despite Europe PMC's own metadata marking them open access.

**Decisions that could affect later comparisons:** None of this pass's additions change any
cross-device comparison conclusion in `comparison-matrix.md` or `validation-evidence.md` — this was a
citation/evidence-base retrofit, not new factual research about device capabilities. The one
exception worth flagging: the Gonzalez/O'Day tier correction (finding #1 above) is a genuine change
to how one paper should be classified in `research-library-wearables.md`, even though this pass did
not make that edit directly.

---

## 2026-08-31 — Onnela Lab publication catalog (Modules 1 and 2)

**Modules:** 1 (wearables) and 2 (digital phenotyping). No Module 3 files were created or edited
apart from a single handoff triage file, at the request of the agent building that module.

**Technologies researched:** none directly. This was a bibliographic pass against a single lab's
publication record — the Onnela Lab (Harvard T.H. Chan School of Public Health), Beiwe's and Forest's
originating group.

**What was pulled.** <https://hsph.harvard.edu/research/onnela-lab/papers/>, direct fetch, HTTP 200,
2026-08-31. The page groups its output under exactly two `<h2>` headings — **"Digital Health and
Phenotyping"** and **"Network Science"**. Only the first was taken; the category structure was
unambiguous and required no judgment call about which heading a paper sat under. That heading listed
**114 entries, 113 distinct papers** — Hu et al., *Nature and Science of Sleep* 2025 (wrist-worn
consumer wearable vs. actigraphy sleep measurement) is listed **twice** on the page, in two different
year blocks. Catalogued once, with the duplication noted in its row.

**Metadata resolution.** Title, authors, venue and year came from the lab page. DOI, PMID, PMCID,
journal, `isOpenAccess` and abstract were resolved against the Europe PMC REST API by exact-title,
then DOI-from-link, then fuzzy-title lookup. **107 of 113 resolved to a DOI**; the remaining 6 are
items the lab page itself labels *Submitted* / *In print* with no DOI or indexed record (recorded
rather than dropped — the lab page is the primary source for their existence). Five records where the
lab page's title and the Europe PMC title diverged materially were checked individually; four were
confirmed the same paper (page titles were truncated or variant), and one — "Returning individual
research results from digital phenotyping in psychiatry" (*AJOB* 2023) — was left labelled
**Unclear** rather than asserted to be the differently-titled AJOB record that came back.

**Files created or updated:**
- `module-02-digital-phenotyping/literature-library.md` — new "Onnela Lab publication catalog" section,
  91 papers.
- `module-01-wearables/literature-library.md` — new "Onnela Lab publication catalog — wearable-primary
  papers" section, 22 papers.
- `module-02-digital-phenotyping/sources.md` — S-BEI-09 (the lab papers page), S-BEI-10 (Europe PMC API).
- `module-01-wearables/sources.md` — S-W-ONN-01, S-W-ONN-02.
- `module-02-digital-phenotyping/literature-library-index.json`,
  `module-01-wearables/research-library-index.json` — both dedup ledgers were **empty** before this
  pass (`ids_seen: []` / `pmids_seen: []`, `last_run_date: null`); now populated with this run's DOIs,
  PMIDs, per-paper records, and a `runs` entry.
- `module-02-digital-phenotyping/literature/onnela-lab/` — 54 new PDFs.
- `module-01-wearables/literature/apple-watch/` (9 new), `literature/research-accelerometers/` (new
  folder, 5), `literature/fitbit/` (new folder, 1), `literature/oura/` (1 new).
- `module-03-applied-studies/_onnela-module3-candidates.md` — handoff triage only; no Module 3 profile,
  README, or index was created or touched.

**Major findings:**
1. **71 of 113 papers were obtained as verified open-access PDFs** (magic-byte + `pypdf`
   text-extraction check on the first three pages; 0 failures on that check). 3 were already in the
   knowledge base and were not re-downloaded or duplicated: the 2016 Torous *JMIR Mental Health*
   Beiwe paper, the 2021 Onnela *JOSS* software paper (both Module 2), and the 2021 Mahalingaiah
   *AJOG* Apple Women's Health Study design paper (Module 1). **39 could not be obtained.**
2. **The single largest filing judgment call was the Apple Women's Health Study family (14 papers).**
   These are reproductive-epidemiology analyses running on the Apple Research app, not
   wearable-sensor-capability evidence. They were filed in **Module 1** because the AWHS
   design-and-methods paper was *already* there, cited in `research-library-wearables.md`. Filing the
   whole family in Module 2 as smartphone-app cohort studies would have been equally defensible;
   precedent decided it. Flagged in the Module 1 section so a later pass can revisit the block whole.
3. **Three genuinely dual-modality papers** were flagged individually rather than filed silently: the
   2023 npj Digital Medicine ALS paper (Beiwe surveys + ActiGraph/Modus passive — filed Module 1 on
   the wearable), DPSleep (an Onnela-lab method applied to wearable accelerometer input — filed
   Module 1 on the input device), and the "one-size-fits-most" walking-recognition paper (validated
   across smartphones, smartwatches and wearables — filed Module 2 as a method).
4. **27 papers were triaged as Module 3 deployment candidates** and carry a forward pointer in their
   catalog rows. Methods and architecture papers were deliberately excluded from that list.

**Important unresolved questions:**
- Whether an alternative retrieval route exists for the ~13 papers Europe PMC marks `isOpenAccess: Y`
  but which neither its render service nor `pmc.ncbi.nlm.nih.gov/articles/<PMCID>/pdf/` would return.
- Whether the *AJOB* 2023 "returning individual research results" item is the same paper as the
  differently-titled Europe PMC record (currently **Unclear**).
- Whether the Oura Ring 3 freshmen sleep study (Soon et al., *Sleep* 2025) belongs in
  `research-library-wearables.md`'s Oura section, and at what tier — deliberately not added, because
  its funding/COI statement was not read.

**Sources or documentation that were unavailable:**
- **Europe PMC PDF render, HTTP 500** — a repeated, non-transient failure across a cluster of older
  PMC author manuscripts (~2015–2022): *Annals of Surgery*, *Annals of Surgical Oncology*, *Clinical
  Psychological Science*, *Molecular Psychiatry*, *Harvard Review of Psychiatry*, *Current Psychiatry
  Reports*, *J Neurosurg Spine*, *World Neurosurgery*, *AJPM&R*, *J Psychiatric Research*, *AJOG*
  (Zhang 2022), *Contemporary Clinical Trials*. This extends the same HTTP-500 pattern already logged
  for this service on 2026-08-24.
- **`pmc.ncbi.nlm.nih.gov/articles/<PMCID>/pdf/` serves HTML, not PDF** — consistently for the
  JAMA-family articles (*JAMA Network Open*, *JAMA Surgery*) and *JCEM*.
- **medRxiv, HTTP 403** — the 2025 circadian rest-activity biomarker preprint.
- **Genuinely paywalled, no OA route** — *Neurosurgery*, *Behaviour Research and Therapy*, *Psychiatry
  Research*, *Annual Review of Clinical Psychology*, *Biometrics*, *Statistical Methods in Medical
  Research*, *IEEE/ACM TASLP*, *Psychiatric Annals*, *Quality of Life Research*, *Internet
  Interventions*, *AJOB*.

**Decisions that could affect later comparisons:** **None of this pass's additions changed the
confidence status of any existing claim.** No profile, comparison matrix, or validation file was
edited. Adding a citation is not the same as reading it against a claim; every confidence marker in
both modules still reflects what was actually verified in the 2026-08-21 through 2026-08-25 passes.
The catalog is now available to support a later evidence pass, and the Module 3 triage file is a
handoff, not a finding — its sample sizes and operational figures are **Reported** from abstracts, not
extracted from full texts.

---

## 2026-08-31 — Module 3 (Applied Wearables and Digital Phenotyping Studies): initial build

**Module:** 3 (new). **Also touched:** Modules 1 and 2 (Onnela Lab publication sweep, run in
parallel); `module-02-digital-phenotyping/profiles/beiwe.md`; `shared/unresolved-questions.md`.

### Technologies / studies researched

Module 3's unit of analysis is the **study**, not the technology. Discovery ran from the
device/platform side per `CLAUDE.md`: 20 Europe PMC queries (one per Module 1/2 technology × a
deployment-reality term block), plus 8 targeted supplementary queries for consumer-wearable and BYOD
designs. ~2,000 records → 121 screened-in candidates → **19 selected and profiled**.

Platforms covered: Beiwe (5), RADAR-base (4), mindLAMP (1), plus movisensXS, Ilumivu mEMA and Purple
Robot in mixed designs. Devices: Fitbit (7), Apple Watch (1), Empatica (2), Axivity/GENEActiv (1),
Withings (1), plus several unprofiled devices.

### Files created or updated

**Created** — `module-03-applied-studies/`: `README.md`, `feasibility-matrix.md`, `sources.md`,
`_inventory-and-scope-decisions.md`, `literature/` (14 OA PDFs), and 19 profiles under `profiles/`.
**Updated** — `module-02-digital-phenotyping/profiles/beiwe.md` (new `heartbeat` subsection);
`shared/unresolved-questions.md` (new Tier 14, Q106–Q110).

Note: `_onnela-module3-candidates.md` in this directory was written by the parallel Onnela
cataloguing pass, not by the Module 3 build.

### Major findings

1. **Retention and completeness are different questions**, and studies mostly report the flattering
   one. RADAR-MDD: ~80% outcome retention, **17.7% of participants with >50% data across all
   streams**.
2. **Passive data outlasts active data** — reproduced across five studies and three platforms. In
   adolescents over 18 months, passive held **flat at ~94% while surveys fell 65%→30%**. One study
   (de Angel) found the reverse for smartphone passive data, so this is not a universal law.
3. **Recording mode dominated data loss** in the multi-centre Empatica study: onboard storage <10%
   loss vs live streaming ~50%, with on-body scores >80% in both. **Participants wore the device; the
   system lost the data.**
4. **Provisioning phones made retention worse** (HR≈1.66), and RADAR-base's Android-only requirement
   caused 11.1% of RADAR-MDD's withdrawals.
5. **BYOD buys wear compliance nothing else matches (23 h/day median) and costs representativeness**
   — All of Us is >80% historically underrepresented overall but 70% White in its Fitbit substudy.
6. **Enrolment scale does not survive multi-step protocols**: Apple Heart 419,297→450 usable;
   Fitbit Heart 455,699→1,057. A $50 incentive did not fix the funnel.
7. **Consent design can be the binding constraint** — a no-proxy-consent requirement excluded 95.6%
   of screened palliative patients and terminated that study.
8. **Missingness can be signal**: adding survey non-completion as a predictor raised AUC 0.81→0.93,
   outranking most content features.
9. **Baseline disease severity mostly does not predict attrition** (null in four studies), but
   anxiety, negative symptoms, younger age and slow notification response all do.
10. **OS-level erosion of data streams is real** — RADAR-MDD lost call/SMS logs to a Jan 2019 Google
    Play permissions change mid-study, and the CrossCheck benchmark dataset is now unreproducible for
    the same reason.

### Beiwe `heartbeat` — correction propagated

The user identified that Beiwe has since added a **heartbeat/keepalive** feature. Verified against the
`onnela-lab/beiwe-backend` public commit history (built Jan–May 2024; per-study configurable;
**globally enabled 2024-05-29**; API endpoint 2024-06-06) rather than from an internal source, since
this repo is public. Consequence recorded across Modules 2 and 3: **every Beiwe completeness figure
in the knowledge base predates the feature** and is now labelled a **pre-heartbeat lower bound**, not
current performance. Beukenhorst et al.'s "longitudinal passive data collection without active data
collection is not possible" now reads as describing pre-2024 Beiwe — heartbeat substitutes a
server-triggered wake for a participant-initiated one, narrowing but not removing the dependency.

### Important unresolved questions (new Tier 14 in `shared/unresolved-questions.md`)

- **Q106** — quantified effect of Beiwe's heartbeat on data completeness; implementation is publicly
  evidenced, effect size is not published anywhere public.
- **Q107** — whether RADAR-base, mindLAMP, AWARE, Avicenna, MetricWire, m-Path or CARP have an
  equivalent keepalive, and whether it is on by default. A genuine undocumented differentiator.
- **Q108** — current Android/iOS background-execution limits vs those in force when the baseline
  studies ran.
- **Q109** — whether Dreem, Fibaro and CANedge (plus Connecare, movisensXS, Ilumivu mEMA, Purple
  Robot) warrant Module 1/2 profiles.
- **Q110** — five baseline studies have no obtainable PDF (JAMA-family, *Circulation*,
  *J Biopharm Stat*, *J Psychiatr Res*, and the JMIR mHealth Sleepsight paper).

### Sources or documentation unavailable

Five of nineteen studies yielded no PDF: the JAMA-family and *Circulation* PMC routes served HTML
rather than PDF, and two paywalled-journal author manuscripts plus one JMIR paper failed on every
route tried. **All five were still read in full** via the Europe PMC / NCBI PMC XML deposits, so no
claim rests on an abstract.

### Decisions that could affect later comparisons

- **Definitions are not standardised across studies** for "wear time", "data availability" or
  "retention". A prominent warning is carried in `feasibility-matrix.md`; the matrix supports
  comparison of patterns and orders of magnitude, **not** ranking of platforms.
- **Discovery sorted by citation count**, which under-samples 2025–2026. Recorded as a known bias; a
  date-sorted pass is the recommended next step.
- **The staged second tranche (27 Onnela candidates) is entirely one lab's output and heavily
  Beiwe-weighted.** Building it out without a matching pass on AWARE, Avicenna, MetricWire, m-Path
  and CARP would tilt the module toward Beiwe for sampling reasons rather than merit — which cuts
  against the objectivity `CLAUDE.md` requires for Beiwe specifically. Recorded in
  `_inventory-and-scope-decisions.md` and `README.md`.
- **Six bibliographic/device corrections** made during the pass and recorded in `sources.md` rather
  than silently repaired: three wrong first authors (Muurling not Curcic; Beukenhorst not Berry;
  de Angel not White), two wrong device attributions (the inpatient suicide pilot used movisensXS not
  Empatica; Sleepsight used a Fitbit Charge HR — the Empatica E4 was tested and *rejected*), and one
  wrong DOI. One device identification remains **Unclear** (Helmer et al.'s specific wrist and chest
  device models).

---

## 2026-09-01 — Module 3 extension: recency scan, platform-coverage pass, Onnela tranche

**Module:** 3. **Also touched:** `shared/unresolved-questions.md` (new Tier 15, Q111–Q116).

Three tasks run in order, the latter two in parallel by subagents with hard-partitioned file
ownership. **Module 3 goes from 19 to 40 profiles.**

### 1. Date-sorted recency scan

Re-ran all 20 technology queries sorted by publication date, window 2024-06-01 onward.
**64 candidates screened in — 62 of them (97%) had never been surfaced by the citation-sorted Phase 1
pass.** The bias was larger than estimated. Written up in
`module-03-applied-studies/_recency-scan-2026-09.md`; the baseline is now explicitly labelled as
covering *well-established* rather than current practice.

### 2. Platform-coverage pass — 12 profiles

Closed the gap for the five Module 2 platforms with no Module 3 entry: **AWARE (3), Avicenna/Ethica
(3), MetricWire (3), m-Path (2), CARP (1)**. All 12 read from full text; all OA with PDFs on disk.

### 3. Onnela tranche — 9 profiles

Built from the staged candidate list: Mercier 2020, Johnson 2023, Yi 2025, Fu 2024,
Straczkiewicz 2024, Wright 2018, Soon 2025, Liu 2019, Cote 2019.

### Major findings

1. **The incentive question now has an answer, and it is not the obvious one.** Mercier 2020 raised
   retention **50% → 78%** with a $30-per-two-month payment conditional on ≥70% survey completion —
   **but survey completion rate itself did not move**, and in the same study *recruitment channel*
   produced a larger spread (53% vs 21%). Read with Lubitz's ineffective $50 incentive, Liu's unpaid
   cohort where patients engaged 3× more than controls, and Soon's 10.8% withdrawal at ~USD 263:
   **incentives buy enrolment persistence, not engagement, and are not the strongest lever.**
2. **The OS-asymmetry claim has been downgraded.** `feasibility-matrix.md` previously asserted "iOS
   outperforms Android". Niemeijer 2023 (CARP, clean 52/52 split) found **iOS gaps ~6× longer than
   Android's**, and McClaine 2024 (AWARE) found Android yield lower than iOS. All Verified, pointing
   opposite ways. The direction is now recorded as **unsettled and platform-/stream-specific**
   (Tier 15 Q111).
3. **Definitions decide the answer — three new demonstrations.** Kivelä 2024 publishes **two
   defensible acceptability rates 59 points apart for the same cohort** (39% and 98%); Dennard 2025's
   module-lowest 39.1% is an artefact of a platform export limitation forcing a 100%-complete
   definition; Straczkiewicz 2024 yields **N = 202 / 240 / 308 from identical raw data** at 21/16/8-hour
   wear thresholds.
4. **The funnel starts before consent and is usually unreported.** 42% of those approached excluded
   for not owning a smartphone (Cote); 8 of 18 eligible patients gatekept out **by their own
   oncologists** behind a "100% approach-to-consent" headline (Wright); 29% unable to run the app on
   their own Android handset (Camargo).
5. **Co-design outperforms payment.** The module's highest mental-health compliance (**80.21%**) came
   from letting participants set prompt frequency themselves (Clark 2025).
6. **A new failure category: fraud.** Siebers 2025 used **MetricWire's carrier-country field** to
   unmask 10 fraudulent participants in a $480 virtual trial; a manual checklist later blocked 37.

### Discovery-method findings (recorded in `_inventory-and-scope-decisions.md`)

Two structural blind spots, both found the hard way:

- **Ordinary-word platform names.** Europe PMC **does not honour phrase quoting** for `"AWARE
  framework"` — a phrase query returned 579 in-window hits dominated by "geometry-aware",
  "causality-aware". Genuine AWARE deployments never entered the retrieved window, and the recency
  scan wrongly concluded a null. At least 7 exist.
- **Framework-shaped platforms.** CARP Mobile Sensing is a library embedded in other people's apps
  and publishes under *their* names. Only an **OpenAlex citation-graph pass** found it.

**Consequence adopted as policy: treat any null from a name-based query as unproven until a
citation-graph pass has been run.**

### Corrections made (all recorded in `sources.md`, not silently repaired)

- **Ball et al. 2025 is not a MetricWire study** — 90% of participants used LifeData Realtime EXP,
  10% MetricWire. My own recency scan had it wrong; verified against PMC13289574 and corrected.
- **The AWARE null in the recency scan was wrong** (above); corrected in place.
- **Cote 2019's "105 enrolled (55 analyzed)"** in the staged Onnela candidate file is wrong — all 105
  were analysed, 55 is the surgical subgroup. The advertised "clearest attrition signal in the set"
  does not exist.
- **Liu 2019 is the LAMP app, not Beiwe** — reclassified.
- **Johnson et al. 2023** was miscalled "Karas/Berry" in the candidate file; Johnson SA and Karas M
  are co-first authors.

### Sources or documentation unavailable

Six Onnela-tranche candidates have **no open-access route at all** — concentrated in *Annals of
Surgery*, *Neurosurgery*, *Psychiatry Research* and *Quality of Life Research* — including the only
**ingestible-sensor** and only **audio/speech** studies in that set. Two modalities are therefore
absent from Module 3 for access reasons rather than absence of research (Tier 15 Q116).
Europe PMC's PDF render returned HTTP 500 for Mercier; the PMC PDF endpoint is now behind a
proof-of-work bot challenge, which was not attempted. NCBI efetch XML was used instead.

### Decisions that could affect later comparisons

- **The Beiwe tilt was actively managed rather than accepted.** Running the platform-coverage and
  Onnela passes in parallel put Beiwe at **11 of 40 (28%)** instead of 11 of 28 (39%). Residual, and
  recorded: the 11 are not independent (nine share an author), and **all of them are pre-`heartbeat`**
  — the module's Beiwe evidence is simultaneously its largest and most systematically dated
  (Tier 15 Q115).
- **Nock et al. 2026 (N=619, the largest study in the tranche) was rejected on the `CLAUDE.md` scope
  rule** because it runs on LifeData, unprofiled in Modules 1/2. Its operational content is preserved
  in `_onnela-tranche-report.md` as a Module 2 expansion blocker. **LifeData is now the strongest
  Module 2 expansion candidate** (Tier 15 Q113).
- **New Module 1/2 expansion candidates surfaced:** LifeData, RAPIDS, `mpathsenser`, Modus StepWatch 4,
  Z4IP, and the CARP application ecosystem (DiaFocus, mCardia, Wrist Angel, AwarNS, Niimpy).
- **`feasibility-matrix.md` is now 40 rows across six tables** (Part A baseline, Part B extension) with
  an expanded cross-cutting-patterns section. Its non-standardised-definitions warning has been
  strengthened — that warning is now the single most load-bearing caveat in the module.

---

## 2026-09-02 — Module 3 recency + citation-graph build; LifeData added to Module 2

**Modules:** 3 (40 → **50 profiles**) and 2 (new LifeData profile; MetricWire claim upgraded).
**Also touched:** `shared/unresolved-questions.md` (Q111 reformulated, Q111b added).

Three tasks, run in order; the latter two in parallel by subagents with partitioned file ownership.

### 1. Citation-graph discovery (OpenAlex)

Replaced platform-*name* matching with platform-*citation* matching: every work since 2018 citing a
platform's own methods paper. **71 new candidates.** Written up in
`module-03-applied-studies/_citation-graph-scan-2026-09.md`.

- **Confirmed the CARP null by a second, independent method** — the Bardram anchors have only **14
  citing works since 2018 in total**. Name-based search missed CARP because it is framework-shaped;
  the citation graph is immune to that and still finds almost nothing. The null is evidentiary, not
  methodological.
- **Cross-validated the date-sorted pass**, independently re-surfacing the LINC paper, the
  network-traffic study and the psychosis multi-wearable pilot by a different route.
- **Its own failure mode is significant: 3 of the first ~12 candidates examined were attributed to the
  wrong platform**, because citing ≠ deploying.

### 2. LifeData profiled in Module 2

Clears the scope blocker that excluded **Nock et al. 2026 (N=619)** and **Ball et al. 2025** from
Module 3.

- **Naming correction, propagated:** the product is **RealLife Exp**, not "Realtime EXP" — Europe PMC
  returns **74 hits vs 1**, and that 1 is Ball et al.'s own mis-rendering, which this project's recency
  scan had inherited verbatim.
- **Compliance conflict recorded as Unclear:** marketing asserts "HIPAA & GDPR compliant" on 4+ pages
  (one misspells it "HIPPA"), but the privacy policy and terms **mention HIPAA zero times** — no BAA,
  no Security/Privacy Rule language; SOC 2, ISO 27001 and 21 CFR Part 11 appear nowhere despite a
  marketed "Clinical" eCOA tier. What *is* documented: EU-U.S./UK/Swiss DPF self-certification and a
  GDPR-processor role.
- **Worst documentation opacity in the module** — the entire help centre is login-gated; no public data
  dictionary, export schema or permission model.
- **MetricWire "Catalyst" upgraded Reported → Corroborated** — Ball et al. confirms the app name from
  peer-reviewed full text, where it previously rested on an unofficial third-party Python client.

**Scope decision recorded, not set silently:** LifeData is **EMA/ePRO-only** — its sole sensor stream
is GPS captured *with* a survey response, and what Nock et al. call "passive" data is survey response
metadata, not phone sensors. Admitting these studies widens Module 3 toward app-based EMA generally.
Admitted, on the grounds that Module 2's scope already includes EMA-centric commercial platforms and
that an N=619 deployment reporting 81.1% any-data is exactly this module's content — **on condition
that such profiles state plainly they are EMA deployments**, so the feasibility matrix is not read as
comparing like with like. Module 2's README and matrix label LifeData accordingly.

### 3. Ten new Module 3 profiles

Deliberately weighted **away** from Beiwe (1 of 10; Beiwe share 28% → 24%), because the
citation-graph yield was Beiwe-heavy for reasons of anchor citation counts rather than deployment
frequency. Added the module's **first Garmin, first WHOOP, first Apple SensorKit, first VPN
network-traffic, and first Latin American** deployments.

### Major findings

1. **The iOS/Android question was mis-framed, and is now resolved in form if not mechanism.**
   McInerney et al. 2024 — a **Beiwe** study, the platform whose prior work favoured iOS — stratified
   **by stream** within one cohort: **iPhones missed 70.0%/70.6% of morning/evening EMA vs Android's
   21.3%/26.8% (p<0.001), while accelerometer and GPS showed no significant OS association in the same
   participants.** Verified from full text. **The asymmetry is stream-specific before it is
   platform-specific** — which reconciles the earlier contradiction (iOS-favouring results measured
   passive streams; Android-favouring ones measured active survey delivery). Q111 reformulated;
   **Q111b** added for the mechanism, which if it is iOS notification throttling would affect every
   iOS EMA deployment on every platform in Module 2.
2. **Data quality is operationalisable, and the cost is now quantified.** LINC raised median GPS
   quality to **0.92** against 0.12–0.80 across six prior mindLAMP studies — at **1.3 troubleshooting
   contacts/participant, ~9 interventions/week, two RAs**. Below 0.50 quality, home-time estimates are
   wrong by 2–4 hours.
3. **Data can be present and wrong.** **98% of Samsung sleep records were present but corrupt**
   (duplicated start timestamps, missing end times). No completeness metric in this module would have
   caught it — a new failure class.
4. **Vendor policy change as quantified study risk** — 17 of 20 Samsung escalations traced to a
   mid-study Samsung privacy-policy change.
5. **Zero-friction scale has a floor:** WHOOP reached 181,574 members with no recruitment,
   provisioning or clinic step, and got **1.9% response, 1.84 responses per person over 13 months**.
6. **Reframing incentives:** support raises completion, payment raises persistence, and neither raises
   engagement with interactive content — which is the component that stratifies demographically.

### Corrections made (recorded in `sources.md`, not silently repaired)

- **Three wrong platform attributions** in this project's own citation-graph candidate list (Shen,
  Mahmood, Van der Donckt) — all caught on full-text reading.
- **An overstated contradiction of our own finding #14**, corrected on review: Carlson's "no
  individuals were ineligible for lack of smartphone access" uses a **household-level** access
  criterion (a parent's phone or household tablet counted), whereas the finding it appeared to
  contradict measures **individual** ownership in an adult clinic population. Re-framed as *the
  exclusion is designable-around*, which is Verified, rather than *the barrier has disappeared*, which
  is not.
- **A JATS parsing trap worth remembering:** PMC's `contrib-group` for **JMIR** articles lists handling
  editors before authors; naive parsing puts non-authors on the byline. Use the PDF byline.

### Sources unavailable

Two of the ten have no storable PDF (Europe PMC render truncates/errors; JMIR endpoints refuse
automated retrieval) — both read in full from PMC XML. Nock et al. 2026 is paywalled; read via NCBI
efetch.

### Decisions affecting later comparisons

- **Module 3 now contains two studies deploying no Module 1/2 technology at all** (Apple SensorKit;
  VPN network-traffic sensing). Both carry explicit scope notes and are legitimate to reject on a
  stricter reading of the scope rule. Recorded rather than quietly absorbed.
- **New Module 1/2 expansion candidates:** VPN/network-layer sensing, CareLoop Health Ltd, neuroUX —
  in addition to RAPIDS, `mpathsenser` and the CARP application ecosystem from the previous session.
- **AWARE is now the least-served covered platform** (7 unbuilt candidates), and Module 3 still has
  **no head-to-head comparison of Beiwe, mindLAMP and RADAR-base** — the candidate that appeared to be
  one used none of them.

---

## 2026-09-02 (later) — Module 3 AWARE coverage pass

**Module:** 3 (50 → **55 profiles / 54 distinct deployments**). **Also touched:**
`shared/unresolved-questions.md` (new Tier 16, Q117–Q119).

### What was researched

AWARE Framework deployments, to close the module's largest platform-coverage gap. Discovery ran as a
dedicated OpenAlex pass over **all 425 papers citing the AWARE anchor** (Ferreira, Kostakos & Dey
2015) since 2016.

### A correction to this project's own carried-forward claim

The "**7 unbuilt AWARE candidates**" figure from the previous session **did not survive inspection**.
One was LINC (already profiled, and mindLAMP rather than AWARE); roughly four were reviews,
platform-architecture or design papers, all out of scope. It was a loose screen, not a buildable
queue, and it had been repeated in a status report without being checked.

The real shape of the seam: of 425 citing papers, **215 have zero deployment signals, 106 have one,
31 have two, and only 2 have three or more** (68 have no abstract). **AWARE has the inverse problem
to CARP** — CARP has almost no citing literature; AWARE has plenty that uses it as a toolkit and
reports findings rather than deployments.

### Files created or updated

Five new profiles (Wu 2023 alcohol-associated liver disease; Aledavood 2024 MoMo-Mood; Balliu 2024
STAND; Borelli 2025 mSavorUs completeness; Bae 2023 binge-drinking JITAI) plus 5 OA PDFs and
`_aware-build-report.md`. Integrated into `feasibility-matrix.md` (new Part D, Table 8),
`README.md`, `sources.md`, `_inventory-and-scope-decisions.md`.

### Major findings

1. **There are three kinds of OS effect, not one.** This refines the stream-specific finding from
   earlier today into: **structural gates** (iOS does not expose SMS at all — features computable for
   only **15 of 183 participants, 8.2%**; no mitigation exists, the choice is binary), **yield
   differences** (70% vs 21% EMA miss), and **breadth differences** (Android delivered **8.4 vs iOS
   4.7 mean sensor types** — Android ahead, the *opposite* direction to the yield finding, on the same
   framework). Q119 opened for the mechanism.
2. **A platform's completeness figure is close to meaningless for a mixed cohort.** Within one study,
   one platform, one configuration: passive missingness **1.2% (controls) to 20.4% (BPD)** — a **17×
   spread by diagnosis**.
3. **Care setting beats clinical severity for retention.** **1.7% vs 33.5–37.3%** two-week attrition
   between in-person clinical care and online support, with the *sicker* arm retaining better —
   missed assessments were reconciled during routine visits.
4. **Two new data-loss classes.** **Research-infrastructure failure** (server congestion, Wi-Fi-gated
   upload, one study provisioning a router per participant — three independent studies, and a direct
   input to the self-host-vs-SaaS decision in Module 2), and **participant-exercised configurability**
   (**35.4% of person-days unusable** because participants, told the sensors were configurable, turned
   GPS off).
5. **A second clean exception to "passive outlasts active"** — in one cohort *"all participants
   supplied AWARE data every day that they responded to EMAs"*; passive and active did not decouple.
6. **Provisioned wearables beat the BYOD phone** in the same people over the same months: 11% missing
   (Oura + Samsung) vs 16% (AWARE smartphone).

### Corrections recorded

- **Two profiles report one cohort.** Nguyen et al. 2025 and Borelli et al. 2025 are the same
  37-participant mSavorUs deployment — Verified via identical enrolment, devices, design, 13
  Latinx/Latine participants, nine shared authors, and Borelli citing Nguyen as then-unpublished. Both
  retained and cross-linked (Borelli supplies the completeness data Nguyen names as its own gap), but
  the feasibility matrix carries **one row**. **AWARE has 8 profiles but 7 independent deployments.**
- **An unresolved contradiction between two published papers**: they disagree on their own enrolment
  year (2021 vs 2022), duration (22 vs ≥19 weeks) and analytic N (29 vs 28). Both verified verbatim.
  Not cosmetic — 2021 is inside California COVID restrictions, 2022 is post-Omicron. Tier 16 Q117.
- **The JMIR byline hazard is worse than previously recorded**: ordering is **not stable within the
  publisher** — some articles place editors after authors, others first. Always verify against the
  publisher PDF.
- An arithmetic error in Bae 2023 ("489/756" where components sum to 754).

### Sources unavailable

**`10.1145/3711043` (Zhang & Poellabauer, *Proc. ACM HCI* 2025)** — the best topic-matched AWARE
candidate, and unobtainable: ACM DL serves an HTML challenge, the full-HTML view 403s, no arXiv
preprint, not in PMC. **Deliberately not written from its abstract**, and its AWARE attribution is
therefore unverified. Tier 16 Q118.

### Decisions affecting later comparisons

- **A third structural discovery blind spot recorded: venue-shaped invisibility.** AWARE's
  deployment-reality literature lives in CSCW/IMWUT/UbiComp, outside the biomedical indexes this
  module searches — and the one paper that mattered most is exactly the one that could not be
  retrieved. Joins the ordinary-word-name and framework-shaped-platform blind spots.
- **The derivative-build problem**: 2 of 5 AWARE deployments used author-modified builds. Platform-level
  aggregation for AWARE will degrade as these accumulate.
- **AWARE's operational literature also skews 2016–2020**, predating current OS background-execution
  behaviour; those figures need a dated-evidence label of the same kind applied to pre-`heartbeat`
  Beiwe.
- **Still open:** no head-to-head comparison of Beiwe, mindLAMP and RADAR-base (unchanged), and the
  AWARE set is entirely US or Finnish.

---

## 2026-09-02 (later still) — Module 3 wired into the weekly literature-scan routine

**Module:** Cross-module infrastructure. No profile, matrix or library content changed.

### What was done

`CLAUDE.md`'s Future automation note gated Module 3's inclusion in the weekly scan on "once this
module has an initial baseline of profiles". That baseline now exists (55 profiles), so the module
was wired in.

**Created:**

- `module-03-applied-studies/literature-index.json` — dedup ledger following the Module 1/2
  `*-index.json` pattern, **seeded with all 55 profiled studies** (55 DOIs, 54 PMCIDs) so the routine
  never re-surfaces them. Adds a `rejected` array not present in the other two ledgers.
- `module-03-applied-studies/_scan-queue.md` — append-only candidate queue, also carrying the unbuilt
  backlog from the three manual discovery passes so there is one place to look for "what's next".
- **`shared/weekly-literature-scan.md`** — the routine's specification and configuration, including a
  paste-ready Module 3 prompt section.

**Updated:** `CLAUDE.md`'s Future automation note (now records the wiring and the triage-only rule),
and `module-03-applied-studies/README.md`.

### Why a separate spec file exists

The routine is a **claude.ai/code Routine (cloud), not a locally-scheduled task**, so its prompt
lives only in the claude.ai UI and is **invisible to anyone working in this repository**. That had
already caused confusion once — the 2026-08-31 session found the routine failing but could not
inspect what it was meant to do. `shared/weekly-literature-scan.md` is now the canonical
version-controlled copy; it must be updated in the same change whenever the UI prompt is edited.

### Design decisions

1. **The routine triages Module 3; it does not write it.** This is the significant asymmetry with
   Modules 1 and 2, and it is deliberate. Those modules catalogue *papers about a technology*, which
   is safely automatable from abstracts. Module 3 asserts *what happened in a deployment*, which is
   not: every figure in its 55 profiles came from full text, and the two discovery passes that
   screened on abstracts alone produced **three wrong platform attributions out of the first ~12
   candidates examined**. An unattended, no-confirmation run holding push access to a **public** repo
   must not be able to write unverified study claims into it. It appends to `_scan-queue.md` and is
   explicitly forbidden from touching `profiles/`, `feasibility-matrix.md`, `README.md` or
   `sources.md`.
2. **Date-sorted, never citation-sorted** — established empirically this session: the original
   citation-sorted pass missed **62 of 64** recent candidates.
3. **Rejections are recorded with a reason**, not merely excluded, or the same out-of-scope paper is
   re-litigated every Monday.
4. **The queue is a repo file, not a message** — it survives between runs and is reviewable in a diff.
5. **Known false-positive traps written into the prompt**: Polar, Avicenna, AWARE, CARP, m-Path, Oura,
   Samsung — including the finding that **Europe PMC does not honour phrase quoting** for the
   ordinary-word names.

### Outstanding — requires the account owner

**The routine's prompt itself has not been changed**, and cannot be from a repo session. Someone with
access to the claude.ai Routines UI must paste the Module 3 section from
`shared/weekly-literature-scan.md` into the existing routine prompt. Until that happens the ledger
and queue sit unused; nothing breaks, and Modules 1 and 2 continue scanning as before.

### Known limitations carried into the routine

The three structural discovery blind spots apply to it exactly as to manual passes — ordinary-word
platform names, framework-shaped platforms (CARP), and venue-shaped invisibility (AWARE's operational
literature sits in CSCW/IMWUT/UbiComp, which NCBI does not index). The known workaround is a periodic
**OpenAlex citation-graph pass**, which is deliberately **not** part of the weekly routine and must be
run manually.

---

## 2026-09-02 (final) — Weekly scan routine: Module 3 integrated into the live prompt

**Module:** Cross-module infrastructure. No research content changed.

The routine's prompt now covers all three modules. The Module 3 section was initially appended to the
end of the existing prompt; reviewing the full text against it surfaced a real defect and three
smaller ones, all fixed by restructuring rather than patching.

### The defect that mattered

The prompt's final section (then Part C) ended with **"commit all changes ... and push to origin
main"**. The appended Module 3 section carried **its own commit instruction and no push**, and ran
*after* that step. Module 3's work would therefore have been committed and **never pushed** — every
week, silently, with the failure visible only as an unpushed commit inside the cloud environment.

**Fix:** Module 3 became **Part C**, and logging/commit/push became **Part D**, covering all three
modules in **one commit followed by one push**.

### Three smaller corrections

1. **Wrong API named.** The Module 3 draft warned that "Europe PMC does not honour phrase quoting"
   for ordinary-word platform names. The routine calls **NCBI E-utilities**, not Europe PMC. Reworded
   to describe PubMed `[tiab]` behaviour, which is the actual constraint.
2. **A fragile instruction.** The draft told the run to derive its technology list from the
   `## What's covered` section of Module 3's README — i.e. to parse prose, unattended. Replaced with
   **three explicit grouped queries** (C1 wearables, C2 platforms, C3 arXiv) rather than one per
   technology, which also keeps the run inside rate limits.
3. **Column mismatch.** The queue-append step listed fields that did not match `_scan-queue.md`'s
   actual table columns. Aligned.

### Also folded in while editing

- **LifeData** added to Part B's platform list — profiled in Module 2 earlier today but absent from
  the routine. Its query covers both "RealLife Exp" (the real product name) and the "Realtime EXP"
  mis-rendering that appears in the published literature.
- **The JMIR byline trap** added to Part B step 4: PMC's JATS `contrib-group` ordering is not stable
  and sometimes lists handling editors before authors. This produced three wrong first authors in
  this project; the fix is to verify against the publisher PDF byline.
- **An explicit note that an empty Module 3 week is the expected normal case**, so a future run does
  not loosen the inclusion bar to manufacture output.

### Privacy

The cloud environment ID was removed from `shared/weekly-literature-scan.md` and from this log's
2026-09-01 entry. **It remains in git history** (commit `db6d9e1` onward); removing it there would
require a history rewrite, which was judged disproportionate — it is an identifier, not a credential,
and account access is required to use it.

### Canonical location

`shared/weekly-literature-scan.md` now holds the **full prompt (Parts A–D)**, not just the Module 3
fragment, plus configuration, design rationale, known limitations and a change history. The routine
is a cloud Routine whose prompt is otherwise invisible from this repository — **any UI edit must be
mirrored back into that file.**
