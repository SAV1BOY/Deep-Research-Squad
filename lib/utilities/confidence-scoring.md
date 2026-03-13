# Confidence Level Scoring

## Purpose

Standardized framework for assessing and communicating confidence levels in claims,
findings, and recommendations throughout the research process.

## Inputs

- Number and quality of supporting/contradicting evidence
- Source trust scores for relevant sources
- Degree of corroboration across independent sources
- Known uncertainties and gaps

## Scoring Criteria

### Evidence Volume (0-20 points)
| Score | Description |
|-------|-------------|
| 15-20 | 5+ independent pieces of evidence |
| 8-14  | 2-4 independent pieces of evidence |
| 0-7   | 0-1 pieces of evidence, inference only |

### Evidence Quality (0-25 points)
| Score | Description |
|-------|-------------|
| 19-25 | Empirical, reproducible, from high-trust sources |
| 10-18 | Moderate evidence, some reliance on expert opinion |
| 0-9   | Weak or anecdotal evidence, speculation only |

### Source Agreement (0-20 points)
| Score | Description |
|-------|-------------|
| 15-20 | All sources agree, no contradictions |
| 8-14  | Majority agree but notable dissent exists |
| 0-7   | Sources split or majority contradict |

### Conditions Clarity (0-15 points)
| Score | Description |
|-------|-------------|
| 11-15 | Conditions under which claim holds are fully specified |
| 6-10  | Most conditions identified, some ambiguity |
| 0-5   | Conditions unclear or unspecified |

### Verification Status (0-20 points)
| Score | Description |
|-------|-------------|
| 15-20 | Independently verified through experiment or primary data |
| 8-14  | Cross-verified across multiple sources |
| 0-7   | Unverified or contested |

## Scale

- **Total: 0-100**, normalized to 0.0-1.0
- **0.90-1.00**: Very High - treat as established fact
- **0.75-0.89**: High - reliable for most decisions
- **0.60-0.74**: Moderate - usable with documented caveats
- **0.40-0.59**: Low - flag as uncertain, seek more evidence
- **0.00-0.39**: Very Low - do not base decisions on this

## Output Format

```yaml
confidence:
  target: "CLM-017: Redis failover under 2 seconds"
  scores: { volume: 16, quality: 18, agreement: 13, conditions: 12, verification: 14 }
  total_score: 73
  confidence: 0.73
  level: moderate
```
