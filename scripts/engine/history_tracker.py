import os
import json
import datetime
from typing import Dict, Any, List, Tuple

class TrendHistoryTracker:
    """Manages persistent trend lifecycle, calculating momentum (ΔS) and acceleration (ΔV)."""

    def __init__(self, base_dir: str = None):
        if not base_dir:
            base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../data"))
        self.base_dir = base_dir
        self.history_file = os.path.join(self.base_dir, "historical", "trend-history.json")
        self.trends_dir = os.path.join(self.base_dir, "trends")
        os.makedirs(os.path.join(self.base_dir, "historical"), exist_ok=True)
        os.makedirs(self.trends_dir, exist_ok=True)
        self.history = self._load_history()

    def _load_history(self) -> Dict[str, Any]:
        if os.path.exists(self.history_file):
            try:
                with open(self.history_file, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                return {}
        return {}

    def _save_history(self):
        with open(self.history_file, "w", encoding="utf-8") as f:
            json.dump(self.history, f, indent=2, ensure_ascii=False)

    def record_daily_snapshot(self, date_str: str, scored_trends: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Updates history and attaches delta scores to today's trends."""
        augmented_trends = []

        for trend in scored_trends:
            key = trend.get("slug") or trend.get("title", "").strip().lower()
            current_score = trend.get("score_breakdown", {}).get("total_score", 0)

            if key in self.history:
                record = self.history[key]
                prev_score = record.get("trend_score", current_score)
                delta_s = current_score - prev_score
                prev_delta = record.get("score_change", 0)
                acceleration = delta_s - prev_delta

                # Update record
                record["last_seen"] = date_str
                record["previous_score"] = prev_score
                record["trend_score"] = current_score
                record["score_change"] = delta_s
                record["acceleration"] = acceleration
                record["trajectory"].append({"date": date_str, "score": current_score})
            else:
                delta_s = 0
                acceleration = 0
                self.history[key] = {
                    "slug": key,
                    "title": trend.get("title"),
                    "category": trend.get("category"),
                    "first_seen": date_str,
                    "last_seen": date_str,
                    "trend_score": current_score,
                    "previous_score": current_score,
                    "score_change": 0,
                    "acceleration": 0,
                    "trajectory": [{"date": date_str, "score": current_score}]
                }

            trend_copy = dict(trend)
            trend_copy["delta_s"] = delta_s
            trend_copy["acceleration"] = acceleration
            trend_copy["first_seen"] = self.history[key]["first_seen"]
            augmented_trends.append(trend_copy)

        self._save_history()

        # Save daily snapshot
        snapshot_file = os.path.join(self.trends_dir, f"{date_str}.json")
        with open(snapshot_file, "w", encoding="utf-8") as f:
            json.dump(augmented_trends, f, indent=2, ensure_ascii=False)

        return augmented_trends

    def get_radar_watchlist(self) -> List[Dict[str, Any]]:
        """Returns rising items with sustained positive trajectory."""
        watchlist = []
        for key, item in self.history.items():
            if item.get("score_change", 0) > 5 or item.get("acceleration", 0) > 0:
                watchlist.append(item)
        return sorted(watchlist, key=lambda x: x.get("score_change", 0), reverse=True)
