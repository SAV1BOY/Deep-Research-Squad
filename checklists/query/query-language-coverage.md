# Query Language Coverage Gate

## Purpose

Ensure that multi-language search is planned and executed when the research
topic has significant non-English dimensions. Prevents anglophone bias in
evidence collection.

## Gate Question

**Is multi-language search included when the topic warrants it?**

## Prerequisites

- Scope boundaries include geographic or cultural dimensions.
- Primary languages of the topic domain identified.
- Translation capabilities assessed (machine translation quality,
  agent language skills).
- Target source landscape reviewed for non-English content.

## Pass Criteria

1. Languages relevant to the topic are identified and listed.
2. At least the top 2 non-English languages are included in the search
   plan when the topic is international.
3. Keyword translations are verified (not just machine-translated without
   review).
4. Language-specific search engines or databases are used where they exist
   (e.g., Baidu for Chinese, CiNii for Japanese).
5. Translation quality is sufficient to assess source relevance.
6. Non-English results are flagged for careful interpretation.
7. Monolingual search is explicitly justified when only English is used.

## Fail Actions

- If relevant languages are missing: add them to the search plan.
- If keyword translations are unverified: cross-check with a second
  translation source or native-language reference.
- If language-specific platforms are unused: add at least one per
  relevant language.
- If monolingual search is unjustified: provide rationale or expand.
- If translation quality is poor: flag affected sources with reduced
  confidence.

## Escalation Rules

- Escalate if the topic critically depends on sources in a language no
  agent can process even with translation tools.
- Escalate if machine translation quality is insufficient for the domain's
  technical terminology.
- Escalate if non-English sources contradict English sources and the
  discrepancy cannot be resolved without native-language expertise.
