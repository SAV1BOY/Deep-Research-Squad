# Source Taxonomy

## Purpose

Classifies information sources into a structured hierarchy, enabling consistent
source type identification, trust calibration, and coverage analysis across research.

## Categories

### 1. Primary Sources
Direct, first-hand information from the origin.

**Subcategories:**
- **Official Documentation** - Vendor or project docs, API references, specifications
- **Primary Research** - Original studies, experiments, peer-reviewed papers
- **Raw Data** - Datasets, benchmarks run by the researcher, logs, metrics
- **Official Announcements** - Release notes, changelogs, press releases

**Examples:** PostgreSQL official docs, a Jepsen consistency test report, AWS pricing page

### 2. Secondary Sources
Analysis, interpretation, or commentary on primary sources.

**Subcategories:**
- **Expert Analysis** - In-depth articles by recognized domain experts
- **Review Articles** - Comparative reviews, technology evaluations
- **Conference Talks** - Recorded presentations at industry conferences
- **Curated Guides** - Tutorials and guides from reputable authors or organizations
- **Books** - Published technical books on the subject

**Examples:** Martin Kleppmann's blog on distributed systems, InfoQ architecture reviews

### 3. Tertiary Sources
Aggregated, summarized, or community-generated information.

**Subcategories:**
- **Community Forums** - Stack Overflow, Reddit, Hacker News discussions
- **Wiki Sources** - Wikipedia, project wikis, community-maintained knowledge bases
- **Social Media** - Twitter/X threads, LinkedIn posts, Mastodon discussions
- **Aggregator Sites** - News aggregators, content curation platforms

**Examples:** Stack Overflow answers, Reddit r/database threads, Wikipedia articles

### 4. Vendor / Commercial Sources
Information produced by entities with commercial interest in the topic.

**Subcategories:**
- **Vendor Whitepapers** - Technical papers published by vendors
- **Marketing Material** - Product pages, sales collateral, case studies by vendors
- **Sponsored Content** - Paid blog posts, sponsored benchmarks, advertorials
- **Analyst Reports** - Gartner, Forrester, IDC reports (paid, may have vendor influence)

**Examples:** MongoDB whitepaper on scaling, Datadog-sponsored performance comparison

### 5. Internal Sources
Information from within the organization conducting the research.

**Subcategories:**
- **Internal Documentation** - Architecture docs, ADRs, runbooks
- **Internal Data** - Production metrics, incident reports, team surveys
- **Institutional Knowledge** - Team expertise, historical decisions, verbal accounts

**Examples:** Company's existing database performance metrics, past migration postmortems

## Usage

Assign each source card a source type from this taxonomy. Use the classification to:
- Ensure source diversity (aim for 3+ categories per research question)
- Calibrate trust scores (primary sources generally score higher)
- Identify coverage gaps (e.g., no primary sources consulted)
- Flag over-reliance on vendor or tertiary sources
