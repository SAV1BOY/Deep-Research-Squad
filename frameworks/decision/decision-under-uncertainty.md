# Decision Under Uncertainty

## Purpose
A collection of decision frameworks for situations where information is incomplete, probabilities are unknown, or the future is fundamentally unpredictable. Standard expected-value analysis fails when you cannot reliably estimate probabilities or outcomes. These frameworks provide principled alternatives.

## When to Use
- When key probabilities cannot be estimated with confidence
- When outcomes are highly variable or include tail risks
- When the decision is irreversible or nearly so
- When traditional cost-benefit analysis feels insufficient given the uncertainty
- When you face deep uncertainty (unknown unknowns) rather than quantifiable risk

## Inputs
- Available options and their potential outcomes
- Known and unknown uncertainties
- The decision-maker's risk tolerance and values
- Any partial probability estimates, even rough ones
- The reversibility and magnitude of each option's consequences

## Process

### 1. Minimax Regret
Minimize the maximum regret you could experience:
- For each option, identify the worst-case outcome
- Calculate the "regret" for each option-scenario pair: the difference between what you got and the best you could have gotten
- Choose the option whose maximum regret across all scenarios is the smallest
- Best for: decisions where avoiding the worst outcome matters more than optimizing the best
- Limitation: can be overly conservative; ignores probability of scenarios

### 2. Robust Decision-Making
Choose strategies that perform acceptably across the widest range of futures:
- Define "acceptable performance" thresholds for key outcomes
- Test each option against many scenarios (not just a few)
- Identify which options meet the acceptable threshold in the most scenarios
- Prefer options that are "good enough" everywhere over options that are optimal somewhere and terrible elsewhere
- Best for: long-term strategic decisions with many possible futures
- Limitation: requires defining what "acceptable" means, which involves judgment

### 3. Real Options Thinking
Treat decisions as options that preserve future flexibility:
- Identify decisions that are reversible versus irreversible
- Prefer options that keep future choices open (buying options) over those that close them
- Calculate the value of waiting for more information before committing
- Stage large commitments into smaller, sequential decisions with decision points
- Best for: investment decisions, market entry, technology adoption
- Limitation: the option to wait has costs (delay, competitor moves, expiring opportunities)

### 4. Satisficing
Choose the first option that meets all minimum requirements:
- Define minimum acceptable criteria for each dimension that matters
- Evaluate options sequentially against these criteria
- Select the first option that passes all thresholds
- Do not optimize further once a satisfactory option is found
- Best for: decisions where the cost of continued analysis exceeds the value of finding the optimum
- Limitation: may miss a significantly better option that was next in the queue

### 5. Pre-Mortem Analysis
Imagine the decision has failed and reason backward:
- For each option, assume it was chosen and failed spectacularly
- Ask: what went wrong? What did we miss? What assumption was incorrect?
- Use these failure narratives to identify hidden risks and blind spots
- Strengthen the chosen option by addressing the most plausible failure modes
- Best for: any high-stakes decision, as a complement to other frameworks
- Limitation: does not help choose between options; helps stress-test a choice

### 6. Decision Hygiene
Reduce noise and bias in the decision process itself:
- Gather independent assessments before group discussion
- Use structured criteria rather than holistic judgment
- Consider the outside view: what happens in similar situations generally?
- Decompose the decision into component judgments and aggregate
- Best for: all decisions, as a meta-framework layered on top of other approaches

## Outputs
- A recommended decision approach matched to the type of uncertainty
- Analysis results from the applied framework
- Explicit acknowledgment of what is not known and how that shaped the decision
- Monitoring plan for key uncertainties that could change the calculus

## Common Pitfalls
- **Applying expected value when probabilities are unknown**: Expected value requires reliable probability estimates. Without them, use the frameworks above.
- **Analysis paralysis**: Uncertainty frameworks can generate endless analysis. Set a decision deadline and commit.
- **Confusing risk with uncertainty**: Risk is quantifiable. Uncertainty is not. Use the right framework for the right situation.
- **Ignoring the cost of inaction**: Every framework above can justify waiting. But waiting is itself a decision with consequences.
- **Over-reliance on one framework**: These frameworks are complementary. Use two or three and see if they converge.
- **Pretending uncertainty away**: The worst response to uncertainty is false precision. Acknowledge what you do not know.
