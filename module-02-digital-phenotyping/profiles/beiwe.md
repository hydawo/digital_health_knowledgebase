# Beiwe

## Quick Facts

| Field | Details |
|---|---|
| Organization | Onnela Lab, Harvard T.H. Chan School of Public Health |
| Category | Open-source smartphone digital phenotyping platform (passive sensing + active EMA) |
| Current status | Active — commits to `beiwe-backend` and `beiwe-ios` observed as recently as Jan–Feb 2026 |
| Platforms/devices | Native iOS and Android apps ("Beiwe2") |
| Open source | Yes — BSD-3-Clause across backend, iOS, and Android repos |
| Hosting/deployment | Self-hosted on AWS (own account), or managed via the Beiwe Service Center (BSC) |
| Pricing model | Software free; self-hosting incurs AWS costs; BSC is a paid managed service with study-specific quoted pricing |
| Last verified | 2026-08-24 |

## Summary

Beiwe is Harvard's open-source smartphone platform for high-throughput digital phenotyping, developed and maintained by the Onnela Lab. It pairs a configurable iOS/Android data-collection app with a Django/AWS backend for study management, and hands off analysis to a companion Python package, **Forest**, that the same lab develops. The platform is BSD-3-licensed end to end, so a technically capable research team can self-host on its own AWS account at zero licence cost, or use the **Beiwe Service Center (BSC)** — the Onnela Lab's own managed-hosting service — to avoid running the infrastructure themselves.

This knowledge base's owner works professionally with the Beiwe Service Center. The assessment below is written to the same evidence standard as every other profile in this knowledge base: documented facts only, vendor/lab claims held to "Reported" unless independently corroborated, and limitations stated as plainly as strengths.

## Products / Platform Architecture

- **Beiwe2 apps** (iOS, Android) — passive sensor collection plus configurable surveys/EMA, available on the App Store / Play Store for use with open-source backend deployments, or sideloaded.
- **beiwe-backend** — Django application deployed on AWS (S3 for raw data storage, EC2 for app servers, Elastic Beanstalk for scaling, RDS/PostgreSQL for the study database). Provides the researcher-facing study-management web portal.
- **Forest** — a separate, Onnela-Lab-maintained Python package (BSD-3) that turns Beiwe's raw passive data into processed/summary statistics (mobility metrics, sociability metrics, etc.). Forest can run standalone against exported raw data, or be invoked from within a Beiwe backend deployment to generate on-demand daily/hourly summaries stored back in the study's relational database.
- **Beiwe Service Center (BSC)** — a paid, Onnela-Lab-run instance of the same open-source stack. Studies run on the lab's own production AWS deployment rather than the researcher's; BSC adds study design consultation, IRB-documentation assistance, a beta-testing phase, participant support, and final analysis using production Forest packages.

## Beiwe and Forest — relationship, stated precisely

Beiwe and Forest are **separate open-source repositories with separate release cadences**, developed by the same lab, designed to be used together but not bundled as one artifact. Beiwe collects and stores raw sensor and survey data; Forest is the analysis layer that turns that raw data into derived, research-usable metrics (e.g., mobility statistics from GPS, sociability statistics from call/text logs). A study can use Beiwe without Forest (working directly from raw exports) or use Forest against Beiwe data collected years earlier. The BSC packages both together as part of its managed service, but that is a service-delivery choice, not evidence that the two are architecturally fused. **Verified** from `onnela-lab/beiwe-backend` and `onnela-lab/forest` READMEs and the Onnela Lab's own platform page.

## Sensors and Data Streams

Passive: GPS/location trajectories, accelerometer, gyroscope, call logs (metadata), text/SMS logs (metadata), Wi-Fi, Bluetooth, screen/power state, and (where enabled) short periodic audio recordings for voice-sample research. All passive streams are researcher-configurable for sampling frequency, on/off duty cycling, and (for GPS) noise injection for privacy.

Active: researcher-defined surveys/EMA (including audio-recording surveys) delivered on a schedule the researcher sets.

