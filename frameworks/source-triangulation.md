# Source Triangulation Framework

## Purpose
Verify critical claims by requiring confirmation from three or more independent
sources or methods. Triangulation reduces the risk of accepting claims that
are only supported by a single perspective, methodology, or data stream,
which may carry undetected biases or errors.

## When to Use
- A claim is critical to the research conclusion.
- A single source provides the only support for an important finding.
- The topic is controversial, politically charged, or commercially motivated.
- High-stakes decisions depend on the accuracy of the claim.
- Initial evidence comes from a source with potential conflicts of interest.

## Inputs
- The specific claim requiring triangulation.
- Initial source(s) and evidence already gathered.
- Domain context to identify appropriate source classes.
- Required confidence threshold for the claim.

## Process

### Step 1: Identify the Claim
- State the claim precisely. Vague claims cannot be triangulated.
- Determine the claim type: factual, statistical, causal, or predictive.
- Assess the criticality: how much does the overall finding depend on this claim?
- Set the triangulation threshold: how many independent confirmations are needed?
  Default minimum is 3 for critical claims, 2 for supporting claims.

### Step 2: Define Source Classes
Sources must come from different classes to count as independent. Classes include:

**By Origin**
- Academic/peer-reviewed research.
- Government or regulatory data.
- Industry reports and filings.
- Journalism and investigative reporting.
- Domain expert testimony.
- Primary data or direct observation.

**By Geography**
- Sources from different countries or regions reduce cultural bias.

**By Institutional Affiliation**
- Sources from different organizations avoid institutional groupthink.

**By Funding/Motivation**
- Sources with different financial incentives reduce commercial bias.

### Step 3: Find Sources from Different Classes
- Search for evidence across at least 3 distinct source classes.
- Prioritize classes with the least overlap in methodology and motivation.
- Document which class each source belongs to.
- If a source class yields no evidence, document the gap.

### Step 4: Verify Independence
For each pair of sources, verify they are truly independent:
- Do they cite each other? (If yes, they are not independent.)
- Do they share a common upstream source? (Trace citation chains.)
- Were they produced by the same team, institution, or funder?
- Do they use the same dataset or methodology?
- Were they produced in response to the same event or prompt?

Sources that fail independence checks count as a single source, not multiple.

### Step 5: Assess Convergence
Rate the degree of agreement across independent sources:

**Strong Convergence**
- All independent sources agree on the claim's substance.
- Minor variations in framing or precision, but no material differences.
- Confidence boost: claim receives a corroboration factor of 0.8-1.0.

**Partial Convergence**
- Most sources agree, but one or more disagree on specifics.
- Core claim is supported, but details or scope are contested.
- Confidence adjustment: corroboration factor of 0.5-0.7.
- Action: investigate the disagreement using Contradiction Mapping.

**Divergence**
- Sources materially disagree on the claim.
- No clear majority position, or methodological differences explain the split.
- Confidence reduction: corroboration factor of 0.1-0.4.
- Action: do not present claim as established. Report as contested.

**No Triangulation Possible**
- Fewer than the required number of independent sources exist.
- The claim rests on a single source or closely related sources.
- Action: flag as untriangulated. Downgrade claim language accordingly.

### Step 6: Document Triangulation Results
- Record all sources consulted, their classes, and independence verification.
- State the convergence level and its impact on claim confidence.
- Note any source classes that were unavailable or inaccessible.

## Types of Triangulation

**Source Triangulation** (most common)
- Same claim confirmed by different sources.

**Method Triangulation**
- Same claim confirmed by different research methods (e.g., survey + experiment).

**Investigator Triangulation**
- Same claim confirmed by different researchers or teams independently.

**Temporal Triangulation**
- Same claim confirmed across different time periods, showing stability.

The strongest triangulation combines multiple types: different sources using
different methods at different times reach the same conclusion.

## Outputs
- Triangulation matrix mapping claims to independent sources.
- Independence verification for each source pair.
- Convergence rating for each triangulated claim.
- Adjusted confidence score reflecting triangulation results.
- List of claims that could not be triangulated with reasons.

## Common Pitfalls
- **Echo chamber sources**: Sources that all trace back to one original report.
  Always trace citation chains to verify true independence.
- **Class confusion**: Two news articles are the same source class, not two
  independent classes. Diversity of class matters more than quantity.
- **Availability bias**: Concluding triangulation is impossible when you have
  only searched familiar source types. Expand to unfamiliar classes.
- **Threshold inflation**: Requiring excessive triangulation for minor claims
  wastes research effort. Scale requirements to claim criticality.
- **Ignoring disconfirmation**: Triangulation that reveals divergence is still
  valuable. It tells you the claim is contested, which is important to report.

## Related Frameworks
- **Evidence Ladder**: Classifies the strength of each triangulated source.
- **Contradiction Mapping**: Handles cases where triangulation reveals disagreement.
- **Confidence Weighting**: Triangulation directly affects the corroboration factor.
- **Claim-to-Evidence Chain**: Triangulated sources strengthen individual chains.

## Templates

### Triangulation Matrix
```
CLAIM: [Precise statement]
CRITICALITY: [High | Medium | Low]
REQUIRED SOURCES: [N]

| # | Source | Class | Independent? | Supports Claim? | Strength |
|---|--------|-------|-------------|-----------------|----------|
| 1 | [Name] | [Class] | Baseline   | [Yes/No/Partial]| Rung [N] |
| 2 | [Name] | [Class] | [Yes/No]   | [Yes/No/Partial]| Rung [N] |
| 3 | [Name] | [Class] | [Yes/No]   | [Yes/No/Partial]| Rung [N] |

CONVERGENCE: [Strong | Partial | Divergence | Not possible]
TRIANGULATION TYPES: [Source | Method | Investigator | Temporal]
ADJUSTED CONFIDENCE: [0.0-1.0]
NOTES: [Key observations or gaps]
```
