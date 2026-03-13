# Script: Audit Research Output

## Purpose

Performs a comprehensive quality audit on a research deliverable before
final delivery. This is the last quality gate — it checks for accuracy,
completeness, consistency, and adherence to standards.

## Trigger

Called as the final step before any research deliverable is sent to the
requester.

## Inputs

- `deliverable`: The complete research output
- `research_brief`: Original brief with requirements
- `evidence_tables`: Supporting evidence tables
- `source_map`: Source map used
- `quality_standards`: Reference to authority/standards/

## Process

### Step 1: Completeness Check
Does the deliverable address all requirements?

| Requirement | Addressed? | Section | Quality |
|------------|-----------|---------|---------|
| Core question answered | Yes/No | [Ref] | [1-5] |
| Sub-question 1 | Yes/No | [Ref] | [1-5] |
| Sub-question 2 | Yes/No | [Ref] | [1-5] |
| Format matches spec | Yes/No | — | [1-5] |

### Step 2: Evidence Audit
For each major claim in the deliverable:
- Is it backed by evidence in the evidence table?
- Is the confidence score present and justified?
- Are contradicting sources acknowledged?
- Is the source cited accessible and verifiable?

### Step 3: Consistency Check
Scan for internal contradictions:
- Do findings in different sections agree?
- Do recommendations follow from findings?
- Are confidence scores consistent with evidence quality?
- Do numbers match across sections?

### Step 4: Standards Compliance
Check against authority/standards/:
- [ ] Epistemic standards met (no overclaiming)
- [ ] Source hierarchy respected (appropriate source weighting)
- [ ] Evidence standards met (minimum sources, diversity)
- [ ] Writing standards met (clarity, active voice, BLUF)
- [ ] Anti-BS protocol passed (no weasel words, no unsupported claims)

### Step 5: Red Flag Scan
Check for common quality issues:
- [ ] No unsourced statistical claims
- [ ] No weasel words ("some experts say", "it is widely believed")
- [ ] No circular reasoning
- [ ] No survivorship bias in examples
- [ ] No conflation of correlation and causation
- [ ] No false precision (reporting 4 decimal places from survey data)

### Step 6: Decision-Readiness Check
Is this deliverable decision-ready?
- Can the reader make a decision based solely on this deliverable?
- Are the next steps clear?
- Are the limitations transparent?
- Is the confidence level appropriate for the stakes?

## Output Template

```
RESEARCH AUDIT
==============
Deliverable: [Title]
Audit Date: [Date]
Auditor: [Agent]

Overall Quality Score: [1-5]

Completeness: [Pass/Fail] — [Notes]
Evidence Quality: [Pass/Fail] — [Notes]
Consistency: [Pass/Fail] — [Notes]
Standards Compliance: [Pass/Fail] — [Notes]
Red Flags: [Count found] — [Details]
Decision-Ready: [Yes/No] — [Notes]

Required Revisions: [List if any]
Recommendation: [Deliver / Revise / Reject]
```

## Quality Checks

- [ ] Every section of the audit completed
- [ ] No rubber-stamping — genuine critical review performed
- [ ] Required revisions are specific and actionable
- [ ] Audit trail preserved for accountability
