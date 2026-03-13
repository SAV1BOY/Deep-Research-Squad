# Scenario Tree Framework

## Purpose

Build branching scenario trees that map possible futures from the present. Each branch point represents a key uncertainty. Each leaf represents a distinct possible future with its own implications. The tree structure makes explicit what is uncertain, what drives divergence between futures, and how probable each scenario is.

## When to Use

- When the future is uncertain and multiple outcomes are plausible.
- When strategic planning requires preparing for different contingencies.
- When a decision depends on which future materializes.
- When communicating uncertainty to stakeholders who think in terms of "what will happen."

## Inputs

- Current situation assessment with known facts and trends.
- Identified key uncertainties that could resolve in different ways.
- Estimates of probability for different uncertainty resolutions.
- Understanding of how uncertainties interact with each other.

## Process

### Step 1: Uncertainty Identification
List all significant uncertainties that could affect the outcome. For each, define:
- What is uncertain (state it as a question).
- What are the possible resolutions (2-4 distinct outcomes per uncertainty).
- What is the estimated timeframe for resolution.
- What evidence or events would signal which resolution is occurring.

### Step 2: Uncertainty Prioritization
Rank uncertainties by two criteria:
- **Impact**: How much does the resolution of this uncertainty affect the overall outcome?
- **Unpredictability**: How evenly balanced are the possible resolutions?
Select the top 2-4 uncertainties for the tree. More than 4 makes the tree unmanageable.

### Step 3: Tree Construction
Build the tree from top (present) to bottom (future):
- **Root node**: Current situation.
- **First branch point**: Highest-priority uncertainty. Create a branch for each possible resolution.
- **Second branch point**: Next uncertainty, applied to each branch from the first level.
- Continue for each selected uncertainty.
- Number of leaf scenarios = product of branches at each level (e.g., 2 x 3 x 2 = 12 scenarios).

### Step 4: Scenario Description
For each leaf (terminal scenario), write a brief narrative:
- What resolved, and how, at each branch point.
- What the world looks like in this scenario.
- Who benefits and who is harmed.
- What the key characteristics of this future are.

### Step 5: Probability Assignment
Assign probabilities to each branch at each branch point. These must sum to 100% at each branch point. Leaf probabilities are the product of branch probabilities along their path. Flag where probability estimates are based on data versus judgment.

### Step 6: Implication Analysis
For each scenario (or at least the most probable and most consequential):
- What actions are optimal in this scenario?
- What actions are harmful in this scenario?
- What early warning signs indicate this scenario is materializing?

### Step 7: Robustness Testing
Identify actions that perform well across multiple scenarios (robust strategies) versus actions that excel in one scenario but fail in others (fragile strategies). Robust strategies are generally preferred unless the probability of one scenario is very high.

### Step 8: Monitoring Plan
For each branch point, define:
- What observable events or data would indicate which branch is being taken.
- When to check for these signals.
- What decision should be triggered by each signal.

## Outputs

- A visual scenario tree diagram with labeled branch points and leaf scenarios.
- Narrative descriptions for each scenario.
- Probability estimates for each branch and each leaf scenario.
- A robustness analysis comparing strategies across scenarios.
- A monitoring plan with early warning indicators for each branch.

## Common Pitfalls

- **Too many branches**: Including every uncertainty produces an unmanageable tree. Limit to 2-4 key uncertainties.
- **Equal probability trap**: Assigning equal probabilities to all branches out of laziness rather than analysis.
- **Scenario naming bias**: Giving scenarios loaded names ("Disaster" vs. "Golden Age") that bias evaluation.
- **Branch dependency neglect**: Treating uncertainties as independent when the resolution of one affects the probability of another.
- **Static trees**: Building the tree once and never updating as new information arrives.
- **Ignoring wild cards**: Excluding low-probability, high-impact scenarios because they seem unlikely.

## Related Frameworks

- **timeline-counterfactual-analysis.md** - Applies similar branching logic retrospectively rather than prospectively.
- **decision-analyst-uncertainty.md** - Provides techniques for making decisions given the scenario tree's probability distribution.
- **insight-modeler-causal-map.md** - Identifies the causal dynamics that drive branch outcomes.
- **decision-analyst-risk-return.md** - Evaluates risk-return profiles for strategies across scenarios.
