# DeepResearch Squad

**Transform any complex request into deep, verifiable, multi-angle research oriented toward decision-making.**

DeepResearch Squad is a multi-agent research system built on the orchestrator-worker pattern. Sixteen specialized agents collaborate through a structured pipeline to turn ambiguous questions into evidence-backed, decision-ready outputs. Every claim is sourced, every contradiction is surfaced, and every conclusion is traceable back to the evidence that supports it.

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

- A **Chief Research Architect** acts as the orchestrator, routing tasks, enforcing quality gates, and managing the overall pipeline.
- **15 specialist agents** act as workers, each owning a specific stage or capability within the pipeline.
- Communication flows through structured handoffs with defined input/output contracts at each stage.
- A central `config.yaml` serves as the routing brain, mapping request types to agent sequences and quality thresholds.

The system supports 8 project types out of the box: competitor war rooms, decision support, deep dives, due diligence, literature reviews, market intelligence, technical evaluations, and trend monitoring.

---

## Agent Roster

| # | Agent | Role |
|---|---|---|
| 1 | **Chief Research Architect** | Orchestrator. Decomposes requests, assigns agents, enforces quality gates, and delivers final outputs. |
| 2 | **Scope Mapper** | Defines research boundaries, sub-questions, and deliverable expectations. |
| 3 | **Query Strategist** | Designs search strategies, keyword taxonomies, and database query plans. |
| 4 | **Source Hunter** | Identifies, ranks, and validates primary and secondary sources. |
| 5 | **Data Researcher** | Collects, cleans, and structures quantitative and qualitative data. |
| 6 | **OSINT Investigator** | Gathers intelligence from open sources, public records, and digital footprints. |
| 7 | **Literature Analyst** | Conducts systematic reviews of academic and professional literature. |
| 8 | **Evidence Verifier** | Cross-checks claims, validates sources, and assigns confidence scores. |
| 9 | **Contrarian Analyst** | Actively seeks disconfirming evidence, alternative explanations, and blind spots. |
| 10 | **Timeline Analyst** | Maps events, trends, and evolution patterns across time. |
| 11 | **Insight Modeler** | Builds mental models, scenarios, and analytical frameworks from evidence. |
| 12 | **Synthesis Writer** | Merges multi-source evidence into coherent, structured narratives. |
| 13 | **Reference Intellectual** | Provides domain context, theoretical grounding, and cross-disciplinary connections. |
| 14 | **Decision Analyst** | Translates research into actionable options with trade-offs and confidence levels. |
| 15 | **Validation Agent** | Runs final quality checks on completeness, accuracy, and internal consistency. |
| 16 | **Discovery Agent** | Explores adjacent topics, emerging signals, and unexpected connections. |

---

## Directory Structure

```
Deep-Research-Squad/
├── agents/             # Agent definitions and configurations
├── archive/            # Archived outputs, deprecated templates, lessons learned
├── authority/          # Standards, agent summaries, workshop kits
├── checklists/         # Per-agent and cross-squad quality checklists
├── data/               # Benchmarks, case studies, confidence maps, experiments
├── docs/               # Documentation and guides
├── frameworks/         # Agent-specific analytical frameworks
├── lib/                # Shared components, patterns, taxonomies, utilities
├── phrases/            # Controlled vocabulary and phrase libraries
├── projects/           # Project type templates (8 types)
├── reference/          # Books, case studies, databases, industry references
├── scripts/            # Analysis, generation, and operations scripts
├── swipe/              # Gold-standard example outputs for calibration
├── swipe-sources/      # Source material for swipe file examples
├── tasks/              # Task definitions: collection, delivery, planning, review
├── templates/          # Output templates: analysis, briefs, evidence, scorecards
├── voice/              # Tone profiles, language guides, channel calibration
└── workflows/          # End-to-end workflow definitions
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

## License

See repository license file for details.
