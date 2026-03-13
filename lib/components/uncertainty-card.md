# Uncertainty Card Component

## Purpose

Explicitly documents areas of uncertainty in the research, including what is unknown,
why it matters, and what could reduce the uncertainty. Prevents false confidence.

## Structure

```yaml
uncertainty_card:
  id: string                    # Unique identifier (e.g., UNC-001)
  title: string                 # Brief description of the uncertainty
  category: string              # data-gap | conflicting-evidence | methodological | scope-limit
  severity: string              # critical | significant | minor
  status: string                # open | mitigated | accepted | resolved
  description: string           # Detailed explanation of what is uncertain
  affected_claims: list[string] # Claim card IDs affected by this uncertainty
  affected_decisions: list[string] # Decision card IDs at risk
  root_cause: string            # Why this uncertainty exists
  impact_assessment: string     # What happens if this uncertainty is not resolved
  mitigation_options:
    - action: string            # What could reduce this uncertainty
      effort: string            # low | medium | high
      expected_reduction: float # How much confidence would improve (0.0 to 1.0)
  current_assumption: string    # What we are assuming in the absence of certainty
  assumption_risk: string       # What happens if the assumption is wrong
  owner: string                 # Who is responsible for tracking this
  deadline: datetime            # By when should this be resolved
```

## Usage Example

```yaml
uncertainty_card:
  id: UNC-004
  title: "Unknown performance under cross-region replication"
  category: data-gap
  severity: critical
  status: open
  description: >
    No benchmarks found for ClickHouse cross-region replication latency
    under our projected write volume of 500K events/second.
  affected_claims: [CLM-017, CLM-031]
  affected_decisions: [DEC-005]
  root_cause: "No public benchmarks exist for this specific configuration"
  impact_assessment: "Could invalidate database selection if latency exceeds SLA"
  mitigation_options:
    - action: "Run proof-of-concept benchmark in staging environment"
      effort: medium
      expected_reduction: 0.7
    - action: "Contact ClickHouse vendor for reference architecture review"
      effort: low
      expected_reduction: 0.3
  current_assumption: "Cross-region latency adds <50ms to query time"
  assumption_risk: "If >200ms, may need to reconsider architecture"
  owner: "research-lead"
  deadline: 2026-03-20T00:00:00Z
```

## When to Use

- When research cannot definitively answer a question with available data
- When confidence in a critical claim is below acceptable thresholds
- When decisions must be made despite incomplete information
- When assumptions are being used as stand-ins for verified facts
- To prevent overconfidence in research conclusions
