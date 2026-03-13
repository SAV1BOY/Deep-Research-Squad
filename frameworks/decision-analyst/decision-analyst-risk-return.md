# Risk-Return Analysis Framework

## Purpose

Evaluate options through a risk-return lens. For each option, assess the expected value, the downside risk, and the upside potential. Identify asymmetric risk profiles where the potential gain far exceeds the potential loss (or vice versa). This framework moves beyond simple expected value to consider the shape and distribution of possible outcomes.

## When to Use

- When options carry meaningful risk and the decision is not just about the most likely outcome.
- When stakeholders need to understand not just what will probably happen but what could happen.
- When comparing options with different risk profiles (e.g., a safe bet vs. a high-risk high-reward play).
- When organizational risk tolerance needs to be explicitly factored into the decision.

## Inputs

- Options to evaluate with their potential outcomes.
- Probability estimates for different outcome scenarios.
- Magnitude of gains and losses under each scenario.
- Organizational or personal risk tolerance level.
- Information about the consequences of worst-case outcomes.

## Process

### Step 1: Outcome Scenario Definition
For each option, define three to five outcome scenarios:
- **Best case**: What happens if everything goes right? (Estimate probability: typically 10-20%)
- **Upside case**: What happens if things go better than expected? (Probability: 20-30%)
- **Base case**: What is the most likely outcome? (Probability: 30-50%)
- **Downside case**: What happens if things go worse than expected? (Probability: 20-30%)
- **Worst case**: What happens if everything goes wrong? (Probability: 10-20%)

### Step 2: Payoff Quantification
For each scenario of each option, quantify the payoff:
- In financial terms where applicable (revenue, cost, profit).
- In strategic terms where financial measures are insufficient (market position, capability, reputation).
- In human terms where relevant (lives affected, well-being, satisfaction).
Use consistent units across options for comparability.

### Step 3: Expected Value Calculation
For each option, calculate the probability-weighted average of all scenario payoffs. This is the expected value. It represents what you would get "on average" if you could make this decision many times.

### Step 4: Downside Risk Assessment
Focus on the negative scenarios:
- **Maximum loss**: What is the worst that could happen?
- **Probability of loss**: What is the chance of any negative outcome?
- **Expected loss**: Probability-weighted average of negative scenarios only.
- **Survivability**: Can the organization survive the worst case? Or is it an existential risk?
- **Recovery time**: If the downside materializes, how long to recover?

### Step 5: Upside Potential Assessment
Focus on the positive scenarios:
- **Maximum gain**: What is the best that could happen?
- **Probability of outsized gain**: What is the chance of exceeding the base case significantly?
- **Optionality**: Does this option create future options that have their own upside?
- **Compounding**: Can the gains build on themselves over time?

### Step 6: Asymmetry Analysis
Compare the downside and upside for each option:
- **Positive asymmetry**: Limited downside, large upside. These are attractive bets.
- **Negative asymmetry**: Limited upside, large downside. These are traps.
- **Symmetric**: Upside and downside are proportional. Standard risk-return trade-off.
Flag options with positive asymmetry as particularly worth considering.

### Step 7: Risk Tolerance Matching
Match each option's risk profile to the decision-maker's risk tolerance:
- **Risk-averse**: Prefer options with limited downside even if upside is also limited.
- **Risk-neutral**: Prefer the option with the highest expected value regardless of distribution.
- **Risk-seeking**: Prefer options with high upside even if downside is also high.
- **Ruin-averse**: Avoid any option where the worst case is unrecoverable, regardless of expected value.

### Step 8: Portfolio Thinking
Consider whether multiple options can be pursued simultaneously to diversify risk. If partial allocation is possible, a portfolio approach may dominate any single option.

## Outputs

- A risk-return profile for each option including expected value, maximum loss, maximum gain, and asymmetry classification.
- A scenario matrix showing payoffs across all scenarios for all options.
- Asymmetry analysis identifying positive and negative asymmetry opportunities.
- Risk tolerance recommendation mapping options to different risk appetites.
- A narrative summary highlighting the key risk-return trade-offs.

## Common Pitfalls

- **Expected value tunnel vision**: Focusing only on the average outcome and ignoring the distribution. An option with expected value of $100 that ranges from -$1000 to +$1200 is very different from one that ranges from $80 to $120.
- **Probability neglect**: Focusing on the magnitude of outcomes without weighting by probability.
- **Survivorship bias**: Studying only successful risk-takers and concluding that risk-taking is always rewarded.
- **Ignoring ruin risk**: No expected value calculation matters if the worst case is organizational death.
- **False precision**: Stating probabilities to two decimal places when the underlying estimates are rough guesses.
- **Static risk assessment**: Treating risk as fixed when it often changes as the situation evolves and information is gathered.

## Related Frameworks

- **decision-analyst-options-matrix.md** - Provides the option descriptions that feed into risk-return analysis.
- **decision-analyst-uncertainty.md** - Provides techniques for decision-making when risk estimates themselves are uncertain.
- **insight-modeler-scenario-tree.md** - Generates the scenarios used in risk-return analysis.
- **decision-analyst-trade-off-table.md** - Examines trade-offs between options with different risk-return profiles.
