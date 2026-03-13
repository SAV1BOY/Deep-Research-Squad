# Audit Reproducibility Check

## Purpose

Assess whether the research could be reproduced by another team following
the same methodology and sources. Reproducible research is more trustworthy
and auditable.

## Gate Question

**Could another team reproduce this research and reach similar conclusions?**

## Prerequisites

- Methodology documented in detail.
- Source list complete with access information.
- Analysis steps documented.
- Data transformations logged.

## Pass Criteria

1. The research methodology is described in enough detail for another
   team to follow.
2. All sources are listed with retrievable references (URLs, DOIs,
   database queries).
3. Search queries used are documented (keywords, operators, platforms).
4. Data processing and transformation steps are recorded.
5. Analytical judgments (e.g., source weighting, conflict resolution) are
   documented with rationale.
6. The path from evidence to conclusion is traceable without requiring
   the original researchers' tacit knowledge.
7. Tools and methods used are identified (not proprietary black boxes).

## Fail Actions

- If methodology description is insufficient: expand it with step-by-step
  detail.
- If sources are not retrievable: add access information or archive copies.
- If search queries are undocumented: reconstruct and record them.
- If analytical judgments are unexplained: add written rationale.
- If the path from evidence to conclusion is opaque: add intermediate
  reasoning steps.

## Escalation Rules

- Escalate if key aspects of the research depend on unreproducible access
  (e.g., one-time conversations, ephemeral data).
- Escalate if the methodology involves proprietary tools or data that
  cannot be shared.
- Escalate if reproducibility gaps are so significant that the research
  cannot be independently verified.
