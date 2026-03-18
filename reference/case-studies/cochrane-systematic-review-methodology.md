# Cochrane Systematic Review Methodology

## Background

The Cochrane Collaboration, founded in 1993 and named after British epidemiologist Archie Cochrane, established the global gold standard for evidence-based research methodology. Cochrane's central insight was that individual studies are unreliable in isolation -- only systematic synthesis of all available evidence produces trustworthy conclusions. The organization now maintains over 8,000 systematic reviews across healthcare, each following a rigorous, pre-registered protocol.

Cochrane methodology matters to Deep Research Squad because it solves the same problem we face: how to synthesize evidence from multiple sources of varying quality into conclusions with calibrated confidence. Their methods for preventing cherry-picking, assessing bias, and grading certainty are directly transferable to intelligence research, even when operating at faster timescales.

## Core Methodology

### Protocol-Driven Research

Every Cochrane review begins with a published protocol -- a detailed plan specifying the research question, search strategy, inclusion/exclusion criteria, and analysis methods before any evidence is examined. The protocol is registered publicly, making post-hoc rationalization visible and accountable.

The protocol answers: What question are we answering? Where will we look? What counts as relevant evidence? How will we assess quality? How will we synthesize findings? These decisions are made before the researcher encounters any data, eliminating the temptation to adjust criteria to fit desired conclusions.

### Inclusion and Exclusion Criteria

Cochrane defines explicit, reproducible rules for what evidence enters the review. Criteria typically cover population, intervention, comparison, outcome, and study design (the PICO framework plus study type). Two independent reviewers apply criteria to every candidate study. Disagreements are resolved by a third reviewer, not by compromise.

This discipline prevents the most common evidence synthesis failure: unconsciously including studies that support the preferred conclusion and excluding those that challenge it.

### Risk of Bias Assessment

Every included study is assessed for bias across standardized domains: selection bias, performance bias, detection bias, attrition bias, reporting bias, and other sources. Studies are not simply labeled "good" or "bad" -- specific bias risks are documented for each domain, producing a granular quality profile.

This assessment directly informs synthesis: when high-bias and low-bias studies reach different conclusions, the systematic reviewer knows which findings to weight more heavily and can test whether removing high-risk studies changes the overall result.

### Meta-Analysis and Heterogeneity

When studies are sufficiently comparable, Cochrane combines results using statistical meta-analysis. Forest plots display individual study effects and the pooled estimate. Critically, heterogeneity statistics (the I-squared measure) quantify how much variation exists across studies beyond chance.

High heterogeneity is a signal, not a problem to suppress. It means the included studies are measuring different things or operating in different contexts. Cochrane requires reviewers to investigate sources of heterogeneity through subgroup analysis rather than burying it in a pooled average.

### GRADE Certainty Assessment

The GRADE framework (Grading of Recommendations Assessment, Development and Evaluation) assigns certainty levels to each finding: High, Moderate, Low, or Very Low. Certainty can be downgraded for risk of bias, inconsistency, indirectness, imprecision, or publication bias. It can be upgraded for large effect sizes, dose-response gradients, or confounders that would reduce the observed effect.

GRADE separates the question "what does the evidence show?" from "how confident are we in what the evidence shows?" This distinction is fundamental to honest research communication.

## Key Techniques

| Technique | Purpose | Deep Research Squad Parallel |
|---|---|---|
| Pre-registered protocol | Prevent post-hoc rationalization | Research brief created at `workflows/01-request-to-research-plan.md` before collection begins |
| PICO question framing | Structure the research question precisely | Scope Mapper's problem framing at `frameworks/scope-mapper/scope-mapper-problem-framing.md` |
| Dual-reviewer screening | Reduce individual bias in evidence selection | Evidence Verifier's cross-source validation at `frameworks/evidence-verifier/evidence-verifier-cross-source.md` |
| PRISMA flow documentation | Make the evidence selection process transparent | Source Hunter's inclusion/exclusion tracking in source maps |
| Risk of bias tables | Assess evidence quality systematically | Evidence Verifier's claim grid at `frameworks/evidence-verifier/evidence-verifier-claim-grid.md` |
| Sensitivity analysis | Test whether conclusions depend on weak evidence | Evidence falsification protocol at `frameworks/evidence-verifier/evidence-verifier-falsification.md` |
| GRADE certainty levels | Calibrate confidence in findings | Confidence weighting framework at `frameworks/confidence-weighting.md` |

