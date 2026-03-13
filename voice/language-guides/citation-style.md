# Citation Style Guide

## Purpose

This guide defines how the squad cites sources in all deliverables. Consistent
citation enables traceability, credibility assessment, and reproducibility.
Every claim must be traceable to its origin.

## Citation Format

### Inline Citations

Use bracketed author-date format for inline references:
- Single author: (Smith, 2025)
- Two authors: (Smith & Jones, 2025)
- Three or more: (Smith et al., 2025)
- Multiple sources: (Smith, 2025; Jones, 2024)
- Direct quote: (Smith, 2025, p. 42)

### Reference List Format

Each entry includes:
```
Author(s). (Year). Title. Source/Publisher. URL [Accessed: Date].
```

Example:
```
Smith, J. (2025). Market Dynamics in AI Infrastructure.
  Journal of Technology Strategy, 12(3), 45-67.
  https://doi.org/10.1234/jts.2025.0042 [Accessed: 2026-03-01].
```

## Source Classification

Tag every source with its type and reliability tier:

| Source Type       | Code | Typical Tier |
|-------------------|------|--------------|
| Peer-reviewed     | PR   | Tier 1       |
| Government/regulatory | GV | Tier 1-2   |
| Industry report   | IR   | Tier 2       |
| News (major outlet) | NM | Tier 2-3   |
| Company filing    | CF   | Tier 2       |
| Expert interview  | EI   | Tier 3       |
| Blog/opinion      | BO   | Tier 4       |
| Social media      | SM   | Tier 4-5     |
| Anonymous/leaked  | AN   | Tier 5       |

## Citation Rules

1. **Every factual claim needs a citation.** No exceptions.
2. **Date-stamp access.** Web sources can change. Record when you accessed them.
3. **Distinguish primary from secondary.** If citing Source B's report of Source A,
   cite both: "According to Source A (as reported by Source B, 2025)..."
4. **Flag interested-party sources.** If the source has a commercial interest,
   note it: "(Smith, 2025 [vendor report])."
5. **Archive volatile sources.** If the source may disappear, capture a snapshot.

## Special Cases

### Data Sources

For datasets and databases:
```
Organization. (Year). Dataset Name [Version]. URL [Accessed: Date].
```

### AI-Generated Content

If AI tools were used in research:
```
[AI Tool Name]. (Date). Response to query: "[query summary]".
Model version: [version]. Not independently verified.
```

### Interviews and Conversations

```
[Name/Role], [Organization]. Personal communication, [Date].
[On/Off record]. [Paraphrased/Direct quote].
```

## Citation Density Guidelines

| Document Type      | Citation Density                     |
|--------------------|--------------------------------------|
| Deep dive          | Every factual claim                  |
| Executive brief    | Key findings only; link to full refs |
| Slack update       | Source count ("based on 5 sources")  |
| Synthesis          | Per-finding attribution              |

## Quality Check

- Is every factual claim cited?
- Are access dates recorded for web sources?
- Are interested-party sources flagged?
- Is the reference list complete and consistently formatted?
- Can a reader trace any claim back to its original source?
