# Literature Taxonomy Builder Framework

## Purpose

Build a structured taxonomy of a research field from its literature. Organize the domain into categories, subcategories, and relationships. Track how the taxonomy has evolved over time. A good taxonomy provides a map of the intellectual territory, making it easier to locate specific work, identify relationships between subfields, and spot areas of over- or under-exploration.

## When to Use

- When entering a broad or fragmented research domain that lacks clear organization.
- When existing categorizations are outdated, incomplete, or contested.
- When needing to communicate the structure of a field to non-experts.
- When planning a comprehensive research effort that must cover the full domain.
- When comparing how different communities categorize the same phenomena.

## Inputs

- A body of literature from the field (ideally from a systematic review).
- Existing categorization schemes, if any (from textbooks, surveys, or standards bodies).
- Keyword and topic data from the literature.
- Expert input or authoritative sources on field structure.

## Process

1. **Collect raw categories.** Extract keywords, topics, themes, and labels from the literature. Note how different authors categorize their own work.
2. **Identify natural clusters.** Group related concepts, methods, and topics. Look for terms that co-occur frequently or that authors use interchangeably.
3. **Define top-level categories.** Establish 3-7 major categories that partition the field. Each category should be mutually exclusive and collectively exhaustive (MECE) where possible.
4. **Define subcategories.** Within each top-level category, identify 2-5 subcategories. Apply the same MECE principle.
5. **Map relationships.** Identify how categories relate to each other: dependencies, overlaps, hierarchies, and cross-cutting concerns.
6. **Trace evolution.** How has the taxonomy changed over time? What categories are new? What categories have merged, split, or disappeared?
7. **Validate with the literature.** Test the taxonomy by classifying a sample of sources. Does every source fit? Are there sources that do not fit any category (indicating a missing category)?
8. **Compare with existing taxonomies.** How does your taxonomy differ from existing ones? Are the differences justified by evidence, or do they reflect different perspectives?
9. **Document boundary cases.** Note sources or topics that sit at the boundary between categories. These boundaries often indicate areas of active research or conceptual ambiguity.
10. **Finalize and annotate.** Produce the taxonomy with definitions for each category, representative examples, and notes on boundary cases.

## Outputs

- A hierarchical taxonomy with top-level categories and subcategories.
- Definitions and scope statements for each category.
- A relationship map showing how categories connect.
- An evolutionary timeline showing how the taxonomy has changed.
- Boundary cases and ambiguous classifications.
- A validation report showing how well the taxonomy covers the literature.

## Common Pitfalls

- **Premature categorization.** Creating categories before reviewing enough literature, then forcing subsequent sources into predetermined boxes.
- **Too many categories.** Granularity is good, but excessive categories reduce usability and clarity.
- **Too few categories.** Overly broad categories hide important distinctions within the field.
- **Ignoring alternative taxonomies.** Different communities may organize the same field differently; all perspectives have value.
- **Static thinking.** Taxonomies evolve; treating them as permanent fixtures leads to outdated classification.
- **Category reification.** Treating categories as real things rather than useful abstractions.
- **Forcing MECE.** Some domains genuinely overlap; forcing mutual exclusivity can distort the taxonomy.

## Quality Criteria

- Top-level categories must be justified with evidence from the literature, not imposed from intuition.
- The taxonomy must be validated by classifying a representative sample of sources; unclassifiable sources indicate missing categories.
- Boundary cases must be explicitly documented, not silently forced into the nearest category.
- The taxonomy must include an evolutionary dimension showing how categories have changed over time.

## Related Frameworks

- `literature-systematic-review.md` - The systematic review provides the literature that the taxonomy organizes.
- `literature-gap-mapping.md` - The taxonomy structures the gap map; empty taxonomy cells indicate gaps.
- `literature-seminal-chain.md` - Seminal works often define the original categories of a field.
- `literature-meta-analysis-lite.md` - Meta-analysis results can be organized using the taxonomy.
