# Confidence Score Calculator Utility

## Purpose

Computes a standardized confidence score (0-100) for claims, findings, and
recommendations by combining multiple evidence dimensions. Complements the
qualitative `confidence-scoring` rubric with a repeatable calculation method.

## Inputs

```yaml
confidence_calculator:
  inputs:
    evidence_items: list[evidence_card]  # All evidence related to the claim
    source_trust_scores: list[float]     # Trust scores for each source (0-1.0)
    claim_type: string                   # factual | predictive | causal | comparative
    corroboration_count: integer         # Independent sources confirming
    contradiction_count: integer         # Independent sources contradicting
    recency_weight: float               # How much recency matters (0-1.0)
  outputs:
    score: integer                       # 0-100 confidence score
    grade: string                        # A/B/C/D/F letter grade
    breakdown: object                    # Score by dimension
    flags: list[string]                  # Warnings or caveats
```

## Calculation Dimensions

### 1. Evidence Volume (0-20 points)

| Evidence Count | Points |
|---------------|--------|
| 6+ independent items | 16-20 |
| 3-5 independent items | 9-15 |
| 1-2 items | 3-8 |
| 0 (inference only) | 0-2 |

Bonus: +2 if evidence spans multiple types (e.g., statistical + expert + empirical).

### 2. Evidence Quality (0-25 points)

| Quality Level | Points |
|--------------|--------|
| Empirical, reproducible, peer-reviewed | 20-25 |
| Strong methodology, credible sources | 13-19 |
| Moderate — expert opinion, surveys | 7-12 |
| Weak — anecdotal, single-source, unverified | 0-6 |

Uses average `evidence_strength` from evidence cards, mapped to point range.

### 3. Source Trust (0-20 points)

Average of `source_trust_scores`, scaled to 0-20.
```
source_trust_points = mean(source_trust_scores) * 20
```

### 4. Corroboration (0-20 points)

```
corroboration_ratio = corroboration_count / (corroboration_count + contradiction_count)
corroboration_points = corroboration_ratio * 20
```

Special case: If contradiction_count > corroboration_count, cap at 8 points and
flag "majority contradiction."

### 5. Claim Type Modifier (0-15 points)

| Claim Type | Max Points | Rationale |
|-----------|-----------|-----------|
| Factual (verifiable) | 15 | Can be confirmed with certainty |
| Comparative | 12 | Relative assessment, bounded uncertainty |
| Causal | 10 | Requires evidence of mechanism |
| Predictive | 8 | Inherently uncertain, time-dependent |

Points awarded proportionally based on evidence strength for the claim type.

## Score Interpretation

| Score | Grade | Interpretation |
|-------|-------|---------------|
| 85-100 | A | High confidence — suitable for critical decisions |
| 70-84 | B | Good confidence — suitable for most decisions |
| 55-69 | C | Moderate — use with caveats, seek additional evidence |
| 40-54 | D | Low — significant gaps, not decision-ready |
| 0-39 | F | Insufficient — do not use for decisions |

## Automatic Flags

| Condition | Flag |
|-----------|------|
| Score > 80 but single source | "High score relies on single source" |
| Contradiction count > 0 | "Contradictory evidence exists" |
| All sources from same type | "Source type concentration risk" |
| Evidence older than 12 months | "Recency concern — evidence may be stale" |
| Claim is predictive + score > 75 | "Predictive claims rarely warrant high confidence" |
| Score < 40 on critical claim | "Below decision threshold — escalate" |

## Usage Example

```yaml
confidence_calculator:
  evidence_items: [EV-001, EV-003, EV-007, EV-012]
  source_trust_scores: [0.85, 0.72, 0.90, 0.68]
  claim_type: "comparative"
  corroboration_count: 3
  contradiction_count: 1
  recency_weight: 0.7

# Output:
  score: 72
  grade: "B"
  breakdown:
    evidence_volume: 14
    evidence_quality: 18
    source_trust: 16
    corroboration: 15
    claim_type_modifier: 9
  flags: ["Contradictory evidence exists"]
```

## Dependencies
- `evidence-card` component for evidence inputs
- `source-card` component for trust scores
- `confidence-scoring` rubric for qualitative alignment
