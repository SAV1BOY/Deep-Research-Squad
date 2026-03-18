# Cross-Squad Handoff Contracts

## Purpose

This document formalizes the handoff contracts between Deep Research Squad and each integrated squad in the 12-squad ecosystem. Each contract specifies exactly what is sent, what is received, quality gates in both directions, SLAs, escalation paths, shared assets, and return protocols. These contracts operationalize the policies defined in `docs/cross-squad-handoff-policy.md` and use the delivery template at `templates/operational/cross-squad-delivery-template.md`.

## Governing Standards

- All outbound deliverables must pass the `checklists/cross-squad-research-delivery-checklist.md` (minimum score 80%).
- All deliverables must include the mandatory metadata header defined in `docs/cross-squad-handoff-policy.md`.
- All handoffs are logged in `data/registries/cross-squad-handoff-registry.yaml`.
- Confidence scoring follows the project-wide 0.0-1.0 scale (`config.yaml` defaults).
- Citation style: APA-7.
- Follow-up availability window: 5 business days post-handoff.

---

## 1. Data Squad

### What Deep Research Sends (Outbound)

| Deliverable | Format | Description |
|---|---|---|
| Raw datasets requiring statistical analysis | CSV/JSON with data dictionary | Unprocessed or lightly processed data collected during research, with source provenance and variable definitions |
| Data-cleaning and normalization requests | Markdown brief + raw files | Specification of cleaning rules, expected output schema, and quality requirements |
| Quantitative modeling tasks | Structured brief (markdown) | Model specification including variables, hypotheses, expected outputs, and constraints |

### What Deep Research Receives (Inbound)

| Deliverable | Expected Format | Description |
|---|---|---|
| Cleaned datasets with methodology notes | CSV/JSON + methodology markdown | Processed data with transformation log, missing-data treatment, and normalization notes |
| Statistical models and significance tests | Report (markdown/PDF) + code artifacts | Model outputs with p-values, confidence intervals, effect sizes, and reproducibility instructions |
| Data visualizations and dashboards | PNG/SVG + interactive links | Publication-ready charts with axis labels, legends, source annotations, and alt text |

### Exit Gate (Before Sending)

- [ ] Cross-squad delivery checklist score >= 80% (`checklists/cross-squad-research-delivery-checklist.md`)
- [ ] Data dictionary included for all tabular deliverables
- [ ] Source provenance documented for every dataset (source, collection date, methodology)
- [ ] Sensitive fields identified and flagged
- [ ] File formats confirmed as compatible with Data Squad tooling

### Entry Gate (When Receiving)

- [ ] Methodology notes accompany all cleaned datasets
- [ ] Statistical significance thresholds are stated and justified
- [ ] Transformations are logged and reversible where possible
- [ ] Visualizations include source data references
- [ ] No unexplained null values or anomalies in returned data

### SLA

| Direction | Turnaround |
|---|---|
| Outbound (Deep Research -> Data Squad) | 2 business days for dataset handoff; 3 business days for modeling briefs |
| Inbound (Data Squad -> Deep Research) | 3 business days for cleaned data; 5 business days for statistical models |

### Escalation

- **Rejection**: If Data Squad rejects a handoff, they must provide specific deficiency notes within 1 business day. Deep Research has 2 business days to remediate and redeliver.
- **Delay**: If SLA is exceeded by more than 2 business days, escalate to Deep Research Chief and Data Squad lead.
- **Quality dispute**: If quality rating falls below 3/5 on two consecutive deliveries, trigger a joint process review.

### Shared Assets

- `data/benchmarks`
- `data/metrics`
- `data/registries`

### Return Protocol

Inadequate deliverables are returned with a structured rejection note containing: (1) specific items that failed, (2) required corrections, (3) revised deadline. Returns are logged in the handoff registry with status `rejected`.

---

## 2. Advisory Board

### What Deep Research Sends (Outbound)

