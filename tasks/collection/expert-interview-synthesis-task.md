# Expert Interview Synthesis Task

## Purpose
Synthesize findings from expert interviews into structured insights, extracting key claims, areas of consensus, points of disagreement, and novel perspectives that inform the broader research effort.

## When to Use
- After completing one or more expert interviews or consultations
- When expert opinion is a primary source category in the research plan
- When reconciling practitioner knowledge with published literature
- When the research topic lacks sufficient written sources

## Agents Involved
- **Lead**: Domain Analyst
- **Supporting**: Synthesis Architect, Evidence Validator
- **Consulted**: Deep Researcher, Contrarian Reviewer

## Inputs
- Interview transcripts, notes, or structured summaries
- Interview guide or question framework used
- Expert profiles (background, affiliation, potential biases)
- Existing research findings to cross-reference
- Source strategy criteria for weighting expert input

## Steps
1. Organize interview materials by expert and tag each with their domain and affiliation
2. Extract discrete claims, predictions, and recommendations from each interview
3. Categorize extracted items by theme aligned to the question tree
4. Identify areas of consensus across multiple experts
5. Flag points of disagreement and document the reasoning behind each position
6. Assess each expert's potential biases based on affiliation and incentives
7. Cross-reference expert claims against published sources and collected data
8. Highlight novel insights not found in other source categories
9. Rate confidence level for each synthesized finding based on corroboration
10. Compile the synthesis into a structured findings document

## Quality Gates
- Every expert's input is represented in the synthesis, not just the most vocal
- Areas of disagreement are documented with both sides, not flattened
- Bias assessment is performed for each expert source
- Claims are cross-referenced, not accepted at face value
- Novel insights are clearly flagged for further investigation
- Confidence ratings reflect the degree of independent corroboration

## Outputs
- Expert interview synthesis report organized by theme
- Consensus and disagreement map
- Expert bias assessment summary
- Cross-reference log (expert claims vs. published sources)
- Novel insights list for further research
- Confidence-rated findings table

## Estimated Effort
- **1-3 interviews**: 1-2 hours
- **4-8 interviews**: 3-5 hours
- **9+ interviews**: 5-8 hours

## Dependencies
- Requires completed interviews or consultation notes
- Feeds into `build-synthesis-report.md` and `build-evidence-table.md`
- Outputs inform `run-contrarian-pass.md` for challenge testing
