# Modeling Causal Validity Check

## Purpose

Ensure that causal relationships represented in the model are empirically
supported and logically sound. Models with invalid causal links produce
plausible but wrong predictions and recommendations.

## Gate Question

**Are the causal relationships in the model valid and evidence-based?**

## Prerequisites

- Model structure with causal links documented.
- Evidence for each causal link collected.
- Domain knowledge of causal mechanisms available.
- Timeline and causality checks completed.

## Pass Criteria

1. Every causal link in the model is supported by at least one piece of
   evidence.
2. The direction of causality is justified (A causes B, not B causes A).
3. Confounding variables are identified and either controlled for or
   acknowledged.
4. Feedback loops are identified and their dynamics described.
5. No causal link relies solely on correlation without mechanism.
6. The model distinguishes between direct and indirect causation.
7. Causal links are rated by confidence level.

## Fail Actions

- If a causal link lacks evidence: find supporting evidence or remove
  the link.
- If direction is unjustified: investigate further or mark as uncertain.
- If confounders are unidentified: analyze for common causes.
- If correlation is mistaken for causation: reframe or remove the link.
- If confidence ratings are missing on causal links: add them.

## Escalation Rules

- Escalate if a critical causal link cannot be validated and the model
  depends on it.
- Escalate if causal validity assessment requires experimental evidence
  that does not exist.
- Escalate if removing invalid causal links fundamentally changes the
  model's predictions.
