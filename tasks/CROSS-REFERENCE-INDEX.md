# Task Cross-Reference Index

## Purpose

Maps every task to its corresponding agents, frameworks, checklists, and templates as defined in `config.yaml` routing. This index serves as the single lookup reference for understanding which system components participate in each task and how tasks connect to the routing brain.

---

## Routing-Mapped Tasks

The following tasks have direct routing entries in `config.yaml`. Each entry shows the exact agents, frameworks, checklists, templates, and registries wired to that route.

---

### build-research-plan

- **Task File**: `tasks/planning/build-research-plan.md`
- **Config Route**: `routing.build-research-plan`
- **Description**: Decompose research question into sub-questions, define scope, and build execution plan
- **Agents**: deepresearch-chief, scope-mapper, query-strategist
- **Frameworks**: frameworks/scope-mapper, frameworks/query-strategist, frameworks/discovery
- **Checklists**: checklists/chief, checklists/scope, checklists/query, checklists/architect
- **Templates**: templates/operational, templates/analysis
- **Registry**: data/registries

---

### design-source-strategy

- **Task File**: `tasks/planning/design-source-strategy.md`
- **Config Route**: `routing.design-source-strategy`
- **Description**: Identify optimal source mix, databases, and collection methods for the research plan
- **Agents**: source-hunter, query-strategist, discovery-scout
- **Frameworks**: frameworks/source-hunter, frameworks/query-strategist, frameworks/discovery
- **Checklists**: checklists/source, checklists/query, checklists/discovery
- **Templates**: templates/operational
- **Registry**: data/registries

---

### run-deep-dive

- **Task File**: `tasks/collection/run-deep-dive.md`
- **Config Route**: `routing.run-deep-dive`
- **Description**: Execute primary research across sources, collect evidence, and build data corpus
- **Agents**: data-researcher, source-hunter, evidence-verifier, timeline-analyst
- **Frameworks**: frameworks/data-researcher, frameworks/source-hunter, frameworks/evidence-verifier, frameworks/timeline-analyst
- **Checklists**: checklists/data, checklists/source, checklists/evidence, checklists/timeline, checklists/verification
- **Templates**: templates/evidence, templates/analysis
- **Registry**: data/registries

---

### run-competitor-research

- **Task File**: `tasks/collection/run-competitor-research.md`
- **Config Route**: `routing.run-competitor-research`
- **Description**: Map competitive landscape, benchmark positioning, and identify strategic gaps
- **Agents**: data-researcher, source-hunter, insight-modeler, contrarian-analyst
- **Frameworks**: frameworks/data-researcher, frameworks/source-hunter, frameworks/insight-modeler, frameworks/contrarian-analyst
- **Checklists**: checklists/data, checklists/source, checklists/modeling, checklists/domain-stacks
- **Templates**: templates/analysis, templates/scorecards
- **Registry**: data/registries

---

### run-market-research

- **Task File**: `tasks/collection/run-market-research.md`
- **Config Route**: `routing.run-market-research`
- **Description**: Analyze market size, segmentation, trends, and customer dynamics
- **Agents**: data-researcher, source-hunter, insight-modeler, timeline-analyst
- **Frameworks**: frameworks/data-researcher, frameworks/source-hunter, frameworks/insight-modeler, frameworks/timeline-analyst
- **Checklists**: checklists/data, checklists/source, checklists/modeling, checklists/timeline
- **Templates**: templates/analysis, templates/scorecards
- **Registry**: data/registries

---

### run-technical-research

- **Task File**: `tasks/collection/run-technical-research.md`
- **Config Route**: `routing.run-technical-research`
- **Description**: Evaluate technology stacks, architectures, patents, and technical feasibility
- **Agents**: data-researcher, source-hunter, evidence-verifier, reference-intellectual
- **Frameworks**: frameworks/data-researcher, frameworks/source-hunter, frameworks/evidence-verifier, frameworks/reference-intellectual
- **Checklists**: checklists/data, checklists/source, checklists/evidence, checklists/verification, checklists/domain-stacks
- **Templates**: templates/evidence, templates/analysis
- **Registry**: data/registries

