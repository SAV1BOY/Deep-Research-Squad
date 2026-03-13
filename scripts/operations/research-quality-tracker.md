# Script: Research Quality Tracker

## Purpose

Tracks quality metrics across all research deliverables over time. Enables
identification of quality trends, common issues, and improvement opportunities
across the research squad's output.

## Trigger

- After every delivery: Log quality metrics
- Weekly: Generate quality summary
- Monthly: Generate quality trend report

## Inputs

- `delivery_metadata`: Metadata from each packaged delivery
- `audit_results`: Results from research audits
- `feedback`: Any feedback received from requesters
- `historical_data`: Previous quality tracker entries

## Process

### Step 1: Log Delivery Metrics
For each delivery, record:

| Field | Value |
|-------|-------|
| Research ID | [Unique ID] |
| Date | [Delivery date] |
| Type | [Brief/Deep dive/DD/etc.] |
| Topic | [Subject area] |
| Confidence score | [0-100] |
| Source count | [Number] |
| Source diversity | [Score] |
| Evidence grade avg | [A-F] |
| Contradictions found | [Count] |
| Audit result | [Pass/Conditional/Revise] |
| Turnaround time | [Hours/days] |
| Requester satisfaction | [1-5 if available] |

### Step 2: Calculate Running Metrics
Maintain rolling averages:
- Average confidence score (30-day, 90-day)
- Average source diversity (30-day, 90-day)
- Average turnaround time by deliverable type
- Audit pass rate (first-pass vs requiring revision)
- Requester satisfaction average

### Step 3: Identify Quality Trends
Flag notable patterns:
- Confidence scores trending up or down
- Source diversity improving or declining
- Turnaround times changing
- Common audit findings recurring

### Step 4: Issue Tracking
Track recurring quality issues:

| Issue | Frequency | Severity | Root Cause | Remediation |
|-------|-----------|----------|------------|-------------|
| Low source diversity | 3 of last 10 | Medium | Time pressure | Expand source checklist |
| Missing contradictions | 2 of last 10 | High | Process gap | Add contradiction step |

### Step 5: Generate Quality Report

```
QUALITY TRACKER REPORT
======================
Period: [Date range]
Deliverables: [Count]

Key Metrics:
  Avg confidence: [Score] (trend: ↑↓→)
  Avg source diversity: [Score] (trend: ↑↓→)
  Audit first-pass rate: [%] (trend: ↑↓→)
  Avg turnaround: [Time] (trend: ↑↓→)

Top Issues:
1. [Issue] — [Frequency] — [Remediation status]

Improvements Made:
- [Improvement implemented] — [Impact observed]

Recommendations:
- [Suggested process change]
```

## Quality Targets

| Metric | Target | Minimum | Current |
|--------|--------|---------|---------|
| Confidence score avg | >75 | >60 | [Current] |
| Source diversity avg | >70 | >50 | [Current] |
| First-pass audit rate | >80% | >60% | [Current] |
| Requester satisfaction | >4.0 | >3.5 | [Current] |
