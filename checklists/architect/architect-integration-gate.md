# Architect Integration Gate

## Purpose

Verify that outputs from all research layers can be and have been integrated
into a coherent whole. Catches structural inconsistencies, format mismatches,
and logical gaps before synthesis.

## Gate Question

**Are all research layers integrated and mutually coherent?**

## Prerequisites

- All assigned agents have submitted their layer outputs.
- Each output follows the agreed format and schema.
- Evidence conflicts have been logged (resolution not required yet).
- Cross-references between layers have been attempted.

## Pass Criteria

1. Every layer output uses the agreed data schema and format.
2. Terminology is consistent across layers (glossary applied if needed).
3. Temporal references align (no layer uses outdated data that contradicts
   another layer's current data without explanation).
4. Causal claims in one layer do not contradict evidence in another.
5. Quantitative figures cited across layers are reconciled or discrepancies
   noted.
6. All layers reference the same scope boundaries (no layer drifted
   out of scope).
7. Integration map shows how each layer's output feeds the synthesis.

## Fail Actions

- If format mismatches exist: return the non-conforming output for
  reformatting.
- If terminology conflicts: produce a reconciliation glossary and have
  agents re-label.
- If temporal misalignment: flag which layer has stale data and request
  an update or note the caveat.
- If causal contradictions: route to conflict resolution gate.
- If a layer drifted out of scope: trim the output to scope boundaries.

## Escalation Rules

- Escalate if more than 30% of layers have integration issues.
- Escalate if causal contradictions cannot be resolved by the agents alone.
- Escalate if integration reveals that the original research design was
  flawed and a redesign is needed.
- Escalate if integration delays would push delivery past the deadline.