| Deliverable | Format | Description |
|---|---|---|
| Decision briefs requiring board-level review | Decision brief (markdown), using `templates/briefs` | Executive-level synthesis with recommendations, risk map, and confidence bands |
| Strategic research findings for governance input | Structured report (markdown/PDF) | Research findings framed for strategic governance decisions |
| Risk assessments needing executive sign-off | Risk assessment brief (markdown) | Quantified risk matrix with likelihood, impact, mitigation options, and confidence levels |

### What Deep Research Receives (Inbound)

| Deliverable | Expected Format | Description |
|---|---|---|
| Strategic priorities and research questions | Structured brief or directive (markdown) | Prioritized list of research questions with context, urgency, and expected use |
| Board-mandated due diligence requests | Formal request (markdown) | Due diligence scope, target entities, specific concerns, and timeline |
| Governance feedback on research methodology | Review memo (markdown) | Feedback on methodology choices, scope adequacy, and quality standards |

### Exit Gate (Before Sending)

- [ ] Cross-squad delivery checklist score >= 92% (elevated threshold for board-level materials)
- [ ] Decision brief contains recommendations, risk assessment, and confidence bands (`quality_gates.mandatory.decision-readiness`)
- [ ] Executive summary under 500 words (`defaults.executive_summary_max_words`)
- [ ] All research jargon eliminated or defined
- [ ] Contrarian review completed (`quality_gates.mandatory.contrarian-review`)

### Entry Gate (When Receiving)

- [ ] Research question is specific and scoped (not open-ended)
- [ ] Priority level and urgency are stated
- [ ] Expected use of research output is described
- [ ] Timeline is realistic given the scope
- [ ] Relevant prior research or context is referenced

### SLA

| Direction | Turnaround |
|---|---|
| Outbound (Deep Research -> Advisory Board) | 5 business days for decision briefs; 3 business days for risk assessments |
| Inbound (Advisory Board -> Deep Research) | Variable; research commissions include their own stated deadlines |

### Escalation

- **Rejection**: Advisory Board rejection triggers immediate review by Deep Research Chief. Remediation within 2 business days with a revised brief.
- **Delay**: Any delay on board-level deliverables escalates to Deep Research Chief on day 1 of SLA breach.
- **Quality dispute**: Board-level quality disputes are escalated to the Chief Research Architect for resolution within 1 business day.

### Shared Assets

- `templates/briefs`
- `data/decisions`

### Return Protocol

Board returns include a formal feedback memo specifying deficiencies. Deep Research Chief personally owns the remediation. Returns are treated as high-priority and resolved within 1 business day.

---

## 3. C-Level Squad

### What Deep Research Sends (Outbound)

| Deliverable | Format | Description |
|---|---|---|
| Executive intelligence briefs | Executive brief (markdown), using `templates/briefs` | Concise, decision-ready intelligence with clear "so what" framing |
| Competitive landscape summaries | Analysis report (markdown), using `templates/analysis` | Competitor positioning, strengths/weaknesses, strategic implications |
| Market opportunity assessments | Structured report (markdown/PDF) | Market sizing, segmentation, growth vectors, and entry/expansion recommendations |

### What Deep Research Receives (Inbound)

| Deliverable | Expected Format | Description |
|---|---|---|
| Strategic research commissions | Structured request (markdown) | Research scope, strategic context, decision timeline, and expected output format |
| Urgent competitive intelligence requests | Priority request (markdown/email) | Specific competitor or market event requiring rapid-turnaround intelligence |
| M&A due diligence mandates | Formal mandate (markdown) | Target entity, diligence scope, risk areas of concern, and hard deadline |

### Exit Gate (Before Sending)

- [ ] Cross-squad delivery checklist score >= 92% (elevated threshold for C-level materials)
- [ ] Executive summary present and under 500 words
- [ ] Recommendations are actionable with clear next steps
- [ ] Confidence levels explained in plain language (no jargon)
- [ ] Bias audit passed (`quality_gates.mandatory.bias-audit`)

### Entry Gate (When Receiving)

