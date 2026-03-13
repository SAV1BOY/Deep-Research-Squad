# Script: Create Evidence Table

## Purpose

Builds a structured evidence table for a specific claim or research question.
Organizes all evidence systematically to make the strength of conclusions
transparent and auditable.

## Trigger

Called when evidence needs to be organized for a specific claim or finding
within a research deliverable.

## Inputs

- `claim`: The specific claim being evaluated
- `sources`: List of sources from the source map
- `confidence_threshold`: Minimum confidence required

## Process

### Step 1: Decompose the Claim
Break compound claims into individually testable components:
- Component A: [Testable statement]
- Component B: [Testable statement]
- Component C: [Testable statement]

### Step 2: Evidence Collection per Component
For each component, gather evidence from all available sources:

| # | Source | Type | Grade | Finding | Direction | Confidence | Date | Caveats |
|---|--------|------|-------|---------|-----------|------------|------|---------|

**Direction values**: Supports / Contradicts / Partial / Neutral
**Grade values**: A (peer-reviewed, replicated) through F (unverified)

### Step 3: Evidence Grading
Apply grading criteria:
- **A**: Peer-reviewed, large sample, replicated results
- **B**: Peer-reviewed OR large sample, single study
- **C**: Credible institutional source, methodology disclosed
- **D**: Self-reported, potential bias, small sample
- **F**: Unverified, anonymous, or conflicted source

### Step 4: Synthesis
For each component and the overall claim:
- Count sources by direction (supporting/contradicting/partial)
- Weight by grade (A sources outweigh D sources)
- Calculate overall confidence score
- Identify the strongest evidence on each side

### Step 5: Confidence Scoring

```
Confidence Score Calculation:
- Base: Proportion of supporting vs contradicting evidence
- Modifier +: High-grade sources, large samples, replication
- Modifier -: Conflicting evidence, low-grade sources, small samples
- Modifier -: Missing evidence types, low source diversity
- Final: 0-100 scale
```

### Step 6: Gap Identification
- What evidence is missing that would strengthen or weaken the claim?
- What methodology would be needed to close the gap?
- Is the gap addressable within the research timeline?

## Output Template

```
EVIDENCE TABLE
==============
Claim: [Specific claim]
Overall Confidence: [0-100]
Verdict: [Confirmed/Likely True/Mixed/Likely False/False/Unverifiable]

[Table from Step 2]

Synthesis:
- Supporting: [Count] sources (grades: [list])
- Contradicting: [Count] sources (grades: [list])
- Key gap: [Description]

Confidence Justification: [2-3 sentences]
```

## Quality Checks

- [ ] Claim is specific and falsifiable
- [ ] All available evidence included (not cherry-picked)
- [ ] Contradicting evidence explicitly addressed
- [ ] Confidence score justified with reasoning
- [ ] Gaps identified and documented
