# Source Trust Scoring Rubric

## Purpose

Provides a standardized method for scoring source trustworthiness, ensuring
consistent evaluation across all research activities and agents.

## Inputs

- Source type (from source taxonomy)
- Author credentials and affiliation
- Publication venue, date, and reputation
- Presence of citations or references
- Known biases or conflicts of interest

## Scoring Criteria

### Authority (0-25 points)
| Score | Description |
|-------|-------------|
| 19-25 | Primary source, recognized domain authority, institutional backing |
| 10-18 | Established practitioner, credible publication |
| 0-9   | Unknown author, no credentials or institutional backing |

### Methodology (0-25 points)
| Score | Description |
|-------|-------------|
| 19-25 | Rigorous methodology, reproducible, transparent data |
| 10-18 | Methodology described but not fully reproducible |
| 0-9   | No methodology; opinion or assertion only |

### Currency (0-20 points)
| Score | Description |
|-------|-------------|
| 15-20 | Published within 6 months, covers latest state |
| 8-14  | Published within 1-2 years, mostly current |
| 0-7   | Older than 2 years, high risk of obsolescence |

### Independence (0-15 points)
| Score | Description |
|-------|-------------|
| 11-15 | Fully independent, no conflicts of interest |
| 6-10  | Minor potential bias, disclosed or inferable |
| 0-5   | Direct commercial interest, marketing material |

### Corroboration (0-15 points)
| Score | Description |
|-------|-------------|
| 11-15 | Claims corroborated by 3+ independent sources |
| 6-10  | Claims corroborated by 1-2 sources |
| 0-5   | Unchecked or contradicted by other sources |

## Scale

- **Total: 0-100**, normalized to 0.0-1.0
- **0.80-1.00**: High trust - suitable as primary evidence
- **0.60-0.79**: Moderate trust - useful with corroboration
- **0.40-0.59**: Low trust - supplementary only
- **0.00-0.39**: Minimal trust - note but do not rely upon

## Output Format

```yaml
source_trust:
  source_id: SRC-042
  scores: { authority: 22, methodology: 18, currency: 17, independence: 10, corroboration: 12 }
  total_score: 79
  trust_score: 0.79
  trust_level: moderate
```
