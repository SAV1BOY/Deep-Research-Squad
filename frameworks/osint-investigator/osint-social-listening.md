# OSINT Social Listening Framework

## Purpose

Collect and analyze intelligence from social media platforms, online communities, forums, review sites, and other public discussion spaces. Social listening goes beyond simple monitoring: it involves systematic detection of sentiment, trends, emerging narratives, key influencers, and community dynamics. The goal is actionable intelligence about public perception and discourse.

## When to Use

- When researching public sentiment about a company, product, technology, or topic.
- When tracking the emergence and spread of narratives or trends.
- When identifying key influencers, advocates, or critics in a space.
- When monitoring competitive positioning and market perception.
- When detecting early warning signals for reputational, market, or technology shifts.

## Inputs

- Target entities, topics, or keywords to monitor.
- Platforms and communities relevant to the domain.
- Baseline data on current sentiment and discourse (if available).
- Time frame for monitoring (point-in-time snapshot or ongoing tracking).
- Ethical guidelines and platform terms of service.

## Process

1. **Define monitoring targets.** Specify the entities, topics, keywords, and hashtags to track. Include known variations, misspellings, and related terms.
2. **Select platforms and sources.** Identify relevant platforms: Twitter/X, LinkedIn, Reddit, industry forums, review sites (G2, Trustpilot, Glassdoor), Hacker News, Stack Overflow, GitHub discussions, YouTube comments, podcast mentions.
3. **Establish baseline.** Capture current state: volume of discussion, prevailing sentiment, dominant narratives, key voices. This baseline enables detection of changes.
4. **Collect systematically.** Use platform search functions, RSS feeds, and alerts. Record posts, threads, reviews, and comments with metadata (date, author, platform, engagement metrics).
5. **Analyze sentiment.** Categorize collected items by sentiment: positive, negative, neutral, mixed. Note intensity and specificity of sentiment.
6. **Identify trends.** Track volume and sentiment over time. Look for spikes, shifts, and emerging topics. Correlate with external events.
7. **Map key voices.** Identify influential contributors: who drives conversation, who shapes opinion, who has credibility in the community.
8. **Detect narratives.** Identify recurring themes, talking points, and frames. Note how narratives emerge, spread, and evolve.
9. **Assess credibility.** Evaluate whether detected sentiment and narratives reflect organic opinion or coordinated campaigns, bots, or astroturfing.
10. **Synthesize and report.** Produce a social listening report with key findings, trends, risks, and opportunities.

## Outputs

- A sentiment summary with distribution (positive, negative, neutral) and trends over time.
- Key themes and narratives with representative examples.
- An influencer map showing key voices and their reach.
- Trend analysis showing emerging, growing, stable, and declining topics.
- Early warning signals for reputational or market risks.
- Platform-by-platform breakdown of discourse characteristics.

## Common Pitfalls

- **Volume bias.** Loud voices are not representative voices; a small group can dominate discussion.
- **Platform bias.** Different platforms attract different demographics and discussion styles.
- **Sentiment oversimplification.** Sarcasm, irony, and nuanced opinions resist simple positive/negative classification.
- **Bot and astroturfing blindness.** Failing to distinguish organic discussion from manufactured sentiment.
- **Recency bias.** Overweighting the most recent discussion at the expense of longer-term trends.
- **Privacy overreach.** Collecting personal data from social profiles beyond what is needed and permitted.
- **Context stripping.** Quoting posts out of context to support a narrative.
- **Echo chamber effects.** Monitoring only one community and mistaking its views for broad consensus.

## Related Frameworks

- `osint-open-source-intelligence.md` - Social listening is a collection method within the broader OSINT cycle.
- `osint-digital-footprint-mapping.md` - Social media profiles are part of the digital footprint.
- `osint-corporate-intelligence.md` - Social listening provides perception data to complement corporate filings data.
- `data-researcher-time-series.md` - Time series methods apply to tracking sentiment and volume trends.
