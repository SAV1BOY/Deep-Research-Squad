# OSINT Footprint Coverage Gate

## Purpose

Verify that the OSINT investigation has covered the full digital and public
footprint relevant to the research target. Incomplete footprint coverage
risks missing critical publicly available information.

## Gate Question

**Has the full relevant public footprint been covered?**

## Prerequisites

- Target entities (persons, organizations, products, events) identified.
- OSINT collection plan with platform list defined.
- Collection tools and techniques selected.
- Legal and ethical boundaries reviewed.

## Pass Criteria

1. Web presence checked: official websites, landing pages, blogs.
2. Social media profiles reviewed across major platforms.
3. Corporate registries and business filings searched.
4. Domain registration (WHOIS) and DNS records checked when relevant.
5. News archives searched for media mentions.
6. Court records and legal filings searched when applicable.
7. Technical footprint assessed (GitHub, patents, publications) when
   relevant to the target.
8. Footprint coverage is mapped against target entities in a matrix.

## Fail Actions

- If a major platform is unchecked: search it before concluding.
- If corporate filings are not reviewed when the target is an
  organization: add that search.
- If technical footprint is skipped for a technology topic: include it.
- If coverage matrix is incomplete: fill in all cells.
- If a platform is inaccessible: document the gap and note what might
  be missing.

## Escalation Rules

- Escalate if the target has taken active measures to minimize their
  public footprint (counter-OSINT).
- Escalate if footprint coverage requires accessing platforms in
  jurisdictions with data access restrictions.
- Escalate if footprint analysis reveals potential PII exposure that
  creates ethical concerns.
