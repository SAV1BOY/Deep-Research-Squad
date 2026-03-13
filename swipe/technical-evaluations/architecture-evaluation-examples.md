# Architecture Evaluation — Swipe Examples

## Purpose

Architecture evaluations assess the technical design of systems, platforms,
or solutions. They go beyond feature comparison to evaluate scalability,
maintainability, security, and alignment with business requirements.

## Gold Standard Structure

### 1. Evaluation Context
- What system or architecture is being evaluated
- What business requirements drive the evaluation
- Evaluation criteria and their weights

### 2. Architecture Overview
- High-level system design description
- Key components and their interactions
- Data flow and storage patterns
- Integration points and dependencies

### 3. Quality Attribute Assessment

| Attribute | Requirement | Current State | Gap | Priority |
|-----------|-----------|--------------|-----|----------|
| Scalability | 10x current load | 3x tested | Large | Critical |
| Latency | <200ms p99 | 450ms p99 | Medium | High |
| Availability | 99.95% | 99.9% | Small | High |
| Security | SOC2 + HIPAA | SOC2 only | Medium | Critical |
| Maintainability | 2-week deploy cycle | 6-week cycle | Large | Medium |

### 4. Technical Debt Assessment
- Identified debt items with estimated remediation cost
- Risk of each debt item if left unaddressed
- Prioritized remediation roadmap

### 5. Scalability Analysis
- Current capacity and utilization
- Scaling strategy (horizontal vs vertical)
- Known bottlenecks and their thresholds
- Cost model at different scale points

### 6. Security Posture
- Authentication and authorization model
- Data encryption (at rest and in transit)
- Compliance certifications and gaps
- Vulnerability management process

## Example Architecture Evaluation

> **System**: Customer data platform (CDP) for mid-market SaaS
> **Evaluation trigger**: Platform hitting scaling limits at 50M events/day
>
> **Key finding**: Architecture is monolithic with shared database.
> Event ingestion, processing, and serving all compete for same resources.
> Recommended: Decompose into event streaming (Kafka), processing (Flink),
> and serving (dedicated read replicas) layers.
>
> **Estimated effort**: 4-6 months with 3-person team
> **Risk of inaction**: Service degradation within 2 quarters at current growth

## Evaluation Anti-Patterns

1. Evaluating architecture without understanding business requirements
2. Focusing on technology choices over design principles
3. Ignoring operational concerns (monitoring, debugging, deployment)
4. Treating security as a separate concern rather than integral
5. Not considering the team's ability to operate the architecture

## Deliverable Standards

- Include architecture diagrams (even text-based)
- Quantify all assessments where possible
- Benchmark against industry standards
- Provide specific remediation recommendations with effort estimates
- Separate "must fix" from "should improve" from "nice to have"
