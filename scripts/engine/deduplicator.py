import re
from typing import List, Dict, Any

class TrendDeduplicator:
    """Clusters and deduplicates candidate news items into canonical technology entities."""

    CLEAN_WORDS = {
        "release", "released", "announcing", "announcement", "show", "hn:", 
        "launches", "introducing", "update", "v1", "v2", "v3", "github", 
        "open", "source", "tool", "framework", "new", "the", "a", "an", "for"
    }

    @classmethod
    def extract_keywords(cls, text: str) -> set:
        words = re.findall(r'[a-zA-Z0-9_\-\.]+', text.lower())
        return {w for w in words if len(w) > 2 and w not in cls.CLEAN_WORDS}

    @classmethod
    def are_similar(cls, title1: str, title2: str, threshold: float = 0.45) -> bool:
        kw1 = cls.extract_keywords(title1)
        kw2 = cls.extract_keywords(title2)
        if not kw1 or not kw2:
            return False
        intersection = kw1.intersection(kw2)
        union = kw1.union(kw2)
        jaccard = len(intersection) / len(union)
        return jaccard >= threshold

    @classmethod
    def cluster_candidates(cls, candidates: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        clusters = []
        for item in candidates:
            title = item.get("title", "")
            matched = False
            for cluster in clusters:
                if cls.are_similar(title, cluster["canonical_title"]):
                    cluster["occurrences"].append(item)
                    cluster["sources"].add(item.get("source", "Unknown"))
                    matched = True
                    break
            if not matched:
                clusters.append({
                    "canonical_title": title,
                    "primary_url": item.get("url", ""),
                    "category": item.get("category", "general"),
                    "occurrences": [item],
                    "sources": {item.get("source", "Unknown")}
                })

        # Format as cleaned candidates
        result = []
        for c in clusters:
            sources_list = sorted(list(c["sources"]))
            result.append({
                "title": c["canonical_title"],
                "url": c["primary_url"],
                "category": c["category"],
                "evidence_count": len(c["occurrences"]),
                "sources": sources_list,
                "occurrences": c["occurrences"]
            })
        return result
