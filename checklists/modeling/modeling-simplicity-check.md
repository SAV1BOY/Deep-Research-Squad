# Modeling Simplicity Check

## Purpose

Ensure the model is as simple as possible while still capturing the essential
dynamics of the problem. Overly complex models are harder to validate, explain,
and use. Overly simple models miss critical factors.

## Gate Question

**Is the model appropriately simple -- no more complex than necessary?**

## Prerequisites

- Model structure documented.
- Variables and relationships listed.
- Model outputs validated against known data points.
- Sensitivity analysis performed or planned.

## Pass Criteria

1. Every variable in the model is justified as necessary for the analysis.
2. Removing any variable would meaningfully reduce the model's accuracy
   or explanatory power.
3. The model can be explained to the target audience in plain language.
4. The number of variables is proportionate to the available data
   (no overfitting).
5. Interaction effects are included only when empirically supported.
6. The model uses the simplest mathematics or logic that captures the
   dynamics.
7. A simpler alternative was considered and rejected with documented
   reasoning.

## Fail Actions

- If unnecessary variables exist: remove them and verify the model still
  performs adequately.
- If the model cannot be explained in plain language: simplify until it
  can.
- If overfitting is suspected: reduce variables or use regularization.
- If no simpler alternative was considered: test a simpler version and
  compare.
- If complexity is unjustified: document why each complex element is
  needed or remove it.

## Escalation Rules

- Escalate if simplification significantly changes the model's conclusions.
- Escalate if the target audience cannot understand the model despite
  simplification efforts.
- Escalate if the tension between simplicity and accuracy cannot be
  resolved and a judgment call is needed.
