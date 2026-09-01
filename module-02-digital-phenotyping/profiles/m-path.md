# m-Path

## Quick Facts

| Field | Details |
|---|---|
| Organization | KU Leuven-affiliated research team (m-Path); commercialized as a platform serving 250+ universities per vendor claim |
| Category | ESM/EMA platform with an add-on passive-sensing module |
| Current status | Active |
| Platforms/devices | Mobile app (regular m-Path) plus "m-Path sense" for passive sensing; web-based point-and-click study builder |
| Open source | No (platform); underlying methodology published in peer-reviewed literature |
| Hosting/deployment | Vendor-hosted |
| Pricing model | **Resolved 2026-08-25**: tiered SaaS subscription (Free/Essential/Standard/Comfort, published rates) plus separately priced add-ons (sensing, API access, cognitive tests, white-label, etc.) |
| Last verified | 2026-08-25 (second pass) |

## Summary

m-Path is a no-code, point-and-click ESM/EMA (Experience Sampling Method / Ecological Momentary Assessment) platform built for researchers and clinicians with limited programming skills, distinguishing itself from most other platforms in this module by leading with EMA/EMI (Ecological Momentary Intervention) design sophistication rather than passive sensing. Passive mobile sensing is offered as a **separate module, "m-Path sense,"** layered onto the core EMA product rather than being the platform's primary identity — an architecture worth noting explicitly, since it means a team choosing m-Path for its EMA strengths needs to confirm m-Path sense meets their passive-sensing needs as a distinct evaluation, not assume parity with dedicated sensing-first platforms.

The platform is documented in a peer-reviewed methods paper (Frontiers in Digital Health, 2023) describing it as supporting "smartphone-based ESM/EMA studies with mobile sensing, wearable triggers, cognitive tasks, and integrated EMI/JITAI interventions" — i.e., it explicitly supports **Just-In-Time Adaptive Intervention (JITAI)** designs, where sensed context can trigger an intervention rather than only a survey prompt. This is a distinctive, well-documented capability among the platforms in this module.

## Products / Platform Architecture

