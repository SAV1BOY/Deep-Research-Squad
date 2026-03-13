# Query Expansion Framework

## Purpose
Systematically expand an initial search query into a comprehensive set of alternative formulations to maximize recall and uncover evidence that a single query would miss. Prevents the common failure of relying on one phrasing and missing critical sources that use different terminology.

## When to Use
- At the start of any search task, before executing queries.
- When an initial query returns insufficient or irrelevant results.
- When the research topic spans multiple disciplines that use different terminology.
- When investigating topics where jargon varies by region, industry, or era.

## Inputs
- The original research question or search query.
- Domain context (which field or industry).
- Known terminology variations.
- Target source platforms.

## Process

### Step 1: Extract Core Concepts
- Break the query into its fundamental concepts (typically 2-5).
- For each concept, identify the precise meaning intended.
- Distinguish between concepts that must all be present (AND logic) and alternatives (OR logic).

### Step 2: Generate Synonyms
- For each core concept, list 3-7 synonyms.
- Include formal/academic terms and informal/colloquial terms.
- Include abbreviations, acronyms, and spelled-out forms.
- Use a thesaurus or domain glossary if available.

### Step 3: Identify Related Concepts
- For each core concept, list adjacent or related concepts.
- These are not synonyms but concepts that co-occur with or are closely tied to the target.
- Include hypernyms (broader terms) and hyponyms (narrower terms).

### Step 4: Generate Alternative Phrasings
- Rewrite the full query in 3-5 different ways.
- Vary sentence structure: question form, statement form, noun phrase form.
- Vary specificity: more specific, more general, more technical, more plain-language.

### Step 5: Add Multilingual Terms
- If the topic has international relevance, identify key terms in other languages.
- Focus on languages where significant research or discussion occurs.
- Include transliterated terms where alphabets differ.

### Step 6: Compile the Expansion Set
- Organize all expanded terms by core concept.
- Create a master query list combining terms with Boolean logic.
- Prioritize queries by expected yield (most promising first).
- Cap the total number of queries to prevent diminishing returns (typically 10-20).

### Step 7: Test and Iterate
- Run the top 3-5 queries and evaluate results.
- If results are poor, revisit expansion using terms found in near-miss results.
- Add new terms discovered in relevant results to the expansion set.

## Outputs
- A structured expansion table: core concept to list of synonyms, related terms, and alternative phrasings.
- A prioritized list of 10-20 expanded queries ready for execution.
- Notes on which platforms each query variant is best suited for.

## Common Pitfalls
- Expanding too broadly, generating noise that overwhelms signal.
- Expanding only with synonyms and missing related concepts that unlock new source pools.
- Ignoring field-specific jargon that differs from everyday language.
- Not testing expansions iteratively; a single round of expansion is rarely sufficient.
- Treating all expanded queries as equal priority instead of ranking them.
- Forgetting to include acronyms and abbreviations, which are often used in titles and abstracts.

## Related Frameworks
- **Semantic Pivoting**: When expansion fails, pivot to adjacent semantic spaces.
- **Keyword Grid**: Systematic multi-dimensional approach to keyword generation.
- **Operator Matrix**: Apply platform-specific operators to expanded queries.
- **Source Class Routing**: Route different expanded queries to appropriate source platforms.
- **Question Pyramid**: Granddaughter questions feed the initial queries to expand.