- [ ] Strategic context is provided (why this research matters now)
- [ ] Decision timeline is stated
- [ ] Scope boundaries are defined (what is in/out)
- [ ] Expected output format is specified
- [ ] Relevant internal data or prior research is shared

### SLA

| Direction | Turnaround |
|---|---|
| Outbound (Deep Research -> C-Level Squad) | 5 business days standard; 2 business days for urgent requests |
| Inbound (C-Level Squad -> Deep Research) | Commissions include stated deadlines; urgent requests flagged with priority |

### Escalation

- **Rejection**: C-Level rejection triggers Deep Research Chief review within 4 hours. Remediation deadline: 1 business day.
- **Delay**: SLA breach on C-Level deliverables escalates immediately to Deep Research Chief.
- **Quality dispute**: Resolved at Chief-to-Chief level within 1 business day.

### Shared Assets

- `templates/briefs`
- `templates/outputs`
- `data/decisions`

### Return Protocol

C-Level returns are highest priority. The Deep Research Chief owns triage and assigns remediation within 4 hours of return. Root cause analysis is mandatory for every C-Level return.

---

## 4. Copy Squad

### What Deep Research Sends (Outbound)

| Deliverable | Format | Description |
|---|---|---|
| Research-backed talking points | Bulleted brief (markdown) | Evidence-sourced claims with source citations, confidence levels, and suggested framing |
| Evidence-sourced claims for copy | Claim-source-confidence triads (markdown table) | Individual claims formatted for direct insertion into copy, each with sourced backing |
| Statistical proof points and data narratives | Data narrative brief (markdown) | Key statistics with context, trends, and recommended narrative framing |

### What Deep Research Receives (Inbound)

| Deliverable | Expected Format | Description |
|---|---|---|
| Fact-check requests on draft copy | Draft copy + specific claims flagged (markdown) | Copy with highlighted claims requiring verification |
| Source verification for published claims | Claim list (markdown table) | Published claims with current sources requiring freshness or accuracy verification |
| Competitor messaging analysis requests | Analysis brief (markdown) | Competitor copy samples with specific analysis questions |

### Exit Gate (Before Sending)

- [ ] Cross-squad delivery checklist score >= 80%
- [ ] Every claim includes at least one verifiable source citation
- [ ] Confidence level attached to each talking point
- [ ] Language is accessible to non-research audiences
- [ ] Domain jargon translated to Copy Squad vocabulary

### Entry Gate (When Receiving)

- [ ] Specific claims to verify are identified (not open-ended "check everything")
- [ ] Draft copy or claim list is provided in editable format
- [ ] Deadline and priority are stated
- [ ] Context for intended use is provided (channel, audience)

### SLA

| Direction | Turnaround |
|---|---|
| Outbound (Deep Research -> Copy Squad) | 2 business days for talking points; 1 business day for proof points |
| Inbound (Copy Squad -> Deep Research) | 2 business days for fact-check requests; 3 business days for competitor messaging analysis |

### Escalation

- **Rejection**: Copy Squad provides specific claim-level feedback. Deep Research remediates within 1 business day.
- **Delay**: SLA breach by more than 1 business day escalates to respective squad leads.
- **Quality dispute**: Joint review session to align on evidence standards for copy use cases.

### Shared Assets

- `reference/reports`
- `data/case-studies`

### Return Protocol

Returns must specify which claims failed verification or lacked adequate sourcing. Deep Research addresses individual claim deficiencies and redelivers the corrected items (not the full package).

---

## 5. Brand Squad

### What Deep Research Sends (Outbound)

| Deliverable | Format | Description |
|---|---|---|
| Market perception research | Analysis report (markdown), using `templates/analysis` | Qualitative and quantitative perception data with sentiment analysis |
| Brand positioning competitive analysis | Competitive matrix (markdown table + narrative) | Positioning maps, differentiation analysis, and white-space identification |
| Audience segmentation data | Structured dataset (CSV/JSON) + narrative brief | Segment profiles with demographics, psychographics, and behavioral data |

