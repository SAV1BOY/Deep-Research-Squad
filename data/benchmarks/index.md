# Benchmarks Data Index

## Purpose
Central index for benchmark data used in comparative evaluations.
Includes industry benchmarks, competitor performance baselines,
and internal capability baselines.

## Directory Structure
```
benchmarks/
  industry/        - Published industry standard benchmarks
  competitor/      - Competitor performance benchmarks
  internal/        - Own organization baseline measurements
  technology/      - Technology-specific performance benchmarks
  methodology/     - Research methodology effectiveness benchmarks
```

## Naming Convention
Files follow: `{category}_{domain}_{benchmark-name}_{date}.{ext}`

## Benchmark Lifecycle
1. **Collection**: Gather benchmark data from verified sources
2. **Validation**: Cross-reference with independent measurements
3. **Normalization**: Adjust for comparability (size, geography)
4. **Application**: Use in evaluations and comparisons
5. **Refresh**: Update when new data becomes available

## Cross-References
- Evaluation projects: see `projects/technical-evaluation-project/`
- Competitor data: see `projects/competitor-war-room-project/`
- Metrics: see `data/metrics/index.md`
- Scorecards: see `data/scorecards/index.md`

## Quality Standards
- Every benchmark must cite its source with access date
- Normalization methodology must be documented
- Benchmark age must be tracked; flag data older than 12 months
- Context and limitations must accompany every benchmark
