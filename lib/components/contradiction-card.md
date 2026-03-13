# Contradiction Card Component

## Purpose

Documents a contradiction found between two or more claims or sources during
research, tracking resolution efforts and the final reconciliation outcome.

## Structure

```yaml
contradiction_card:
  id: string                      # Unique identifier (e.g., CONTRA-001)
  title: string                   # Brief description of the contradiction
  severity: string                # critical | significant | minor
  status: string                  # detected | investigating | resolved | unresolvable
  claim_ids: list[string]         # Conflicting claim card IDs
  source_ids: list[string]        # Sources involved in the conflict
  description: string             # Detailed explanation of the contradiction
  possible_explanations:
    - explanation: string         # A potential reason for the conflict
      likelihood: float           # 0.0 to 1.0
      evidence: list[string]      # Evidence card IDs supporting this explanation
  resolution:
    method: string                # How it was resolved (see contradiction-resolution-patterns)
    outcome: string               # The reconciled understanding
    winning_claim_id: string      # Which claim prevailed, if applicable
    confidence: float             # 0.0 to 1.0
    resolved_by: string           # Who or what resolved it
    resolved_date: datetime
  impact_on_research: string      # How this contradiction affects conclusions
  notes: string
```

## Usage Example

```yaml
contradiction_card:
  id: CONTRA-003
  title: "Conflicting Redis failover time reports"
  severity: significant
  status: resolved
  claim_ids: [CLM-017, CLM-023]
  source_ids: [SRC-042, SRC-058]
  description: "Official docs claim sub-2s failover; blog reports 5-8s under load"
  possible_explanations:
    - explanation: "Blog tested under extreme write load exceeding typical use"
      likelihood: 0.75
      evidence: [EV-048, EV-055]
    - explanation: "Blog used older Redis version with different defaults"
      likelihood: 0.20
      evidence: [EV-056]
  resolution:
    method: "contextual-reconciliation"
    outcome: "Both claims valid in their contexts; failover time is load-dependent"
    winning_claim_id: null
    confidence: 0.85
    resolved_by: "analysis-agent"
    resolved_date: 2026-03-13T14:00:00Z
  impact_on_research: "Must qualify failover claims with load conditions"
  notes: "Added load-dependent caveat to final recommendation"
```

## When to Use

- When two or more sources provide conflicting information on the same topic
- When evidence points in opposite directions for a given claim
- When statistical data from different sources does not align
- During synthesis when reconciling diverse perspectives is required
