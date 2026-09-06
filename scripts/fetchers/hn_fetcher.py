import requests
import json
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Dict, Any

logger = logging.getLogger(__name__)

class HackerNewsFetcher:
    """Fetches high-signal developer stories from Hacker News Firebase API concurrently."""
    
    BASE_URL = "https://hacker-news.firebaseio.com/v0"

    def __init__(self, limit: int = 30):
        self.limit = limit
        self.session = requests.Session()

    def _fetch_item(self, item_id: int) -> Dict[str, Any]:
        try:
            resp = self.session.get(f"{self.BASE_URL}/item/{item_id}.json", timeout=5)
            if resp.status_code == 200:
                data = resp.json()
                if data and data.get("type") == "story" and "title" in data:
                    return {
                        "source": "HackerNews",
                        "title": data.get("title"),
                        "url": data.get("url", f"https://news.ycombinator.com/item?id={item_id}"),
                        "hn_discussion_url": f"https://news.ycombinator.com/item?id={item_id}",
                        "points": data.get("score", 0),
                        "comments_count": data.get("descendants", 0),
                        "timestamp": data.get("time", 0),
                        "author": data.get("by", "anonymous")
                    }
        except Exception:
            pass
        return None

    def fetch_top_and_show(self) -> List[Dict[str, Any]]:
        stories = []
        try:
            top_resp = self.session.get(f"{self.BASE_URL}/topstories.json", timeout=5)
            show_resp = self.session.get(f"{self.BASE_URL}/showstories.json", timeout=5)
            
            top_ids = top_resp.json()[:self.limit] if top_resp.status_code == 200 else []
            show_ids = show_resp.json()[:15] if show_resp.status_code == 200 else []
            
            target_ids = list(dict.fromkeys(top_ids + show_ids))

            with ThreadPoolExecutor(max_workers=10) as executor:
                futures = [executor.submit(self._fetch_item, item_id) for item_id in target_ids]
                for future in as_completed(futures):
                    res = future.result()
                    if res:
                        stories.append(res)
        except Exception as e:
            logger.error(f"Error fetching HN data: {e}")

        # Sort by points descending
        stories.sort(key=lambda x: x.get("points", 0), reverse=True)
        return stories

if __name__ == "__main__":
    fetcher = HackerNewsFetcher(limit=15)
    results = fetcher.fetch_top_and_show()
    print(f"Fetched {len(results)} stories concurrently from Hacker News")
