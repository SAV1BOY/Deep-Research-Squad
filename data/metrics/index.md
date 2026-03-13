# Metrics Data Index

## Purpose
Central index for quantitative metrics collected and computed across
research projects. Includes market metrics, performance benchmarks,
and research quality indicators.

## Directory Structure
```
metrics/
  market/          - Market size, growth, share metrics
  performance/     - Product and technology performance data
  financial/       - Financial metrics and ratios
  research-quality/ - Meta-metrics on research effectiveness
  custom/          - Project-specific custom metrics
```

## Naming Convention
Files follow the pattern: `{domain}_{metric-type}_{date}.{ext}`

## Supported Formats
- YAML for structured metric definitions
- CSV for time-series data
- JSON for complex nested metrics

## Data Freshness
- Market metrics: refresh quarterly or when source updates
- Performance metrics: refresh per evaluation cycle
- Research quality: compute after each project completion

## Cross-References
- Benchmarks: see `data/benchmarks/index.md`
- Scorecards: see `data/scorecards/index.md`
- Source data: see `data/registries/source-registry.yaml`

## Quality Standards
- All metrics must have defined units and measurement methodology
- Time-series data must include collection timestamps
- Derived metrics must document their calculation formula
- Confidence intervals should accompany estimates
