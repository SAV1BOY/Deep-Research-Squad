# Decisions Data Index

## Purpose
Central index for decision artifacts including decision frameworks,
analysis workpapers, and outcome tracking documents. Complements
the decision registry with detailed supporting materials.

## Directory Structure
```
decisions/
  {decision-id}/
    brief.md          - Decision context and framing
    analysis/         - Supporting analysis documents
    options/          - Option evaluation materials
    recommendation.md - Final recommendation document
    outcome/          - Post-decision outcome tracking
```

## Naming Convention
Decision folders use IDs from the decision registry: `DEC-YYYY-NNN`

## Decision Artifact Lifecycle
1. **Framing**: Document the decision context and criteria
2. **Analysis**: Store all analytical workpapers
3. **Recommendation**: Archive the final recommendation
4. **Tracking**: Monitor and document outcomes over time
5. **Review**: Conduct retrospective analysis

## Cross-References
- Decision registry: see `data/registries/decision-registry.yaml`
- Supporting research: see `data/research/index.md`
- Lessons learned: see `data/registries/lessons-learned-registry.yaml`

## Quality Standards
- Every decision folder must link to a decision registry entry
- Analysis workpapers must be reproducible
- Outcome tracking should continue for at least 6 months
- Retrospectives should be completed within 3 months of outcome
