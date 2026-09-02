# LifeData profile — handoff report for Module 2 integration

**Written 2026-09-02.** Produced by the LifeData research pass. The only files this pass created are
`profiles/lifedata.md` and this report. Nothing else in the repo was touched; no git commands were run.
No literature PDFs were added (see "PDFs" below).

---

## 1. What LifeData is

**LifeData, LLC** (Marion, Indiana, ~14 years old) sells a commercial **EMA / ESM / eDiary / ePRO /
eCOA** platform. Participant apps + web researcher console, vendor SaaS only, closed source, no API.

**It is not a passive-sensing digital phenotyping platform**, and this is the finding that matters most
for the module. See §5.

**Naming, needed before anything else is filed:** the vendor's product is **RealLife Exp**.
"**Realtime EXP**" — the name in the task brief and in Ball et al. 2025 — is a **literature
mis-rendering**, not a product name. Europe PMC returns exactly **1** hit for `"Realtime EXP"` against
**74** for `"RealLife Exp"`. Any index entry, matrix row, or `sources.md` line should read
**"LifeData (RealLife Exp)"**, with "Realtime EXP" noted as an alias so future searches resolve.

**Two live generations**, presented by the vendor as a current choice, not a completed migration:

| | Original | LifeData+ |
|---|---|---|
| App | RealLife Exp (iOS 2015-01-03, Android 2015-01-11; both updated Apr 2026) | LifeData (iOS 2025-05-28, Android 2025-11-27; updated Jul/Aug 2026) |
| Console | `server.lifedatacorp.com` | `app.lifedatacorp.com` |
| Min iOS | 13.0 | **18.0** |
| Published deployments | ~260 vendor-listed publications, 2016–2026 | **none** |

---

## 2. Comparison dimensions — established vs. non-public

**Established (usable in `comparison-matrix.md`):**

| Dimension | Finding |
|---|---|
| Organization / type / status | LifeData, LLC; commercial SaaS; **Active** (four app-store updates Apr–Aug 2026, site rebuilt 2026, new platform generation 2025–26) |
| iOS / Android | Both, native, two generations. Parity **not independently verified** (per CLAUDE.md, not assumed) |
| Open source | **No** — Verified: no GitHub org (`api.github.com/orgs/lifedatacorp` → 404), zero repos, no SDK |
| Hosting | Vendor SaaS only; **US-only data residency**; onward hosting via **Microsoft Azure** (named in the privacy policy — the most specific hosting disclosure of any commercial platform in this module) |
| Passive sensors | **Response-linked GPS only.** Nothing else. Corroborated across 5 vendor pages + 2 app-store listings + 2 Play data-safety declarations |
| Survey / EMA | **Deepest documented scheduling engine in the module** — fixed/random/triggered/event-based with configurable minimum inter-prompt spacing; branching; two trigger types incl. one that activates an entire new schedule (EMI/JITAI-adjacent); 13 question types; display logic, piped text, computed scores, adaptive automation; offline collection; RTL languages |
| Raw data access / export | CSV + media; "multiple formats… including multilevel modeling"; millisecond notification/response timestamps; real-time dashboards |
| API | **None public.** No SDK, webhook, or DB access. `api.lifedatacorp.com` resolves but 404s on `/`, `/docs`, `/swagger`, `/v1`, `/api-docs`, `/health` |
| Self-hosting | **No** |
| Study management | Web builder, roles/permissions, institutional master subscriptions with department sub-accounts, multi-site (Clinical tier), QR/link/code onboarding, researcher-assigned IDs, real-time alerts on responses/scores/events |
| Participant monitoring | Real-time engagement/response-rate dashboards, smart reminders |
| Wearable / HealthKit / Health Connect / FHIR | **None documented anywhere** |
| Retention & deletion | **Numeric and Verified**: 180 days post-cancellation; ≤30 days for researcher-initiated deletion; 12-month inactivity termination. Most specific in the module |
| Privacy / compliance | **EU-U.S. DPF + UK Extension + Swiss-U.S. DPF** self-certified to the U.S. Dept of Commerce, FTC jurisdiction, binding arbitration; **GDPR processor** role. See §4 for the HIPAA problem |
| Evidence of use | ~260 vendor-listed publications 2016–2026 (26 from 2026); 74 Europe PMC hits for `"RealLife Exp"`; Harvard/Stanford/Yale/Cambridge/HKU etc. |
| Technical burden | **Lowest in the module** — zero infrastructure |
| Operational support | Heaviest paid-services menu in the module (10 named services incl. protocol building, UAT, site training, methodological consultation) |

**Non-public / requires vendor contact:**

- **All pricing.** No `/pricing` page (404), no free tier or trial advertised. Model *is* public
  (researcher-count × duration × participant-count; five tiers; grad-student discount; all features
  included in every tier; multi-project at no extra cost) — figures are not.
- **All researcher documentation.** The help centre (`support.lifedatacorp.com`) is **entirely
  login-gated**: HTTP 403 to anonymous fetch, Zendesk API returns `"Couldn't authenticate you"`. No
  data dictionary, export schema, permission model, or scheduling reference is publicly readable.
  **This is the worst documentation opacity of any platform in the module** — worse than MetricWire,
  whose site is bot-blocked but whose feature pages are at least indexed.
