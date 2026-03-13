# Technical Depth Calibration Guide

## Purpose and Scope

This guide defines a 5-level scale for calibrating the technical depth of research outputs. It governs how much domain-specific detail, jargon, quantitative data, and methodological explanation to include. Use this guide alongside the Formality Calibration Guide to produce outputs matched to the audience's expertise.

## Technical Depth Scale

### Level 1 -- Executive Overview

**When to use:** C-suite briefings, non-technical stakeholders, high-level decision support.

**Characteristics:**
- No jargon; all terms explained in plain language
- Focus on implications and recommendations, not methods
- Quantitative data limited to 2-3 headline numbers
- Analogies and comparisons preferred over raw data

**Example:**
> The new system processes research queries roughly three times faster than the previous version, which means the team can handle the current backlog within two weeks instead of six.

---

### Level 2 -- Informed Summary

**When to use:** Product managers, cross-functional teams, general business audience with some domain familiarity.

**Characteristics:**
- Common technical terms used without definition
- Key metrics presented with brief context
- Methods mentioned but not explained in detail
- Charts and tables used for clarity

**Example:**
> Query latency improved from a p50 of 45 minutes to 25 minutes after switching to targeted retrieval. Source diversity held steady at 0.75, indicating the speed gain did not come at the cost of coverage.

---

### Level 3 -- Practitioner Detail (Default)

**When to use:** Technical team members, engineers, analysts, domain practitioners.

**Characteristics:**
- Domain terminology used freely
- Methodology described with enough detail to evaluate validity
- Supporting data included (sample sizes, confidence intervals)
- Trade-offs and limitations discussed explicitly

**Example:**
> Targeted retrieval reduced p50 end-to-end latency from 45 to 25 minutes (n=95, p<0.01). Evidence yield rose from 0.42 to 0.61. However, source diversity in the policy domain dropped by 8%, likely due to over-filtering on recency. We recommend a hybrid approach for policy queries.

---

### Level 4 -- Deep Technical

**When to use:** Specialist engineers, researchers, architecture reviews, technical documentation.

**Characteristics:**
- Full methodological detail including parameters and configurations
- Raw data or detailed breakdowns provided
- Edge cases and failure modes documented
- References to specific algorithms, models, or system components

**Example:**
> The retrieval module applies a BM25 + dense embedding hybrid with alpha=0.6 weighting toward semantic similarity. Query-time filters include: recency (last 24 months), domain classification (top-2 predicted domains, threshold 0.7), and source-type whitelist. On the policy evaluation set, this configuration produced an evidence yield of 0.61 (SD=0.09) but exhibited a 0.08 decrease in source diversity (Shannon entropy) compared to unfiltered retrieval.

---

### Level 5 -- Research Grade

**When to use:** Academic publications, reproducibility documentation, formal methodology papers.

**Characteristics:**
- Complete reproducibility information (versions, seeds, hardware)
- Statistical methodology fully specified
- All assumptions stated explicitly
- Formal notation where appropriate
- Related work and comparison to prior approaches included

**Example:**
> We evaluate retrieval quality using evidence yield (EY), defined as |R_relevant| / |R_total|, where relevance is determined by majority vote among three independent annotators (Fleiss kappa = 0.74). The hybrid retrieval function f(q) = alpha * sim_dense(q, d) + (1 - alpha) * BM25(q, d), alpha = 0.6, was optimized via grid search over alpha in {0.2, 0.4, 0.6, 0.8} on a held-out validation set (n=40). All experiments conducted using Python 3.11, FAISS 1.7.4, index type IVF4096,PQ32.

---

## Selecting the Right Level

| Audience                  | Default Level | Adjustable Range |
|----------------------------|:---:|:---:|
| Executives / non-technical | 1   | 1-2 |
| Product / business teams   | 2   | 1-3 |
| Technical practitioners    | 3   | 2-4 |
| Specialist engineers       | 4   | 3-5 |
| Academic / research peers  | 5   | 4-5 |

## Interaction with Formality

Technical depth and formality are independent axes. A Level 4 technical depth output can be written at Formality Level 2 (conversational) for an internal engineering chat, or at Formality Level 5 (academic) for a journal submission. Always calibrate both dimensions.

When in doubt, default to Level 3 (Practitioner Detail) and adjust based on the stated audience.
