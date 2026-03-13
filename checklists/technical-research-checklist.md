# Technical Research Quality Checklist

## Purpose
Ensure that technical research deliverables meet standards for accuracy, depth, and practical applicability. This checklist validates that technical evaluations, architecture assessments, and technology analyses are rigorous and useful for engineering and product decisions.

## When to Use
- Before delivering technical research reports, evaluations, or recommendations
- When reviewing technology comparison analyses or proof-of-concept findings
- During assessment of architecture, infrastructure, or tooling research
- When technical research feeds into build-vs-buy or adoption decisions

## Prerequisites
- Technical research scope and questions have been defined
- Target technology stack, constraints, and requirements are documented
- Access to relevant technical documentation, repositories, and environments is confirmed
- Evaluation criteria and weighting have been agreed upon with stakeholders
- Subject matter experts have been identified for consultation

## Checklist Items

### Section 1: Problem Definition and Scope
1. [ ] Technical problem or research question is clearly articulated — PASS: specific and measurable question; FAIL: vague or ambiguous
2. [ ] Scope boundaries are defined (what is in and out of scope) — PASS: explicit boundaries; FAIL: unbounded investigation
3. [ ] Success criteria or evaluation framework is established upfront — PASS: criteria defined before research; FAIL: criteria developed post-hoc
4. [ ] Constraints (budget, timeline, existing stack, compliance) are documented — PASS: constraints listed; FAIL: constraints not considered

### Section 2: Technical Depth and Accuracy
5. [ ] Architecture or system design is described with appropriate diagrams — PASS: diagrams present and accurate; FAIL: text-only description of complex systems
6. [ ] Technical claims are verified through documentation, testing, or expert validation — PASS: claims verified; FAIL: unverified vendor claims repeated
7. [ ] Performance characteristics are quantified where applicable — PASS: benchmarks or metrics provided; FAIL: qualitative performance claims only
8. [ ] Scalability considerations are addressed — PASS: scaling analysis present; FAIL: scalability not discussed
9. [ ] Security implications are evaluated — PASS: security assessment included; FAIL: security not considered
10. [ ] Integration complexity with existing systems is assessed — PASS: integration analysis done; FAIL: standalone evaluation only

### Section 3: Evaluation Methodology
11. [ ] Evaluation criteria are weighted by importance — PASS: weighted scoring; FAIL: unweighted or no criteria
12. [ ] At least 3 alternatives or approaches are evaluated — PASS: 3+ options compared; FAIL: fewer than 3 without justification
13. [ ] Hands-on testing or proof-of-concept has been conducted where feasible — PASS: practical testing done; FAIL: theoretical evaluation only when testing was possible
14. [ ] Trade-offs between options are explicitly documented — PASS: trade-off matrix present; FAIL: trade-offs not discussed
15. [ ] Total cost of ownership (TCO) is estimated for recommended options — PASS: TCO analysis included; FAIL: upfront cost only

### Section 4: Risk and Feasibility
16. [ ] Technical risks are identified and rated by likelihood and impact — PASS: risk assessment present; FAIL: risks not cataloged
17. [ ] Mitigation strategies are proposed for high-priority risks — PASS: mitigations documented; FAIL: risks identified without mitigations
18. [ ] Implementation timeline and resource requirements are estimated — PASS: timeline and effort estimated; FAIL: no implementation planning
19. [ ] Dependencies on external systems, teams, or vendors are mapped — PASS: dependencies identified; FAIL: dependency blind spots
20. [ ] Vendor or community support and longevity are assessed for external technologies — PASS: sustainability evaluated; FAIL: no longevity analysis

### Section 5: Documentation and Reproducibility
21. [ ] All test environments, configurations, and versions are documented — PASS: reproducible setup; FAIL: environment details missing
22. [ ] Code samples, scripts, or configurations are included where relevant — PASS: artifacts provided; FAIL: verbal descriptions of code
23. [ ] Recommendation is clearly stated with supporting rationale — PASS: explicit recommendation; FAIL: ambiguous conclusion
24. [ ] Dissenting views or minority opinions from experts are noted — PASS: alternative perspectives included; FAIL: single viewpoint only
25. [ ] Next steps for implementation or further evaluation are outlined — PASS: action plan provided; FAIL: no forward path

## Scoring
- Count the total number of items marked PASS
- Quality Score = (PASS count / 25) x 100
- Grade thresholds:
  - 92-100%: Excellent — technically rigorous and implementation-ready
  - 80-91%: Good — sound research with minor gaps
  - 68-79%: Acceptable — needs strengthening before decisions are made
  - Below 68%: Insufficient — major gaps in technical rigor

## Escalation
- **Accept**: Score of 80% or above with no FAIL on items 1, 6, 7, or 16
- **Revise**: Score of 68-79%, or any FAIL on items 1, 6, 7, or 16
- **Escalate to lead**: Score below 68%, or fundamental technical accuracy concerns, or evaluation methodology questioned by subject matter experts
- **Escalate to stakeholder**: Research reveals that original technical assumptions are invalid, or timeline for decision is at risk due to evaluation complexity
