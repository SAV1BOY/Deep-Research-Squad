# Bias Audit Task

## Purpose
Systematically audit the research process and findings for cognitive, methodological, and source biases that could distort conclusions or reduce the reliability of the deliverable.

## When to Use
- As a standard quality gate before finalizing research conclusions
- When the research topic is politically sensitive or commercially contested
- When the source pool is dominated by a single perspective or stakeholder group
- When initial findings strongly confirm pre-existing expectations
- When the Contrarian Analyst flags potential bias concerns

## Agents Involved
- **Lead**: Contrarian Analyst
- **Supporting**: Evidence Verifier, Source Hunter
- **Consulted**: DeepResearch Chief, Domain Specialist

## Inputs
- Draft research findings and conclusions
- Source inventory with provenance and affiliation metadata
- Search queries and methodology documentation
- Question tree and scope boundaries
- Prior assumptions or hypotheses stated at project outset

## Steps
1. Review the source pool for representation bias (geographic, temporal, ideological, industry)
2. Check for confirmation bias by examining whether disconfirming evidence was actively sought
3. Assess anchoring bias by reviewing whether early findings disproportionately shaped conclusions
4. Evaluate availability bias by checking if easily accessible sources dominated the analysis
5. Examine survivorship bias in datasets (are failures and negatives represented, not just successes?)
6. Audit the search methodology for selection bias in query design and filtering
7. Check for authority bias by verifying that high-profile sources received appropriate scrutiny
8. Review framing effects in how questions were posed and findings were presented
9. Document each identified bias with its potential impact on conclusions
10. Recommend specific corrections, caveats, or additional research to address identified biases

## Quality Gates
- At least six distinct bias categories are evaluated, not just one or two
- Each bias assessment references specific evidence from the research process
- Identified biases include an impact rating (minimal, moderate, significant)
- Recommendations are actionable and proportionate to the bias impact
- The audit covers both source-level and process-level biases
- Findings are documented regardless of whether bias is found (absence is also recorded)

## Outputs
- Bias audit report organized by bias category
- Source diversity assessment with gap identification
- Impact analysis for each identified bias
- Recommended corrections or caveats for affected findings
- Process improvement suggestions for future research
- Updated confidence ratings reflecting bias assessment

## Estimated Effort
- **Narrow scope, few sources**: 1-2 hours
- **Moderate scope**: 2-4 hours
- **Broad scope, sensitive topic**: 4-6 hours

## Dependencies
- Requires draft findings from `build-synthesis-report.md`
- Should follow or run parallel to `run-contrarian-pass.md`
- Outputs feed into `audit-research-quality.md` and `review-source-diversity.md`