---

### run-literature-review

- **Task File**: `tasks/collection/run-literature-review.md`
- **Config Route**: `routing.run-literature-review`
- **Description**: Systematic review of academic papers, reports, and published research
- **Agents**: literature-analyst, reference-intellectual, evidence-verifier
- **Frameworks**: frameworks/literature-analyst, frameworks/reference-intellectual, frameworks/evidence-verifier
- **Checklists**: checklists/literature, checklists/evidence, checklists/verification
- **Templates**: templates/evidence, templates/analysis
- **Registry**: data/registries

---

### run-osint-investigation

- **Task File**: `tasks/collection/run-osint-investigation.md`
- **Config Route**: `routing.run-osint-investigation`
- **Description**: Open-source intelligence gathering across public records, social, and digital footprints
- **Agents**: osint-investigator, source-hunter, evidence-verifier, timeline-analyst
- **Frameworks**: frameworks/osint-investigator, frameworks/source-hunter, frameworks/evidence-verifier, frameworks/timeline-analyst
- **Checklists**: checklists/osint, checklists/source, checklists/evidence, checklists/timeline, checklists/verification
- **Templates**: templates/evidence, templates/analysis
- **Registry**: data/registries

---

### run-due-diligence

- **Task File**: `tasks/collection/run-due-diligence.md`
- **Config Route**: `routing.run-due-diligence`
- **Description**: Comprehensive due diligence on entities, financials, legal, and operational risk
- **Agents**: data-researcher, osint-investigator, evidence-verifier, timeline-analyst, contrarian-analyst
- **Frameworks**: frameworks/data-researcher, frameworks/osint-investigator, frameworks/evidence-verifier, frameworks/timeline-analyst, frameworks/contrarian-analyst
- **Checklists**: checklists/data, checklists/osint, checklists/evidence, checklists/timeline, checklists/verification, checklists/contrarian
- **Templates**: templates/evidence, templates/analysis, templates/scorecards
- **Registry**: data/registries

---

### run-trend-analysis

- **Task File**: `tasks/collection/run-trend-analysis.md`
- **Config Route**: `routing.run-trend-analysis`
- **Description**: Identify, validate, and project trends across time-series data and qualitative signals
- **Agents**: timeline-analyst, insight-modeler, data-researcher, discovery-scout
- **Frameworks**: frameworks/timeline-analyst, frameworks/insight-modeler, frameworks/data-researcher, frameworks/discovery
- **Checklists**: checklists/timeline, checklists/modeling, checklists/data, checklists/discovery
- **Templates**: templates/analysis, templates/scorecards
- **Registry**: data/registries

---

### run-thesis-test

- **Task File**: `tasks/validation/run-thesis-test.md`
- **Config Route**: `routing.run-thesis-test`
- **Description**: Stress-test the working thesis against evidence, counter-arguments, and edge cases
- **Agents**: contrarian-analyst, evidence-verifier, insight-modeler
- **Frameworks**: frameworks/contrarian-analyst, frameworks/evidence-verifier, frameworks/insight-modeler
- **Checklists**: checklists/contrarian, checklists/evidence, checklists/modeling, checklists/validation
- **Templates**: templates/analysis, templates/scorecards
- **Registry**: data/registries

---

### run-contrarian-pass

- **Task File**: `tasks/validation/run-contrarian-pass.md`
- **Config Route**: `routing.run-contrarian-pass`
- **Description**: Dedicated adversarial review -- steel-man opposites, find blind spots, rate confidence
- **Agents**: contrarian-analyst, reference-intellectual
- **Frameworks**: frameworks/contrarian-analyst, frameworks/reference-intellectual
- **Checklists**: checklists/contrarian, checklists/validation
- **Templates**: templates/analysis, templates/scorecards
- **Registry**: data/registries

---

### build-synthesis-report

