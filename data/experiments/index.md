# Experiments Data Index

## Purpose
Central index for research experiments, methodology trials, and
analytical technique tests. Tracks both successful and failed
experiments to build institutional knowledge.

## Directory Structure
```
experiments/
  {experiment-id}/
    protocol.md    - Experiment design and hypothesis
    data/          - Raw and processed experiment data
    results.md     - Results and statistical analysis
    conclusions.md - Conclusions and recommendations
```

## Naming Convention
Experiment IDs follow: `EXP-{YYYY}-{NNN}`

## Experiment Protocol Template
Each experiment should document:
- Hypothesis to test (linked to hypothesis registry)
- Variables: independent, dependent, controlled
- Methodology and measurement approach
- Success criteria and statistical thresholds
- Expected duration and resource requirements

## Experiment Types
- **Methodology experiments**: Testing new research approaches
- **Source experiments**: Evaluating new data source quality
- **Tool experiments**: Assessing new analytical tools
- **Framework experiments**: Validating analytical frameworks

## Cross-References
- Hypotheses: see `data/registries/hypothesis-registry.yaml`
- Methodologies: see `data/registries/methodology-registry.yaml`
- Lessons learned: see `data/registries/lessons-learned-registry.yaml`

## Quality Standards
- All experiments must have pre-registered hypotheses
- Negative results must be documented, not discarded
- Methodology must be documented for reproducibility
- Statistical analysis must include effect sizes and confidence
