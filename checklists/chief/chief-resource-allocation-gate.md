# Chief Resource Allocation Gate

## Purpose

Confirm that the correct agents have been assigned to the research task and
that no critical capability gap exists in the allocated team. Ensures efficient
use of agent capacity and prevents bottlenecks.

## Gate Question

**Are the right agents allocated with appropriate capacity for this research
task?**

## Prerequisites

- Approved scope document with identified research layers.
- Agent capability matrix available (which agent handles which layer).
- Current agent workload dashboard reviewed.
- Methodology recommendation from Architect Agent received.

## Pass Criteria

1. Every research layer in the scope maps to at least one assigned agent.
2. No single agent is assigned more than 3 concurrent layers.
3. Critical-path agents (Source, Evidence, Verification) are not overloaded.
4. Specialist agents (OSINT, Data, Literature) are included when the scope
   requires their domain expertise.
5. Contrarian Agent is assigned for any research rated high-confidence or
   high-stakes.
6. Synthesis Agent is pre-allocated and aware of the expected input format.
7. Estimated total agent-hours fit within the time budget.

## Fail Actions

- If a required capability is missing: activate the dormant specialist agent
  or flag the gap for manual coverage.
- If an agent is overloaded: redistribute tasks or queue lower-priority work.
- If Contrarian Agent is omitted on high-stakes research: add immediately
  and note the oversight.
- If total agent-hours exceed budget: negotiate scope reduction with requester
  or request deadline extension.

## Escalation Rules

- Escalate if no agent can cover a required research layer (capability gap).
- Escalate if more than 50% of agents are at capacity and new P0 arrives.
- Escalate if resource conflict exists between two P0 tasks requiring the
  same specialist agent simultaneously.
- Escalate if an agent repeatedly fails quality gates, suggesting it should
  be replaced or retrained.
