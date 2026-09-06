# Pass 3: Mathematical Scoring & Hype Evaluation Protocol

## Objective
Apply the 100-point Trend Scoring model, classify the trend type, and calculate the Hype vs Practical Value dual score for every validated candidate.

## Scoring Formula & Weights
Calculate each component according to `config/scoring.yaml`:
1. **Recency (15 max):** <24h = 15, <72h = 10, <7d = 5, >7d = 2.
2. **Cross-Platform Mentions (15 max):** >=4 platforms = 15, 3 = 11, 2 = 7, 1 = 3.
3. **Growth Velocity (15 max):** Rate of growth in stars, engagement, comments, views.
4. **Developer Interest (10 max):** Code contributions, benchmark reviews, implementation questions.
5. **Search Momentum (10 max):** Google Trends breakout status or search volume acceleration.
6. **GitHub Momentum (10 max):** Star velocity, forks, active pull requests, release cadence.
7. **Social Engagement (5 max):** High-signal developer reposts, Reddit upvotes, bookmarks.
8. **Official Confirmation (5 max):** Validated by company/maintainer engineering documentation.
9. **Real-World Adoption (5 max):** Active production integration or developer deployment.
10. **Business Impact (5 max):** Direct monetization wedge, cost reduction, or commercial leverage.

$$\text{Base Score} = \sum \text{Components (max 100)}$$

## Qualitative Modifiers
- Multiply by **1.15** for Core Areas: AI Automation, Telegram Bots, Website Development.
- Add **+5** for fully open-source, reproducible code.
- Add **+10** for critical zero-day or high-impact cybersecurity advisories.
- Cap final score at 100.

## Dual Score: Hype vs Practical Value
- **Hype Score (0–100):** Driven by marketing hype, influencer hyperbole, speculative claims.
- **Practical Value Score (0–100):** Driven by code quality, documentation, production utility, and immediate project-building value.

## Classification Assignment
Assign one of the 8 canonical statuses:
- 🔥 **Exploding** (Score >= 88, high velocity)
- 🚀 **Rising** (Score >= 75, consistent acceleration)
- 👀 **Emerging** (Score >= 65, early signal, high upside)
- 🧠 **Important** (Score >= 70, deep technical significance, non-viral)
- 🏢 **Industry Shift** (Score >= 80, paradigm change)
- 🛠 **Developer Opportunity** (Score >= 72, immediate build wedge)
- ⚠️ **Security Alert** (Critical patch or exploit)
- 📉 **Fading** (Decelerating momentum)
