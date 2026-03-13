# Source Card Component

## Purpose

Captures structured metadata about a single information source, enabling consistent
evaluation, citation, and trust scoring across all research activities.

## Structure

```yaml
source_card:
  id: string                    # Unique source identifier (e.g., SRC-001)
  title: string                 # Title of the source
  url: string                   # URL or location reference
  source_type: string           # official-docs | peer-reviewed | blog | forum | book | api
  author: string                # Author or organization
  publication_date: date        # When published or last updated
  access_date: date             # When the researcher accessed it
  trust_score: float            # 0.0 to 1.0 (see source-scoring utility)
  relevance_score: float        # 0.0 to 1.0
  bias_indicators: list[string] # Known biases or conflicts of interest
  key_claims: list[string]      # Main claims extracted from this source
  excerpts:
    - text: string              # Direct quote or paraphrase
      location: string          # Page number, section, or paragraph
      is_direct_quote: boolean
  verification_status: string   # unverified | corroborated | disputed | retracted
  notes: string                 # Researcher notes about this source
```

## Usage Example

```yaml
source_card:
  id: SRC-042
  title: "PostgreSQL 17 Performance Benchmarks"
  url: "https://postgresql.org/docs/17/performance.html"
  source_type: official-docs
  author: "PostgreSQL Global Development Group"
  publication_date: 2025-09-15
  access_date: 2026-03-13
  trust_score: 0.92
  relevance_score: 0.85
  bias_indicators: ["vendor documentation - may emphasize strengths"]
  key_claims: ["50% improvement in parallel query execution"]
  excerpts:
    - text: "Parallel hash joins now scale linearly up to 16 cores"
      location: "Section 4.2"
      is_direct_quote: true
  verification_status: corroborated
  notes: "Cross-referenced with independent benchmarks from Percona"
```

## When to Use

- Every time a new information source is consulted during research
- When building an evidence base that requires traceable citations
- When comparing conflicting information across multiple sources
- During source quality audits or trust calibration exercises
