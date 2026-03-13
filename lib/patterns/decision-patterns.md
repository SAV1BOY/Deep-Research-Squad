# Decision-Making Patterns

## Pattern Name: Weighted Criteria Matrix

**Problem:** Decisions with multiple options and criteria are hard to make consistently.

**Solution:** Define criteria with explicit weights. Score each option against each
criterion using evidence. Compute weighted totals. Use as a discussion tool.

**When to Use:** When there are 3+ options and 4+ evaluation criteria.

**Example:**
| Criteria (weight)        | ClickHouse | TimescaleDB | Druid |
|--------------------------|-----------|-------------|-------|
| Query speed (0.30)       | 0.95      | 0.70        | 0.85  |
| Ops simplicity (0.25)    | 0.50      | 0.85        | 0.40  |
| Cost efficiency (0.20)   | 0.75      | 0.80        | 0.60  |

---

## Pattern Name: Reversibility-First Decision

**Problem:** Not all decisions carry equal risk. Treating all decisions the same wastes
time on low-stakes choices and under-invests in high-stakes ones.

**Solution:** Classify by reversibility: easily-reversible, costly-to-reverse, irreversible.
Decide quickly on reversible choices; demand high confidence for irreversible ones.

**When to Use:** When prioritizing which decisions need more research investment.

**Example:** Logging library (easily reversible) vs. primary database (costly to reverse).

---

## Pattern Name: Minimum Viable Decision

**Problem:** Research can continue indefinitely. Waiting for perfect information delays
action without materially improving the outcome.

**Solution:** Define upfront what minimum confidence and evidence is sufficient. When
thresholds are met, decide. Document remaining uncertainties as risks to monitor.

**When to Use:** Under time pressure or when additional research has diminishing returns.

**Example:** "Decide when we have 3+ benchmarks, confirmed usage at our scale, and >0.75
confidence on critical claims."

---

## Pattern Name: Decision Staging

**Problem:** Large decisions are overwhelming as a single choice point.

**Solution:** Break into sequential stages. Early stages use coarse criteria to eliminate
unfit options. Later stages use fine-grained analysis on remaining candidates.

**When to Use:** When the initial option set is large (5+).

**Example:** Stage 1: Eliminate databases below our scale (removes 60%). Stage 2: Benchmark
remaining 3. Stage 3: Evaluate operational fit of top 2.
