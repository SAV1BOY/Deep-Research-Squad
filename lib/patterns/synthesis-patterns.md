# Synthesis Patterns

## Pattern Name: Convergent Synthesis

**Problem:** Research produces many individual findings, but stakeholders need a coherent
narrative that integrates diverse evidence into unified conclusions.

**Solution:** Group related claims and evidence by theme. For each theme, identify the
dominant finding, note dissenting evidence, and state the synthesized conclusion with
confidence level. Build from individual facts to thematic conclusions to overall narrative.

**When to Use:** When transitioning from the analysis phase to the delivery phase, and the
research has produced 10+ claims across multiple themes.

**Example:**
- Theme: "Write Performance" - 5 claims converge on ClickHouse superiority for analytics
- Theme: "Operational Complexity" - 3 claims suggest higher ops burden for ClickHouse
- Synthesis: "ClickHouse is faster but costlier to operate; net recommendation depends on
  team capacity"

---

## Pattern Name: Gap-Aware Synthesis

**Problem:** Synthesis that ignores gaps in evidence creates false confidence. Stakeholders
need to know what was NOT found as much as what was found.

**Solution:** Explicitly catalog gaps alongside findings. For each conclusion, note what
additional evidence would strengthen or weaken it. Create uncertainty cards for significant
gaps and include them in the final deliverable.

**When to Use:** Always. Every synthesis should include gap analysis.

**Example:** "We found strong evidence for query performance but no data on long-term
storage cost at our projected data volume. This gap could affect the ROI calculation."

---

## Pattern Name: Multi-Perspective Synthesis

**Problem:** Research viewed from only one stakeholder perspective may miss critical concerns
that affect adoption, maintenance, or long-term viability.

**Solution:** Synthesize findings through multiple lenses: technical performance, operational
burden, cost, team skill alignment, ecosystem maturity, and strategic fit. Present each
perspective explicitly rather than collapsing them into a single score.

**When to Use:** When the decision affects multiple stakeholder groups or when the research
has cross-cutting implications.

**Example:** A database recommendation synthesized through: developer experience lens,
SRE operations lens, finance cost lens, and CTO strategic alignment lens.

---

## Pattern Name: Temporal Synthesis

**Problem:** Point-in-time analysis misses trends, momentum, and trajectory that are
critical for forward-looking decisions.

**Solution:** Arrange findings along a timeline. Identify trends in adoption, performance
improvements, community growth, and ecosystem development. Extrapolate where the technology
or domain is heading, not just where it is now.

**When to Use:** For technology selection, market analysis, or any research where the
future state matters as much as the current state.

**Example:** "PostgreSQL analytics performance has improved 40% per major release for three
consecutive versions, suggesting the gap with specialized OLAP databases is narrowing."
