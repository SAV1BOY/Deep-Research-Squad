# Architect Research Design Gate

## Purpose

Validate that the overall research architecture is sound before agents begin
executing. Ensures the design decomposes the question effectively, assigns
appropriate methods, and anticipates integration challenges.

## Gate Question

**Is the research architecture solid enough to guide reliable execution?**

## Prerequisites

- Approved scope with sub-questions from Scope Agent.
- Question type classified (factual, causal, comparative, predictive, etc.).
- Available source landscape surveyed at a high level.
- Time and depth constraints from Chief Agent confirmed.

## Pass Criteria

1. Each sub-question has a designated research layer and responsible agent.
2. Dependencies between layers are mapped (e.g., timeline feeds causality).
3. The design specifies data flow: which agent outputs feed which inputs.
4. At least two independent evidence paths exist for critical claims.
5. Integration points are identified where partial results will be merged.
6. The design includes explicit checkpoints for mid-course correction.
7. Risk register lists top 3 threats to research quality with mitigations.

## Fail Actions

- If sub-questions lack layer assignment: complete the mapping before launch.
- If dependencies are circular: restructure the execution order.
- If only one evidence path exists for critical claims: add a second path
  or flag the fragility to Chief Agent.
- If no checkpoints exist: insert at least two progress reviews.
- If risk register is empty: architect must identify at least 3 risks.

## Escalation Rules

- Escalate if the question type is novel and no existing design template fits.
- Escalate if the research requires more than 10 parallel agent streams,
  exceeding coordination capacity.
- Escalate if a required data source is behind a paywall or access barrier
  not yet cleared.
