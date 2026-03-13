# Evidence Ladder Framework

## Purpose
Classify evidence by strength on a defined hierarchy, enabling consistent
evaluation of how much weight to assign any given piece of evidence. This
prevents treating all sources as equally authoritative and provides clear
rules for when evidence is sufficient versus when corroboration is needed.

## When to Use
- Evaluating whether a claim is adequately supported.
- Comparing conflicting claims backed by different evidence types.
- Deciding whether additional research is needed.
- Communicating the strength of findings to others.
- Prioritizing which sources to seek during research.

## Inputs
- A claim or set of claims to evaluate.
- Available evidence supporting or contradicting each claim.
- Context about the domain (medical, social, technical, etc.).

## Process

### Step 1: Collect All Evidence
- Gather every piece of evidence related to the claim.
- Note the source, date, and context of each piece.

### Step 2: Classify Each Piece on the Ladder
Assign each piece of evidence to its rung, from weakest to strongest:

**Rung 1 - Opinion (Weight: 0.05-0.10)**
- Definition: Personal belief without systematic backing.
- Sufficient alone: Never. Opinions indicate areas worth investigating.
- Needs corroboration: Always, from Rung 4 or higher.

**Rung 2 - Anecdote (Weight: 0.10-0.15)**
- Definition: Individual experience or isolated example.
- Sufficient alone: Never. Anecdotes illustrate but do not prove.
- Needs corroboration: Always, from Rung 4 or higher.

**Rung 3 - Case Study (Weight: 0.15-0.25)**
- Definition: Detailed examination of a single instance or small set.
- Sufficient alone: Only for existence proofs ("it is possible").
- Needs corroboration: For any generalizable claim.

**Rung 4 - Survey Data (Weight: 0.20-0.35)**
- Definition: Systematic collection of self-reported data across a population.
- Sufficient alone: For claims about opinions, preferences, or prevalence.
- Needs corroboration: For causal claims or objective measurements.

**Rung 5 - Observational Study (Weight: 0.30-0.45)**
- Definition: Systematic observation without intervention or control groups.
- Sufficient alone: For correlational claims with strong effect sizes.
- Needs corroboration: For causal claims. Confounders limit conclusions.

**Rung 6 - Controlled Experiment (Weight: 0.50-0.70)**
- Definition: Study with intervention, control group, and randomization.
- Sufficient alone: For narrow causal claims within experimental conditions.
- Needs corroboration: For broad generalization beyond study context.

**Rung 7 - Systematic Review (Weight: 0.65-0.80)**
- Definition: Comprehensive, methodical synthesis of all relevant studies.
- Sufficient alone: For well-defined empirical questions with adequate literature.
- Needs corroboration: When review scope is limited or field is rapidly evolving.

**Rung 8 - Meta-Analysis (Weight: 0.75-0.90)**
- Definition: Statistical aggregation of results across multiple studies.
- Sufficient alone: For quantitative claims where included studies are high quality.
- Needs corroboration: When heterogeneity across studies is high.

**Rung 9 - Scientific Consensus (Weight: 0.85-0.95)**
- Definition: Broad agreement among domain experts supported by extensive evidence.
- Sufficient alone: For established empirical questions in mature fields.
- Needs corroboration: When consensus is recent, narrow, or politically influenced.

### Step 3: Assess Overall Evidence Strength
- Identify the highest rung reached.
- Count how many independent pieces of evidence exist at each rung.
- Apply the sufficiency rules: is the highest rung sufficient for the claim type?
- Check for contradictory evidence at equal or higher rungs.

### Step 4: Determine Verdict
- **Well-supported**: Rung 6+ evidence with corroboration and no higher contradictions.
- **Moderately supported**: Rung 4-5 evidence or single Rung 6 without replication.
- **Weakly supported**: Only Rung 1-3 evidence available.
- **Contested**: Contradictory evidence at similar rungs.
- **Insufficient**: No relevant evidence found.

## Outputs
- Evidence classification table mapping each piece to its rung.
- Overall strength assessment for each claim.
- Gaps identified (rungs where evidence is missing but obtainable).
- Verdict with justification.

## Common Pitfalls
- **Rung inflation**: Treating a well-written opinion as if it were a study.
  Always classify by methodology, not by presentation quality.
- **Ignoring context**: A controlled experiment in one domain may not transfer.
  Consider external validity alongside the rung.
- **Quantity over quality**: Ten anecdotes do not equal one controlled experiment.
  The ladder measures type of evidence, not volume.
- **Consensus appeal**: Scientific consensus is strong but not infallible.
  Note when consensus is evolving or contested within the field.
- **Recency bias**: Older high-rung evidence may outweigh newer low-rung evidence.
  Evaluate methodology before recency.

## Related Frameworks
- **Confidence Weighting**: Translates evidence ladder positions into numerical scores.
- **Claim-to-Evidence Chain**: Uses ladder rungs as the strength rating component.
- **Source Triangulation**: Complements by requiring independence across sources.
- **Contradiction Mapping**: Applies when evidence at similar rungs conflicts.

## Templates

### Evidence Classification Table
```
CLAIM: [Statement being evaluated]

| # | Evidence Description | Source | Rung | Weight | Notes |
|---|---------------------|--------|------|--------|-------|
| 1 | [Description]       | [Src]  | [1-9]| [0-1]  | [Context] |
| 2 | [Description]       | [Src]  | [1-9]| [0-1]  | [Context] |

HIGHEST RUNG REACHED: [N]
CONTRADICTIONS: [Yes/No - details]
VERDICT: [Well-supported | Moderately supported | Weakly supported | Contested | Insufficient]
JUSTIFICATION: [Why this verdict]
```
