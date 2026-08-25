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
| Pricing model | Not established this session |
| Last verified | 2026-08-24 |

## Summary

m-Path is a no-code, point-and-click ESM/EMA (Experience Sampling Method / Ecological Momentary Assessment) platform built for researchers and clinicians with limited programming skills, distinguishing itself from most other platforms in this module by leading with EMA/EMI (Ecological Momentary Intervention) design sophistication rather than passive sensing. Passive mobile sensing is offered as a **separate module, "m-Path sense,"** layered onto the core EMA product rather than being the platform's primary identity — an architecture worth noting explicitly, since it means a team choosing m-Path for its EMA strengths needs to confirm m-Path sense meets their passive-sensing needs as a distinct evaluation, not assume parity with dedicated sensing-first platforms.

The platform is documented in a peer-reviewed methods paper (Frontiers in Digital Health, 2023) describing it as supporting "smartphone-based ESM/EMA studies with mobile sensing, wearable triggers, cognitive tasks, and integrated EMI/JITAI interventions" — i.e., it explicitly supports **Just-In-Time Adaptive Intervention (JITAI)** designs, where sensed context can trigger an intervention rather than only a survey prompt. This is a distinctive, well-documented capability among the platforms in this module.

## Products / Platform Architecture

- **m-Path** — the core web-based ESM/EMA/EMI study-builder and app.
- **m-Path sense** — the passive mobile-sensing module (GPS, Bluetooth, pedometer, and other embedded smartphone sensors per the vendor's own description).
- Wearable-triggered assessment ("wearable triggers") is explicitly named, implying integration with external wearable signals to trigger EMA prompts — not independently verified in depth this session.

## Sensors and Data Streams

Per the vendor's own materials, m-Path sense captures location, Bluetooth-based proximity/social-context signals, pedometer/activity data, and (per the general framing) noise/environmental context — used to "unobtrusively acquire objective information about participants' current surroundings... and behavior." Exact sampling configurability and iOS-vs-Android parity were **not independently verified against current developer documentation** this session.

## Active Data Collection

This is m-Path's core strength: point-and-click design of "complex and highly adjustable EMA and EMI designs with advanced functionalities" without requiring programming skill, per the peer-reviewed methods paper describing the platform. Explicit support for JITAI (context-triggered intervention delivery, not just context-triggered surveys) is a distinctive, published capability.

## Researcher and Study Management Features

Not independently verified in depth this session beyond the web-based, no-code study-builder interface described in the platform's own and peer-reviewed materials.

## Data Access and Export

Not independently verified this session.

## APIs, SDKs, and Extensibility

Not independently verified this session.

## Deployment and Infrastructure

Vendor-hosted; no self-hosting option identified.

## Privacy, Security, and Compliance

Not independently verified this session.

## Pricing

Not established this session — no pricing information was located in available materials; flagged as requiring vendor contact.

## Research Evidence and Validation

The core platform methodology is documented in a peer-reviewed, open-access methods paper: Mestdagh M, Verdonck S, Piot M, Niemeijer K, Kilani G, Tuerlinckx F, Kuppens P, Dejonckheere E, "m-Path: an easy-to-use and highly tailorable platform for ecological momentary assessment and intervention in behavioral research and clinical practice," *Frontiers in Digital Health* 2023;5:1182175 (CC BY, Verified open access — confirmed via the retrieved full-text PDF, see `../literature/m-path/2023-mestdagh-frontiersdigitalhealth-m-path-platform.pdf`), also indexed on PubMed. This is a stronger methods-paper foundation than several other commercial platforms in this module, which typically rely only on vendor marketing materials rather than a dedicated peer-reviewed platform-description paper.

## Strengths

- Dedicated peer-reviewed methods paper describing the platform's design and capabilities — a stronger evidentiary foundation than most commercial competitors in this module.
- No-code, point-and-click EMA/EMI study design, explicitly aimed at researchers/clinicians without programming background.
- Explicit, published support for JITAI (context-triggered intervention, not just context-triggered survey) designs.
- Wearable-triggered assessment is a named integration point, potentially useful for studies pairing this platform with a Module 1 wearable ecosystem.
- Reported use by 250+ universities (vendor claim — Reported, not independently verified).

## Limitations

- Passive sensing (m-Path sense) is an add-on module rather than the platform's core identity; its depth relative to dedicated sensing-first platforms (Beiwe, RADAR-base, AWARE) was not independently benchmarked this session.
- Closed-source, vendor-hosted only.
- Pricing, compliance documentation, data export mechanics, and API availability were not independently established this session — a substantial detail gap.
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

- What is m-Path sense's full current sensor catalog, and how does it compare in depth to dedicated passive-sensing platforms?
- What is the pricing model (per-study, per-participant, institutional licence)?
- What compliance documentation (GDPR — relevant given apparent EU/Belgium origin — HIPAA, etc.) exists?
- Is there a documented developer API for data export or integration?
- What wearable devices are supported for "wearable triggers," and through what integration mechanism?

## Key Links

- Official site: https://m-path.io/
- Manual/knowledge base: https://m-path.io/manual/knowledge-base/welcome-to-m-path/
- Research page: https://m-path.io/landing/research/

## Sources

1. m-Path — official site. https://m-path.io/ (accessed 2026-08-24, search summary). **Primary.** Platform framing, m-Path sense module, JITAI/EMI support.
2. Mestdagh M, Verdonck S, Piot M, Niemeijer K, Kilani G, Tuerlinckx F, Kuppens P, Dejonckheere E. "m-Path: an easy-to-use and highly tailorable platform for ecological momentary assessment and intervention in behavioral research and clinical practice." *Frontiers in Digital Health* 2023;5:1182175. https://www.frontiersin.org/journals/digital-health/articles/10.3389/fdgth.2023.1182175/full ; PMC mirror: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10619650/ ; full-text PDF retrieved and verified, CC BY (accessed 2026-08-24, Direct — see `../literature/m-path/2023-mestdagh-frontiersdigitalhealth-m-path-platform.pdf`). Peer-reviewed platform-description paper.
3. m-Path — Research page. https://m-path.io/landing/research/ (accessed 2026-08-24, search summary). "250+ Universities" user-base claim — Reported, not independently verified.