- **Task File**: `tasks/synthesis/build-synthesis-report.md`
- **Config Route**: `routing.build-synthesis-report`
- **Description**: Weave all evidence, analysis, and contrarian findings into a unified research report
- **Agents**: synthesis-writer, insight-modeler, deepresearch-chief
- **Frameworks**: frameworks/synthesis-writer, frameworks/synthesis, frameworks/insight-modeler
- **Checklists**: checklists/synthesis, checklists/synthesis-stack, checklists/modeling
- **Templates**: templates/outputs, templates/analysis
- **Registry**: data/registries

---

### build-decision-brief

- **Task File**: `tasks/synthesis/build-decision-brief.md`
- **Config Route**: `routing.build-decision-brief`
- **Description**: Distill research into an actionable decision brief with recommendations and risk map
- **Agents**: decision-analyst, synthesis-writer, deepresearch-chief
- **Frameworks**: frameworks/decision-analyst, frameworks/decision, frameworks/synthesis-writer
- **Checklists**: checklists/decision, checklists/synthesis, checklists/chief
- **Templates**: templates/briefs, templates/outputs
- **Registry**: data/registries

---

### audit-research-quality

- **Task File**: `tasks/review/audit-research-quality.md`
- **Config Route**: `routing.audit-research-quality`
- **Description**: Post-delivery quality audit -- evidence integrity, bias check, completeness score
- **Agents**: research-auditor, deepresearch-chief
- **Frameworks**: frameworks/validation, frameworks/evidence-verifier
- **Checklists**: checklists/audit, checklists/validation, checklists/verification
- **Templates**: templates/scorecards, templates/operational
- **Registry**: data/registries

---

### compress-to-executive-summary

- **Task File**: `tasks/synthesis/compress-to-executive-summary.md`
- **Config Route**: `routing.compress-to-executive-summary`
- **Description**: Compress full research output into a one-page executive summary for time-constrained stakeholders
- **Agents**: synthesis-writer, decision-analyst
- **Frameworks**: frameworks/synthesis-writer, frameworks/decision-analyst
- **Checklists**: checklists/synthesis, checklists/decision
- **Templates**: templates/briefs, templates/outputs
- **Registry**: data/registries

---

### cross-squad-research-handoff

- **Task File**: `tasks/delivery/cross-squad-research-handoff.md`
- **Config Route**: `routing.cross-squad-research-handoff`
- **Description**: Package and hand off research artifacts to other squads with context and usage notes
- **Agents**: deepresearch-chief, synthesis-writer
- **Frameworks**: frameworks/synthesis-writer, frameworks/synthesis
- **Checklists**: checklists/cross-squad, checklists/chief
- **Templates**: templates/operational, templates/briefs
- **Registry**: data/registries

---

### update-registries

- **Task File**: `tasks/operations/update-registries.md`
- **Config Route**: `routing.update-registries`
- **Description**: Refresh source registries, confidence maps, and benchmark data stores
- **Agents**: deepresearch-chief, research-auditor, data-researcher
- **Frameworks**: frameworks/validation, frameworks/data-researcher
- **Checklists**: checklists/chief, checklists/audit, checklists/data
- **Templates**: templates/operational
- **Registry**: data/registries

---

### quarterly-research-quality-review

- **Task File**: `tasks/operations/review-research-quality-trends.md`
- **Config Route**: `routing.quarterly-research-quality-review`
- **Description**: Quarterly meta-review of research accuracy, prediction tracking, and process improvement
- **Agents**: deepresearch-chief, research-auditor, insight-modeler
- **Frameworks**: frameworks/validation, frameworks/insight-modeler
- **Checklists**: checklists/audit, checklists/validation, checklists/chief
- **Templates**: templates/scorecards, templates/operational
- **Registry**: data/registries, data/metrics, data/scorecards

---

## Non-Routed Tasks

The following 36 tasks do not have direct routing entries in `config.yaml`. Each is mapped to the routing entry it most likely supports based on its category, name, and functional purpose.

