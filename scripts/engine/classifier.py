from typing import Dict, Any

class TrendClassifier:
    """Classifies trends into one of the 8 canonical status archetypes."""

    STATUS_MAP = {
        "exploding": "🔥 Exploding",
        "rising": "🚀 Rising",
        "emerging": "👀 Emerging",
        "important": "🧠 Important",
        "industry_shift": "🏢 Industry Shift",
        "developer_opportunity": "🛠 Developer Opportunity",
        "security_alert": "⚠️ Security Alert",
        "fading": "📉 Fading"
    }

    @classmethod
    def classify(cls, score_breakdown: Dict[str, Any], delta_score: float = 0.0) -> str:
        total_score = score_breakdown.get("total_score", 0)
        velocity = score_breakdown.get("growth_velocity", 0)
        recency = score_breakdown.get("recency", 0)
        dev_interest = score_breakdown.get("developer_interest", 0)
        is_security = score_breakdown.get("is_security", False)
        adoption = score_breakdown.get("real_world_adoption", 0)
        business = score_breakdown.get("business_impact", 0)

        # 1. Security Alert takes absolute priority if triggered
        if is_security:
            return cls.STATUS_MAP["security_alert"]

        # 2. Fading detection
        if delta_score <= -10:
            return cls.STATUS_MAP["fading"]

        # 3. Exploding
        if total_score >= 88 and velocity >= 12 and recency >= 12:
            return cls.STATUS_MAP["exploding"]

        # 4. Industry Shift
        if total_score >= 80 and business >= 4 and adoption >= 4:
            return cls.STATUS_MAP["industry_shift"]

        # 5. Rising
        if total_score >= 75 and velocity >= 9:
            return cls.STATUS_MAP["rising"]

        # 6. Important
        if total_score >= 70 and dev_interest >= 8:
            return cls.STATUS_MAP["important"]

        # 7. Developer Opportunity
        if total_score >= 68 and adoption >= 3 and business >= 3:
            return cls.STATUS_MAP["developer_opportunity"]

        # 8. Emerging (early signal)
        if total_score >= 55 and recency >= 10:
            return cls.STATUS_MAP["emerging"]

        return cls.STATUS_MAP["rising"]
