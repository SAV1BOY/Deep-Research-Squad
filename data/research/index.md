# Research Data Index

## Purpose
Central index for raw and processed research data collected across
all projects. Organized by project and research phase for easy
retrieval and cross-referencing.

## Directory Structure
```
research/
  {project-id}/
    raw/          - Unprocessed source materials
    processed/    - Cleaned and structured data
    extracts/     - Key excerpts and quotes
    metadata/     - Collection metadata and logs
```

## Naming Convention
Files follow the pattern: `{project-id}_{phase}_{source-id}_{desc}.{ext}`

## Data Retention
- Raw data: Retained for 2 years after project completion
- Processed data: Retained for 5 years
- Extracts: Retained indefinitely as part of knowledge base

## Cross-References
- Source details: see `data/registries/source-registry.yaml`
- Claims extracted: see `data/registries/claim-registry.yaml`
- Citations: see `data/registries/citation-registry.yaml`

## Quality Standards
- All files must have corresponding metadata entries
- Raw data must not be modified after collection
- Processed data must document transformation steps
- Extracts must include source page/section references