### What Deep Research Receives (Inbound)

| Deliverable | Expected Format | Description |
|---|---|---|
| Brand audit research requests | Structured request (markdown) | Brand audit scope, target competitors, evaluation dimensions |
| Category landscape mapping needs | Brief (markdown) | Category definition, boundaries, and specific mapping questions |
| Cultural trend research briefs | Research brief (markdown) | Cultural phenomena to investigate, relevance hypothesis, and geographic scope |

### Exit Gate (Before Sending)

- [ ] Cross-squad delivery checklist score >= 80%
- [ ] Perception data includes methodology and sample characteristics
- [ ] Competitive analysis includes at least 5 competitors with consistent evaluation criteria
- [ ] Audience segments are defined with actionable precision
- [ ] Source diversity requirement met (minimum 3 independent source types)

### Entry Gate (When Receiving)

- [ ] Research scope is bounded (specific markets, categories, or audiences)
- [ ] Evaluation criteria or dimensions are specified
- [ ] Existing brand assets or prior research are referenced
- [ ] Timeline aligns with brand planning cycles

### SLA

| Direction | Turnaround |
|---|---|
| Outbound (Deep Research -> Brand Squad) | 5 business days for perception research; 3 business days for competitive analysis |
| Inbound (Brand Squad -> Deep Research) | Requests include stated deadlines aligned with brand planning cycles |

### Escalation

- **Rejection**: Brand Squad specifies which dimensions or segments are inadequate. Deep Research remediates within 3 business days.
- **Delay**: SLA breach by more than 2 business days escalates to squad leads.
- **Quality dispute**: Joint calibration session to align research depth with brand strategy needs.

### Shared Assets

- `reference/reports`
- `data/research`

### Return Protocol

Returns specify inadequate dimensions or missing segments. Deep Research supplements (not replaces) the original deliverable with corrected or additional materials.

---

## 6. Design Squad

### What Deep Research Sends (Outbound)

| Deliverable | Format | Description |
|---|---|---|
| UX research findings and usability data | Research report (markdown) + data files | Usability test results, heuristic evaluations, user journey findings |
| Design trend analysis reports | Trend report (markdown), using `templates/analysis` | Design trend identification with evidence, adoption curves, and relevance assessment |
| Accessibility research and compliance data | Compliance brief (markdown) + checklist | Regulatory requirements, WCAG compliance status, and remediation recommendations |

### What Deep Research Receives (Inbound)

| Deliverable | Expected Format | Description |
|---|---|---|
| User research study requests | Research brief (markdown) | Study objectives, target users, research questions, and methodology preferences |
| Design benchmark and best-practice research | Request brief (markdown) | Specific design patterns or components to benchmark with evaluation criteria |
| A/B test result analysis needs | Test data (CSV/JSON) + context brief | Raw test data with hypothesis, variants, and success metrics |

### Exit Gate (Before Sending)

- [ ] Cross-squad delivery checklist score >= 80%
- [ ] UX findings include participant demographics and methodology transparency
- [ ] Trend analysis includes adoption evidence (not speculation)
- [ ] Accessibility data references specific standards (WCAG 2.1, ADA, etc.)
- [ ] Visual examples or screenshots are included where applicable

### Entry Gate (When Receiving)

- [ ] Research questions are specific and testable
- [ ] Target user profiles or segments are defined
- [ ] A/B test data includes sample sizes and test duration
- [ ] Success metrics are pre-defined

### SLA

| Direction | Turnaround |
|---|---|
| Outbound (Deep Research -> Design Squad) | 5 business days for UX research; 3 business days for trend reports |
| Inbound (Design Squad -> Deep Research) | 2 business days for A/B test analysis; 5 business days for study requests |

### Escalation

- **Rejection**: Design Squad provides specific usability or methodology concerns. Deep Research remediates within 2 business days.
- **Delay**: SLA breach by more than 2 business days escalates to squad leads.
- **Quality dispute**: Joint methodology review to align UX research standards.

### Shared Assets

