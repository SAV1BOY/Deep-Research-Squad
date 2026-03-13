# Script: Compress Executive Summary

## Purpose

Takes a full research deliverable and compresses it into a tight executive
summary. The goal is maximum information density — every word must earn
its place. A busy executive should get the full picture in under 2 minutes.

## Trigger

Called as the final step before delivering any research output that exceeds
2 pages.

## Inputs

- `full_report`: The complete research deliverable
- `target_length`: Maximum word count for summary (default: 300 words)
- `audience`: Who will read this (role, context)
- `decision_context`: What decision this informs (if applicable)

## Process

### Step 1: Extract Core Elements
From the full report, identify:
- **The answer**: What is the bottom line? (1-2 sentences max)
- **Key findings**: Top 3-5 findings by importance (not by order in report)
- **Confidence**: Overall confidence level
- **Key risk**: The single biggest risk or uncertainty
- **Recommendation**: What should be done (if applicable)

### Step 2: Apply BLUF Structure
Write Bottom Line Up Front:
1. First sentence: The answer to the research question
2. Second sentence: The confidence level and key qualifier
3. Third sentence: The most important implication

### Step 3: Compress Findings
For each key finding, compress to one line:
- Format: "[Claim] ([evidence quality indicator], confidence: [score])"
- Delete all supporting detail — it lives in the full report
- Keep only the number that matters most

### Step 4: Apply Compression Rules

**Delete**:
- Background the reader already knows
- Methodology details (reference full report)
- Hedging language that doesn't add information
- Adjectives that don't change meaning
- Any sentence the reader could guess from context

**Keep**:
- Specific numbers and data points
- Surprising or counterintuitive findings
- Decision-relevant risks and uncertainties
- Clear recommendations with rationale

### Step 5: Readability Check
- Every sentence < 25 words
- No paragraph > 3 sentences
- Active voice throughout
- Zero jargon without definition
- One idea per sentence

### Step 6: Final Test
Read the summary aloud. If any sentence requires re-reading, rewrite it.
Time yourself reading it. Must be under 2 minutes.

## Output Template

```
EXECUTIVE SUMMARY
=================
[BLUF: 2-3 sentences]

Key Findings:
1. [Compressed finding + confidence]
2. [Compressed finding + confidence]
3. [Compressed finding + confidence]

Key Risk: [One sentence]
Recommendation: [One sentence]

Confidence: [Overall score] | Sources: [Count] | Diversity: [Score]
Full report: [Reference]
```

## Quality Checks

- [ ] BLUF answers the question in first sentence
- [ ] Under target word count
- [ ] Readable in under 2 minutes
- [ ] No finding without confidence score
- [ ] Key risk explicitly stated
- [ ] Links to full report for detail
