# Decision Readiness Rubric

## Purpose

Assesses whether research has produced sufficient evidence, analysis, and clarity
to support a confident decision, or whether further work is needed.

## Inputs

- Decision card with options and criteria
- Evidence base with confidence scores on critical claims
- Unresolved contradictions and uncertainties
- Stakeholder requirements and time constraints

## Scoring Criteria

### Evidence Sufficiency (0-20 points)
| Score | Description |
|-------|-------------|
| 15-20 | All critical claims have strong evidence (confidence >0.80) |
| 8-14  | Most critical claims well-evidenced, some gaps |
| 0-7   | Multiple critical claims lack adequate evidence |

### Option Coverage (0-15 points)
| Score | Description |
|-------|-------------|
| 11-15 | All viable options evaluated with comparable depth |
| 6-10  | Most options evaluated, some depth imbalances |
| 0-5   | Only 1-2 options evaluated, others ignored |

### Trade-off Clarity (0-15 points)
| Score | Description |
|-------|-------------|
| 11-15 | All major trade-offs explicitly documented |
| 6-10  | Most trade-offs documented |
| 0-5   | Trade-offs not adequately analyzed |

### Risk Identification (0-15 points)
| Score | Description |
|-------|-------------|
| 11-15 | Risks identified with likelihood and impact for each option |
| 6-10  | Major risks identified, some without full assessment |
| 0-5   | Risks not adequately considered |

### Contradiction Resolution (0-15 points)
| Score | Description |
|-------|-------------|
| 11-15 | All critical contradictions resolved or explicitly accepted |
| 6-10  | Most contradictions resolved, remaining are non-critical |
| 0-5   | Critical contradictions unresolved |

### Stakeholder Alignment (0-20 points)
| Score | Description |
|-------|-------------|
| 15-20 | Decision criteria validated, priorities agreed |
| 8-14  | Most criteria agreed, minor disagreements |
| 0-7   | Significant stakeholder misalignment |

## Scale

- **Total: 0-100**, normalized to 0.0-1.0
- **0.80-1.00**: Ready - proceed with confidence
- **0.60-0.79**: Nearly ready - address specific gaps first
- **0.40-0.59**: Not ready - significant gaps remain
- **0.00-0.39**: Premature - insufficient basis for decision

## Output Format

```yaml
decision_readiness:
  decision_id: DEC-005
  scores: { evidence: 16, options: 13, tradeoffs: 12, risks: 11, contradictions: 13, alignment: 15 }
  total_score: 80
  readiness_score: 0.80
  readiness_level: ready
  blockers: []
```
