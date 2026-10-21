# Gap hunt: terra (2026-10-11)

Scope: Terra Enabling Developers, Inc. (Delaware; UK subsidiary Terra Enabling Developers Ltd),
"Terra API", tryterra.co, a unified wearable-data API. Compared against
`module-01-wearables/profiles/data-intermediaries.md` (profile; Terra appears only at lines 138, 166,
210, 218 and 238), `module-01-wearables/comparison-matrix.md` (no Terra row; unified APIs mentioned
at lines 365 and 388), `module-01-wearables/README.md` and `facts/terra.yaml` (every field
`unresearched`, so "KB has it" below refers to the profile, matrix and README). Every quote below
returned `exact 1.0` from `tools/facts/quote_probe.py` on 2026-10-11.

The single biggest gap: the KB treats Terra purely as a pipe ("a third-party data processor",
profile line 162). Terra is also a data user. Its End User Privacy Policy lets it run its own
"statistical, scientific, or market research" on pooled end-user data and keep de-identified
derivatives indefinitely; a clause added between October 2025 and February 2026. Terra's in-house
research team has used that pool for a peer-reviewed paper (npj Biological Timing and Sleep, June
2026) and dozens of blog studies. For an IRB this matters: participants routed through Terra become
part of a commercial research dataset by default.

## A. Contradictions and missing programs

### 1. Terra uses end-user data for its own research and publication (KB silent; profile frames Terra only as processor)
- Fields: `ai_training_terms` (secondary use of data, benchmarking), `retention_terms`, `academic_vs_commercial`
- Found: The End User Privacy Policy (last updated 24 September 2026) lists "Generate insights
  (including research and publication)" as a processing purpose under legitimate interest, and
  allows retention of de-identified derivatives beyond the normal two-day window. The October 2025
  version of the same policy limited "Generate insights" to helping connected app developers; the
  research-and-publication wording is present by the 24 February 2026 snapshot.
- URLs and quotes:
  - https://tryterra.co/end-user-privacy
    - "we generate insights and conduct statistical, scientific, or market research related to wearable and health data"
    - "Any such publication or dissemination will contain only aggregated and/or de-identified information and will not identify you."
    - "we may retain aggregated and/or de-identified information derived from your data for longer periods for research, analytics, and service improvement"
    - "Last updated: 24th September 2026"
  - Earlier wording, Wayback 2025-10-16: https://web.archive.org/web/20251016010147/https://tryterra.co/end-user-privacy
    - "Generate insights: by analysing the data we've collected, we generate insights. These insights assist connected app developers in offering improved services or enhancing user experiences"
  - Wayback 2026-02-24 (research wording present): https://web.archive.org/web/20260224075518/https://tryterra.co/end-user-privacy
    - "we generate insights and conduct statistical, scientific, or market research related to wearable and health data"
- Date: policy change between 2025-10-16 and 2026-02-24; current version 2026-09-24. Source type: vendor_legal.
- Note for judge: Terra's December 2025 adherence study (item 2) states it used data from 1 May to
  1 August 2025, a window when the archived policy did not yet name research and publication. The
  general (non-end-user) privacy policy did mention "data analysis, identifying usage trends". This
  is an observation of dates, not a finding of non-compliance.
- KB: **no.** Profile line 162 says only "They add a third-party data processor to the compliance
  surface"; nothing on Terra's own secondary use.

### 2. Terra Research: in-house research team publishing on pooled customer data, including a peer-reviewed paper (KB silent)
- Fields: `research_program` (context: Terra is a research producer, not a research-access program), `ai_training_terms`
- Found: Terra Research, led by Head of Research Alistair Brownlee, publishes weekly analyses on
  pooled wearable data (e.g. 77,000+ nights across six wearables; 93-day adherence across Fitbit,
  Apple Watch, Garmin). Peer-reviewed output: Akhtar, Brownlee & Crawford, "Variation in sleep
  duration across latitudes and countries", npj Biol Timing Sleep 3, 27 (2026),
  doi:10.1038/s44323-026-00092-2, 697 people, 185,143 nights, 49 countries. The paper relies on the
  platform consent, not study-specific consent, and did not go to an NHS REC. Data not shared.
