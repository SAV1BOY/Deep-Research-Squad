# AI Research Methodology Papers

## Key Papers on AI/ML Methods and Their Evaluation

### Foundational AI Methodology

#### Bender & Koller (2020) - Climbing towards NLU
- **Citation**: Bender, E.M. & Koller, A. (2020). *ACL 2020*
- Language models trained on form alone cannot learn meaning
- Grounds expectations about LLM-based research capabilities
- **Implication**: AI research tools have inherent limitations in understanding

#### Lipton & Steinhardt (2019) - Troubling Trends in ML Scholarship
- **Citation**: Lipton, Z.C. & Steinhardt, J. (2019). *Queue*, 17(1), 45-77
- ML papers fail to distinguish explanation from speculation
- Mathiness: using math to obscure rather than clarify
- **Implication**: Critically evaluate AI/ML claims in research outputs

#### Sculley et al. (2015) - Hidden Technical Debt in ML Systems
- **Citation**: Sculley, D. et al. (2015). *NeurIPS 2015*
- ML systems accumulate complex technical debt beyond code
- Configuration, data dependencies, and feedback loops create fragility
- **Implication**: Real-world AI implementation is harder than benchmarks suggest

### AI Evaluation and Documentation

#### Mitchell et al. (2019) - Model Cards for Model Reporting
- **Citation**: Mitchell, M. et al. (2019). *FAT* 2019*
- Standardized framework for documenting ML model performance
- Includes intended use, limitations, evaluation data, ethical considerations
- **Implication**: Evaluate AI tool claims systematically using model cards

#### Gebru et al. (2021) - Datasheets for Datasets
- **Citation**: Gebru, T. et al. (2021). *Communications of the ACM*, 64(12), 86-92
- Standardized documentation for datasets
- Covers motivation, composition, collection, preprocessing, distribution
- **Implication**: Assess data quality underlying AI research claims

#### Pineau et al. (2020) - ML Reproducibility Checklist
- Checklist for NeurIPS submissions to improve reproducibility
- Code availability, hyperparameter reporting, statistical tests
- **Implication**: Use checklist criteria when evaluating ML research claims

### AI Reasoning and Alignment

#### Wei et al. (2022) - Chain-of-Thought Prompting
- **Citation**: Wei, J. et al. (2022). *NeurIPS 2022*
- Step-by-step reasoning improves LLM performance on complex tasks
- Emergent capability in large-scale models
- **Implication**: Structure AI-assisted research workflows with explicit reasoning steps

#### Bai et al. (2022) - Constitutional AI
- **Citation**: Bai, Y. et al. (2022). *arXiv:2212.08073*
- Methods for aligning AI systems with human values
- AI-generated feedback for training helpful and harmless assistants
- **Implication**: Understand capabilities and limitations of AI research assistants

#### Yao et al. (2023) - Tree of Thoughts
- Deliberate problem solving with language models via tree search
- Enables exploration of multiple reasoning paths
- **Implication**: Multi-path reasoning improves AI research quality

### AI-Specific Research Challenges
- **Data contamination**: Benchmark data may be in training data; use novel benchmarks
- **Evaluation limits**: Benchmarks may not reflect real-world performance (Goodhart's law)
- **Hallucination**: AI generates plausible but false information; always verify against primary sources

## AI Methodology Assessment Checklist
- What training data was used? (biases, recency)
- Were benchmarks appropriate? Is there contamination risk?
- Are confidence intervals or error bars reported?
- Has the result been independently reproduced?
- What are the known failure modes and limitations?

## Application to Deep Research
- Always verify AI-generated claims against primary sources
- Use chain-of-thought reasoning for complex analysis tasks
- Document AI tool limitations alongside findings
- Apply model card criteria when evaluating AI-generated research
- Be aware of hallucination risks in any AI-assisted research
- Combine AI capabilities with human judgment for quality assurance
