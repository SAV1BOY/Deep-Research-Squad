# Cross-Squad Delivery Patterns

## Pattern Name: Structured Handoff

**Problem:** Research findings passed between squads without structure lose context and
critical caveats, leading to misinterpretation or wasted rework.

**Solution:** Use a standardized handoff: original question, key findings with confidence,
methodology summary, limitations, unresolved uncertainties, and next steps.

**When to Use:** Every time research output is passed from one squad to another.

**Example:** Handoff includes: "Kafka handles our throughput with 3x headroom (0.88
confidence). Unresolved: multi-tenant isolation under peak load (UNC-004)."

---

## Pattern Name: Progressive Disclosure

**Problem:** Delivering all findings at once overwhelms the receiving squad.

**Solution:** Structure in three layers: (1) Executive summary with top findings in 5-10
bullets. (2) Detailed findings with evidence and confidence. (3) Full artifact inventory.
Let the receiver choose their depth.

**When to Use:** When research output is extensive (20+ artifacts).

**Example:** Layer 1: "Recommend ClickHouse, 0.85 confidence, key risk: ops complexity."
Layer 2: Comparison table with 5 options and 8 criteria. Layer 3: All 47 source cards.

---

## Pattern Name: Assumption Contract

**Problem:** Research conclusions depend on assumptions the receiving squad may not share.

**Solution:** List all assumptions baked into findings. Have the receiving squad validate
before adopting conclusions. Flag which findings need re-evaluation if assumptions differ.

**When to Use:** When conclusions are sensitive to environmental or business assumptions.

**Example:** Assumption: "Write volume under 500K events/sec for 12 months." If wrong,
database recommendation may change. Receiving squad must confirm.

---

## Pattern Name: Feedback Loop

**Problem:** Research quality cannot improve without feedback from consuming squads.

**Solution:** After the receiving squad acts on findings, they report: what was accurate,
what was missing, what was surprising. Feed this into research process improvements.

**When to Use:** After every cross-squad delivery, with follow-up 2-4 weeks later.

**Example:** "ClickHouse throughput matched predictions, but migration tooling was worse
than expected. Add migration tooling to future database evaluations."
