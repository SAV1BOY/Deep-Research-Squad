# DeepResearch Squad -- Architecture

This document describes the system design, agent hierarchy, pipeline mechanics, and engineering standards that govern the DeepResearch Squad.

---

## System Design Philosophy

The DeepResearch Squad is built on three architectural convictions:

1. **Research is a pipeline, not a prompt.** Complex research cannot be solved in a single generation step. It requires decomposition, parallel collection, adversarial verification, and structured synthesis -- each owned by a specialist.

2. **Quality is enforced at transitions, not at the end.** Every handoff between agents passes through a quality gate. Bad evidence never reaches synthesis. Unsourced claims never reach the decision layer.

3. **Memory compounds value.** Every engagement deposits patterns, failures, and validated knowledge into the archive. The system improves with use, not just with updates.

---

## Hierarchical Agent Model

The 16 agents are organized into seven functional layers. Each layer has clear responsibilities and defined interfaces with adjacent layers.

```
┌─────────────────────────────────────────────────┐
│  COMMAND                                        │
│  Chief Research Architect                       │
│  (orchestration, routing, quality enforcement)  │
├─────────────────────────────────────────────────┤
│  DECOMPOSITION                                  │
│  Scope Mapper · Query Strategist · Discovery    │
│  (question → researchable sub-questions)        │
├─────────────────────────────────────────────────┤
│  COLLECTION                                     │
│  Source Hunter · Data Researcher                │
│  OSINT Investigator · Literature Analyst        │
│  (sub-questions → raw evidence)                 │
├─────────────────────────────────────────────────┤
│  VERIFICATION                                   │
│  Evidence Verifier · Contrarian Analyst         │
│  (raw evidence → verified evidence)             │
├─────────────────────────────────────────────────┤
│  SYNTHESIS                                      │
│  Synthesis Writer · Reference Intellectual      │
│  (verified evidence → coherent narrative)       │
├─────────────────────────────────────────────────┤
│  DECISION                                       │
│  Decision Analyst · Insight Modeler             │
│  Timeline Analyst · Validation Agent            │
│  (narrative → actionable recommendations)       │
├─────────────────────────────────────────────────┤
│  MEMORY                                         │
│  Archive subsystem                              │
│  (outcomes → stored patterns and lessons)       │
└─────────────────────────────────────────────────┘
```

### Layer Responsibilities

**Command** -- The Chief Research Architect receives the initial request, classifies the project type, selects the agent sequence, and manages the full lifecycle. It is the only agent that communicates with the requester. All other agents communicate exclusively through structured handoffs.

**Decomposition** -- The Scope Mapper breaks the question into bounded sub-questions. The Query Strategist translates those sub-questions into executable search plans. The Discovery Agent explores adjacent territory for signals the scope might miss.

**Collection** -- Four agents work in parallel. The Source Hunter identifies and ranks sources. The Data Researcher pulls quantitative and qualitative data. The OSINT Investigator taps open-source intelligence channels. The Literature Analyst conducts systematic reviews.

**Verification** -- The Evidence Verifier cross-references claims against multiple sources and assigns confidence scores. The Contrarian Analyst deliberately seeks disconfirming evidence, alternative explanations, and logical weaknesses.

**Synthesis** -- The Synthesis Writer merges verified evidence into a structured narrative. The Reference Intellectual enriches the synthesis with theoretical context, historical parallels, and cross-disciplinary insight.

**Decision** -- The Decision Analyst produces options, trade-offs, and recommendations. The Insight Modeler builds scenarios and frameworks. The Timeline Analyst provides temporal context. The Validation Agent runs a final completeness and consistency check.

**Memory** -- After delivery, the archive subsystem stores findings, methodology notes, confidence maps, failures, and lessons learned. This layer feeds back into future decomposition and collection stages.

---

## Pipeline Stages and Data Flow

Each stage produces a typed artifact that the next stage consumes.

```
Stage              Input Artifact              Output Artifact             Owner(s)
─────              ──────────────              ───────────────             ────────
1. Intake          Raw request                 Classified request          Chief Architect
2. Scoping         Classified request          Scope document              Scope Mapper
3. Query Design    Scope document              Source plan + queries        Query Strategist, Source Hunter
4. Collection      Source plan                 Evidence table              Data Researcher, OSINT, Literature
5. Verification    Evidence table              Verified evidence table     Evidence Verifier, Contrarian
6. Synthesis       Verified evidence           Research narrative          Synthesis Writer, Reference
7. Modeling        Research narrative           Models + scenarios          Insight Modeler, Timeline Analyst
8. Decision        Models + narrative          Decision brief              Decision Analyst
9. Validation      Decision brief              Validated output            Validation Agent
10. Delivery       Validated output            Final deliverable           Chief Architect
11. Archival       Final deliverable           Memory artifacts            Archive subsystem
```

Data flows strictly downward through the pipeline. Feedback loops exist only at quality gate failures, where the artifact is returned to its producing layer with specific remediation instructions.

---

## Quality Gates

Every transition between pipeline stages passes through a quality gate. Gates are not optional -- an artifact that fails its gate does not advance.

### Gate Definitions

