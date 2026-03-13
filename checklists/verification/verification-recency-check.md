# Verification Recency Check

## Purpose

Confirm that verified claims still hold true as of the most recent available
information. Facts verified against older sources may have been superseded
by newer developments.

## Gate Question

**Are verified claims still current and not superseded by recent events?**

## Prerequisites

- Claims verified through cross-source and citation chain checks.
- Publication dates of verification sources recorded.
- Recent news and update feeds for the topic monitored.
- Domain rate-of-change classification available.

## Pass Criteria

1. All critical claims have been checked against sources from the most
   recent 6 months (for fast-moving topics) or 2 years (for stable topics).
2. No verified claim has been contradicted by a more recent authoritative
   source.
3. Known recent developments (legislation, market changes, new studies)
   have been cross-referenced against existing claims.
4. Claims about ongoing situations include a "verified as of [date]"
   timestamp.
5. Superseded claims are updated or marked as historical.
6. The recency check covers regulatory, legal, and policy changes that
   could invalidate prior facts.
7. Recency check results are logged with dates.

## Fail Actions

- If a claim is superseded: update it with current information and cite
  the newer source.
- If recency check was not performed for fast-moving topics: do it now
  before delivery.
- If recent developments are found that affect conclusions: integrate
  them and update the synthesis.
- If a "verified as of" timestamp is missing: add it.
- If the recency check reveals a major shift: flag to Chief Agent for
  possible scope adjustment.

## Escalation Rules

- Escalate if a major conclusion is overturned by very recent information
  discovered during the recency check.
- Escalate if the topic is changing so rapidly that conclusions may be
  outdated by the time of delivery.
- Escalate if recency verification requires access to real-time data
  feeds not currently available.
