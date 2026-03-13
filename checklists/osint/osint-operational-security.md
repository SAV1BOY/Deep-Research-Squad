# OSINT Operational Security Gate

## Purpose

Ensure that the OSINT collection process does not expose the research team,
its methods, or its targets to unnecessary risk. Poor operational security
can tip off targets, reveal collection interests, or compromise the team.

## Gate Question

**Is operational security maintained throughout the OSINT process?**

## Prerequisites

- Threat model for the research engagement defined.
- Operational security (OPSEC) policy reviewed.
- Collection tools and their footprint assessed.
- Team's digital exposure understood.

## Pass Criteria

1. Collection activities do not reveal the identity or intent of the
   research team to the target.
2. Searches are conducted through privacy-preserving methods when the
   topic is sensitive.
3. No direct contact with the target was made without authorization.
4. Collection tools do not leak metadata about the research team.
5. Downloaded files are scanned for tracking mechanisms (web beacons,
   metadata).
6. Research notes and collected data are stored securely.
7. OPSEC measures are proportionate to the sensitivity of the research.

## Fail Actions

- If team identity was exposed: assess the impact and adjust collection
  strategy.
- If privacy-preserving methods were not used: switch to them for
  remaining collection.
- If unauthorized contact was made: report it and assess consequences.
- If metadata leakage occurred: mitigate by changing tools or methods.
- If data is not stored securely: move it to a secure location
  immediately.

## Escalation Rules

- Escalate immediately if the target appears to be aware of the
  investigation.
- Escalate if collection tools are compromised or behaving unexpectedly.
- Escalate if the sensitivity level of the research increases mid-task
  and OPSEC measures need to be strengthened.
- Escalate if any team member's identity is exposed in connection with
  the research.
