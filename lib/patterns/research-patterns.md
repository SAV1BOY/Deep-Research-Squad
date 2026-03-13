# Common Research Patterns

## Pattern Name: Breadth-First Exploration

**Problem:** Starting research too narrowly risks missing critical context, alternative
solutions, or important constraints that only surface through broader exploration.

**Solution:** Begin with a wide survey of the landscape before diving deep. Allocate the
first 20-30% of research time to breadth: scan multiple source types, identify key players,
map the solution space, and note areas that warrant deeper investigation.

**When to Use:** At the start of any new research question, especially when the domain is
unfamiliar or the question has many possible dimensions.

**Example:** Before evaluating specific databases, first survey: what categories exist
(relational, document, graph, time-series), what the industry trends are, and what
comparable organizations have chosen.

---

## Pattern Name: Depth-First Investigation

**Problem:** Breadth-first alone produces shallow understanding. Critical details, edge
cases, and nuanced trade-offs only emerge through focused deep investigation.

**Solution:** After breadth-first exploration identifies promising areas, allocate focused
time to investigate each in depth. Follow evidence chains, read primary sources, and test
claims against specific conditions relevant to the research question.

**When to Use:** After initial survey has identified 2-4 key areas warranting detailed analysis.

**Example:** After identifying ClickHouse and TimescaleDB as top candidates, deep-dive into
each: read architecture docs, find benchmark comparisons, study failure modes, and interview
community forums for operational experience.

---

## Pattern Name: Iterative Refinement

**Problem:** Research questions often evolve as new information is discovered. Rigid
adherence to the original question leads to irrelevant or incomplete findings.

**Solution:** Treat the research question as a living artifact. After each research cycle,
revisit and refine the question based on what has been learned. Update the question tree,
re-prioritize branches, and communicate scope changes to stakeholders.

**When to Use:** At every phase transition or when significant new information changes the
research landscape.

**Example:** Original question "Which database is best?" refines to "Which column-oriented
database handles 500K events/sec with sub-100ms query latency?" after initial exploration.

---

## Pattern Name: Triangulation

**Problem:** Relying on a single source or evidence type creates vulnerability to bias,
error, or outdated information.

**Solution:** For every critical claim, seek corroboration from at least three independent
sources of different types (e.g., official docs, independent benchmarks, community reports).
Only elevate confidence when multiple independent sources converge.

**When to Use:** For any claim that will directly influence a decision or recommendation.

**Example:** Verify database throughput claims using: vendor benchmarks, third-party test
results, and production reports from community case studies.
