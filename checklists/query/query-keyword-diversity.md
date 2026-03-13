# Query Keyword Diversity Gate

## Purpose

Verify that the keyword set is diverse enough to capture relevant results
across different terminologies, synonyms, and phrasings. Prevents echo-
chamber searching where the same concepts are queried repeatedly.

## Gate Question

**Are keywords diverse, comprehensive, and non-redundant?**

## Prerequisites

- Search strategy defined with target platforms.
- Domain terminology reviewed (including jargon and colloquial terms).
- Problem framing and key concepts identified.
- Known aliases, acronyms, and alternative spellings catalogued.

## Pass Criteria

1. Each core concept has at least 3 synonym or alternate-phrasing variants.
2. Technical and lay terminology are both represented.
3. Acronyms and their expanded forms are both included.
4. Historical terms (older names for the same concept) are included when
   the time scope warrants it.
5. No two keyword sets are functionally identical (redundancy < 20%).
6. Negative keywords are defined to filter irrelevant results.
7. Keywords are organized by sub-question for traceability.

## Fail Actions

- If synonym coverage is thin: use a thesaurus pass and domain glossary
  to expand.
- If only technical terms used: add plain-language equivalents.
- If redundancy exceeds 20%: merge or eliminate duplicate keyword sets.
- If negative keywords are absent: add at least 3 exclusion terms per
  sub-question.
- If acronyms are missing: scan the domain for common abbreviations.

## Escalation Rules

- Escalate if the domain uses highly specialized jargon that the Query
  Agent cannot generate without expert input.
- Escalate if the topic crosses multiple languages and keyword translation
  quality is uncertain.
- Escalate if keyword expansion causes result volume to become unmanageable.
