# Script: Quarterly Quality Review Builder

## Purpose

Compiles a comprehensive quarterly review of research squad quality,
productivity, and improvement. This is the strategic quality document
that drives process improvements and resource allocation.

## Trigger

End of each quarter (or on-demand for mid-quarter reviews).

## Inputs

- `quality_tracker_data`: All quality metrics from the quarter
- `delivery_logs`: All deliverables produced
- `cross_squad_data`: Cross-squad delivery performance
- `feedback_data`: All requester feedback received
- `previous_quarter`: Last quarter's review for comparison

## Process

### Step 1: Aggregate Quarterly Metrics

| Metric | Q Current | Q Previous | Trend | Target |
|--------|----------|-----------|-------|--------|
| Total deliverables | [N] | [N] | ↑↓→ | [N] |
| Avg confidence score | [Score] | [Score] | ↑↓→ | >75 |
| Avg source diversity | [Score] | [Score] | ↑↓→ | >70 |
| Audit first-pass rate | [%] | [%] | ↑↓→ | >80% |
| On-time delivery rate | [%] | [%] | ↑↓→ | >90% |
| Requester satisfaction | [Score] | [Score] | ↑↓→ | >4.0 |
| Cross-squad on-time | [%] | [%] | ↑↓→ | >95% |

### Step 2: Deliverable Breakdown
Analyze output by type:

| Type | Count | Avg Quality | Avg Turnaround | Notes |
|------|-------|------------|----------------|-------|
| Executive briefs | [N] | [Score] | [Time] | |
| Deep dives | [N] | [Score] | [Time] | |
| Competitor analyses | [N] | [Score] | [Time] | |
| Due diligence | [N] | [Score] | [Time] | |
| Market maps | [N] | [Score] | [Time] | |

### Step 3: Quality Issue Analysis
Top quality issues this quarter:

1. **[Issue]**: Occurred [N] times, severity [level]
   - Root cause: [Analysis]
   - Remediation: [Action taken or proposed]
   - Status: [Resolved/In progress/Open]

### Step 4: Wins and Improvements
Document what went well:
- Process improvements implemented and their impact
- Notable high-quality deliverables
- Positive requester feedback highlights
- New capabilities developed

### Step 5: Agent Performance Summary
Per-agent contribution and quality:
- Deliverables contributed to
- Quality scores on assigned components
- Improvement areas identified
- Training or calibration needed

### Step 6: Next Quarter Priorities

Based on this quarter's data:
1. **Priority 1**: [Improvement area] — [Specific action]
2. **Priority 2**: [Improvement area] — [Specific action]
3. **Priority 3**: [Improvement area] — [Specific action]

## Output Template

```
QUARTERLY QUALITY REVIEW
========================
Quarter: [Q# YYYY]
Prepared: [Date]

EXECUTIVE SUMMARY
[3-5 sentence summary of quarter performance]

METRICS DASHBOARD
[Table from Step 1]

DELIVERABLE ANALYSIS
[From Step 2]

QUALITY ISSUES
[From Step 3]

WINS
[From Step 4]

NEXT QUARTER PRIORITIES
[From Step 6]
```

## Review Process

1. Draft prepared by operations agent
2. Reviewed by chief research agent
3. Shared with all squad agents
4. Action items assigned with owners and deadlines
5. Progress tracked in next quarter's review
