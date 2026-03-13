# Cloud Migration Evaluation — Swipe Example

## Why This Is Gold Standard

Cloud migration evaluations must balance technical feasibility with business case rigor.
The best examples avoid vendor marketing claims by grounding every comparison in
workload-specific data. They assess not just "which cloud" but "which migration
pattern for which workload" and surface the hidden costs that derail migration budgets.

## Structure Template

### 1. Evaluation Context
- **Current state**: On-premises data center (2 locations), 340 VMs, 180TB storage
- **Migration driver**: Lease expiry in 14 months; modernization mandate from board
- **Budget envelope**: $2.8M migration + first-year run cost
- **Decision deadline**: 6 weeks
- **Evaluation confidence**: 0.76

### 2. Workload Classification

| Category | Count | % of Total | Migration Pattern | Complexity |
|----------|-------|-----------|-------------------|------------|
| Web applications (stateless) | 45 | 13% | Rehost (lift-and-shift) | Low |
| API services | 62 | 18% | Rehost or replatform | Low-Medium |
| Relational databases | 28 | 8% | Replatform | Medium |
| Legacy monoliths (.NET Framework) | 12 | 4% | Replatform or refactor | High |
| Data pipelines (Hadoop/Spark) | 8 | 2% | Refactor to managed services | High |
| Stateful services | 35 | 10% | Rehost with storage mapping | Medium |
| Batch processing | 48 | 14% | Replatform to serverless | Medium |
| Development/test environments | 82 | 24% | Rehost | Low |
| Compliance-restricted workloads | 20 | 6% | Rehost to dedicated/gov cloud | High |

### 3. Provider Comparison (Workload-Matched)

| Criterion | AWS | Azure | GCP | Weight |
|-----------|-----|-------|-----|--------|
| Compute cost (modeled, annual) | $1.42M | $1.38M | $1.31M | 25% |
| .NET workload support | Good | Excellent | Adequate | 15% |
| Data pipeline managed services | Excellent | Good | Excellent | 15% |
| Compliance certifications (FedRAMP, SOC2) | Excellent | Excellent | Good | 15% |
| Migration tooling maturity | Excellent | Good | Good | 10% |
| Team skill alignment | Medium (3 certified) | High (8 certified) | Low (1 certified) | 10% |
| Enterprise support SLA | 99.99% | 99.99% | 99.95% | 5% |
| Egress cost (modeled) | $84K/yr | $72K/yr | $68K/yr | 5% |
| **Weighted score** | **0.78** | **0.82** | **0.71** | |

### 4. Total Cost of Ownership (3-Year)

| Cost Category | On-Prem (status quo) | AWS | Azure | GCP |
|---------------|---------------------|-----|-------|-----|
| Infrastructure | $4.2M | $4.1M | $3.9M | $3.7M |
| Migration (one-time) | — | $1.1M | $0.9M | $1.2M |
| Training/upskilling | — | $180K | $80K | $240K |
| Licensing changes | — | $320K | -$150K (AHUB) | $320K |
| Staffing impact | $2.4M | $2.1M | $2.0M | $2.1M |
| Egress/data transfer | — | $252K | $216K | $204K |
| Hidden costs (estimated) | $600K | $400K | $350K | $450K |
| **3-Year Total** | **$7.2M** | **$8.4M** | **$7.3M** | **$8.2M** |

**Note on hidden costs:** Includes re-architecture for cloud-native patterns,
performance tuning, security tooling gaps, and vendor lock-in mitigation.

### 5. Risk Assessment

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| Migration timeline exceeds 14-month lease deadline | 0.45 | High | Phase 1 critical workloads first; negotiate 3-month lease extension |
| Cost overrun >20% | 0.35 | Medium | Monthly cost reviews; reserved instance commitment delayed 90 days |
| Performance degradation post-migration | 0.30 | High | Benchmark critical workloads pre-migration; acceptance criteria per workload |
| Compliance gap during migration | 0.20 | Critical | Migrate compliance workloads last; maintain parallel environment |
| Skill gap delays | 0.40 | Medium | Engage migration partner for Phase 1; upskill team during Phase 2 |
| Vendor lock-in | 0.60 | Medium | Use Terraform, container-based deployments, avoid proprietary services where practical |

### 6. Migration Phasing

| Phase | Months | Workloads | Count | Risk | Dependencies |
|-------|--------|-----------|-------|------|-------------|
| Phase 0: Foundation | 1-2 | Landing zone, networking, IAM, security | — | Low | None |
| Phase 1: Low-risk | 3-5 | Dev/test, stateless web apps | 127 | Low | Phase 0 |
| Phase 2: Core services | 6-9 | APIs, databases, stateful services | 125 | Medium | Phase 1 validation |
| Phase 3: Complex | 10-13 | Legacy monoliths, data pipelines, batch | 68 | High | Phase 2 stable |
| Phase 4: Compliance | 12-14 | Compliance-restricted workloads | 20 | High | Compliance validation |

### 7. Recommendation

**Primary recommendation**: Azure — highest weighted score driven by .NET alignment,
team skills, and licensing advantage (Azure Hybrid Use Benefit saves ~$150K/yr).

**Conditions:**
1. Negotiate 3-month lease extension as buffer ($120K cost, high-value insurance)
2. Engage migration partner for Phase 1 ($200K, accelerates timeline by 6 weeks)
3. Establish cost governance from day one — weekly spend reviews in Phase 1
4. Accept that 12 legacy monoliths will require refactoring in Year 2 (post-migration)
5. Defer proprietary service adoption until workload patterns are understood (90 days)

**Alternative if Azure terms unfavorable**: AWS, with additional $180K training investment.

## Quality Checklist
- [ ] Workloads classified by migration pattern and complexity
- [ ] Provider comparison uses workload-specific data, not generic benchmarks
- [ ] TCO includes hidden costs and licensing impact
- [ ] Risk assessment includes probability and mitigation for each risk
- [ ] Migration phased with dependencies and timeline
- [ ] Recommendation includes conditions and alternative
- [ ] Team skill alignment factored into decision
- [ ] Vendor lock-in risk explicitly addressed
