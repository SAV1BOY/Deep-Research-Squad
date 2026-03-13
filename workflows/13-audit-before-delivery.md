# Workflow 13: Audit Before Delivery

## Purpose
Perform a final comprehensive audit of the entire research output before delivery. Check methodology soundness, identify unexamined biases, verify completeness against the original scope, ensure reproducibility of findings, and assign an overall quality score. This is the last gate before the research reaches the requester.

## Trigger
- Decision brief is complete from Workflow 12.
- All synthesis and model documents are finalized.
- Research Lead signals readiness for final audit.

## Agents Involved
- **Quality Auditor**: Leads the audit and owns the quality score.
- **Research Lead**: Co-reviews and approves the final output.
- **Methodology Reviewer**: Evaluates research process integrity.
- **Evidence Analyst**: Verifies evidence chain completeness.

## Inputs
- All research outputs: intake card, research plan, question tree, source strategy, evidence registry, contradiction map, timeline, benchmarks, Layer 1 synthesis, Layer 2 synthesis, models, decision brief.
- Original research request from Workflow 00.
- Quality targets from Workflow 01.

## Steps

1. **Scope completeness check**: Compare the final output against the original scope:
   - Every in-scope item from the research plan must be addressed.
   - Every subquestion in the question tree must have findings (certain, probable, or acknowledged as unanswerable).
   - No out-of-scope items should have crept in without documented justification.
   - Score: Complete / Mostly Complete / Gaps Identified.

2. **Methodology audit**: Review the research process for soundness:
   - Was the source strategy adequate? Were sufficient source classes used?
   - Was the evidence grading applied consistently?
   - Were contradictions properly identified and addressed?
   - Were benchmarks appropriate and fairly applied?
   - Were probability estimates calibrated using proper methods?
   - Score: Sound / Minor Issues / Major Issues.

3. **Evidence chain verification**: For every key claim in the final output:
   - Trace it back to its source evidence.
   - Verify the evidence grade is accurately reported.
   - Verify the source exists and says what is attributed to it.
   - Check for broken chains (claims that cannot be traced to evidence).
   - Spot-check at least 30% of all claims. Score: Verified / Partially Verified / Failures Found.

4. **Bias audit**: Examine the full research for systematic biases:
   - **Confirmation bias**: Did the research team favor evidence supporting initial hypotheses?
   - **Source bias**: Is the evidence dominated by sources with a particular perspective?
   - **Framing bias**: Is the narrative framed in a way that favors certain conclusions?
   - **Omission bias**: Are there obvious viewpoints or evidence types that were excluded?
   - **Anchoring bias**: Were early findings given disproportionate weight?
   - Document each bias checked and whether it was detected.

5. **Contradiction resolution audit**: Review the contradiction map:
   - Were all critical contradictions resolved or escalated?
   - Are resolution rationales sound and well-documented?
   - Were any contradictions swept under the rug?
   - Score: Fully Addressed / Partially Addressed / Unaddressed Issues.

6. **Confidence calibration check**: Review all confidence and probability claims:
   - Are certainties truly certain (meeting the defined threshold)?
   - Are probabilities calibrated (not systematically over- or under-confident)?
   - Does the language match the confidence level (no certain language for probable claims)?
   - Compare confidence levels against evidence strength for consistency.

7. **Reproducibility assessment**: Evaluate whether the research could be reproduced:
   - Are all sources cited with sufficient detail to find them again?
   - Are search queries and tool selections documented?
   - Are analytical methods described clearly enough to replicate?
   - Is the reasoning chain transparent (could another analyst follow it)?
   - Score: Reproducible / Mostly Reproducible / Not Reproducible.

8. **Compute overall quality score**: Calculate a composite quality score across all audit dimensions:
   - Scope completeness (0-20 points).
   - Methodology soundness (0-20 points).
   - Evidence chain integrity (0-20 points).
   - Bias management (0-20 points).
   - Reproducibility (0-20 points).
   - Total: 0-100 points.
   - Minimum passing score: 70. Below 70 requires rework.

9. **Write audit report**: Compile the full audit findings:
   - Score for each dimension with brief justification.
   - Overall quality score.
   - List of issues found (critical, major, minor).
   - Required fixes before delivery (for any issues rated critical or major).
   - Suggested improvements (for minor issues, optional to fix).

10. **Decision on delivery readiness**: Based on the audit:
    - **Pass (score >= 80)**: Approved for delivery. Minor suggestions noted.
    - **Conditional pass (score 70-79)**: Approved with required fixes. Re-audit the fixed items.
    - **Fail (score < 70)**: Not approved. Return to the appropriate workflow for rework. Specify which workflows need revisiting.

## Quality Gates
- All five audit dimensions must be scored.
- Evidence chain spot-check must cover at least 30% of key claims.
- Bias audit must check for all five specified bias types.
- Overall quality score must be calculated using the defined formula.
- Any score below 70 must trigger rework with specific workflow assignments.
- Audit report must be completed and attached to the research output.

## Outputs
- Audit report with dimension scores, issues, and required fixes.
- Overall quality score (0-100).
- Delivery decision (pass, conditional pass, or fail).
- Required fix list (if conditional pass or fail).
- Audit trail for the research record.

## Next Workflow
- **14-executive-compression.md** (if audit passes, compress for delivery).
- **Rework loop**: Return to the specific workflow(s) identified for fixes.
- **15-registry-and-memory-update.md** (log audit results regardless of outcome).
