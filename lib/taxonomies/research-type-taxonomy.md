# Research Type Taxonomy

## Purpose

Classifies research efforts by their type and goal, guiding methodology selection,
resource allocation, deliverable format, and quality criteria for each engagement.

## Categories

### 1. Exploratory Research
Broad investigation to map an unfamiliar space.

**Subcategories:**
- **Landscape Survey** - Map the full solution space, identify major players and options
- **Feasibility Study** - Determine whether a proposed approach is viable
- **Technology Scan** - Identify emerging technologies relevant to a need

**Examples:** "What message queue options exist for our use case?" "Is it feasible to
migrate from MongoDB to PostgreSQL?"

### 2. Evaluative Research
Systematic assessment of specific options against criteria.

**Subcategories:**
- **Comparative Evaluation** - Side-by-side comparison of 2+ options on defined criteria
- **Benchmark Study** - Performance-focused evaluation with quantitative metrics
- **Risk Assessment** - Evaluation focused on identifying and quantifying risks
- **Maturity Assessment** - Evaluation of readiness for production use

**Examples:** "Compare Kafka vs. Pulsar for event streaming." "Benchmark ClickHouse
query performance at 10TB scale."

### 3. Investigative Research
Deep dive into a specific question or problem.

**Subcategories:**
- **Root Cause Analysis** - Investigate why something is happening
- **Architecture Analysis** - Deep study of how a system works internally
- **Failure Mode Analysis** - Identify how and why a system can fail

**Examples:** "Why are our database queries slowing down after 6 months?"
"What are the failure modes of CockroachDB under network partition?"

### 4. Predictive Research
Forward-looking analysis to inform strategic decisions.

**Subcategories:**
- **Trend Analysis** - Identify and project technology or market trends
- **Scenario Planning** - Evaluate outcomes under different future scenarios
- **Capacity Planning** - Project future resource needs based on growth models

**Examples:** "How will our storage costs grow over the next 3 years?"
"What if our user base grows 10x in 12 months?"

### 5. Synthesis Research
Combining existing knowledge into new understanding.

**Subcategories:**
- **Literature Review** - Comprehensive survey and synthesis of existing work
- **Best Practice Compilation** - Gather and synthesize proven approaches
- **Decision Framework** - Build a reusable framework for recurring decisions

**Examples:** "What are the best practices for database migration?"
"Create a framework for evaluating new third-party dependencies."

### 6. Validation Research
Confirming or disproving specific hypotheses or assumptions.

**Subcategories:**
- **Hypothesis Testing** - Test a specific claim or assumption
- **Proof of Concept** - Validate technical feasibility through implementation
- **Assumption Audit** - Review and validate assumptions underlying a decision

**Examples:** "Validate that Redis can handle our session volume."
"Test whether our assumed 99.99% uptime SLA is achievable with this architecture."

## Usage

Classify each research engagement by type at the outset. Use this to:
- Select methodology (evaluative needs benchmarks; exploratory needs broad search)
- Set expectations for deliverable format and depth
- Allocate appropriate time and resources (investigative takes longer than validation)
- Choose quality rubric criteria weights (predictive weighs uncertainty higher)
- Communicate scope and intent to stakeholders clearly
