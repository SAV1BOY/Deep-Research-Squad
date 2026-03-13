# Synthesis Quality Rubric

## Purpose

Evaluates how well individual findings are integrated into coherent, nuanced,
and actionable conclusions during research synthesis.

## Inputs

- Synthesized findings document
- Underlying claim cards and evidence cards
- Contradiction and uncertainty cards
- Insight cards generated during synthesis

## Scoring Criteria

### Integration Completeness (0-20 points)
| Score | Description |
|-------|-------------|
| 15-20 | All relevant claims and evidence incorporated |
| 8-14  | Most findings integrated, omissions minor |
| 0-7   | Many findings not integrated, synthesis is partial |

### Logical Coherence (0-20 points)
| Score | Description |
|-------|-------------|
| 15-20 | Arguments flow logically, no internal contradictions |
| 8-14  | Generally coherent, minor logical gaps |
| 0-7   | Multiple logical gaps or unsupported jumps |

### Nuance and Balance (0-20 points)
| Score | Description |
|-------|-------------|
| 15-20 | Multiple perspectives represented, trade-offs explicit |
| 8-14  | Good balance, most perspectives included |
| 0-7   | One-sided, oversimplified, or ignores dissenting evidence |

### Insight Generation (0-15 points)
| Score | Description |
|-------|-------------|
| 11-15 | Novel insights emerge beyond individual findings |
| 6-10  | Some new observations, mostly summarization |
| 0-5   | No added value beyond listing findings |

### Actionability (0-15 points)
| Score | Description |
|-------|-------------|
| 11-15 | Clear, specific recommendations with implementation guidance |
| 6-10  | Recommendations present but could be more specific |
| 0-5   | Vague or missing recommendations |

### Traceability (0-10 points)
| Score | Description |
|-------|-------------|
| 8-10  | Every conclusion traceable to specific evidence and sources |
| 4-7   | Most conclusions traceable, some gaps |
| 0-3   | Limited traceability, many unsourced conclusions |

## Scale

- **Total: 0-100**, normalized to 0.0-1.0
- **0.85-1.00**: Excellent - insightful, balanced, and actionable
- **0.70-0.84**: Good - solid integration with minor gaps
- **0.55-0.69**: Adequate - functional but lacks depth
- **0.00-0.54**: Below standard - requires rework

## Output Format

```yaml
synthesis_quality:
  scores: { integration: 17, coherence: 16, nuance: 18, insight: 12, actionability: 13, traceability: 8 }
  total_score: 84
  quality_score: 0.84
  quality_level: good
```
