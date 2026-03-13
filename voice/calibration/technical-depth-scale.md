# Technical Depth Scale

## Purpose

This guide defines how to calibrate the technical depth of deliverables
based on the reader's technical sophistication. The same finding requires
different framing for a business stakeholder versus an engineer.

## The Four Depth Levels

### Level 1: Business

**Profile:** Non-technical stakeholders focused on outcomes and impact.
**Objective:** Understand what it means, not how it works.

| Attribute         | Guideline                                  |
|-------------------|--------------------------------------------|
| Technical terms   | Avoid; use plain language equivalents       |
| Explanations      | Analogy-driven                              |
| Numbers           | Round figures, percentages, comparisons     |
| Mechanisms        | Describe effects, not processes             |
| Visuals           | Conceptual diagrams, outcome charts         |

**Example:**
- Instead of: "The LLM achieves 0.92 F1-score on the benchmark."
- Write: "The system correctly identifies the right answer 92% of the time."

---

### Level 2: Analyst

**Profile:** Quantitatively literate, domain-aware, but not a builder.
**Objective:** Understand the methodology and assess the evidence.

| Attribute         | Guideline                                  |
|-------------------|--------------------------------------------|
| Technical terms   | Use with brief definitions                  |
| Explanations      | Logic-driven with supporting data           |
| Numbers           | Precise figures with context                |
| Mechanisms        | Describe at the system level                |
| Visuals           | Data charts, comparison tables              |

**Example:**
- "The model achieves an F1-score of 0.92 on the MMLU benchmark,
  which measures broad knowledge across 57 subjects."

---

### Level 3: Engineer

**Profile:** Builds and operates systems. Needs implementation-level detail.
**Objective:** Understand how it works and how to use it.

| Attribute         | Guideline                                  |
|-------------------|--------------------------------------------|
| Technical terms   | Full domain vocabulary expected             |
| Explanations      | Architecture-level with trade-off analysis  |
| Numbers           | Exact metrics, configurations, thresholds   |
| Mechanisms        | Describe the system internals               |
| Visuals           | Architecture diagrams, flow charts, configs |

**Example:**
- "The model achieves F1=0.92 on MMLU using 4-shot prompting with
  chain-of-thought. Inference latency is 340ms at batch_size=1 on A100."

---

### Level 4: Scientist / Researcher

**Profile:** Designs experiments and advances the state of the art.
**Objective:** Understand the theoretical basis and evaluate rigor.

| Attribute         | Guideline                                   |
|-------------------|---------------------------------------------|
| Technical terms   | Specialist vocabulary with formal definitions|
| Explanations      | Theory-grounded with mathematical precision  |
| Numbers           | Full statistical reporting (CI, p-values)    |
| Mechanisms        | Formal models and proofs where applicable    |
| Visuals           | Ablation studies, statistical plots          |

**Example:**
- "F1=0.92 (95% CI: 0.90-0.94) on MMLU using 4-shot CoT prompting.
  Performance degrades to 0.84 under distribution shift (MMLU-Redux)."

## Calibration Rules

1. **Identify the reader's depth level before writing.**
2. **Never mix levels within a section.** Use layered documents if the audience is mixed.
3. **Each level should be self-contained.** A Level 1 reader should not need Level 3.
4. **Translate up, not down.** Start at the reader's level and simplify.
5. **When in doubt, write one level simpler than you think necessary.**

## Cross-Reference

- For audience seniority calibration, see `audience-depth-scale.md`.
- For tone selection, see `voice/tone-profiles/`.
