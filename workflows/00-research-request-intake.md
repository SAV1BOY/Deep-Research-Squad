# Workflow 00: Research Request Intake

## Purpose
Receive, decode, and classify incoming research requests. Parse the requester's intent, classify the research type, assess complexity and effort, and determine priority ranking so the squad can allocate resources effectively from the first moment.

## Trigger
- A new research request arrives via any input channel (chat, API, internal handoff, cross-squad request).
- A previously paused or deferred request is reactivated.

## Agents Involved
- **Research Lead**: Owns intake triage and final classification.
- **Intent Decoder**: Parses raw request into structured components.
- **Complexity Assessor**: Scores effort, ambiguity, and domain difficulty.

## Inputs
- Raw research request (text, voice transcript, or structured form).
- Requester identity and context (role, squad, urgency signals).
- Historical request log for deduplication check.
- Research type taxonomy (reference classification for categorization).
- Priority framework (criteria and tier definitions for ranking).

## Steps

1. **Receive raw request**: Capture the incoming request verbatim. Log timestamp, source channel, and requester identity. Assign a unique request ID.

2. **Deduplication check**: Query the request registry for semantically similar past requests. If a match is found with >85% similarity, flag it and link to the prior research output. Decide whether to reuse, update, or start fresh.

3. **Parse intent**: Extract the core question the requester is actually asking. Identify explicit goals (what they stated) and implicit goals (what they likely need but did not articulate). Rewrite the request as a clear, unambiguous research question.

4. **Classify research type**: Assign one or more type labels from the taxonomy:
   - Fact-finding (what is true?)
   - Comparative analysis (which option is better?)
   - Causal investigation (why did this happen?)
   - Forecasting (what will happen?)
   - Decision support (what should we do?)
   - Landscape mapping (what exists in this space?)

5. **Assess complexity**: Score the request on four dimensions (1-5 each):
   - **Breadth**: How many sub-questions or domains are involved?
   - **Depth**: How deep must the analysis go?
   - **Ambiguity**: How well-defined is the question?
   - **Data availability**: How accessible are the needed sources?
   - Compute a composite complexity score (sum / 20).

6. **Determine priority**: Combine complexity score with urgency signals from the requester, strategic importance, and current squad workload. Assign a priority tier: P0 (drop everything), P1 (next in queue), P2 (scheduled), P3 (backlog).

7. **Identify domain signals**: Flag any specialized domains (legal, medical, financial, technical) that may require domain specialist activation later. Cross-reference against the specialist roster to confirm availability.

8. **Estimate resource requirements**: Based on complexity and type, produce a preliminary estimate of:
   - Number of agents needed (collection, analysis, synthesis).
   - Estimated calendar time (hours, days, or weeks).
   - Key tool and data dependencies.
   - This is a rough estimate refined in Workflow 01.

9. **Draft intake summary**: Produce a structured intake card containing: request ID, parsed question, research type, complexity score, priority tier, domain flags, resource estimate, estimated timeline range, and any open clarification questions.

10. **Stakeholder notification**: Notify relevant stakeholders that the request has been received:
    - Send acknowledgment to the requester with the request ID and estimated timeline.
    - Notify the Research Lead that a new request is queued for review.
    - If priority is P0, send immediate alert to all available agents.

11. **Clarification round (if needed)**: If ambiguity score is >= 3, send clarification questions back to the requester before proceeding. Prepare specific, targeted questions (not open-ended). Set a timeout for response (default: 24 hours). If timeout expires, proceed with assumptions documented.

12. **Approve and route**: Research Lead reviews the intake card, approves or modifies it, and routes the request to the next workflow. If the card is rejected, document the rejection reason and notify the requester.

## Quality Gates
- Parsed question must be a single, answerable research question (no compound questions without decomposition).
- Complexity score must be justified with brief reasoning for each dimension.
- Priority assignment must reference at least one objective criterion (not just requester urgency).
- Deduplication check must be completed before any new work begins.
- Intake card must be fully populated with no blank fields.
- Requester must receive acknowledgment within 1 hour of request receipt.
- Resource estimate must be provided even if preliminary.

## Outputs
- Approved intake card (structured document).
- Request entry in the research request registry.
- Clarification questions sent to requester (if applicable).
- Routing decision to next workflow.

## Next Workflow
- **01-request-to-research-plan.md** (default path).
- **17-domain-specialist-escalation.md** (if domain flags indicate specialist needed at intake).
