# Financial Databases

## Regulatory and Public Filing Databases

### SEC EDGAR
- **URL**: sec.gov/edgar
- **Coverage**: All US public company filings since 1996
- **Key Filings**: 10-K (annual), 10-Q (quarterly), 8-K (events), S-1 (IPO), DEF 14A (proxy)
- **Full-Text Search**: efts.sec.gov/LATEST/search-index?q=
- **API**: EDGAR Full-Text Search API, Company Search API
- **XBRL**: Machine-readable financial data via inline XBRL
- **Strengths**: Authoritative, free, complete US public company data
- **Use**: Financial analysis, corporate governance, executive compensation, risk factors

### CVM (Brazil)
- **URL**: dados.cvm.gov.br
- **Coverage**: Brazilian public company filings, fund data
- **Use**: Brazilian capital markets research

## Market Data Platforms

### Bloomberg Terminal
- **Coverage**: Global financial markets, news, analytics
- **Strengths**: Real-time data, fixed income, derivatives, ESG, private company data
- **Limitations**: Expensive ($24K+/year), terminal-based access
- **Use**: Professional financial analysis, trading, portfolio management

### Refinitiv Eikon (LSEG)
- **Coverage**: Global financial markets, comparable to Bloomberg
- **Strengths**: Strong news (Reuters), screening tools, deal analytics
- **Use**: Financial research, deal analysis, market data

### Yahoo Finance
- **URL**: finance.yahoo.com
- **Coverage**: US and international stock quotes, financials, news
- **Strengths**: Free, API access (unofficial), historical price data
- **Limitations**: Data accuracy can lag, limited fundamentals depth
- **Use**: Quick financial data lookups, price history, basic screening

### FRED (Federal Reserve Economic Data)
- **URL**: fred.stlouisfed.org
- **Coverage**: 800K+ economic and financial time series
- **Strengths**: Free API, excellent for macro/financial indicators
- **Use**: Interest rates, yield curves, monetary aggregates, economic indicators

## Alternative Financial Data

### SEC Whistleblower and Enforcement
- **URL**: sec.gov/litigation
- **Use**: Fraud detection signals, regulatory risk assessment

### OpenCorporates
- **URL**: opencorporates.com
- **Coverage**: 200M+ companies worldwide from official registers
- **Use**: Corporate structure research, beneficial ownership, entity verification

### Company House (UK)
- **URL**: find-and-update.company-information.service.gov.uk
- **Use**: UK company filings, director information

## Financial Database Best Practices
1. SEC EDGAR is the gold standard for US public companies - always verify there
2. Use XBRL data for structured financial analysis at scale
3. Cross-reference financial data across at least two sources
4. For private companies, combine Crunchbase + PitchBook + state filings
5. Free alternatives (Yahoo Finance, FRED) are adequate for directional analysis
6. Always note the filing date vs. reporting period when citing financial data
7. Read risk factor sections in 10-Ks for qualitative competitive intelligence
