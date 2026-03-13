# Claim-to-Evidence Chain Framework

## Purpose
Ensure every claim in a research output is linked to its supporting evidence
through a traceable, auditable chain. This eliminates orphan claims (assertions
without evidence), unsourced facts, and unverifiable conclusions by enforcing
a strict provenance requirement.

## When to Use
- Drafting or reviewing any research output.
- Verifying that conclusions are fully supported before delivery.
- Auditing existing research for unsupported assertions.
- Building arguments that must withstand scrutiny.
- Any time a claim will be presented as a finding or fact.

## Inputs
- All claims made or to be made in the research output.
- Available evidence for each claim.
- Source metadata (author, publication, date, methodology).
- Evidence Ladder classifications.
- Confidence scores from the Confidence Weighting framework.

## Process

### Step 1: Extract All Claims
- Read through the research output and list every assertion of fact,
  every conclusion, and every recommendation.
- Include implicit claims (statements presented as obvious that still need backing).
- Number each claim sequentially for tracking.
- Classify each claim: factual, causal, evaluative, or predictive.

### Step 2: Build the Chain for Each Claim
Every claim must have a complete chain with these links:

**Link 1: Claim**
- The precise statement being asserted.
- Classification: factual, causal, evaluative, or predictive.

**Link 2: Supporting Evidence**
- What specific evidence supports this claim?
- Quote or summarize the evidence precisely.
- Note if evidence is direct (proves claim) or indirect (supports inference).

**Link 3: Source**
- Where does this evidence come from?
- Full citation: author, title, publication, date, URL if applicable.
- Source type: primary data, secondary analysis, expert commentary, etc.

**Link 4: Methodology**
- How was this evidence produced?
- Study design, sample size, data collection method, analysis approach.
- Note methodological limitations acknowledged by the source.

**Link 5: Strength Rating**
- Evidence Ladder rung (1-9).
- Justification for the assigned rung.

**Link 6: Confidence Score**
- Numerical score from the Confidence Weighting framework.
- Confidence band: Low, Medium, High, or Very High.

### Step 3: Validate Chain Integrity
- **No orphan claims**: Every claim must have at least one complete chain.
  If a claim lacks evidence, either find evidence or remove the claim.
- **No unsourced facts**: Every piece of evidence must trace to a verifiable source.
  "Common knowledge" is not a source; find the primary reference.
- **No broken links**: Every link in the chain must be present and connected.
  A claim with evidence but no source is incomplete.
- **Strength proportionality**: Stronger claims require stronger chains.
  Extraordinary claims require extraordinary evidence.

### Step 4: Handle Weak Chains
When a chain is incomplete or weak:
- **Downgrade the claim**: Restate as a hypothesis, speculation, or observation.
- **Add hedging language**: "Evidence suggests..." rather than "X is true."
- **Flag for further research**: Note that additional evidence is needed.
- **Remove if unsupportable**: Better to omit than to assert without basis.

### Step 5: Cross-Reference Chains
- Identify claims that share evidence (potential circular reasoning).
- Check that independent claims have independent evidence.
- Verify that chain conclusions do not contradict each other.
- Ensure aggregate conclusions are supported by the combined chains.

## Outputs
- Numbered claim register with complete chains.
- Orphan claim report (claims lacking evidence, flagged for resolution).
- Chain strength summary (distribution of confidence scores).
- Cross-reference map showing shared evidence between claims.
- Overall research integrity score (percentage of claims with complete chains).

## Common Pitfalls
- **Circular evidence**: Claim A is supported by Source X, which itself cites
  the same claim without independent evidence. Trace to original data.
- **Citation laundering**: A weak source is cited by a stronger outlet, making
  it appear more authoritative. Always check the primary source.
- **Implicit claims**: Statements that read as background or context may contain
  unsupported assertions. Treat every factual statement as a claim.
- **Chain of chains**: Complex claims built on sub-claims need recursive chain
  validation. A chain is only as strong as its weakest link.
- **Excessive hedging**: Over-qualifying every statement makes research useless.
  Use hedging proportionally to actual uncertainty, not as a blanket disclaimer.
- **Source exhaustion**: Spending too long finding evidence for minor claims.
  Prioritize chains for central claims; peripheral claims can have shorter chains.

## Related Frameworks
- **Evidence Ladder**: Provides the strength rating for Link 5.
- **Confidence Weighting**: Provides the confidence score for Link 6.
- **Source Triangulation**: Strengthens chains by requiring multiple source classes.
- **Contradiction Mapping**: Activated when chains for competing claims conflict.
- **Unknowns and Assumptions**: Handles claims that cannot form complete chains.

## Templates

### Claim Chain Template
```
CLAIM #[N]: [Precise statement]
Type: [Factual | Causal | Evaluative | Predictive]

EVIDENCE: [Quote or summary of supporting evidence]
  Direct/Indirect: [Direct proof | Indirect inference]

SOURCE: [Full citation]
  Source type: [Primary data | Secondary analysis | Expert commentary | ...]

METHODOLOGY: [How evidence was produced]
  Limitations: [Noted limitations]

STRENGTH: Rung [1-9] - [Rung name]
CONFIDENCE: [0.0-1.0] - [Low | Medium | High | Very High]

CHAIN STATUS: [Complete | Incomplete - missing: link X]
```

### Research Integrity Summary
```
Total claims: [N]
Complete chains: [N] ([%])
Incomplete chains: [N] ([%])
Orphan claims: [N] (must be resolved)
Average confidence: [0.0-1.0]
Weakest chain: Claim #[N] - [reason]
```
