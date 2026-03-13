# Timelines Data Index

## Purpose
Central index for timeline data including market evolution timelines,
technology adoption curves, competitive event histories, and project
milestone tracking.

## Directory Structure
```
timelines/
  market/          - Market evolution and milestone timelines
  technology/      - Technology adoption and maturity timelines
  competitive/     - Competitor action and event timelines
  regulatory/      - Regulatory and policy change timelines
  project/         - Research project milestone timelines
```

## Naming Convention
Files follow: `{category}_{domain}_{subject}_{date-range}.{ext}`

## Timeline Data Format
Each timeline entry should include:
- Event date (exact or estimated range)
- Event description
- Source citation
- Impact assessment (significance level)
- Confidence in date accuracy

## Timeline Types
- **Historical**: Documented past events for pattern analysis
- **Current**: Ongoing events and recent developments
- **Projected**: Forecasted events with probability estimates
- **Comparative**: Multi-entity parallel timelines

## Cross-References
- Trend analysis: see `projects/trend-monitoring-project/`
- Competitor events: see `projects/competitor-war-room-project/`
- Source data: see `data/registries/source-registry.yaml`

## Quality Standards
- Historical events must have source citations
- Projected events must include probability and confidence
- Timeline granularity should match analytical needs
- Update timelines when new information changes the picture
