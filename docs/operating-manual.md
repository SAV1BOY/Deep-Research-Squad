# Operating Manual

## Purpose

This manual describes how the Deep Research Squad operates on a day-to-day
basis. It covers the research lifecycle, agent coordination, and delivery flow.

## Research Lifecycle

### Phase 1: Intake and Scoping

1. Research request is received with question, context, and constraints.
2. Research Director reviews for clarity, feasibility, and decision relevance.
3. Scope document is created defining: question, boundaries, audience, format, deadline.
4. Agents are assigned based on scope requirements.

### Phase 2: Source Collection

1. Source Hunter identifies candidate sources.
2. Sources are classified by type and tier (see `evidence-policy.md`).
3. Source inventory is shared with assigned analysts.
4. Gaps in source coverage are flagged early.

### Phase 3: Analysis

1. Deep Analysts conduct primary analysis on assigned sub-questions.
2. Each finding is tagged with confidence level and evidence tier.
3. Specialist agents (Domain, Quantitative, Regulatory, etc.) are activated as needed.
4. Interim findings are shared for early feedback and course correction.

### Phase 4: Synthesis

1. Synthesizer integrates findings across analysts and domains.
2. Five-layer synthesis model is applied (convergence, divergence, integration, implications, gaps).
3. Red Team reviews the synthesis for weaknesses and alternative explanations.
4. Synthesis is revised based on adversarial feedback.

### Phase 5: Quality Review

1. Quality Gate Keeper evaluates against gate criteria.
2. Evidence Auditor verifies citations and tier assignments.
3. Issues are returned for correction before delivery.
4. Final sign-off by Research Director.

### Phase 6: Delivery

1. Executive Translator creates audience-appropriate formats.
2. Delivery Coordinator selects channel and timing.
3. Deliverable is distributed with appropriate metadata.
4. Follow-up questions are tracked for future research.

## Agent Coordination

### Communication Channels

- **Internal:** Agents communicate through structured handoffs (see templates).
- **Status updates:** Regular cadence updates on progress and blockers.
- **Escalation:** Issues that block progress are escalated per `escalation-rules.md`.

### Handoff Protocol

Every agent-to-agent handoff includes:
- What was done and what was found.
- Confidence level of findings.
- What the next agent needs to do.
- Known gaps or concerns.

## Time Management

| Research Type         | Target Duration   |
|-----------------------|-------------------|
| Quick-turn brief      | 1-2 hours         |
| Standard analysis     | 1-2 days          |
| Deep dive             | 3-5 days          |
| Comprehensive study   | 1-2 weeks         |

## Feedback Loop

After delivery:
1. Collect stakeholder feedback on usefulness and accuracy.
2. Document lessons learned.
3. Update processes based on recurring issues.
4. Feed improvements into quality gate criteria.

## Key References

- Agent roles: `docs/agent-roles-guide.md`
- Quality gates: `docs/quality-gates-guide.md`
- Escalation: `docs/escalation-rules.md`
- Evidence handling: `docs/evidence-policy.md`
