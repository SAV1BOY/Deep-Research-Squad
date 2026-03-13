# Research Quality Rubric

## Purpose

Evaluates the overall quality of a completed research effort, covering breadth,
depth, evidence rigor, and clarity of communication.

## Inputs

- Complete research deliverable (findings, evidence, recommendations)
- Question tree with coverage metrics
- Source and evidence inventories with scores
- Uncertainty and contradiction inventories

## Scoring Criteria

### Coverage Breadth (0-20 points)
| Score | Description |
|-------|-------------|
| 15-20 | All question tree branches explored, no obvious gaps |
| 8-14  | 70%+ branches explored, gaps documented |
| 0-7   | Narrow investigation, major areas unexplored |

### Source Diversity (0-15 points)
| Score | Description |
|-------|-------------|
| 11-15 | 4+ source types consulted, multiple perspectives |
| 6-10  | 2-3 source types, limited perspective range |
| 0-5   | Single source type, monoculture risk |

### Evidence Rigor (0-20 points)
| Score | Description |
|-------|-------------|
| 15-20 | All critical claims backed by strong evidence, chains documented |
| 8-14  | Most critical claims well-evidenced, minor gaps |
| 0-7   | Many claims weakly supported or unsupported |

### Contradiction Handling (0-15 points)
| Score | Description |
|-------|-------------|
| 11-15 | All contradictions identified, investigated, resolved or documented |
| 6-10  | Most contradictions addressed, few unresolved |
| 0-5   | Contradictions ignored or undetected |

### Uncertainty Transparency (0-15 points)
| Score | Description |
|-------|-------------|
| 11-15 | All uncertainties documented with mitigation paths |
| 6-10  | Major uncertainties documented |
| 0-5   | Uncertainties not addressed, false confidence |

### Communication Clarity (0-15 points)
| Score | Description |
|-------|-------------|
| 11-15 | Clear structure, progressive disclosure, actionable conclusions |
| 6-10  | Generally clear, minor organizational issues |
| 0-5   | Unclear, difficult to extract actionable information |

## Scale

- **Total: 0-100**, normalized to 0.0-1.0
- **0.85-1.00**: Excellent - thorough, rigorous, well-communicated
- **0.70-0.84**: Good - solid with minor gaps
- **0.55-0.69**: Adequate - usable but notable weaknesses
- **0.00-0.54**: Below standard - significant rework needed

## Output Format

```yaml
research_quality:
  scores: { coverage: 16, sources: 12, evidence: 15, contradictions: 13, uncertainty: 11, clarity: 13 }
  total_score: 80
  quality_score: 0.80
  quality_level: good
```
