# Evidence Strength Rubric

## Purpose

Scores individual evidence pieces consistently for fair comparison and aggregation.

## Inputs

- Evidence type, methodology, sample size, reproducibility, source trust, recency

## Scoring Criteria

### Evidence Type Weight (0-20 points)
| Score | Description |
|-------|-------------|
| 15-20 | Controlled experiment or systematic empirical study |
| 8-14  | Statistical analysis or recognized expert opinion |
| 0-7   | Anecdotal, case study, or unattributed |

### Methodology Quality (0-20 points)
| Score | Description |
|-------|-------------|
| 15-20 | Rigorous, transparent, reproducible |
| 8-14  | Clear methodology, reasonable controls |
| 0-7   | Methodology vague or not stated |

### Sample Adequacy (0-15 points)
| Score | Description |
|-------|-------------|
| 11-15 | Large, representative sample |
| 6-10  | Moderate, reasonably representative |
| 0-5   | Small sample or single observation |

### Reproducibility (0-15 points)
| Score | Description |
|-------|-------------|
| 11-15 | Independently reproduced |
| 6-10  | Reproducible in principle |
| 0-5   | Not reproducible or testable |

### Relevance (0-15 points)
| Score | Description |
|-------|-------------|
| 11-15 | Directly addresses the claim and context |
| 6-10  | Related but different context |
| 0-5   | Tangential, requires inference |

### Recency (0-15 points)
| Score | Description |
|-------|-------------|
| 11-15 | Within last 6 months |
| 6-10  | Within 1-2 years |
| 0-5   | Older than 2 years in fast-moving domain |

## Scale

- **Total: 0-100**, normalized to 0.0-1.0
- **0.80-1.00**: Strong | **0.60-0.79**: Moderate | **0.40-0.59**: Weak | **0.00-0.39**: Very weak

## Output Format

```yaml
evidence_strength:
  evidence_id: EV-033
  scores: { type: 17, methodology: 16, sample: 12, reproducibility: 12, relevance: 14, recency: 13 }
  total: 84
  strength: 0.84
  level: strong
```
