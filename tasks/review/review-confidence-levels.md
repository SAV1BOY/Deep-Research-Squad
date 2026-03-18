# Review Confidence Levels

## Purpose
Critically review the confidence levels assigned to research findings to ensure they are well-calibrated, internally consistent, and honestly reflect the strength of supporting evidence.

## When to Use
- After the confidence map is built and before final delivery
- When confidence assessments seem misaligned with evidence strength
- As part of the overall quality audit process
- When stakeholders question the reliability claims in the research
- For calibration exercises to improve future confidence assignments

## Agents Involved
- **Lead**: Contrarian Analyst
- **Executing**: Evidence Verifier
- **Supporting**: DeepResearch Chief, Domain Specialist
- **Consulted**: Agents who assigned original confidence levels

## Inputs
- Confidence map with all assigned levels
- Evidence table with source mappings and quality scores
- Contradiction map and resolution statuses
- Source audit and diversity review results
- Contrarian pass vulnerability ratings
- Historical calibration data (if available)

## Steps
1. Review the confidence scale definition for clarity and consistency
2. For each high-confidence finding, verify that evidence strength justifies the level
3. For each low-confidence finding, verify that the level is not overly conservative
4. Check that dependent findings reflect upstream uncertainty appropriately
5. Compare confidence levels across similar evidence strengths for consistency
6. Identify cases where confidence may be inflated by confirmation bias
7. Verify that contradictions appropriately reduce confidence levels
8. Check that single-source findings have appropriately lowered confidence
9. Assess whether domain-specific uncertainty factors are reflected
10. Compare confidence distribution against calibration benchmarks
11. Recommend adjustments where confidence levels appear miscalibrated
12. Document the review findings and any adjusted confidence levels

## Quality Gates
- Every confidence level above the median is individually verified
- Internal consistency is checked across all findings
- Upstream uncertainty propagation is validated
- Contradiction impact on confidence is verified
- No finding has confidence higher than its weakest evidence link
- Review is conducted by someone other than the original confidence assigner

## Outputs
- Confidence level review report
- Adjustment recommendations with rationale
- Calibration consistency analysis
- Over-confidence and under-confidence flags
- Dependency chain validation results
- Updated confidence map (if adjustments are accepted)

## Estimated Effort
- **Small research (10-15 findings)**: 30-60 minutes
- **Medium research (15-30 findings)**: 1-3 hours
- **Large research (30+ findings)**: 3-5 hours
