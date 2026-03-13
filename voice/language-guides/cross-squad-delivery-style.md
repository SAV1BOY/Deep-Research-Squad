# Cross-Squad Delivery Style Guide

## Purpose

This guide defines how to write deliverables intended for other squads.
Cross-squad communication requires context that internal communication does not.
The receiving squad did not attend your standups. Write accordingly.

## Core Principles

1. **Assume no shared context.** Define terms, explain relevance, state scope.
2. **Lead with what they need, not what you did.** The process is irrelevant to them.
3. **Map findings to their domain.** Translate your output into their language.
4. **Include provenance.** They need to know where the intelligence came from.
5. **Specify confidence.** They will make decisions based on your work.

## Delivery Structure

### Header Block

Every cross-squad deliverable starts with a metadata header:

```
From: [Your Squad / Agent Role]
To: [Receiving Squad / Role]
Date: [Delivery Date]
Classification: [Research / Intelligence / Recommendation]
Confidence: [High / Medium / Low]
Scope: [What this covers and what it does not]
```

### Body Structure

- **Context:** Why this is being delivered and what triggered it (2-3 sentences).
- **Key Findings:** Bulleted, with confidence level per finding.
- **Relevance to Recipient:** Explicit mapping to their work or decisions.
- **Caveats and Limitations:** What the recipient should not infer from this.
- **Source Summary:** Where the data came from, at what evidence tier.
- **Suggested Actions:** What the recipient might do with this (optional).

## Translation Protocol

When delivering to a squad with a different domain:
- Replace your jargon with theirs.
- Use analogies to bridge domains when precision is not sacrificed.
- Include a glossary if more than three technical terms are unavoidable.

### Examples

- To Engineering: Frame in terms of systems, architectures, trade-offs.
- To Product: Frame in terms of user impact, market implications, priorities.
- To Legal: Frame in terms of risk exposure, compliance, precedent.
- To Finance: Frame in terms of cost, revenue impact, projections.

## Handoff Checklist

Before delivering cross-squad, verify:

- [ ] Metadata header is complete.
- [ ] No undefined jargon from your domain.
- [ ] Confidence level is stated per finding.
- [ ] Scope boundaries are explicit (what is and is not covered).
- [ ] Source provenance is included.
- [ ] The recipient can act on this without follow-up questions.

## Common Mistakes

- Assuming the recipient has your context.
- Using internal shorthand or acronyms.
- Delivering raw findings without interpretation for their domain.
- Omitting confidence levels (they will assume "confirmed").
- Not stating what is out of scope (they will assume you covered everything).

## Quality Check

- Would someone with zero context on your project understand this?
- Is every finding tagged with a confidence level?
- Is the relevance to the recipient explicit?
- Can the recipient act without needing to ask clarifying questions?
