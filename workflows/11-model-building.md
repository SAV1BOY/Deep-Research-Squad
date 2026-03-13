# Workflow 11: Model Building

## Purpose
Build structured models that transform synthesized findings into actionable frameworks. Construct causal maps to show how factors connect, taxonomies to classify elements, scenario trees to map possible futures, and decision matrices to compare options. These models make complex research navigable and decision-ready.

## Trigger
- Layer 1 (certainties) and Layer 2 (probabilities) synthesis are complete.
- A specific model type is requested to support a decision.

## Agents Involved
- **Research Lead**: Selects model types and validates outputs.
- **Model Builder**: Constructs the structural models.
- **Data Analyst**: Provides quantitative inputs for models.
- **Synthesis Writer**: Ensures models align with synthesized findings.

## Inputs
- Layer 1 Synthesis Document from Workflow 09.
- Layer 2 Synthesis Document from Workflow 10.
- Contradiction map from Workflow 06.
- Master timeline from Workflow 07.
- Benchmark data from Workflow 08.
- Research question and question tree from Workflows 00-02.

## Steps

1. **Select model types**: Based on the research question type and requester needs, select which models to build:
   - **Causal map**: When the research involves understanding why things happen. Shows cause-effect relationships with strength indicators.
   - **Taxonomy**: When the research involves classifying or categorizing entities. Shows hierarchical groupings with defining attributes.
   - **Scenario tree**: When the research involves forecasting or planning. Shows branching futures with probability weights.
   - **Decision matrix**: When the research involves choosing between options. Shows options scored against weighted criteria.
   - Select 1-3 models based on relevance. Document the selection rationale.

2. **Build causal map (if selected)**:
   - List all causal claims from synthesis (both certain and probable).
   - Draw directed arrows from cause to effect.
   - Label each arrow with: strength (strong/moderate/weak), confidence (certain/probable), and evidence grade.
   - Identify feedback loops (A causes B causes A).
   - Identify root causes (nodes with no incoming arrows).
   - Identify terminal outcomes (nodes with no outgoing arrows).
   - Validate against the timeline: every causal arrow must respect temporal ordering.

3. **Build taxonomy (if selected)**:
   - Identify the entities or concepts to be classified.
   - Define the classification dimensions (attributes that distinguish categories).
   - Build the hierarchical structure (top-level categories, subcategories).
   - Apply MECE principles: every entity fits in exactly one category, all entities are covered.
   - Annotate each category with: size/prevalence, key characteristics, and relevant findings from synthesis.

4. **Build scenario tree (if selected)**:
   - Identify the key uncertainties that drive different futures.
   - Define branching points (decision nodes or chance nodes).
   - For each branch, assign a probability (from Layer 2) or mark as decision-dependent.
   - Trace each path through the tree to its terminal scenario.
   - Describe each terminal scenario: what happens, who is affected, what are the implications.
   - Assign an overall probability to each terminal scenario (product of branch probabilities).
   - Identify the highest-probability scenario and the highest-impact scenario.

5. **Build decision matrix (if selected)**:
   - List all options or alternatives identified in the research.
   - Define evaluation criteria (derived from the research question and requester needs).
   - Assign weights to criteria (based on requester priorities or evidence of importance).
   - Score each option on each criterion using evidence from synthesis.
   - Calculate weighted scores and rank options.
   - Perform sensitivity analysis: how much would weights need to change to alter the ranking?

6. **Cross-validate models**: If multiple models are built, check for consistency:
   - Do causal map root causes align with scenario tree branching points?
   - Do taxonomy categories map to decision matrix options?
   - Do scenario probabilities align with Layer 2 probability estimates?
   - Resolve any inconsistencies.

7. **Stress-test models**: For each model, apply three stress tests:
   - **Omission test**: What happens if we remove the weakest evidence? Does the model hold?
   - **Inversion test**: What if a key assumption is wrong? How does the model change?
   - **Extreme test**: What happens at the tails of uncertainty? Are there catastrophic scenarios?

8. **Annotate confidence levels**: For every element in every model:
   - Mark whether it is based on Layer 1 (certain) or Layer 2 (probable) evidence.
   - Flag elements based on Grade C or lower evidence.
   - Ensure no model element is treated as more certain than its underlying evidence.

9. **Create model documentation**: For each model, produce:
   - Visual representation (diagram, table, or tree).
   - Narrative explanation of what the model shows.
   - Methodology note (how it was constructed and what assumptions were made).
   - Limitations statement (what the model does NOT capture).

10. **Research Lead review**: Review all models for:
    - Logical consistency with synthesized findings.
    - Appropriate confidence attribution.
    - Practical utility for the requester.
    - Approve or request revision.

## Quality Gates
- Every model element must trace to evidence in Layer 1 or Layer 2.
- Causal maps must respect temporal ordering from the timeline.
- Scenario tree probabilities must sum correctly at each branching point.
- Decision matrix weights must be justified and sensitivity-tested.
- All models must pass at least the omission stress test.
- Confidence annotations must be present on all model elements.

## Outputs
- Completed models (causal maps, taxonomies, scenario trees, decision matrices as applicable).
- Model documentation with visuals, narratives, methodology, and limitations.
- Stress test results.
- Cross-validation report (if multiple models built).

## Next Workflow
- **12-decision-translation.md** (translate models into decision-ready format).
- **13-audit-before-delivery.md** (audit models as part of final quality check).
