# Chief Research Priority Gate

## Purpose

Validate that the research request has been correctly prioritized relative to
urgency, impact, and available capacity. Prevents misallocation of deep-research
effort to low-value or already-answered questions.

## Gate Question

**Is the assigned priority correct, and is the question worth the requested
depth of investigation?**

## Prerequisites

- Research request received with initial priority tag (P0-P3).
- Requester context and stated deadline available.
- Current squad workload summary accessible.
- Prior-research index checked for duplicates or near-duplicates.

## Pass Criteria

1. Priority tag matches the impact/urgency matrix (high-impact + time-sensitive = P0).
2. No existing research output already answers >= 80% of the question.
3. Estimated effort is proportionate to the decision the research will inform.
4. The question is not purely opinion-based; it has a researchable core.
5. Stakeholder who will act on the output has been identified.
6. Depth level (quick scan / standard / deep dive) aligns with priority.
7. The topic does not duplicate work currently in progress by another thread.

## Fail Actions

- If priority is inflated: downgrade and notify requester with justification.
- If question is already answered: return pointer to existing research asset.
- If effort is disproportionate: propose a lighter research tier and seek approval.
- If no actionable stakeholder exists: pause and request clarification on use-case.
- If duplicate in progress: merge requests or queue behind the active thread.

## Escalation Rules

- Escalate to human operator if two or more priority assessments conflict after
  re-evaluation.
- Escalate if the request involves legal, ethical, or safety-critical domains
  that require human sign-off before research begins.
- Escalate if requester disputes the downgrade and insists on original priority
  after one round of justification.
- Auto-escalate any P0 request so a human confirms the urgency before full
  squad mobilization.
