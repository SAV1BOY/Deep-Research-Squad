# Pearl & Mackenzie - The Book of Why: The New Science of Cause and Effect

## The Ladder of Causation

### Rung 1: Association (Seeing)
- Observing correlations in data
- "What if I see X?" / "How are X and Y related?"
- Most machine learning operates here
- Correlation does NOT imply causation

### Rung 2: Intervention (Doing)
- What happens if I change X?
- Requires understanding the causal mechanism
- Randomized controlled trials operate here
- "What if I do X?" differs from "What if I see X?"

### Rung 3: Counterfactuals (Imagining)
- What would have happened if X had been different?
- Requires a causal model of the world
- "What if X had not occurred?"
- Highest level of causal reasoning

## Key Concepts

### Confounders
- A variable that causes both X and Y, creating a spurious correlation
- Example: Ice cream sales and drowning deaths (confounder: hot weather)
- **Research impact**: Must identify and control for confounders
- Use DAGs (Directed Acyclic Graphs) to map causal relationships

### Mediators
- A variable on the causal path between X and Y
- X causes M, M causes Y
- Controlling for mediators removes the causal effect you want to measure

### Colliders
- A variable caused by both X and Y
- Conditioning on a collider creates a spurious association
- "Berkson's paradox": selecting on an outcome variable creates false correlations

### Simpson's Paradox
- A trend in aggregated data reverses when data is separated into groups
- Cannot be resolved by statistics alone; requires causal reasoning
- Must know the causal structure to decide whether to aggregate or separate

## Causal Reasoning Checklist
1. Draw a causal diagram (DAG) before analyzing data
2. Identify potential confounders
3. Determine if you need to control for a variable or not
4. Never control for a collider
5. Never control for a mediator if you want the total effect
6. Ask: Is this an association, intervention, or counterfactual question?
7. Check if the same data could support a different causal story

## Common Causal Fallacies in Research
- Confusing correlation with causation (the classic)
- Reversing cause and effect
- Ignoring common causes (omitted variable bias)
- Conditioning on colliders (selection bias)
- Using observational data to answer interventional questions

## Application to Deep Research
- Always ask "What is the causal mechanism?" not just "What is the correlation?"
- Draw causal diagrams for key relationships in your analysis
- When recommending actions, you need Rung 2 (intervention) reasoning
- For "what if" scenarios, you need Rung 3 (counterfactual) reasoning
- Be explicit about whether your evidence is associational or causal
- Flag causal claims that lack intervention or experimental evidence