- **m-Path** — the core web-based ESM/EMA/EMI study-builder and app.
- **m-Path sense** — the passive mobile-sensing module (GPS, Bluetooth, pedometer, and other embedded smartphone sensors per the vendor's own description). **Updated 2026-08-25 (second pass, Verified via direct fetch of `m-path.io/pricing/`):** m-Path sense is not merely "an add-on module" in a loose sense — it is a **separately priced product line** with two tiers, "Sensing Lite" (€3,000) and "Sensing Full" (€10,000), confirming quantitatively that passive sensing sits entirely outside the base subscription tiers.
- Wearable-triggered assessment ("wearable triggers") is explicitly named, implying integration with external wearable signals to trigger EMA prompts — not independently verified in depth this session. A separate "Smartwatch Integration" add-on (€3,000) is also listed on the pricing page, suggesting wearable-trigger support itself may be gated behind this specific add-on rather than included by default — this is an inference from the pricing page's structure, not a directly confirmed statement, and is flagged as a new open question below.

## Sensors and Data Streams

Per the vendor's own materials, m-Path sense captures location, Bluetooth-based proximity/social-context signals, pedometer/activity data, and (per the general framing) noise/environmental context — used to "unobtrusively acquire objective information about participants' current surroundings... and behavior." Exact sampling configurability and iOS-vs-Android parity were **still not independently verified against current developer documentation** this session — a direct fetch of the manual's "Welcome to m-Path" landing page did not surface sensor-level or platform-parity detail; the specific sensor sub-pages of the manual were not reached this pass.

## Active Data Collection

This is m-Path's core strength: point-and-click design of "complex and highly adjustable EMA and EMI designs with advanced functionalities" without requiring programming skill, per the peer-reviewed methods paper describing the platform. Explicit support for JITAI (context-triggered intervention delivery, not just context-triggered surveys) is a distinctive, published capability.

## Researcher and Study Management Features

Not independently verified in depth this session beyond the web-based, no-code study-builder interface described in the platform's own and peer-reviewed materials.

## Data Access and Export

Not independently verified this session.

## APIs, SDKs, and Extensibility

**Updated 2026-08-25 (second pass, Verified via direct fetch of `m-path.io/pricing/`).** A developer API is confirmed to exist — **"API Access" is a named, separately priced add-on (€5,000)** on m-Path's own pricing page. This resolves the prior "not independently verified" status to Verified-present, but with an important qualifier CLAUDE.md's evidence standard calls for: the API is not a free/included capability the way it is on some competitors — it is a specific, priced commercial add-on, and no API *documentation* (endpoints, auth model, data schema) was located or fetched this session. Whether it is a full researcher-facing REST API or a narrower integration hook was not established.

## Deployment and Infrastructure

Vendor-hosted; no self-hosting option identified.

## Privacy, Security, and Compliance

**Updated 2026-08-25 (second pass, Corroborated via direct fetch of `m-path.io`'s homepage plus a targeted search).** m-Path's own homepage states directly: "Secure data processing and storage, compliant with GDPR and HIPAA." This is a vendor self-declared compliance claim, not an independently audited certification (contrast Avicenna Research's dated, audited ISO 27001:2022 certificate found this same pass) — per CLAUDE.md's instruction not to manufacture certainty, this is recorded as **Corroborated** (a specific, findable claim on the vendor's own primary page) rather than **Verified** (which would require third-party audit evidence, not located this session). Additional corroboration: m-Path is confirmed as "an original spin-off from KU Leuven's research group Quantitative Psychology and Individual Differences" (search-summary source), consistent with the platform's already-noted Belgium/KU Leuven academic origin, and a dedicated `m-path.io/Privacy_Policy_m-Path_Sense.html` privacy policy exists specifically for the sensing module — evidence the vendor treats sensing data's privacy posture as materially distinct from the core EMA product's. No SOC 2, ISO 27001, or DPA-template document was located.

## Pricing

**Resolved 2026-08-25 (second pass, resolving unresolved-question #93's pricing component, Verified via direct fetch of `m-path.io/pricing/`).** Full published tier structure:

| Tier | Annual cost | Participants/year | Notable inclusions |
|---|---|---|---|
| Free | €0 | 50 | Basic data export, questionnaire editor, response visualization, client personalization, manual/community support |
| Essential | €1,599–€2,958 (scales with participant count) | 300–600 | Advanced data export, automatic scheduler, participant management |
| Standard | €2,099–€3,616 | 300–600 | + priority email support, unlimited projects/accounts, collaboration, add-on selection |
| Comfort | €3,099–€5,338 | 300–600 | + online-meeting support, advanced troubleshooting, yearly workshop, yearly study review |

**Add-ons** (all separately priced, confirmed on the same page): Cognitive Tests (€4,500), Sensing Lite (€3,000), Sensing Full (€10,000), Intervention Editor (€6,000), Moodboard Editor (€6,000), Smartwatch Integration (€3,000), White-Label App (€10,000), API Access (€5,000), plus unpriced custom consulting/development options.

This is now among the most transparent, itemized pricing structures in this module — more granular than Beiwe's BSC figures and far more so than Avicenna Research's or RADAR-base's still-nonpublic rates. It also materially reframes m-Path's earlier "no-code EMA platform with a passive-sensing add-on" description: sensing, API access, and smartwatch integration are all priced *well above* even the top Comfort subscription tier's base cost, meaning a full-featured deployment (EMA + sensing + API + wearable triggers) could plausibly cost more in add-ons than in the base subscription. That combination was not priced as a bundle by any source found this session.

## Research Evidence and Validation

The core platform methodology is documented in a peer-reviewed, open-access methods paper: Mestdagh M, Verdonck S, Piot M, Niemeijer K, Kilani G, Tuerlinckx F, Kuppens P, Dejonckheere E, "m-Path: an easy-to-use and highly tailorable platform for ecological momentary assessment and intervention in behavioral research and clinical practice," *Frontiers in Digital Health* 2023;5:1182175 (CC BY, Verified open access — confirmed via the retrieved full-text PDF, see `../literature/m-path/2023-mestdagh-frontiersdigitalhealth-m-path-platform.pdf`), also indexed on PubMed. This is a stronger methods-paper foundation than several other commercial platforms in this module, which typically rely only on vendor marketing materials rather than a dedicated peer-reviewed platform-description paper.

## Strengths

- Dedicated peer-reviewed methods paper describing the platform's design and capabilities — a stronger evidentiary foundation than most commercial competitors in this module.
- No-code, point-and-click EMA/EMI study design, explicitly aimed at researchers/clinicians without programming background.
- Explicit, published support for JITAI (context-triggered intervention, not just context-triggered survey) designs.
- Wearable-triggered assessment is a named integration point, potentially useful for studies pairing this platform with a Module 1 wearable ecosystem.
- Reported use by 250+ universities (vendor claim — Reported, not independently verified).

## Limitations

- Passive sensing (m-Path sense) is a **separately priced** add-on module (€3,000–€10,000/year on top of the base subscription), not the platform's core identity or an included capability; its depth relative to dedicated sensing-first platforms (Beiwe, RADAR-base, AWARE) was not independently benchmarked this session.
- Closed-source, vendor-hosted only.
- ~~Pricing... were not independently established this session~~ — **resolved 2026-08-25**: full tier and add-on pricing is now public (see Pricing above). Data export mechanics and API-endpoint-level documentation remain unestablished; compliance is now Corroborated (vendor's own GDPR/HIPAA claim) but not independently audited.
- API access, smartwatch/wearable-trigger integration, and full sensing are all **additional paid add-ons on top of even the top subscription tier** — a materially higher realistic cost than the base subscription price alone suggests for any study wanting the platform's full-featured combination.
- The "250+ Universities" user-base figure is a vendor claim not independently corroborated.

## Best-Fit Use Cases

- Studies whose primary design need is sophisticated, no-code EMA/EMI/JITAI logic, with passive sensing as a secondary/supporting data stream.
- Clinical or blended-care contexts where non-programmer clinicians need to design their own assessment/intervention protocols.
- Studies pairing wearable-triggered prompts with EMA.

## Poor-Fit Use Cases

- Studies where passive sensing depth and breadth (not EMA sophistication) is the primary requirement — dedicated sensing platforms should be evaluated first.
- Teams needing self-hosting or full source-code control.

## Open Questions

*(Directed to: m-Path — via https://m-path.io)*

- What is m-Path sense's full current sensor catalog, and how does it compare in depth to dedicated passive-sensing platforms? (still open — pricing tier now known, sensor-level detail is not)
- ~~What is the pricing model?~~ **Resolved 2026-08-25** — see Pricing above.
- ~~What compliance documentation (GDPR, HIPAA) exists?~~ **Largely resolved 2026-08-25** — vendor states GDPR + HIPAA compliance directly (Corroborated, not independently audited). SOC 2/ISO status and a formal DPA template remain unconfirmed.
- ~~Is there a documented developer API?~~ **Resolved (existence) 2026-08-25** — "API Access" is a named €5,000/year add-on. **New sub-question**: what does the API actually expose (endpoints, auth, data schema), and is documentation available before purchase?
- What wearable devices are supported for "wearable triggers," and is this the same as, or distinct from, the separately priced "Smartwatch Integration" (€3,000) add-on found on the pricing page this pass?
- Does the Free tier's "50 participants/year" cap reset annually or is it a lifetime/rolling cap, and is academic/non-profit pricing distinct from the published tiers?

## Key Links

- Official site: https://m-path.io/
- Manual/knowledge base: https://m-path.io/manual/knowledge-base/welcome-to-m-path/
- Research page: https://m-path.io/landing/research/

## Sources

1. m-Path — official site. https://m-path.io/ (accessed 2026-08-24, search summary). **Primary.** Platform framing, m-Path sense module, JITAI/EMI support.
2. Mestdagh M, Verdonck S, Piot M, Niemeijer K, Kilani G, Tuerlinckx F, Kuppens P, Dejonckheere E. "m-Path: an easy-to-use and highly tailorable platform for ecological momentary assessment and intervention in behavioral research and clinical practice." *Frontiers in Digital Health* 2023;5:1182175. https://www.frontiersin.org/journals/digital-health/articles/10.3389/fdgth.2023.1182175/full ; PMC mirror: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10619650/ ; full-text PDF retrieved and verified, CC BY (accessed 2026-08-24, Direct — see `../literature/m-path/2023-mestdagh-frontiersdigitalhealth-m-path-platform.pdf`). Peer-reviewed platform-description paper.
3. m-Path — Research page. https://m-path.io/landing/research/ (accessed 2026-08-24, search summary). "250+ Universities" user-base claim — Reported, not independently verified.
4. m-Path — homepage (second-pass direct fetch). https://m-path.io/ (accessed 2026-08-25). **Primary/Direct.** "Secure data processing and storage, compliant with GDPR and HIPAA" (vendor self-declared, Corroborated not Verified).
5. m-Path — Pricing. http://m-path.io/pricing/ (accessed 2026-08-25, second pass). **Primary/Verified.** Full tier structure (Free/Essential/Standard/Comfort) and add-on pricing (Sensing Lite/Full, API Access, Smartwatch Integration, Cognitive Tests, Intervention Editor, Moodboard Editor, White-Label App). Resolves unresolved-question #93's pricing component.
6. m-Path — "Welcome to m-Path" manual landing page (second-pass direct fetch). https://m-path.io/manual/knowledge-base/welcome-to-m-path/ (accessed 2026-08-25). **Primary/Direct, limited yield.** Confirmed no sensor-level or pricing/API detail present on this specific landing page — the manual's deeper sensor-specific sub-pages were not reached this pass.
7. Search-summary corroboration of m-Path's KU Leuven spin-off origin and GDPR-specific privacy commitments (accessed 2026-08-25, search summary, not a single direct-fetched primary page — synthesized from m-path.io and m-path.io/Privacy_Policy_m-Path_Sense.html search results).
