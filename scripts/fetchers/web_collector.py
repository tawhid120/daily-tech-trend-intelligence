import json
import logging
from typing import List, Dict, Any
from .hn_fetcher import HackerNewsFetcher
from .github_fetcher import GitHubFetcher
from .reddit_fetcher import RedditFetcher
from .lobsters_fetcher import LobstersFetcher

logger = logging.getLogger(__name__)

class MultiSourceCollector:
    """Aggregates multi-source signals across Hacker News, GitHub, Reddit, and Lobste.rs."""

    def __init__(self):
        self.hn = HackerNewsFetcher(limit=25)
        self.gh = GitHubFetcher()
        self.reddit = RedditFetcher()
        self.lobsters = LobstersFetcher()

    def collect_all_raw_signals(self) -> Dict[str, Any]:
        """Runs all collectors and tags items with initial taxonomy keywords."""
        signals = {
            "hacker_news": [],
            "github_trending": [],
            "reddit_discussions": [],
            "lobsters": []
        }

        try:
            signals["hacker_news"] = self.hn.fetch_top_and_show()
        except Exception as e:
            logger.warning(f"Failed to fetch Hacker News: {e}")

        try:
            signals["github_trending"] = self.gh.fetch_trending_repos()
        except Exception as e:
            logger.warning(f"Failed to fetch GitHub: {e}")

        try:
            signals["reddit_discussions"] = self.reddit.fetch_top_posts()
        except Exception as e:
            logger.warning(f"Failed to fetch Reddit: {e}")

        try:
            signals["lobsters"] = self.lobsters.fetch_stories(limit=15)
        except Exception as e:
            logger.warning(f"Failed to fetch Lobste.rs: {e}")

        total_items = sum(len(v) for v in signals.values())
        logger.info(f"Collected total of {total_items} raw multi-source signals.")
        return signals

if __name__ == "__main__":
    collector = MultiSourceCollector()
    data = collector.collect_all_raw_signals()
    print("MultiSourceCollector Summary:")
    for src, items in data.items():
        print(f" - {src}: {len(items)} items")
