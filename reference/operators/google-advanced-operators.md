# Google Advanced Search Operators

## Core Operators

### Site and URL Operators
- `site:domain.com` - Search within a specific domain
- `site:domain.com/path` - Search within a specific path
- `-site:domain.com` - Exclude a domain from results
- `inurl:keyword` - Keyword must appear in URL
- `allinurl:keyword1 keyword2` - All keywords must appear in URL

### Title and Text Operators
- `intitle:keyword` - Keyword must appear in page title
- `allintitle:keyword1 keyword2` - All keywords must appear in title
- `intext:keyword` - Keyword must appear in body text
- `allintext:keyword1 keyword2` - All keywords in body text

### File Type and Format
- `filetype:pdf` - Search for specific file types
- `filetype:xlsx` - Find spreadsheet files
- `filetype:pptx` - Find presentation files
- `filetype:csv` - Find data files
- Common types: pdf, doc, docx, xls, xlsx, ppt, pptx, csv, txt

### Exact Match and Exclusion
- `"exact phrase"` - Exact phrase match (most important operator)
- `-keyword` - Exclude keyword from results
- `keyword1 OR keyword2` - Either keyword (must be capitalized OR)
- `keyword1 | keyword2` - Alternative OR syntax
- `(keyword1 OR keyword2) keyword3` - Grouping with parentheses

### Range and Wildcard
- `*` - Wildcard for unknown words in exact phrases ("CEO of * announced")
- `2020..2024` - Number range (works for years, prices, quantities)
- `$100..$500` - Price range search

## Research-Specific Combinations

### Finding Reports and Studies
- `"market size" filetype:pdf site:mckinsey.com`
- `intitle:"state of" "2024" filetype:pdf`
- `"industry report" OR "market report" filetype:pdf [industry]`

### Finding Data and Statistics
- `"according to" site:statista.com [topic]`
- `filetype:csv OR filetype:xlsx [topic] data`
- `site:data.worldbank.org [indicator]`

### Finding Expert Opinions
- `site:hbr.org [topic]` - Harvard Business Review
- `site:ssrn.com [topic]` - Working papers
- `site:arxiv.org [topic]` - Preprints

### Competitive Intelligence
- `site:linkedin.com/in "current company" [company name]`
- `"[company name]" "revenue" OR "funding" OR "valuation"`
- `"[company name]" filetype:pdf "investor" OR "annual report"`

### News and Recency
- Use Google News (news.google.com) for time-filtered news search
- `after:2024-01-01` - Results after date (works in Google Search Tools)
- `before:2024-12-31` - Results before date

## Operator Combination Tips
1. Combine 2-3 operators maximum for best results
2. Use exact phrases liberally to reduce noise
3. Start broad, then narrow with operators
4. Negative operators (-) are powerful for filtering irrelevant results
5. Site: operator + filetype: is the most useful research combination