- URLs and quotes:
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC13287479/
    - "All participants were provided notice and consented to Terra’s processing of their data to operate, maintain and improve the Terra platform and to generate aggregated analytics and insights."
    - "NHS Research Ethics Committee review was not required, as confirmed using the HRA decision tool"
    - "The authors are employees of Terra Enabling Developers, which provides the wearable data infrastructure used in this study."
    - "The datasets generated and analysed during the current study are not publicly available"
  - https://tryterra.co/research/terra-research-nature-publication
    - "Author affiliation: Terra Enabling Developers (Terra API)"
  - https://tryterra.co/research/sleep-tracking-accuracy-adherence-analysis
    - "I used data from four wearables over 93 days, from 1 May to 1 August 2025."
    - "our analysis reveals it suffers from the lowest user adherence (69.3%)"
- Date: paper published 2026-06-22; adherence post 2025-12-09. Source types: paper, vendor_page.
- KB: **no.** Also relevant to Module 3 / adherence work (vendor-authored, not peer-reviewed except the npj paper).

### 3. No academic program; the only research route is the Startup Accelerator credits (KB silent)
- Fields: `research_program`, `program_eligibility`, `program_application`, `academic_pricing`, `academic_vs_commercial`
- Found: No academic or research pricing or program. The Startup Accelerator (up to $100k in API
  credits, up to six months) explicitly admits research projects on condition that Terra is
  credited in publications and datasets. A card is required; billing continues on the chosen plan
  when credits end.
- URL and quotes: https://tryterra.co/accelerator
  - "Are research projects eligible? Yes, if health data is central to the work and you credit Terra in any resulting publications and datasets."
  - "Credits last up to six months. Applying is free and we take no equity."
  - "A card is required to activate; nothing is charged while your credit covers your invoices."
- Date: accessed 2026-10-11 (page undated). Source type: vendor_page.
- KB: **no.** Profile line 166 says "Neither publishes academic pricing", which stays true, but the
  accelerator route is not mentioned. Acceptance rate (about 1.8%) appeared only in a search
  summary and was not confirmed on the page, so it is left out.

### 4. Fitbit / Google Health via Terra: Terra says it manages Fitbit credentials and Google Health is GA (possible contradiction with KB's "own Google Cloud project and CASA")
- Fields: `developer_program_status`, `export_routes`, `deprecations`
- Found: Terra's Fitbit integration page says Terra holds the credentials; its August 2026 update
  says Google Health went generally available "in connections" after a summer preview. Neither page
  says whether a Terra customer needs its own Google Cloud project, verification or CASA for the
  Google Health API. Terra's May 2026 guide gives the Fitbit sunset as "September 2026"
  (consistent with Google's 30 September end of support; the KB's 30 October turn-off date is not
  contradicted).
- URLs and quotes:
  - https://tryterra.co/integrations/fitbit : "Terra manages the Fitbit API credentials, so there is nothing to register"
  - https://tryterra.co/blog/august-2026-product-update : "Google Health is now generally available in connections, having been in preview through the summer."
  - https://tryterra.co/blog/everything-you-need-to-know-about-google-health-new-api : "The Fitbit Web API sunsets in September 2026 and existing OAuth tokens do not transfer."
- Date: Aug update published 2026-09-01; guide 2026-05-18. Source type: vendor_page.
- KB: **contradicts or unclear.** `module-01-wearables/README.md` line 124 "Unified APIs need the
  study's own Google Cloud project, verified app and CASA"; data-intermediaries.md line 212 and
  comparison-matrix.md line 365 say the same (Corroborated). Terra's page may describe the legacy
  Fitbit Web API only. Needs a direct question to Terra (or a docs check by the docs researchers)
  before either statement is kept.

### 5. Garmin data through Terra while Garmin's program is closed (KB omits Terra as a route)
- Fields: `developer_program_status`, `export_routes`
- Found: Terra holds its own Garmin credentials as a long-standing partner, so a Terra customer does
  not need its own Garmin Connect Developer Program approval. Terra's own Garmin pause post (already
  cited in the KB as S-GRM-09) says this.
- URLs and quotes:
  - https://tryterra.co/integrations/garmin : "Terra manages the Garmin API credentials, so there is nothing to register"
  - https://tryterra.co/blog/garmin-connect-developer-program-pause : "Terra has maintained a Garmin integration for years as an established partner"
  - same: "Terra is working with Garmin as a partner and will fold any new requirements into its integration"
- Date: post 2026-09-07; integration page accessed 2026-10-11. Source type: vendor_page.
- KB: **no.** Decision heuristic, data-intermediaries.md line 207, names only Labfront and Fitrockr
  as the practical Garmin route "while Garmin's own programme is closed to new applicants". Note
  Garmin Enhanced BBI is licence-fee for commercial use per Terra's own post; whether Terra passes
  BBI through is a docs question.

