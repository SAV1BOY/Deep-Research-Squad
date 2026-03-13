# Signal vs Noise Framework

## Purpose
A systematic method for separating meaningful information (signal) from irrelevant, misleading, or random data (noise). Prevents research conclusions from being built on unreliable foundations by classifying and weighting every data point before it enters synthesis.

## When to Use
- During evidence collection and validation (Research Stack Layer 2, RalphLoop R7-R8)
- When confronted with large volumes of data from mixed-quality sources
- When a finding seems surprising — determine if it is genuine signal or noise artifact
- Before any data point influences a conclusion
- When sources conflict and you need to decide which to trust

## Inputs
- Raw data points, claims, or observations from research
- Source metadata (origin, reliability, recency, independence)
- Base rate information for the domain
- Known biases and incentive structures of sources

## Process (step-by-step)

### Step 1: Catalogue Data Points
List every data point, claim, or observation individually. For each, record:
- The specific claim or observation
- The source and its characteristics
- The date of the observation
- How the data was obtained (methodology)

### Step 2: Apply Signal Indicators
Evaluate each data point against signal indicators. More indicators = higher signal probability.

**Consistency Across Sources**
Does this data point appear in multiple independent sources?
- 3+ independent sources: Strong signal indicator
- 2 independent sources: Moderate signal indicator
- 1 source only: Weak — could be signal or noise

**Corroboration by Different Methods**
Is the finding supported by different methodologies?
- Multiple methods converge: Strong signal indicator
- Single method, replicated: Moderate signal indicator
- Single method, single instance: Weak

**Mechanism Explanation**
Is there a plausible causal mechanism?
- Known and well-understood mechanism: Strong signal indicator
- Plausible but untested mechanism: Moderate signal indicator
- No known mechanism: Noise indicator (extraordinary claims need extraordinary evidence)

**Base Rate Alignment**
Is the finding consistent with known base rates?
- Consistent with base rates: Neutral (expected)
- Moderate deviation from base rates: Warrants investigation
- Extreme deviation from base rates: Likely noise unless very strong evidence

**Predictive Track Record**
Has the source or method successfully predicted outcomes before?
- Strong track record: Signal indicator
- No track record: Neutral
- Poor track record: Noise indicator

### Step 3: Apply Noise Indicators
Evaluate each data point against noise indicators. More indicators = higher noise probability.

**Single Source Dependency**
The claim comes from exactly one source with no independent corroboration.

**No Mechanism**
No plausible explanation for why the claim would be true. Correlation without causation.

**Outlier Status**
The data point is a statistical outlier relative to the rest of the dataset.

**Source Bias**
The source has a known incentive to present the data in a particular way (financial, ideological, reputational).

**Recency Bias Trigger**
The data is recent and emotionally vivid, which may cause it to be overweighted relative to its actual diagnostic value.

**Cherry-Picking Indicators**
The data point was selected from a larger set where most other points tell a different story.

**Unfalsifiable Framing**
The claim is structured so that no possible evidence could disprove it.

### Step 4: Classify Each Data Point
Based on the signal and noise indicators, assign each data point a classification:

- **Strong Signal:** Multiple signal indicators, no noise indicators. Use with high confidence.
- **Probable Signal:** Several signal indicators, minor noise concerns. Use with moderate confidence.
- **Ambiguous:** Mixed signal and noise indicators. Investigate further before using. Do not build conclusions on ambiguous data.
- **Probable Noise:** Several noise indicators, weak signal support. Exclude unless additional evidence arrives.
- **Strong Noise:** Multiple noise indicators, no signal support. Exclude from analysis.

### Step 5: Weight by Signal Strength
Assign weights for synthesis:
- Strong Signal: Full weight in analysis
- Probable Signal: Reduced weight, note the caveat
- Ambiguous: Quarantine — do not include in conclusions, flag for further research
- Probable Noise: Exclude, document why
- Strong Noise: Exclude, document why

### Step 6: Filter and Document
Produce two outputs:
1. The filtered dataset containing only Strong and Probable Signal data points
2. A noise log documenting every excluded data point and the reason for exclusion

## Outputs
- Classified dataset with signal/noise ratings for every data point
- Filtered evidence set ready for synthesis
- Noise log with exclusion rationale (audit trail)
- List of ambiguous data points requiring further investigation
- Confidence assessment of the filtered dataset's overall reliability

## Common Pitfalls
- Treating all data equally — not all data points deserve equal weight
- Dismissing inconvenient data as noise without checking signal indicators first
- Treating quantity of sources as quality — ten articles citing the same original source is still single-source
- Ignoring base rates when evaluating surprising findings
- Keeping ambiguous data in the analysis rather than quarantining it
- Filtering so aggressively that genuine weak signals are lost — balance rigor with openness
- Not documenting exclusions — makes the filtering process unauditable

## Related Frameworks
- bayesian-updating.md (signal strength maps to likelihood ratios for belief updating)
- research-stack.md (signal/noise filtering is core to the Validation layer)
- ralphloop-deepresearch.md (used in R7: Collect Evidence and R8: Verify Claims)
- epistemic-humility-framework.md (ambiguous data should be classified at lower confidence levels)

## Templates (recommended)

### Data Point Classification Card
```
Data Point: [claim or observation]
Source: [reference]
Date: [when observed]
Methodology: [how obtained]

Signal Indicators Present: [list]
Noise Indicators Present: [list]
Classification: [Strong Signal / Probable Signal / Ambiguous / Probable Noise / Strong Noise]
Weight for Synthesis: [Full / Reduced / Quarantined / Excluded]
Rationale: [brief explanation]
```

### Noise Log Entry
```
Excluded Data Point: [description]
Source: [reference]
Noise Indicators: [which ones triggered]
Reason for Exclusion: [explanation]
Reconsider If: [what new evidence would change this classification]
```
