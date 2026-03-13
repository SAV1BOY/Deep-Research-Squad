# Hassan & Hijazi - Hacking Search Engines: Advanced Search Techniques

## Advanced Google Search Operators

### Basic Operators
- `"exact phrase"` - Exact match
- `term1 OR term2` - Either term
- `-term` - Exclude term
- `*` - Wildcard for any word
- `..` - Number range (e.g., `$100..$500`)

### Site-Specific Operators
- `site:example.com` - Restrict to domain
- `site:*.example.com` - Include subdomains
- `site:example.com -site:blog.example.com` - Exclude subdomain
- `site:.gov` - Restrict to TLD
- `site:.edu filetype:pdf` - Academic PDFs

### Content-Specific Operators
- `intitle:"search term"` - Term in page title
- `allintitle:term1 term2` - All terms in title
- `inurl:keyword` - Term in URL
- `intext:"specific phrase"` - Term in body text
- `filetype:pdf|doc|xls|ppt` - Specific file types

### Date-Based Operators
- `before:2024-01-01` - Content before date
- `after:2023-01-01` - Content after date
- Tools > Any time > Custom range (GUI)

## Advanced Search Patterns

### Finding Specific Document Types
```
"annual report" filetype:pdf site:company.com
"investor presentation" filetype:pptx
"financial statements" filetype:xlsx
"strategic plan" filetype:pdf site:.gov
```

### Competitive Intelligence Searches
```
site:linkedin.com/in "company name" "joined"
site:glassdoor.com "company name" reviews
"company name" "partnership" OR "acquisition" OR "merger"
"company name" hiring OR "job opening" OR "we're hiring"
```

### Finding Leaked or Exposed Data
```
"confidential" filetype:pdf site:company.com
"internal use only" filetype:doc
"not for distribution" filetype:pdf
inurl:admin OR inurl:dashboard site:company.com
```

### Market Research Searches
```
"market size" "CAGR" "industry" filetype:pdf
"TAM" OR "total addressable market" "industry name"
"industry report" "2024" OR "2025" filetype:pdf
"market share" "company name" "percent"
```

## Search Engine Alternatives

### Specialized Search Tools
- **Google Scholar**: Academic papers, citations, legal opinions
- **Google Patents**: Patent search with classification browsing
- **Google Books/Ngrams**: Historical text analysis
- **Archive.org**: Historical web pages
- **Shodan**: Internet-connected devices
- **Censys**: Internet infrastructure

### Search Aggregators
- **Carrot2**: Clusters search results by topic
- **Searx**: Meta-search engine aggregating multiple sources
- **Wolfram Alpha**: Computational answers

## Search Automation Tips
- Save complex queries for reuse
- Set up Google Alerts for ongoing monitoring
- Use RSS feeds for regular source checking
- Create custom search engines (Google CSE) for specific domains
- Combine operators for precision

## Boolean Logic for Complex Queries
- `(term1 OR term2) AND (term3 OR term4)` - Combine groups
- Use parentheses to group logical operations
- Build queries incrementally: test each component separately
- Document working queries for future use

## Application to Deep Research
- Master site-specific operators for targeted intelligence gathering
- Use file type operators to find specific document types
- Combine date ranges with topic searches for trend analysis
- Set up monitoring queries for ongoing competitive intelligence
- Always document your search queries for reproducibility
- Use multiple search engines; each has different coverage
