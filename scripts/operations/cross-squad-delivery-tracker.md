# Script: Cross-Squad Delivery Tracker

## Purpose

Tracks research deliverables requested by or delivered to other squads.
Ensures cross-squad dependencies are visible, deadlines are met, and
handoffs are clean.

## Trigger

- When a cross-squad research request is received
- When a deliverable is sent to another squad
- Weekly: Status review of all open cross-squad items

## Inputs

- `requests`: Incoming research requests from other squads
- `deliveries`: Outgoing deliverables to other squads
- `deadlines`: Committed delivery dates
- `feedback`: Feedback from receiving squads

## Process

### Step 1: Log Cross-Squad Request

| Field | Value |
|-------|-------|
| Request ID | [Unique ID] |
| Requesting squad | [Squad name] |
| Requester contact | [Name/role] |
| Request summary | [One sentence] |
| Date received | [Date] |
| Deadline | [Date] |
| Priority | [Critical/High/Medium/Low] |
| Status | [Received/In Progress/Review/Delivered] |
| Assigned to | [Agent(s)] |
| Dependencies | [What we need from others] |

### Step 2: Track Progress

Update status at each stage:
1. **Received**: Request logged, brief being created
2. **Scoped**: Research brief completed, effort estimated
3. **In Progress**: Active research underway
4. **Review**: Draft complete, under quality audit
5. **Delivered**: Final package sent to requesting squad
6. **Accepted**: Requesting squad confirms receipt and adequacy

### Step 3: Dependency Management
Track what the research squad needs from other squads:

| Dependency | From Squad | Status | Impact if Delayed |
|-----------|-----------|--------|-------------------|
| Customer data | Data Squad | Pending | Blocks analysis |
| Technical specs | Engineering | Received | None |

### Step 4: Deadline Risk Assessment
For each open item:
- Days until deadline
- Estimated completion date
- Risk level (Green/Yellow/Red)
- Mitigation if at risk

### Step 5: Weekly Status Report

```
CROSS-SQUAD DELIVERY STATUS
============================
Week of: [Date]

Active Requests: [Count]
  On Track: [Count]
  At Risk: [Count]
  Overdue: [Count]

Completed This Week: [Count]
New Requests This Week: [Count]

[Table of active items with status]

Blockers:
- [Blocker description] — [Action needed from whom]

Upcoming Deadlines (Next 7 Days):
- [Request ID]: [Summary] — Due [Date]
```

### Step 6: Feedback Loop
After delivery acceptance:
- Log requester feedback
- Note integration issues
- Track if deliverable was actually used
- Identify process improvements

## Escalation Rules

1. **Yellow**: Delivery at risk of missing deadline by 1-2 days → Notify requester
2. **Red**: Delivery will miss deadline by 3+ days → Escalate to squad leads
3. **Blocked**: External dependency preventing progress → Immediate escalation

## Quality Standards for Cross-Squad Deliveries

- All cross-squad deliverables must pass standard audit
- Include integration notes specific to receiving squad's needs
- Handoff meeting or written handoff notes required for complex deliverables
- Follow-up check 48 hours after delivery for questions
