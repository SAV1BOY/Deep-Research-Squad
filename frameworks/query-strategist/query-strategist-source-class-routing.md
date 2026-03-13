# Source Class Routing Framework

## Purpose
Match each research question type to the most appropriate class of sources. Prevents the common error of searching the wrong source universe for a given question, which wastes effort and produces weak evidence.

## When to Use
- When planning which sources to search for each sub-question.
- When initial searches in one source class yield poor results.
- When the research requires different types of evidence (quantitative data, expert opinion, primary accounts).
- When building a search plan that spans multiple agents and source types.

## Inputs
- Research sub-questions from the issue tree or question pyramid.
- Required evidence types (statistical, qualitative, primary, secondary).
- Available source platforms and databases.
- Time and access constraints.

## Process

### Step 1: Classify the Question Type
- **Factual/definitional**: What is X? How does X work?
- **Quantitative**: How much? How many? What is the rate?
- **Causal**: Why does X happen? What causes Y?
- **Comparative**: How does X differ from Y?
- **Predictive**: What will happen if X?
- **Evaluative**: Is X good/effective/appropriate?
- **Exploratory**: What is known about X? What are the perspectives?

### Step 2: Map Question Type to Source Class

| Question Type | Primary Sources | Secondary Sources | Tertiary Sources |
|---|---|---|---|
| Factual | Standards docs, specs | Textbooks, encyclopedias | Wikipedia, glossaries |
| Quantitative | Databases, surveys, filings | Research papers, reports | Data aggregators |
| Causal | Experiments, case studies | Meta-analyses, reviews | Summaries, overviews |
| Comparative | Direct measurements | Comparative studies | Comparison websites |
| Predictive | Forecasting models, expert panels | Analyst reports | News forecasts |
| Evaluative | User studies, trials | Systematic reviews | Rating sites |
| Exploratory | Interviews, fieldwork | Literature reviews | Topic overviews |

### Step 3: Select Specific Source Platforms
- **Academic**: Google Scholar, PubMed, SSRN, arXiv, IEEE, JSTOR.
- **Market/Business**: Company filings, industry reports, trade publications, press releases.
- **Government/Policy**: Government databases, regulatory filings, legislative records.
- **OSINT/Current**: News aggregators, social media, forums, blogs, podcasts.
- **Primary/Original**: Direct interviews, surveys, datasets, official statistics.
- **Patent/Technical**: Patent databases, technical standards bodies, RFCs.

### Step 4: Assess Source Availability and Access
- Which sources are freely accessible vs paywalled?
- Which require specialized search techniques?
- What are the expected result volumes for each source?
- Rank sources by accessibility and expected yield.

### Step 5: Build the Routing Table
- For each sub-question, assign a primary source class and 1-2 fallback classes.
- Specify the exact platforms to search within each class.
- Note any special considerations (access requirements, search syntax).

### Step 6: Execute and Adjust
- Search the primary source class first.
- If results are insufficient, move to fallback classes.
- If a source class consistently outperforms expectations, increase its priority.

## Outputs
- A routing table mapping each sub-question to its assigned source classes and platforms.
- Platform-specific search instructions for each route.
- Fallback routing for when primary sources are insufficient.

## Common Pitfalls
- Defaulting to web search for everything instead of targeting specialized databases.
- Using academic sources for fast-moving market questions that journals have not yet covered.
- Using news sources for technical depth that only academic literature can provide.
- Ignoring primary sources and relying entirely on secondary interpretations.
- Not having fallback routes, leading to dead ends when the primary source class fails.
- Treating all questions as the same type and routing them identically.

## Related Frameworks
- **Query Expansion**: Expand queries before routing to maximize coverage within each source class.
- **Operator Matrix**: Each platform has different search operators; consult after routing.
- **Primary-Secondary Split**: Detailed guidance on classifying sources within a class.
- **Authority Proximity**: Evaluate source quality within the selected class.
- **Signal-Noise Scoring**: Score results from each source class for quality.
