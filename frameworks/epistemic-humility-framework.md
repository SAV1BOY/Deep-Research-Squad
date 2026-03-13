# Epistemic Humility Framework

## Purpose
A systematic approach to classifying and communicating the certainty level of every research conclusion. Prevents false precision, makes uncertainty explicit, and ensures that stakeholders understand not just what we believe but how strongly we believe it and why.

## When to Use
- When stating any research conclusion or recommendation
- During synthesis (Research Stack Layer 3-4, RalphLoop R13-R16)
- When communicating findings to decision-makers
- As a final check before any deliverable is finalized
- Whenever the temptation arises to present a conclusion as more certain than the evidence warrants

## Inputs
- Research conclusions and recommendations
- The evidence base supporting each conclusion
- Knowledge of evidence gaps, contradictions, and limitations
- Understanding of the domain's inherent predictability

## Process (step-by-step)

### Step 1: Classify Every Conclusion
Assign each conclusion to one of five levels on the epistemic scale:

**Level 1: Certain**
- Definition: Supported by overwhelming, independently verified evidence with no credible counter-evidence
- Evidence standard: Multiple independent sources, replicated findings, well-understood mechanism, strong base rate alignment
- Language: "The evidence conclusively shows..." / "It is established that..."
- Caution: True certainty is rare in research. Reserve this level for findings where being wrong would overturn fundamental knowledge.

**Level 2: Probable**
- Definition: Supported by strong evidence with minor gaps or caveats. The most likely conclusion given current data.
- Evidence standard: Multiple corroborating sources, plausible mechanism, consistent with base rates. Some gaps or unresolved minor contradictions remain.
- Language: "The evidence strongly suggests..." / "It is highly likely that..."
- Probability range: Roughly 70-95% confidence

**Level 3: Plausible**
- Definition: Supported by moderate evidence. A reasonable conclusion but alternatives remain viable.
- Evidence standard: Some corroboration, a plausible mechanism, but significant gaps or contradictions exist. Alternative explanations have not been fully ruled out.
- Language: "The evidence indicates..." / "It appears likely that..." / "The balance of evidence suggests..."
- Probability range: Roughly 40-70% confidence

**Level 4: Speculative**
- Definition: Based on limited evidence, inference, or extrapolation. Could be right but could easily be wrong.
- Evidence standard: Thin evidence base, untested mechanism, reliance on analogy or extrapolation. Presented as a hypothesis rather than a conclusion.
- Language: "It is possible that..." / "One hypothesis is..." / "Preliminary evidence suggests..."
- Probability range: Roughly 10-40% confidence

**Level 5: Unknown**
- Definition: Insufficient evidence to form any conclusion. The honest answer is "we do not know."
- Evidence standard: No reliable data, no applicable base rates, no testable mechanism. The domain may be inherently unpredictable.
- Language: "The evidence is insufficient to determine..." / "This remains an open question..." / "We do not currently know..."
- Caution: Declaring "unknown" is a valid and often courageous research conclusion. Do not fabricate a position where none is warranted.

### Step 2: Be Explicit About Uncertainty
For each conclusion, document:
- Which epistemic level it occupies and why
- What specific evidence supports the classification
- What evidence gaps prevent a higher confidence classification
- What new evidence would move it up or down the scale

### Step 3: Avoid False Precision
Common violations to watch for:
- Stating a percentage ("73% likely") when the underlying data does not support that granularity. Use ranges instead.
- Using hedging language ("might," "could") without specifying an epistemic level — hedging is not the same as calibrated uncertainty.
- Presenting model outputs as facts — models encode assumptions that create uncertainty.
- Rounding up certainty because the audience wants definitive answers.

### Step 4: Document Confidence Ranges
For Probable and Plausible conclusions, provide:
- A confidence range rather than a point estimate
- The key assumptions the range depends on
- Sensitivity: which assumptions, if wrong, would most change the range

### Step 5: Map Known Unknowns and Unknown Unknowns
**Known Unknowns:** Questions we know we cannot currently answer.
- List them explicitly
- Explain why they are unanswerable with current evidence
- Describe what research would be needed to answer them

**Unknown Unknowns:** Factors we may not even be aware of.
- Acknowledge their existence as a category
- Use historical analogies from the domain to estimate their potential impact
- Design monitoring triggers for surprises

### Step 6: Communicate Calibration to Stakeholders
Present conclusions with their uncertainty classification front and center:
- Lead with the epistemic level, not the conclusion
- Use consistent language matched to the level (see Step 1)
- Provide a summary uncertainty profile for the overall deliverable

## Outputs
- Every conclusion tagged with an epistemic level (Certain through Unknown)
- Confidence ranges for Probable and Plausible conclusions
- Explicit list of known unknowns with research recommendations
- Acknowledgment of unknown unknowns with monitoring triggers
- Uncertainty profile summarizing the overall confidence distribution of the deliverable

## Common Pitfalls
- Inflating confidence to appear authoritative — false certainty is worse than honest uncertainty
- Deflating confidence to avoid accountability — everything is uncertain, but some things are more certain than others
- Using epistemic levels inconsistently across a single deliverable
- Treating uncertainty as a weakness rather than as valuable information for decision-makers
- Neglecting to revisit classifications as new evidence arrives
- Providing precise numbers without error bars — all estimates should have ranges
- Confusing "I do not know" with "no one can know" — the former is honest, the latter is often premature

## Related Frameworks
- bayesian-updating.md (updating epistemic levels when new evidence arrives)
- research-stack.md (epistemic classification is the final step in the Decision layer)
- ralphloop-deepresearch.md (R13-R14 explicitly separate certainties from probabilities)
- signal-vs-noise-framework.md (signal strength feeds into epistemic classification)
- pre-mortem-research.md (residual risks map to the lower epistemic levels)

## Templates (recommended)

### Conclusion Confidence Card
```
Conclusion: [statement]
Epistemic Level: [Certain / Probable / Plausible / Speculative / Unknown]
Confidence Range: [if applicable, e.g., 60-75%]
Supporting Evidence: [key references]
Evidence Gaps: [what is missing]
Key Assumptions: [what must be true for this conclusion to hold]
Upgrade Trigger: [what evidence would increase confidence]
Downgrade Trigger: [what evidence would decrease confidence]
```

### Deliverable Uncertainty Profile
```
Total Conclusions: [count]
Certain: [count and percentage]
Probable: [count and percentage]
Plausible: [count and percentage]
Speculative: [count and percentage]
Unknown: [count and percentage]

Overall Assessment: [summary statement about the deliverable's confidence level]
Highest-Risk Conclusions: [which conclusions are most sensitive to new evidence]
Recommended Follow-Up: [what research would most improve overall confidence]
```
