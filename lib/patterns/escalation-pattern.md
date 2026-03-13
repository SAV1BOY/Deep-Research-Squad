# Escalation Pattern

## Pattern Name: Structured Research Escalation

**Problem:** During research, situations arise that require human intervention,
expanded scope, additional resources, or stakeholder decisions. Without a standard
escalation protocol, these situations cause delays, scope creep, or silent failures.

**Solution:** Define a tiered escalation framework with clear triggers, routing
rules, and required context for each escalation type.

---

## Escalation Tiers

### Tier 1 — Informational Escalation
**Trigger:** Research is proceeding but stakeholder should be aware of a finding.
**Action:** Log finding and continue. Include in next scheduled update.
**Required context:** Finding summary, confidence, relevance to original question.
**Example:** "Discovered that target company's CTO departed last month — may affect
technology assessment. Continuing with analysis."

### Tier 2 — Decision Required
**Trigger:** Research has reached a branch point that requires stakeholder input.
**Action:** Pause affected workstream. Present options with tradeoffs.
**Required context:** Decision needed, options (2-3), tradeoffs, recommendation,
deadline for decision before it blocks progress.
**Example:** "Competitor analysis reveals two distinct market segments. Should we
analyze both (adds 2 days) or prioritize enterprise segment only?"

### Tier 3 — Scope Expansion
**Trigger:** Original question cannot be adequately answered within current scope.
**Action:** Document scope gap. Present expansion options with resource/time impact.
**Required context:** Original scope, why it is insufficient, proposed expanded scope,
additional time/resources needed, alternative: deliver partial findings.
**Example:** "Regulatory analysis requires jurisdiction-specific review for 4 additional
countries. Expansion adds 3 days. Alternative: general assessment with country-specific
gaps flagged."

### Tier 4 — Confidence Failure
**Trigger:** Critical finding cannot reach minimum confidence threshold despite
reasonable research effort.
**Action:** Escalate to human expert or additional data source.
**Required context:** Claim in question, current confidence, target confidence,
what has been tried, what would resolve the gap.
**Example:** "Cannot confirm market size estimate above 0.55 confidence after 12
sources. Three sources contradict. Recommend expert interview or proprietary data."

### Tier 5 — Critical Finding
**Trigger:** Research uncovers something that demands immediate stakeholder attention
regardless of research completion status.
**Action:** Immediate notification. Do not wait for scheduled update.
**Required context:** Finding, evidence, confidence, potential impact, recommended
immediate action.
**Example:** "Target acquisition company has undisclosed pending litigation that
could materially affect valuation. Recommend legal review before proceeding."

---

## Escalation Message Template

```
ESCALATION — Tier [1-5]: [Category]

Finding: [One sentence]
Confidence: [0-1.0]
Impact: [What this affects]

Context: [2-3 sentences of background]

Options:
  A. [Option with tradeoff]
  B. [Option with tradeoff]

Recommendation: [If applicable]
Decision needed by: [Date/time]
```

## Anti-Patterns
- **Silent swallowing**: Absorbing a problem without surfacing it
- **Over-escalation**: Escalating decisions that are within research discretion
- **Context-free escalation**: "I found a problem" without evidence or options
- **Delayed critical escalation**: Waiting for a scheduled update on Tier 5 items
