# Digital Health Knowledge Base

## Guardrail: Beiwe Repo Issues Require Explicit Permission

**Never create a new GitHub issue, or reply to an existing one, in a Beiwe-related repo until the full text has been shown to Hassan and he replies with the literal phrase "confirmed, post it".** Email keeps its own phrase, "confirmed, send it".

Nothing else is permission for those two actions. Not "go ahead", not "yes", not approval of the task that produced the text. An edit to an issue body or comment already posted counts the same way, so show the new full text and ask again.

Beiwe-related repos are the `onnela-lab` ones: `beiwe-discussions`, `beiwe-backend`, `beiwe-ios`, `beiwe-android`, `forest`, `mano`.

Nothing else needs the phrase. Pull requests, commits and pushes, Notion, Slack, other repos, and ordinary project work all proceed normally, with the usual judgment about anything irreversible or outward-facing.

**Never @-mention anyone unless Hassan has explicitly asked for that person to be tagged.** An @handle is a notification, not a citation.

**Run the `humanizer` skill on reader-facing prose before showing it for approval.**

Full rule at [`../brainiac/conventions/publishing-permission.md`](../brainiac/conventions/publishing-permission.md).

### Scope in this repo

This repo has a public GitHub remote, but pushes here are not gated. Commit and push normally,
including reader-facing prose and the weekly literature-scan routine's logging writes. The phrase is
only for new issues and issue replies in the Beiwe repos, which this project does not touch.

---

## Project Purpose

This project is a structured, evidence-based knowledge base covering
digital health technologies used for research, with an initial focus on:

1.  **Module 1: Wearables**
2.  **Module 2: Mobile Digital Phenotyping Platforms**

The knowledge base should support product research, competitive
analysis, study planning, technical evaluation, and future content
development.

The goal is not to produce a one-time market report. Build a durable,
modular research resource that can be updated over time and reused for
downstream analysis, comparisons, writing, and other projects.

------------------------------------------------------------------------

# Core Operating Rules

## Research is initiated explicitly

Do **not** automatically begin researching a module merely because this
`CLAUDE.md` file is present.

Research each module as a separate phase and only when explicitly
instructed.

Examples:

> Start Module 1. Follow the workflow in CLAUDE.md.

> Start Module 2. Follow the workflow in CLAUDE.md.

If a module has already been researched, do not repeat the entire
research process unless explicitly asked. Update or extend the existing
knowledge base instead.

## Research standard

For all modules:

-   Prioritize primary sources.
-   Use official product pages, developer documentation, API
    documentation, technical documentation, support documentation,
    privacy/security documentation, published validation studies,
    peer-reviewed literature, regulatory materials, and official pricing
    information whenever available.
-   Use high-quality secondary sources when primary documentation is
    incomplete.
-   Distinguish documented facts from inference.
-   Do not treat marketing claims as independently validated evidence.
-   Record conflicting information rather than silently choosing one
    source.
-   Record when information cannot be determined.
-   Capture the date information was verified when the underlying fact
    may change over time.
-   Preserve source URLs so claims can be checked later.
-   Prefer current documentation, but retain historically important
    information when it helps explain platform capabilities or changes.

## Evidence confidence

Important claims should be assigned one of the following statuses when
useful:

-   **Verified:** directly supported by a current authoritative primary
    source.
-   **Corroborated:** supported by multiple credible sources but not
    clearly established in current primary documentation.
-   **Reported:** found in a credible source but not independently
    confirmed.
-   **Unclear:** available evidence is incomplete, conflicting, or
    ambiguous.

Do not manufacture certainty.

## Links and contact information

For every company, device, platform, or service, capture relevant links
whenever available, including:

-   Official homepage
-   Product/platform page
-   Developer portal
-   API documentation
-   Technical documentation
-   Research documentation
-   Data export documentation
-   Privacy/security documentation
-   Pricing page
-   Contact or sales page
-   Other high-value primary sources

Include these even for large, well-known companies.

------------------------------------------------------------------------

