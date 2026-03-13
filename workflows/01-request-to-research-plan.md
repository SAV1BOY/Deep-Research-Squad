# Workflow 01: Request to Research Plan

## Purpose
Transform an approved intake card into a fully scoped, actionable research plan. Define the research scope, select methodology, estimate timeline, identify which agents are needed, and get the plan approved before any collection work begins.

## Trigger
- An approved intake card arrives from Workflow 00.
- A request returns from clarification with updated parameters.

## Agents Involved
- **Research Lead**: Designs and approves the research plan.
- **Methodology Advisor**: Recommends research approaches based on question type.
- **Resource Allocator**: Maps agent availability and estimates capacity.

## Inputs
- Approved intake card from Workflow 00.
- Agent availability roster and current workload snapshot.
- Methodology playbook (reference catalog of research approaches).
- Historical plans for similar research types (for estimation calibration).

## Steps

1. **Review intake card**: Research Lead reviews the parsed question, complexity score, priority tier, and domain flags. Confirm that the question is still valid and no new context has emerged.

2. **Define research scope**: Write explicit scope boundaries:
   - **In scope**: List exactly what will be investigated.
   - **Out of scope**: List what will NOT be investigated and why.
   - **Scope risks**: Identify areas where scope may creep and set tripwires.

3. **Select methodology**: Based on research type and complexity, choose the primary methodology:
   - Systematic review (for fact-finding and landscape mapping).
   - Comparative framework (for comparative analysis).
   - Causal chain analysis (for causal investigation).
   - Scenario modeling (for forecasting).
   - Decision matrix construction (for decision support).
   - Document the rationale for methodology selection.

4. **Design question hierarchy**: Break the main research question into 3-7 sub-questions that, when answered, fully address the main question. Each sub-question must be independently answerable and collectively exhaustive.

5. **Identify required agents**: Map each sub-question to the agent best suited to answer it. Flag any gaps where no current agent has the needed capability. List agents:
   - Literature Analyst
   - OSINT Collector
   - Data Analyst
   - Domain Specialist (specify domain)
   - Synthesis Writer
   - Quality Auditor

6. **Estimate timeline**: For each sub-question, estimate collection time, analysis time, and synthesis time. Add buffer for contradictions and rework (default: 20% of total). Produce a Gantt-style sequence showing parallel and sequential phases.

7. **Define evidence requirements**: Set minimum evidence thresholds for each sub-question:
   - Minimum number of independent sources.
   - Required source diversity (at least 2 source classes).
   - Acceptable evidence grades (from the evidence ladder).

8. **Set quality targets**: Define what "done" looks like:
   - Minimum confidence level for final answer (e.g., 70% for P2, 90% for P0).
   - Maximum acceptable contradiction rate.
   - Required audit pass before delivery.

9. **Risk assessment**: Identify top 3 risks to plan success (e.g., data unavailability, domain complexity, time pressure). For each risk, define a mitigation strategy and an escalation trigger.

10. **Compile research plan document**: Assemble all elements into a single research plan document with sections for scope, methodology, question hierarchy, agent assignments, timeline, evidence requirements, quality targets, and risks.

11. **Plan review and approval**: Research Lead reviews the complete plan. If complexity score > 0.7 or priority is P0, require a second reviewer. Approve, request revision, or reject with rationale.

12. **Distribute assignments**: Once approved, distribute sub-question assignments to designated agents with their specific instructions, evidence requirements, and deadlines.

## Quality Gates
- Scope must have explicit in/out boundaries with no ambiguous zones.
- Question hierarchy must pass MECE check (mutually exclusive, collectively exhaustive).
- Every sub-question must have an assigned agent.
- Timeline must include buffer and must not exceed requester's deadline.
- Evidence requirements must be specific and measurable.
- Plan document must be complete with no placeholder sections.

## Outputs
- Approved research plan document.
- Agent assignment notifications with sub-question briefs.
- Timeline with milestones and checkpoints.
- Updated research request registry entry with plan link.

## Next Workflow
- **02-scope-and-decomposition.md** (for detailed MECE decomposition).
- **03-source-strategy-and-routing.md** (for source planning, can run in parallel).
