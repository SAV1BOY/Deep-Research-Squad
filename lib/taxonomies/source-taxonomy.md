# Source Taxonomy

## Purpose

Classifies information sources into a structured hierarchy for consistent type
identification, trust calibration, and coverage analysis.

## Categories

### 1. Primary Sources
Direct, first-hand information from the origin.
- **Official Documentation** - Vendor docs, API references, specifications
- **Primary Research** - Original studies, experiments, peer-reviewed papers
- **Raw Data** - Datasets, researcher-run benchmarks, logs, metrics
- **Official Announcements** - Release notes, changelogs, press releases

**Example:** PostgreSQL official docs, Jepsen test report, AWS pricing page

### 2. Secondary Sources
Analysis or commentary on primary sources.
- **Expert Analysis** - In-depth articles by domain experts
- **Review Articles** - Comparative reviews, technology evaluations
- **Conference Talks** - Presentations at industry conferences
- **Books** - Published technical books

**Example:** Martin Kleppmann's distributed systems blog, InfoQ reviews

### 3. Tertiary Sources
Aggregated or community-generated information.
- **Community Forums** - Stack Overflow, Reddit, Hacker News
- **Wiki Sources** - Wikipedia, project wikis, community knowledge bases
- **Social Media** - Twitter/X threads, LinkedIn posts

**Example:** Stack Overflow answers, Reddit r/database threads

### 4. Vendor / Commercial Sources
Information from entities with commercial interest.
- **Vendor Whitepapers** - Technical papers by vendors
- **Marketing Material** - Product pages, sales collateral
- **Sponsored Content** - Paid posts, sponsored benchmarks
- **Analyst Reports** - Gartner, Forrester reports

**Example:** MongoDB scaling whitepaper, Datadog-sponsored comparison

### 5. Internal Sources
Information from within the researching organization.
- **Internal Documentation** - Architecture docs, ADRs, runbooks
- **Internal Data** - Production metrics, incident reports
- **Institutional Knowledge** - Team expertise, historical decisions

**Example:** Company database metrics, past migration postmortems

## Usage

Assign each source card a type to ensure diversity (aim for 3+ categories),
calibrate trust scores, identify coverage gaps, and flag over-reliance on
vendor or tertiary sources.
