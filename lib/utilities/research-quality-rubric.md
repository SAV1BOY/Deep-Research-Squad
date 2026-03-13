# Research Quality Rubric

## Purpose

Evaluates overall quality of a completed research effort across breadth, depth,
evidence rigor, and communication clarity.

## Inputs

- Complete research deliverable with question tree and all inventories

## Scoring Criteria

### Coverage Breadth (0-20 points)
| Score | Description |
|-------|-------------|
| 15-20 | All question tree branches explored |
| 8-14  | 70%+ explored, gaps documented |
| 0-7   | Major areas unexplored |

### Source Diversity (0-15 points)
| Score | Description |
|-------|-------------|
| 11-15 | 4+ source types, multiple perspectives |
| 6-10  | 2-3 source types |
| 0-5   | Single source type |

### Evidence Rigor (0-20 points)
| Score | Description |
|-------|-------------|
| 15-20 | All critical claims backed by strong evidence |
| 8-14  | Most claims well-evidenced |
| 0-7   | Many claims weakly supported |

### Contradiction Handling (0-15 points)
| Score | Description |
|-------|-------------|
| 11-15 | All contradictions investigated and resolved or documented |
| 6-10  | Most addressed, few unresolved |
| 0-5   | Contradictions ignored or undetected |

### Uncertainty Transparency (0-15 points)
| Score | Description |
|-------|-------------|
| 11-15 | All uncertainties documented with mitigation paths |
| 6-10  | Major uncertainties documented |
| 0-5   | Uncertainties not addressed |

### Communication Clarity (0-15 points)
| Score | Description |
|-------|-------------|
| 11-15 | Clear structure, actionable conclusions |
| 6-10  | Generally clear, minor issues |
| 0-5   | Unclear or disorganized |

## Scale

- **Total: 0-100**, normalized to 0.0-1.0
- **0.85-1.00**: Excellent | **0.70-0.84**: Good | **0.55-0.69**: Adequate | **0.00-0.54**: Below standard

## Output Format

```yaml
research_quality:
  scores: { coverage: 16, sources: 12, evidence: 15, contradictions: 13, uncertainty: 11, clarity: 13 }
  total: 80
  quality: 0.80
  level: good
```
