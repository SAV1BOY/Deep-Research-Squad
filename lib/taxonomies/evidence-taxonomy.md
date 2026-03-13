# Evidence Taxonomy

## Purpose

Classifies evidence types to enable appropriate strength assessment and weighted
aggregation based on evidence category.

## Categories

### 1. Empirical Evidence
Derived from direct observation or measurement.
- **Experimental** - Controlled experiments with defined variables
- **Observational** - Real-world observation without controls
- **Measurement** - Direct instrument readings or quantitative data

**Example:** A/B test results, production latency measurements, load test output

### 2. Statistical Evidence
Derived from statistical analysis of data sets.
- **Descriptive** - Summaries, distributions, averages, percentiles
- **Inferential** - Hypothesis tests, confidence intervals, regression
- **Predictive** - Model outputs, forecasts, trend projections

**Example:** p99 latency distribution, correlation between load and response time

### 3. Testimonial Evidence
Based on statements or opinions of individuals.
- **Expert Opinion** - Judgment from a recognized domain authority
- **Practitioner Report** - First-hand experience from a technology user
- **User Testimony** - End-user feedback, reviews

**Example:** CTO blog on migration experience, conference talk on production use

### 4. Documentary Evidence
Derived from written or recorded documents.
- **Specification** - Formal specs, standards, protocol definitions
- **Documentation** - Official product documentation
- **Case Study** - Documented implementation with outcomes
- **Incident Report** - Post-incident analysis, postmortems

**Example:** RFC specifications, vendor case study, public postmortem

### 5. Comparative Evidence
Derived from direct comparison between options.
- **Benchmark** - Standardized performance comparison
- **Feature Matrix** - Structured capability comparison
- **Migration Story** - Account of switching with outcomes

**Example:** TPC-H benchmark results, feature comparison table

### 6. Negative Evidence
Characterized by the absence of something.
- **Absence of Reports** - No failures found despite wide adoption
- **Failed Search** - Deliberate counter-evidence search yielded nothing
- **Null Result** - Test showed no effect

**Example:** No data corruption reports across 200+ production deployments

## Usage

Assign each evidence card a type to apply appropriate strength scoring, ensure
diversity, weight correctly during aggregation, and identify missing evidence types.
