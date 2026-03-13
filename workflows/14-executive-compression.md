# Workflow 14: Executive Compression

## Purpose
Compress the full research output into an executive format of 1-2 pages maximum. Distill the essential findings, recommendations, and confidence levels so that a time-constrained decision-maker can grasp the research value in under 5 minutes without losing critical nuance.

## Trigger
- Research passes audit from Workflow 13 (score >= 70 with fixes applied).
- Requester profile indicates executive or summary format is needed.
- Cross-squad handoff requires a compressed briefing.

## Agents Involved
- **Synthesis Writer**: Drafts the compressed executive brief.
- **Research Lead**: Validates that compression preserves accuracy and nuance.
- **Decision Translator**: Ensures decision-relevant elements survive compression.

## Inputs
- Full research output (all synthesis layers, models, decision brief).
- Audit report and quality score from Workflow 13.
- Requester profile and preferences from Workflow 00.
- Original research question.

## Steps

1. **Identify the essential message**: Distill the entire research into a single sentence:
   - What is the one thing the reader must know?
   - This becomes the opening line of the executive brief.
   - Test: if the reader reads only this sentence, do they get the core insight?

2. **Select the compression structure**: Choose the format based on research type:
   - **Decision research**: Recommendation first, then options, then evidence.
   - **Fact-finding research**: Key finding first, then supporting evidence, then caveats.
   - **Landscape mapping**: Overview first, then segments, then implications.
   - **Forecasting**: Most likely scenario first, then alternatives, then key uncertainties.

3. **Extract top findings**: Select the 3-5 most important findings from Layer 1 and Layer 2:
   - Prioritize findings that directly answer the research question.
   - Prioritize findings with the highest confidence.
   - Prioritize findings with the largest impact on the decision.
   - Each finding must be expressible in 1-2 sentences.

4. **Preserve critical nuance**: Identify the 2-3 nuances that MUST survive compression:
   - Key caveats that change the interpretation of findings.
   - Confidence levels that prevent over-reading the results.
   - Unresolved contradictions that the reader should be aware of.
   - Build these into the brief as explicit callouts, not footnotes.

5. **Compress the recommendation**: If the research includes recommendations:
   - State the recommendation in one sentence.
   - State the primary reason in one sentence.
   - State the biggest risk in one sentence.
   - State the confidence level in one phrase.
   - If the recommendation is conditional, state the condition clearly.

6. **Build visual summary**: Create one visual element that captures the key structure:
   - A simple table (options vs. criteria with color-coded scores).
   - A 2x2 matrix (if two key dimensions exist).
   - A timeline with 3-5 key events (if temporal narrative matters).
   - A ranked list with confidence indicators.
   - One visual only. It must be understandable without reading the text.

7. **Draft the executive brief**: Write the compressed document:
   - **Line 1**: Essential message (one sentence).
   - **Section 1 (1/4 page)**: Context and question being answered.
   - **Section 2 (1/2 page)**: Key findings with confidence levels.
   - **Section 3 (1/4 page)**: Recommendation with trade-offs and risks.
   - **Section 4 (callout box)**: Critical caveats and uncertainties.
   - **Visual**: Embedded in the most relevant section.
   - Total: 1-2 pages, no more.

8. **Apply the "so what" test**: Read every sentence and ask "so what?":
   - If a sentence does not directly serve the reader's decision or understanding, cut it.
   - If a sentence repeats something already stated, cut it.
   - If a sentence requires insider knowledge to understand, rewrite it.
   - Every sentence must earn its place in the brief.

9. **Validate accuracy after compression**: Research Lead reviews:
   - Does the brief accurately represent the full research?
   - Has compression introduced any distortions or overstatements?
   - Are confidence levels faithfully preserved?
   - Would reading only the brief lead to the same decision as reading the full output?
   - If any check fails, revise the brief.

10. **Link to full research**: Include clear pointers to the full output:
    - Reference to full decision brief for detailed analysis.
    - Reference to evidence registry for source verification.
    - Reference to models for structural understanding.
    - The brief must be self-contained but connected to depth.

## Quality Gates
- Executive brief must not exceed 2 pages.
- The essential message must be present in the opening line.
- Confidence levels must be stated for all findings and recommendations.
- At least 2 critical nuances must be preserved as explicit callouts.
- The "so what" test must be applied to every sentence.
- Research Lead must confirm compression accuracy before delivery.

## Outputs
- Executive brief (1-2 pages, structured and visual).
- Links to full research outputs for deeper reading.
- Compression notes (what was cut and why, for internal record).

## Next Workflow
- **16-cross-squad-handoff.md** (if delivering to another squad).
- **15-registry-and-memory-update.md** (update registries with research completion).
