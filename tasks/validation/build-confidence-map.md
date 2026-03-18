# Build Confidence Map

## Purpose
Create a comprehensive confidence map that assigns calibrated confidence levels to every finding and conclusion in the research, making uncertainty explicit and enabling informed decision-making.

## When to Use
- After validation steps are complete and evidence quality is assessed
- Before synthesis to guide how findings should be presented
- When stakeholders need to understand reliability of different findings
- As a standard quality artifact for any research delivery

## Agents Involved
- **Lead**: Evidence Verifier
- **Executing**: Contrarian Analyst, Domain Specialist
- **Supporting**: DeepResearch Chief
- **Consulted**: All agents who contributed findings

## Inputs
- Evidence table with quality assessments
- Contradiction map with resolution statuses
- Source audit results
- Thesis test results (if applicable)
- Contrarian pass vulnerability ratings
- Domain-specific calibration benchmarks

## Steps
1. Define the confidence scale with clear criteria for each level (e.g., 1-5 or percentage)
2. List all findings and conclusions requiring confidence assessment
3. For each finding, assess evidence strength from the evidence table
4. Adjust confidence based on source diversity from the source audit
5. Adjust confidence based on contradictions from the contradiction map
6. Adjust confidence based on vulnerability ratings from the contrarian pass
7. Consider domain-specific uncertainty factors (fast-changing field, limited data, etc.)
8. Calibrate confidence levels for internal consistency across findings
9. Identify confidence clusters (groups of findings at similar levels)
10. Map confidence levels visually across the research structure
11. Document the rationale for each confidence assignment
12. Produce summary statistics and highlight high-confidence and low-confidence zones

## Quality Gates
- Every finding and conclusion has an assigned confidence level
- Confidence levels are calibrated to evidence, not researcher conviction
- The confidence scale is consistently applied across all findings
- Low-confidence findings have documented reasons and improvement paths
- Confidence assignments account for all validation inputs
- The map is internally consistent (dependent findings reflect upstream uncertainty)

## Outputs
- Confidence map with levels assigned to all findings and conclusions
- Confidence level rationale documentation
- Summary statistics (distribution of confidence levels)
- High-confidence finding highlights
- Low-confidence finding warnings with improvement recommendations
- Visual confidence overlay on research structure

## Estimated Effort
- **Small research (10-15 findings)**: 1-2 hours
- **Medium research (15-30 findings)**: 2-4 hours
- **Large research (30+ findings)**: 4-6 hours
