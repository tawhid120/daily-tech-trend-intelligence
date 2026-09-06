# Trend Signals & Evaluation Guide

This guide defines the 12 primary signals of the **Daily Tech Trend Intelligence System**, how each signal is validated, and how the 100-point Trend Score is mathematically derived.

---

## The 12 Primary Signals

### Signal 1: Search Momentum (0–10 pts)
- **What it measures:** Acceleration of public search interest on Google Trends, Google Search, and Bing.
- **Metrics:** Breakout percentage (>5000% search surge), 24h query acceleration, related topic clustering.
- **Scoring Rubric:**
  - `9-10`: "Breakout" status on Google Trends or >300% search surge in 24h.
  - `6-8`: Sustained elevated search volume across multiple related search terms.
  - `3-5`: Mild upward trajectory in query trends.
  - `0-2`: Baseline search volume or declining interest.

### Signal 2: YouTube Momentum (0–5 pts, part of Growth Velocity / Social)
- **What it measures:** Rate of video creation, viewer velocity, and audience retention.
- **Metrics:** High View-to-Age ratio ($V/A = \frac{\text{views}}{\text{hours elapsed}}$).
- **Signal Quality:** Differentiate between clickbait ("This kills ChatGPT!") and technical walkthroughs ("Building an autonomous agent with the new MCP server in 10 mins").

### Signal 3: Reddit Momentum (0–10 pts, part of Developer Interest)
- **What it measures:** Authentic grassroots developer discussion, troubleshooting, complaints, and adoption stories.
- **Target Subreddits:** r/MachineLearning, r/LocalLLaMA, r/artificial, r/programming, r/webdev, r/reactjs, r/Python, r/devops, r/kubernetes, r/Telegram, r/SaaS.
- **Scoring Rubric:**
  - High engagement: >300 upvotes and >100 technical comments in <24 hours.
  - Multiple threads appearing across 3+ unrelated subreddits simultaneously.

### Signal 4: X / Twitter Momentum (0–10 pts, part of Cross-platform / Growth)
- **What it measures:** Real-time engineering discussions, breaking announcements, benchmark releases.
- **Key Indicators:** Reposts and quote-tweets by recognized builders, core maintainers, and researchers.

### Signal 5: LinkedIn Momentum (0–5 pts, part of Social / Business)
- **What it measures:** Enterprise and engineering management adoption, startup founder reflections, enterprise POC discussions.
- **Key Indicators:** Posts by CTOs, Staff Engineers, and VCs discussing budget allocations or team workflows.

### Signal 6: GitHub Momentum (0–10 pts)
- **What it measures:** Code velocity, star growth rate ($\frac{\Delta \text{stars}}{\Delta \text{time}}$), fork velocity, PR activity, and release tags.
- **Scoring Rubric:**
  - `9-10`: >1,000 stars gained in 24 hours, or a newly created repo reaching >500 stars with multiple active contributors.
  - `6-8`: 200–500 stars in 24 hours with active issues and forks.
  - `3-5`: 50–200 stars in 24 hours.
  - `0-2`: Stagnant repo or historical high star count with zero current velocity.

### Signal 7: Hacker News Momentum (0–10 pts, part of Developer Interest)
- **What it measures:** High-caliber technical scrutiny and intellectual interest from experienced engineers.
- **Key Indicators:** Frontpage rank #1–#5, >200 points within 6 hours, high comment-to-point ratio indicating deep debate.

### Signal 8: News Momentum (0–5 pts)
- **What it measures:** Mainstream tech journalism coverage (TechCrunch, The Verge, Ars Technica, Wired).
- **Validation Rule:** Must not rely purely on syndicated PR press releases. Must be cross-referenced with developer signals.

### Signal 9: Official Release & Verification (0–5 pts)
- **What it measures:** Direct primary-source release note, documentation commit, or signed changelog from the creator/organization.
- **Scoring Rubric:**
  - `5`: Official blog post or GitHub release from the primary maintainer / org.
  - `3`: Verified third-party report citing the official repository commit.
  - `0`: Unverified rumor or leak without architectural confirmation.

### Signal 10: Real-World Adoption (0–5 pts)
- **What it measures:** Whether engineers are deploying this into production or using it to solve actual problems, versus just playing with a toy demo.
- **Indicators:** Production case studies, integration PRs in major open-source repos, enterprise rollout notes.

### Signal 11: Business Impact & Monetization (0–5 pts)
- **What it measures:** Revenue potential, SaaS monetization opportunities, cost-reduction leverage, market creation.
- **Scoring Rubric:**
  - `5`: Opens direct monetization wedge (e.g. Telegram Stars payment flow, enterprise automation replacement).
  - `3`: Incremental efficiency improvement for existing revenue streams.
  - `1`: Purely academic or recreational.

### Signal 12: Novelty & Paradigm Shift (0–15 pts, part of Recency & Growth)
- **What it measures:** Is this a net-new paradigm (e.g., introduction of MCP, WebGPU in browsers, Telegram Stars) or merely an incremental minor version patch?

---

## 100-Point Score Mathematical Compilation

$$\text{Trend Score} = S_{\text{recency}} (15) + S_{\text{cross-platform}} (15) + S_{\text{velocity}} (15) + S_{\text{dev-interest}} (10) + S_{\text{search}} (10) + S_{\text{github}} (10) + S_{\text{social}} (5) + S_{\text{official}} (5) + S_{\text{adoption}} (5) + S_{\text{business}} (5)$$

### Qualitative Adjustment Formula:
$$\text{Final Score} = \min\left(100, \text{Trend Score} \times M_{\text{core\_area}} + B_{\text{reproducible}} + B_{\text{security}}\right)$$
Where:
- $M_{\text{core\_area}} = 1.15$ if topic directly maps to AI Automation, Telegram Bots, or Website Development.
- $B_{\text{security}} = +10$ if it is a verified critical security vulnerability requiring immediate patch.
- $B_{\text{reproducible}} = +5$ if fully open-source with reproducible benchmarks.

---

## Hype Score vs Practical Value Matrix

Every evaluated candidate receives two secondary scores:
1. **Hype Score (0–100):** Volume of marketing, viral adjectives, unverified claims, influencer endorsements.
2. **Practical Value Score (0–100):** Ease of setup, documentation clarity, API stability, actual problems solved, developer utility.

| Category | Hype Score | Practical Value | Recommended Action |
| :--- | :--- | :--- | :--- |
| **Golden Opportunity** | 40–70 | 85–100 | **🔥 Must Learn / Must Build Now** |
| **Viral Breakthrough** | 85–100 | 80–100 | **🚀 High Priority (Ride Momentum)** |
| **Silent Workhorse** | 10–30 | 85–100 | **🧠 Deep Technical Asset** |
| **Pure Hype Trap** | 85–100 | 10–40 | **❌ What NOT to Chase** |
