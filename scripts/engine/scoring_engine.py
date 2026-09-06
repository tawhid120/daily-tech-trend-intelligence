from typing import Dict, Any, List

class TrendScoringEngine:
    """Calculates the 100-point Trend Score and Dual Score (Hype vs Practical Value)."""

    @classmethod
    def evaluate(cls, candidate: Dict[str, Any]) -> Dict[str, Any]:
        # 1. Recency (15 max)
        # Assumed fresh if observed in today's scrape
        recency = candidate.get("recency_score", 14)

        # 2. Cross-platform mentions (15 max)
        sources_count = len(candidate.get("sources", []))
        if sources_count >= 4:
            cross_platform = 15
        elif sources_count == 3:
            cross_platform = 11
        elif sources_count == 2:
            cross_platform = 8
        else:
            cross_platform = 4

        # 3. Growth Velocity (15 max)
        velocity = candidate.get("velocity_score", 11)

        # 4. Developer Interest (10 max)
        dev_interest = candidate.get("dev_interest_score", 8)

        # 5. Search Momentum (10 max)
        search = candidate.get("search_score", 7)

        # 6. GitHub Momentum (10 max)
        stars = candidate.get("stars", 0)
        if stars > 1000:
            gh_score = 10
        elif stars > 300:
            gh_score = 8
        elif stars > 50:
            gh_score = 6
        elif "GitHub" in candidate.get("sources", []):
            gh_score = 5
        else:
            gh_score = 2

        # 7. Social Engagement (5 max)
        social = candidate.get("social_score", 4)

        # 8. Official Confirmation (5 max)
        official = candidate.get("official_score", 4 if candidate.get("is_official") else 2)

        # 9. Real-World Adoption (5 max)
        adoption = candidate.get("adoption_score", 4)

        # 10. Business Impact (5 max)
        business = candidate.get("business_score", 4)

        raw_sum = (
            recency + cross_platform + velocity + dev_interest +
            search + gh_score + social + official + adoption + business
        )

        # Core Area Multiplier
        category = candidate.get("category", "")
        core_categories = {"ai_automation", "telegram_bots", "web_development"}
        multiplier = 1.15 if category in core_categories else 1.0

        total_score = min(100, round(raw_sum * multiplier))

        # Hype Score vs Practical Value Score
        hype_score = candidate.get("hype_score", 45)
        practical_value = candidate.get("practical_value", 85)

        return {
            "total_score": total_score,
            "raw_sum": raw_sum,
            "recency": recency,
            "cross_platform": cross_platform,
            "growth_velocity": velocity,
            "developer_interest": dev_interest,
            "search_momentum": search,
            "github_momentum": gh_score,
            "social_engagement": social,
            "official_confirmation": official,
            "real_world_adoption": adoption,
            "business_impact": business,
            "hype_score": hype_score,
            "practical_value": practical_value,
            "is_security": candidate.get("is_security", False)
        }
