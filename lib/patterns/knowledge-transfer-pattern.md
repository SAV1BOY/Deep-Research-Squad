# Knowledge Transfer Pattern

## Pattern Name: Structured Knowledge Transfer

**Problem:** Research findings lose value when they cannot be effectively transferred
to downstream consumers — whether that is a different team, a future research effort,
or a decision-maker unfamiliar with the domain. Knowledge is lost in handoffs.

**Solution:** Apply a structured knowledge transfer protocol that packages research
outputs with sufficient context, provenance, and accessibility for the target audience.

---

## Transfer Modes

### Mode 1 — Deliverable Handoff
**Use when:** Completed research is delivered to the requesting stakeholder.
**Package includes:**
- Final deliverable in requested format
- Methodology disclosure (see methodology-disclosure-component)
- Source index with access instructions
- Confidence summary by finding
- Known gaps and suggested follow-up questions

### Mode 2 — Research Continuation
**Use when:** Another researcher or team will continue or extend this research.
**Package includes:**
- All Mode 1 items, plus:
- Research log: what was tried, what worked, what did not
- Dead ends documented (to avoid re-exploration)
- Working hypotheses not yet validated
- Source leads not yet pursued
- Tool configurations and search queries used

### Mode 3 — Decision Support
**Use when:** Research feeds directly into a decision process.
**Package includes:**
- Decision brief (see research-brief-component)
- Decision-relevant findings only (filtered from full research)
- Options with tradeoffs mapped to findings
- Risk factors with confidence levels
- "What would change this recommendation" triggers

---

## Transfer Quality Checklist

| Criterion | Required For |
|-----------|-------------|
| Findings are self-contained (readable without prior context) | All modes |
| Sources are accessible to the recipient | All modes |
| Confidence scores explained, not just stated | All modes |
| Methodology is documented | All modes |
| Dead ends are recorded | Mode 2 |
| Search queries and tool configs preserved | Mode 2 |
| Findings filtered for decision relevance | Mode 3 |
| Decision options explicitly tied to evidence | Mode 3 |

## Transfer Anti-Patterns

- **Data dump**: Handing over raw notes without synthesis
- **Orphaned context**: Findings that make sense only to the original researcher
- **Confidence theater**: Scores without justification
- **Perfectionism**: Withholding useful partial findings while waiting for completeness
- **Channel mismatch**: Sending a 40-page report when a 1-page brief was needed

## Audience Calibration

| Audience | Preferred Format | Detail Level | Jargon Tolerance |
|----------|-----------------|-------------|------------------|
| C-suite | 1-page brief | Conclusions only | Low |
| VP/Director | 3-5 page report | Findings + key evidence | Medium |
| Technical lead | Full report + appendices | Full evidence chain | High |
| Research peer | Raw research package | Everything including dead ends | High |
| Legal/compliance | Structured evidence table | Precise citations required | Domain-specific |

## Implementation

1. Identify transfer mode based on recipient and purpose
2. Package deliverable using the appropriate checklist
3. Calibrate format and detail level to audience
4. Verify recipient can access all referenced sources
5. Include explicit "questions this does not answer" section
