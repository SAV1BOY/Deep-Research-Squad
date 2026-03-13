# Script: Confidence Scorer

## Purpose

Calculates a rigorous, transparent confidence score (0-100) for research
claims and findings. Confidence scores prevent false precision and make
the strength of evidence visible to decision-makers.

## Trigger

Called for every claim, finding, or conclusion in a research deliverable.

## Inputs

- `claim`: The specific claim being scored
- `evidence_table`: Evidence supporting and contradicting the claim
- `source_diversity`: Diversity metrics from source map

## Process

### Step 1: Base Score from Evidence Direction
Count evidence by direction:
- Supporting sources: [Count]
- Contradicting sources: [Count]
- Partial/mixed sources: [Count]

Base score = (Supporting / Total) × 70

### Step 2: Quality Modifier (±15 points)
Adjust based on source quality:
- Majority Grade A/B sources: +10 to +15
- Majority Grade C sources: +0 to +5
- Majority Grade D/F sources: -5 to -15
- Mixed quality: Weighted average

### Step 3: Diversity Modifier (±10 points)
Adjust based on source diversity:
- 4+ source types represented: +8 to +10
- 3 source types: +4 to +7
- 2 source types: +0 to +3
- 1 source type: -5 to -10

### Step 4: Contradiction Penalty (-0 to -15 points)
Adjust for contradictions:
- No contradictions: -0
- Minor contradictions resolved: -2 to -5
- Significant contradictions partially resolved: -5 to -10
- Unresolved critical contradictions: -10 to -15

### Step 5: Recency Modifier (±5 points)
Adjust for data freshness:
- All data <6 months old: +5
- Most data <1 year old: +2
- Significant data >2 years old: -3 to -5
- Topic is fast-moving and data is stale: -5

### Step 6: Calculate Final Score

```
Final Score = Base + Quality + Diversity + Contradiction + Recency
Clamp to range [5, 98] — never 0 or 100
```

### Score Interpretation

| Range | Label | Meaning |
|-------|-------|---------|
| 90-98 | Very High | Strong evidence, multiple high-quality sources agree |
| 75-89 | High | Good evidence, minor gaps or contradictions |
| 60-74 | Moderate | Adequate evidence but notable limitations |
| 40-59 | Low | Limited evidence, significant contradictions or gaps |
| 20-39 | Very Low | Minimal evidence, major uncertainty |
| 5-19 | Speculative | Almost no supporting evidence, mostly inference |

## Output Template

```
CONFIDENCE SCORE
================
Claim: [Claim text]
Score: [Final score] ([Label])

Breakdown:
  Base (evidence direction): [score]
  Quality modifier: [modifier]
  Diversity modifier: [modifier]
  Contradiction penalty: [modifier]
  Recency modifier: [modifier]
  ---
  Final: [score]

Justification: [2-3 sentences explaining the score]
What would increase confidence: [1-2 specific evidence gaps]
```

## Calibration Rules

1. Never assign 100 — all knowledge is provisional
2. Never assign 0 — the claim was worth investigating
3. Scores should be calibrated: 80% confidence claims should be right ~80% of the time
4. When in doubt, round down — overconfidence is more dangerous than underconfidence
5. Document reasoning — a score without justification is meaningless
