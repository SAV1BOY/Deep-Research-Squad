# Bayesian Updating

## Purpose
A disciplined method for updating beliefs when new evidence arrives. Ensures that prior knowledge is respected, new evidence is weighted appropriately, and the reasoning chain from prior to posterior is fully transparent and auditable.

## When to Use
- When new evidence arrives that may change an existing conclusion
- During evidence verification (RalphLoop R8) to update claim confidence
- When integrating findings from multiple sources with varying reliability
- Whenever a research conclusion needs to be revised rather than rebuilt from scratch
- To avoid both overreaction to new data and stubborn anchoring to old beliefs

## Inputs
- Prior belief: the current best estimate before new evidence (stated as a probability or confidence level)
- New evidence: the observation, data point, or claim being integrated
- Likelihood assessment: how expected this evidence would be if the belief were true vs. false
- Context: base rates, source reliability, and known biases

## Process (step-by-step)

### Step 1: State the Prior Belief
Articulate the current belief explicitly before encountering new evidence.
- What do you currently believe and with what confidence?
- What evidence supports this prior?
- Document this before looking at new evidence to prevent hindsight contamination.

### Step 2: Receive and Characterize New Evidence
Examine the new evidence on its own terms:
- What exactly does the evidence say?
- How reliable is the source?
- Is this evidence independent of the sources that formed the prior?
- Could this evidence have been produced by a different mechanism than the one assumed?

### Step 3: Calculate the Likelihood Ratio
Assess the diagnostic power of the evidence:
- **If the belief is true**, how likely is this evidence? (P(E|H))
- **If the belief is false**, how likely is this evidence? (P(E|not-H))
- The ratio P(E|H) / P(E|not-H) determines how much the evidence should shift the belief.

Interpretation guide:
- Ratio near 1: Evidence is equally expected under both hypotheses — low diagnostic value, minimal update
- Ratio >> 1: Evidence is much more expected if the belief is true — update toward the belief
- Ratio << 1: Evidence is much more expected if the belief is false — update away from the belief

### Step 4: Update the Posterior
Combine the prior with the likelihood ratio to form the updated belief:
- If the evidence is strongly confirming (ratio >> 1): increase confidence proportionally
- If the evidence is strongly disconfirming (ratio << 1): decrease confidence proportionally
- If the evidence is ambiguous (ratio near 1): minimal change — do not force an update

### Step 5: Document the Reasoning Chain
Record the full update path:
- Prior belief and confidence level
- New evidence and its source
- Likelihood ratio assessment and reasoning
- Posterior belief and updated confidence level
- What further evidence would cause the next update

## Handling Special Cases

### Confirming Evidence
- Confirming evidence should increase confidence, but with diminishing returns
- The tenth piece of confirming evidence matters less than the first
- Watch for confirmation bias: are you selectively noticing confirming evidence?

### Disconfirming Evidence
- Disconfirming evidence is more diagnostic than confirming evidence in most cases
- A single strong disconfirmation can outweigh multiple weak confirmations
- Resist the urge to dismiss disconfirming evidence by attacking the source

### Base Rate Neglect
- Always anchor on the base rate before updating with specific evidence
- Rare events remain rare even with seemingly strong evidence (the false positive paradox)
- Ask: "How common is this in the reference class?" before asking "How strong is this evidence?"

### Extraordinary Claims
- Extraordinary claims require extraordinary evidence — the prior for rare events is low
- A single source making an extraordinary claim should produce only a modest update
- Multiple independent sources making the same extraordinary claim warrant a larger update

## Outputs
- Updated belief with explicit confidence level
- Full reasoning chain from prior to posterior
- Documented likelihood ratio and its justification
- Identification of what further evidence would change the belief again
- Flag if the update was minimal (ambiguous evidence) or dramatic (strong disconfirmation)

## Common Pitfalls
- Anchoring too strongly on the prior and under-weighting new evidence
- Over-updating on vivid or emotionally compelling evidence regardless of its diagnostic power
- Ignoring base rates — the most common error in probabilistic reasoning
- Treating non-independent evidence as independent (double-counting correlated sources)
- Failing to state the prior explicitly — makes the update invisible and unauditable
- Confusing the absence of evidence with evidence of absence

## Related Frameworks
- research-stack.md (Bayesian updating operates within the Validation layer)
- ralphloop-deepresearch.md (used in R8: Verify Claims and R11: Analyze Data)
- signal-vs-noise-framework.md (signal strength maps to likelihood ratios)
- epistemic-humility-framework.md (posterior confidence maps to the epistemic scale)

## Templates (recommended)

### Belief Update Log
```
Belief: [statement]
Prior Confidence: [level or probability]
Prior Basis: [what evidence supported the prior]

New Evidence: [description]
Source: [reference]
Source Reliability: [High / Medium / Low]
Independent of Prior Sources: [Yes / No]

Likelihood if True (P(E|H)): [estimate]
Likelihood if False (P(E|not-H)): [estimate]
Likelihood Ratio: [value and interpretation]

Posterior Confidence: [updated level or probability]
Reasoning: [why this update magnitude]
Next Update Trigger: [what evidence would shift this further]
```
