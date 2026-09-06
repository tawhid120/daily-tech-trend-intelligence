# Pass 1: Multi-Source Discovery Protocol

## Objective
Execute a broad, multi-signal scan across all primary intelligence sources to identify raw trend candidates across the 3 Core Areas (AI Automation, Telegram Bots, Website Development) and the broader engineering taxonomy.

## Operating Rules
1. **Never Skip Core Areas:** You MUST identify candidate signals for AI Automation, Telegram Bots, and Web Development. If activity is slow in one area, widen the window to 72h or state the factual lull clearly.
2. **Multi-Source Requirement:** Do not rely on a single source or single query. Use the `query_playbook.md` to query across:
   - Hacker News (Top & Show HN)
   - GitHub Trending & Recent High-Velocity Repositories
   - Reddit Tech Subreddits (RSS/Search)
   - Official Engineering Releases (OpenAI, Anthropic, Google DeepMind, Telegram API, Vercel, etc.)
   - Real-time dev chatter on X/Twitter and YouTube tutorial velocities.
3. **Capture Raw Metadata:** For every candidate discovered, record:
   - `candidate_title`: Distinct name of the technology, release, framework, or event.
   - `first_observed_source`: Where it was initially picked up.
   - `observed_timestamp`: Publication date/time (verify it is within 24h–72h).
   - `primary_url`: Direct URL to the announcement, repository, or thread.
   - `initial_category`: Map to Priority 1, 2, or 3 taxonomy.

## Discovery Checklist
- [ ] Hacker News API fetched (top 30 stories inspected)
- [ ] GitHub search executed for `topic:ai-agent`, `topic:telegram-bot`, `topic:mcp-server`, `topic:nextjs`
- [ ] Reddit top daily threads scanned across r/LocalLLaMA, r/programming, r/webdev, r/Telegram
- [ ] Official changelogs checked (Telegram Bot API, Anthropic, OpenAI, React/Next.js)
- [ ] Candidate pool assembled (aim for 25–40 raw candidates before validation)
