# Workflow 04: Collection Sprint

## Purpose
Execute a parallel collection sprint where Literature, OSINT, and Data teams collect evidence simultaneously across all assigned subquestions. Maximize coverage and speed by running collection in parallel while maintaining coordination to avoid duplication and ensure completeness.

## Trigger
- Approved source routing table arrives from Workflow 03.
- A targeted re-collection is requested after filtering reveals evidence gaps.

## Agents Involved
- **Research Lead**: Monitors sprint progress and resolves blockers.
- **Literature Analyst**: Collects from academic and published sources.
- **OSINT Collector**: Collects from open-source intelligence channels.
- **Data Analyst**: Collects structured data from databases and APIs.
- **Sprint Coordinator**: Tracks progress, deduplicates in real-time, manages time budgets.

## Inputs
- Source routing table with queries, tools, and quotas per subquestion.
- Agent assignments from Workflow 03.
- Time budget per subquestion.
- Evidence collection template (standardized format for captured evidence).

## Steps

1. **Sprint kickoff**: Sprint Coordinator briefs all collecting agents on their assignments, time budgets, and quality expectations. Confirm all agents have access to their designated tools. Set sprint clock.

2. **Parallel collection launch**: All three collection teams begin simultaneously:
   - **Literature track**: Execute academic queries, retrieve papers, extract key findings, capture metadata (authors, date, journal, citation count).
   - **OSINT track**: Execute open-source queries, capture web content, archive snapshots, record source URLs and access timestamps.
   - **Data track**: Execute data queries, download datasets, capture summary statistics, record data provenance and methodology.

3. **Real-time progress tracking**: Sprint Coordinator maintains a live dashboard:
   - Sources found per subquestion vs. quota.
   - Time elapsed vs. budget per subquestion.
   - Emerging patterns or surprises flagged by collectors.
   - Blockers or tool failures reported.

4. **Mid-sprint check-in**: At 50% of time budget, Sprint Coordinator reviews progress:
   - Are any subquestions falling behind on collection quotas?
   - Are any subquestions over-collecting (diminishing returns)?
   - Reallocate time and resources across subquestions as needed.
   - Redirect agents from over-served areas to under-served areas.

5. **Evidence capture protocol**: Each piece of evidence must be captured in standard format:
   - **Source identifier**: URL, DOI, database ID, or reference.
   - **Source class**: Which category (academic, news, data, etc.).
   - **Extraction date**: When it was collected.
   - **Key claim or data point**: The specific finding extracted.
   - **Relevance tag**: Which subquestion(s) it addresses.
   - **Collector notes**: Initial assessment of quality and relevance.

6. **Deduplication during collection**: Sprint Coordinator runs continuous dedup:
   - Flag when multiple collectors find the same source.
   - Merge duplicate entries and credit the first collector.
   - Redirect duplicate effort to uncovered ground.

7. **Surprise and anomaly flagging**: Collectors flag any unexpected findings:
   - Evidence that contradicts the working hypothesis.
   - Data points that are statistical outliers.
   - Sources that reference unknown but potentially important topics.
   - These flags feed directly into Workflow 06 (Contradiction Hunt).

8. **Source chain documentation**: For each critical source, document how it was found:
   - Which query produced it.
   - Which tool was used.
   - What filters were applied.
   - This enables reproducibility and audit.

9. **Sprint close-out**: When time budget expires or quotas are met:
   - Each collector submits their evidence collection.
   - Sprint Coordinator compiles a unified evidence inventory.
   - Count total sources per subquestion and source class.
   - Identify any subquestions that did not meet minimum collection quotas.

10. **Gap assessment**: For under-collected subquestions, decide:
    - Extend collection time (if schedule allows).
    - Accept lower evidence density (if confidence threshold still achievable).
    - Escalate to source strategy revision (return to Workflow 03).

## Quality Gates
- Every subquestion must meet its minimum collection quota or have a documented exception.
- Every piece of evidence must be captured in the standard format with all fields populated.
- Source chain documentation must exist for all critical sources.
- Deduplication must be completed before evidence inventory is finalized.
- Sprint must complete within the allocated time budget (with approved extensions only).
- At least 3 source classes must be represented in the overall collection.

## Outputs
- Unified evidence inventory (all collected evidence in standard format).
- Collection statistics (sources per subquestion, per source class, per agent).
- Anomaly and surprise flag list.
- Gap report for under-collected subquestions.
- Source chain documentation for reproducibility.

## Next Workflow
- **05-evidence-filtering-and-grading.md** (filter and grade the collected evidence).
- **03-source-strategy-and-routing.md** (if gap assessment requires strategy revision).
