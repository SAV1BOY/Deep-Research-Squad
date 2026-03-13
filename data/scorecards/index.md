# Scorecards Data Index

## Purpose
Central index for evaluation scorecards used in technology evaluations,
competitor assessments, and vendor comparisons. Provides standardized
scoring templates and completed scorecard archives.

## Directory Structure
```
scorecards/
  templates/       - Blank scorecard templates by evaluation type
  completed/       - Filled scorecards organized by project
  comparative/     - Side-by-side comparison scorecards
  historical/      - Archived scorecards from past evaluations
```

## Naming Convention
Files follow: `{project-id}_{subject}_{version}_{date}.{ext}`

## Scorecard Components
- Evaluation criteria with descriptions
- Weight assignments per criterion
- Scoring rubric (scale definition and anchors)
- Raw scores and weighted composite calculations
- Assessor identification and date

## Standard Templates
- Technology evaluation scorecard (6 dimensions)
- Vendor assessment scorecard (8 dimensions)
- Competitor capability scorecard (5 dimensions)
- Source reliability scorecard (4 dimensions)
- Research quality scorecard (7 dimensions)

## Cross-References
- Evaluation projects: see `projects/technical-evaluation-project/`
- Benchmarks: see `data/benchmarks/index.md`
- Metrics: see `data/metrics/index.md`

## Quality Standards
- Weights must be approved before scoring begins
- Multiple assessors should score independently when possible
- Inter-rater reliability should be calculated and reported
- Historical scorecards must not be modified after completion