# Knowledge Base Structure

Create a modular directory structure rather than placing the research
itself inside `CLAUDE.md`.

Recommended structure:

``` text
digital-health-knowledge-base/
├── CLAUDE.md
├── module-01-wearables/
│   ├── README.md
│   ├── comparison-matrix.md
│   ├── sources.md
│   └── profiles/
│       ├── [company-or-device].md
│       └── ...
├── module-02-digital-phenotyping/
│   ├── README.md
│   ├── comparison-matrix.md
│   ├── sources.md
│   └── profiles/
│       ├── [platform].md
│       └── ...
└── shared/
    ├── terminology.md
    ├── research-log.md
    └── unresolved-questions.md
```

The exact file organization may evolve if a better structure becomes
apparent during research, but preserve the modular approach.

------------------------------------------------------------------------

# Standard Module Workflow

When instructed to start a module:

## Phase 1: Scope and discovery

1.  Review the module instructions in this file.
2.  Identify the major products/platforms that belong in scope.
3.  Search broadly enough to identify important competitors or
    technologies not listed here.
4.  Establish a working inventory before performing detailed profiles.
5.  Record uncertain inclusion decisions rather than excluding
    potentially important technologies without explanation.

## Phase 2: Deep research

Research each included technology systematically using the
module-specific schema.

Do not rely on a single search or source.

Where practical, trace important claims back to primary documentation.

## Phase 3: Build structured profiles

Create one detailed Markdown profile per technology.

Profiles should be optimized for later machine reading as well as human
review. Use consistent headings and terminology.

## Phase 4: Build comparison resources

After individual profiles are sufficiently complete:

-   Create or update the module comparison matrix.
-   Create a module overview/README.
-   Consolidate sources.
-   Record unresolved questions and research gaps.
-   Highlight meaningful differentiators rather than merely listing
    features.

## Phase 5: Quality control

Before considering the initial module research complete:

-   Check major claims against sources.
-   Check links.
-   Identify missing data.
-   Check consistency across profiles.
-   Make sure unknown information is labeled as unknown rather than
    inferred.
-   Note areas where vendor contact would be required to obtain reliable
    information.

## Phase 6: Stop and report

At the end of the research phase, provide a concise summary of:

-   What was created
-   Technologies covered
-   Major gaps
-   Questions requiring direct vendor contact
-   Any important scope decisions
-   Recommended next research steps

Do not automatically begin another module.

------------------------------------------------------------------------

# Module 1: Wearables

## Purpose

Build a detailed knowledge base of wearable devices and ecosystems
relevant to digital health research.

The module should emphasize the practical question:

**What can researchers actually collect, access, export, and use from
each wearable ecosystem, under what conditions, and at what cost?**

The analysis should distinguish consumer-facing functionality from
functionality genuinely available to researchers or developers.

## Scope

Identify and evaluate major wearable ecosystems relevant to research.
This may include, but is not limited to:

-   Apple Watch / Apple Health / HealthKit
-   Oura
-   WHOOP
-   Fitbit / Google
-   Garmin
-   Samsung
-   Polar
-   Withings
-   Empatica
-   ActiGraph
-   Other research-grade or consumer wearable platforms that materially
    belong in the comparison

The list above is a starting point, not a closed list.

## Research questions

For each wearable ecosystem, investigate:

### Product and ecosystem

-   Company
-   Relevant devices
-   Current device generations
-   Intended market
-   Consumer vs research orientation
-   Geographic availability
-   Research programs or institutional offerings

### Sensors

Document available hardware sensors where relevant, such as:

-   PPG
-   ECG
-   Accelerometer
-   Gyroscope
-   Temperature
-   SpO2
-   GPS
-   Barometer/altimeter
-   EDA
-   Other relevant sensors

Distinguish the presence of a sensor from researcher access to its
underlying data.

### Data and metrics

Document available data streams and derived metrics, including where
relevant:

-   Heart rate
-   Inter-beat interval / beat-to-beat data
-   HRV
-   Resting heart rate
-   Respiratory rate
-   Sleep stages
-   Sleep timing
-   Sleep scores
-   Activity
-   Steps
-   Energy expenditure
-   Workouts
-   Temperature
-   SpO2
-   Stress/recovery/readiness metrics
-   Location
-   Other proprietary metrics

For each important stream, determine where possible:

-   Raw vs processed
-   Sampling frequency or temporal resolution
-   On-device vs cloud processing
-   Historical access
-   Real-time or near-real-time access
-   Researcher access
-   Participant export access
-   API access
-   SDK access
-   HealthKit/Health Connect or other ecosystem integration
-   Known limitations

### Research access

Investigate:

-   Public API
-   Research API
-   SDK
-   OAuth
-   Bulk export
-   Participant-level export
-   Enterprise/research portals
-   Study management functionality
-   Research partnerships
-   Eligibility restrictions
-   Approval requirements
-   Rate limits
-   Data latency
-   Retention limits

### Study operations

Where relevant:

-   Remote deployment
-   Account provisioning
-   Participant onboarding
-   Device management
-   Adherence monitoring
-   Battery life
-   Charging burden
-   Wear location
-   Offline collection
-   Sync requirements
-   Data completeness considerations
-   Multi-device study feasibility

### Privacy, security, and governance

Capture documented information on:

-   Data storage
-   Encryption
-   HIPAA-related offerings
-   GDPR
-   SOC 2 or comparable certifications
-   Data processing agreements
-   Research consent considerations
-   Data deletion
-   Participant control
-   Relevant geographic restrictions

Do not infer compliance merely from general company claims.

### Cost

Determine where possible:

-   Device cost
-   Subscription cost
-   Research pricing
-   API/platform fees
-   Enterprise pricing
-   Minimum commitments
-   Whether pricing requires vendor contact
-   Other meaningful study costs

Clearly label unavailable or non-public pricing.

### Evidence and validation

Identify important evidence concerning:

-   Sensor validity
-   Metric validity
-   Sleep staging
-   Heart rate
-   HRV
-   Activity
-   Energy expenditure
-   Other major outputs

The purpose is not to exhaustively review every validation paper.
Capture the strongest and most decision-relevant evidence and link to
important literature.

### Strengths and limitations

Provide an evidence-grounded assessment of:

-   Major strengths
-   Major limitations
-   Research use cases for which the platform is especially well suited
-   Research use cases for which it is poorly suited
-   Important tradeoffs
-   Unique capabilities
-   Lock-in or access concerns

------------------------------------------------------------------------

# Module 2: Mobile Digital Phenotyping Platforms

## Purpose

Build a comprehensive competitive and technical knowledge base of
**mobile-phone-based digital phenotyping and passive sensing
platforms**.

This module should include Beiwe and the major platforms that directly
or meaningfully compete with it.

The central question is:

**What can a research team collect and do with each platform, how
configurable and accessible is the resulting data, what infrastructure
and operational model does it require, and what are the practical
tradeoffs compared with alternatives?**

## Scope

Start with known platforms and expand through systematic discovery.

Potential platforms include:

-   Beiwe
-   RADAR-base
-   mindLAMP
-   AWARE / AWARE Framework
-   Ethica
-   Avicenna
-   MetricWire
-   Other actively used academic, open-source, commercial, or hybrid
    digital phenotyping platforms identified during research

Do not assume every platform listed above remains active or comparable.
Verify current status.

Also identify discontinued or legacy platforms when they remain
important to understanding the field, but clearly label their status.

## Research questions

For each platform, investigate:

### Platform overview

-   Organization/company/lab
-   Platform name
-   Current status
-   Year introduced where known
-   Open source, commercial, academic, or hybrid
-   Primary intended users
-   Typical research domains
-   iOS support
-   Android support
-   Web/admin interfaces
-   Geographic availability
-   Hosting model

### Passive smartphone data collection

Determine which data streams can be collected, including where relevant:

-   GPS/location
-   Accelerometer
-   Gyroscope
-   Magnetometer
-   Barometer
-   Ambient light
-   Proximity
-   Device motion/activity
-   Screen state
-   Device usage
-   App usage
-   Battery
-   Charging
-   Network/connectivity
-   Wi-Fi
-   Bluetooth
-   Calls
-   SMS/text metadata
-   Keyboard-related data
-   Audio
-   Microphone-derived features
-   Notifications
-   Communication metadata
-   Device information
-   Other operating-system-accessible signals

For every important data stream, distinguish:

-   iOS availability
-   Android availability
-   Raw data vs derived features
-   Sampling configurability
-   Background collection constraints
-   Required permissions
-   Special entitlements or OS restrictions
-   Data resolution
-   Upload behavior
-   Known platform limitations

Do not assume parity between iOS and Android.

### Active data collection

Investigate:

-   Surveys
-   EMA
-   Branching logic
-   Scheduled surveys
-   Randomized surveys
-   Event-triggered surveys
-   Notifications
-   Audio diaries
-   Cognitive tasks
-   Custom tasks
-   Multimedia
-   Participant messaging
-   Other active assessments

### Study configuration

Determine:

-   Sensor configuration flexibility
-   Sampling frequency configuration
-   Study-specific configuration
-   Remote configuration changes
-   Participant groups/arms
-   Study cloning/templates
-   Scheduling
-   Enrollment methods
-   QR codes or invitation links
-   Participant identifiers
-   Multi-study support
-   Localization/languages

### Researcher/admin functionality

Investigate:

-   Web dashboard
-   Study creation
-   User roles
-   Administrator accounts
-   Participant management
-   Enrollment monitoring
-   Adherence/data-flow monitoring
-   Device troubleshooting
-   Notifications/alerts
-   Audit logs
-   Data quality monitoring
-   Support tools
-   API access
-   Automation capabilities

### Data architecture and access

Determine:

-   Raw data availability
-   Processed/derived data availability
-   Data schema
-   Export formats
-   Bulk export
-   APIs
-   Direct database access
-   Streaming or near-real-time access
-   Data latency
-   Data retention
-   Cloud storage
-   Researcher-controlled storage
-   Self-hosting
-   On-premises deployment
-   Supported cloud providers
-   Data residency options
-   Offline collection and later synchronization

### Derived features and analytics

Investigate whether the platform provides:

-   Built-in feature extraction
-   Mobility metrics
-   Sleep inference
-   Sociability/communication metrics
-   Activity metrics
-   Circadian/routine metrics
-   Digital biomarkers
-   Visualization
-   Statistical analysis
-   ML pipelines
-   External analysis packages
-   Reproducible open-source analytics

Where relevant, distinguish platform-native analytics from separate
companion tools.

For Beiwe, this includes careful treatment of the relationship between
Beiwe and Forest.

### Extensibility and technical architecture

Investigate:

-   Open-source repositories
-   License
-   SDK availability
-   API availability
-   Plugin architecture
-   Custom sensors
-   Custom assessments
-   Custom app builds
-   White labeling
-   Backend extensibility
-   Integration with wearables
-   Integration with HealthKit
-   Integration with Health Connect
-   Integration with EHR/FHIR systems
-   Integration with external research tools

### Deployment and infrastructure

Determine:

-   SaaS vs self-hosted
-   Cloud requirements
-   AWS/Azure/GCP support
-   Containerization
-   Installation complexity
-   Maintenance burden
-   Required technical expertise
-   Scalability
-   Multi-site deployment
-   Enterprise/institutional deployment
-   Availability of managed hosting

### Privacy, security, and compliance

Capture documented information concerning:

-   Encryption in transit
-   Encryption at rest
-   Identifier separation
-   De-identification/pseudonymization
-   HIPAA
-   GDPR
-   SOC 2
-   ISO certifications
-   IRB/research use
-   Data processing agreements
-   Data residency
-   Access controls
-   Audit logging
-   Participant data deletion
-   Consent support

Do not infer compliance from academic use alone.