### 6. Bring-your-own credentials for WHOOP, Strava, Dexcom and Samsung (bears on KB's WHOOP licensing warning)
- Fields: `developer_program_status`, `program_application`, `export_routes`
- Found: For WHOOP, Strava and Dexcom the customer supplies its own developer credentials; for
  Samsung the customer's app needs its own Samsung developer approval. Terra-managed credentials:
  Garmin, Fitbit, Oura, Polar, Withings, Google Fit. Apple Health needs no provider credentials but
  needs a native app (item 9).
- URLs and quotes:
  - https://tryterra.co/integrations/whoop : "You supply your own WHOOP app credentials"
  - https://tryterra.co/integrations/strava : "You supply your own Strava app credentials"
  - https://tryterra.co/integrations/dexcom : "You supply your own Dexcom app credentials"
  - https://tryterra.co/integrations/samsung : "Your app needs its own Samsung developer approval"
  - https://tryterra.co/integrations/oura : "Terra manages the Oura API credentials, so there is nothing to register"
- Date: accessed 2026-10-11. Source type: vendor_page.
- KB: **no.** Profile line 162 to 165 warns that WHOOP's terms bar licensing API data to third
  parties (whoop.md line 119), implying an intermediary is a problem. Terra's design (the study is
  the WHOOP developer; Terra is the study's processor) is the answer the KB does not record. A study
  would still need its own WHOOP, Strava, Dexcom or Samsung approval.

## B. Data terms, compliance and other changes

### 7. Default retention is two days, maximum six months; storage is an Enterprise feature
- Fields: `retention_terms`, `history_depth`
- URLs and quotes:
  - https://tryterra.co/end-user-privacy : "Usually, your data is retained for two days after the point of collection and then automatically deleted."
  - same: "None of your data will be stored in our databases for longer than six months from the point of collection."
  - https://tryterra.co/pricing (Enterprise column) : "Enable data storage for your users"
  - https://tryterra.co/dpa : "Within ninety (90) days following termination or expiration of this DPA"
- Date: policy 2026-09-24; DPA 2026-09-24. Source types: vendor_legal, vendor_page.
- KB: **no.** Practical consequence for researchers: Terra is a pass-through, so the study must run
  its own webhook destination or storage; missed payloads rely on Terra's failsafe or re-requests
  to the provider.

### 8. DPA, sub-processors (including Anthropic and OpenAI on end-user data) and data residency
- Fields: `dpa`, `data_residency`, `ai_training_terms`, `soc2`
- Found: Click-through DPA (updated 2026-09-24) with EU SCCs and UK Addendum, no signature needed.
  Primary processing in the UK and Netherlands, with possible US transfer. Sub-processor list
  (effective 2026-02-10) has AWS and GCP hosting end-user data in US, UK, EU, and lists Anthropic and
  OpenAI for AI-assisted support and debugging "involving end user data", stated as anonymized,
  with an opt-out. DPA Annex says an annual SOC 2 Type II audit.
- URLs and quotes:
  - https://tryterra.co/dpa : "acceptance of the Agreement constitutes execution of this DPA"
  - same: "Vendor's primary processing operations take place in the United Kingdom and the Netherlands"
  - same: "Vendor undergoes annual SOC 2 Type II audit (including the Security, Confidentiality, and Availability Trust Service Criteria)."
  - https://tryterra.co/privacy/subprocessors : "Stores and processes end user data (e.g., health/activity metrics) via Terra’s APIs."
  - same: "Used to assist with customer support queries and debugging involving end user data."
  - same: "Customers may opt out of AI-assisted support by submitting a request through our support portal."
  - same: "Effective Date: 10th February 2026"
- Date: as given. Source type: vendor_legal.
- KB: **no.** All compliance fields in the KB for Terra are only "BAA on Enterprise" (profile line 166).

