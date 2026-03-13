# Workflow 03: Source Strategy and Routing

## Purpose
Design a comprehensive source strategy for the research plan. Select the right search tools and databases for each subquestion, classify sources by type and reliability, and route queries to the appropriate source classes so collection is efficient, diverse, and thorough.

## Trigger
- Question tree is approved from Workflow 02.
- A source gap is identified during collection, requiring strategy revision.

## Agents Involved
- **Research Lead**: Approves the source strategy.
- **Source Strategist**: Designs the strategy and routing map.
- **OSINT Collector**: Advises on open-source intelligence availability.
- **Literature Analyst**: Advises on academic and published source availability.
- **Data Analyst**: Advises on structured data and dataset availability.

## Inputs
- Approved question tree with leaf-level subquestions.
- Source registry (catalog of previously used and known sources).
- Tool inventory (available search engines, databases, APIs, scrapers).
- Domain-specific source guides (if available).

## Steps

1. **Inventory available source classes**: List all source classes available to the squad:
   - Academic literature (journals, preprints, conference papers).
   - Government and institutional reports.
   - News and media (mainstream, trade, investigative).
   - Structured datasets (public databases, APIs, data portals).
   - Expert networks and interviews.
   - OSINT (social media, forums, public records).
   - Internal knowledge base and prior research outputs.

2. **Map subquestions to source classes**: For each leaf-level subquestion, identify which source classes are most likely to contain relevant evidence. Assign a primary source class and 1-2 secondary classes. Document rationale.

3. **Select search tools per source class**: For each source class being used, select the specific tools:
   - Academic: Semantic Scholar, Google Scholar, PubMed, arXiv.
   - Government: Official portals, FOIA databases, legislative records.
   - News: News APIs, media archives, press release databases.
   - Data: Data.gov, World Bank, OECD, domain-specific APIs.
   - OSINT: Social media APIs, web scrapers, archive.org.
   - Internal: Knowledge base search, prior research index.

4. **Design query strategy**: For each subquestion and source class combination, draft:
   - Primary search query (optimized for recall).
   - Refined search query (optimized for precision).
   - Exclusion terms to filter noise.
   - Date range constraints (if temporal scope applies).
   - Language and geographic filters (if applicable).

5. **Set source diversity requirements**: Define minimum diversity for the overall research:
   - At least 3 different source classes must contribute evidence.
   - No single source class may represent more than 50% of total evidence.
   - At least 1 source must be adversarial or contrarian to prevent echo chamber.

6. **Assess source reliability**: For each source class, document known reliability characteristics:
   - Peer review status (for academic sources).
   - Editorial standards (for news sources).
   - Data provenance and methodology (for datasets).
   - Potential biases and conflicts of interest.
   - Recency and update frequency.

7. **Build routing table**: Create a structured routing table:
   | Subquestion ID | Primary Source Class | Tool | Query | Secondary Source Class | Tool | Query |
   Route each subquestion to specific agents based on their source class expertise.

8. **Identify source gaps**: For any subquestion where no good source class exists, flag it as a source gap. Determine if:
   - The gap is acceptable (lower confidence is tolerable).
   - Alternative indirect evidence can substitute.
   - Escalation to domain specialist is needed.

9. **Set collection quotas**: For each subquestion, set:
   - Maximum number of sources to collect (prevent over-collection).
   - Minimum number of sources to collect (prevent under-collection).
   - Time budget for collection (prevent rabbit holes).

10. **Review and approve**: Source Strategist presents the complete routing plan. Research Lead reviews for completeness, diversity, and efficiency. Approve or request adjustments.

## Quality Gates
- Every leaf subquestion must be mapped to at least one source class with a specific tool and query.
- Source diversity requirements must be met at the plan level.
- No subquestion may rely on a single source class alone.
- Source gaps must be explicitly flagged and addressed.
- Collection quotas must be set for every subquestion.
- Reliability assessment must be documented for each source class used.

## Outputs
- Approved source routing table.
- Query library (all search queries organized by subquestion).
- Source gap report with mitigation plans.
- Collection quotas and time budgets per subquestion.
- Agent routing assignments.

## Next Workflow
- **04-collection-sprint.md** (execute the collection plan).
- **17-domain-specialist-escalation.md** (if source gaps require specialist input).
