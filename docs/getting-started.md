# Getting Started with Deep Research Squad

## Welcome

This guide walks you through the essentials of working with the Deep Research
Squad. Whether you are requesting research, contributing as an agent, or
reviewing deliverables, start here.

## What Is the Deep Research Squad?

The Deep Research Squad is a multi-agent research system designed to produce
rigorous, evidence-based intelligence. It operates with 16 specialized agent
roles, standardized quality gates, and consistent voice and tone profiles.

## Quick Start for Research Requesters

### Step 1: Define Your Question

A good research question is:
- Specific enough to scope (not "tell me about AI").
- Tied to a decision or action ("should we enter market X?").
- Bounded by timeframe, geography, or domain.

### Step 2: Submit Your Request

Include in your request:
- The research question.
- The decision it informs.
- The audience and their technical depth.
- The desired output format (deep dive, brief, presentation).
- The deadline.

### Step 3: Receive the Deliverable

Deliverables include:
- Confidence-tagged findings ([CONFIRMED], [PROBABLE], [HYPOTHESIS], [UNKNOWN]).
- Source attribution at the appropriate evidence tier.
- Explicit limitations and gaps.
- Actionable recommendations when evidence supports them.

## Quick Start for Agents

### Step 1: Understand Your Role

Review your agent role in `docs/agent-roles-guide.md`. Each role has specific
responsibilities, inputs, and outputs.

### Step 2: Learn the Standards

Read these foundational documents:
- `docs/research-philosophy.md` - Why we do what we do.
- `docs/evidence-policy.md` - How we handle evidence.
- `docs/quality-gates-guide.md` - What quality looks like.
- `voice/tone-profiles/` - How we write.

### Step 3: Follow the Workflow

1. Receive assignment with scoped question.
2. Conduct research following evidence policy.
3. Document findings with confidence tags.
4. Submit through quality gates.
5. Iterate based on review feedback.

## Key Concepts

| Concept           | Where to Learn More                     |
|-------------------|-----------------------------------------|
| Evidence tiers    | `docs/evidence-policy.md`               |
| Confidence scale  | `voice/calibration/confidence-scale-guide.md` |
| Tone profiles     | `voice/tone-profiles/`                  |
| Quality gates     | `docs/quality-gates-guide.md`           |
| Definition of done| `docs/definition-of-done.md`            |

## Directory Structure

```
voice/           - Tone, language, calibration, and channel guides
phrases/         - Reusable language patterns and reasoning blocks
docs/            - Policies, guides, and operational documentation
```

## Getting Help

- Operational questions: See `docs/operating-manual.md`.
- Naming and conventions: See `docs/naming-conventions.md`.
- Contributing improvements: See `docs/contribution-guide.md`.
- Escalation: See `docs/escalation-rules.md`.
