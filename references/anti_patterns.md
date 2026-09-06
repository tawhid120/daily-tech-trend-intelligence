# Anti-Patterns & False Positive Filtering

To guarantee that the **Daily Tech Trend Intelligence System** produces authentic, high-value intelligence rather than regurgitating noise, every agent executing this skill must enforce strict anti-pattern filters.

---

## 1. Primary Anti-Patterns

### Anti-Pattern 1: The "Star-Gazing" Bot Farm (Fake GitHub Trending)
- **Symptom:** A repository created 3 days ago jumps from 0 to 4,000 stars, but has only 1 commit ("Initial commit"), zero issues, zero PRs, and commit history consists of a single markdown file with external affiliate links.
- **Verification:** Inspect the contributor list, commit frequency, issue discussions, and stargazer account ages.
- **Action:** Flag as **False Positive / Spam**; disqualify immediately.

### Anti-Pattern 2: The Syndicated PR Echo Chamber (Duplicate News)
- **Symptom:** 25 tech blogs (e.g., TechCrunch, Yahoo Finance, VentureBeat, Barchart) publish identical articles within 1 hour about "Startup X raises $5M for Revolutionary Agent".
- **Rule:** Do NOT count this as 25 distinct trends.
- **Action:** Cluster into a single underlying event. Distinguish paid PR wire syndication from organic developer interest.

### Anti-Pattern 3: The "Kills / RIP" Influencer Clickbait
- **Symptom:** YouTube videos or X threads titled: *"OpenAI just KILLED all software engineers"* or *"RIP React! This new framework is 10000x faster"*.
- **Analysis:** Check actual technical benchmarks. Is there a new breaking API or just an incremental patch?
- **Action:** Assign high Hype Score (>90) and low Practical Value Score (<30). Move to the **❌ WHAT NOT TO CHASE** section.

### Anti-Pattern 4: The Closed-Beta Vaporware Trap
- **Symptom:** Viral landing page with sleek animations, waitlist form, but no docs, no open-source code, no API spec, and no public beta access.
- **Action:** Move to Watchlist / Tier 3 Emerging only. Do not classify as a Tier 1 confirmed trend until developers have hands-on access.

### Anti-Pattern 5: Resurfaced Old News
- **Symptom:** A 2-year-old Reddit post or 2023 paper suddenly reposted on social media and re-indexed.
- **Verification:** Check the original publication timestamp of the underlying paper, commit, or domain.
- **Action:** Label as **"Resurfacing / Historical Discussion"**, not a new breaking trend.

---

## 2. Red Flags Checklist

Before confirming any topic as a **Top 10 Trend**, verify that it does NOT contain:
- [ ] Only 1 isolated social post with no corroborating links
- [ ] Anonymous author claiming unsubstantiated benchmark results
- [ ] Commercial affiliate link masquerading as technical tutorial
- [ ] Crypto token presale requirement disguised as an AI agent protocol
- [ ] Absence of working code, API reference, or functional demo

---

## 3. The "Unverified" Flag Rule

If a topic has intense community chatter but lacks primary-source confirmation or technical verification:
- Mark clearly with: `⚠️ [Unverified / Early Signal]`
- Never state developer adoption as a confirmed fact without primary evidence.
