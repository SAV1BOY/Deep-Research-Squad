# Query Operator Usage Gate

## Purpose

Ensure that search operators (Boolean, site-specific, date filters, etc.)
are correctly applied for each target source. Improper operator usage leads
to either too many irrelevant results or missed relevant ones.

## Gate Question

**Are the correct search operators being used for each source platform?**

## Prerequisites

- Target search platforms identified (Google, Scholar, PubMed, SEC EDGAR,
  news databases, etc.).
- Operator syntax for each platform documented or known.
- Keywords and keyword groups finalized.
- Desired precision-recall balance determined per sub-question.

## Pass Criteria

1. Boolean operators (AND, OR, NOT) are used correctly in every query.
2. Phrase matching (quotes) is applied for multi-word concepts.
3. Site/domain filters are used when targeting specific source types.
4. Date range operators are applied when temporal boundaries exist.
5. Wildcard and proximity operators are used where supported and useful.
6. Platform-specific syntax is correct (e.g., PubMed MeSH terms, Google
   Scholar author: operator).
7. Queries are tested with a dry run before full execution where possible.

## Fail Actions

- If Boolean logic is wrong: correct the operator placement and retest.
- If phrase matching is missing: add quotes around multi-word key terms.
- If platform syntax is incorrect: consult the platform's search guide
  and fix.
- If date filters are absent when boundaries exist: add them.
- If no dry run was performed: execute a sample query and review the
  first 10 results for relevance.

## Escalation Rules

- Escalate if a platform's API or search interface has changed and
  documented operators no longer work.
- Escalate if the query complexity exceeds the platform's operator support.
- Escalate if dry-run results suggest the entire search strategy needs
  redesign.
