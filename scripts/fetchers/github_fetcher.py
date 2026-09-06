import requests
import datetime
from typing import List, Dict, Any

class GitHubFetcher:
    """Fetches trending and rapidly growing repositories across our Core Areas."""

    SEARCH_API = "https://api.github.com/search/repositories"

    QUERIES = [
        {"category": "ai_automation", "q": "topic:ai-agent created:>2026-08-01 stars:>20"},
        {"category": "ai_automation", "q": "topic:mcp-server stars:>10"},
        {"category": "telegram_bots", "q": "topic:telegram-bot created:>2026-08-01 stars:>10"},
        {"category": "telegram_bots", "q": "topic:telegram-mini-app stars:>5"},
        {"category": "web_development", "q": "topic:webgpu language:typescript stars:>20"},
        {"category": "web_development", "q": "topic:nextjs created:>2026-08-01 stars:>30"}
    ]

    def __init__(self):
        self.headers = {
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "DailyTechTrendIntelligence/1.0"
        }

    def fetch_trending_repos(self) -> List[Dict[str, Any]]:
        results = []
        seen_repos = set()

        for item in self.QUERIES:
            category = item["category"]
            query = item["q"]
            try:
                params = {
                    "q": query,
                    "sort": "stars",
                    "order": "desc",
                    "per_page": 6
                }
                resp = requests.get(self.SEARCH_API, headers=self.headers, params=params, timeout=10)
                if resp.status_code == 200:
                    data = resp.json()
                    for repo in data.get("items", []):
                        repo_full = repo.get("full_name")
                        if repo_full not in seen_repos:
                            seen_repos.add(repo_full)
                            results.append({
                                "source": "GitHub",
                                "title": f"{repo.get('name')}: {repo.get('description') or 'No description'}",
                                "repo_name": repo_full,
                                "url": repo.get("html_url"),
                                "stars": repo.get("stargazers_count", 0),
                                "forks": repo.get("forks_count", 0),
                                "language": repo.get("language"),
                                "category": category,
                                "created_at": repo.get("created_at"),
                                "updated_at": repo.get("updated_at"),
                                "open_issues": repo.get("open_issues_count", 0)
                            })
            except Exception as e:
                continue

        return results

if __name__ == "__main__":
    fetcher = GitHubFetcher()
    repos = fetcher.fetch_trending_repos()
    print(f"Fetched {len(repos)} repos from GitHub")
    for r in repos[:3]:
        print(f"- [{r['stars']} stars] {r['repo_name']} ({r['category']}): {r['url']}")
