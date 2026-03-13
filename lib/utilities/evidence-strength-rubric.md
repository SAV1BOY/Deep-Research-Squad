# Evidence Strength Rubric

## Purpose

Scores individual pieces of evidence on a consistent scale, enabling fair comparison
and weighted aggregation across the evidence base.

## Inputs

- Evidence type (empirical, statistical, expert opinion, anecdotal, experimental)
- Methodology description and sample size
- Reproducibility status and source trust score
- Recency and relevance to the specific claim

## Scoring Criteria

### Evidence Type Weight (0-20 points)
| Score | Description |
|-------|-------------|
| 15-20 | Controlled experiment or systematic empirical study |
| 8-14  | Statistical analysis or expert opinion from recognized authority |
| 0-7   | Case study, anecdotal, or unattributed |

### Methodology Quality (0-20 points)
| Score | Description |
|-------|-------------|
| 15-20 | Rigorous, transparent, peer-reviewed or reproducible |
| 8-14  | Clear methodology with reasonable controls |
| 0-7   | Methodology vague or not stated |

### Sample Adequacy (0-15 points)
| Score | Description |
|-------|-------------|
| 11-15 | Large, representative sample |
| 6-10  | Moderate sample, reasonably representative |
| 0-5   | Small sample, single observation, or N/A |

### Reproducibility (0-15 points)
| Score | Description |
|-------|-------------|
| 11-15 | Independently reproduced by others |
| 6-10  | Reproducible in principle, methodology available |
| 0-5   | Not reproducible or not testable |

### Relevance (0-15 points)
| Score | Description |
|-------|-------------|
| 11-15 | Directly addresses the specific claim and context |
| 6-10  | Closely related but different context |
| 0-5   | Tangentially related, requires inference to apply |

### Recency (0-15 points)
| Score | Description |
|-------|-------------|
| 11-15 | Generated within the last 6 months |
| 6-10  | Generated within the last 1-2 years |
| 0-5   | Older than 2 years in a fast-moving domain |

## Scale

- **Total: 0-100**, normalized to 0.0-1.0
- **0.80-1.00**: Strong - high weight in aggregation
- **0.60-0.79**: Moderate - standard weight
- **0.40-0.59**: Weak - reduced weight, seek corroboration
- **0.00-0.39**: Very weak - minimal weight, flag for caution

## Output Format

```yaml
evidence_strength:
  evidence_id: EV-033
  scores: { type: 17, methodology: 16, sample: 12, reproducibility: 12, relevance: 14, recency: 13 }
  total_score: 84
  strength: 0.84
  strength_level: strong
```
