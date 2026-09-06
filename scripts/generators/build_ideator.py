from typing import List, Dict, Any

class BuildOpportunityIdeator:
    """Derives structured, commercially viable project opportunities from verified trends."""

    @classmethod
    def generate_opportunities(cls, trends: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        opportunities = []

        for trend in trends[:10]:
            title = trend.get("title", "")
            category = trend.get("category", "")
            slug = trend.get("slug", title.lower())

            # Domain tailored generation
            if "telegram" in category or "telegram" in title.lower():
                opportunities.append({
                    "idea": f"Telegram Mini App Suite: {title[:40]} Automation Gateway",
                    "problem": "Telegram users struggle with multi-step off-platform workflows and manual payment friction.",
                    "target_user": "Digital product sellers, bot operators, Telegram community owners.",
                    "technology": "Next.js 15 App Router + @telegram-apps/sdk + Python Aiogram 3 + Telegram Stars API + Redis FSM",
                    "why_now": "Recent Telegram Bot API and Stars monetization capabilities provide zero-friction payment conversion inside Telegram.",
                    "difficulty": "Intermediate",
                    "monetization": "Telegram Stars micropayments (10-50 Stars/action) + monthly VIP tier subscription.",
                    "competition": "Low to Moderate; very few developers have mastered native Telegram Stars invoice integration.",
                    "time_to_mvp": "3 to 4 days (Weekend build)",
                    "why_consider": "Direct access to 950M+ active Telegram users without App Store or Google Play fee hurdles."
                })
            elif "ai_automation" in category or "agent" in title.lower() or "mcp" in title.lower():
                opportunities.append({
                    "idea": f"Autonomous Agent Micro-SaaS: Automated {title[:35]} Pipeline",
                    "problem": "Manual orchestration between disparate developer tools and APIs creates engineering fatigue and latency.",
                    "target_user": "Engineering teams, solo founders, workflow automators.",
                    "technology": "Python LangGraph / CrewAI + MCP Server protocol + FastAPI + Docker E2B sandboxes",
                    "why_now": "The rapid standardization of Model Context Protocol (MCP) enables seamless plug-and-play agent tooling.",
                    "difficulty": "Intermediate to Advanced",
                    "monetization": "Usage-based API tokens + $29/mo starter SaaS plan.",
                    "competition": "Emerging Blue Ocean; agent tooling standards are forming right now.",
                    "time_to_mvp": "1 Week",
                    "why_consider": "High-value enterprise wedge; automate high-friction operational tasks with measurable ROI."
                })
            elif "web" in category or "next" in title.lower() or "react" in title.lower() or "webgpu" in title.lower():
                opportunities.append({
                    "idea": f"Next-Gen Real-Time Web Platform based on {title[:35]}",
                    "problem": "Heavy client-side bundles and slow database hydration degrading Core Web Vitals (INP) and conversion rates.",
                    "target_user": "Modern web developers, e-commerce storefronts, high-traffic SaaS.",
                    "technology": "Next.js 15 Server Components + Turbopack + Cloudflare Workers edge caching + Supabase pgvector",
                    "why_now": "New runtime optimizations and edge rendering benchmarks allow sub-50ms worldwide latency.",
                    "difficulty": "Intermediate",
                    "monetization": "Open-core template with $79 commercial license + hosted cloud sync.",
                    "competition": "Moderate; differentiator is zero-latency edge performance.",
                    "time_to_mvp": "3 to 5 days",
                    "why_consider": "Positions developer at the forefront of modern web architecture with immediate portfolio impact."
                })
            elif "security" in category:
                opportunities.append({
                    "idea": f"Automated Security Sentinel for {title[:35]}",
                    "problem": "Vulnerabilities in agent tool calling and prompt injection bypasses risk severe data leakage.",
                    "target_user": "AI application builders, security engineers, compliance leads.",
                    "technology": "Python FastAPI reverse proxy + Garak red teaming rules + regex/token semantic filter",
                    "why_now": "Rapid emergence of tool-calling agents creates an urgent enterprise demand for agent firewalls.",
                    "difficulty": "Advanced",
                    "monetization": "B2B enterprise licensing ($199–$499/mo per protected agent cluster).",
                    "competition": "Low; most security solutions are still focused on traditional legacy web apps.",
                    "time_to_mvp": "1 to 2 Weeks",
                    "why_consider": "Mission-critical infrastructure with strong customer retention."
                })

        # Ensure at least 5 opportunities exist
        if len(opportunities) < 5:
            opportunities.append({
                "idea": "Universal Multi-Agent Orchestrator CLI for DevOps",
                "problem": "Repetitive deployment diagnostics and log triaging waste hours of engineering time daily.",
                "target_user": "DevOps engineers, SREs, full-stack builders.",
                "technology": "Python Click / Typer + Claude/GPT-4o API + Docker SDK + Telegram Alerts Bot",
                "why_now": "Autonomous agent tool calling has matured to handle shell diagnostics safely.",
                "difficulty": "Intermediate",
                "monetization": "Open-source core CLI + paid team collaboration hub.",
                "competition": "Moderate",
                "time_to_mvp": "2 to 3 days",
                "why_consider": "Builds high operational efficiency and strong open-source developer reputation."
            })

        return opportunities[:8]
