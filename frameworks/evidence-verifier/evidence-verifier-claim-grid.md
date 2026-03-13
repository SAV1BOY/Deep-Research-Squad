# Claim Grid Framework

## Purpose
Provide a structured grid for tracking, evaluating, and documenting every claim in the research output. Each claim is mapped to its source, evidence type, evidence strength, corroboration status, and overall confidence level. Creates a transparent, auditable evidence base.

## When to Use
- When assembling findings from multiple sources into a coherent evidence base.
- When preparing the final research output and needing to justify confidence levels.
- When reviewing evidence for gaps, weaknesses, or over-reliance on single sources.
- Throughout the research process as claims accumulate.

## Inputs
- Claims extracted from research sources.
- Source metadata (author, publication, date, type).
- Evidence classification from other frameworks (source category, proximity, signal score).

## Process

### Step 1: Extract and State Each Claim Precisely
- Write each claim as a single, specific, falsifiable statement.
- Avoid compound claims. Split "X is true and Y is increasing" into two separate claims.
- Use precise language. Replace "significant" with the actual figure or threshold.
- Number each claim for reference.

### Step 2: Build the Grid Structure

| # | Claim | Source | Evidence Type | Strength | Corroboration | Confidence |
|---|---|---|---|---|---|---|
| 1 | [Precise claim] | [Source ref] | [Type] | [Rating] | [Status] | [Level] |

### Step 3: Classify Evidence Type
For each claim, identify the evidence type:
- **Empirical data**: Statistical data, measurements, experimental results.
- **Expert testimony**: Statements from recognized authorities.
- **Case evidence**: Specific instances or examples.
- **Logical argument**: Reasoning from established principles.
- **Anecdotal**: Individual stories or unverified accounts.
- **Consensus**: Widely accepted position in the field.

### Step 4: Rate Evidence Strength
Rate each piece of evidence on a four-level scale:
- **Strong**: Primary source, empirical data, peer-reviewed, replicable.
- **Moderate**: Credible secondary source, expert analysis, consistent methodology.
- **Weak**: Tertiary source, opinion, anecdotal, single unreplicated finding.
- **Insufficient**: No verifiable source, hearsay, unsubstantiated assertion.

### Step 5: Assess Corroboration
For each claim, document corroboration status:
- **Corroborated**: Multiple independent sources confirm the claim.
- **Partially corroborated**: Some supporting evidence from independent sources but not definitive.
- **Uncorroborated**: Only one source supports the claim.
- **Contested**: Sources actively disagree about this claim.
- Record which specific sources provide corroboration.

### Step 6: Assign Confidence Level
Combine evidence type, strength, and corroboration to assign overall confidence:
- **High confidence**: Strong evidence, corroborated by independent sources, consistent methodology.
- **Moderate confidence**: Moderate evidence, partially corroborated, or strong evidence from a single source.
- **Low confidence**: Weak evidence, uncorroborated, or contested claims with no resolution.
- **Unverified**: Insufficient evidence to assign any confidence level.

### Step 7: Identify Grid Gaps
- Review the completed grid for patterns:
  - Claims with only weak or insufficient evidence.
  - Claims with no corroboration.
  - Clusters of claims all relying on a single source.
  - Contested claims that need resolution.
- Flag these gaps for further investigation or explicit caveats in the output.

### Step 8: Update Continuously
- The claim grid is a living document. Update it as new evidence arrives.
- Upgrade or downgrade confidence as corroboration changes.
- Remove claims that are disproven or no longer relevant.

## Outputs
- A completed claim grid with all columns populated.
- A gap analysis identifying weak points in the evidence base.
- Confidence summary: distribution of claims across confidence levels.
- Flags for claims needing further investigation.

## Common Pitfalls
- Writing vague claims that cannot be meaningfully evaluated.
- Conflating the number of sources with corroboration strength (10 sources citing the same origin is not corroboration).
- Assigning high confidence based on source prestige alone without checking evidence quality.
- Not updating the grid as new evidence emerges.
- Leaving the corroboration column empty because checking is time-consuming.
- Treating all evidence types as equally strong.

## Related Frameworks
- **Ladder Application**: Maps evidence types to the strength rating system.
- **Cross-Source Verification**: Feeds corroboration assessments into the grid.
- **Citation Integrity**: Validates that cited evidence actually supports the claimed strength.
- **Falsification**: Tests whether high-confidence claims survive falsification attempts.
- **Signal-Noise Scoring**: Source quality scores inform the strength and confidence columns.
