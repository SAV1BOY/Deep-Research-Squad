# Visual Synthesis Task

## Purpose
Create visual representations of research findings that make complex relationships, trends, and comparisons immediately comprehensible, enhancing the impact and accessibility of the research deliverable.

## When to Use
- When findings involve complex relationships, hierarchies, or networks
- When temporal trends or comparative data benefit from graphical presentation
- When the audience responds better to visual formats than dense text
- When synthesizing large volumes of information into digestible overviews

## Agents Involved
- **Lead**: Synthesis Writer
- **Supporting**: Data Researcher, Domain Specialist
- **Consulted**: DeepResearch Chief

## Inputs
- Validated research findings and synthesis report
- Quantitative data tables, trend data, and comparison matrices
- Taxonomy, causal map, or relationship structures from synthesis
- Audience preferences and presentation context
- Brand or formatting guidelines (if applicable)

## Steps
1. Inventory the findings and identify which are best communicated visually
2. Select the appropriate visualization type for each finding (timeline, matrix, flowchart, map, chart, network diagram)
3. Extract and organize the underlying data for each planned visual
4. Design the visual layout emphasizing clarity and the key insight
5. Annotate each visual with context, labels, and a one-line takeaway
6. Ensure visual encodings (color, size, position) are accurate and not misleading
7. Create a narrative sequence that connects visuals into a coherent story
8. Test each visual for standalone comprehensibility without surrounding text
9. Generate alt-text descriptions for accessibility
10. Integrate visuals into the synthesis report and delivery materials

## Quality Gates
- Visualization types match the nature of the data (no pie charts for trends, etc.)
- Visual encodings accurately represent the underlying data without distortion
- Each visual has a clear title, labels, legend, and source attribution
- Visuals are accessible (alt-text, colorblind-friendly palettes)
- The visual narrative supports, not contradicts, the written findings
- Complexity is reduced without sacrificing accuracy

## Outputs
- Set of annotated research visualizations
- Visual narrative sequence with linking commentary
- Data tables underlying each visualization
- Alt-text descriptions for all visual elements
- Integration guide for embedding visuals in reports and presentations

## Estimated Effort
- **3-5 simple visuals**: 1-2 hours
- **5-10 visuals with moderate complexity**: 2-4 hours
- **10+ visuals or interactive/complex formats**: 4-8 hours

## Dependencies
- Requires completed `build-synthesis-report.md` or sufficient validated findings
- Benefits from completed `build-taxonomy.md` and `build-causal-map.md`
- Outputs feed into `prepare-final-delivery.md` and `presentation-prep-task.md`