- iOS/Android parity per stream; encryption at rest; data latency; EU/UK residency option; BAA
  availability; SOC 2 / ISO 27001 / 21 CFR Part 11; LifeData+ vs Original end-of-support and
  migration path.

---

## 3. Maintenance status: **Active**, with a stale-marketing caveat

- **Active:** four app-store listings updated Apr–Aug 2026; site rebuilt 2026 (© 2026, Elementor asset
  timestamps); a whole new platform generation shipped 2025–26; staffed team page (CEO, two PhD
  co-founders, five engineers, a designer); publication list carrying 26 entries from 2026.
- **Stale:** blog dead since **2024-07-30** (WordPress post sitemap `lastmod`); the footer "Products"
  link points at `?page_id=23768`, which returns the site's own 404 page.
- Verdict: website neglect, not product abandonment. No abandonment signal found.

---

## 4. vs. MetricWire and Avicenna Research

| | LifeData | MetricWire | Avicenna Research |
|---|---|---|---|
| Public feature detail | **Best of the three** — scheduling/logic documented to a level neither competitor matches | Thin (site 403s; feature list is a search-summary characterization) | Good (`avicennaresearch.dev`) |
| Researcher docs | **Worst — fully login-gated** | Site bot-blocked but indexed | Public feature docs |
| Evidence of use | **Strongest** — ~260 publications 2016–2026, decade-long trail | Weakest — no publication list located across two passes | Academic lineage (Ethica/iEpi), no count attempted |
| Pricing | Non-public; **model** unusually clearly described | Non-public; "Site Licence" tier hinted | Non-public; free trial (third-party Reported) |
| Compliance | DPF-certified + numeric retention terms; **HIPAA claim marketing-only** | **Nothing located across two passes** — weakest | **Strongest** — ISO 27001:2022, dated, audited, zero nonconformities |
| API | None; not even an unofficial client | None public, but a private **"Catalyst"** API is evidenced | None confirmed |
| Export | CSV + media, multilevel-model-ready layouts | Not verified | CSV, JSON, GEXF, KML; "minutes after upload" |
| Passive sensing | GPS-with-response only | "Passive sensor and geolocation capture" claimed, catalog unverified | "Wide range of smartphone sensors and wearables," catalog unverified |

Rough placement: **LifeData beats both on evidence-of-use and on documented EMA depth; beats MetricWire
on compliance and loses to Avicenna on it; loses to both on public documentation accessibility.**

**Bonus finding for `metricwire.md` (I did not edit that file):** Ball et al. 2025 **independently
confirms from peer-reviewed full text** that MetricWire's participant app is called **"Catalyst"** —
`metricwire.md` currently rests that name on an unofficial third-party Python client (`zeolite`) alone.
That is a genuine **Reported → Corroborated** upgrade, and Ball et al. is also the only published
**head-to-head LifeData/MetricWire deployment** (a mid-study platform switch inside one cohort), so it
is worth citing in both profiles.

---

## 5. Are the two Module 3 studies unblocked? **Yes for the scope rule — with a caveat worth a decision.**

Both are now **verified from full text**, not abstracts:

- **Nock et al. 2026** (`10.1037/abn0001117`, PMC13308188, **not OA**): "installed an app on their
  smartphone (**LifeData**)." N=619; 502/619 (**81.1%**) provided any data; **79,448** surveys started;
  rolling median/mean initialization **<50% and declining** over three months. Predictors were survey
  responses plus "passively collected survey **meta-data**."
- **Ball et al. 2025** (`10.1016/j.beth.2025.05.007`, PMC13289574, OA): "**Due to platform changes
  during the study, 90% (n = 90) received EMA through the smartphone application (app) Realtime EXP by
  LifeData, and 10% (n = 10) received EMA through the smartphone app Catalyst by MetricWire.**"

The scope rule ("platform already profiled in Module 1 or 2") is satisfied. Both are flagged as Module 3
candidates in `profiles/lifedata.md` under "Module 3 candidates — two deployments identified". I wrote
no Module 3 files.

**The caveat, flagged rather than decided:** LifeData is an **EMA/ePRO platform, not a digital
phenotyping platform** in this module's passive-sensing sense. Its only sensor stream is GPS captured
*with a response* — vendor wording, repeated verbatim across five pages: "Gather GPS coordinates with
each user response," "Collect participants' geolocation when they respond, if needed." No
accelerometer, screen/app usage, communication metadata, Bluetooth, audio, wearable, HealthKit, Health
Connect, or FHIR anywhere on the public site. Google Play data-safety declares only "Location, Personal
info and 3 [or 4] others." Nock et al.'s "passive" metadata is **survey response metadata, not phone
sensors**.

So the two studies are **smartphone-EMA deployments, not digital-phenotyping deployments**. Three
things follow, and they are yours to decide, not mine:

1. Module 3's stated remit — *"used one or more Module 1 devices and/or Module 2 platforms as its
   data-collection instrument"* — is met on its face. Both belong.