**iOS/Android parity is not assumed and was not independently re-verified stream-by-stream in this session** — flagged as an open question below; historically, platforms in this category have had iOS background-execution limits that materially constrain GPS/accelerometer duty cycling relative to Android, and this is a documented general iOS constraint (see CLAUDE.md's explicit instruction not to assume parity), not a Beiwe-specific claim.

## Derived Metrics / Analytics

Via Forest: GPS-derived mobility metrics (e.g., time at home, distance traveled, radius of gyration — exact metric names not independently verified against current Forest documentation this session), and call/text-derived sociability metrics. Forest is positioned by the lab as addressing "the main bottleneck" in digital phenotyping research — that data analysis, not collection, is the harder problem. **Reported** framing from the lab's own materials.

## Active Data Collection

Configurable surveys and EMA prompts, including audio-recording survey items, scheduled by the researcher through the backend portal. Branching logic, randomized/event-triggered scheduling, and other advanced EMA features were **not independently verified against current documentation** this session.

## Researcher and Study Management Features

Web-based study administration portal (part of `beiwe-backend`): study creation, device/participant registration, survey configuration, data-stream configuration (sampling rates, upload behavior). Multi-study support exists in that a single backend deployment can host multiple studies. Adherence/data-flow monitoring, audit logging, and role-based admin accounts were referenced in the repo/wiki but not independently verified in depth this session.

## Data Access and Export

Raw data lands in S3 (self-hosted) or the BSC's AWS storage, and is described as being made available to researchers, including "access to raw data and summary metrics" under the BSC service model. Data is encrypted on-device before upload, in transit (RSA-AES hybrid), and at rest with a study-specific master key; phone numbers and other identifiers are hashed (SHA-256 + PBKDF2) with device-specific salts that are never uploaded. **Verified** from the `beiwe-backend` README's security section. Bulk/API-level export mechanics, exact file formats, and retention defaults were not independently re-verified against current documentation this session.

## APIs, SDKs, and Extensibility

Fully open source (BSD-3) across backend, iOS, and Android — the strongest extensibility position of any platform in this module by definition: a research team can fork and modify any layer. No first-party public REST API for third-party integration was identified in this session (data access appears to be through the study database / exports rather than a documented external API) — **flagged as unresolved** rather than assumed absent.

## Deployment and Infrastructure

- **Self-hosted**: AWS only (S3, EC2, Elastic Beanstalk, RDS/PostgreSQL). Requires "moderate AWS and Python expertise," per the backend README. No documented support for non-AWS clouds.
- **Managed (BSC)**: runs on the Onnela Lab's own AWS deployment; researchers do not manage infrastructure. Pricing is quote-based, computed from three study-specific variables (see Pricing).
- Backend uses rolling releases; mobile apps use semantic versioning.

## Participant Experience

Native app on the participant's own or a study-provisioned phone; background passive collection plus scheduled surveys. Battery impact, permission burden, and BYOD-vs-provisioned suitability were **not independently benchmarked** this session — this is a real gap given how decisive these factors were for wearables in Module 1, and should be treated as an open question pending direct testing or BSC/Onnela Lab documentation review.

## Privacy, Security, and Compliance

- **Verified**: multi-stage encryption (on-device, in-transit RSA-AES hybrid, at-rest with study master key) and identifier hashing, per the backend README.
- HIPAA, GDPR/DPA, SOC 2, and IRB-support specifics were **not independently verified against current documentation** in this session. Do not infer regulatory compliance from "Harvard" as an institutional affiliation — CLAUDE.md's instruction not to infer compliance from general claims applies here as much as to any vendor.
- Self-hosting gives a research team full data custody (the Onnela Lab is never in the data path); using the BSC puts the Onnela Lab's AWS deployment in the data path, which is a materially different governance posture and should be weighed like any other vendor-hosted arrangement.

## Pricing

- **Software**: free, BSD-3-Clause, no licence fee under either deployment path.
- **Self-hosting**: AWS infrastructure costs only (S3/EC2/RDS), which scale with study size and are not separately published — this is a "your AWS bill" cost, not a Beiwe-specific fee.
- **Beiwe Service Center**: quote-based. Per the BSC's own published cost-model description, pricing combines (a) a fixed monthly fee scaled to total study duration (T, months from first enrollment to last participant's data-collection end) and (b) a variable fee tied to total **Active Participant Months** (participants N × per-participant collection length in months). **Verified** as the stated methodology from the BSC's own site; the actual rate figures are not public and require a study-specific quote.

## Research Evidence and Validation

