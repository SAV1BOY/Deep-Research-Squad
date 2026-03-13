# CLAUDE.md -- Project Configuration for Claude Code

## Project Overview

DeepResearch Squad is a multi-agent deep research system that transforms complex questions into evidence-backed, decision-ready intelligence. It uses an orchestrator-worker architecture with 19 agents, 114 frameworks, 130+ checklists, 21 workflows, and 754+ total files. The system supports 8 project types: competitor war rooms, decision support, deep dives, due diligence, literature reviews, market intelligence, technical evaluations, and trend monitoring.

## Architecture

**Pattern:** Orchestrator-worker. The Chief Research Architect orchestrates; specialist agents execute.

**Pipeline flow:**
```
Question -> Scope -> Source Plan -> Evidence -> Contradictions -> Synthesis -> Models -> Decision -> Memory
```

**Seven layers:**
1. **Command** -- Chief Research Architect (orchestration, routing, quality enforcement)
2. **Decomposition** -- Scope Mapper, Query Strategist, Discovery Scout (question -> sub-questions)
3. **Collection** -- Source Hunter, Data Researcher, OSINT Investigator, Literature Analyst (sub-questions -> raw evidence)
4. **Verification** -- Evidence Verifier, Contrarian Analyst (raw evidence -> verified evidence)
5. **Synthesis** -- Synthesis Writer, Reference Intellectual (verified evidence -> narrative)
6. **Decision** -- Decision Analyst, Insight Modeler, Timeline Analyst, Research Auditor (narrative -> recommendations)
7. **Memory** -- Knowledge Librarian, archive subsystem (outcomes -> stored patterns)

## Key Files and Directories

| Path | Purpose |
|---|---|
| `config.yaml` | Routing brain -- maps request types to agent sequences, quality thresholds, templates |
| `agents/` | 17 agent definition files (markdown, HRM prompt engineering) |
| `frameworks/` | 114 frameworks -- universal, agent-specific, layer, and reference |
| `workflows/` | 21 pipeline stage definitions (numbered 00-20) |
| `checklists/` | 130+ quality gates -- per-agent, macro, and system-level |
| `templates/` | 45 output templates (briefs, evidence tables, scorecards) |
| `projects/` | 8 project types with phased execution templates |
| `tasks/` | 55 atomic task definitions across 7 categories |
| `lib/` | Shared components, patterns, taxonomies, utilities |
| `reference/` | 91 external references -- books, papers, methods |
| `swipe/` | Gold-standard example outputs for calibration |
| `data/` | Registries, benchmarks, metrics, glossaries |
| `voice/` | Tone profiles, language guides, calibration |
| `archive/` | Memory layer -- lessons learned, deprecated outputs |

## Agent Roster

All 19 agents as defined in `config.yaml`:

| Agent File | Role |
|---|---|
| `deepresearch-chief` | Orchestrator -- routes tasks, enforces quality gates, delivers final outputs |
| `research-architect` | Designs research methodology and execution plans |
| `scope-mapper` | Decomposes questions into bounded sub-questions (MECE) |
| `query-strategist` | Builds search strategies, keyword taxonomies, database query plans |
| `source-hunter` | Identifies, ranks, and validates primary/secondary sources |
| `data-researcher` | Collects and structures quantitative and qualitative data |
| `evidence-verifier` | Cross-checks claims, validates sources, assigns confidence scores |
| `literature-analyst` | Conducts systematic reviews of academic and professional literature |
| `osint-investigator` | Gathers intelligence from open sources and public records |
| `timeline-analyst` | Maps events, trends, and evolution patterns across time |
| `contrarian-analyst` | Seeks disconfirming evidence, alternative explanations, blind spots |
| `insight-modeler` | Builds mental models, scenarios, and analytical frameworks |
| `synthesis-writer` | Merges multi-source evidence into coherent structured narratives |
| `decision-analyst` | Produces actionable recommendations with trade-offs and confidence levels |
| `research-auditor` | Runs final quality checks on completeness, accuracy, consistency |
| `discovery-scout` | Explores adjacent topics, emerging signals, unexpected connections |
| `reference-intellectual` | Provides domain context, theoretical grounding, cross-disciplinary links |
| `domain-specialist` | Deep expertise for domain-specific analysis |
| `knowledge-librarian` | Archives findings, patterns, and lessons for future research cycles |

## Conventions

- **File naming:** kebab-case for all files and directories (e.g., `evidence-verifier.md`, `source-hunter`).
- **Markdown structure:** All agent and framework files use structured markdown with clear section headers.
- **Framework sections:** Every framework must include these sections in order: Purpose, When to Apply, Core Principles, Step-by-Step, Output Format, Integration, Anti-Patterns.
- **Agent prompt structure:** Uses HRM (Hierarchical Role Modeling) -- identity, mission, scope, pipeline position, output format, failure modes.
- **Workflow numbering:** Workflows are numbered 00-20 in execution order.

## Quality Standards

- **Evidence-first:** No claim enters the pipeline without a verifiable source. Unsourced assertions are rejected at quality gates.
- **MECE decomposition:** Sub-questions must be mutually exclusive and collectively exhaustive.
- **Confidence scoring:** 4-level scale -- High, Medium, Low, Contested. Levels must reflect genuine epistemic state, never inflated certainty.
- **Contradiction surfacing:** Opposing evidence is actively sought before synthesis. Both positions are recorded; the system does not silently pick a winner.
- **Quality gates at every transition:** Artifacts that fail a gate do not advance. After 2 consecutive failures, the Chief Architect intervenes.
- **Source diversity:** Minimum 3 independent source types required (academic, industry, government, journalistic).
- **Prompt engineering:** All agents use CoT (Chain-of-Thought) reasoning, ReAct (Reasoning + Acting) patterns, and role-based prompting.

## Rules for Modifying This Project

1. **Agent files:** Maintain the standard section structure (identity, mission, scope, pipeline position, methodology, output format, quality gates, escalation protocols, anti-patterns). Do not remove sections.
2. **Frameworks:** When adding a new framework, include all required sections: Purpose, When to Apply, Core Principles, Step-by-Step, Output Format, Integration, Anti-Patterns.
3. **Evidence policy:** All claims need evidence. Every factual statement must cite at least one source. Evidence chains must be traceable from raw source to final deliverable.
4. **Confidence calibration:** Confidence levels must be calibrated honestly. High = multiple independent authoritative sources. Contested = credible sources directly contradict each other.
5. **Config changes:** `config.yaml` controls routing logic. Changes to agent sequences or quality thresholds go here, not in agent files. Agents do not decide what comes next -- the config does.
6. **Pipeline integrity:** Data flows strictly downward. Feedback loops exist only at quality gate failures with specific remediation instructions.
7. **New agents:** Must be added to `config.yaml` under `squad.agents`, given an agent file in `agents/`, and wired into relevant routing entries.
