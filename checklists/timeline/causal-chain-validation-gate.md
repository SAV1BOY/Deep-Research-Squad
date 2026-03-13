# Causal Chain Validation Gate

## Purpose

Validate that cause-effect relationships claimed in timelines are logically
sound, evidentially supported, and free from common causal fallacies. A
timeline that asserts causation without rigorous validation risks misleading
downstream analysis and recommendations.

## When Triggered

- After causal links are annotated on a timeline.
- Before timeline-based reasoning is incorporated into synthesis outputs.
- When a stakeholder challenges a claimed causal relationship.

## Prerequisites

- Completed timeline with events ordered and dated.
- Causal links explicitly annotated between events.
- Evidence base supporting each claimed causal relationship.

## Checklist

- [ ] Each causal claim identifies a specific cause event and a specific effect event.
- [ ] The cause precedes the effect in time (temporal precedence confirmed).
- [ ] A plausible mechanism connecting cause to effect is articulated.
- [ ] Alternative explanations for the effect have been considered and documented.
- [ ] Confounding variables that could explain the correlation are identified.
- [ ] The causal chain does not rely solely on post-hoc-ergo-propter-hoc reasoning.
- [ ] Magnitude of the cause is proportional to the magnitude of the effect.
- [ ] Intermediate steps in multi-link causal chains are each independently validated.
- [ ] Feedback loops and bidirectional causation are identified where present.
- [ ] Causal claims are consistent with domain-specific knowledge and established theory.
- [ ] Each causal link has a confidence rating (high, medium, low) based on evidence strength.
- [ ] Absence of evidence for a link is distinguished from evidence of absence.

## Pass / Fail Criteria

**Pass**: Every causal link has temporal precedence, a stated mechanism,
consideration of alternatives, and an evidence-based confidence rating.

**Fail**: Any causal link lacks temporal precedence, has no stated mechanism,
or ignores plausible alternative explanations.

## Escalation if Failed

- Return weak causal claims to the Evidence squad for additional support.
- If a causal chain is central to the thesis and cannot be validated,
  escalate to the Contrarian squad for adversarial review.
- Downgrade affected conclusions from "causal" to "correlational" in
  synthesis outputs until resolved.
