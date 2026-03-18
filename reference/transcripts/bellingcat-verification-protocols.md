# Bellingcat Verification Protocols

## Introduction

Bellingcat, the open-source investigative collective founded by Eliot Higgins in 2014, pioneered a rigorous methodology for verifying digital evidence using only publicly available tools and data. Their work on the downing of MH17, the Skripal poisoning, and conflict zone documentation established a replicable standard for OSINT verification that intelligence agencies now study.

This transcript documents the core verification protocols that inform the DeepResearch Squad's approach to open-source evidence, particularly through the OSINT Investigator (`agents/osint-investigator.md`) and the OSINT framework suite at `frameworks/osint-investigator/`. These protocols are not theoretical -- they are battle-tested procedures for establishing whether digital evidence is authentic, unaltered, and correctly attributed.

## Core Verification Protocols

### 1. Geolocation Verification

**Description:** Confirming the precise location where a photograph, video, or event occurred by matching visible features -- landmarks, terrain, signage, shadows, infrastructure, vegetation -- against satellite imagery, street-level views, and known reference points. Geolocation answers: "Was this really taken where the source claims?"

**Workflow:**
1. Identify all visible reference points in the source material (buildings, road patterns, mountain ridgelines, utility infrastructure, commercial signage).
2. Cross-reference against satellite imagery services (Google Earth, Sentinel Hub, Mapillary) to find candidate locations.
3. Match at least three independent reference points to confirm location. Two-point matches are insufficient due to coincidental similarity.
4. Document the match with annotated comparison images showing each reference point alignment.
5. Check for temporal consistency: do the visible features (construction state, vegetation season, infrastructure changes) align with the claimed date?

### 2. Chronolocation (Temporal Verification)

**Description:** Determining when a photo or video was actually captured, independent of metadata timestamps which can be edited. Chronolocation uses sun position, shadow angles, lighting conditions, and environmental context to establish or verify the time and date.

**Workflow:**
1. Analyze shadow direction and length in the source material.
2. Use sun position calculators (SunCalc, ShadowCalculator) with the geolocated coordinates to determine what time of day and year would produce the observed shadow pattern.
3. Cross-check against weather records for the location and claimed date -- cloud cover, precipitation, and lighting conditions should match.
4. Look for time-stamped contextual clues: newspaper headlines visible in frame, TV broadcasts on screens, event-specific decorations, seasonal vegetation state.
5. Compare against the source's claimed timeline. Flag discrepancies as verification failures.

### 3. Reverse Image Search Chains

**Description:** Tracing an image back to its earliest known appearance online to identify the original source, detect manipulation, and uncover reuse or misattribution. A single reverse image search is insufficient -- the protocol requires chaining searches across multiple engines and following each trail.

**Workflow:**
1. Run the image through multiple reverse search engines (Google Images, TinEye, Yandex Images, Bing Visual Search) -- each indexes different portions of the web.
2. Sort results by date to find the earliest known posting. The earliest posting is a candidate for the original source but is not conclusive proof of origin.
3. Check whether cropped or altered versions exist. Search cropped sub-regions of the image independently to detect composite images.
4. Follow the provenance chain: who posted first, what was their stated source, and can that chain be traced to a primary witness or photographer?
5. Flag images that appear in unrelated contexts (stock photo databases, older news stories) as likely misattributed.

### 4. Metadata Analysis

**Description:** Extracting and evaluating embedded metadata (EXIF data, document properties, file system timestamps) from digital files. While metadata can be stripped or forged, its presence or absence is itself evidence. Inconsistencies between metadata and claimed provenance are strong indicators of manipulation.

**Workflow:**
1. Extract all available metadata using tools like ExifTool, Jeffrey's EXIF Viewer, or Metadata2Go.
2. Check camera model, GPS coordinates, timestamps, and software editing history against the source's claims.
3. Evaluate metadata absence: social media platforms strip EXIF data on upload, so an image with full EXIF data was likely not sourced from social media, despite claims to the contrary.
4. Look for editing signatures: Adobe Photoshop markers, multiple save iterations, or resolution inconsistencies that indicate post-processing.
5. Cross-reference metadata GPS coordinates with the geolocation analysis. Discrepancies between embedded GPS and visual geolocation require explanation.