- `reference/case-studies`
- `data/experiments`

### Return Protocol

Returns specify which findings lack sufficient evidence or methodological rigor. Deep Research addresses specific deficiencies and redelivers affected sections.

---

## 7. Storytelling Squad

### What Deep Research Sends (Outbound)

| Deliverable | Format | Description |
|---|---|---|
| Narrative-ready research findings | Structured narrative brief (markdown) | Findings pre-organized into narrative arcs with protagonist, conflict, resolution framing |
| Case study evidence packages | Evidence package (markdown + supporting files) | Complete case study materials: timeline, key actors, outcomes, source materials |
| Historical context and timeline data | Timeline report (markdown), using `templates/analysis` | Chronological event mapping with causal connections and turning points |

### What Deep Research Receives (Inbound)

| Deliverable | Expected Format | Description |
|---|---|---|
| Story angle research requests | Creative brief (markdown) | Proposed narrative angle, target audience, and specific research questions |
| Fact-verification for narratives | Draft narrative + flagged claims (markdown) | Story draft with specific factual claims requiring verification |
| Primary source interview analysis | Transcript + analysis brief (markdown) | Interview transcripts with specific analysis questions |

### Exit Gate (Before Sending)

- [ ] Cross-squad delivery checklist score >= 80%
- [ ] Findings are organized for narrative consumption (not academic structure)
- [ ] Case study packages include human-interest elements where available
- [ ] Timelines include causal narrative connections, not just chronological listing
- [ ] Source materials are accessible and quotable

### Entry Gate (When Receiving)

- [ ] Story angle is defined with target audience
- [ ] Specific claims to verify are identified in draft narratives
- [ ] Interview transcripts are complete and legible
- [ ] Analysis questions are specific (not "tell us what you find")

### SLA

| Direction | Turnaround |
|---|---|
| Outbound (Deep Research -> Storytelling Squad) | 5 business days for evidence packages; 3 business days for timeline data |
| Inbound (Storytelling Squad -> Deep Research) | 2 business days for fact-verification; 3 business days for story angle research |

### Escalation

- **Rejection**: Storytelling Squad specifies which narrative elements lack sufficient evidence. Deep Research supplements within 2 business days.
- **Delay**: SLA breach by more than 2 business days escalates to squad leads.
- **Quality dispute**: Joint session to calibrate research depth vs. narrative accessibility.

### Shared Assets

- `reference/case-studies`
- `reference/transcripts`
- `data/timelines`

### Return Protocol

Returns specify which narrative elements are unsupported or which case study components are missing. Deep Research supplements the original package rather than replacing it.

---

## 8. Movement Squad

### What Deep Research Sends (Outbound)

| Deliverable | Format | Description |
|---|---|---|
| Community sentiment research | Sentiment report (markdown), using `templates/analysis` | Sentiment analysis with methodology, sample characteristics, and trend direction |
| Social movement trend analysis | Trend report (markdown) | Movement identification, trajectory analysis, key actors, and momentum indicators |
| Audience behavior and motivation data | Behavioral analysis (markdown + data files) | Motivation frameworks, behavioral drivers, and engagement pattern analysis |

### What Deep Research Receives (Inbound)

| Deliverable | Expected Format | Description |
|---|---|---|
| Community insight research requests | Research brief (markdown) | Community definition, insight questions, and geographic/demographic scope |
| Movement trajectory analysis needs | Analysis brief (markdown) | Movement definition, trajectory questions, and comparison movements |
| Advocacy landscape mapping briefs | Mapping brief (markdown) | Advocacy domain, key players to map, and influence dimensions |

### Exit Gate (Before Sending)

- [ ] Cross-squad delivery checklist score >= 80%
- [ ] Sentiment analysis includes methodology and confidence intervals
- [ ] Movement analysis includes momentum indicators with evidence
- [ ] Behavioral data includes sample representativeness assessment
- [ ] Ethical considerations for community research are documented

### Entry Gate (When Receiving)