Beiwe has been used across numerous published studies, including deployments at Harvard-affiliated teaching hospitals, per the Onnela Lab's own platform page. This session did **not** conduct the kind of systematic published-use-count or methods-paper survey CLAUDE.md's "Evidence of use" section calls for; that remains an open task (see Open Questions). As an infrastructure platform rather than a measurement device, "validation" here is less about signal accuracy (Module 1's concern) and more about published, reproducible use — which was not exhaustively catalogued this session.

## Strengths

- Fully open source across every layer (backend, iOS, Android, and the Forest analysis package) under a permissive BSD-3 licence — a research team can audit, fork, and modify anything.
- Two genuinely distinct deployment paths — free self-hosted vs. paid managed (BSC) — giving smaller or infrastructure-constrained teams a route that doesn't require in-house AWS/Django expertise.
- Documented, specific, multi-stage encryption and identifier-hashing design, unusual in this module for how concretely it is written into the public README rather than asserted only in marketing copy.
- Native iOS and Android apps under active, visible development (recent commit activity in both mobile repos).
- A dedicated, purpose-built analysis package (Forest) rather than leaving derived-metric computation entirely to the researcher.

## Limitations

- Self-hosting requires real AWS/Django/Python engineering capacity; this is a genuine adoption barrier relative to fully managed commercial platforms (Avicenna Research, MetricWire) in this module.
- No first-party public REST API for third-party integration was located — data access appears to be export/database-mediated rather than API-mediated, which is a meaningfully different integration story than several competitors.
- iOS/Android feature and sampling parity was not independently verified this session and should not be assumed.
- HIPAA/GDPR/SOC 2 compliance posture is undocumented in what this session could access; do not infer compliance from Harvard's institutional affiliation.
- BSC pricing is not public; every study needs a quote.
- Session did not verify branching-logic EMA sophistication, exact derived-metric catalog from Forest, or bulk-export file formats against current documentation.

## Best-Fit Use Cases

- Studies where full data custody, algorithmic transparency, and freedom to modify the collection app are priorities (self-hosted path).
- Teams that want an established, actively maintained open-source stack but prefer not to run their own AWS infrastructure (BSC path).
- Research questions centered on GPS mobility and communication-log sociability metrics, where Forest's existing analysis routines are directly applicable.

## Poor-Fit Use Cases

- Teams needing a no-code, point-and-click study builder with a polished commercial dashboard and immediate third-party integrations (see Avicenna Research, MetricWire, m-Path for that profile shape).
- Studies requiring a documented, stable third-party REST API for real-time integration with external systems — this was not identified as a current Beiwe capability.
- Very small pilots where BSC's quote-based pricing model is disproportionate to study size (self-hosting may be more appropriate, if AWS/Django capacity exists).

## Open Questions

*(Directed to: Onnela Lab / Beiwe Service Center — https://beiwe.hsph.harvard.edu, hsph.harvard.edu/research/onnela-lab)*

- Is there a documented public REST API for third-party data access, distinct from the study database/export mechanism?
- What are the exact iOS-vs-Android differences in passive-stream sampling and background execution?
- What is Forest's current full catalog of derived metrics, and how are they versioned across releases?
- What HIPAA, GDPR/DPA, SOC 2, or comparable compliance documentation exists for BSC-hosted studies specifically (as distinct from self-hosted deployments where the researcher is the data controller)?
- What are actual BSC rate figures (the fixed and variable fee amounts), even as an indicative range?
- What published, systematic count of Beiwe-based peer-reviewed studies exists (this session did not attempt an exhaustive literature count)?

## Key Links

- Official site / Onnela Lab platform page: https://hsph.harvard.edu/research/onnela-lab/digital-phenotyping-and-beiwe-research-platform/
- Beiwe Service Center: https://beiwe.hsph.harvard.edu/
- Backend repository: https://github.com/onnela-lab/beiwe-backend
- iOS app repository: https://github.com/onnela-lab/beiwe-ios
- Android app repository: https://github.com/onnela-lab/beiwe-android
- Forest (analysis package): https://github.com/onnela-lab/forest
- Beiwe/Forest documentation site: https://jponnela.com/bf20/

## Sources

1. Onnela Lab — "Digital Phenotyping and Beiwe Research Platform." https://hsph.harvard.edu/research/onnela-lab/digital-phenotyping-and-beiwe-research-platform/ (accessed 2026-08-24). **Primary.** Data types, iOS/Android support, architecture summary, BSD-3 licence, self-host vs BSC paths.
2. `onnela-lab/beiwe-backend` README. https://github.com/onnela-lab/beiwe-backend (accessed 2026-08-24). **Primary.** Django/AWS architecture, encryption design, identifier hashing, BSD-3 licence, related repos.
3. `onnela-lab/forest` repository. https://github.com/onnela-lab/forest (accessed 2026-08-24). **Primary.** Forest's purpose and relationship to Beiwe.
4. Beiwe Service Center overview. https://www.beiwe.org/beiwe-service-center-overview/ and https://hsph.harvard.edu/research/onnela-lab/beiwe-service-center/ (accessed 2026-08-24). **Primary.** BSC service scope, pricing methodology (fixed + variable fee structure).
5. `onnela-lab` GitHub organization (activity check). https://github.com/onnela-lab (accessed 2026-08-24). Recent commit activity across `beiwe-backend` (Jan 2026) and `beiwe-ios` (Feb 2026) used to support "Active" status.
