# Benchmark Comparison Utility

## Purpose

Structured method for comparing benchmarks across sources, normalizing methodology
differences to enable fair and accurate comparison.

## Inputs

- Two or more benchmark results to compare
- Source cards and test conditions for each benchmark
- Metrics measured (throughput, latency, resource usage)
- Methodology descriptions

## Scoring Criteria

### Comparability Assessment (0-25 points)
| Score | Description |
|-------|-------------|
| 19-25 | Same methodology, hardware class, and software version |
| 10-18 | Similar methodology, comparable hardware, same major version |
| 0-9   | Significant methodological differences, not directly comparable |

### Methodology Rigor (0-25 points per benchmark)
| Score | Description |
|-------|-------------|
| 19-25 | Published methodology, reproducible, raw data available |
| 10-18 | Methodology described, key parameters stated |
| 0-9   | Minimal or no methodology description |

### Environmental Control (0-25 points per benchmark)
| Score | Description |
|-------|-------------|
| 19-25 | Controlled environment, isolated resources, multiple runs |
| 10-18 | Production-like environment, limited isolation |
| 0-9   | Shared, uncontrolled, or undescribed environment |

### Statistical Validity (0-25 points per benchmark)
| Score | Description |
|-------|-------------|
| 19-25 | Confidence intervals, multiple runs, outlier analysis |
| 10-18 | Multiple runs with averages reported |
| 0-9   | Single run or unclear repetition |

## Scale

- **Comparability: 0-25**, determines if comparison is valid
- **Per-benchmark quality: 0-75**, sum of methodology + environment + statistics
- **0.80-1.00**: High confidence in comparison validity
- **0.60-0.79**: Moderate, note methodology differences
- **0.40-0.59**: Low, comparison is directional only
- **0.00-0.39**: Comparison not valid

## Output Format

```yaml
benchmark_comparison:
  id: BC-003
  benchmarks:
    - source_id: SRC-042
      quality_total: 60
    - source_id: SRC-058
      quality_total: 45
  comparability_score: 14
  comparison_confidence: 0.56
  verdict: "Directional comparison only; methodologies differ significantly"
```