### Participant experience

Evaluate where information is available:

-   Installation
-   Enrollment
-   Permission burden
-   Background operation
-   Battery impact
-   Data usage
-   App visibility
-   Participant-facing dashboard
-   Survey experience
-   Troubleshooting burden
-   Longitudinal adherence considerations
-   BYOD vs provisioned-device suitability

### Pricing and service model

Determine:

-   Free/open-source availability
-   Hosting cost
-   License fees
-   Per-study fees
-   Per-participant fees
-   Per-month fees
-   Setup fees
-   Support fees
-   Analysis fees
-   Enterprise pricing
-   Academic pricing
-   Minimum commitments
-   Whether pricing is public
-   Whether a quote or sales contact is required

Separate software cost from infrastructure and service costs whenever
possible.

### Support and services

Investigate:

-   Documentation quality
-   Technical support
-   Study onboarding
-   Training
-   Study configuration
-   IRB support
-   Participant support
-   Custom development
-   Data analysis
-   Managed services
-   Service-level agreements

### Evidence of use

Capture:

-   Peer-reviewed studies
-   Approximate breadth of published use where reasonably measurable
-   Major institutions using the platform
-   Large or notable deployments
-   Clinical/research domains
-   Validation or methods papers
-   Evidence of active maintenance and current adoption

Avoid using publication count as a proxy for quality without context.

### Competitive assessment

For each platform, summarize:

-   Core strengths
-   Core weaknesses
-   Unique capabilities
-   Missing capabilities
-   Technical burden
-   Operational burden
-   Data-access advantages
-   Data-access limitations
-   Best-fit research use cases
-   Poor-fit research use cases

For Beiwe specifically, maintain an objective evidence-based assessment
rather than assuming it is superior.

------------------------------------------------------------------------

# Module 3: Applied Wearables and Digital Phenotyping Studies

## Purpose

Modules 1 and 2 build reference knowledge about **technologies** — what a
wearable ecosystem or phenotyping platform can theoretically do. Module 3
builds reference knowledge about **studies** — what happens when researchers
actually deploy those technologies in the field.

Central question:

**When research teams have actually used these devices and platforms in real
studies, what worked, what didn't, and what does that reveal about
feasibility that vendor documentation and platform capabilities alone can't
show?**

This module is a companion to Modules 1 and 2, not a replacement for their
existing literature libraries. Module 1's `research-library-wearables.md` /
`literature-library.md` and Module 2's `literature-library.md` already
catalog validation and use-case papers per device/platform. Module 3 does
not duplicate that cataloging. It exists at a different altitude: the
**study** is the unit of analysis, not the **device or platform**, and the
questions it asks are about **operational and methodological deployment
reality** (recruitment, retention, adherence, technical failure modes,
multi-device integration), not about sensor accuracy or platform
capability.

## Relationship to Modules 1 and 2

-   A paper that validates a device's sleep-staging accuracy against PSG
    belongs in Module 1's literature library, not here — Module 3 skips pure
    validation studies.
