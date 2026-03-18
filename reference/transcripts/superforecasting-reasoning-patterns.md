# Superforecasting Reasoning Patterns

## Introduction

Philip Tetlock's research on superforecasting, published in *Superforecasting: The Art and Science of Prediction* (2015) and drawn from the multi-year Good Judgment Project, identified a set of cognitive strategies that separate elite forecasters from domain experts and casual predictors. Superforecasters are not smarter or more credentialed -- they think differently. They update often, decompose rigorously, and resist the gravitational pull of narrative certainty.

This transcript distills the core reasoning patterns that the DeepResearch Squad draws on when producing probabilistic assessments, calibrating confidence, and evaluating competing hypotheses. The primary framework implementation lives at `frameworks/reference-intellectual/tetlock-superforecasting.md`.

## Key Reasoning Patterns

### 1. Base Rate Thinking (Outside View First)

**Description:** Before analyzing any case-specific detail, superforecasters ask: "How often does this type of thing happen in general?" The base rate anchors the estimate in empirical frequency rather than anecdotal impression. Only after establishing the outside view do they adjust for inside-view details.

**Example:** When estimating the probability that a startup will reach Series B funding, a superforecaster starts with the historical rate (roughly 30-35% of Series A companies) rather than the founder's pitch narrative, then adjusts based on sector, team, and traction specifics.

### 2. Incremental Bayesian Updating

**Description:** Superforecasters treat beliefs as probabilities to be updated, not positions to be defended. Each new piece of evidence shifts the estimate by an amount proportional to the evidence's diagnostic value -- its ability to distinguish between competing hypotheses. They avoid both anchoring (refusing to move) and overreaction (swinging wildly on a single data point).

**Example:** An initial estimate that a regulation will pass might be 40%. A credible insider report of bipartisan support shifts it to 55%. A subsequent committee delay shifts it back to 48%. Each update is logged with its rationale, creating a traceable audit trail.

### 3. Fox vs. Hedgehog Thinking

**Description:** Tetlock's earlier research in *Expert Political Judgment* (2005) found that hedgehog thinkers -- those who filter everything through one big explanatory framework -- performed worse than foxes, who draw on many models and tolerate ambiguity. Superforecasters are extreme foxes: they synthesize across disciplines, resist grand narratives, and are comfortable saying "it depends."

**Example:** A hedgehog analyst might interpret every geopolitical event through a "great power competition" lens. A fox analyst uses that lens alongside economic interdependence theory, domestic politics analysis, and historical analogy -- weighting each by its relevance to the specific question.

### 4. Granular Probability Estimates

**Description:** Vague language like "likely" or "possible" is the enemy of accountability and calibration. Superforecasters assign numerical probabilities (e.g., 72% rather than "probable") because granularity forces more careful thinking and enables post-hoc scoring. The discipline of choosing between 65% and 75% demands examining the actual evidence.

**Example:** Instead of stating "the market is likely to recover in Q3," a superforecaster writes "62% probability of recovery by end of Q3, with the key swing factor being central bank policy in the June-July window." This makes the forecast testable and the reasoning visible.

### 5. Brier Score Discipline

**Description:** The Brier score measures the accuracy of probabilistic predictions on a 0-to-2 scale (lower is better). Superforecasters internalize this metric: they know that extreme confidence (95%+) on wrong calls is catastrophically expensive to their score. This creates a healthy aversion to overconfidence and rewards well-calibrated uncertainty.

**Example:** An analyst who consistently assigns 90% confidence but is correct only 70% of the time has a worse Brier score than one who assigns 75% confidence and is correct 75% of the time. The scoring function punishes miscalibration more than it rewards boldness.

### 6. Fermi Decomposition of Complex Questions

**Description:** Rather than estimating a complex outcome directly, superforecasters break it into independently estimable components and combine them. This reduces cognitive load, exposes hidden assumptions, and identifies which sub-estimates drive the most uncertainty -- enabling targeted evidence collection.

**Example:** Instead of directly estimating "will Company X enter the European market by 2027?", decompose into: (a) probability the company seeks international expansion (80%), (b) probability Europe is chosen over Asia-Pacific given expansion (55%), (c) probability of regulatory approval within the timeline (70%). Combined: roughly 31%.

## Application to Deep Research Squad

These reasoning patterns are operationalized across the squad's pipeline:

- **Evidence Verifier** (`agents/evidence-verifier.md`): Applies base rate thinking when assessing whether a claimed finding is plausible. Uses Brier score logic to challenge inflated confidence levels -- a claim rated "High confidence" must survive the question: "If we made 10 claims at this confidence level, would we expect 8-9 to hold up?"

- **Contrarian Analyst** (`agents/contrarian-analyst.md`): Embodies fox thinking by actively seeking frameworks that contradict the emerging consensus. Prevents the squad from collapsing into hedgehog mode around a single narrative.

- **Decision Analyst** (`agents/decision-analyst.md`): Uses granular probability estimates in scenario analysis and recommendation trade-offs. Avoids vague language in deliverables; every probabilistic claim carries a numerical estimate and a stated basis.

- **Scope Mapper** (`agents/scope-mapper.md`): Applies Fermi decomposition to break research questions into MECE sub-questions, each of which can be independently estimated and investigated.

- **Reference Intellectual** (`agents/reference-intellectual.md`): Provides theoretical grounding using the full Tetlock framework at `frameworks/reference-intellectual/tetlock-superforecasting.md`, including calibration protocols and updating discipline.

- **Research Auditor** (`agents/research-auditor.md`): Performs postmortem-style checks on final deliverables, verifying that confidence scores are calibrated and that the evidence base supports the stated probability ranges.

## Common Failures

1. **Anchoring on the first estimate.** Early numbers exert disproportionate pull. Mitigation: always document the base rate separately from case-specific adjustments.
2. **Narrative seduction.** A coherent story feels more certain than it is. Mitigation: require the contrarian analyst to present at least one equally coherent alternative narrative.
3. **Scope insensitivity.** Treating 10x differences as marginal adjustments. Mitigation: force order-of-magnitude checks during Fermi decomposition.
4. **Motivated reasoning in updates.** Updating enthusiastically on confirming evidence and sluggishly on disconfirming evidence. Mitigation: log all updates symmetrically and flag asymmetric patterns during audit.
5. **Confidence as identity.** Analysts who treat their estimates as personal commitments rather than probability distributions. Mitigation: normalize frequent small updates and celebrate calibration accuracy over prediction boldness.
