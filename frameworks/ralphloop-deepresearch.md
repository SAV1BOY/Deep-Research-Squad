# RalphLoop Deep Research

## Purpose
A complete iterative research cycle with 18 discrete steps (R1-R18) that provides granular control over every phase of deep research. Named for its loop structure — R18 feeds back into R1 for iterative refinement.

## When to Use
- Complex, multi-session research requiring coordination across multiple agents
- When the simpler Research Stack needs to be expanded into actionable steps
- High-stakes research where auditability and quality gates at every step are essential
- Any research that will be updated over time (the loop enables iterative deepening)

## Inputs
- Research request from a user or upstream system
- Any prior research artifacts from previous loop iterations
- Memory context from earlier sessions

## Process (step-by-step)

### R1: Receive Request
**Agent:** Query Strategist | **Inputs:** Raw user request | **Outputs:** Parsed request with intent, constraints, urgency
**Quality Gate:** Request is unambiguous; clarification sought if not.

### R2: Frame Problem
**Agent:** Query Strategist | **Inputs:** Parsed request | **Outputs:** Problem statement, success criteria, key assumptions
**Quality Gate:** Problem statement is falsifiable and scoped.

### R3: Define Scope
**Agent:** Scope Mapper | **Inputs:** Problem statement | **Outputs:** Scope boundary (in/out), depth targets, resource allocation
**Quality Gate:** Scope is bounded and achievable within constraints.

### R4: Design Architecture
**Agent:** Scope Mapper | **Inputs:** Scope boundary | **Outputs:** Research plan, agent assignments, dependency graph
**Quality Gate:** Every scope element has an assigned agent and method.

### R5: Plan Sources
**Agent:** Source Hunter | **Inputs:** Research plan | **Outputs:** Prioritized source list, access plan, search strategies
**Quality Gate:** At least 3 independent source categories; no single-category dependency.

### R6: Execute Search
**Agent:** Data Researcher | **Inputs:** Source list, search strategies | **Outputs:** Raw search results, access logs
**Quality Gate:** Search coverage matches the source plan; gaps documented.

### R7: Collect Evidence
**Agent:** Data Researcher | **Inputs:** Raw search results | **Outputs:** Structured evidence cards (claim, source, date, relevance)
**Quality Gate:** Every evidence card has provenance and a relevance tag.

### R8: Verify Claims
**Agent:** Evidence Verifier | **Inputs:** Evidence cards | **Outputs:** Verified/unverified/disputed classification for each card
**Quality Gate:** Key claims have independent corroboration or are flagged.

### R9: Map Contradictions
**Agent:** Evidence Verifier | **Inputs:** Verified evidence set | **Outputs:** Contradiction map with severity ratings
**Quality Gate:** No contradiction is left unacknowledged.

### R10: Build Timeline
**Agent:** Timeline Analyst | **Inputs:** Verified evidence | **Outputs:** Chronological event sequence, causal links
**Quality Gate:** Timeline is internally consistent; gaps are marked.

### R11: Analyze Data
**Agent:** Insight Modeler | **Inputs:** Verified evidence, timeline, contradiction map | **Outputs:** Patterns, trends, anomalies, statistical summaries
**Quality Gate:** Analysis accounts for contradictions; anomalies are explained or flagged.

### R12: Run Contrarian Pass
**Agent:** Contrarian Analyst | **Inputs:** Preliminary analysis | **Outputs:** Counter-arguments, alternative explanations, blind spot report
**Quality Gate:** At least 2 substantive counter-arguments generated and addressed.

### R13: Synthesize Layer 1 (Certainties)
**Agent:** Synthesis Writer | **Inputs:** Verified, corroborated evidence | **Outputs:** High-confidence conclusions with evidence chains
**Quality Gate:** Every certainty has 3+ independent supporting sources.

### R14: Synthesize Layer 2 (Probabilities)
**Agent:** Synthesis Writer | **Inputs:** Moderate-confidence evidence, model outputs | **Outputs:** Probabilistic conclusions with confidence ranges
**Quality Gate:** Each conclusion has an explicit probability range and key assumptions stated.

### R15: Build Models
**Agent:** Insight Modeler | **Inputs:** Synthesized conclusions | **Outputs:** Explanatory models, scenario trees, decision frameworks
**Quality Gate:** Models are internally consistent and account for contradictions.

### R16: Translate to Decisions
**Agent:** Decision Analyst | **Inputs:** Models, scenarios | **Outputs:** Options, trade-offs, ranked recommendations, reversal conditions
**Quality Gate:** Every recommendation has confidence level and reversal condition.

### R17: Audit Quality
**Agent:** Decision Analyst | **Inputs:** Complete research artifact | **Outputs:** Quality scorecard, gap list, bias assessment
**Quality Gate:** No critical gaps; bias risks documented.

### R18: Update Memory
**Agent:** All Agents | **Inputs:** Final artifact, quality scorecard | **Outputs:** Updated memory store, lessons learned, iteration trigger
**Quality Gate:** Key findings persisted; loop-back decision made (stop or re-enter at R1).

## Outputs
- Complete research artifact with full audit trail
- Quality scorecard with gap analysis
- Updated memory for future iterations
- Decision on whether to loop (iterate) or finalize

## Common Pitfalls
- Treating the loop as strictly linear — skip back to earlier steps when evidence demands it
- Skipping R12 (Contrarian Pass) — this is where blind spots are caught
- Rushing R8-R9 (Verification) under time pressure — unverified claims poison downstream synthesis
- Not persisting to memory in R18 — losing institutional knowledge across sessions
- Over-iterating when diminishing returns have set in — know when to stop the loop

## Related Frameworks
- research-stack.md (the 4-layer abstraction this loop implements)
- pre-mortem-research.md (complementary to R12 Contrarian Pass)
- bayesian-updating.md (used within R8 and R11)
- epistemic-humility-framework.md (used in R13-R14 for confidence classification)

## Templates (recommended)

### Evidence Card (R7)
```
Claim: [statement]
Source: [full reference]
Date: [when published/observed]
Relevance: [High / Medium / Low]
Verification Status: [Pending / Verified / Disputed / Unverifiable]
```

### Contradiction Entry (R9)
```
Claim A: [statement] — Source: [ref]
Claim B: [conflicting statement] — Source: [ref]
Severity: [Critical / Moderate / Minor]
Resolution: [Resolved / Open / Irrelevant]
```

### Quality Scorecard (R17)
```
Evidence Coverage: [% of scope covered]
Verification Rate: [% of claims verified]
Contradiction Resolution: [% resolved]
Source Diversity: [number of independent categories]
Contrarian Challenges Addressed: [count]
Overall Confidence: [Certain / Probable / Plausible / Speculative]
```
