# Academic Search Operators

## Google Scholar Operators
- `author:"J Smith"` - Search by author name
- `allintitle:keyword1 keyword2` - All keywords in paper title
- `"exact phrase"` - Exact phrase in full text
- `source:"Journal Name"` - Search within specific journal
- `-patent` - Exclude patents from results
- `-citation` - Exclude citations
- Use "Cited by" link to find papers citing a key work (forward citation)
- Use date range slider for temporal filtering

## PubMed Search Syntax
- `[MeSH Terms]` - Controlled vocabulary search (e.g., "artificial intelligence"[MeSH])
- `[tiab]` - Title and abstract field (e.g., "machine learning"[tiab])
- `[au]` - Author field (e.g., "Smith J"[au])
- `[dp]` - Date of publication (e.g., "2023"[dp])
- `[pt]` - Publication type (e.g., "Review"[pt], "Meta-Analysis"[pt])
- `AND / OR / NOT` - Boolean operators
- PubMed Clinical Queries: built-in filters for therapy, diagnosis, prognosis, etiology

## arXiv Search
- Category filters: cs.AI, cs.CL, cs.LG, stat.ML, q-fin, econ, etc.
- `ti:keyword` - Title search
- `au:author_name` - Author search
- `abs:keyword` - Abstract search
- `all:keyword` - All fields
- Combine with AND, OR, ANDNOT
- Use Semantic Scholar or Connected Papers for citation graph exploration of arXiv papers

## SSRN Search
- Filter by Research Network (FEN, LSN, ERN, etc.)
- Sort by downloads, date, or relevance
- Use "eJournal" subscriptions for topic-specific feeds

## Scopus Search
- `TITLE-ABS-KEY(keyword)` - Search title, abstract, keywords
- `AUTH(lastname)` - Author search
- `SRCTITLE("Journal Name")` - Source title
- `SUBJAREA(COMP)` - Subject area filter
- `PUBYEAR > 2020` - Date filter
- `DOCTYPE(re)` - Document type (ar=article, re=review, cp=conference)

## Web of Science
- `TS=(keyword)` - Topic search (title, abstract, keywords)
- `AU=(author)` - Author
- `SO=(journal)` - Source
- `OG=(organization)` - Organization
- Combine with AND, OR, NOT

## Cross-Database Search Strategies
1. **Start with Google Scholar** for broad discovery
2. **Use PubMed** for health/bio with MeSH terms for precision
3. **Check arXiv** for latest AI/ML/CS/physics preprints
4. **Search SSRN** for economics, finance, law working papers
5. **Use Semantic Scholar** for AI-powered related paper discovery
6. **Citation chaining**: Forward (who cited this?) + Backward (what did this cite?)
7. **Pearl growing**: Find one good paper, then explore its citation network
8. **Systematic search**: Document your search strategy for reproducibility

## Filters That Matter Most
- **Publication type**: Prioritize systematic reviews and meta-analyses
- **Date range**: Balance recency with foundational works
- **Citation count**: Higher cited = more vetted (but not always better)
- **Open access filter**: Ensures you can actually read the full text
