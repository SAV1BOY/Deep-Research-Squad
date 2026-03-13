# Citation Formatter Utility

## Purpose

Standardizes citation formatting across all research deliverables. Ensures consistent
attribution, verifiability, and appropriate detail level based on source type and
deliverable format.

## Inputs

```yaml
citation_formatter:
  inputs:
    source: source_card            # The source being cited
    format: string                 # inline | footnote | bibliography | evidence-table
    include_confidence: boolean    # Whether to append confidence score
    include_access_date: boolean   # Whether to include access date
```

## Output Formats

### Inline Citation
Used within body text for quick attribution.
```
(Author/Org, Year; confidence: 0.XX)
```
**Example:** (Gartner, 2025; confidence: 0.82)

### Footnote Citation
Used for detailed attribution without disrupting reading flow.
```
[N] Author/Org. "Title." Publication/Platform, Date. URL. Accessed: Date.
    Confidence: 0.XX. Evidence type: [type].
```
**Example:**
[1] McKinsey Global Institute. "The State of AI in 2025." McKinsey.com,
    Jan 2025. https://mckinsey.com/ai-2025. Accessed: Mar 2026.
    Confidence: 0.85. Evidence type: expert-analysis.

### Bibliography Entry
Used in source lists and reference sections.
```
Author/Org (Year). "Title." Publication. URL [Accessed: Date].
  Type: [source-taxonomy type]. Trust: [0-1.0]. Notes: [brief].
```

### Evidence Table Citation
Used within evidence tables for compact, structured reference.
```
Source | Date | Type | Confidence | Key Data Point
```

## Formatting Rules

| Rule | Specification |
|------|--------------|
| Author unknown | Use organization name; if unknown, use "Anonymous" |
| Date unknown | Use "n.d." (no date) |
| URL unavailable | Note "offline source" or "paywalled" |
| Multiple authors | First author et al. for 3+ authors |
| Confidence score | Always 0.00-1.00 with two decimal places |
| Access date | Required for all web sources |
| Source type | Must use source-taxonomy classification |

## Special Cases

### Conflicting Sources
When citing sources that contradict each other:
```
(Source A, Year, confidence: 0.XX — supports; Source B, Year, confidence: 0.XX — refutes)
```

### Paywalled or Restricted Sources
```
[N] Author. "Title." Publication, Date. [Paywalled — accessed via institutional license].
```

### Interview or Expert Consultation
```
[N] Name, Title at Organization. Personal communication, Date. [Not publicly verifiable].
```

### AI-Generated or AI-Assisted Content
```
[N] "Query description." AI Tool Name, Date. [AI-generated — independently verified: yes/no].
```

## Validation Rules

- Every citation must map to a source_card in the research package
- Confidence score must match the source_card's trust score
- URLs must be checked for accessibility at time of publication
- Paywalled sources must be flagged explicitly

## Dependencies
- `source-card` component for source metadata
- `source-taxonomy` for type classification
- `confidence-scoring` utility for trust scores
