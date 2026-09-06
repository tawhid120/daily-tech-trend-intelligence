# 🌐 Daily Tech Trend Intelligence System
### *Production-Grade, Multi-Source, Multi-Signal Technology Radar & Trend Research Engine*

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Status: Production](https://img.shields.io/badge/status-production--ready-success.svg)]()
[![Platform: Cross-Platform](https://img.shields.io/badge/platform-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey.svg)]()

> **Created by:** [MD Tawhid Islam](https://github.com/tawhid120)  
> **Repository:** `tawhid120/daily-tech-trend-intelligence`

---

## 📖 সারসংক্ষেপ (Overview in Bengali)

**Daily Tech Trend Intelligence** হলো একটি শক্তিশালী, persistent, evidence-based প্রযুক্তি গবেষণা এবং ট্রেন্ড ডিটেকশন সিস্টেম। এটি কোনো সাধারণ নিউজ স্ক্র্যাপার বা সাধারণ Google Trends স্ক্র্যাপার নয়।

এই সিস্টেমটির মূল উদ্দেশ্য হলো প্রতিদিন ইন্টারনেটের টেকনোলজি ইকোসিস্টেম স্ক্যান করে বের করা:
1. **আজ বা গত কয়েক দিনে নতুন কোন প্রযুক্তি, ফ্রেমওয়ার্ক, লাইব্রেরি, মডেল বা টুল এসেছে?**
2. **কোন বিষয়টি ডেভেলপার এবং ইঞ্জিনিয়ারদের মধ্যে দ্রুত মোমেন্টাম পাচ্ছে?**
3. **কোন প্রযুক্তিটি শেখা বা প্রজেক্ট তৈরিতে ব্যবহার করলে আগামী কয়েক মাসে আমার জন্য আনফেয়ার কম্পিটিটিভ অ্যাডভান্টেজ তৈরি হবে?**
4. **কোন বিষয়টি আসল টেকনিক্যাল ব্রেকথ্রু এবং কোনটা শুধুই সোশ্যাল মিডিয়া হাইপ (Hype vs. Practical Value)?**

বিশেষভাবে এই সিস্টেমটি তিনটি **Core Priority-1 Area**-র ওপর জোর দেয়:
- 🤖 **AI Automation & Agentic Systems** (MCP, Autonomous Agents, Multi-agent, Tool Calling, Workflows)
- 📱 **Telegram Bot Development** (Bot API, Mini Apps, Telegram Stars, Aiogram, Pyrogram, Monetization)
- 🌐 **Website & Modern Web Development** (Next.js, React, Bun, RSC, WebGPU, Cloudflare Workers, Edge)

---

## 🏛 System Architecture

```text
daily-tech-trend-intelligence/
├── SKILL.md                          # Master Agent Skill Specification (Frontmatter & Runbooks)
├── README.md                         # Documentation & Usage Guide
├── config/                           # System Configurations
│   ├── topics.yaml                   # Taxonomy & Priority Matrix (Priorities 1, 2, 3)
│   ├── sources.yaml                  # Feed Endpoints, Weights & Reliability Scores
│   └── scoring.yaml                  # 100-Point Scoring Model & Hype Formulas
├── prompts/                          # 5-Pass Research Prompts
│   ├── discovery.md                  # Pass 1: Multi-Source Discovery
│   ├── validation.md                 # Pass 2: Source Corroboration & Anti-Spam
│   ├── scoring.md                    # Pass 3: 100-Point Scoring & Hype Evaluation
│   ├── synthesis.md                  # Pass 4: Historical Comparison & Momentum (ΔS)
│   └── report.md                     # Pass 5: Final Production Report Formatting
├── sources/                          # Platform-Specific Scraping & Signal Guides
│   ├── github.md                     # Star velocity, commit cadence, fork spikes
│   ├── hackernews.md                 # Firebase API, Show HN, point velocity
│   ├── reddit.md                     # Developer subreddits (r/LocalLLaMA, r/programming, r/webdev)
│   ├── x_twitter.md                  # Real-time announcements & viral tech threads
│   ├── youtube.md                    # View-to-Age velocity & tutorial clustering
│   ├── producthunt.md                # New launches & early adopter traction
│   ├── google_trends.md              # Breakout queries & search surges
│   ├── tech_news.md                  # Tier-1 journalism vs PR syndication
│   └── official_sources.md           # OpenAI, Anthropic, Telegram API, Vercel Changelogs
├── references/                       # Deep Engineering References
│   ├── taxonomy.md                   # Full 3-Tier Technology Taxonomy
│   ├── signals_guide.md              # 12-Signal Evaluation Rubric & Math
│   ├── anti_patterns.md              # Anti-Hype, Bot Farms & Fake Repo Filter
│   ├── build_opportunities_matrix.md # 10-Dimension Project Blueprint Generator
│   └── query_playbook.md             # Advanced Search Operators & Boolean Dorks
├── scripts/                          # Executable Python Engine & CLI
│   ├── trend_scout.py                # Master CLI Orchestrator
│   ├── fetchers/                     # Concurrent Network Collectors (HN, GitHub, Reddit, Lobsters)
│   ├── engine/                       # Classifier, Scorer, Deduplicator, History Tracker
│   └── generators/                   # Report Generator & Build Ideator
├── data/                             # Persistent Storage & Database
│   ├── trends/                       # Daily Snapshots (YYYY-MM-DD.json)
│   └── historical/                   # trend-history.json (Trajectories, ΔS, ΔV)
└── examples/
    ├── sample_daily_report_2026_09_06.md  # Real-world Sample Production Report
    └── sample_trend_data.json             # Sample Structured Trend Data
```

---

## ⚡ The 12 Signals & 100-Point Trend Score

সিস্টেমটি প্রতিটি সম্ভাব্য ট্রেন্ডকে নিচের ১২টি সিগন্যালের ভিত্তিতে ০ থেকে ১০০ স্কেলে স্কোর করে:

$$
\text{Trend Score} = S_{\text{recency}} (15) + S_{\text{cross-platform}} (15) + S_{\text{velocity}} (15) + S_{\text{dev-interest}} (10) + S_{\text{search}} (10) + S_{\text{github}} (10) + S_{\text{social}} (5) + S_{\text{official}} (5) + S_{\text{adoption}} (5) + S_{\text{business}} (5)
$$

### Qualitative Multipliers
- **Core Area Bonus:** $\times 1.15$ multiplier for AI Automation, Telegram Bots, and Web Development.
- **Reproducibility Bonus:** $+5$ pts if open-source with reproducible benchmarks.
- **Security Alert:** $+10$ pts for critical zero-day vulnerabilities.

### Dual Score: Hype vs Practical Value
| Classification | Hype (0-100) | Practical Value (0-100) | Recommendation |
| :--- | :--- | :--- | :--- |
| **Golden Opportunity** | 40–70 | 85–100 | 🔥 Must Learn & Build Now |
| **Viral Breakthrough** | 85–100 | 80–100 | 🚀 High Priority (Ride Wave) |
| **Silent Workhorse** | 10–30 | 85–100 | 🧠 Deep Technical Asset |
| **Pure Hype Trap** | 85–100 | 10–40 | ❌ What NOT to Chase |

---

## 🚀 Quickstart & Usage

### 1. Installation

```bash
# Clone the repository
git clone https://github.com/tawhid120/daily-tech-trend-intelligence.git
cd daily-tech-trend-intelligence

# Install lightweight dependencies (only requests and pyyaml required)
pip install requests pyyaml
```

### 2. Run Daily Intelligence Scan via CLI

```bash
# Execute end-to-end multi-source scan and print report to terminal
python3 scripts/trend_scout.py run-all

# Execute scan and save to a specific markdown report file
python3 scripts/trend_scout.py run-all --output data/reports/report-2026-09-06.md

# Inspect historical trajectories and momentum (ΔS)
python3 scripts/trend_scout.py history --limit 10
```

### 3. Use as an Antigravity / Claude Agent Skill

This folder is completely compliant with Antigravity and Claude Code agent skill specifications.
To enable it in your agent environment, simply place it in:
- `~/.agents/skills/daily-tech-trend-intelligence/` or
- `.agents/skills/daily-tech-trend-intelligence/`

The agent will automatically recognize the skill from `SKILL.md` whenever you ask for:
- *"Today's tech trends"*
- *"Run daily tech trend intelligence"*
- *"What should I build today with AI automation and Telegram bots?"*

---

## 📊 Historical Momentum Tracking ($\Delta S$ & $\Delta V$)

The engine stores all observed topics in `data/historical/trend-history.json`:
- **Momentum ($\Delta S$):** $S_{\text{today}} - S_{\text{yesterday}}$
- **Acceleration ($\Delta V$):** $\Delta S_t - \Delta S_{t-1}$

This enables identifying topics that were obscure yesterday (Score 45) but surged today (Score 85, $\Delta S = +40$).

---

## 🛠 Customization

- **Add new research topics:** Edit `config/topics.yaml`.
- **Add new RSS / API feeds:** Edit `config/sources.yaml`.
- **Adjust scoring weights:** Edit `config/scoring.yaml`.

---

## 📄 License
Distributed under the MIT License. See `LICENSE` for details.