### Planning Tasks (Non-Routed)

| Task File | Likely Supporting Route(s) | Rationale |
|---|---|---|
| `tasks/planning/build-question-tree.md` | `routing.build-research-plan` | Question decomposition is a sub-step of research plan construction |
| `tasks/planning/define-scope-and-boundaries.md` | `routing.build-research-plan` | Scope definition feeds directly into the research plan |
| `tasks/planning/allocate-research-agents.md` | `routing.build-research-plan` | Agent allocation is an execution planning step within research plan build |
| `tasks/planning/risk-assessment-task.md` | `routing.build-research-plan`, `routing.run-due-diligence` | Risk assessment informs both planning and due diligence routes |
| `tasks/planning/stakeholder-alignment-task.md` | `routing.build-research-plan`, `routing.build-decision-brief` | Stakeholder alignment shapes both plan scope and decision brief framing |

### Collection Tasks (Non-Routed)

| Task File | Likely Supporting Route(s) | Rationale |
|---|---|---|
| `tasks/collection/run-data-collection.md` | `routing.run-deep-dive`, `routing.run-market-research` | General data collection supports deep dives and market research |
| `tasks/collection/run-benchmarking.md` | `routing.run-competitor-research`, `routing.run-technical-research` | Benchmarking feeds competitive and technical evaluations |
| `tasks/collection/patent-landscape-task.md` | `routing.run-technical-research` | Patent analysis is a sub-task of technical research |
| `tasks/collection/regulatory-scan-task.md` | `routing.run-due-diligence`, `routing.run-technical-research` | Regulatory scanning supports due diligence and tech compliance |
| `tasks/collection/expert-interview-synthesis-task.md` | `routing.run-deep-dive`, `routing.run-literature-review` | Expert interviews augment primary research and literature reviews |

### Validation Tasks (Non-Routed)

| Task File | Likely Supporting Route(s) | Rationale |
|---|---|---|
| `tasks/validation/build-evidence-table.md` | `routing.run-deep-dive`, `routing.run-thesis-test` | Evidence tables are built during deep dives and tested during thesis tests |
| `tasks/validation/build-confidence-map.md` | `routing.run-thesis-test`, `routing.audit-research-quality` | Confidence maps feed thesis testing and quality audits |
| `tasks/validation/build-contradiction-map.md` | `routing.run-contrarian-pass`, `routing.run-thesis-test` | Contradiction maps are core outputs of contrarian and thesis test passes |
| `tasks/validation/verify-claims.md` | `routing.run-deep-dive`, `routing.run-thesis-test` | Claim verification is a sub-task of evidence collection and thesis testing |
| `tasks/validation/run-source-audit.md` | `routing.audit-research-quality`, `routing.design-source-strategy` | Source auditing supports quality audits and strategy validation |
| `tasks/validation/bias-audit-task.md` | `routing.audit-research-quality`, `routing.run-contrarian-pass` | Bias audits are part of quality review and adversarial analysis |
| `tasks/validation/reproducibility-check-task.md` | `routing.audit-research-quality`, `routing.run-literature-review` | Reproducibility checking supports audits and literature reviews |

### Synthesis Tasks (Non-Routed)

| Task File | Likely Supporting Route(s) | Rationale |
|---|---|---|
| `tasks/synthesis/run-scenario-analysis.md` | `routing.build-synthesis-report`, `routing.build-decision-brief` | Scenario analysis feeds synthesis and decision outputs |
| `tasks/synthesis/build-causal-map.md` | `routing.build-synthesis-report`, `routing.run-trend-analysis` | Causal mapping supports synthesis narratives and trend analysis |
| `tasks/synthesis/build-implications-map.md` | `routing.build-decision-brief`, `routing.build-synthesis-report` | Implications mapping feeds decision briefs and synthesis |
| `tasks/synthesis/build-taxonomy.md` | `routing.build-research-plan`, `routing.build-synthesis-report` | Taxonomy construction supports both planning and synthesis |
| `tasks/synthesis/executive-summary-task.md` | `routing.compress-to-executive-summary` | Direct sub-task of executive summary compression |
| `tasks/synthesis/visual-synthesis-task.md` | `routing.build-synthesis-report`, `routing.compress-to-executive-summary` | Visual synthesis augments reports and executive summaries |

