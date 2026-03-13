# Claim Card Component

## Purpose

Tracks a specific factual claim encountered during research, linking it to its
sources, supporting evidence, and verification status for rigorous fact-tracking.

## Structure

```yaml
claim_card:
  id: string                     # Unique claim identifier (e.g., CLM-001)
  claim_text: string             # The claim stated clearly and precisely
  category: string               # factual | statistical | causal | predictive | opinion
  source_ids: list[string]       # Source cards where this claim appears
  first_encountered: datetime    # When the claim was first found
  status: string                 # unverified | supported | contested | refuted | uncertain
  confidence: float              # 0.0 to 1.0
  supporting_evidence: list[string]  # Evidence card IDs that support
  contradicting_evidence: list[string] # Evidence card IDs that contradict
  scope: string                  # Universal applicability or conditional
  conditions: list[string]       # Conditions under which the claim holds
  verification_method: string    # How the claim was or should be verified
  impact_if_wrong: string        # high | medium | low
  notes: string                  # Additional context or researcher notes
```

## Usage Example

```yaml
claim_card:
  id: CLM-017
  claim_text: "Redis Cluster supports automatic failover in under 2 seconds"
  category: factual
  source_ids: [SRC-042, SRC-051]
  first_encountered: 2026-03-13T10:30:00Z
  status: supported
  confidence: 0.82
  supporting_evidence: [EV-033, EV-041]
  contradicting_evidence: [EV-048]
  scope: "Applies to Redis 7.x+ with default sentinel configuration"
  conditions:
    - "Cluster has minimum 3 master nodes"
    - "Network partition is clean (not partial)"
  verification_method: "Cross-referenced official docs with third-party benchmarks"
  impact_if_wrong: high
  notes: "One source reports higher failover times under heavy write load"
```

## When to Use

- When a specific factual assertion needs tracking across the research lifecycle
- When multiple sources make the same or conflicting claims
- When the accuracy of a claim is critical to downstream decisions
- During synthesis to identify which claims are well-supported vs. speculative
- When building argument chains that depend on foundational facts
