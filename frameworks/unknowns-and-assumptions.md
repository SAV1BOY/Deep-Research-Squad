# Unknowns and Assumptions Framework

## Purpose
Explicitly categorize every element of a research investigation into what is
known, what is unknown, and what is assumed. This prevents hidden assumptions
from silently shaping conclusions and ensures that knowledge gaps are visible,
acknowledged, and addressed where possible.

## When to Use
- At the start of any research project to map the knowledge landscape.
- When findings feel "complete" but may have unexamined blind spots.
- When assumptions are driving conclusions without being stated.
- Before delivering final research outputs to ensure transparency.
- When stakeholders need to understand the limits of what was found.

## Inputs
- All claims, findings, and conclusions from the research.
- Sources consulted and their coverage.
- Research questions and sub-questions.
- Domain knowledge and contextual information.

## Process

### Step 1: List All Claims and Premises
- Extract every factual claim from the research output.
- Include premises that underpin the analysis (even if unstated).
- Note conclusions, recommendations, and predictions.
- Include methodological choices and their justifications.

### Step 2: Classify Each Item

**Category 1: Known Knowns**
- Definition: Things we know and can verify with evidence.
- Criteria: Supported by evidence at Rung 4+ on the Evidence Ladder,
  corroborated by independent sources, methodology is sound.
- Action: These form the foundation of the research. Document evidence chains.
- Example: "The company's Q3 revenue was $12M" (verified from SEC filings).

**Category 2: Known Unknowns**
- Definition: Things we know we do not know. Questions we can articulate
  but cannot currently answer.
- Criteria: We can state the question precisely but lack the evidence,
  access, or methodology to answer it now.
- Action: Document each unknown. Assess impact on conclusions. Identify
  what would be needed to convert to a Known Known.
- Example: "We do not know the competitor's internal cost structure."

**Category 3: Unknown Unknowns**
- Definition: Things we do not know that we do not know. Blind spots we
  have not yet identified.
- Criteria: By definition, these cannot be listed directly. They are surfaced
  through structured probing techniques.
- Action: Use probing questions to surface potential unknown unknowns.
  Apply adversarial thinking: what could invalidate our conclusions?
- Probing techniques:
  - "What perspectives have we not considered?"
  - "What domain expertise is missing from our analysis?"
  - "What would someone who disagrees with our conclusion point to?"
  - "What events or changes could make our findings obsolete?"
  - "What data did we not think to look for?"

**Category 4: Assumptions**
- Definition: Things we treat as true without direct verification.
- Sub-types:
  - **Explicit assumptions**: Stated and acknowledged in the analysis.
  - **Implicit assumptions**: Unstated beliefs embedded in the methodology or reasoning.
  - **Domain assumptions**: Standard beliefs in the field taken for granted.
- Criteria: Any premise that is used in reasoning but not independently verified.
- Action: Surface all assumptions. Classify each by risk level. Validate
  high-risk assumptions or convert them to Known Unknowns.

### Step 3: Flag Assumptions Requiring Validation
For each assumption, assess:
- **Impact**: If this assumption is wrong, how much does it affect conclusions?
  Rate: Low (minor detail changes), Medium (some conclusions affected),
  High (core findings invalidated), Critical (entire analysis undermined).
- **Likelihood of being wrong**: Based on available evidence and domain knowledge.
  Rate: Unlikely, Possible, Likely, Unknown.
- **Validation difficulty**: How hard would it be to verify this assumption?
  Rate: Easy (quick check), Moderate (requires research), Hard (requires
  primary data collection), Impractical (cannot be verified with available resources).

Priority matrix:
- **Validate immediately**: High/Critical impact + Possible/Likely wrong + Easy/Moderate to verify.
- **Flag prominently**: High/Critical impact + any likelihood + Hard/Impractical to verify.
- **Validate if time permits**: Medium impact + Easy to verify.
- **Accept and document**: Low impact regardless of other factors.

### Step 4: Identify Gaps
- Compare Known Unknowns against the research questions: are there questions
  we set out to answer that remain unanswered?
- Review the Unknown Unknowns probing results: did we surface new areas
  that need investigation?
- Check assumption validation results: did any validated assumptions
  turn out to be false, requiring revision?
- Document each gap with its impact on the overall research.

### Step 5: Produce the Knowledge Map
- Create a structured summary of all four categories.
- Highlight critical assumptions and high-impact unknowns.
- Provide recommendations for addressing key gaps.
- State clearly what the research can and cannot conclude.

## Outputs
- Categorized inventory: Known Knowns, Known Unknowns, Unknown Unknowns
  (surfaced), and Assumptions.
- Assumption risk register with impact, likelihood, and validation priority.
- Gap analysis showing unanswered questions and missing perspectives.
- Knowledge map summary for stakeholder communication.
- Recommendations for further research to address critical gaps.

## Common Pitfalls
- **Assumption blindness**: The most dangerous assumptions are the ones so
  deeply embedded they are invisible. Actively challenge "obvious" premises.
- **Completeness illusion**: A thorough-looking analysis can still have massive
  blind spots. Unknown unknowns exist in every investigation.
- **Ignoring low-probability risks**: Unlikely-but-high-impact assumptions
  deserve attention. Do not dismiss them solely on probability.
- **Analysis paralysis**: Not every assumption needs formal validation.
  Use the priority matrix to focus effort where it matters most.
- **False precision about unknowns**: Estimating what you do not know is
  inherently imprecise. Use ranges and qualitative assessments, not false numbers.

## Related Frameworks
- **Question Decomposition**: Surfaces assumptions during question analysis.
- **First-Principles Research**: Strips away assumptions to find bedrock facts.
- **Evidence Ladder**: Validates whether Known Knowns actually have sufficient evidence.
- **Confidence Weighting**: Adjusts scores based on assumption risk.

## Templates

### Knowledge Map Template
```
RESEARCH TOPIC: [Topic]

KNOWN KNOWNS:
1. [Claim] - Evidence: [Source, Rung]
2. [Claim] - Evidence: [Source, Rung]

KNOWN UNKNOWNS:
1. [Question we cannot answer] - Impact: [L/M/H/C] - Needed: [what would answer it]
2. [Question we cannot answer] - Impact: [L/M/H/C] - Needed: [what would answer it]

SURFACED UNKNOWN UNKNOWNS:
1. [Blind spot identified through probing] - Action: [investigate / accept]

ASSUMPTIONS:
| # | Assumption | Type | Impact | Likely Wrong? | Validate? |
|---|-----------|------|--------|--------------|-----------|
| 1 | [Statement]| [Explicit/Implicit/Domain] | [L/M/H/C] | [U/P/L/?] | [Priority] |

CRITICAL GAPS:
- [Gap 1]: [Impact on conclusions and recommended action]
```
