import requests
from typing import List, Dict, Any

class LobstersFetcher:
    """Fetches hottest stories from Lobste.rs for deep technical signals."""

    URL = "https://lobste.rs/hottest.json"

    def fetch_stories(self, limit: int = 15) -> List[Dict[str, Any]]:
        stories = []
        try:
            resp = requests.get(self.URL, timeout=6)
            if resp.status_code == 200:
                data = resp.json()
                for item in data[:limit]:
                    stories.append({
                        "source": "Lobste.rs",
                        "title": item.get("title"),
                        "url": item.get("url"),
                        "comments_url": item.get("comments_url"),
                        "score": item.get("score", 0),
                        "comment_count": item.get("comment_count", 0),
                        "tags": item.get("tags", [])
                    })
        except Exception:
            pass
        return stories

if __name__ == "__main__":
    fetcher = LobstersFetcher()
    stories = fetcher.fetch_stories(5)
    print(f"Fetched {len(stories)} stories from Lobste.rs")
