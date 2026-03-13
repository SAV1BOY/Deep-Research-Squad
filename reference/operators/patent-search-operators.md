# Patent Search Operators

## Google Patents Operators
- `"exact phrase"` - Exact phrase in patent text
- `inventor:"John Smith"` - Search by inventor name
- `assignee:"Company Name"` - Search by patent assignee/owner
- `country:US` - Filter by country (US, EP, WO, CN, JP, KR, etc.)
- `language:english` - Filter by language
- `before:filing:20240101` - Filed before date
- `after:filing:20200101` - Filed after date
- `before:publication:20240101` - Published before date
- `status:grant` - Only granted patents
- `status:application` - Only applications
- `type:patent` - Exclude design patents, utility models
- `classification:CPC_code` - CPC classification filter (e.g., G06F)

## CPC Classification Codes (Most Relevant)
- **G06**: Computing, calculating, counting
  - G06F: Electrical digital data processing
  - G06N: Computer systems based on biological models (AI/ML)
  - G06Q: Data processing for business/financial purposes
- **H04**: Electric communication technique
  - H04L: Digital information transmission
  - H04W: Wireless communication networks
- **A61**: Medical or veterinary science
- **B60**: Vehicles in general (autonomous vehicles)
- **G16**: Healthcare informatics (G16H)

## USPTO Search (PatFT/AppFT)
- `TTL/keyword` - Title field
- `ABST/keyword` - Abstract field
- `ACLM/keyword` - Claims field
- `SPEC/keyword` - Description/specification
- `IN/inventor-name` - Inventor
- `AN/assignee-name` - Assignee
- `ISD/YYYYMMDD` - Issue date
- `ICL/class` - International classification
- `CCL/class` - Current CPC classification
- Boolean: AND, OR, ANDNOT
- Truncation: `comput$` matches computing, computer, computational

## Espacenet Search
- Smart search: Natural language query
- Advanced search: Title, abstract, publication number, applicant, inventor
- Classification search: CPC/IPC tree browser
- **Patent family**: Same invention across countries (crucial for completeness)
- Use "Global Dossier" for prosecution history across offices

## WIPO PATENTSCOPE
- Field codes: FP (front page), EN_TI (English title), EN_AB (English abstract)
- CLIR: Cross-Lingual Information Retrieval (searches in multiple languages)
- PCT data: International phase applications
- Filter by: filing office, IPC, dates

## Patent Landscape Analysis Strategy
1. Start with keyword search in Google Patents for broad discovery
2. Identify relevant CPC codes from initial results
3. Refine search using CPC codes + keywords for precision
4. Analyze top assignees to map competitive landscape
5. Check patent families for international filing patterns
6. Review citation networks to identify foundational patents
7. Track filing trends over time for technology maturity signals
8. Note: patent = filed, not necessarily commercially viable or enforceable

## Common Research Queries
- `assignee:"[Company]" after:filing:20200101 classification:G06N` - Company AI patents since 2020
- `"large language model" OR "transformer architecture" status:grant` - Granted LLM patents
- `classification:G06Q10 assignee:"[Company]"` - Company business method patents