| Transition | Gate Name | Checks |
|---|---|---|
| Intake → Scoping | **Clarity Gate** | Request is unambiguous; project type is classified; success criteria are defined. |
| Scoping → Query Design | **Boundary Gate** | Sub-questions are MECE (mutually exclusive, collectively exhaustive); scope is neither too broad nor too narrow. |
| Query Design → Collection | **Coverage Gate** | Source plan covers at least 3 independent source types; no single-source dependency. |
| Collection → Verification | **Completeness Gate** | Evidence table has entries for every sub-question; data gaps are explicitly flagged. |
| Verification → Synthesis | **Confidence Gate** | Every claim has a confidence score; low-confidence items are marked; contradictions are documented. |
| Synthesis → Modeling | **Coherence Gate** | Narrative is internally consistent; all claims trace to verified evidence; no orphan assertions. |
| Modeling → Decision | **Utility Gate** | Models are actionable; scenarios have probability estimates; frameworks map to real options. |
| Decision → Validation | **Completeness Gate** | All original sub-questions are answered; confidence levels are stated; limitations are disclosed. |
| Validation → Delivery | **Release Gate** | Output matches the project template; evidence chain is intact; executive summary is present. |

### Gate Failure Protocol

1. The gate produces a rejection with specific failure reasons.
2. The artifact is returned to the producing agent with remediation instructions.
3. The agent revises and resubmits.
4. After 2 consecutive failures at the same gate, the Chief Architect intervenes to re-scope or reassign.

---

## Config.yaml as Routing Brain

The central configuration file acts as the system's routing brain. It defines:

- **Project type classification rules** -- How incoming requests are mapped to one of the 8 supported project types.
- **Agent sequences** -- Which agents are activated and in what order for each project type. Not every project type uses all 16 agents.
- **Quality thresholds** -- Minimum confidence scores, minimum source counts, and maximum allowed data gaps per project type.
- **Template mappings** -- Which output templates from `/templates/` are used for each project type.
- **Timeout and escalation rules** -- Maximum time per stage and escalation paths when agents stall.

The config separates routing logic from agent logic. Agents do not decide what comes next -- the config does. This makes the pipeline auditable, reproducible, and modifiable without touching agent prompts.

---

## Cross-Squad Integration Model

DeepResearch Squad is designed to operate both standalone and as part of a larger multi-squad ecosystem. Integration points:

- **Inbound** -- Other squads can submit research requests through a standardized request schema. The Chief Architect classifies and processes them identically to direct requests.
- **Outbound** -- Research outputs follow a standardized deliverable schema so downstream squads (strategy, operations, execution) can consume them without translation.
- **Shared memory** -- The archive subsystem exposes a read interface so other squads can query past findings without re-running research.
- **Cross-squad checklists** -- The `/checklists/cross-squad/` directory contains integration checklists ensuring handoffs between squads maintain evidence chains.

---

## Prompt Engineering Standards

All agent prompts in the squad follow three complementary techniques:

### Chain-of-Thought (CoT)

Every agent is instructed to show its reasoning steps explicitly before producing output. This serves two purposes: it improves output quality through structured thinking, and it creates an audit trail that the Validation Agent can inspect.

### ReAct (Reasoning + Acting)

Collection-layer agents (Source Hunter, Data Researcher, OSINT Investigator, Literature Analyst) use the ReAct pattern: reason about what information is needed, act to retrieve it, observe the result, and iterate. This prevents blind data collection and keeps collection targeted.

### Role-Based Prompting

Each agent operates with a defined role identity that includes:
- A specific professional persona (e.g., "You are a senior investigative analyst...")
- Explicit scope boundaries (what the agent is and is not responsible for)
- Output format requirements (structured artifacts, not free text)
- Failure modes to watch for and self-correct

Prompts are stored in `/frameworks/` with one directory per agent. Each framework directory contains the agent's methodology, decision rules, and output specifications.

---

## Evidence Policy

Evidence is the core currency of the system. The following rules apply globally:

1. **Source requirement** -- Every factual claim must cite at least one source. Unsourced claims are rejected at the Confidence Gate.

2. **Confidence scoring** -- Evidence is scored on a 4-level scale:
   - **High** -- Multiple independent, authoritative sources confirm the claim.
   - **Medium** -- At least one authoritative source confirms; no contradicting evidence found.
   - **Low** -- Single source or non-authoritative source; or minor contradictions exist.
   - **Contested** -- Credible sources directly contradict each other.

3. **Contradiction documentation** -- When sources disagree, both positions are recorded with their supporting evidence. The system does not silently pick a winner.

4. **Recency weighting** -- More recent sources are preferred, all else being equal. The evidence table records publication dates and flags stale data.

5. **Source diversity** -- The Coverage Gate requires at least 3 independent source types (e.g., academic, industry, government, journalistic). Mono-source research is rejected.

6. **Evidence chain integrity** -- From raw source to final deliverable, every transformation of a claim is logged. The Validation Agent can trace any statement in the output back to its original source.

---

## Directory Mapping to Architecture

| Directory | Architectural Role |
|---|---|
| `agents/` | Agent runtime definitions |
| `frameworks/` | Agent methodologies and decision rules |
| `checklists/` | Quality gate criteria per agent and stage |
| `templates/` | Output format specifications |
| `projects/` | Project type configurations |
| `tasks/` | Atomic task definitions for pipeline stages |
| `workflows/` | End-to-end pipeline definitions |
| `lib/` | Shared components and utilities |
| `data/` | Benchmarks, case studies, and experimental results |
| `reference/` | External reference material |
| `swipe/` | Gold-standard output examples |
| `voice/` | Tone and language calibration |
| `archive/` | Memory layer storage |
| `authority/` | Standards and governance |
| `scripts/` | Operational automation |
| `docs/` | System documentation |
| `phrases/` | Controlled vocabulary |