### Delivery Tasks (Non-Routed)

| Task File | Likely Supporting Route(s) | Rationale |
|---|---|---|
| `tasks/delivery/build-source-map.md` | `routing.design-source-strategy`, `routing.build-synthesis-report` | Source maps support strategy design and synthesis outputs |
| `tasks/delivery/prepare-final-delivery.md` | `routing.build-decision-brief`, `routing.build-synthesis-report` | Final delivery packaging follows decision brief and synthesis completion |
| `tasks/delivery/present-research-findings.md` | `routing.build-decision-brief`, `routing.compress-to-executive-summary` | Presentation prep follows decision brief and executive summary creation |
| `tasks/delivery/presentation-prep-task.md` | `routing.build-decision-brief`, `routing.compress-to-executive-summary` | Presentation materials support decision briefs and summaries |

### Review Tasks (Non-Routed)

| Task File | Likely Supporting Route(s) | Rationale |
|---|---|---|
| `tasks/review/review-confidence-levels.md` | `routing.audit-research-quality`, `routing.run-thesis-test` | Confidence review is a sub-step of audits and thesis tests |
| `tasks/review/review-methodology.md` | `routing.audit-research-quality`, `routing.quarterly-research-quality-review` | Methodology review supports quality audits and quarterly reviews |
| `tasks/review/review-source-diversity.md` | `routing.audit-research-quality`, `routing.design-source-strategy` | Source diversity review feeds audits and strategy validation |
| `tasks/review/peer-review-task.md` | `routing.audit-research-quality` | Peer review is a sub-process of quality auditing |
| `tasks/review/run-pre-mortem.md` | `routing.build-research-plan`, `routing.run-thesis-test` | Pre-mortem analysis supports planning risk assessment and thesis testing |

### Operations Tasks (Non-Routed)

| Task File | Likely Supporting Route(s) | Rationale |
|---|---|---|
| `tasks/operations/curate-source-library.md` | `routing.update-registries`, `routing.design-source-strategy` | Source library curation supports registry updates and strategy design |
| `tasks/operations/update-domain-knowledge.md` | `routing.update-registries`, `routing.quarterly-research-quality-review` | Domain knowledge updates feed registries and quarterly reviews |
| `tasks/operations/onboard-new-researcher.md` | `routing.quarterly-research-quality-review` | Onboarding is an operational process tied to quality review cycles |
| `tasks/operations/knowledge-transfer-task.md` | `routing.cross-squad-research-handoff`, `routing.quarterly-research-quality-review` | Knowledge transfer supports cross-squad handoffs and review cycles |

---

## Agent Coverage Matrix

This matrix shows which of the 19 agents participate in which routed tasks. An **X** marks agent participation as defined in `config.yaml` routing.

