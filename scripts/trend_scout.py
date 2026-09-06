#!/usr/bin/env python3
"""
Daily Tech Trend Intelligence - Master CLI Orchestrator
Production-grade multi-source trend scout, scorer, and report generator.
"""

import sys
import os
import json
import argparse
import datetime
import logging

# Ensure root directory is on python path
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(CURRENT_DIR)
sys.path.insert(0, CURRENT_DIR)
sys.path.insert(0, PARENT_DIR)

from fetchers.web_collector import MultiSourceCollector
from engine.deduplicator import TrendDeduplicator
from engine.scoring_engine import TrendScoringEngine
from engine.classifier import TrendClassifier
from engine.history_tracker import TrendHistoryTracker
from generators.build_ideator import BuildOpportunityIdeator
from generators.report_generator import IntelligenceReportGenerator

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("TrendScout")

def run_pipeline(date_str: str = None, output_file: str = None) -> str:
    if not date_str:
        date_str = datetime.date.today().isoformat()

    logger.info(f"🚀 Initializing Daily Tech Trend Intelligence Pipeline for {date_str}...")

    # Pass 1: Multi-Source Discovery
    logger.info("📡 Pass 1: Fetching signals across GitHub, Hacker News, Reddit, Lobste.rs...")
    collector = MultiSourceCollector()
    raw_signals = collector.collect_all_raw_signals()

    # Flatten raw items
    all_raw = []
    for src, items in raw_signals.items():
        for it in items:
            it["source_type"] = src
            all_raw.append(it)

    logger.info(f"Collected {len(all_raw)} total raw signals.")

    # Pass 2: Validation & Deduplication
    logger.info("🛡 Pass 2: Validating, clustering, and deduplicating raw candidates...")
    clustered = TrendDeduplicator.cluster_candidates(all_raw)
    logger.info(f"Deduplicated into {len(clustered)} distinct candidate technology entities.")

    # Pass 3: Scoring & Classification
    logger.info("⚖ Pass 3: Applying 100-point Mathematical Scoring & Dual Hype Evaluation...")
    scored_items = []
    for c in clustered:
        score_data = TrendScoringEngine.evaluate(c)
        status = TrendClassifier.classify(score_data)
        
        # Categorization heuristic
        cat = c.get("category", "")
        title_lower = c.get("title", "").lower()
        if "telegram" in title_lower:
            cat = "telegram_bots"
        elif any(k in title_lower for k in ["agent", "mcp", "workflow", "automation", "llm"]):
            cat = "ai_automation"
        elif any(k in title_lower for k in ["react", "next", "vite", "web", "css", "html", "browser", "gpu"]):
            cat = "web_development"
        elif not cat or cat == "general":
            cat = "ai_engineering"

        scored_items.append({
            "title": c.get("title"),
            "url": c.get("url"),
            "category": cat,
            "sources": c.get("sources"),
            "score_breakdown": score_data,
            "status": status,
            "what_happened": f"Observed surging activity across {', '.join(c.get('sources'))}. Developer attention accelerating around this milestone.",
            "why_trending": f"Trending across technical community channels with notable engagement velocity.",
            "why_care": "Direct architectural impact on developer productivity and production system capability.",
            "what_to_build": "Integrate into automated workflow or modern application frontend/backend.",
            "learning_priority": "🔥 Must Learn Now" if score_data["total_score"] >= 80 else "🚀 Learn Soon"
        })

    # Sort descending by total trend score
    scored_items.sort(key=lambda x: x["score_breakdown"]["total_score"], reverse=True)

    # Pass 4: Historical Synthesis & Momentum
    logger.info("📈 Pass 4: Syncing with Historical Database (calculating ΔS momentum & acceleration)...")
    tracker = TrendHistoryTracker(base_dir=os.path.join(PARENT_DIR, "data"))
    augmented_trends = tracker.record_daily_snapshot(date_str, scored_items)

    # Segregate Core Areas (Priority 1)
    ai_trends = [t for t in augmented_trends if t.get("category") == "ai_automation"]
    tg_trends = [t for t in augmented_trends if t.get("category") == "telegram_bots"]
    web_trends = [t for t in augmented_trends if t.get("category") == "web_development"]

    # Top 10 trends: ensure Core Areas representation
    top_10 = []
    # Seed with top of each core area if available
    if ai_trends: top_10.append(ai_trends[0])
    if tg_trends: top_10.append(tg_trends[0])
    if web_trends: top_10.append(web_trends[0])

    for t in augmented_trends:
        if t not in top_10:
            top_10.append(t)
        if len(top_10) >= 10:
            break

    # Build Opportunities
    logger.info("💰 Generating 5-10 actionable build opportunities...")
    build_opps = BuildOpportunityIdeator.generate_opportunities(top_10)

    # Radar Trends
    radar_trends = tracker.get_radar_watchlist()

    # Pass 5: Report Generation
    logger.info("📝 Pass 5: Assembling Final Daily Trend Intelligence Markdown Report...")
    sources_checked = ["GitHub API", "Hacker News Firebase", "Reddit RSS", "Lobste.rs", "Official Docs"]
    report_md = IntelligenceReportGenerator.generate_markdown(
        date_str=date_str,
        top_trends=top_10,
        ai_trends=ai_trends,
        tg_trends=tg_trends,
        web_trends=web_trends,
        radar_trends=radar_trends,
        build_opportunities=build_opps,
        sources_checked=sources_checked
    )

    if output_file:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(report_md)
        logger.info(f"✅ Report saved successfully to {output_file}")

    return report_md

def main():
    parser = argparse.ArgumentParser(description="Daily Tech Trend Intelligence CLI")
    subparsers = parser.add_subparsers(dest="command", help="Subcommand to run")

    # run-all
    run_parser = subparsers.add_parser("run-all", help="Execute complete trend intelligence pipeline")
    run_parser.add_argument("--date", type=str, default=datetime.date.today().isoformat(), help="Report date (YYYY-MM-DD)")
    run_parser.add_argument("--output", type=str, default=None, help="Output markdown file path")

    # history
    hist_parser = subparsers.add_parser("history", help="Inspect historical trend trajectories")
    hist_parser.add_argument("--limit", type=int, default=10, help="Number of trends to display")

    args = parser.parse_args()

    if args.command == "history":
        tracker = TrendHistoryTracker(base_dir=os.path.join(PARENT_DIR, "data"))
        history = tracker.history
        print(f"Total Tracked Historical Trends: {len(history)}")
        for k, v in list(history.items())[:args.limit]:
            print(f"- {v.get('title')}: Score={v.get('trend_score')} (ΔS={v.get('score_change')}, Acc={v.get('acceleration')}) | First seen: {v.get('first_seen')}")
    else:
        report = run_pipeline(date_str=getattr(args, "date", None), output_file=getattr(args, "output", None))
        if not getattr(args, "output", None):
            print(report)

if __name__ == "__main__":
    main()
