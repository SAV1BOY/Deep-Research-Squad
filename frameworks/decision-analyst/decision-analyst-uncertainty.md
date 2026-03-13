# Decision-Making Under Uncertainty Framework

## Purpose

Provide structured techniques for making decisions when outcomes are uncertain and probability estimates may be unreliable. This framework covers classical decision theory approaches (minimax, maximin, expected value) as well as modern techniques (real options, reversible vs. irreversible decisions) to help decision-makers act wisely even when they cannot predict outcomes confidently.

## When to Use

- When the decision involves significant uncertainty that cannot be resolved before acting.
- When probability estimates for key outcomes are unreliable or contested.
- When the cost of waiting for more information may exceed the cost of acting now.
- When stakeholders are paralyzed by uncertainty and need a structured path forward.

## Inputs

- The decision to be made and the available options.
- Known uncertainties and their possible resolutions.
- Any available probability estimates (even rough ones).
- Payoff estimates for each option under each possible state of the world.
- The decision-maker's risk tolerance and constraints.

## Process

### Step 1: Uncertainty Characterization
Classify the type of uncertainty:
- **Risk**: Probabilities are known or estimable (e.g., historical data exists).
- **Ambiguity**: Probabilities are unknown but possible states are known.
- **Deep uncertainty**: Neither probabilities nor possible states are fully known.
The appropriate decision technique depends on the type of uncertainty.

### Step 2: Payoff Matrix Construction
Build a matrix with options as rows and possible states of the world as columns. Each cell contains the payoff (outcome value) if that option is chosen and that state occurs. If probabilities are available, note them above each column.

### Step 3: Decision Criteria Selection
Choose the appropriate decision criterion based on uncertainty type and risk tolerance:

**For decisions under risk (probabilities known):**
- **Expected Value**: Choose the option with the highest probability-weighted average payoff. Best when the decision is repeated many times or the stakes are moderate.
- **Expected Utility**: Like expected value but adjusted for risk aversion. Use when stakes are high enough that the decision-maker cares about variance, not just average.

**For decisions under ambiguity (probabilities unknown):**
- **Maximin (pessimistic)**: For each option, find the worst possible payoff. Choose the option whose worst case is least bad. Conservative strategy that guards against disaster.
- **Maximax (optimistic)**: For each option, find the best possible payoff. Choose the option with the highest best case. Aggressive strategy for risk-seekers.
- **Minimax Regret**: For each state, find the best option. Calculate regret for each cell (best payoff in that state minus actual payoff). Choose the option that minimizes maximum regret. Balanced strategy.
- **Laplace (principle of insufficient reason)**: Assign equal probability to all states and maximize expected value. Reasonable when there is genuinely no basis for distinguishing probabilities.

### Step 4: Reversibility Analysis
Classify each option by reversibility:
- **Reversible decisions**: Can be undone at low cost. Bias toward action; try and learn.
- **Irreversible decisions**: Cannot be undone. Bias toward caution; gather more information.
- **Partially reversible**: Can be undone but at significant cost. Moderate caution.
Jeff Bezos' framework: Type 1 (irreversible) vs. Type 2 (reversible) decisions.

### Step 5: Real Options Assessment
Identify whether any option creates future options that have independent value:
- Does Option A open doors that Option B closes?
- Can you take a small initial step that preserves future flexibility?
- What is the value of waiting for more information before committing fully?
In high uncertainty, options that preserve flexibility are worth more than their immediate payoff suggests.

### Step 6: Information Value Analysis
Assess whether gathering more information before deciding is worthwhile:
- What information would change the decision?
- How much would it cost to obtain?
- How long would it take?
- Is the information reliable enough to change the uncertainty classification?
If no obtainable information would change the decision, stop researching and decide.

### Step 7: Robustness Check
Test whether the chosen option performs acceptably across all plausible states, not just the most likely ones. A robust choice may not be optimal in any single state but avoids catastrophe in all of them.

### Step 8: Decision Documentation
Record the decision, the technique used, the uncertainties acknowledged, and the conditions under which the decision should be revisited.

## Outputs

- A completed payoff matrix with options, states, and payoffs.
- Application of at least two decision criteria with their respective recommendations.
- Reversibility classification for each option.
- Real options analysis identifying flexibility-preserving options.
- A justified decision recommendation with explicit uncertainty acknowledgment.
- Trigger conditions for revisiting the decision as uncertainty resolves.

## Common Pitfalls

- **Analysis paralysis**: Using uncertainty as a reason to never decide. At some point, the cost of delay exceeds the value of additional information.
- **False certainty**: Treating uncertain probability estimates as precise and applying expected value maximization when the estimates are unreliable.
- **Criterion shopping**: Trying multiple decision criteria until one supports the preferred option.
- **Ignoring reversibility**: Treating reversible and irreversible decisions with the same level of caution.
- **Option blindness**: Failing to see that waiting, staging, or piloting are options that preserve flexibility.
- **Uncertainty conflation**: Treating all uncertainties as the same type when they require different techniques.

## Related Frameworks

- **decision-analyst-risk-return.md** - Provides detailed risk-return analysis for decisions under risk.
- **insight-modeler-scenario-tree.md** - Generates the scenarios that populate the payoff matrix.
- **decision-analyst-recommendation.md** - Structures the final recommendation incorporating uncertainty analysis.
- **timeline-counterfactual-analysis.md** - Tests causal assumptions that underlie uncertainty estimates.
