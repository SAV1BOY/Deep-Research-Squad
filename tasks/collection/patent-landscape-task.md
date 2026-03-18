# Patent Landscape Analysis Task

## Purpose
Analyze the patent landscape for a given technology or domain, mapping key players, innovation trends, white spaces, and potential freedom-to-operate considerations relevant to the research topic.

## When to Use
- When researching technology trends or competitive positioning
- When evaluating innovation activity in a specific domain
- When assessing freedom to operate for a product or technology strategy
- When identifying potential partners, acquirers, or competitors by IP portfolio

## Agents Involved
- **Lead**: Data Researcher
- **Supporting**: Domain Specialist, Data Researcher
- **Consulted**: Contrarian Analyst, Timeline Analyst

## Inputs
- Technology domain or specific technical area to analyze
- Key terms, classification codes, or seed patents
- List of known players or companies of interest
- Geographic scope for patent filings
- Time window for the analysis (e.g., last 5 years, last 10 years)

## Steps
1. Define the patent search scope using keywords, classification codes, and assignee filters
2. Execute searches across patent databases to build the initial corpus
3. Deduplicate and clean the patent set, removing irrelevant filings
4. Categorize patents by technology sub-domain, application area, and claim type
5. Map filing trends over time to identify acceleration or decline in activity
6. Identify top assignees and analyze their portfolio focus and filing velocity
7. Detect emerging technology clusters and white-space opportunities
8. Analyze citation networks to find foundational and influential patents
9. Assess geographic filing patterns for market intent signals
10. Compile the landscape into a structured analysis with visualizable data

## Quality Gates
- Search strategy is broad enough to capture relevant filings, not just exact matches
- Patent families are properly grouped to avoid double-counting
- Analysis distinguishes between granted patents and pending applications
- Top assignees are verified against current corporate structures (mergers, acquisitions)
- White-space identification is based on gap analysis, not just absence of filings
- Citation analysis captures both forward and backward citation patterns

## Outputs
- Patent landscape overview with filing trends and key statistics
- Top assignee ranking with portfolio characterization
- Technology cluster map with sub-domain categorization
- White-space analysis identifying underexplored areas
- Citation network summary highlighting foundational patents
- Geographic filing pattern analysis
- Raw dataset for further analysis or visualization

## Estimated Effort
- **Narrow domain, few players**: 2-3 hours
- **Moderate domain breadth**: 4-6 hours
- **Broad technology area, global scope**: 8-12 hours

## Dependencies
- Requires defined technology scope from the research plan
- Feeds into `run-competitor-research.md` and `run-trend-analysis.md`
- Outputs inform `build-decision-brief.md` for strategic recommendations
