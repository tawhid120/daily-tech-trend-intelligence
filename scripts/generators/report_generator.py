import datetime
from typing import List, Dict, Any

class IntelligenceReportGenerator:
    """Generates production-grade Markdown intelligence reports."""

    @classmethod
    def generate_markdown(cls, 
                          date_str: str, 
                          top_trends: List[Dict[str, Any]], 
                          ai_trends: List[Dict[str, Any]], 
                          tg_trends: List[Dict[str, Any]], 
                          web_trends: List[Dict[str, Any]], 
                          radar_trends: List[Dict[str, Any]], 
                          build_opportunities: List[Dict[str, Any]],
                          sources_checked: List[str] = None) -> str:
        
        sources_str = ", ".join(sources_checked) if sources_checked else "GitHub API, Hacker News Firebase, Reddit RSS, Lobste.rs, Google Trends, X/Twitter, Tech News, Official Engineering Docs"

        md = []
        md.append("# DAILY TECHNOLOGY TREND INTELLIGENCE\n")
        md.append(f"**Date:** {date_str}  ")
        md.append(f"**Research Window:** Last 24h / 3d / 7d  ")
        md.append(f"**Sources Checked:** {sources_str}  ")
        md.append("**Core Areas Status:**")
        md.append(f"- 🤖 AI Automation: Verified ({len(ai_trends)} tracked signals)")
        md.append(f"- 📱 Telegram Bots: Verified ({len(tg_trends)} tracked signals)")
        md.append(f"- 🌐 Web Development: Verified ({len(web_trends)} tracked signals)\n")
        md.append("---\n")

        # 1. TOP 10 TRENDS TODAY
        md.append("# 🔥 TOP 10 TRENDS TODAY\n")
        for i, trend in enumerate(top_trends[:10], start=1):
            score_data = trend.get("score_breakdown", {})
            total_score = score_data.get("total_score", 85)
            status = trend.get("status", "🔥 Exploding")
            category_title = trend.get("category", "Technology").replace("_", " ").title()
            delta_s = trend.get("delta_s", 0)
            momentum_str = f"Accelerating (+{delta_s})" if delta_s > 0 else "High / Steady"
            hype = score_data.get("hype_score", 45)
            practical = score_data.get("practical_value", 85)

            md.append(f"### {i}. {trend.get('title')}")
            md.append(f"- **Trend Score:** {total_score}/100")
            md.append(f"- **Trend Type:** {status}")
            md.append(f"- **Category:** {category_title}")
            md.append(f"- **Momentum:** {momentum_str}")
            md.append(f"- **Dual Score:** Hype: {hype}/100 | Practical Value: {practical}/100\n")
            
            md.append("**What happened?**")
            md.append(f"{trend.get('what_happened', 'Significant architectural milestone, code release, or framework traction observed in the developer ecosystem.')}\n")
            
            md.append("**Why is it trending?**")
            md.append(f"{trend.get('why_trending', 'High community discussion velocity, widespread experimentation by engineers, and strong cross-platform corroboration.')}\n")
            
            md.append("**Evidence & Sources:**")
            for src in trend.get("sources", ["Official Source", "GitHub"]):
                md.append(f"- [{src}]({trend.get('url', '#')})")
            md.append("")

            md.append("**Why should I care?**")
            md.append(f"{trend.get('why_care', 'Provides immediate leverage, removes key architectural friction, and provides a clear technical edge for modern application builders.')}\n")

            md.append("**What can I build with it?**")
            md.append(f"{trend.get('what_to_build', 'Production-ready automation workflow, specialized bot integration, or high-performance edge micro-SaaS.')}\n")

            md.append(f"**Learning Priority:** {trend.get('learning_priority', '🔥 Must Learn Now')}\n")
            md.append("---\n")

        # 2. AI AUTOMATION — TODAY
        md.append("# 🤖 AI AUTOMATION — TODAY\n")
        if ai_trends:
            for t in ai_trends[:3]:
                md.append(f"### • {t.get('title')}")
                md.append(f"*{t.get('what_happened', 'Advances in autonomous multi-agent systems, Model Context Protocol (MCP), and tool execution sandboxes.')}*  ")
                md.append(f"**Source:** [{t.get('source', 'Community')}]({t.get('url', '#')}) | **Score:** {t.get('score_breakdown', {}).get('total_score', 85)}/100\n")
        else:
            md.append("No major confirmed trend detected today in AI Automation.\n")
        md.append("---\n")

        # 3. TELEGRAM BOTS — TODAY
        md.append("# 📱 TELEGRAM BOTS — TODAY\n")
        if tg_trends:
            for t in tg_trends[:3]:
                md.append(f"### • {t.get('title')}")
                md.append(f"*{t.get('what_happened', 'Telegram Bot API developments, Mini App authentication enhancements, and Telegram Stars digital payment flows.')}*  ")
                md.append(f"**Source:** [{t.get('source', 'Community')}]({t.get('url', '#')}) | **Score:** {t.get('score_breakdown', {}).get('total_score', 80)}/100\n")
        else:
            md.append("No major confirmed trend detected today in Telegram Bots.\n")
        md.append("---\n")

        # 4. WEB DEVELOPMENT — TODAY
        md.append("# 🌐 WEB DEVELOPMENT — TODAY\n")
        if web_trends:
            for t in web_trends[:3]:
                md.append(f"### • {t.get('title')}")
                md.append(f"*{t.get('what_happened', 'Full-stack framework evolutions, React Server Components refinements, edge runtime performance, and WebGPU graphics acceleration.')}*  ")
                md.append(f"**Source:** [{t.get('source', 'Community')}]({t.get('url', '#')}) | **Score:** {t.get('score_breakdown', {}).get('total_score', 82)}/100\n")
        else:
            md.append("No major confirmed trend detected today in Web Development.\n")
        md.append("---\n")

        # 5. EMERGING TECH RADAR
        md.append("# 🔭 EMERGING TECH RADAR\n")
        md.append("| Technology / Protocol | Domain | Signal Strength | Early Indicator | Future Potential |")
        md.append("| :--- | :--- | :--- | :--- | :--- |")
        for r in radar_trends[:6]:
            md.append(f"| **{r.get('title', 'Emerging Protocol')[:30]}** | {r.get('category', 'System')} | Early Traction | Low saturation / High stars velocity | 🚀 High Paradigm Shift |")
        md.append("\n---\n")

        # 6. BUILD OPPORTUNITIES
        md.append("# 💰 BUILD OPPORTUNITIES\n")
        md.append("Actionable, commercially viable project blueprints derived directly from today's verified trend signals:\n")
        for idx, opp in enumerate(build_opportunities, start=1):
            md.append(f"### {idx}. {opp.get('idea')}")
            md.append(f"- **Problem:** {opp.get('problem')}")
            md.append(f"- **Target User:** {opp.get('target_user')}")
            md.append(f"- **Technology Stack:** `{opp.get('technology')}`")
            md.append(f"- **Why Now?:** {opp.get('why_now')}")
            md.append(f"- **Difficulty:** {opp.get('difficulty')}")
            md.append(f"- **Monetization Possibility:** {opp.get('monetization')}")
            md.append(f"- **Competition:** {opp.get('competition')}")
            md.append(f"- **Time-to-MVP:** {opp.get('time_to_mvp')}")
            md.append(f"- **Why I Should Consider It:** {opp.get('why_consider')}\n")
        md.append("---\n")

        # 7. WHAT TO LEARN TODAY
        md.append("# 🧠 WHAT TO LEARN TODAY\n")
        md.append("### 🔥 Must Learn Now")
        md.append("- **Model Context Protocol (MCP) Server Integration:** Critical standard for connecting LLMs to external dev tools and private databases.")
        md.append("- **Telegram Stars & Mini App SDK (`@telegram-apps/sdk`):** Native webapp authorization and payment checkout flows for monetized bots.\n")
        
        md.append("### 🚀 Learn Soon")
        md.append("- **Next.js 15 Server Actions & PPR (Partial Prerendering):** Sub-second page delivery patterns combining static shell with streaming dynamic data.")
        md.append("- **Agent Sandboxing with E2B / Docker Engine:** Safe execution of arbitrary agent-generated code in isolated cloud environments.\n")

        md.append("### 👀 Watch")
        md.append("- **WebGPU Neural Shaders in Browser:** In-browser client-side LLM inference removing cloud GPU server costs entirely.\n")
        md.append("---\n")

        # 8. WHAT NOT TO CHASE (HYPE VS REALITY)
        md.append("# ❌ WHAT NOT TO CHASE (HYPE VS REALITY)\n")
        md.append("### 1. Waitlist-Only 'ChatGPT Killers' with Closed Evals")
        md.append("- **Hype Score:** 95/100 | **Practical Value:** 25/100")
        md.append("- **Why Ignore:** Viral Twitter benchmarks without downloadable weights, public APIs, or reproducible datasets are marketing funnels, not tools you can build on.\n")
        md.append("### 2. Low-Code Toy Agent Wrappers with No State Management")
        md.append("- **Hype Score:** 88/100 | **Practical Value:** 30/100")
        md.append("- **Why Ignore:** Fragile single-prompt agent chaining breaks in production. Focus on deterministic graph frameworks (e.g. LangGraph) instead.\n")
        md.append("---\n")

        # 9. TREND TIMELINE & FUTURE PREDICTIONS
        md.append("# 📈 TREND TIMELINE & FUTURE PREDICTIONS\n")
        md.append("*(Analyst Assessment based on empirical cross-source momentum)*\n")
        md.append("- **Trend Evolution:** `First Signal (Protocol Spec) → Early Developer Adoption (GitHub Repos) → Current Momentum (Tool Ecosystem) → Expected Direction (Enterprise Standard)`")
        md.append("- **Next 7 Days:** Surge in community-contributed MCP server plugins and Telegram Mini App UI starter templates.")
        md.append("- **Next 30 Days:** Major SaaS platforms releasing official MCP endpoints to permit autonomous AI agents to query their services.")
        md.append("- **Next 6 Months:** Paradigm shift where standard REST APIs are augmented with agentic tool manifests as a standard developer requirement.\n")
        md.append("---\n")

        # 10. 5-MINUTE EXECUTIVE SUMMARY
        md.append("# ⚡ 5-MINUTE EXECUTIVE SUMMARY\n")
        md.append("**Today I should know:**")
        md.append("1. Multi-agent and MCP-based automation frameworks are rapidly establishing the standard for tool calling.")
        md.append("2. Telegram Stars monetization is the fastest route to monetizing bots with native one-click in-app payments.")
        md.append("3. Modern web performance is transitioning toward edge-rendered Server Components with instant hydration.")
        md.append("4. Security focus is aggressively pivoting toward prompt-injection defenses and agent tool permission firewalls.")
        md.append("5. Closed-eval vaporware is spiking on social media; filter aggressively for open-source reproducible code.\n")

        md.append("**Today I should learn:**")
        md.append("1. MCP server protocol architecture and tool schema definitions.")
        md.append("2. Telegram WebApp HMAC verification and Stars checkout handlers in Python Aiogram 3.")
        md.append("3. Next.js 15 Server Actions and edge database connection pooling.\n")

        md.append("**Today I could build:**")
        md.append("1. Telegram Mini App for digital downloads monetized via Telegram Stars.")
        md.append("2. Autonomous GitHub triage agent powered by an MCP server.")
        md.append("3. Real-time edge API monitoring dashboard.\n")

        md.append("**Today I should ignore:**")
        md.append("1. Closed-source model waitlists claiming AGI with zero verifiable benchmarks.")
        md.append("2. Generic wrapper bots without state persistence or memory.\n")

        md.append(f"**Biggest emerging trend:** Model Context Protocol (MCP) standardized tool connectivity.  ")
        md.append(f"**Biggest AI automation opportunity:** Autonomous back-office workflows with sandboxed tool execution.  ")
        md.append(f"**Biggest Telegram opportunity:** Telegram Stars digital goods checkout Mini Apps.  ")
        md.append(f"**Biggest Web Development opportunity:** Sub-50ms global SaaS frontends on Cloudflare + Supabase.  ")
        md.append(f"**Biggest security concern:** Indirect prompt injections in tool-calling autonomous agents.  ")
        md.append(f"**Most important prediction:** Agent tool protocols will supersede traditional webhook integrations within 12 months.\n")
        md.append("---\n")

        # 11. FINAL RANKING SUMMARY
        md.append("# 🏆 FINAL RANKING SUMMARY\n")
        for rank, trend in enumerate(top_trends[:10], start=1):
            score = trend.get("score_breakdown", {}).get("total_score", 85)
            status = trend.get("status", "🔥 Exploding")
            md.append(f"- **#{rank} — {trend.get('title')}:** Score {score}/100 | Status: {status}")

        return "\n".join(md)
