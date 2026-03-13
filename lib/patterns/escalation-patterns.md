# Escalation Patterns

## Pattern Name: Confidence Threshold Escalation

**Problem:** A critical finding cannot achieve the minimum confidence level required,
and further research has diminishing returns.

**Solution:** Define confidence thresholds at project start. When a critical claim remains
below threshold after reasonable effort, escalate to a human expert. Provide current
evidence, the confidence gap, and what has been tried.

**When to Use:** When confidence on a critical claim is below 0.6 after two or more
research iterations.

**Example:** After 8 sources, cross-region latency confidence remains 0.45. Escalate:
"Need expert validation or proof-of-concept to resolve."

---

## Pattern Name: Scope Escalation

**Problem:** The original question cannot be answered without expanding scope significantly.

**Solution:** Document the scope gap and impact. Present options: (1) expand scope and
timeline, (2) deliver partial findings with gaps, (3) reframe the question to fit scope.

**When to Use:** When proper answers require investigating domains beyond the mandate.

**Example:** "Cannot recommend a database without understanding ingestion patterns, which
is out of scope. Recommend expanding scope or accepting assumption X."

---

## Pattern Name: Contradiction Escalation

**Problem:** A critical contradiction blocks the recommendation and cannot be resolved.

**Solution:** Escalate with full documentation: both claims, sources, evidence, resolution
methods tried, and impact on deliverables. Request expert judgment or authorization
to proceed with an explicit assumption.

**When to Use:** When a critical contradiction remains unresolved after attempting all
contradiction resolution patterns.

**Example:** "Two authoritative sources disagree on consistency guarantees. Recommend
contacting vendor engineering or running a Jepsen-style test."

---

## Pattern Name: Time Pressure Escalation

**Problem:** The research timeline is insufficient for the required depth.

**Solution:** Escalate proactively when the gap between required and achievable quality is
clear. Present what can be delivered in available time vs. what needs more time.

**When to Use:** When remaining effort exceeds available time by more than 30%.

**Example:** "Full evaluation needs 3 more days. In 1 day, I can compare top 2 candidates
with gaps documented for others. Which approach do you prefer?"
