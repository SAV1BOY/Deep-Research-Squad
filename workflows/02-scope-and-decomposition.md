# Workflow 02: Scope and Decomposition

## Purpose
Break the approved research scope into a comprehensive set of subquestions using the MECE principle (Mutually Exclusive, Collectively Exhaustive). Build a structured question tree that ensures no gaps and no overlaps in coverage, so every agent knows exactly what they are responsible for.

## Trigger
- Approved research plan arrives from Workflow 01.
- A scope revision is requested after discovering gaps during collection.

## Agents Involved
- **Research Lead**: Validates the decomposition and approves the question tree.
- **Decomposition Analyst**: Performs the structured breakdown.
- **Domain Specialist**: Consulted when domain knowledge is needed to identify hidden subquestions.

## Inputs
- Approved research plan with preliminary question hierarchy.
- Domain context and terminology reference.
- Prior decompositions for similar research types (templates).

## Steps

1. **Extract the root question**: Isolate the single, overarching research question from the plan. Restate it in precise language. Confirm with Research Lead that this root captures the full intent.

2. **Choose decomposition framework**: Select the most appropriate decomposition lens:
   - **By dimension**: Break by aspects (technical, economic, social, legal).
   - **By time**: Break by past, present, future.
   - **By stakeholder**: Break by who is affected or involved.
   - **By process**: Break by stages or phases.
   - **By geography**: Break by region or jurisdiction.
   - Document why this framework was chosen.

3. **First-level decomposition**: Split the root question into 3-7 first-level subquestions. Each must be:
   - **Mutually exclusive**: No overlap in what two subquestions cover.
   - **Collectively exhaustive**: Together they cover 100% of the root question.
   - Independently answerable with available methods.

4. **MECE validation pass**: For each pair of first-level subquestions, explicitly test for overlap. For the full set, test for gaps by asking: "If we answer all of these, is there anything about the root question we still would not know?" Fix any failures.

5. **Second-level decomposition**: For each first-level subquestion with complexity score > 0.5, decompose further into 2-5 second-level subquestions. Apply the same MECE criteria. Limit tree depth to 3 levels maximum to avoid over-fragmentation.

6. **Identify cross-cutting themes**: Some topics cut across multiple branches (e.g., data quality, regulatory context). List these as cross-cutting themes that must be addressed in synthesis but are not standalone branches.

7. **Assign evidence requirements per node**: For each leaf-level subquestion, specify:
   - Minimum number of sources required.
   - Types of evidence acceptable (empirical data, expert opinion, case study).
   - Confidence threshold for considering the subquestion answered.

8. **Map dependencies**: Identify which subquestions depend on answers from other subquestions. Draw dependency arrows. Flag any circular dependencies as errors to resolve.

9. **Build the question tree document**: Produce a visual or structured representation of the full tree:
   - Root question at top.
   - First-level branches with labels.
   - Second-level leaves with evidence requirements.
   - Cross-cutting themes listed separately.
   - Dependency arrows annotated.

10. **Assign ownership**: Map each leaf-level subquestion to a specific agent or agent pair. Ensure no agent is overloaded (max 5 leaf questions per agent). Confirm agent acceptance.

11. **Stress-test the tree**: Run three challenges:
    - **Devil's advocate**: What question is this tree NOT asking that it should?
    - **So-what test**: If we answer every leaf, can we construct a meaningful answer to the root?
    - **Efficiency test**: Are any leaves redundant or unlikely to yield useful evidence?

12. **Approve and distribute**: Research Lead approves the final question tree. Distribute leaf assignments to agents with context on how their piece fits the whole.

## Quality Gates
- Every pair of sibling subquestions must pass the mutual exclusivity test.
- The full set of first-level subquestions must pass the collective exhaustiveness test.
- No leaf-level subquestion may be unanswerable with available methods.
- Tree depth must not exceed 3 levels.
- Every leaf must have an assigned owner and evidence requirements.
- The stress-test must be documented with responses to all three challenges.

## Outputs
- Approved question tree document (structured and visual).
- Leaf-level assignment cards for each agent.
- Cross-cutting themes list for synthesis phase.
- Dependency map for sequencing collection work.

## Next Workflow
- **03-source-strategy-and-routing.md** (design source strategy for each leaf).
- **04-collection-sprint.md** (begin collection once sources are identified).