-   A paper that is substantially about a platform's own architecture
    (already the target of Module 2's literature library) does not need a
    separate Module 3 entry unless it also carries substantial
    deployment/operational detail (recruitment numbers, retention rates,
    technical failure notes) not already captured there.
-   A paper qualifies for Module 3 when it is a real research deployment —
    a study that used one or more Module 1 devices and/or Module 2
    platforms as its data-collection instrument to answer a substantive
    research question, and reports enough about *how the deployment went*
    (not just what it found) to be useful for future study design.
-   Cross-reference liberally: a Module 3 profile should link back to the
    relevant Module 1/Module 2 profile(s) for the devices/platforms
    involved, and Module 1/2 profiles' "Research Evidence" sections may
    link forward to relevant Module 3 entries — do not duplicate content,
    link it.

## Scope

Studies are in scope regardless of the specific device/platform, as long as
the device/platform is one already profiled in Module 1 or Module 2 — this
module does not introduce new technologies, only new depth on how existing
profiled technologies perform in practice. Priority areas:

-   Longitudinal / multi-week-or-longer deployments (adherence and
    retention data only becomes meaningful over time)
-   Multi-device or multi-modal studies (a wearable + a phenotyping
    platform together; multiple wearables compared in the same cohort)
-   Large-cohort or multi-site studies (recruitment/retention patterns at
    scale)
-   Studies explicitly reporting feasibility, adherence, retention, or
    technical-failure data as an outcome (not just a footnote)
-   Both academic and clinical/community-health deployments, for any
    Module 1/2 device or platform

Out of scope (deliberately excluded, not merely deprioritized):

-   Pure device-accuracy/validation studies (already Module 1's territory)
-   Platform-architecture/methods papers with no deployment cohort
    (already Module 2's territory)
-   Feasibility studies for devices/platforms not yet profiled in Module 1
    or 2 — flag as a candidate for Module 1/2 expansion instead, don't
    silently absorb into Module 3

## Research questions per study

For each qualifying study, investigate:

### Study identification

-   Title, authors, year, journal/venue, DOI/URL
-   Study design (RCT, prospective cohort, observational, pilot/feasibility)
-   Funding source and any vendor sponsorship/COI

### Population and duration

-   Sample size (enrolled vs. analyzed — note attrition explicitly)
-   Population/setting (general population, clinical, athletic, older
    adult, etc.)
-   Study duration and follow-up structure

### Instrumentation

-   Which Module 1 device(s) and/or Module 2 platform(s) were used, and how
    (concurrently, sequentially, as primary vs. secondary instrument)
-   Deployment model: participant-owned (BYOD) vs. researcher-provisioned
-   Any custom integration, middleware, or data-aggregation layer used to
    combine devices/platforms

### Recruitment and retention

-   Recruitment method and setting
-   Retention/completion rate, with the specific definition used (e.g.,
    "wore device ≥X hours/day for ≥Y% of study days")
-   Attrition reasons where reported (device discomfort, technical
    failure, participant burden, dropout for unrelated reasons)

### Data completeness and technical issues

-   Reported data completeness/missingness
-   Any explicitly documented technical failure modes: device failures,
    sync/upload issues, battery burden, app crashes, connectivity gaps
-   Whether/how missing data was handled (imputation, exclusion,
    sensitivity analysis)

### Feasibility findings

-   The study's own stated conclusions about feasibility of this
    device/platform/combination for this population and use case
-   Any explicit recommendations for future study design

### Relevance and confidence

-   One-paragraph synthesis: what does this study teach about deploying
    this device/platform combination in practice, that a future study team
    should know before choosing it
-   Evidence confidence marker per this project's standard scale
    (Verified/Corroborated/Reported/Unclear), applied to the *feasibility
    claims* specifically — not to any accuracy claims already covered
    elsewhere

## Profile template (Module 3-specific)

Do not reuse the Module 1/2 technology profile template unchanged — the
unit of analysis is a study, not a technology. Use:

``` markdown
# [Short Study Identifier — e.g., "Smith et al. 2025 — Multi-site Oura + Beiwe deployment, N=412"]

## Quick Facts

| Field | Details |
|---|---|
| Citation | |
| Study design | |
| Sample size (enrolled / analyzed) | |
| Population | |
| Duration | |
| Devices/platforms used | (link to Module 1/2 profiles) |
| Funding/COI | |
| Last verified | |

## Summary

## Instrumentation and Deployment Model

## Recruitment and Retention

## Data Completeness and Technical Issues

## Feasibility Findings

## Relevance to Future Study Design

## Evidence Confidence

## Key Links

## Sources
```

## Comparison resource

Maintain `feasibility-matrix.md` (Module 3's equivalent of a comparison
matrix): one row per study, columns for device/platform combination, sample
size, duration, retention rate, major technical issues, and a one-line
feasibility takeaway. This is the resource future study designers will
actually want — who else tried this combination, at what scale, and did it
hold up.

## Directory structure

``` text
module-03-applied-studies/
├── README.md
├── feasibility-matrix.md
├── sources.md
└── profiles/
    ├── [short-study-slug].md
    └── ...
```

## Workflow

Follow this project's Standard Module Workflow (Phases 1–6, defined above)
exactly, with two Module 3-specific notes:

-   **Phase 1 (scope/discovery)** should build the working inventory by
    searching from the *device/platform side* (search each Module 1/2
    technology plus deployment/feasibility/adherence/retention terms)
    rather than starting from a fixed list of studies — the study universe
    is not enumerable up front the way the platform universe was for
    Modules 1–2.
-   **Phase 4 (comparison resources)** produces `feasibility-matrix.md`
    instead of the Module 1/2-style comparison matrix, per the resource
    described above.

## Future automation note

**Status: wired in, 2026-09-02.** The baseline now exists (55 profiles), and the
repo-side work is done — `module-03-applied-studies/literature-index.json`
(dedup ledger, seeded with all 55) and `_scan-queue.md` (candidate queue).
The routine's **full prompt** (Parts A–D) is version-controlled at
**`shared/weekly-literature-scan.md`** — read that before changing anything
about the scan, and mirror any edit made in the claude.ai Routines UI back into
it. Module 3 is **Part C**; logging, commit and push are Part D and cover all
three modules in a single commit.

**One deliberate difference from Modules 1 and 2: the routine triages Module 3,
it does not write it.** It appends candidates to `_scan-queue.md` and must never
create or edit a file under `module-03-applied-studies/profiles/`. Modules 1
and 2 catalogue papers *about* a technology, which is safely automatable from
abstracts; Module 3 asserts *what happened in a deployment*, which is not.
Every figure in its profiles came from full text, and abstract-level screening
in this project has a measured platform-misattribution rate of roughly 3 in 12.

------------------------------------------------------------------------

# Standard Technology Profile Template

Use a consistent profile structure, adapting sections when they
genuinely do not apply.

``` markdown
# [Technology / Platform Name]

## Quick Facts

| Field | Details |
|---|---|
| Organization | |
| Category | |
| Current status | |
| Platforms/devices | |
| Open source | |
| Hosting/deployment | |
| Pricing model | |
| Last verified | |

## Summary

## Products / Platform Architecture

## Sensors and Data Streams

## Derived Metrics / Analytics

## Active Data Collection

## Researcher and Study Management Features

## Data Access and Export

## APIs, SDKs, and Extensibility

## Deployment and Infrastructure

## Participant Experience

## Privacy, Security, and Compliance

## Pricing

## Research Evidence and Validation

## Strengths

## Limitations

## Best-Fit Use Cases

## Poor-Fit Use Cases

## Open Questions

## Key Links

- Official site:
- Product/platform page:
- Documentation:
- Developer/API documentation:
- GitHub:
- Pricing:
- Security/privacy:
- Contact/sales:

## Sources

1. ...
2. ...
```

Remove irrelevant headings rather than filling them with meaningless
boilerplate.

------------------------------------------------------------------------

# Comparison Matrices

Each module should maintain a comparison matrix designed for rapid
cross-platform analysis.

Do not attempt to force every detail into one enormous table. Use
multiple tables if necessary.

## Wearables comparison areas

At minimum compare:

-   Device/ecosystem
-   Sensors
-   Major accessible data streams
-   Raw data availability
-   API availability
-   Research access
-   Sampling/resolution
-   Export
-   Study management
-   Research validation
-   Privacy/security
-   Cost
-   Key strengths
-   Key limitations

## Digital phenotyping comparison areas

At minimum compare:

-   Platform
-   iOS
-   Android
-   Open source
-   Hosting model
-   Passive sensors
-   Survey/EMA capabilities
-   Sampling configurability
-   Raw data access
-   Derived metrics
-   API
-   Self-hosting
-   Study management
-   Participant monitoring
-   Wearable/HealthKit integration
-   Privacy/security
-   Pricing/service model
-   Technical burden
-   Operational support
-   Key strengths
-   Key limitations

------------------------------------------------------------------------

# Source Management

Maintain a module-level `sources.md` in addition to citations within
profiles.

For sources, capture when possible:

-   Title
-   Organization/authors
-   URL or DOI
-   Source type
-   Publication/update date
-   Date accessed
-   Relevant technology
-   Notes on what the source establishes

Avoid duplicate source entries when the same source supports multiple
claims.

------------------------------------------------------------------------

# Research Log

Maintain `shared/research-log.md`.

For each substantial research session, record:

-   Date
-   Module
-   Technologies researched
-   Files created or updated
-   Major findings
-   Important unresolved questions
-   Sources or documentation that were unavailable
-   Decisions that could affect later comparisons

This should make future updates auditable and prevent unnecessary
re-research.

------------------------------------------------------------------------

# Unresolved Questions

Maintain `shared/unresolved-questions.md`.

Use it for questions that cannot be reliably answered from available
sources, especially:

-   Non-public pricing
-   Enterprise terms
-   Research API access requirements
-   Undocumented sampling limitations
-   Hosting arrangements
-   Security/compliance details
-   Platform status
-   Features requiring vendor confirmation

When possible, include the specific vendor or organization that could
answer the question and an official contact link.

------------------------------------------------------------------------

# Future Modules

The knowledge base is intended to expand beyond the first two modules.

Potential future modules may include areas such as:

-   Digital biomarkers and analytics tools
-   Health data aggregation platforms
-   Remote patient monitoring technologies
-   Connected medical devices
-   Digital therapeutics
-   Research data infrastructure
-   Health data interoperability

Do not begin or design these modules in detail unless explicitly
requested.

------------------------------------------------------------------------

# Maintenance

Treat this knowledge base as living research.

When asked to update it:

1.  Identify claims likely to have changed.
2.  Re-check primary documentation.
3.  Preserve useful historical context.
4.  Update verification dates.
5.  Record material changes in the research log.
6.  Update comparison matrices when changes affect cross-platform
    conclusions.

Do not overwrite uncertainty or historical facts merely because a vendor
page changed.

------------------------------------------------------------------------

# Downstream Use

This knowledge base may later be used to create:

-   Competitive analyses
-   Product strategy documents
-   Research study recommendations
-   Platform-selection guidance
-   Technical comparisons
-   Website content
-   Articles
-   Case studies
-   Internal documentation
-   Marketing content
-   Interview preparation
-   Other digital health research products

When producing downstream content, use the structured knowledge base as
the factual foundation and return to primary sources when a claim is
consequential or potentially outdated.

The knowledge base itself should remain evidence-focused and relatively
neutral so it can support many different downstream uses.

------------------------------------------------------------------------

# Cross-Project Context

This project is part of a shared-context system across several related
projects — see [`../shared_context/MAP.md`](../shared_context/MAP.md).

-   **Role: direct reference source, not a writeup producer.** Unlike
    `health_data_analytics`, `bsc_assistant`, and `beiwe_platform_metrics`,
    this project does not run a `writeup` skill or push curated briefs into
    `../brainiac/writeups/`. The knowledge base itself is already the
    reference artifact — other projects (starting with
    `health_data_analytics`, when analyzing wearable data or writing up
    findings) consult it directly by path, e.g.
    `../digital_health_knowledgebase/module-01-wearables/`, rather than
    through a vault-mediated brief.
-   **Activity tracking:** `/logoff` keeps
    [`../brainiac/activity/digital_health_knowledgebase.md`](../brainiac/activity/digital_health_knowledgebase.md)
    current with which modules are under active research, so other
    projects can see what's here without opening the whole knowledge base.
-   **Session close:** `/logoff` follows the shared four-phase contract at
    [`../shared_context/session_close.md`](../shared_context/session_close.md)
    — same command everywhere, this project's specifics in
    `.claude/commands/logoff.md`. This repo has a GitHub remote
    (`digital_health_knowledgebase`, public), so `/logoff` commits and
    pushes.
