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

The 19 agents are organized into seven functional layers. Each layer has clear responsibilities and defined interfaces with adjacent layers.

```
┌─────────────────────────────────────────────────┐
│  COMMAND                                        │
│  DeepResearch Chief                       │
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

**Command** -- The DeepResearch Chief receives the initial request, classifies the project type, selects the agent sequence, and manages the full lifecycle. It is the only agent that communicates with the requester. All other agents communicate exclusively through structured handoffs.

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
- **Agent sequences** -- Which agents are activated and in what order for each project type. Not every project type uses all 19 agents.
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

---

## HRM Decision Cascade

The Hierarchical Role Modeling (HRM) Decision Cascade defines five levels of authority, validation, and escalation. Each level has its own quality gate. Output must clear the gate at its current level before it can rise to the next.

```
┌─────────────────────────────────────────────────────────────────┐
│  Level 5: HRM Chief (System-Level)                              │
│  Final authority. If output is below standard, loops back to    │
│  the appropriate level with remediation instructions.           │
├─────────────────────────────────────────────────────────────────┤
│  Level 4: Cross-Squad Handoff                                   │
│  Exit gate at sending squad + Entry gate at receiving squad.    │
│  Both gates must pass for handoff to complete.                  │
├─────────────────────────────────────────────────────────────────┤
│  Level 3: Chief Orchestration                                   │
│  Chief Architect validates assembled output against the         │
│  original request. Final squad-level quality gate.              │
├─────────────────────────────────────────────────────────────────┤
│  Level 2: Team / Layer Coordination                             │
│  Layer lead checks that all agents within the layer produced    │
│  compatible, complete artifacts. Layer quality gate.            │
├─────────────────────────────────────────────────────────────────┤
│  Level 1: Agent Execution                                       │
│  Individual agent executes subtask and self-validates against   │
│  its own checklist. Agent quality gate.                         │
└─────────────────────────────────────────────────────────────────┘
```

### Level-by-Level Detail

**Level 1 -- Agent Execution**
- The agent receives a typed input artifact and produces a typed output artifact.
- Before submitting, the agent runs its own checklist (found in `checklists/agents/`).
- **On failure:** The agent revises internally. If the agent fails its own gate twice, it escalates to Level 2 with a description of what it cannot resolve.

**Level 2 -- Team / Layer Coordination**
- The layer coordinator checks that all agent outputs within the layer are mutually consistent, complete, and properly formatted.
- The layer quality gate (found in `checklists/macro/`) validates cross-agent alignment.
- **On failure:** The coordinator identifies which agent produced the non-conforming artifact and returns it with specific remediation instructions. If the layer fails its gate twice, it escalates to Level 3.

**Level 3 -- Chief Orchestration**
- The Chief Research Architect validates the assembled pipeline output against the original request scope, confidence requirements, and template expectations.
- This is the final squad-level quality gate. It checks end-to-end evidence chain integrity, completeness against the scope document, and deliverable formatting.
- **On failure:** The Chief identifies the weakest link in the pipeline and routes the artifact back to the responsible layer (Level 2) or agent (Level 1) with targeted instructions. After 2 consecutive chief-level rejections, the Chief may re-scope the engagement or reassign agents.

**Level 4 -- Cross-Squad Handoff**
- When output leaves the DeepResearch Squad for another squad, it must pass the exit gate (completeness, confidence thresholds, proper packaging).
- The receiving squad applies its own entry gate to verify the handoff package meets its input requirements.
- **On failure at exit gate:** Output is returned to Level 3 for remediation. **On failure at entry gate:** The receiving squad returns the package with specific deficiency notes; the sending squad's Chief addresses them at Level 3.

**Level 5 -- HRM Chief (System-Level)**
- The HRM Chief monitors cross-squad flow and overall system performance.
- If any squad's output consistently fails downstream entry gates or if end-to-end latency exceeds thresholds, the HRM Chief intervenes.
- **On failure:** The HRM Chief can loop output back to any level (1 through 4) with remediation directives, reassign work across squads, or trigger a full re-scope of the engagement.

---

## RalphLoop / Kaizen Protocol

The RalphLoop is the system's continuous improvement cycle. It operates at four cadences, ensuring the squad becomes more effective with every engagement.

### After Every Research Engagement

- **Lessons learned capture:** The Knowledge Librarian records what worked, what failed, and what was unexpected. Stored in `archive/lessons/`.
- **Registry updates:** Every completed task updates the relevant registries in `data/registries/`. Source quality ratings, methodology effectiveness scores, and agent performance metrics are refreshed.
- **Failure documentation:** Every quality gate failure during the engagement is logged with root cause analysis and the remediation that resolved it. Stored in `archive/failures/`.

### Quarterly Review

- **Prediction accuracy:** Compare forecasts and confidence scores from past engagements against actual outcomes. Recalibrate confidence scoring if systematic bias is detected.
- **Methodology effectiveness:** Rank frameworks by how often they contributed to high-confidence outputs versus how often they were associated with gate failures. Flag underperforming frameworks for review.
- **Agent utilization:** Identify agents that are consistently underused or overburdened. Adjust routing rules in `config.yaml` if patterns warrant it.
- **Metrics rollup:** Aggregate per-engagement KPIs into quarterly scorecards stored in `data/scorecards/`.

### Semi-Annual Review

- **Framework refresh:** Update frameworks in `frameworks/` based on quarterly findings. Retire weak patterns that consistently underperform. Promote strong emerging patterns to standard use.
- **Checklist revision:** Update quality gate checklists in `checklists/` to reflect new failure modes discovered in the preceding period.
- **Reference refresh:** Review `reference/` materials for staleness. Add newly discovered authoritative sources. Remove or flag outdated references.
- **Agent prompt tuning:** Revise agent definitions in `agents/` based on accumulated performance data and failure analysis.

### Continuous (Every Task)

- **Registry writes:** Every completed atomic task writes its results to the relevant registry. This is not batched -- it happens immediately upon task completion.
- **Pattern recognition:** The Knowledge Librarian flags recurring failure patterns. If the same root cause appears three or more times, it triggers a framework or checklist update outside the normal review cadence.

---

## Operational Memory Architecture

The `data/` directory is the squad's operational memory. Unlike the `archive/` directory (which stores completed engagement outputs), `data/` contains living operational data that is read and written during active engagements.

### Components

**Registries** (`data/registries/`)
- Living databases updated after every task completion.
- Include source quality ratings, domain expert directories, methodology performance scores, and tool effectiveness records.
- Agents in the Collection and Decomposition layers read registries to inform their strategies.

**Metrics** (`data/metrics/`)
- KPI tracking at two granularities: per-engagement and quarterly aggregate.
- Tracked metrics include time-per-stage, gate pass/fail rates, confidence score distributions, source diversity indices, and requester satisfaction scores.
- The Research Auditor and Chief Architect reference metrics to identify systemic issues.

**Decisions** (`data/decisions/`)
- Log of every Chief Architect routing and escalation decision, with full context: what the input was, what options were considered, what was chosen, and why.
- Enables post-engagement auditing and supports the quarterly methodology review.

**Scorecards** (`data/scorecards/`)
- Periodic squad performance snapshots produced during quarterly reviews.
- Capture aggregated gate pass rates, average confidence scores, engagement cycle times, and agent utilization rates.
- Used by the HRM Chief (Level 5) to assess squad health.

**Research** (`data/research/`)
- Structured outputs from completed research engagements, indexed for retrieval.
- The Knowledge Librarian maintains the index. Other squads can query this store through the shared memory interface.

### Feedback Loop

Memory feeds back into the pipeline at three points:

1. **Decomposition** -- The Scope Mapper and Query Strategist consult registries and past research to avoid redundant work and to identify known knowledge gaps.
2. **Collection** -- Source Hunter and Data Researcher check source quality registries to prioritize high-quality sources and avoid previously unreliable ones.
3. **Validation** -- The Research Auditor compares current engagement metrics against historical baselines to flag anomalies (unusually low confidence, unusually fast completion, etc.).

---

## Cross-Squad Handoff Protocol

When the DeepResearch Squad sends output to or receives input from another squad, the following protocol governs the handoff.

### Exit Gate

Before output can leave the squad, it must satisfy all of the following:

- All sub-questions from the original scope are answered or explicitly marked as unanswerable with justification.
- Confidence scores are assigned to every claim.
- The evidence chain is intact from source to conclusion.
- The output conforms to the designated project template.
- Limitations and caveats are explicitly stated.
- The Research Auditor has signed off.

### Handoff Package

Every cross-squad handoff is wrapped in a standardized envelope containing:

| Component | Description |
|---|---|
| **Output artifact** | The research deliverable itself (brief, report, evidence table, etc.) |
| **Context summary** | The original request, scope boundaries, and methodology used |
| **Confidence map** | Per-claim confidence scores with justification |
| **Limitations disclosure** | Known gaps, contested findings, and areas of uncertainty |
| **Usage notes** | How the output should and should not be used; known constraints on applicability |
| **Source manifest** | Complete list of sources consulted, with quality ratings |
| **Engagement metadata** | Timeline, agents involved, gate pass/fail history |

### Entry Gate at Receiving Squad

The receiving squad checks:

- The handoff package is structurally complete (all components present).
- Confidence scores meet the receiving squad's minimum thresholds for its intended use.
- Limitations are acceptable given the downstream application.
- The source manifest demonstrates adequate diversity and quality.

### Return Protocol

If the entry gate fails:

1. The receiving squad produces a rejection notice with specific deficiencies listed.
2. The rejection is sent to the DeepResearch Squad's Chief Architect.
3. The Chief Architect triages: minor gaps are routed to the responsible agent; major gaps may trigger a partial re-run of the pipeline.
4. The revised handoff package is resubmitted. If rejected a second time, both Chiefs escalate to the HRM Chief (Level 5).

### SLA (Service-Level Agreements)

| Handoff Type | Expected Response Time |
|---|---|
| Standard research request | Determined by project type and scope complexity |
| Urgent / time-sensitive request | Prioritized in the Chief's queue; expedited pipeline with reduced but documented quality thresholds |
| Rejection turnaround | Acknowledged within one cycle; remediated within two cycles |
| Escalation to HRM Chief | Resolved within one cycle of escalation |

Response times are measured in pipeline cycles, not wall-clock time, since the system operates within AI orchestration contexts.

---

## Failure Modes and Recovery

The following are the primary failure modes the system is designed to detect and recover from.

### Scope Creep

**Symptom:** Sub-questions multiply beyond the original scope boundary. Collection agents pursue tangential evidence. Pipeline stages take disproportionately long.

**Detection:** The Chief Architect monitors scope document growth and collection breadth against the original classified request.

**Recovery:** The Chief intervenes to re-bound the scope. Extraneous sub-questions are pruned or deferred to a follow-up engagement. The Scope Mapper is directed to produce a revised, tighter scope document. The pipeline resumes from the revised scope.

### Source Drought

**Symptom:** Collection agents return insufficient evidence for one or more sub-questions. The Completeness Gate fails due to empty cells in the evidence table.

**Detection:** The Completeness Gate flags sub-questions with zero or below-threshold evidence entries.

**Recovery:**
1. The Query Strategist generates alternative search strategies (different keywords, different databases, different source types).
2. The OSINT Investigator broadens its aperture to include non-traditional sources.
3. The Discovery Scout explores adjacent domains for transferable evidence.
4. If the drought persists after two collection cycles, the Chief Architect reclassifies the sub-question as unanswerable with justification and adjusts confidence scores accordingly.

### Contradictory Evidence

**Symptom:** The Confidence Gate flags multiple claims with "Contested" status. The evidence table contains irreconcilable data from credible sources.

**Detection:** The Evidence Verifier identifies contradictions during cross-referencing. The Confidence Gate surfaces them formally.

**Recovery:**
1. The Contrarian Analyst is escalated to lead a dedicated contradiction resolution pass.
2. Both positions are documented with full evidence chains.
3. The Insight Modeler builds scenarios for each position, showing downstream implications.
4. The Decision Analyst presents the contradiction transparently in the output, with recommendations conditional on which position holds.
5. The output is never allowed to silently pick a winner.

### Quality Gate Cascade Failure

**Symptom:** An artifact fails the same gate three or more times. Or artifacts fail at multiple sequential gates, indicating a systemic issue rather than a localized error.

**Detection:** The Chief Architect tracks gate failure counts per engagement. Two consecutive failures at the same gate trigger intervention (per standard protocol). Three or more trigger cascade analysis.

**Recovery:**
1. The Chief Architect halts forward pipeline progress.
2. Root cause analysis: Is the issue with the agent, the input it received, or the gate criteria itself?
3. **Agent issue:** Reassign to a different agent or adjust the agent's framework parameters.
4. **Input issue:** Trace back to the producing layer and remediate there first.
5. **Gate criteria issue:** If the gate is flagged as potentially miscalibrated, the Research Auditor reviews the gate definition. Gate changes require Chief approval and are logged in `data/decisions/`.
6. The pipeline resumes from the point of remediation.

### Cross-Squad Blockage

**Symptom:** A handoff package is rejected by the receiving squad, and remediation efforts within the DeepResearch Squad do not resolve the deficiency. Or the receiving squad is unresponsive.

**Detection:** The return protocol tracks rejection cycles. Two rejections of the same handoff trigger escalation.

**Recovery:**
1. **Remediation failure:** Both Chiefs (sending and receiving) confer to align on requirements. If alignment fails, the HRM Chief arbitrates.
2. **Unresponsive receiver:** The Chief Architect routes the output to an alternative consuming squad if one exists, or queues the output with an alert to the HRM Chief.
3. **Fundamental mismatch:** If the research output cannot satisfy the receiver's needs due to inherent limitations (e.g., insufficient data exists), this is documented as a system constraint and escalated to the HRM Chief for strategic resolution.
