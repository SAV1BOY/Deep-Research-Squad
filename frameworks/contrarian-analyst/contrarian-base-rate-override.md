# Contrarian Base Rate Override Framework

## Purpose

Check base rates before accepting any exceptional claim. Before asking "Is this claim well-supported?" ask "How often do claims like this turn out to be true?" Base rates provide the prior probability that anchors rational evaluation. A claim supported by seemingly strong evidence can still be unlikely if the base rate for such claims is very low.

## When to Use

- When evaluating claims that something is exceptional, unprecedented, or transformative.
- When a startup, technology, or trend is described as "the next big thing."
- When predictions are made about future outcomes in uncertain domains.
- When a single study or data point is used to support a broad conclusion.
- When the claim would require you to update significantly from conventional wisdom.

## Inputs

- The specific claim being evaluated.
- Historical data on similar claims, predictions, or ventures in the same domain.
- The evidence presented in support of the claim.
- Context about the domain's track record of accuracy.

## Process

1. **Classify the claim.** What category does this claim belong to? (e.g., startup success prediction, medical breakthrough, market forecast, technology adoption timeline.)
2. **Find the base rate.** Research how often claims in this category turn out to be true. Use historical data, meta-analyses, or domain expertise.
3. **Establish the prior.** Before looking at case-specific evidence, state the probability based solely on the base rate.
4. **Evaluate the case-specific evidence.** Now examine the evidence for this particular claim. How strong is it? How unique is this case compared to the reference class?
5. **Apply Bayesian updating.** Update the base rate probability in light of the case-specific evidence. Strong, unique evidence can override a low base rate, but the evidence must be genuinely strong.
6. **Check for base rate neglect.** Are you or the source ignoring the base rate in favor of a compelling narrative? Narratives are persuasive but not evidence.
7. **Calibrate the final estimate.** The final probability should be between the base rate and whatever the case-specific evidence suggests, weighted by the strength of that evidence.
8. **State the conclusion with calibrated confidence.** Express the conclusion in terms that reflect the base rate context.

## Outputs

- The reference class and its historical base rate.
- The prior probability before case-specific evidence.
- The case-specific evidence and its assessed strength.
- The updated probability after incorporating case-specific evidence.
- A clearly stated conclusion that reflects base rate context.
- Comparison: what the conclusion would be with versus without base rate adjustment.

## Common Pitfalls

- **Wrong reference class.** Choosing a reference class that is too broad or too narrow to be informative.
- **Base rate neglect.** The most common error: ignoring base rates entirely because the specific case seems compelling.
- **Narrative override.** Letting a good story override statistical reality.
- **Anchoring on the base rate.** Refusing to update even when case-specific evidence is genuinely exceptional.
- **Availability bias.** Using memorable examples instead of actual base rate data.
- **Conflating frequency with applicability.** A base rate applies to a class; any individual case may differ.
- **Not searching hard enough for the base rate.** Base rate data often exists but requires effort to find.

## Quality Criteria

- The reference class must be explicitly stated and justified; do not use an implicit or assumed reference class.
- The base rate must come from actual data, not intuition or anecdote.
- The prior probability must be stated numerically or in a defined range before examining case-specific evidence.
- The final estimate must show the calculation path: base rate, evidence strength, updated probability.

## Related Frameworks

- `contrarian-null-hypothesis.md` - The null hypothesis often aligns with the base rate expectation.
- `contrarian-survivorship-audit.md` - Survivorship bias distorts perceived base rates upward.
- `data-researcher-base-rate-context.md` - Detailed methodology for finding and applying base rates.
- `data-researcher-statistical-literacy.md` - Statistical foundations for understanding base rates and Bayesian reasoning.
