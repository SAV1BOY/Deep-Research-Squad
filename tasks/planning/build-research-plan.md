# Build Research Plan

## Purpose
Transform a raw research request into a structured, actionable research plan with clear objectives, decomposed questions, source strategies, agent assignments, and quality criteria.

## When to Use
- A new research request has been received from a user or upstream squad
- An existing research plan needs to be rebuilt due to significant scope changes
- A complex question requires formal planning before execution begins

## Agents Involved
- **Lead**: Research Orchestrator
- **Supporting**: Domain Analyst, Source Curator, Contrarian Reviewer
- **Consulted**: All specialist researchers relevant to the domain

## Inputs
- Raw research request or question from the user
- Any constraints (timeline, depth, format, audience)
- Domain context or prior research if available
- Available agent roster and current workload

## Steps
1. Parse the research request to extract the core question, sub-questions, and implicit assumptions
2. Classify the research type (exploratory, evaluative, comparative, predictive, descriptive)
3. Define the target audience and required output format
4. Decompose the core question into a question tree (see `build-question-tree.md`)
5. Define scope and boundaries for each branch (see `define-scope-and-boundaries.md`)
6. Design the source strategy for each branch (see `design-source-strategy.md`)
7. Estimate effort and assign priority weights to each branch
8. Allocate agents to branches based on expertise (see `allocate-research-agents.md`)
9. Define quality gates and confidence thresholds for each branch
10. Set milestones, checkpoints, and a review schedule
11. Assemble the full plan document and submit for review
12. Incorporate feedback and finalize the plan

## Quality Gates
- Every sub-question maps back to the original request
- No critical dimension of the question is left unaddressed
- Source strategy covers at least three independent source categories
- Agent assignments match domain expertise requirements
- Timeline is realistic given scope and available resources
- Quality thresholds are explicitly stated for each deliverable

## Outputs
- Structured research plan document with all sections completed
- Question decomposition tree
- Agent assignment matrix
- Timeline with milestones and checkpoints
- Quality criteria checklist

## Estimated Effort
- **Simple request**: 15-30 minutes
- **Moderate complexity**: 1-2 hours
- **High complexity / multi-domain**: 2-4 hours
