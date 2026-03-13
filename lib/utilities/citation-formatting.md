# Citation Formatting Guide

## Purpose

Ensures consistent, traceable citations across all research deliverables, enabling
readers to locate and verify original sources.

## Inputs

- Source card data (author, title, URL, date, source type)
- Specific location within the source (section, page, timestamp)
- Whether the reference is a direct quote or paraphrase

## Formatting Criteria

### Inline Citations

Use bracketed source IDs for inline references:
- Single source: `[SRC-042]`
- Multiple sources: `[SRC-042, SRC-058]`
- With location: `[SRC-042, Section 4.2]`
- Direct quote: `"quoted text" [SRC-042, p.15]`

### Full Citation Formats

**Official Documentation:**
`[SRC-ID] Org. "Page Title." Doc Name, version. URL. Accessed: YYYY-MM-DD.`

**Blog Post / Article:**
`[SRC-ID] Author. "Title." Publication, YYYY-MM-DD. URL. Accessed: YYYY-MM-DD.`

**Academic / Peer-Reviewed:**
`[SRC-ID] Author(s). "Paper Title." Journal, Vol(Issue), pp. Pages, YYYY. DOI.`

**Forum / Community:**
`[SRC-ID] Username. "Thread Title." Platform, YYYY-MM-DD. URL. [Trust: score]`

**Book:**
`[SRC-ID] Author(s). Title. Publisher, YYYY. ISBN. pp. Pages.`

### Trust Annotations

Append trust level for non-obvious source quality:
- `[Trust: 0.85/high]` - formal trust assessment
- `[Vendor source]` - potential vendor bias
- `[Unverified]` - not yet corroborated

## Scale

Citations are assessed for completeness:
- **Complete**: All fields populated, URL verified accessible
- **Partial**: Missing minor fields (e.g., access date)
- **Incomplete**: Missing critical fields (author, date, or URL)

## Output Format

```yaml
citation:
  source_id: SRC-042
  inline: "[SRC-042]"
  full: "[SRC-042] PostgreSQL Global Development Group. 'Performance Tuning.' PostgreSQL 17 Docs. https://postgresql.org/docs/17/performance.html. Accessed: 2026-03-13."
  completeness: complete
  trust_annotation: "[Vendor source, Trust: 0.79]"
```
