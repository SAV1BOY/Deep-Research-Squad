# Keyword Grid Framework

## Purpose
Generate a comprehensive, systematic set of search keywords by combining terms across multiple dimensions. Prevents the ad hoc keyword selection that misses important term combinations and ensures thorough coverage of the search space.

## When to Use
- When planning searches for a complex, multi-faceted research question.
- When a single dimension of keywords is insufficient to capture the topic.
- When the research spans multiple contexts, domains, or geographies.
- When you need to ensure no important keyword combination is overlooked.

## Inputs
- Core concepts from the research question.
- Scope boundaries (temporal, geographic, domain).
- Known terminology from initial exploration.
- Target source platforms.

## Process

### Step 1: Define Grid Axes
Select 3-5 axes from the following dimensions:

- **Concept axis**: The core subject matter terms (e.g., "machine learning," "artificial intelligence," "deep learning").
- **Context axis**: The setting or application area (e.g., "healthcare," "diagnosis," "clinical").
- **Domain axis**: The academic or professional field (e.g., "computer science," "medicine," "biostatistics").
- **Time axis**: Temporal qualifiers (e.g., "2024," "recent," "emerging," "future").
- **Geography axis**: Location-specific terms (e.g., "European," "US," "global," "developing countries").
- **Method axis**: Research methodology terms (e.g., "randomized trial," "case study," "meta-analysis").
- **Outcome axis**: Result or impact terms (e.g., "accuracy," "cost reduction," "patient outcomes").

### Step 2: Populate Each Axis
- List 3-8 terms per axis.
- Include synonyms, abbreviations, and variant spellings.
- Order terms from most specific to most general within each axis.

### Step 3: Generate Combinations
- Create combinations by selecting one term from each axis.
- Not all combinations are meaningful; filter out nonsensical pairings.
- For a 3-axis grid with 5 terms each, the maximum is 125 combinations. Most will be pruned.
- Focus on combinations that represent realistic search scenarios.

### Step 4: Prioritize Combinations
- Rate each combination on two scales:
  - **Expected relevance**: How likely is this combination to return on-topic results?
  - **Expected uniqueness**: How likely is this combination to surface results not found by other combinations?
- Prioritize high-relevance, high-uniqueness combinations.
- Discard low-relevance combinations regardless of uniqueness.

### Step 5: Format for Platform
- Convert prioritized combinations into platform-appropriate query syntax.
- Apply Boolean operators (AND, OR, NOT) as needed.
- Adjust for platform-specific limitations (character limits, operator support).
- Group queries by platform if using multiple search engines.

### Step 6: Execute in Batches
- Run queries in priority order, not randomly.
- After each batch (typically 5-10 queries), assess results.
- If a particular axis is producing strong results, explore more combinations along that axis.
- If an axis consistently adds noise, consider dropping it.

### Step 7: Iterate the Grid
- Add new terms discovered in search results to the relevant axes.
- Remove terms that consistently produce no useful results.
- The grid is a living document, not a one-time creation.

## Outputs
- A populated keyword grid showing all axes and their terms.
- A prioritized list of keyword combinations ready for search.
- Platform-formatted queries for each combination.
- An iteration log tracking which combinations were productive.

## Common Pitfalls
- Too many axes, creating an unmanageable number of combinations.
- Too few terms per axis, missing important variations.
- Not pruning nonsensical combinations, wasting search effort.
- Treating the grid as exhaustive on first draft instead of iterating.
- Ignoring platform-specific formatting, leading to syntax errors.
- Equal-weighting all combinations instead of prioritizing by expected value.

## Related Frameworks
- **Query Expansion**: Expansion techniques populate the grid axes.
- **Semantic Pivoting**: When the grid fails, pivot to new conceptual territories.
- **Operator Matrix**: Provides the syntax for formatting grid combinations.
- **Source Class Routing**: Different grid combinations may route to different source classes.
- **Scope Bounding**: Grid axes should respect scope boundaries.