## Lessons for Deep Research Squad

**Adopt fully:**
- Protocol-first discipline. No collection begins until the research brief defines what we are looking for, where we will look, and what counts as relevant. This maps directly to `workflows/00-research-request-intake.md` and `workflows/02-scope-and-decomposition.md`.
- Explicit inclusion/exclusion criteria. The Source Hunter must document why sources were included or excluded, not just which sources were used. See `frameworks/source-hunter/source-hunter-signal-noise-scoring.md` for the scoring mechanism.
- Bias assessment of every source. The Evidence Verifier must evaluate each source for specific bias risks, not just assign a generic quality score. The `checklists/evidence/evidence-strength-gate.md` enforces this at the quality gate.
- Certainty grading separate from findings. Our confidence levels (High, Medium, Low, Contested) must reflect genuine epistemic state, calibrated using `frameworks/confidence-weighting.md`, never inflated to sound more authoritative.

**Adapt with caution:**
- Cochrane reviews take 12-24 months. We operate in hours to days. Our adaptation is the "rapid systematic review" -- following the protocol discipline and bias assessment while accepting narrower search scope. The key is being transparent about what scope limitations exist, not pretending our faster process is equally comprehensive.
- Dual-reviewer screening requires two independent assessors. In our system, the Evidence Verifier and Contrarian Analyst serve analogous roles -- the Verifier assesses evidence quality while the Contrarian actively seeks disconfirming evidence. See `workflows/06-contradiction-hunt.md`.
- Meta-analysis requires quantitative data in comparable formats. Most of our evidence is qualitative or mixed. Our `frameworks/literature-analyst/literature-meta-analysis-lite.md` adapts meta-analytic thinking for qualitative synthesis.

**Reject explicitly:**
- Nothing in Cochrane methodology should be rejected. The question is always degree of adaptation, not whether to apply these principles. Any research system that ignores protocol discipline, bias assessment, or certainty calibration is doing something worse than Cochrane, not something different.

## Anti-Patterns to Avoid

1. **Protocol drift.** Changing inclusion criteria mid-research to accommodate inconvenient findings. Once the research brief is set, scope changes require explicit documentation and Chief Research Architect approval.
2. **Quality assessment theater.** Filling out bias checklists without actually changing how evidence is weighted. If a source scores poorly on bias assessment, that must visibly reduce its influence on conclusions.
3. **Heterogeneity suppression.** When sources disagree, the temptation is to explain away disagreement rather than investigate it. Our `frameworks/contradiction-mapping.md` and `workflows/06-contradiction-hunt.md` make disagreement a first-class research finding.
4. **Certainty inflation.** Reporting "High confidence" when evidence is sparse or contested. The `checklists/evidence/evidence-consistency-gate.md` checks for alignment between stated confidence and actual evidence strength.
5. **Comprehensiveness without discrimination.** Collecting everything available without assessing relevance or quality. Volume of sources is not a proxy for rigor. See `frameworks/source-hunter/source-hunter-authority-proximity.md` for quality-based source prioritization.

## References

- Higgins, Julian P.T. and Sally Green, eds. *Cochrane Handbook for Systematic Reviews of Interventions*. Cochrane Collaboration/Wiley, 2008.
- Moher, David et al. "Preferred Reporting Items for Systematic Reviews and Meta-Analyses: The PRISMA Statement." *PLoS Medicine* 6.7 (2009).
- Guyatt, Gordon et al. "GRADE: An Emerging Consensus on Rating Quality of Evidence and Strength of Recommendations." *BMJ* 336 (2008).
- Cochrane, Archie. *Effectiveness and Efficiency: Random Reflections on Health Services*. Nuffield Provincial Hospitals Trust, 1972.
- See also: `archive/iconic-research/cochrane-systematic-reviews.md` for the foundational reference.
- See also: `frameworks/literature-analyst/literature-systematic-review.md` for our adapted systematic review framework.
