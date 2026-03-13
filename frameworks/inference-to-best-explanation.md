# Inference to Best Explanation

## Purpose
A systematic method for choosing among competing explanations by evaluating each on multiple criteria of explanatory quality. Ensures that the selected explanation is not merely plausible but demonstrably superior to alternatives across a defined set of dimensions.

## When to Use
- When multiple hypotheses could explain the same set of observations
- During synthesis (Research Stack Layer 3) to select among competing models
- When building explanatory models (RalphLoop R15)
- When a phenomenon has no single obvious cause and competing theories exist
- Before committing to a causal narrative in any research deliverable

## Inputs
- The phenomenon, pattern, or dataset to be explained
- A set of competing explanations (at least 2, ideally 3-5)
- The available evidence base
- Background knowledge and established theories in the domain

## Process (step-by-step)

### Step 1: Define the Explanandum
State precisely what needs to be explained:
- What is the specific observation, pattern, or phenomenon?
- What are its boundaries — what counts as part of it and what does not?
- What would a complete explanation need to account for?

### Step 2: Generate Competing Explanations
List all plausible explanations, including:
- The leading hypothesis
- Alternative hypotheses from credible sources
- At least one heterodox or unconventional explanation
- The null hypothesis (the phenomenon is random, coincidental, or an artifact)

Rule: Do not pre-filter. Include explanations that feel unlikely. Premature elimination is a bias.

### Step 3: Evaluate Each Explanation on Criteria

**Criterion 1: Explanatory Breadth**
How much of the evidence does this explanation account for?
- Does it explain all key observations, or only a subset?
- Does it handle edge cases and anomalies?
- Score: Comprehensive / Partial / Narrow

**Criterion 2: Simplicity (Parsimony)**
How many assumptions does the explanation require?
- Fewer ad hoc assumptions are better, all else equal
- Complexity is acceptable only when simpler explanations fail
- Score: Parsimonious / Moderate / Complex

**Criterion 3: Coherence with Known Facts**
Is the explanation consistent with established knowledge?
- Does it contradict well-established findings?
- Does it fit within known causal mechanisms?
- Score: Coherent / Partially Coherent / Incoherent

**Criterion 4: Predictive Power**
Does the explanation predict new observations that can be checked?
- Explanations that only explain past data are weaker than those that predict future data
- Has it made predictions that were subsequently confirmed?
- Score: Strong / Moderate / Weak / None

**Criterion 5: Testability**
Can the explanation be tested or falsified?
- What evidence would confirm it? What evidence would refute it?
- If no evidence could refute it, it has low explanatory value
- Score: Testable / Partially Testable / Unfalsifiable

### Step 4: Compare and Select
Build a comparison matrix with all explanations scored on all criteria. The best explanation is the one that scores highest across the full set of criteria, with particular weight on breadth and coherence.

Decision rules:
- If one explanation dominates on all criteria, select it
- If explanations trade off across criteria, weight breadth and coherence most heavily
- If two explanations are close, prefer the simpler one (Occam's razor as tiebreaker)
- If no explanation is clearly best, document the tie and identify what evidence would break it

### Step 5: Document Why Alternatives Were Rejected
For each rejected explanation, record:
- Which criteria it failed on
- What specific evidence it could not account for
- Under what conditions it might be reconsidered

This creates an audit trail and prevents re-litigation of settled questions.

### Step 6: State Confidence and Limitations
- How much better is the selected explanation than the next-best alternative?
- What evidence is the selection most sensitive to?
- What new evidence would cause a revision?

## Outputs
- Ranked list of explanations with scores on all five criteria
- Selected best explanation with supporting rationale
- Rejection rationale for each alternative
- Confidence assessment and reversal conditions
- Evidence gaps that would strengthen or weaken the selection

## Common Pitfalls
- Evaluating only two explanations (my theory vs. obviously wrong) — always include a third
- Conflating familiarity with explanatory power — well-known explanations are not always best
- Over-weighting simplicity at the expense of explanatory breadth
- Ignoring the null hypothesis — sometimes the data is noise
- Failing to document why alternatives were rejected — leads to re-litigation
- Selecting an explanation that is coherent but unfalsifiable — coherence without testability is weak
- Anchoring on the first explanation encountered

## Related Frameworks
- steel-manning.md (steelman alternative explanations before rejecting them)
- signal-vs-noise-framework.md (verify the explanandum is signal before explaining it)
- bayesian-updating.md (update explanation selection when new evidence arrives)
- research-stack.md (IBE operates within the Synthesis layer)

## Templates (recommended)

### Explanation Comparison Matrix
```
Explanandum: [what is being explained]

| Criterion          | Explanation A | Explanation B | Explanation C | Null Hypothesis |
|--------------------|---------------|---------------|---------------|-----------------|
| Breadth            |               |               |               |                 |
| Simplicity         |               |               |               |                 |
| Coherence          |               |               |               |                 |
| Predictive Power   |               |               |               |                 |
| Testability        |               |               |               |                 |
| Overall            |               |               |               |                 |

Selected: [which and why]
Runner-up: [which and what would change the selection]
```

### Rejection Record
```
Explanation: [description]
Failed Criteria: [list]
Key Evidence Not Explained: [specifics]
Reconsider If: [what new evidence would reopen this explanation]
```
