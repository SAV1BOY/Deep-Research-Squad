# DeepResearch Squad

**Transform any complex request into deep, verifiable, multi-angle research oriented toward decision-making.**

DeepResearch Squad is a multi-agent research system built on the orchestrator-worker pattern. Nineteen specialized agents collaborate through a structured pipeline to turn ambiguous questions into evidence-backed, decision-ready outputs. Every claim is sourced, every contradiction is surfaced, and every conclusion is traceable back to the evidence that supports it.

---

## Principles

The squad operates under six non-negotiable principles:

| Principle | Meaning |
|---|---|
| **evidence_before_opinion** | No claim enters the pipeline without a verifiable source. |
| **contradiction_before_conclusion** | Opposing evidence is actively sought before any synthesis is written. |
| **traceability_before_eloquence** | Every statement must trace back to its origin; style never overrides provenance. |
| **decision_before_ornament** | Outputs exist to support decisions, not to impress. |
| **memory_before_repetition** | Lessons, failures, and patterns are stored so research never starts from zero. |
| **clarity_before_volume** | A concise, precise answer beats a long, vague one every time. |

---

## Pipeline

Every research engagement flows through a defined sequence of stages:

```
Question → Scope → Source Plan → Evidence → Contradictions → Synthesis → Models → Decision → Memory
```

1. **Question** -- The raw request enters the system.
2. **Scope** -- The Scope Mapper decomposes the question into researchable sub-questions with boundaries.
3. **Source Plan** -- The Source Hunter and Query Strategist build a collection plan across databases, APIs, and open sources.
4. **Evidence** -- The Data Researcher, OSINT Investigator, and Literature Analyst collect and structure raw evidence.
5. **Contradictions** -- The Contrarian Analyst and Evidence Verifier stress-test claims, surface conflicts, and flag weaknesses.
6. **Synthesis** -- The Synthesis Writer and Reference Intellectual merge verified evidence into coherent narratives.
7. **Models** -- The Insight Modeler and Timeline Analyst build frameworks, scenarios, and projections.
8. **Decision** -- The Decision Analyst produces actionable recommendations with confidence levels.
9. **Memory** -- Findings, patterns, and lessons are archived for future research cycles.

---

## Architecture Overview

DeepResearch Squad follows an **orchestrator-worker** architecture:

- A **DeepResearch Chief** acts as the orchestrator, routing tasks, enforcing quality gates, and managing the overall pipeline.
- **18 specialist agents** act as workers, each owning a specific stage or capability within the pipeline.
- Communication flows through structured handoffs with defined input/output contracts at each stage.
- A central `config.yaml` serves as the routing brain, mapping request types to agent sequences and quality thresholds.

The system supports 8 project types out of the box: competitor war rooms, decision support, deep dives, due diligence, literature reviews, market intelligence, technical evaluations, and trend monitoring.

---

## Agent Roster

| # | Agent | Role |
|---|---|---|
| 1 | **DeepResearch Chief** | Orchestrator. Decomposes requests, assigns agents, enforces quality gates, and delivers final outputs. |
| 2 | **Research Architect** | Methodology designer. Structures investigation layers, defines research strategy, and designs agent coordination. |
| 3 | **Scope Mapper** | Defines research boundaries, sub-questions, and deliverable expectations. |
| 4 | **Query Strategist** | Designs search strategies, keyword taxonomies, and database query plans. |
| 5 | **Source Hunter** | Identifies, ranks, and validates primary and secondary sources. |
| 6 | **Data Researcher** | Collects, cleans, and structures quantitative and qualitative data. |
| 7 | **OSINT Investigator** | Gathers intelligence from open sources, public records, and digital footprints. |
| 8 | **Literature Analyst** | Conducts systematic reviews of academic and professional literature. |
| 9 | **Evidence Verifier** | Cross-checks claims, validates sources, and assigns confidence scores. |
| 10 | **Contrarian Analyst** | Actively seeks disconfirming evidence, alternative explanations, and blind spots. |
| 11 | **Timeline Analyst** | Maps events, trends, and evolution patterns across time. |
| 12 | **Insight Modeler** | Builds mental models, scenarios, and analytical frameworks from evidence. |
| 13 | **Synthesis Writer** | Merges multi-source evidence into coherent, structured narratives. |
| 14 | **Reference Intellectual** | Provides theoretical grounding, cross-disciplinary connections, and intellectual depth. |
| 15 | **Decision Analyst** | Translates research into actionable options with trade-offs and confidence levels. |
| 16 | **Research Auditor** | Runs final quality checks on completeness, accuracy, and internal consistency. |
| 17 | **Discovery Scout** | Explores adjacent topics, emerging signals, and unexpected connections. |
| 18 | **Domain Specialist** | Adaptable domain expert that provides context-specific knowledge across industries. |
| 19 | **Knowledge Librarian** | Manages institutional memory, registries, and cross-investigation knowledge transfer. |

---

## Directory Structure

