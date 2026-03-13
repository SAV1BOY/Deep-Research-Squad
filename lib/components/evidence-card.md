# Evidence Card Component

## Purpose

Documents a discrete piece of evidence gathered during research, linking it to
claims it supports or refutes and providing structured strength assessment.

## Structure

```yaml
evidence_card:
  id: string                    # Unique evidence identifier (e.g., EV-001)
  description: string           # What this evidence shows
  evidence_type: string         # empirical | anecdotal | statistical | expert-opinion | experimental
  source_id: string             # Source card this evidence comes from
  claim_ids: list[string]       # Claims this evidence relates to
  relationship: string          # supports | refutes | qualifies | neutral
  strength: float               # 0.0 to 1.0 (see evidence-strength-rubric)
  methodology: string           # How the evidence was produced
  sample_size: string           # If applicable, the sample size or scope
  reproducibility: string       # reproducible | partially | not-tested | not-reproducible
  date_of_evidence: date        # When the evidence was generated
  context: string               # Conditions or environment of the evidence
  limitations: list[string]     # Known limitations of this evidence
  raw_data_available: boolean   # Whether underlying data can be accessed
  excerpt: string               # Key quote or data point
```

## Usage Example

```yaml
evidence_card:
  id: EV-033
  description: "Benchmark showing Redis Cluster failover timing"
  evidence_type: experimental
  source_id: SRC-042
  claim_ids: [CLM-017]
  relationship: supports
  strength: 0.78
  methodology: "Controlled test with 5-node cluster, simulated node failure"
  sample_size: "100 failover events over 48 hours"
  reproducibility: reproducible
  date_of_evidence: 2025-11-20
  context: "AWS EC2 instances, same availability zone, moderate load"
  limitations:
    - "Single cloud provider"
    - "Did not test cross-AZ latency impact"
  raw_data_available: true
  excerpt: "Median failover time: 1.4s, p99: 1.9s across 100 events"
```

## When to Use

- When capturing specific data points, benchmarks, or observations
- When building evidence chains to support or refute claims
- When the strength and quality of evidence needs formal assessment
- During contradiction resolution to weigh competing evidence
- When an audit trail of evidence is required for the final deliverable
