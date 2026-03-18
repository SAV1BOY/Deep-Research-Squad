# Quality Gate Cascade — Operational Reference

## Purpose

This document defines the complete quality gate cascade for the Deep Research Squad. It shows how validation flows from individual agent output through five levels of review before an artifact can be delivered externally. Every transition in the pipeline is gated — no artifact advances without passing its gate.

---

## Gate Levels

### Level 1: Agent Self-Check

**Who:** Each individual agent validates their own output before submitting.

**How:** The agent applies their agent-specific checklists from `checklists/<agent>/`. Each checklist contains numbered pass/fail criteria with explicit thresholds.

**Gate behavior:**
- PASS → Submit artifact to the next layer
- FAIL → Agent revises internally and re-checks
- FAIL x2 → Agent escalates to Level 2 with a description of the unresolvable issue

**Checklists by agent:**

| Agent | Primary Checklists |
|---|---|
| scope-mapper | `checklists/scope/` (5 checklists) |
| query-strategist | `checklists/query/` (5 checklists) |
| source-hunter | `checklists/source/` (5 checklists) |
| data-researcher | `checklists/data/` (5 checklists) |
| evidence-verifier | `checklists/evidence/` (5 checklists) |
| literature-analyst | `checklists/literature/` (5 checklists) |
| osint-investigator | `checklists/osint/` (5 checklists) |
| timeline-analyst | `checklists/timeline/` (5 checklists) |
| contrarian-analyst | `checklists/contrarian/` (5 checklists) |
| synthesis-writer | `checklists/synthesis/` (5 checklists) |
| insight-modeler | `checklists/modeling/` (5 checklists) |
| decision-analyst | `checklists/decision/` (5 checklists) |
| discovery-scout | `checklists/discovery/` (4 checklists) |
| domain-specialist | `checklists/domain-stacks/` (11 domain checklists) |

---

### Level 2: Peer / Layer Gate

**Who:** Specialist validators check artifacts produced within their pipeline layer.

**How:**

| Pipeline Layer | Peer Validator | Gate Checklists |
|---|---|---|
| Decomposition | research-architect | `checklists/architect/` |
| Collection | evidence-verifier | `checklists/evidence/`, `checklists/verification/` |
| Verification | contrarian-analyst | `checklists/contrarian/`, `checklists/validation/` |
| Synthesis | research-auditor | `checklists/synthesis-stack/`, `checklists/audit/` |
| Decision | research-auditor | `checklists/decision/`, `checklists/audit/` |

**Gate behavior:**
- PASS → Artifact advances to next pipeline stage
- FAIL → Return to producing agent with specific remediation instructions
- FAIL x2 → Escalate to Level 3 (Chief) with failure history

---

### Level 3: Chief Gate (Final Squad Gate)

**Who:** The deepresearch-chief validates the assembled pipeline output.

**How:** The Chief applies `checklists/chief/` (5 checklists) plus the 8 mandatory gates from `config.yaml`.

**Mandatory gates (from config.yaml quality_gates.mandatory):**

| Gate | Enforced By | Threshold |
|---|---|---|
| source-verification | evidence-verifier | 100% of cited sources verified |
| confidence-calibration | research-auditor | All claims tagged with confidence scores |
| contrarian-review | contrarian-analyst | Minimum 1 contrarian pass per thesis |
| bias-audit | research-auditor | Bias score < 0.2 |
| question-coverage | deepresearch-chief | 100% coverage or explicit gap declaration |
| recency-check | timeline-analyst | Primary sources within domain window |
| cross-reference-minimum | evidence-verifier | Minimum 2 independent sources per claim |
| decision-readiness | decision-analyst | Recommendations + risk assessment + confidence present |

**Gate behavior:**
- PASS → Output is approved for delivery or cross-squad handoff
- FAIL → Chief identifies the weakest link and routes back to the responsible layer (Level 2) or agent (Level 1)
- FAIL x2 → Chief may re-scope the engagement or reassign agents per `config.yaml escalation_protocols`
- FAIL x3 → Task is returned to Scope Mapper for re-decomposition

**This gate is absolute: NO output leaves the squad without Chief sign-off.**

---

### Level 4: Cross-Squad Gate

**Who:** Exit gate at DeepResearch Squad + entry gate at receiving squad.

