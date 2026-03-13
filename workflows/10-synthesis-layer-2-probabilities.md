# Workflow 10: Synthesis Layer 2 - Probabilities

## Purpose
Synthesize probable findings that do not meet the certainty threshold but are supported by reasonable evidence. Assign calibrated probability estimates to each finding, document the reasoning behind each estimate, and clearly distinguish what is probable from what is certain or speculative.

## Trigger
- Layer 1 certainties are finalized from Workflow 09.
- Demoted claims from Layer 1 arrive for probability assessment.
- Evidence that did not meet certainty thresholds needs synthesis.

## Agents Involved
- **Research Lead**: Reviews probability assignments and reasoning.
- **Synthesis Writer**: Drafts probability layer narrative with calibrated language.
- **Evidence Analyst**: Provides evidence backing and identifies reasoning gaps.
- **Contradiction Analyst**: Provides context on unresolved tensions affecting probabilities.

## Inputs
- Graded evidence registry from Workflow 05.
- Contradiction map (including unresolved contradictions) from Workflow 06.
- Demoted claims list from Workflow 09.
- Benchmark summary from Workflow 08.
- Master timeline from Workflow 07.

## Steps

1. **Define probability tiers**: Establish calibrated probability bands for this research:
   - **High probability (75-89%)**: Strong but not conclusive evidence. Minor gaps or caveats.
   - **Moderate probability (50-74%)**: Reasonable evidence but notable uncertainties or partial contradictions.
   - **Low probability (25-49%)**: Limited evidence, significant contradictions, or extrapolation required.
   - **Speculative (<25%)**: Minimal direct evidence. Included only for completeness. Clearly labeled.

2. **Gather probability candidates**: Collect all findings not in Layer 1:
   - Claims demoted from Layer 1 for insufficient corroboration.
   - Claims based on Grade C evidence.
   - Claims with partially resolved contradictions.
   - Inferences drawn from combining multiple pieces of indirect evidence.
   - Extrapolations from trends or patterns in the timeline.

3. **Assess each candidate**: For every probability candidate, evaluate:
   - **Evidence strength**: What grade evidence supports it? How many sources?
   - **Contradiction status**: Are there unresolved contradictions? How severe?
   - **Logical coherence**: Does it fit with the certainties from Layer 1?
   - **Base rate alignment**: Is it consistent with relevant base rates from benchmarking?
   - **Expert consensus**: Do domain experts agree or disagree?

4. **Assign probability estimates**: For each candidate, assign a probability tier with a specific point estimate:
   - Use the assessment factors to calibrate.
   - Apply the "equivalent bet" test: "Would I bet at these odds?"
   - Document the three strongest reasons for the estimate.
   - Document the single strongest reason the estimate could be wrong.

5. **Identify key uncertainties**: For each probability finding, list the specific uncertainties:
   - What information, if available, would move this to certainty?
   - What information, if discovered, would drop this to speculative?
   - What is the most likely direction of error (overestimated or underestimated)?
   - This makes the probability actionable rather than just a number.

6. **Check for reasoning traps**: Screen each probability for common reasoning errors:
   - **Anchoring**: Is the estimate influenced by an arbitrary starting point?
   - **Availability bias**: Are vivid examples over-weighted?
   - **Conjunction fallacy**: Is a complex scenario rated as more likely than its components?
   - **Neglect of base rates**: Is prior probability properly considered?
   - Adjust estimates where traps are detected.

7. **Build probability clusters**: Group findings by theme to identify patterns:
   - Are multiple uncertain findings all pointing in the same direction? (Increases cumulative confidence.)
   - Are uncertain findings scattered with no pattern? (Suggests genuine ambiguity.)
   - Are there two coherent but opposing clusters? (Suggests a genuine dilemma.)

8. **Write probability statements**: Draft each finding with calibrated language:
   - "There is approximately a 70% likelihood that..." (not "it is likely that...").
   - Include the point estimate, the tier, and a one-line rationale.
   - State the key uncertainty that could change the estimate.
   - Use consistent hedging language mapped to probability tiers.

9. **Compile Layer 2 synthesis document**: Assemble the probability layer:
   - Summary of all probable findings organized by subquestion.
   - Probability assignments with reasoning chains.
   - Key uncertainties and their potential impact.
   - Probability clusters and their implications.
   - Visual: probability heat map across the question tree.

10. **Research Lead review**: Review the Layer 2 document for:
    - Calibration consistency (similar evidence should produce similar probabilities).
    - Completeness (all non-certain evidence is accounted for).
    - Clarity (a reader can understand why each probability was assigned).
    - Approve, adjust, or request re-assessment.

## Quality Gates
- Every probability must have a specific point estimate and tier assignment.
- Every probability must document at least three supporting reasons and one risk factor.
- Reasoning trap screening must be performed for all high-probability findings.
- Probability statements must use calibrated language matching their tier.
- No finding may be left unclassified between Layer 1 and Layer 2.
- Research Lead must approve all probability assignments.

## Outputs
- Layer 2 Synthesis Document (probable findings with calibrated estimates).
- Key uncertainty register (what would change each probability).
- Probability heat map across the question tree.
- Probability cluster analysis.
- Combined Layer 1 + Layer 2 evidence map.

## Next Workflow
- **11-model-building.md** (use certainties and probabilities to build models).
- **12-decision-translation.md** (translate findings into decision format).