```
Deep-Research-Squad/                  754+ files
├── agents/             (19)    Agent definitions with HRM prompt engineering
├── archive/            (21)    Archived outputs, deprecated templates, lessons learned
├── authority/          (22)    Standards, agent summaries, workshop kits
├── checklists/        (130)    Per-agent gates, macro, and system-level quality gates
├── data/               (34)    Registries, benchmarks, metrics, glossaries, experiments
├── docs/               (18)    Documentation, guides, policies, operating manuals
├── frameworks/        (114)    Universal, agent-specific, layer, and reference frameworks
├── lib/                (32)    Shared components, patterns, taxonomies, utilities
├── phrases/            (18)    Controlled vocabulary and reasoning phrase libraries
├── projects/           (55)    8 project types with phased execution templates
├── reference/          (91)    Books, papers, reports, databases, methods, psychology
├── scripts/            (14)    Generation, analysis, and operations automation
├── swipe/              (30)    Gold-standard example outputs for calibration
├── swipe-sources/       (8)    Source material references for swipe files
├── tasks/              (55)    Planning, collection, validation, synthesis, review, ops
├── templates/          (45)    Briefs, outputs, evidence, analysis, scorecards
├── voice/              (22)    Tone profiles, language guides, calibration, channels
└── workflows/          (21)    End-to-end pipeline workflow definitions (00-20)
```

---

## Quick Start

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Deep-Research-Squad
   ```

2. **Understand the project type**
   Browse `/projects/` to find the project template closest to your research need (e.g., `deep-dive-project`, `due-diligence-project`, `market-intelligence-project`).

3. **Review the checklist**
   Open the matching checklist in `/checklists/` to understand quality gates and required steps.

4. **Select and configure agents**
   Use the frameworks in `/frameworks/` to understand each agent's methodology. The Chief Research Architect orchestrates the pipeline; start there.

5. **Use templates for output**
   Pick an output template from `/templates/` to structure the deliverable (briefs, evidence tables, scorecards, analysis reports).

6. **Calibrate with swipe files**
   Compare your outputs against gold-standard examples in `/swipe/` before delivering.

7. **Archive lessons**
   After every engagement, record failures, successes, and patterns in `/archive/` so the squad gets smarter over time.

---

## Project Types

| Project | Description |
|---|---|
| Competitor War Room | Competitive intelligence and teardown analysis |
| Decision Support | Evidence-backed decision recommendations |
| Deep Dive | Comprehensive single-topic research |
| Due Diligence | Investment, vendor, or partner investigation |
| Literature Review | Systematic academic and professional literature synthesis |
| Market Intelligence | Market landscape, sizing, and trend analysis |
| Technical Evaluation | Architecture, technology, and capability assessment |
| Trend Monitoring | Ongoing signal detection and emerging trend tracking |

---

## System Statistics

| Category | Count | Description |
|---|---|---|
| Total Files | **754+** | Complete system across 17 directories |
| Agents | 19 | Specialized research agents with full CoT/ReAct protocols |
| Frameworks | 114 | Universal, agent-specific, layer, and reference frameworks |
| Checklists | 130 | Quality gates at every pipeline stage |
| Templates | 45 | Structured output templates for all deliverable types |
| Tasks | 55 | Executable task definitions across 7 categories |
| Workflows | 21 | End-to-end pipeline workflows (00-20) |
| Reference | 91 | Books, papers, methods, psychology, industry references |
| Projects | 55 | 8 project types with phased execution |
| Data/Registries | 34 | YAML registries, benchmarks, metrics, glossaries |

## Prompt Engineering

Every agent uses state-of-the-art prompt engineering:

- **Hierarchical Role Modeling (HRM)** — Identity, mission, scope, pipeline position
- **Chain-of-Thought (CoT)** — Step-by-step reasoning protocols
- **ReAct** — Reasoning + Acting interleaved patterns
- **Role-based Prompting** — Deep identity anchors with anti-patterns
- **Quality Gates** — Mandatory checkpoints before handoff
- **Escalation Protocols** — Clear rules for when to escalate vs. resolve

## Cross-Squad Integration

DeepResearch Squad integrates with 10 specialized squads:

| Squad | Integration |
|---|---|
| Data Squad | Raw datasets, statistical analysis, data visualizations |
| Advisory Board | Board-level reviews, governance, strategic priorities |
| C-Level Squad | Executive briefs, competitive intelligence, M&A mandates |
| Copy Squad | Fact-checking, evidence-sourced claims, data narratives |
| Brand Squad | Market perception, brand positioning, audience segmentation |
| Design Squad | UX research, design benchmarks, A/B test analysis |
| Storytelling Squad | Narrative research, case studies, historical context |
| Movement Squad | Community sentiment, social trends, advocacy landscape |
| Traffic Squad | SEO research, content gaps, channel benchmarks |
| Cybersecurity Squad | Threat landscape, vulnerability intelligence, compliance |

---

## License

MIT License. See [LICENSE](LICENSE) for details.
