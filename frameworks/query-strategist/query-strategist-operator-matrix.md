# Operator Matrix Framework

## Purpose
Provide a comprehensive reference for platform-specific search operators, syntax rules, and best practices. Ensures the Query Strategist agent constructs maximally effective queries for each target platform rather than using generic search terms everywhere.

## When to Use
- When formatting queries for specific search platforms.
- When basic keyword searches return too many irrelevant results.
- When precise filtering by date, source type, domain, or field is needed.
- As a reference during query execution across multiple platforms.

## Inputs
- Expanded keywords and keyword grid combinations.
- Target platforms identified by source class routing.
- Specific filtering needs (date range, language, file type, domain).

## Process

### Step 1: Identify Target Platforms
- List all platforms that will be searched for this research task.
- Confirm access and any authentication requirements.
- Note platform-specific limitations (rate limits, result caps).

### Step 2: Apply Google Search Operators
- `"exact phrase"` — Force exact match.
- `site:domain.com` — Restrict to a specific domain.
- `filetype:pdf` — Restrict to file type (pdf, csv, xlsx, doc).
- `-term` — Exclude a term.
- `intitle:term` — Term must appear in the page title.
- `inurl:term` — Term must appear in the URL.
- `before:YYYY-MM-DD` / `after:YYYY-MM-DD` — Date filtering.
- `OR` — Boolean OR between terms (must be capitalized).
- `*` — Wildcard for unknown words in a phrase.
- Best practice: Combine 2-3 operators per query. Avoid over-constraining.

### Step 3: Apply Google Scholar Operators
- `"exact phrase"` — Exact match in title or body.
- `author:lastname` — Filter by author.
- `source:"Journal Name"` — Filter by publication.
- Date range filter via the sidebar (not an operator).
- `allintitle:terms` — All terms must appear in the title.
- Best practice: Use shorter queries than web search. Scholar handles natural language well.

### Step 4: Apply PubMed Operators
- `[MeSH Terms]` — Use Medical Subject Headings for precise biomedical search.
- `[Title/Abstract]` — Restrict search to title and abstract.
- `[Author]` — Filter by author name.
- `AND`, `OR`, `NOT` — Boolean operators (capitalized).
- `"phrase"[Title]` — Exact phrase in title only.
- Date filters: `YYYY/MM/DD:YYYY/MM/DD[dp]`.
- Best practice: Always start with MeSH terms for biomedical topics. Supplement with free-text.

### Step 5: Apply Social Media Operators
- **Twitter/X**: `from:user`, `since:YYYY-MM-DD`, `until:YYYY-MM-DD`, `filter:links`, `min_faves:N`.
- **Reddit**: `site:reddit.com/r/subreddit`, `flair:tag`, or use Reddit's native search with `subreddit:name`.
- **LinkedIn**: Limited operators; use Google with `site:linkedin.com/pulse` for articles.
- Best practice: Social media search is noisy. Combine with temporal filters aggressively.

### Step 6: Apply Patent Database Operators
- **Google Patents**: `inventor:name`, `assignee:company`, `before:YYYY`, `after:YYYY`, CPC classification codes.
- **USPTO**: Use structured search with field codes (IN/ for inventor, AN/ for assignee, ISD/ for issue date).
- **Espacenet**: CPC/IPC classification, applicant name, publication date.
- Best practice: Use classification codes over keywords for precision. Keywords miss patents that describe the same concept differently.

### Step 7: Build Platform-Specific Query Templates
- For each research task, create reusable query templates per platform.
- Template format: `[core concept] [operator:filter] [operator:filter]`.
- Document which template worked best for future reference.

## Outputs
- A matrix mapping each platform to its supported operators and syntax.
- Platform-specific formatted queries ready for execution.
- Reusable query templates for common research patterns.
- Notes on platform quirks and limitations.

## Common Pitfalls
- Using Google syntax on platforms that do not support it.
- Over-constraining queries with too many operators, returning zero results.
- Forgetting that some operators are case-sensitive (OR vs or).
- Not using controlled vocabularies (MeSH, CPC codes) on platforms that support them.
- Ignoring platform-specific date filtering, missing temporal precision.
- Assuming all platforms handle Boolean logic the same way.

## Related Frameworks
- **Query Expansion**: Provides the keywords to which operators are applied.
- **Keyword Grid**: Grid combinations are formatted using these operators.
- **Source Class Routing**: Determines which platforms to target and thus which operators to use.
- **Semantic Pivoting**: After operator-enhanced queries fail, consider semantic pivoting.
- **Signal-Noise Scoring**: Evaluate whether operator use improved result quality.
