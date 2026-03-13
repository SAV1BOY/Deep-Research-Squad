# AI System Evaluation — Swipe Examples

## Purpose

AI system evaluations assess AI/ML solutions for fitness, reliability,
and responsible deployment. They combine technical benchmarking with
business alignment and risk assessment.

## Gold Standard Structure

### 1. Evaluation Summary
- System being evaluated and its intended use case
- Key metrics and results
- Overall recommendation with confidence level

### 2. Model Performance Assessment

| Metric | Benchmark | System Score | Acceptable? | Notes |
|--------|----------|-------------|------------|-------|
| Accuracy | >92% | 94.3% | Yes | Test set n=10K |
| Latency (p50) | <100ms | 85ms | Yes | Production load |
| Latency (p99) | <500ms | 720ms | No | Spikes under load |
| Fairness (demographic parity) | <5% gap | 3.2% gap | Yes | Across 4 groups |
| Hallucination rate | <2% | 4.7% | No | Critical for use case |

### 3. Data Quality Assessment
- Training data composition and representativeness
- Data freshness and update cadence
- Known biases in training data
- Data governance and lineage

### 4. Reliability and Robustness
- Performance under edge cases
- Adversarial robustness testing results
- Graceful degradation behavior
- Monitoring and alerting coverage

### 5. Responsible AI Assessment
- Bias and fairness analysis across protected categories
- Explainability: can decisions be explained to affected users?
- Privacy: data minimization, consent, retention
- Human oversight: escalation paths, override mechanisms

### 6. Integration and Operations
- API design and documentation quality
- Deployment complexity and requirements
- Monitoring and observability
- Model update and retraining process

## Example AI Evaluation Finding

> **System**: LLM-powered customer support automation
> **Finding**: The system performs well on common queries (92% resolution rate)
> but fails silently on edge cases. When it doesn't know the answer, it
> generates plausible but incorrect responses 4.7% of the time. For a
> customer-facing system, this is above acceptable threshold.
>
> **Recommendation**: Deploy with mandatory confidence thresholds.
> Route queries below 85% confidence to human agents. This reduces
> automation rate from 72% to 58% but eliminates most hallucination risk.

## AI Evaluation Red Flags

1. No evaluation on data representative of production distribution
2. Accuracy reported only on aggregate, not per-segment
3. No adversarial or edge-case testing
4. Explainability treated as optional
5. No plan for model drift monitoring
6. Training data provenance unclear

## Evaluation Standards for Research Squad

- All AI evaluations must include fairness assessment
- Hallucination rates must be measured and reported
- Confidence calibration must be tested (is 90% confidence actually 90%?)
- Human-in-the-loop requirements must be specified
- Total cost of ownership must include retraining and monitoring
