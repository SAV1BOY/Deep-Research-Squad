# Confidence Maps Data Index

## Purpose
Central index for confidence maps that visualize certainty levels
across research findings, claims, and conclusions. Provides
stakeholders with transparent uncertainty communication.

## Directory Structure
```
confidence-maps/
  project/         - Per-project confidence assessments
  domain/          - Domain-level knowledge confidence
  aggregate/       - Cross-project confidence summaries
  templates/       - Confidence map templates and rubrics
```

## Naming Convention
Files follow: `{scope}_{subject}_{date}.{ext}`

## Confidence Scale
- **High (0.8-1.0)**: Multiple strong, corroborated sources
- **Medium (0.5-0.79)**: Some evidence, partial corroboration
- **Low (0.2-0.49)**: Limited evidence, single source or weak
- **Speculative (0.0-0.19)**: Inference or expert opinion only

## Confidence Map Components
- Finding or claim statement
- Confidence score with justification
- Evidence base summary (number and quality of sources)
- Key assumptions affecting confidence
- What would increase or decrease confidence
- Sensitivity: how much would conclusions change if wrong

## Cross-References
- Claims: see `data/registries/claim-registry.yaml`
- Unknowns: see `data/registries/unknowns-registry.yaml`
- Contradictions: see `data/registries/contradiction-registry.yaml`

## Quality Standards
- Every synthesis output should have a confidence map
- Confidence scores must be justified, not intuited
- Assumptions affecting confidence must be documented
- Confidence maps should be updated when new evidence arrives
