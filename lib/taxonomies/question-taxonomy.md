# Question Taxonomy

## Purpose

Classifies research questions by type to guide the appropriate research methodology,
evidence requirements, and expected deliverable format for each question.

## Categories

### 1. Factual Questions
Seek objective, verifiable information.

**Subcategories:**
- **Definitional** - "What is X?" - seeks definition or explanation
- **Descriptive** - "How does X work?" - seeks mechanism or process description
- **Quantitative** - "How much/many?" - seeks specific numbers or measurements
- **Existence** - "Does X exist/support Y?" - seeks confirmation of capability

**Examples:** "What consistency model does CockroachDB use?" "How many nodes can Kafka
support in a single cluster?"

### 2. Comparative Questions
Seek to evaluate relative merits of options.

**Subcategories:**
- **Binary Comparison** - "Is X better than Y for Z?" - two options compared
- **Multi-Option** - "Which of X, Y, Z is best for W?" - multiple options ranked
- **Trade-off** - "What are the trade-offs between X and Y?" - balanced analysis
- **Fit Assessment** - "Does X meet our requirements?" - option vs. criteria

**Examples:** "How does ClickHouse compare to Druid for real-time analytics?"

### 3. Causal Questions
Seek to understand cause-and-effect relationships.

**Subcategories:**
- **Root Cause** - "Why does X happen?" - seeks underlying causes
- **Impact** - "What happens if we do X?" - seeks consequences of actions
- **Dependency** - "Does X depend on Y?" - seeks causal relationships

**Examples:** "Why does query latency increase above 10TB?" "What happens if a node fails
during a write-heavy period?"

### 4. Predictive Questions
Seek to forecast future states or outcomes.

**Subcategories:**
- **Trend** - "Where is X heading?" - seeks trajectory or direction
- **Scenario** - "What if X happens?" - seeks outcomes of hypothetical situations
- **Feasibility** - "Can we achieve X by Y?" - seeks viability assessment

**Examples:** "Will PostgreSQL close the OLAP performance gap within 2 years?"

### 5. Evaluative Questions
Seek judgment or assessment against criteria.

**Subcategories:**
- **Quality** - "How good is X?" - seeks quality assessment
- **Risk** - "How risky is X?" - seeks risk evaluation
- **Readiness** - "Is X ready for production?" - seeks maturity assessment
- **Suitability** - "Is X appropriate for our context?" - seeks contextual fit

**Examples:** "Is CockroachDB mature enough for our payment processing system?"

### 6. Strategic Questions
Seek guidance on direction or approach.

**Subcategories:**
- **Approach** - "How should we do X?" - seeks methodology or strategy
- **Priority** - "What should we do first?" - seeks ordering or prioritization
- **Architecture** - "How should we structure X?" - seeks design guidance

**Examples:** "Should we adopt a polyglot persistence strategy?"

## Usage

Classify each question in the question tree by type. Use this to:
- Select appropriate research patterns (comparative questions need benchmarks)
- Set evidence requirements (factual needs verification, predictive needs trends)
- Define deliverable format (comparative needs matrices, evaluative needs rubrics)
- Estimate research effort (strategic questions typically require more time)
