# Freshness Matrix Framework

## Purpose
Determine when source freshness (recency) matters and when older sources are equally or more valuable. Prevents two opposite errors: dismissing valid older research in favor of shallow recent content, and relying on outdated information when the landscape has changed.

## When to Use
- When calibrating the recency factor in Signal-Noise Scoring.
- When deciding whether to include or exclude sources based on publication date.
- When the research spans topics with different rates of change.
- When stakeholders question why older or newer sources were used.

## Inputs
- The research sub-question being addressed.
- The field or domain of the sub-question.
- Known rate of change in the relevant area.
- Publication dates of available sources.

## Process

### Step 1: Classify the Topic's Rate of Change
Assign the topic to one of four change-rate categories:

**Rapid change (half-life: months)**
- Examples: cryptocurrency prices, social media trends, breaking news, startup landscapes, AI model capabilities.
- Sources older than 6-12 months may be significantly outdated.

**Moderate change (half-life: 1-3 years)**
- Examples: market share, technology adoption, regulatory environments, competitive landscapes.
- Sources older than 2-3 years need freshness verification.

**Slow change (half-life: 5-10 years)**
- Examples: demographic trends, institutional structures, industry standards, established scientific knowledge.
- Sources up to 5-10 years old are generally reliable.

**Stable (half-life: decades or more)**
- Examples: mathematical principles, fundamental physics, historical events, foundational theory.
- Age of source is largely irrelevant; quality and rigor matter more.

### Step 2: Determine Freshness Requirements
Based on the change-rate category, set freshness thresholds:

| Change Rate | Preferred Window | Acceptable Window | Outdated |
|---|---|---|---|
| Rapid | Last 6 months | Last 12 months | Older than 1 year |
| Moderate | Last 2 years | Last 3-5 years | Older than 5 years |
| Slow | Last 5 years | Last 10 years | Older than 10 years |
| Stable | Any time period | Any time period | Never solely on age |

### Step 3: Apply Freshness Adjustments to Scoring
- Sources within the preferred window: No penalty. Score recency as 5.
- Sources within the acceptable window: Minor penalty. Score recency as 3.
- Sources in the outdated range: Significant penalty. Score recency as 1-2.
- Exception: Foundational or seminal works score 5 regardless of age if the knowledge they contain has not been superseded.

### Step 4: Check for Superseding Sources
- Even if a source is within the freshness window, check whether newer work has superseded it.
- A 2-year-old study may be outdated if a more recent study with better methodology has been published.
- Conversely, a 10-year-old study may be current if no subsequent work has challenged or updated it.

### Step 5: Handle Mixed-Rate Research
- When a research question spans topics with different change rates, apply freshness requirements independently to each sub-question.
- Example: A question about "AI regulation" has a rapid-change component (AI capabilities) and a moderate-change component (regulatory frameworks). Apply different freshness thresholds to each.

### Step 6: Document Freshness Decisions
- For each source, record the change-rate classification and freshness assessment.
- When including older sources, document why they remain valid.
- When excluding recent sources, document why they were superseded or insufficient.

## Outputs
- A freshness classification for the research topic or each sub-topic.
- Freshness thresholds (preferred, acceptable, outdated) for each sub-topic.
- Adjusted recency scores for each source.
- Documentation of freshness-related inclusion/exclusion decisions.

## Common Pitfalls
- Applying a single freshness standard across topics with different rates of change.
- Reflexively preferring newer sources even when older foundational work is more rigorous.
- Dismissing an entire source because its data is from a slightly outdated period, even when its methodology or framework remains valid.
- Not checking for superseding sources within the freshness window.
- Confusing publication date with data date. A 2025 paper may use 2020 data.
- Assuming rapid-change topics have no stable foundational knowledge worth citing.

## Related Frameworks
- **Signal-Noise Scoring**: Freshness matrix calibrates the recency factor in scoring.
- **Primary-Secondary Split**: Primary data sources may have different freshness requirements than secondary analyses.
- **Authority Proximity**: Freshness and authority interact; a recent but low-authority source may be less valuable than an older high-authority one.
- **Scope Bounding**: Temporal bounds in scope bounding should align with freshness thresholds.
- **Cross-Source Verification**: When cross-referencing, ensure sources are from comparable time periods.
