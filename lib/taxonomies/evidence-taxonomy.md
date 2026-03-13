# Evidence Taxonomy

## Purpose

Classifies types of evidence encountered during research, enabling appropriate
strength assessment and aggregation based on evidence category.

## Categories

### 1. Empirical Evidence
Derived from direct observation or measurement.

**Subcategories:**
- **Experimental** - Results from controlled experiments with defined variables
- **Observational** - Data collected from real-world observation without control
- **Measurement** - Direct instrument readings, metrics, or quantitative data

**Examples:** A/B test results, production latency measurements, load test output

### 2. Statistical Evidence
Derived from statistical analysis of data sets.

**Subcategories:**
- **Descriptive** - Summary statistics, distributions, averages, percentiles
- **Inferential** - Hypothesis tests, confidence intervals, regression analysis
- **Predictive** - Model outputs, forecasts, trend projections

**Examples:** p99 latency distribution, correlation between load and response time

### 3. Testimonial Evidence
Based on the statements or opinions of individuals.

**Subcategories:**
- **Expert Opinion** - Judgment from a recognized domain authority
- **Practitioner Report** - First-hand experience from someone who used the technology
- **User Testimony** - End-user feedback, satisfaction reports, reviews

**Examples:** CTO blog post on migration experience, conference talk on production use

### 4. Documentary Evidence
Derived from written or recorded documents.

**Subcategories:**
- **Specification** - Formal specifications, standards, protocol definitions
- **Documentation** - Official product or project documentation
- **Case Study** - Documented real-world implementation with outcomes
- **Incident Report** - Post-incident analysis, postmortem documentation

**Examples:** RFC specifications, vendor case study, public postmortem blog post

### 5. Comparative Evidence
Derived from direct comparison between options.

**Subcategories:**
- **Benchmark** - Standardized performance comparison under controlled conditions
- **Feature Matrix** - Structured comparison of capabilities across options
- **Migration Story** - Account of switching from one option to another with outcomes

**Examples:** TPC-H benchmark results, feature comparison table, migration blog post

### 6. Negative Evidence
Evidence characterized by the absence of something.

**Subcategories:**
- **Absence of Reports** - No failure reports found despite wide adoption
- **Failed Search** - Deliberate search for counter-evidence yielded nothing
- **Null Result** - Experiment or test that showed no effect

**Examples:** No data corruption reports across 200+ production case studies

## Usage

Assign each evidence card a type from this taxonomy. Use the classification to:
- Apply appropriate strength scoring (empirical > testimonial > negative)
- Ensure evidence diversity (avoid relying solely on one evidence type)
- Weight evidence correctly during aggregation
- Identify what types of evidence are missing from the research
