# Contradiction Resolution Patterns

## Pattern Name: Contextual Reconciliation

**Problem:** Two claims appear contradictory but are both valid under different conditions.

**Solution:** Identify the specific conditions under which each claim holds. The resolution
is a conditional statement: "Claim A holds when X; Claim B holds when Y."

**When to Use:** When contradicting sources describe different environments or configurations.

**Example:** "Redis failover is sub-2s" and "failover takes 5-8s" are both true -- failover
time is load-dependent. Under moderate load, sub-2s; under heavy load, 5-8s.

---

## Pattern Name: Temporal Resolution

**Problem:** Claims contradict because they describe the same thing at different points in
time, and the underlying reality has changed.

**Solution:** Verify source dates and check for intervening changes. Identify which claim
reflects the current state. The older claim may be historically accurate but outdated.

**When to Use:** When sources have different publication dates in a fast-moving domain.

**Example:** "No columnar storage" (2022) vs. "supports columnar via pg_columnar" (2025).

---

## Pattern Name: Methodology Decomposition

**Problem:** Contradictory results stem from different measurement methodologies.

**Solution:** Examine methodology behind each claim. Identify differences in test
conditions, sample sizes, or definitions. Normalize for comparison or document
why direct comparison is invalid.

**When to Use:** When numerical claims from different sources conflict.

**Example:** Source A: "99.99% uptime" (planned hours only). Source B: "99.5% uptime"
(including maintenance). The numbers measure different things.

---

## Pattern Name: Authority Hierarchy

**Problem:** Sources of different authority levels make contradictory claims.

**Solution:** Apply source trust scoring. Primary sources outrank secondary. Official docs
outrank blog posts. Prefer higher methodological rigor unless multiple independent
lower-tier sources converge on the alternative.

**When to Use:** When contextual reconciliation does not apply.

**Example:** Vendor docs vs. Stack Overflow answer -- prefer official docs unless multiple
independent users corroborate the alternative.

---

## Pattern Name: Escalation to Experiment

**Problem:** Available sources cannot resolve the contradiction and stakes are high.

**Solution:** Design a targeted experiment to resolve the contradiction directly. Define
the question, success criteria, and methodology before executing.

**When to Use:** When the contradiction is critical, existing sources are exhausted, and
the effort to experiment is justified by the decision impact.

**Example:** Contradictory throughput claims resolved by running a controlled benchmark.
