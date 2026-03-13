# Script: Create Source Map

## Purpose

Creates a structured map of all sources relevant to a research question.
Organizes sources by type, reliability, and relevance to enable systematic
evidence gathering and identify coverage gaps.

## Trigger

Called after a research brief is created and before deep research begins.

## Inputs

- `research_brief`: The structured research brief
- `existing_sources`: Any sources already identified
- `source_registries`: References to swipe-sources/ registry files

## Process

### Step 1: Identify Source Categories
For the research question, determine which source types are relevant:
- [ ] Academic/peer-reviewed
- [ ] Government/regulatory
- [ ] Industry reports (consulting firms)
- [ ] Company filings and documents
- [ ] Journalism and media
- [ ] Expert commentary and analysis
- [ ] Data repositories and databases
- [ ] Grey literature (working papers, pre-prints, reports)

### Step 2: Source Search per Category
For each relevant category:
1. Query the swipe-sources/ registry for relevant databases
2. Identify specific sources to search
3. Record search terms used
4. Log results: found, relevance rating, quality assessment

### Step 3: Source Quality Assessment

| Source | Type | Reliability | Relevance | Recency | Bias Risk | Access |
|--------|------|------------|-----------|---------|-----------|--------|
| [Name] | [Cat] | 1-5 | 1-5 | Date | Low/Med/High | Open/Gated |

### Step 4: Coverage Analysis
- Which sub-questions have adequate source coverage?
- Which sub-questions have gaps?
- What source types are missing?
- Is the source diversity sufficient?

### Step 5: Source Diversity Score
Calculate diversity across:
- Geographic diversity: sources from multiple regions
- Type diversity: academic, industry, government, media mix
- Perspective diversity: multiple viewpoints represented
- Temporal diversity: historical and current sources

## Output: Source Map

```
SOURCE MAP
==========
Research Question: [From brief]
Sources Identified: [Count]
Diversity Score: [0-100]

Source List:
[Table from Step 3]

Coverage Assessment:
- Sub-Q 1: [Adequate/Gap] — [Notes]
- Sub-Q 2: [Adequate/Gap] — [Notes]

Gaps Identified:
- [Gap description] — [Mitigation strategy]

Recommended Additional Searches:
- [Specific search to fill gaps]
```

## Quality Checks

- [ ] Minimum 3 sources per sub-question
- [ ] At least 2 source types per sub-question
- [ ] Diversity score above 60
- [ ] All gaps documented with mitigation plans
- [ ] No over-reliance on single source type
