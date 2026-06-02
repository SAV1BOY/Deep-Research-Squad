# reflexion.md — L0 verbal reflection (PROT, Deep-Research leaf)

> Same per-task L0 protocol as the fleet, for KPI **citation_accuracy** (auto/external). Cheap; turns each
> task's gate verdict into a learning signal appended to `data/metrics/evolution_log.tsv`.

## When
After the Step-11 verification cascade emits a `verification_result` for a research task.

## Steps
1. Read the gate outcome: `gate_pass`, `gate_score`, and the measured `citation_accuracy`
   (resolved_citations / total_citations — a non-LLM external check).
2. Write a one-paragraph reflection: which sources/methods raised citation accuracy, what was weak, what
   to try next. Emit `reflexion_verdict ∈ {good, bad, neutral}`.
3. Append one row to `data/metrics/evolution_log.tsv`:
   `task_id, timestamp, task_type, gate_pass, citation_accuracy, gate_score, reflexion_verdict, crystallized_skill_ref`.
4. On a clean pass, consider crystallizing a reusable source-triangulation skill (Voyager).
5. `scripts/reporting/fitness.py` rolls up `citation_accuracy`. Because this KPI is auto/external (not
   conformance), it MAY drive L1 selection once the kernel is armed.

## Contract
Append-only; never edit prior rows or the kernel. The verbal reflection is qualitative; the durable
signal is the appended row consumed by the DET rollup.
