# Script: Source Diversity Analyzer

## Purpose

Analyzes the diversity of sources used in a research deliverable. Source
diversity is a key quality indicator — research drawing from multiple
independent source types is more robust than research relying on one type.

## Trigger

Called during quality review of any research deliverable before final delivery.

## Inputs

- `source_list`: All sources used in the deliverable
- `evidence_tables`: Evidence tables with source classifications
- `research_brief`: Original brief with diversity requirements

## Process

### Step 1: Classify Sources
Categorize each source into types:

| Source | Type | Geography | Perspective | Date | Independence |
|--------|------|-----------|------------|------|-------------|
| [Name] | Academic/Industry/Gov/Media/Company | Region | Bull/Bear/Neutral | Date | Yes/No |

### Step 2: Calculate Type Diversity
Source types represented (max 8):
- [ ] Academic/peer-reviewed
- [ ] Government/regulatory
- [ ] Industry reports
- [ ] Company documents
- [ ] Journalism/media
- [ ] Expert commentary
- [ ] Data repositories
- [ ] Grey literature

Type Diversity Score = (Types used / 8) × 100

### Step 3: Calculate Geographic Diversity
Regions represented:
- [ ] North America
- [ ] Europe
- [ ] Asia-Pacific
- [ ] Latin America
- [ ] Middle East/Africa

Geographic Score = (Regions / relevant regions) × 100

### Step 4: Calculate Perspective Diversity
Viewpoints represented:
- [ ] Bullish/optimistic perspectives
- [ ] Bearish/pessimistic perspectives
- [ ] Neutral/analytical perspectives
- [ ] Contrarian viewpoints

Perspective Score = (Viewpoints / 4) × 100

### Step 5: Calculate Independence Score
Check for source independence:
- How many sources are truly independent (different organizations)?
- Are any sources citing each other (circular sourcing)?
- Are any sources from the same parent organization?

Independence Score = (Independent sources / Total sources) × 100

### Step 6: Calculate Overall Diversity Score

```
Overall = (Type × 0.30) + (Geographic × 0.20) +
          (Perspective × 0.30) + (Independence × 0.20)
```

### Diversity Thresholds

| Score | Rating | Action |
|-------|--------|--------|
| 80-100 | Excellent | Proceed with delivery |
| 60-79 | Good | Note limitations, proceed |
| 40-59 | Adequate | Flag gaps, seek additional sources if time permits |
| 20-39 | Poor | Must seek additional sources before delivery |
| 0-19 | Failing | Research is unreliable, do not deliver without improvement |

## Output Template

```
SOURCE DIVERSITY ANALYSIS
=========================
Sources Analyzed: [Count]
Overall Diversity Score: [Score] ([Rating])

Breakdown:
  Type diversity: [Score] ([Types used] of 8)
  Geographic diversity: [Score] ([Regions] of [relevant])
  Perspective diversity: [Score] ([Viewpoints] of 4)
  Independence: [Score] ([Independent] of [Total])

Gaps:
- [Missing source type or perspective]

Recommendations:
- [Specific source to add for better diversity]
```

## Quality Checks

- [ ] All sources classified accurately
- [ ] Circular sourcing detected and flagged
- [ ] Geographic relevance appropriately scoped
- [ ] Perspective diversity includes contrarian views
- [ ] Overall score meets minimum threshold for delivery
