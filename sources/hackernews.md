# Hacker News Research Playbook

## Objectives
Hacker News is the premier intellectual signal for senior engineers, founders, and systems architects. Use HN to gauge deep technical sentiment, controversial architectural shifts, and grassroots developer tools.

## Endpoints & APIs
- Firebase API:
  - Top Stories: `https://hacker-news.firebaseio.com/v0/topstories.json`
  - Show HN Stories: `https://hacker-news.firebaseio.com/v0/showstories.json`
  - Ask HN Stories: `https://hacker-news.firebaseio.com/v0/askstories.json`
  - Item Details: `https://hacker-news.firebaseio.com/v0/item/{id}.json`
- Algolia HN Search API:
  - `https://hn.algolia.com/api/v1/search_by_date?tags=story&numericFilters=points>50`

## Signal Interpretation
- **Point Velocity:** A story reaching >150 points in <4 hours indicates a major event or breakthrough.
- **Comment-to-Point Ratio:**
  - High ratio (>1.0): Deep controversy, architectural disagreement, or security concern.
  - Low ratio (<0.3): Broad acclaim or cool demo.
- **"Show HN" Value:** Inspect Show HNs for newly released developer tools, local AI tools, and niche open-source utilities.