2. But if Module 3 is implicitly meant to be about *phenotyping* deployments, admitting these two
   quietly widens it to *any* app-based EMA study. Worth an explicit line in Module 3's README either
   way, since these two will be the precedent.
3. Their operational value is real and independent of that question: **81.1% any-data rate**, **<50%
   and declining prompt-initialization over three months** in a high-acuity psychiatric sample, and a
   **mid-study platform migration inside a live cohort** are exactly the failure modes
   `feasibility-matrix.md` exists to record. They also happen to come from the same Harvard/Boston
   research programme, so they are **not independent replications** of each other — worth a note in the
   matrix.

If Module 2's own boundary is being kept strict, the cleanest resolution is to keep LifeData in Module 2
but label it explicitly in `README.md` and `comparison-matrix.md` as **EMA/ePRO-only, not passive
sensing** — the profile already carries a "Scope note" section written for exactly that purpose, and
the module README's existing three-posture framing (self-hosted OSS / managed SaaS / build-your-own
framework) may want a fourth axis, or a footnote, distinguishing sensing breadth from EMA depth.

---

## 6. What needs direct vendor contact

Fourteen numbered questions are in the profile's Open Questions section. The five that would actually
block a study-design decision:

1. **Will LifeData sign a BAA, and what backs the site-wide "HIPAA compliant" claim?** — the privacy
   policy and terms of use mention HIPAA **zero times**; one page even misspells it "HIPPA." Per
   CLAUDE.md this must not be inferred from marketing. Recorded as **Unclear**.
2. **SOC 2 / ISO 27001 / 21 CFR Part 11** — none appear anywhere, despite a marketed "Clinical" eCOA
   tier for regulated multi-site trials.
3. **Actual pricing**, incl. service-menu rates (**audit trails are sold as bespoke work**, not a
   shipped feature — a likely surprise for anyone assuming audit logging is included).
4. **EU/UK data residency** — US-only storage is documented; DPF certification is the vendor's answer
   to EU data flows, not in-region hosting. Likely disqualifying under some European institutional
   policies.
5. **LifeData+ vs Original** — no end-of-support date, no migration path, and the entire published
   evidence base attaches to the Original app while LifeData+ requires **iOS 18.0** (a real recruitment
   constraint for older participant devices).

---

## 7. Integration notes / suggested matrix cells

- Table 1: `**LifeData (RealLife Exp)** | LifeData, LLC (Marion, IN) | Commercial SaaS | Active, founded ~2012, apps shipping since 2015; two live generations (Original / LifeData+, 2025–26) | Closed source`
- Table 2: iOS Yes (native) / Android Yes (native) / parity **not independently verified**
- Table 3: Open source **No** (Verified via GitHub 404) | Self-hosting **No** | Hosting requirement **None — fully managed**
- Sensor table: consider a dedicated cell or footnote — **"GPS only, captured with each response; no
  background/continuous sensing documented"** — since a bare "GPS: Yes" would badly overstate it
  alongside Beiwe/RADAR-base/AWARE.
- Pricing table: **Non-public, quote-only; no free tier advertised**; note that the pricing *formula*
  (researchers × duration × participants, all features included, unlimited parallel projects) is
  public even though figures are not, and that a graduate-student discount exists.
- Compliance table: **EU-U.S. DPF / UK Extension / Swiss-U.S. DPF self-certified (Corroborated —
  externally checkable at dataprivacyframework.gov, automated verification blocked this pass);
  GDPR processor; US-only residency; Azure-hosted; HIPAA Unclear (marketing-only); SOC 2 / ISO 27001 /
  Part 11 absent.** This makes LifeData the **second-best-documented compliance posture** among the
  commercial platforms, behind Avicenna Research and ahead of MetricWire.
- README §4 (pricing) and §5 (compliance) both need LifeData added: it joins Avicenna and MetricWire in
  the "requires vendor contact" pricing group (now 3 of 4 commercial platforms), and joins the
  "has *some* documented compliance evidence" group alongside Avicenna and m-Path.
- `unresolved-questions.md`: 14 new items are drafted in the profile's Open Questions section, all
  addressed to `contact@lifedatacorp.com` / `support@lifedatacorp.com` / the consultation booking page.

---

## 8. PDFs

**None added; `literature/lifedata/` was not created.** Both target papers resisted PDF retrieval:

- **Ball et al. 2025** is open access, but Europe PMC's `fullTextPDF` endpoint returns **404** for
  PMC13289574 and PMC's own PDF routes return an HTML challenge page to automated requests. Full text
  *was* obtained and read via `fullTextXML`, so every quotation in the profile is verified verbatim
  from full text.
- **Nock et al. 2026 is not open access.** Full text was obtained via NCBI `efetch` (`db=pmc`,
  `id=13308188`) and read; per the project's standing rule, it is flagged as **paywalled**, and no PDF
  is stored.

Both are recorded with DOI, PMID and PMCID in the profile's Sources so a future pass — or the Module 3
agent, who owns these studies — can retry retrieval.
