# Glossaries Data Index

## Purpose
Central index for domain-specific glossaries and terminology databases.
Ensures consistent terminology use across research projects and
facilitates knowledge transfer between teams.

## Directory Structure
```
glossaries/
  {domain}/
    terms.yaml       - Term definitions and relationships
    acronyms.yaml    - Acronym expansions and context
    jargon-map.yaml  - Industry jargon translations
```

## Naming Convention
Files follow: `{domain}_{glossary-type}.yaml`

## Term Entry Format
Each glossary entry should include:
- Term (canonical form)
- Definition (clear, concise, domain-appropriate)
- Synonyms and aliases
- Related terms
- Source of definition
- Domain context and usage notes

## Glossary Types
- **Domain glossaries**: Technical terms per subject area
- **Acronym databases**: Expansion and context for abbreviations
- **Jargon maps**: Translation of industry-specific language
- **Cross-domain bridges**: Terms that differ across domains

## Cross-References
- Domain knowledge: see `data/registries/domain-registry.yaml`
- Research projects: see `projects/` subdirectories
- Stakeholder communication plans in project briefs

## Quality Standards
- Definitions must be precise and unambiguous
- Domain context must be specified when terms vary across fields
- Glossaries should be reviewed by domain experts
- New terms discovered during research should be added promptly
