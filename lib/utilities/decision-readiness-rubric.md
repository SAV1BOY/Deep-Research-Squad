# Decision Readiness Rubric

## Purpose

Assesses whether research supports a confident decision or needs further work.

## Inputs

- Decision card with options, evidence base, contradictions, uncertainties
- Stakeholder requirements and time constraints

## Scoring Criteria

### Evidence Sufficiency (0-20 points)
| Score | Description |
|-------|-------------|
| 15-20 | All critical claims have strong evidence (confidence >0.80) |
| 8-14  | Most claims well-evidenced, some gaps |
| 0-7   | Multiple critical claims lack adequate evidence |

### Option Coverage (0-15 points)
| Score | Description |
|-------|-------------|
| 11-15 | All viable options evaluated comparably |
| 6-10  | Most options evaluated, some imbalances |
| 0-5   | Only 1-2 options evaluated |

### Trade-off Clarity (0-15 points)
| Score | Description |
|-------|-------------|
| 11-15 | All major trade-offs explicitly documented |
| 6-10  | Most trade-offs documented |
| 0-5   | Trade-offs not adequately analyzed |

### Risk Identification (0-15 points)
| Score | Description |
|-------|-------------|
| 11-15 | Risks identified with likelihood and impact |
| 6-10  | Major risks identified, some incomplete |
| 0-5   | Risks not adequately considered |

### Contradiction Resolution (0-15 points)
| Score | Description |
|-------|-------------|
| 11-15 | Critical contradictions resolved or accepted |
| 6-10  | Most resolved, remaining non-critical |
| 0-5   | Critical contradictions unresolved |

### Stakeholder Alignment (0-20 points)
| Score | Description |
|-------|-------------|
| 15-20 | Criteria validated, priorities agreed |
| 8-14  | Most criteria agreed, minor disagreements |
| 0-7   | Significant misalignment |

## Scale

- **Total: 0-100**, normalized to 0.0-1.0
- **0.80-1.00**: Ready to decide | **0.60-0.79**: Nearly ready | **0.40-0.59**: Not ready | **0.00-0.39**: Premature

## Output Format

```yaml
decision_readiness:
  decision_id: DEC-005
  scores: { evidence: 16, options: 13, tradeoffs: 12, risks: 11, contradictions: 13, alignment: 15 }
  total: 80
  readiness: 0.80
  level: ready
```