### 5. Social Media Provenance

**Description:** Establishing the authenticity and original source of social media content by analyzing account history, posting patterns, network connections, and platform-specific artifacts. This protocol guards against sock puppet accounts, coordinated inauthentic behavior, and content laundering.

**Workflow:**
1. Examine the posting account's history: creation date, posting frequency, follower-to-following ratio, and content consistency. Accounts created shortly before posting breaking content warrant additional scrutiny.
2. Check whether the account has a verifiable real-world identity or is connected to known individuals through mutual interactions.
3. Analyze the content's spread pattern: organic sharing follows power-law distributions; coordinated amplification shows suspicious simultaneity.
4. Use platform archival tools (Wayback Machine, Archive.today, CachedView) to capture content before potential deletion or editing.
5. Cross-reference the social media post against other accounts reporting the same event to establish whether the poster was a primary witness or a secondary relay.

### 6. Multi-Source Triangulation

**Description:** No single verification protocol is sufficient on its own. Bellingcat's core principle is that verification requires convergence across independent methods and independent sources. A finding is verified only when geolocation, chronolocation, provenance, and metadata all point to the same conclusion.

**Workflow:**
1. Apply at least three independent verification protocols to every piece of critical evidence.
2. Map each protocol's conclusion: does geolocation agree with metadata GPS? Does chronolocation agree with the claimed date? Does provenance trace to a credible primary source?
3. Assess convergence: full agreement across protocols yields high confidence. Partial agreement with explainable discrepancies yields moderate confidence. Contradictions between protocols yield low confidence and trigger further investigation.
4. Document the triangulation matrix showing which protocols confirmed, partially confirmed, or contradicted the claim.

## Application to Deep Research Squad

These verification protocols map directly onto the squad's verification and collection layers:

- **OSINT Investigator** (`agents/osint-investigator.md`): Executes protocols 1-5 during the collection phase. The agent's scope explicitly includes geolocation from public data, metadata analysis, and social media intelligence (SOCMINT). The OSINT framework suite at `frameworks/osint-investigator/` provides operational detail, particularly `osint-digital-footprint-mapping.md` for social media provenance and `osint-open-source-intelligence.md` for the full intelligence cycle.

- **Evidence Verifier** (`agents/evidence-verifier.md`): Applies protocol 6 (multi-source triangulation) as the quality gate. The verifier's mandate to block unsubstantiated claims directly mirrors Bellingcat's requirement for convergence across independent verification methods before publishing.

- **Source Hunter** (`agents/source-hunter.md`): Identifies and ranks sources using provenance analysis principles from protocol 3 (reverse image search chains) and protocol 5 (social media provenance), ensuring source diversity meets the squad's minimum of three independent source types.

- **Research Auditor** (`agents/research-auditor.md`): Reviews final deliverables for verification completeness, confirming that critical claims underwent multi-source triangulation and that the verification audit trail is documented.

## Ethical Boundaries

Bellingcat's methodology operates within strict ethical limits that the DeepResearch Squad adopts in full, as codified in `frameworks/osint-investigator/osint-open-source-intelligence.md`:

1. **Public sources only.** All information must be legally and freely accessible. No hacking, no unauthorized access, no circumvention of access controls.
2. **No deception.** Investigators do not create fake accounts, impersonate individuals, or use social engineering to extract information. Collection relies on what is already public.
3. **Minimization of harm.** When investigations involve individuals, publish only what is necessary and relevant. Do not expose private information beyond what the investigation requires.
4. **Reproducibility.** Every verification step must be documented well enough that an independent analyst could reproduce it. This serves both quality assurance and legal defensibility.
5. **Acknowledging uncertainty.** When verification protocols yield ambiguous results, state the ambiguity explicitly. Never present partially verified findings as fully confirmed. Confidence levels must reflect the actual state of the evidence, consistent with the squad's four-level confidence scale (High, Medium, Low, Contested).
