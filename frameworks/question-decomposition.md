# Question Decomposition Framework

## Purpose
Break complex research questions into structured hierarchies of sub-questions,
enabling systematic investigation where each component can be independently
researched, verified, and reassembled into a comprehensive answer.

## When to Use
- The research question is multi-faceted or ambiguous.
- A direct answer would require synthesizing multiple domains.
- The question contains hidden assumptions that need surfacing.
- Initial research attempts return scattered or incomplete results.
- The scope of investigation is unclear.

## Inputs
- Original research question or topic.
- Domain context (if available).
- Known constraints or boundaries.
- Requester's intent and depth expectations.

## Process

### Step 1: Identify the Core Question
- Restate the question in the simplest possible form.
- Determine the question type: factual, causal, comparative, evaluative, or predictive.
- Clarify what a complete answer looks like.

### Step 2: Extract Hidden Assumptions
- List every assumption embedded in the question.
- Mark each as validated, unvalidated, or contested.
- Reformulate the question if assumptions prove false.

### Step 3: Decompose into Sub-Questions
- Break into Level 1 sub-questions (direct components of the core question).
- Break Level 1 into Level 2 sub-questions (supporting details).
- Continue decomposition until each sub-question is independently answerable.
- Aim for 3-7 sub-questions per level to maintain manageability.

### Step 4: Organize Hierarchically
- Arrange sub-questions in a tree structure.
- Label each node with its level and sequence number (e.g., 1.2.3).
- Group related sub-questions under common parent nodes.

### Step 5: Identify Dependencies
- Map which sub-questions depend on answers from others.
- Mark independent sub-questions that can be researched in parallel.
- Identify critical-path questions that block downstream investigation.
- Flag circular dependencies and resolve them.

### Step 6: Validate Completeness
- Check: does answering all sub-questions fully answer the core question?
- Identify gaps where no sub-question addresses a needed aspect.
- Verify no sub-question is redundant or out of scope.
- Confirm the decomposition matches the requester's intent.

## Outputs
- Hierarchical question tree with numbered nodes.
- Dependency map showing relationships between sub-questions.
- List of surfaced assumptions with validation status.
- Prioritized research order based on dependencies.
- Completeness assessment with identified gaps.

## Common Pitfalls
- **Over-decomposition**: Breaking questions so finely they lose meaning. Stop when
  sub-questions become trivially answerable.
- **Missing the real question**: Decomposing what was literally asked rather than
  what was actually meant. Always clarify intent.
- **Ignoring assumptions**: Treating embedded assumptions as facts leads to
  researching the wrong sub-questions entirely.
- **Flat decomposition**: Creating a long list instead of a hierarchy loses the
  logical relationships between sub-questions.
- **Scope creep**: Sub-questions that expand beyond the original question's
  boundaries. Each sub-question must serve the core question.
- **Dependency blindness**: Researching sub-questions in the wrong order wastes
  effort when earlier answers would reshape later questions.

## Related Frameworks
- **First-Principles Research**: Use when sub-questions hit fundamental concepts.
- **Unknowns and Assumptions**: Feeds directly into Step 2 assumption extraction.
- **Causal Layering**: Provides an alternative decomposition axis by depth of analysis.
- **Claim-to-Evidence Chain**: Apply to each sub-question's answer.

## Templates

### Question Tree Template
```
CORE QUESTION: [Restated core question]
Type: [factual | causal | comparative | evaluative | predictive]

1. [Level 1 Sub-Question A]
   1.1 [Level 2 Sub-Question]
   1.2 [Level 2 Sub-Question]
2. [Level 1 Sub-Question B]
   2.1 [Level 2 Sub-Question]
3. [Level 1 Sub-Question C]

ASSUMPTIONS:
- [Assumption 1]: [validated | unvalidated | contested]
- [Assumption 2]: [validated | unvalidated | contested]

DEPENDENCIES:
- Q2.1 depends on Q1 answer
- Q1 and Q3 are independent (parallel research)

GAPS IDENTIFIED:
- [Any aspect not covered by sub-questions]
```
