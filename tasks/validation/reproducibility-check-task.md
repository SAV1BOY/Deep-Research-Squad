# Reproducibility Check Task

## Purpose
Verify that key research findings can be independently reproduced by re-executing searches, recalculating analyses, and confirming that the same inputs yield consistent results.

## When to Use
- Before delivering high-stakes research conclusions
- When findings rely on specific data queries or calculations
- When a claim seems surprising or counterintuitive
- As part of the final quality assurance pass before delivery
- When updating previously delivered research with new data

## Agents Involved
- **Lead**: Evidence Verifier
- **Supporting**: Data Researcher, Data Researcher
- **Reviewed by**: Contrarian Analyst, DeepResearch Chief

## Inputs
- Finalized research findings with documented methodology
- Original search queries, data sources, and parameters used
- Calculations, models, or analytical steps applied to raw data
- Source materials referenced in the findings
- Confidence ratings from prior validation steps

## Steps
1. Select findings for reproducibility testing, prioritizing high-impact conclusions
2. Document the original methodology for each finding in reproducible detail
3. Re-execute original search queries and compare result sets for consistency
4. Verify that cited sources still contain the referenced information
5. Recalculate any quantitative analyses from raw inputs independently
6. Check that analytical steps produce the same intermediate and final results
7. Test whether reasonable methodology variations yield materially different conclusions
8. Document any discrepancies found and assess their impact on findings
9. Classify each tested finding as reproducible, partially reproducible, or non-reproducible
10. Recommend corrections or caveats for findings that fail reproducibility

## Quality Gates
- High-impact findings are all tested, not just a convenience sample
- Re-execution uses the documented methodology, not improvised shortcuts
- Source availability is checked (links not broken, data not retracted)
- Quantitative results match within acceptable tolerance margins
- Sensitivity to methodology variations is assessed, not just exact replication
- Non-reproducible findings are escalated with clear documentation

## Outputs
- Reproducibility test results for each selected finding
- Discrepancy log with impact assessment
- Source availability verification report
- Sensitivity analysis for methodology-dependent conclusions
- Recommended corrections or caveats for non-reproducible findings
- Updated confidence ratings reflecting reproducibility outcomes

## Estimated Effort
- **5-10 findings**: 1-3 hours
- **10-20 findings**: 3-5 hours
- **20+ findings or complex analyses**: 5-8 hours

## Dependencies
- Requires completed findings from synthesis phase
- Should follow `verify-claims.md` and `build-evidence-table.md`
- Outputs feed into `audit-research-quality.md` and `prepare-final-delivery.md`
