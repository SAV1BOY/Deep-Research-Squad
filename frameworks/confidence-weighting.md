# Confidence Weighting Framework

## Purpose
Assign rigorous, reproducible confidence scores to research claims by evaluating
multiple factors systematically. This replaces vague qualifiers ("probably,"
"likely") with calibrated numerical scores that can be aggregated, compared,
and communicated precisely.

## When to Use
- Reporting findings that vary in certainty.
- Comparing competing claims on the same topic.
- Deciding whether a claim is reliable enough to act on.
- Aggregating conclusions from multiple sub-questions.
- Communicating uncertainty transparently to stakeholders.

## Inputs
- A specific claim to evaluate.
- Available evidence and its sources.
- Evidence Ladder classification of supporting evidence.
- Information about source authority and methodology.

## Process

### Step 1: Evaluate Individual Factors
Score each factor on a 0.0-1.0 scale:

**Factor 1: Source Authority (SA)**
- 0.1-0.2: Anonymous, unverifiable, or known-unreliable source.
- 0.3-0.4: Non-expert individual or informal publication.
- 0.5-0.6: Credentialed professional or reputable organization.
- 0.7-0.8: Domain expert or leading institution.
- 0.9-1.0: Preeminent authority with track record in this specific area.

**Factor 2: Evidence Strength (ES)**
- Map directly from Evidence Ladder rung weights.
- Rung 1-2: 0.05-0.15 | Rung 3-4: 0.15-0.35 | Rung 5-6: 0.30-0.70
- Rung 7-8: 0.65-0.90 | Rung 9: 0.85-0.95

**Factor 3: Corroboration Count (CC)**
- 0.1-0.2: Single source, no corroboration.
- 0.3-0.4: Two sources in agreement.
- 0.5-0.6: Three sources from different classes.
- 0.7-0.8: Multiple independent sources with convergent findings.
- 0.9-1.0: Broad independent corroboration across methods and contexts.

**Factor 4: Recency (RE)**
- 0.1-0.3: Information is outdated; field has evolved significantly.
- 0.4-0.6: Information is older but field is stable; likely still valid.
- 0.7-0.8: Information is recent and current.
- 0.9-1.0: Information is very recent with no superseding developments.
- Note: For timeless facts (mathematics, historical events), default to 0.8.

**Factor 5: Methodology Quality (MQ)**
- 0.1-0.2: No discernible methodology; assertion without process.
- 0.3-0.4: Informal or ad-hoc methodology with significant gaps.
- 0.5-0.6: Reasonable methodology with some limitations noted.
- 0.7-0.8: Rigorous methodology with peer review or equivalent scrutiny.
- 0.9-1.0: Gold-standard methodology (RCT, formal verification, etc.).

### Step 2: Calculate Weighted Confidence Score
Default weights (adjust per domain):
- Source Authority: 15%
- Evidence Strength: 30%
- Corroboration Count: 25%
- Recency: 10%
- Methodology Quality: 20%

Formula: CS = (SA x 0.15) + (ES x 0.30) + (CC x 0.25) + (RE x 0.10) + (MQ x 0.20)

### Step 3: Apply Confidence Band
- **Low (0.1-0.3)**: Claim is speculative. Present as hypothesis only.
- **Medium (0.4-0.6)**: Claim has partial support. Present with caveats.
- **High (0.7-0.9)**: Claim is well-supported. Present as finding with confidence noted.
- **Very High (0.9-1.0)**: Claim is robustly established. Present as established fact.

### Step 4: Aggregation Rules for Multiple Claims
- **Independent claims**: Average the individual scores.
- **Dependent chain**: Multiply scores (confidence drops with chain length).
- **Contradictory claims**: Report both scores; do not average.
- **Corroborating claims**: Take the highest score, add 10% of each additional
  corroborating score (cap at 0.95).

## Outputs
- Numerical confidence score (0.0-1.0) for each claim.
- Factor breakdown showing which factors contribute most.
- Confidence band classification (Low / Medium / High / Very High).
- Aggregated scores for composite conclusions.
- Explicit statement of what would raise or lower the score.

## Common Pitfalls
- **False precision**: A score of 0.73 vs 0.74 is meaningless. Use bands,
  not exact decimals, for communication.
- **Authority bias**: Overweighting source authority when evidence is weak.
  A famous expert's opinion is still an opinion.
- **Stale recency scores**: Failing to update recency as time passes.
  Recency should be re-evaluated periodically.
- **Corroboration double-counting**: Sources that cite each other are not
  independent. Verify true independence before counting.
- **Ignoring low scores**: A single low-factor score can indicate a fatal
  flaw regardless of other scores. Review any factor below 0.3.

## Related Frameworks
- **Evidence Ladder**: Provides the evidence strength factor input.
- **Source Triangulation**: Informs the corroboration count factor.
- **Claim-to-Evidence Chain**: Each link in the chain receives its own score.
- **Contradiction Mapping**: Handles cases where confidence must account for disputes.

## Templates

### Confidence Score Card
```
CLAIM: [Precise statement]

| Factor               | Score | Weight | Weighted |
|----------------------|-------|--------|----------|
| Source Authority      | [0-1] | 0.15   | [calc]   |
| Evidence Strength    | [0-1] | 0.30   | [calc]   |
| Corroboration Count  | [0-1] | 0.25   | [calc]   |
| Recency              | [0-1] | 0.10   | [calc]   |
| Methodology Quality  | [0-1] | 0.20   | [calc]   |

CONFIDENCE SCORE: [sum]
CONFIDENCE BAND: [Low | Medium | High | Very High]
KEY LIMITING FACTOR: [Which factor is lowest and why]
TO INCREASE CONFIDENCE: [What evidence would raise the score]
```
