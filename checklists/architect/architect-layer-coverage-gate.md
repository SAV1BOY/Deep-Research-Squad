# Architect Layer Coverage Gate

## Purpose

Verify that all necessary research layers are included in the design and
that no critical dimension of the question is left uncovered. Prevents blind
spots that would weaken the final output.

## Gate Question

**Are all required research layers covered with no critical gaps?**

## Prerequisites

- Research design document with layer assignments.
- Scope sub-questions mapped to layers.
- Agent capability matrix consulted.
- Question type and complexity assessment completed.

## Pass Criteria

1. Every sub-question is covered by at least one research layer.
2. High-stakes claims are covered by at least two complementary layers
   (e.g., literature + data, or OSINT + verification).
3. Temporal dimension is covered if the question involves change over time.
4. Contrarian layer is included for any question with strong prior beliefs.
5. Source diversity layer ensures no single source type dominates.
6. No layer is orphaned (assigned but with no sub-question feeding into it).
7. Coverage matrix shows >= 90% of sub-questions with multi-layer support.

## Fail Actions

- If a sub-question has zero layer coverage: assign at minimum one layer.
- If high-stakes claims have single-layer coverage: add a second layer.
- If temporal dimension is missing when relevant: add Timeline Agent.
- If Contrarian layer is absent on belief-heavy topics: add it immediately.
- If orphan layers exist: remove them or link them to valid sub-questions.

## Escalation Rules

- Escalate if adding required layers would exceed the time or resource budget.
- Escalate if no available agent can cover a mandatory layer.
- Escalate if the question spans domains requiring layers not in the current
  agent repertoire (e.g., quantitative modeling for a purely qualitative team).