- [ ] Community or movement is defined with clear boundaries
- [ ] Research questions are specific and answerable
- [ ] Geographic and demographic scope is stated
- [ ] Ethical considerations for community research are acknowledged

### SLA

| Direction | Turnaround |
|---|---|
| Outbound (Deep Research -> Movement Squad) | 5 business days for sentiment research; 3 business days for trend analysis |
| Inbound (Movement Squad -> Deep Research) | Requests include stated deadlines aligned with campaign cycles |

### Escalation

- **Rejection**: Movement Squad specifies which community insights or sentiment findings are inadequate. Deep Research remediates within 3 business days.
- **Delay**: SLA breach by more than 2 business days escalates to squad leads.
- **Quality dispute**: Joint review to align on community research methodology standards.

### Shared Assets

- `reference/reports`
- `data/research`

### Return Protocol

Returns specify which community segments or behavioral findings are inadequate. Deep Research supplements with additional data collection or re-analysis of existing data.

---

## 9. Traffic Squad

### What Deep Research Sends (Outbound)

| Deliverable | Format | Description |
|---|---|---|
| SEO keyword research and opportunity data | Keyword report (CSV + narrative markdown) | Keyword clusters, search volume, difficulty, opportunity scores, and strategic recommendations |
| Content gap analysis reports | Gap analysis (markdown), using `templates/analysis` | Content coverage mapping, competitor content audit, and priority gap identification |
| Channel performance benchmarks | Benchmark report (markdown + data tables) | Channel-specific performance data with industry comparisons and trend direction |

### What Deep Research Receives (Inbound)

| Deliverable | Expected Format | Description |
|---|---|---|
| Search trend research requests | Research brief (markdown) | Target topics, geographic scope, and trend analysis timeframe |
| Audience intent analysis needs | Analysis brief (markdown) | Target audience, intent categories to analyze, and decision-stage mapping |
| Platform algorithm research briefs | Research brief (markdown) | Specific platforms, algorithm dimensions to investigate, and recency requirements |

### Exit Gate (Before Sending)

- [ ] Cross-squad delivery checklist score >= 80%
- [ ] Keyword data includes search volume, difficulty, and opportunity scoring methodology
- [ ] Content gap analysis includes competitor coverage for at least 3 competitors
- [ ] Benchmarks include data recency dates and source methodology
- [ ] Recency check passed -- all SEO/traffic data within 90-day window

### Entry Gate (When Receiving)

- [ ] Target topics or keywords are specified
- [ ] Geographic and language scope is defined
- [ ] Timeframe for trend analysis is stated
- [ ] Platform-specific requirements are identified

### SLA

| Direction | Turnaround |
|---|---|
| Outbound (Deep Research -> Traffic Squad) | 3 business days for keyword research; 5 business days for gap analysis |
| Inbound (Traffic Squad -> Deep Research) | 2 business days for search trend requests; 3 business days for intent analysis |

### Escalation

- **Rejection**: Traffic Squad specifies which data points or analysis dimensions are inadequate. Deep Research remediates within 2 business days.
- **Delay**: SLA breach by more than 2 business days escalates to squad leads.
- **Quality dispute**: Joint calibration on data freshness and methodology standards for SEO/traffic research.

### Shared Assets

- `data/benchmarks`
- `data/metrics`

### Return Protocol

Returns specify which data points are stale, which analysis dimensions are missing, or which methodology concerns exist. Deep Research refreshes specific data or extends analysis scope.

---

## 10. Cybersecurity Squad

### What Deep Research Sends (Outbound)

| Deliverable | Format | Description |
|---|---|---|
| Threat landscape research reports | Intelligence report (markdown), using `templates/analysis` | Threat actor profiles, attack vector analysis, and risk prioritization |
| Vulnerability intelligence briefings | Intelligence brief (markdown), using `templates/briefs` | Vulnerability assessments with exploitation likelihood, impact scoring, and remediation context |
| Regulatory compliance research | Compliance report (markdown) | Regulatory requirements mapping, compliance gap analysis, and jurisdiction-specific guidance |