**Exit gate checks (before sending):**
- All sub-questions answered or marked as gaps
- Confidence scores assigned to every claim
- Evidence chain intact from source to conclusion
- Output conforms to project template
- Limitations and caveats explicitly stated
- Research Auditor signed off
- Handoff package complete (see `docs/cross-squad-handoff-contracts.md`)

**Entry gate checks (at receiving squad):**
- Handoff package structurally complete
- Confidence scores meet receiver's minimum thresholds
- Limitations acceptable for downstream application
- Source manifest demonstrates adequate diversity

**Gate behavior:**
- PASS both → Handoff completes
- FAIL exit → Return to Level 3 for remediation
- FAIL entry → Receiving squad returns rejection notice; Chief triages per `config.yaml escalation_protocols.cross_squad_failure`

---

### Level 5: HRM System Gate

**Who:** HRM Chief (system-level authority across all 12 squads).

**When triggered:**
- Cross-squad handoff rejected twice on the same artifact
- Squad KPIs consistently breach thresholds (per `config.yaml kpis`)
- Quarterly research quality review flags systemic issues
- Multiple squads report quality issues with DeepResearch outputs

**Gate behavior:**
- Loop output back to any level (1-4) with remediation directives
- Reassign work across squads
- Trigger full re-scope of the engagement
- Commission methodology review

---

## Per-Domain Gates

In addition to the universal gates above, domain-specific research triggers additional gates from `checklists/domain-stacks/`:

| Domain | Gate Checklists | Key Checks |
|---|---|---|
| Financial | `domain-stacks/financial-research.md` | SEC verification, currency normalization, forward-looking labels |
| Legal | `domain-stacks/legal-research.md` | Jurisdiction, case law verification, regulatory status |
| Medical/Health | `domain-stacks/health-research.md` | Peer-review trace, sample size, regulatory approval |
| Technology | `domain-stacks/technical-research.md` | Official docs verification, version numbers, license compliance |
| Geopolitical | `domain-stacks/geopolitical-research.md` | Multiple perspectives, source affiliations, timeline verification |
| AI/ML | `domain-stacks/ai-research.md` | Benchmark validity, reproducibility, model limitation disclosure |
| Crypto/Web3 | `domain-stacks/crypto-research.md` | On-chain verification, tokenomics validation |
| Business/Strategy | `domain-stacks/business-strategy-research.md` | Market data currency, competitive landscape completeness |
| Marketing | `domain-stacks/marketing-research.md` | Audience data validity, channel metrics accuracy |
| Policy | `domain-stacks/policy-research.md` | Multi-stakeholder perspectives, regulatory timeline accuracy |
| Cross-Domain | `domain-stacks/cross-domain-research.md` | Inter-domain consistency, translation accuracy |

---

## Gate Metrics

Gate performance is tracked through the following metrics (stored in `data/metrics/`):

| Metric | Target | Measurement |
|---|---|---|
| First-pass rate (Level 1) | >= 85% | Agent outputs passing self-check on first attempt |
| First-pass rate (Level 2) | >= 80% | Artifacts passing peer review on first attempt |
| First-pass rate (Level 3) | >= 80% | Outputs passing Chief gate on first attempt |
| Average rework cycles | <= 1.5 | Mean number of revision cycles per artifact |
| Gate failure root causes | Tracked | Top 3 failure reasons per gate per quarter |
| Time-in-gate | Tracked per stage | Time spent in quality review vs. production |

---

## Anti-Patterns

| Anti-Pattern | Description | Correction |
|---|---|---|
| Rubber-stamp gate | Approving without checking criteria | Every gate must reference specific checklist items |
| Perfectionism gate | Rejecting work that meets the bar but could be "better" | Gates enforce minimum standards, not maximum quality |
| Skipped gate | Advancing artifacts without gate review due to urgency | Gates are never optional; urgent work uses expedited but complete reviews |
| Vague rejection | Rejecting without specific, actionable feedback | Every rejection must list specific failing criteria and remediation steps |
| Gate inflation | Adding criteria beyond the defined checklist | Gate criteria are defined in checklists; changes require Chief approval |
| Blame-shifting | Using gates to avoid responsibility for upstream quality | Each level owns its output quality; gates are verification, not production |
