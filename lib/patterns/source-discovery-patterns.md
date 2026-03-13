# Source Discovery Patterns

## Pattern Name: Concentric Search

**Problem:** Starting with a random or overly narrow search strategy leads to incomplete
source coverage and missed critical information.

**Solution:** Search in expanding concentric rings. Start with the most authoritative
sources (official docs, primary research), then move to secondary sources (curated reviews,
expert blogs), then tertiary (forums, social media). At each ring, assess whether enough
evidence has been gathered before expanding further.

**When to Use:** For any research question. This is the default source discovery strategy.

**Example:** Ring 1: PostgreSQL official documentation. Ring 2: Database comparison articles
from reputable engineering blogs. Ring 3: Reddit and Hacker News discussions from
practitioners. Ring 4: Stack Overflow Q&A for edge cases.

---

## Pattern Name: Citation Chain Following

**Problem:** Key sources are not easily found through direct search but are referenced
in the bibliographies or links of other sources.

**Solution:** When a high-quality source is found, examine its references and citations.
Follow links to primary data, foundational papers, or related work. Build a citation
graph to discover sources that search engines may not surface directly.

**When to Use:** When direct searches are not yielding authoritative primary sources, or
when a found source references important upstream work.

**Example:** A benchmark blog post cites a GitHub repository with raw test data, which in
turn references the database's architecture whitepaper. Following the chain surfaces
sources not found through keyword search.

---

## Pattern Name: Adversarial Source Seeking

**Problem:** Natural search tends to find sources that confirm the prevailing narrative,
missing critical dissenting views or failure cases.

**Solution:** Deliberately search for negative experiences, failure cases, migration-away
stories, and critical reviews. Use search terms like "problems with X," "migrating away
from X," "X vs Y limitations," and "X postmortem."

**When to Use:** After initial positive sources are gathered, to ensure balanced coverage.

**Example:** After finding several positive ClickHouse case studies, deliberately search:
"ClickHouse problems production," "moved away from ClickHouse," "ClickHouse limitations."

---

## Pattern Name: Expert Identification

**Problem:** The most valuable insights often come from recognized domain experts whose
work may not rank highly in general search results.

**Solution:** Identify key experts in the domain by looking at: conference speakers,
frequent contributors to authoritative publications, maintainers of relevant open-source
projects, and authors of seminal papers. Then search specifically for their writings.

**When to Use:** When the research question requires deep domain expertise and general
sources lack sufficient depth.

**Example:** For database internals, identify authors of database architecture papers,
core committers to the database project, and speakers at database-focused conferences.
Search for their blog posts, talks, and publications directly.

---

## Pattern Name: Temporal Bracketing

**Problem:** Search results mix outdated and current information, leading to confusion
about what is still accurate.

**Solution:** Perform time-bracketed searches: first search for recent content (last 6-12
months) to establish the current state, then search older content only for historical
context or foundational concepts that remain stable.

**When to Use:** In fast-moving domains (technology, policy, markets) where information
has a short shelf life.

**Example:** Search "ClickHouse performance 2025-2026" for current benchmarks. Only
consult older sources if they cover architectural fundamentals unchanged by recent releases.
