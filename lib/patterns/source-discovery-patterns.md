# Source Discovery Patterns

## Pattern Name: Concentric Search

**Problem:** Random or overly narrow search leads to incomplete source coverage.

**Solution:** Search in expanding rings. Start with authoritative sources (official docs),
then secondary (expert blogs, reviews), then tertiary (forums, social media). Assess
coverage at each ring before expanding.

**When to Use:** Default source discovery strategy for any research question.

**Example:** Ring 1: PostgreSQL docs. Ring 2: Engineering blog comparisons. Ring 3: Reddit
discussions. Ring 4: Stack Overflow for edge cases.

---

## Pattern Name: Citation Chain Following

**Problem:** Key sources are not found through direct search but are referenced by others.

**Solution:** When a high-quality source is found, examine its references. Follow links to
primary data, foundational papers, or related work. Build a citation graph.

**When to Use:** When direct searches miss authoritative primary sources.

**Example:** A benchmark blog cites a GitHub repo with raw data, which references an
architecture whitepaper not surfaced by keyword search.

---

## Pattern Name: Adversarial Source Seeking

**Problem:** Natural search finds sources confirming the prevailing narrative, missing
critical dissenting views or failure cases.

**Solution:** Deliberately search for negatives: "problems with X," "migrating away from
X," "X limitations," and "X postmortem."

**When to Use:** After initial positive sources are gathered, to ensure balance.

**Example:** After positive ClickHouse case studies, search: "ClickHouse problems
production," "moved away from ClickHouse."

---

## Pattern Name: Expert Identification

**Problem:** Valuable insights from domain experts may not rank highly in search results.

**Solution:** Identify experts by: conference speakers, frequent contributors, project
maintainers, seminal paper authors. Search for their writings directly.

**When to Use:** When deep domain expertise is needed and general sources lack depth.

**Example:** Find core database committers and search for their blog posts and talks.

---

## Pattern Name: Temporal Bracketing

**Problem:** Search results mix outdated and current information.

**Solution:** Search recent content first (last 6-12 months) for current state, then
older content only for stable fundamentals.

**When to Use:** In fast-moving domains where information has a short shelf life.

**Example:** Search "ClickHouse performance 2025-2026" for current benchmarks.
