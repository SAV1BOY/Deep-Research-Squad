# Model Assumptions Gate

## Purpose

Validate that all assumptions underlying analytical models, forecasts, or
scenario analyses are explicitly stated, justified, and stress-tested.
Hidden or invalid assumptions are the most common source of model failure
and misleading predictions.

## When Triggered

- Before any model output is used in research conclusions.
- When model parameters or inputs are changed significantly.
- During peer review of modeling methodology.

## Prerequisites

- Model structure and methodology documented.
- Input data sources identified and evaluated.
- Intended use case for model outputs defined.

## Checklist

- [ ] All assumptions are explicitly listed and documented (no implicit assumptions).
- [ ] Each assumption has a stated justification grounded in evidence or domain knowledge.
- [ ] Boundary conditions and valid ranges for each assumption are specified.
- [ ] Sensitivity analysis performed: which assumptions most affect outputs?
- [ ] Assumptions are tested against historical data where available.
- [ ] Assumptions are internally consistent (no contradictions between them).
- [ ] Assumptions about independence, stationarity, or distribution are validated against data.
- [ ] Known limitations of each assumption are documented.
- [ ] Alternative assumption sets have been considered and their impact assessed.
- [ ] Assumptions are appropriate for the model's intended use (not borrowed from a different context).
- [ ] Time-dependent assumptions are flagged with expiration dates or review triggers.
- [ ] Stakeholders who provided domain assumptions are identified for traceability.

## Pass / Fail Criteria

**Pass**: All assumptions are explicit, justified, sensitivity-tested, and
internally consistent. Boundary conditions are defined.

**Fail**: Any assumption is implicit, unjustified, untested for sensitivity,
or contradicts another assumption.

## Escalation if Failed

- Return to the modeling team to make implicit assumptions explicit and
  justify each one.
- If sensitivity analysis reveals brittle assumptions, present results as
  ranges rather than point estimates.
- Escalate to the Architect if assumption failures undermine the research
  methodology.
- Flag high-sensitivity assumptions in all downstream reports for
  stakeholder awareness.