### 9. BAA only on Enterprise; HIPAA and SOC 2 Type II are self-claims; trust portal is on Vanta
- Fields: `baa`, `hipaa_statement`, `soc2`, `gdpr_statement`, `iso27001`
- Found: BAA listed only on the custom Enterprise plan (KB has this). HIPAA and SOC 2 Type II are
  vendor claims (enterprise page; SOC 2 announced December 2022 on the blog). GDPR page (updated
  2026-03-01) links a downloadable GDPR assessment and a Vanta-hosted trust center
  (https://app.vanta.com/tryterra.co/trust/ta17vkzrua0zm6l68uo2), which renders blank to automated
  fetches, so no audit date, auditor or report was confirmed. No ISO 27001 claim found.
- URLs and quotes:
  - https://tryterra.co/pricing : "Signed BAA (data protection agreement)"
  - https://tryterra.co/enterprise : "we adhere to HIPAA standards and implement rigorous physical, network, and security measures"
  - https://tryterra.co/enterprise : "SOC2 TYPE2"
  - https://tryterra.co/gdpr : "You may download a detailed assessment of Terra's GDPR compliance here"
  - https://tryterra.co/gdpr : "Last updated: March 1st, 2026"
- Source types: vendor_page (self-claims; cap at Reported under `self_claim_cap`).
- KB: **partly yes** (BAA on Enterprise, line 166); SOC 2, HIPAA claim, GDPR assessment and trust portal **no**.

### 10. Apple Health needs a native app; Terra offers its own "Avengers" iOS app as a no-build route
- Fields: `export_routes`
- URL and quotes: https://tryterra.co/community/is-there-an-already-published-app-to-help-us-gather-health-data-from-ios
  - "For iOS (Apple Health), the data is only accessible via our Mobile SDK, there's no cloud API from Apple, so a native app is required."
  - "you can also use Terra's Avengers app to connect users to Apple"
- Date: staff reply about five months before 2026-10-11 (forum shows relative dates only). Source type: secondary (vendor forum, staff reply to a hospital research project).
- KB: **no.** Useful for small BYOD studies that cannot build an iOS app.

### 11. Imputed values: "health context" fills missing days with a per-cell confidence value
- Fields: `derived_metrics`
- URL and quotes: https://tryterra.co/blog/august-2026-product-update
  - "Health context estimates the missing values across sleep, daily and activity data."
  - "every estimated cell carries its own confidence value"
- Date: published 2026-09-01. Source type: vendor_page.
- KB: **no.** Methodological warning for the profile: a study must exclude or flag estimated cells;
  whether health context is opt-in or on by default is not stated in the post.

### 12. Provider rate limits are shared across all of a customer's users; coverage endpoint added
- Fields: `rate_limits`, `history_depth`
- URL and quotes: https://tryterra.co/blog/march-2026-product-update
  - "Providers impose rate limits, and those limits are shared across all of your users rather than being per user."
  - "The month cap that originally limited how far back you could ask about was removed during the same month"
- Date: published 2026-04-01. Source type: vendor_page.
- KB: **no.** The second quote concerns the coverage endpoint, not backfill depth itself.

### 13. Terms of Service: free development accounts are evaluation-only; raw end-user data belongs to the end user
- Fields: `api_platform_fees`, `academic_vs_commercial`, `retention_terms`
- URL and quotes: https://tryterra.co/terms-of-service
  - "Last updated: May 1st, 2026"
  - "Customer may use Development Accounts solely for internal evaluation of the Services to determine whether to place a paid Order"
  - "except for raw End User data, which belongs to the End User"
- Source type: vendor_legal.
- KB: **no.** Rules out running a small pilot study on a free sandbox account.

### 14. Pricing page details beyond the KB entry: dedicated server by region on Enterprise
- Fields: `data_residency`, `api_platform_fees`
- URL and quote: https://tryterra.co/pricing : "Dedicated instance to localised area"
- KB: **no** (KB has the $499/$399 entry price and 100,000 credits, line 166, which still match).

## C. Searched, nothing found

- FDA, CE/MDR: Terra is software infrastructure, no device clearances found; `fda_clearances` is likely not_applicable.
- ISO 27001: no claim on tryterra.co pages checked or in search.
- Independent SOC 2 evidence: Vanta trust portal exists but did not render; no third-party audit report found.
- Funding, acquisition, layoffs, shutdown: nothing after the 2021 $2.8M round (TechCrunch); no 2025 or 2026 events found (search results dominated by unrelated "Terra" companies).
- Pricing or credit changes in the last 12 months: none found beyond the current page; add-on prices (Streaming, Planned Workouts $99 per month plus usage, Lab Reports $499) are on the pricing page.
- Academic studies naming Terra as their collection route: PubMed search for "Terra API"/tryterra returns only Terra's own npj paper; web search found none.
- App Store listing for the Avengers app: not found by search.
- GitHub (github.com/tryterra): 52 public repos, SDKs actively maintained (TerraiOS, terra-react, terra-flutter pushed Sept and Oct 2026, MIT or BSD-3), plus an MCP server (terramcp) and agent-skills repo. Nothing research-specific; no quote taken.
- Partner/integrator pages (Fitabase, Labfront, Thryve) mentioning Terra: none found.
- Job postings, conference talks: nothing decision-relevant found.
- terms-of-purchase page: returned no content (dead fetch).
