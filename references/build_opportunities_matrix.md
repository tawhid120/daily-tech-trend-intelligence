# Build Opportunities Generation Matrix

This reference guides the agent in deriving actionable, commercially viable project ideas from daily technical trends.

---

## 1. Opportunity Formulation Framework

Every build opportunity must be practical, specific, and tied directly to the day's detected technology signals. Generic suggestions (e.g., *"Build an AI chatbot"*) are strictly prohibited.

Each project idea must fill out these 10 required dimensions:

1. **Idea:** Concise, descriptive title of the system or product.
2. **Problem:** The specific technical friction, cost, or operational bottleneck it solves.
3. **Target User:** Clear persona (e.g., Solo SaaS founders, Telegram community managers, DevOps engineers).
4. **Technology Stack:** Specific tools, libraries, and frameworks (e.g., *Aiogram 3, FastAPI, Redis, Next.js 15 App Router, Supabase, Anthropic Tool Use API*).
5. **Why Now?:** The exact trend, release, or API update that made this project possible or urgent today.
6. **Difficulty:** Rated *Beginner / Intermediate / Advanced / Complex Systems*.
7. **Monetization Possibility:** Freemium subscription, Telegram Stars microtransactions, usage-based API billing, one-time lifetime license.
8. **Competition:** Assessment of existing alternatives (*Low / Moderate / Saturated / Emerging Blue Ocean*).
9. **Time-to-MVP:** Realistic build timeframe (e.g., *24 hours, Weekend Build (2-3 days), 1-2 Weeks*).
10. **Why Consider It:** The strategic competitive advantage or leverage gained by building it now.

---

## 2. Core Domain Archetypes

### Archetype A: Telegram Bot / Mini App (TMA) Wedge
- **Sweet Spot:** Converting complex web or AI workflows into frictionless, mobile-first Telegram Mini Apps.
- **Monetization:** Telegram Stars (`sendInvoice`, digital goods, premium features).
- **Core Stacks:**
  - Frontend: React / Next.js / Vite + `@telegram-apps/sdk` + Tailwind CSS
  - Backend: Python (Aiogram 3 / Pyrogram) + Redis FSM + PostgreSQL
  - Security: `initData` HMAC-SHA256 signature verification.

### Archetype B: Autonomous Agent / AI Automation Workflow
- **Sweet Spot:** Multi-step business workflows that replace manual data entry, scraping, triaging, or customer workflows.
- **Core Stacks:**
  - MCP (Model Context Protocol) servers and custom tool integrations.
  - Python / LangGraph / Temporal / Prefect / Docker sandboxing (E2B).
  - Webhooks + Postgres + Queue workers.

### Archetype C: Web Application & Developer SaaS Wedge
- **Sweet Spot:** Micro-SaaS addressing developer tooling friction, API monitoring, authentication boilerplate, or niche workflow automation.
- **Core Stacks:**
  - Next.js 15, TypeScript, Tailwind, Server Actions, Supabase / Neon Postgres, Stripe / LemonSqueezy.
  - Edge middleware on Cloudflare Workers.

### Archetype D: AI Security & Observability Gateway
- **Sweet Spot:** Reverse proxies for LLM calls that filter prompt injections, redact PII, track token budgets, and provide fallback routing.
- **Core Stacks:**
  - Rust / Go / Python (FastAPI), Redis rate limiting, semantic caching.
