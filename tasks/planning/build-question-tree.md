# Build Question Tree

## Purpose
Decompose a complex research question into a hierarchical tree of sub-questions, ensuring comprehensive coverage and enabling parallel investigation by multiple agents.

## When to Use
- During research planning to break down a complex question
- When a single question spans multiple domains or dimensions
- When the research requires different methodologies for different aspects
- To identify gaps in the current understanding of a topic

## Agents Involved
- **Lead**: DeepResearch Chief
- **Supporting**: Domain Specialist
- **Consulted**: Specialist researchers for domain-specific sub-questions

## Inputs
- Core research question (clearly stated)
- Scope and boundary definitions
- Domain context and known information
- Desired depth of decomposition

## Steps
1. State the root question at Level 0 of the tree
2. Identify the major dimensions or facets of the question (Level 1 branches)
3. For each Level 1 branch, generate sub-questions that must be answered to address it
4. Continue decomposition to Level 2 and Level 3 as needed
5. Mark each leaf node as either answerable directly or requiring further decomposition
6. Identify dependencies between branches (questions that require answers from other branches)
7. Flag questions that overlap across branches to avoid duplicate work
8. Assign priority weights to each branch based on importance to the root question
9. Validate that answering all leaf questions would fully answer the root question
10. Identify any gaps where important aspects are not covered by any branch
11. Add bridge questions that connect related branches
12. Finalize the tree structure and document the decomposition rationale

## Quality Gates
- The tree covers all dimensions identified in scope definition
- Each leaf question is specific enough to be actionable
- No circular dependencies exist between branches
- Priority weights sum to a coherent allocation of effort
- Answering all leaves would comprehensively answer the root question
- Redundancy between branches is minimized

## Outputs
- Question decomposition tree (hierarchical structure)
- Dependency map between branches
- Priority-weighted branch list
- Gap analysis report
- Decomposition rationale notes

## Estimated Effort
- **Simple question (2-3 branches)**: 15-20 minutes
- **Moderate question (4-6 branches)**: 30-60 minutes
- **Complex question (7+ branches)**: 1-3 hours
