import requests
import xml.etree.ElementTree as ET
import logging
from typing import List, Dict, Any

logger = logging.getLogger(__name__)

class RedditFetcher:
    """Fetches high-signal posts from key developer subreddits via RSS."""

    SUBREDDITS = [
        "LocalLLaMA",
        "programming",
        "webdev",
        "Telegram",
        "SaaS",
        "devops"
    ]

    def __init__(self):
        self.headers = {
            "User-Agent": "DailyTechTrendIntelligence/1.0 (Scout Bot for Research)"
        }

    def fetch_top_posts(self) -> List[Dict[str, Any]]:
        results = []
        for sub in self.SUBREDDITS:
            try:
                url = f"https://www.reddit.com/r/{sub}/.rss"
                resp = requests.get(url, headers=self.headers, timeout=6)
                if resp.status_code == 200:
                    root = ET.fromstring(resp.content)
                    # Atom namespace
                    ns = {'atom': 'http://www.w3.org/2005/Atom'}
                    entries = root.findall('atom:entry', ns)
                    for entry in entries[:4]:
                        title = entry.find('atom:title', ns)
                        link = entry.find('atom:link', ns)
                        updated = entry.find('atom:updated', ns)
                        
                        title_text = title.text if title is not None else ""
                        link_href = link.attrib.get('href') if link is not None else ""
                        updated_text = updated.text if updated is not None else ""

                        results.append({
                            "source": f"Reddit (r/{sub})",
                            "title": title_text,
                            "url": link_href,
                            "subreddit": sub,
                            "updated_at": updated_text
                        })
            except Exception as e:
                continue

        return results

if __name__ == "__main__":
    fetcher = RedditFetcher()
    posts = fetcher.fetch_top_posts()
    print(f"Fetched {len(posts)} posts from Reddit RSS")
    for p in posts[:3]:
        print(f"- [{p['subreddit']}] {p['title']}")
