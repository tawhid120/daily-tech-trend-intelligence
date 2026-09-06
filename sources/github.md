# GitHub Research Playbook

## Objectives
Extract high-velocity open-source repositories, rapidly trending tools, and framework releases. Detect authentic developer traction versus artificially boosted repositories.

## Metrics & Thresholds
- **Star Velocity ($\Delta \text{Stars}/\text{day}$):**
  - Extreme surge: >1,000 stars/day
  - High traction: 200–500 stars/day
  - Sustained growth: 50–200 stars/day
- **Commit Frequency & Recency:** Latest commit must be within 7 days.
- **Issues & PR Activity:** Ratio of active PRs and issues to stars. Empty issue trackers with thousands of stars indicate bot farms.

## Search Queries & APIs
1. **GitHub Search API:**
   - AI Agents: `topic:ai-agent created:>2026-08-01 sort:stars-desc`
   - Model Context Protocol: `topic:mcp-server sort:updated-desc`
   - Telegram Bots & Mini Apps: `topic:telegram-mini-app sort:stars-desc`, `telegram bot aiogram stars:>50`
   - Modern Web: `topic:webgpu language:typescript created:>2026-07-01`
2. **Release Feeds:** Check releases of major frameworks (Next.js, Vite, Fastify, Aiogram, Pydantic, vLLM).

## Anti-Pattern Check
- If repo has only 1 commit, no source code, and redirect links -> **FLAG AS SPAM**.
