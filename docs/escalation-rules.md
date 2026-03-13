# Escalation Rules

## Purpose

This document defines when and how to escalate issues during the research
process. Escalation is not failure; it is a mechanism for resolving blockers,
managing risk, and ensuring timely delivery.

## When to Escalate

### Mandatory Escalation Triggers

Escalate immediately when:

1. **Evidence contradicts a critical stakeholder assumption.** The finding is
   material and may change the decision.
2. **Time-sensitive intelligence.** A finding has a decision window that is
   closing faster than the research timeline allows.
3. **Source credibility crisis.** A key source is found to be unreliable,
   compromised, or interested-party, affecting the core conclusion.
4. **Irreconcilable contradiction.** Two high-tier sources directly conflict
   on a material point with no resolution.
5. **Scope creep beyond capacity.** The research question has expanded beyond
   what can be delivered in the agreed timeline.

### Recommended Escalation Triggers

Consider escalating when:

- Confidence drops below [PROBABLE] on a critical finding.
- A quality gate fails twice on the same issue.
- An agent is blocked waiting for input or access.
- The research reveals risks outside the original question's domain.
- Stakeholder expectations appear misaligned with what evidence can support.

## Escalation Levels

| Level  | Recipient             | When to Use                           |
|--------|-----------------------|---------------------------------------|
| Level 1| Research Director     | Process issues, scope questions, delays|
| Level 2| Research Director + Stakeholder | Material findings, timeline risk |
| Level 3| Leadership            | Critical intelligence, strategic risk  |

## Escalation Protocol

### Step 1: Document the Issue

Before escalating, prepare:
- **What:** A clear description of the issue.
- **Why it matters:** Impact on the research or the stakeholder's decision.
- **What was tried:** Steps already taken to resolve.
- **What is needed:** Specific request (decision, access, time, resources).

### Step 2: Select the Channel

| Urgency        | Channel                                |
|----------------|----------------------------------------|
| Critical (< 2h)| Direct message + follow-up call       |
| Urgent (< 24h) | Slack #research-alerts + tag recipient |
| Standard        | Escalation ticket in tracking system   |

### Step 3: Follow Up

- Critical: Follow up within 2 hours if no response.
- Urgent: Follow up within 24 hours.
- Standard: Follow up within 48 hours.

## Escalation Message Format

```
ESCALATION: [Level 1/2/3]
Issue: [One-sentence description]
Impact: [What this affects and why it matters]
Attempted resolution: [What was already tried]
Request: [What is needed from the recipient]
Deadline: [When a response is needed]
```

## De-Escalation

An escalation is resolved when:
- The blocker is removed and work can proceed.
- The scope is adjusted with stakeholder agreement.
- The deliverable is revised to reflect the new information.
- The resolution is documented for future reference.

## Tracking

All escalations are logged with:
- Date and time raised.
- Level and recipient.
- Issue description.
- Resolution and date resolved.
- Lessons learned.

## Quality Check

- Are mandatory triggers well understood by all agents?
- Is the escalation message complete and actionable?
- Are escalations being tracked and reviewed for patterns?
- Is de-escalation confirmed and documented?
