# Research Brief Component

## Purpose

A reusable building block for generating structured research briefs. Encapsulates
the standard sections, formatting rules, and quality gates that every research brief
must satisfy regardless of topic or audience.

## Interface

```yaml
research_brief:
  inputs:
    topic: string                  # Research question or topic
    audience: string               # Target reader (e.g., "C-suite", "technical lead")
    urgency: string                # routine | expedited | urgent
    depth: string                  # scan | analysis | deep-dive
    max_length: string             # "1 page" | "3 pages" | "full report"
  outputs:
    brief: structured_document     # The formatted research brief
    confidence: float              # Overall confidence score (0-1.0)
    source_count: integer          # Number of sources used
    gaps: list[string]             # Identified knowledge gaps
```

## Required Sections

### 1. Header Block
- Topic (specific, not generic)
- Date of analysis
- Confidence score (0-100)
- Audience designation
- Shelf life (when this analysis expires)

### 2. Bottom Line Up Front (BLUF)
- 2-3 sentences maximum
- States the answer, confidence, and primary implication
- Written for the designated audience level

### 3. Key Findings
- 3-7 findings, each as: **Claim** + Evidence + Confidence
- Ordered by importance to the decision, not by topic
- Each finding must cite at least one source

### 4. Evidence Quality Summary
- Source count and diversity
- Contradictions noted (if any)
- Strongest and weakest evidence identified

### 5. Recommendations
- Numbered, tied to specific findings
- Each actionable within the audience's authority

### 6. Knowledge Gaps
- What could not be determined
- What additional research would resolve

## Formatting Rules

| Element | Rule |
|---------|------|
| Confidence scores | Always 0-100 integer, never qualitative alone |
| Claims | Declarative sentences, no hedging language |
| Sources | Inline citation format: (Source, Date; confidence: X) |
| Recommendations | Start with action verb |
| Gaps | Framed as questions, not statements |

## Quality Gates

- [ ] BLUF is comprehensible without reading the rest of the brief
- [ ] Every claim has at least one cited source
- [ ] Confidence score is justified, not arbitrary
- [ ] Recommendations are within audience's decision authority
- [ ] Knowledge gaps section is present and non-empty
- [ ] Brief fits within specified max_length

## Usage Example

```
research_brief:
  topic: "Impact of EU Carbon Border Adjustment Mechanism on steel imports"
  audience: "VP Supply Chain"
  urgency: "expedited"
  depth: "analysis"
  max_length: "3 pages"
```

## Dependencies
- `confidence-scoring` utility for score calculation
- `citation-formatting` utility for source formatting
- `source-card` component for source documentation