| Agent | build-research-plan | design-source-strategy | run-deep-dive | run-competitor-research | run-market-research | run-technical-research | run-literature-review | run-osint-investigation | run-due-diligence | run-trend-analysis | run-thesis-test | run-contrarian-pass | build-synthesis-report | build-decision-brief | audit-research-quality | compress-to-exec-summary | cross-squad-handoff | update-registries | quarterly-quality-review | **Total** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| deepresearch-chief | X | | | | | | | | | | | | X | X | X | | X | X | X | **6** |
| research-architect | | | | | | | | | | | | | | | | | | | | **0** |
| scope-mapper | X | | | | | | | | | | | | | | | | | | | **1** |
| query-strategist | X | X | | | | | | | | | | | | | | | | | | **2** |
| source-hunter | | X | X | X | X | X | | X | | | | | | | | | | | | **6** |
| data-researcher | | | X | X | X | X | | | X | X | | | | | | | | X | | **7** |
| evidence-verifier | | | X | | | X | X | X | X | | X | | | | | | | | | **6** |
| literature-analyst | | | | | | | X | | | | | | | | | | | | | **1** |
| osint-investigator | | | | | | | | X | X | | | | | | | | | | | **2** |
| timeline-analyst | | | X | | X | | | X | X | X | | | | | | | | | | **5** |
| contrarian-analyst | | | | X | | | | | X | | X | X | | | | | | | | **4** |
| insight-modeler | | | | X | X | | | | | X | X | | X | | | | | | X | **6** |
| synthesis-writer | | | | | | | | | | | | | X | X | | X | X | | | **4** |
| decision-analyst | | | | | | | | | | | | | | X | | X | | | | **2** |
| research-auditor | | | | | | | | | | | | | | | X | | | X | X | **3** |
| discovery-scout | | X | | | | | | | | X | | | | | | | | | | **2** |
| reference-intellectual | | | | | | X | X | | | | | X | | | | | | | | **3** |
| domain-specialist | | | | | | | | | | | | | | | | | | | | **0** |
| knowledge-librarian | | | | | | | | | | | | | | | | | | | | **0** |

### Coverage Summary

- **Most utilized agents** (6-7 routes): data-researcher (7), deepresearch-chief (6), source-hunter (6), evidence-verifier (6), insight-modeler (6)
- **Moderately utilized agents** (3-5 routes): timeline-analyst (5), contrarian-analyst (4), synthesis-writer (4), research-auditor (3), reference-intellectual (3)
- **Lightly utilized agents** (1-2 routes): scope-mapper (1), query-strategist (2), literature-analyst (1), osint-investigator (2), decision-analyst (2), discovery-scout (2)
- **Not routed** (0 routes): research-architect, domain-specialist, knowledge-librarian -- these agents are listed in `squad.agents` but have no direct routing entries; they are invoked dynamically by the Chief Research Architect or serve infrastructure roles

---

## Route-to-Task File Summary

| Config Route | Task File | Category |
|---|---|---|
| `routing.build-research-plan` | `tasks/planning/build-research-plan.md` | Planning |
| `routing.design-source-strategy` | `tasks/planning/design-source-strategy.md` | Planning |
| `routing.run-deep-dive` | `tasks/collection/run-deep-dive.md` | Collection |
| `routing.run-competitor-research` | `tasks/collection/run-competitor-research.md` | Collection |
| `routing.run-market-research` | `tasks/collection/run-market-research.md` | Collection |
| `routing.run-technical-research` | `tasks/collection/run-technical-research.md` | Collection |
| `routing.run-literature-review` | `tasks/collection/run-literature-review.md` | Collection |
| `routing.run-osint-investigation` | `tasks/collection/run-osint-investigation.md` | Collection |
| `routing.run-due-diligence` | `tasks/collection/run-due-diligence.md` | Collection |
| `routing.run-trend-analysis` | `tasks/collection/run-trend-analysis.md` | Collection |
| `routing.run-thesis-test` | `tasks/validation/run-thesis-test.md` | Validation |
| `routing.run-contrarian-pass` | `tasks/validation/run-contrarian-pass.md` | Validation |
| `routing.build-synthesis-report` | `tasks/synthesis/build-synthesis-report.md` | Synthesis |
| `routing.build-decision-brief` | `tasks/synthesis/build-decision-brief.md` | Synthesis |
| `routing.audit-research-quality` | `tasks/review/audit-research-quality.md` | Review |
| `routing.compress-to-executive-summary` | `tasks/synthesis/compress-to-executive-summary.md` | Synthesis |
| `routing.cross-squad-research-handoff` | `tasks/delivery/cross-squad-research-handoff.md` | Delivery |
| `routing.update-registries` | `tasks/operations/update-registries.md` | Operations |
| `routing.quarterly-research-quality-review` | `tasks/operations/review-research-quality-trends.md` | Operations |
