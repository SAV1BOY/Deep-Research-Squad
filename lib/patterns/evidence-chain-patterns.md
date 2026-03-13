# Evidence Chain Patterns

## Pattern Name: Linear Evidence Chain

**Problem:** A conclusion depends on a sequence of claims. If any link is weak, the
entire conclusion is unreliable.

**Solution:** Map the chain explicitly: Claim A leads to Claim B leads to Conclusion C.
Assess each link independently. Chain confidence equals the weakest link.

**When to Use:** When conclusions are derived through multi-step logical inference.

**Example:**
- Link 1: "Our workload is 80% writes" (strength: 0.95)
- Link 2: "LSM-tree outperforms B-tree for write-heavy workloads" (strength: 0.85)
- Link 3: "Cassandra uses LSM-tree" (strength: 0.99)
- Chain confidence: 0.85 (weakest link)

---

## Pattern Name: Convergent Evidence Chain

**Problem:** A single evidence thread may be insufficient for high confidence.

**Solution:** Identify multiple independent paths to the same conclusion. Three paths of
moderate strength often outweigh one strong path. Document each path, then assess
convergent confidence.

**When to Use:** When building the case for a critical recommendation.

**Example:**
- Path 1: Vendor benchmarks (strength: 0.70)
- Path 2: Production case study (strength: 0.80)
- Path 3: Independent consortium benchmark (strength: 0.85)
- Convergent confidence: 0.92

---

## Pattern Name: Negative Evidence Chain

**Problem:** The absence of evidence is itself informative but easy to overlook.

**Solution:** Document deliberate searches that yielded no results. Track negative
findings: "Searched for X failure cases across Y sources, found none."

**When to Use:** When a claim's strength partly depends on absence of problems.

**Example:** "Searched 50+ case studies; zero data corruption incidents reported. This
absence supports the durability claim, though it is not proof."

---

## Pattern Name: Evidence Strength Aggregation

**Problem:** Evidence of varying types and strengths needs combining into an overall score.

**Solution:** Categorize by type. Apply the evidence strength rubric. Aggregate using
weighted averaging where empirical weighs more than anecdotal. Document the method.

**When to Use:** When synthesizing a body of evidence into a single confidence score.

**Example:** 1 empirical (weight 3, score 0.85) + 2 expert opinions (weight 2, score 0.75)
+ 2 anecdotal (weight 1, score 0.60) = aggregated score of ~0.74.
