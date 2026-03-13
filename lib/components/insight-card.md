# Insight Card Component

## Purpose

Captures a novel insight, pattern, or non-obvious finding that emerges during
research synthesis, going beyond individual claims to document higher-order understanding.

## Structure

```yaml
insight_card:
  id: string                    # Unique identifier (e.g., INS-001)
  title: string                 # Brief title of the insight
  description: string           # Full explanation of the insight
  insight_type: string          # pattern | correlation | gap | implication | trend
  derived_from:
    claim_ids: list[string]     # Claims that led to this insight
    evidence_ids: list[string]  # Evidence that supports this insight
    source_ids: list[string]    # Sources consulted
  confidence: float             # 0.0 to 1.0
  novelty: string               # high | medium | low - how unexpected is this
  actionability: string         # high | medium | low - how actionable is this
  implications: list[string]    # What this insight means for the research
  related_insights: list[string] # Other insight card IDs
  validation_status: string     # hypothesis | partially-validated | validated
  stakeholder_relevance: string # Who cares about this insight
  tags: list[string]            # Categorization tags
  discovered_at: datetime
```

## Usage Example

```yaml
insight_card:
  id: INS-008
  title: "Write-heavy workloads invert traditional database rankings"
  description: >
    Under write-heavy conditions (>80% writes), databases typically recommended
    for read performance (PostgreSQL, MySQL) are outperformed by LSM-tree based
    systems (Cassandra, ScyllaDB) by 3-5x on throughput metrics.
  insight_type: pattern
  derived_from:
    claim_ids: [CLM-017, CLM-031, CLM-045]
    evidence_ids: [EV-033, EV-061, EV-072]
    source_ids: [SRC-042, SRC-058, SRC-071]
  confidence: 0.88
  novelty: medium
  actionability: high
  implications:
    - "Workload characterization must precede database selection"
    - "Mixed workload systems may benefit from polyglot persistence"
  related_insights: [INS-003, INS-005]
  validation_status: partially-validated
  stakeholder_relevance: "Engineering team evaluating database options"
  tags: [databases, performance, write-patterns]
  discovered_at: 2026-03-13T15:30:00Z
```

## When to Use

- When analysis reveals a pattern not obvious from any single source
- When connecting findings across multiple research threads yields new understanding
- When a gap in existing knowledge or literature becomes apparent
- When research uncovers implications beyond the original question scope
