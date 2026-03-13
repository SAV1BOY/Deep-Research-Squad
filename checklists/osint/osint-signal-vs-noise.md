# OSINT Signal vs. Noise Gate

## Purpose

Ensure that open-source intelligence collection distinguishes genuine
signals from noise, misinformation, and irrelevant data. OSINT sources
are inherently noisy and require rigorous filtering.

## Gate Question

**Has signal been effectively separated from noise in OSINT collection?**

## Prerequisites

- OSINT collection phase completed or substantially underway.
- Source reliability ratings assigned (A-F scale or equivalent).
- Information credibility assessed per item.
- Cross-referencing against known facts completed.

## Pass Criteria

1. Each OSINT data point has a reliability + credibility rating.
2. Information from anonymous or unverified sources is flagged and not
   treated as confirmed.
3. Social media content is corroborated before inclusion as evidence.
4. Bot-generated, astroturfed, or coordinated inauthentic content is
   identified and excluded.
5. Satire, parody, and opinion are distinguished from factual reporting.
6. Signal-to-noise ratio is documented (what percentage of collected
   data was usable).
7. Filtering criteria are documented and applied consistently.

## Fail Actions

- If reliability ratings are missing: apply the rating framework to all
  OSINT items.
- If social media content is uncorroborated: seek independent confirmation
  or downgrade to "unconfirmed."
- If bot/astroturf content is not screened: apply detection heuristics.
- If satire is mistaken for fact: correct and flag the error.
- If signal-to-noise ratio is undocumented: calculate and report it.

## Escalation Rules

- Escalate if the signal-to-noise ratio is below 20% (mostly noise).
- Escalate if coordinated disinformation campaigns are detected around
  the topic.
- Escalate if OSINT findings contradict verified intelligence and the
  discrepancy cannot be resolved.