### What Deep Research Receives (Inbound)

| Deliverable | Expected Format | Description |
|---|---|---|
| Threat actor research requests | Research brief (markdown) | Specific threat actors or groups, TTPs of interest, and scope boundaries |
| Security incident investigation briefs | Investigation brief (markdown) | Incident summary, indicators of compromise, and specific research questions |
| Compliance requirement research needs | Research brief (markdown) | Regulatory frameworks, jurisdictions, and specific compliance questions |

### Exit Gate (Before Sending)

- [ ] Cross-squad delivery checklist score >= 80%
- [ ] Threat intelligence includes confidence levels per attribution claim
- [ ] Vulnerability data references CVE identifiers where applicable
- [ ] Compliance research specifies exact regulatory provisions and effective dates
- [ ] Sensitive intelligence is classified and handling instructions are included
- [ ] Source verification completed for all threat intelligence claims

### Entry Gate (When Receiving)

- [ ] Threat actors or incident scope is clearly defined
- [ ] Classification level and handling instructions are provided
- [ ] Specific research questions are articulated (not open-ended)
- [ ] Timeline urgency is stated (incidents may require expedited turnaround)
- [ ] Relevant IOCs or technical artifacts are shared

### SLA

| Direction | Turnaround |
|---|---|
| Outbound (Deep Research -> Cybersecurity Squad) | 3 business days for threat reports; 1 business day for urgent vulnerability briefings |
| Inbound (Cybersecurity Squad -> Deep Research) | Incident investigations include stated urgency; compliance requests: 3 business days |

### Escalation

- **Rejection**: Cybersecurity Squad specifies which intelligence assessments or compliance findings are inadequate. Deep Research remediates within 1 business day for security-critical items.
- **Delay**: Any delay on active incident research escalates immediately to Deep Research Chief and Cybersecurity Squad lead.
- **Quality dispute**: Joint review with emphasis on attribution confidence and source reliability standards.

### Shared Assets

- `reference/reports`
- `reference/databases`
- `data/registries`

### Return Protocol

Returns on security-critical materials are treated as high-priority. Cybersecurity Squad provides specific intelligence gaps or accuracy concerns. Deep Research remediates within 1 business day and conducts a root cause review for attribution or sourcing failures.

---

## Universal Handoff Rules

These rules apply to all squad contracts above.

### Outbound Checklist (All Squads)

Every outbound handoff must satisfy:

1. Cross-squad delivery checklist passed (`checklists/cross-squad-research-delivery-checklist.md`, minimum 80% score; 92% for Advisory Board and C-Level Squad)
2. Metadata header present per `docs/cross-squad-handoff-policy.md`
3. Delivery package formatted per `templates/operational/cross-squad-delivery-template.md`
4. Handoff logged in `data/registries/cross-squad-handoff-registry.yaml`
5. Follow-up contact identified and available for 5 business days

### Inbound Checklist (All Squads)

Every inbound handoff is validated for:

1. Request scope is specific and bounded
2. Expected output format is stated
3. Timeline and priority are defined
4. Relevant context and prior research are provided
5. Point of contact for clarifying questions is identified

### Rejection and Return Workflow

1. Receiving squad issues a structured rejection within 1 business day of receipt.
2. Rejection includes specific deficiency items referencing the relevant contract section.
3. Originating squad acknowledges rejection within 4 hours.
4. Remediation deadline is set based on the contract SLA for that squad.
5. Remediated deliverable is resubmitted through the same handoff process.
6. If a second rejection occurs on the same deliverable, escalate to the Deep Research Chief and the receiving squad's lead for joint resolution.
7. All rejections and returns are logged in the handoff registry.

### Contract Review Cadence

- These contracts are reviewed quarterly as part of the `quarterly-research-quality-review` routing in `config.yaml`.
- SLA performance is tracked via the `cross-squad-utility` KPI.
- Contract amendments require agreement from both the Deep Research Chief and the counterpart squad lead.
