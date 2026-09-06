# Search Query Playbook & Discovery Matrix

This guide provides targeted search query syntax and Boolean combinations to execute multi-source trend discovery across Google, Reddit, Hacker News, GitHub, and X/Twitter.

---

## 1. Google & Tech News Query Templates

### Date-Bounded Search Operators
- `&tbs=qdr:d` (Past 24 hours)
- `&tbs=qdr:w` (Past week)
- `&tbs=qdr:m` (Past month)

### Priority 1 Queries (AI Automation, Telegram, Web Dev)
- `"AI agent" OR "agentic workflow" ("release" OR "announced" OR "open source") after:2026-08-15`
- `"Model Context Protocol" OR "MCP server" ("new" OR "release" OR "GitHub")`
- `"Telegram Bot API" (update OR changelog OR "new features" OR "Stars")`
- `"Telegram Mini App" OR "TMA" ("tutorial" OR "launch" OR "SDK" OR "template")`
- `"Next.js" OR "React 19" ("release" OR "benchmark" OR "server actions")`
- `site:news.ycombinator.com "Show HN" ("agent" OR "Telegram" OR "frontend" OR "automation")`
- `site:reddit.com/r/LocalLLaMA ("released" OR "new model" OR "framework")`
- `site:reddit.com/r/webdev ("anyone tried" OR "new library" OR "alternative")`

---

## 2. GitHub Search Query Syntax

### High-Velocity Emerging Repositories
- `topic:ai-agent created:>2026-08-01 stars:>50 sort:stars-desc`
- `topic:mcp-server created:>2026-08-01 sort:stars-desc`
- `topic:telegram-bot "stars" created:>2026-08-01 sort:updated-desc`
- `topic:telegram-mini-app sort:stars-desc`
- `topic:webgpu language:typescript created:>2026-07-01`
- `language:python "autonomous agent" stars:>100 created:>2026-08-01`

---

## 3. Hacker News Search & Filter Syntax

- Algolia HN Search API: `https://hn.algolia.com/api/v1/search_by_date?tags=(story,show_hn)&numericFilters=points>30`
- Keywords: `agent`, `Telegram`, `workflow`, `automation`, `framework`, `security`, `Postgres`, `Rust`, `Next.js`

---

## 4. Reddit Specific Feeds

- RSS URLs:
  - `https://www.reddit.com/r/LocalLLaMA/top/.rss?t=day`
  - `https://www.reddit.com/r/programming/top/.rss?t=day`
  - `https://www.reddit.com/r/webdev/top/.rss?t=day`
  - `https://www.reddit.com/r/Telegram/top/.rss?t=week`
  - `https://www.reddit.com/r/SaaS/top/.rss?t=day`

---

## 5. Query Escalation Pattern: Broad -> Specific -> Community -> Official -> Validation

1. **Broad Discovery:** Scan HN top stories, GitHub trending, and Reddit RSS.
2. **Specific Focus:** Deep dive into candidate tools using precise queries (`"<tool_name>" benchmark`, `"<tool_name>" site:github.com`).
3. **Community Pulse:** Check sentiment on Reddit and X (`"<tool_name>" site:reddit.com`, `"<tool_name>" complaint OR issue`).
4. **Official Verification:** Locate repository, documentation, or company blog.
5. **Validation & Deduplication:** Confirm release timestamp, discard PR duplicates, calculate final score.
