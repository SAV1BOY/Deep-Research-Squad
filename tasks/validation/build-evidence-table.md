# Build Evidence Table

## Purpose
Construct a structured evidence table that maps every claim in the research to its supporting sources, evidence quality, and confidence level, creating a traceable foundation for all conclusions.

## When to Use
- After collection phases are complete and findings are ready for validation
- When preparing research for synthesis to ensure all claims are grounded
- When stakeholders question the evidence basis for specific findings
- As a standard quality step before any research delivery

## Agents Involved
- **Lead**: Evidence Verifier
- **Executing**: Data Researcher, Domain Specialist
- **Supporting**: Source Hunter
- **Reviewed by**: Contrarian Analyst

## Inputs
- All collected findings organized by research branch
- Source registry with quality assessments
- Claim statements extracted from research findings
- Evidence quality criteria and confidence thresholds

## Steps
1. Extract all explicit and implicit claims from the research findings
2. Categorize claims by type (factual, analytical, predictive, evaluative)
3. For each claim, identify all supporting sources from the evidence base
4. For each claim, identify any contradicting sources
5. Assess the quality of evidence for each claim (direct, indirect, circumstantial)
6. Rate source independence (are supporting sources truly independent?)
7. Assign an initial confidence level to each claim based on evidence strength
8. Flag claims with insufficient evidence or single-source dependency
9. Flag claims where contradicting evidence exists
10. Identify orphan claims (conclusions not traceable to any source)
11. Compile the evidence table with all mappings, ratings, and flags
12. Generate a summary of evidence strength distribution across the research

## Quality Gates
- Every claim in the research is represented in the evidence table
- Each claim has at least one source mapping (or is flagged as unsupported)
- Evidence quality ratings use a consistent, defined scale
- Source independence is assessed, not assumed
- Contradicting evidence is documented alongside supporting evidence
- Confidence levels are calibrated to evidence strength, not researcher conviction

## Outputs
- Complete evidence table (claim, sources, quality, confidence, flags)
- Evidence strength distribution summary
- Unsupported claims list requiring additional evidence
- Single-source dependency warnings
- Contradiction flags for further investigation
- Evidence quality summary statistics

## Estimated Effort
- **Small research (10-20 claims)**: 1-2 hours
- **Medium research (20-50 claims)**: 2-4 hours
- **Large research (50+ claims)**: 4-8 hours
