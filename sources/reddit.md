# Reddit Research Playbook

## Objectives
Extract unvarnished developer feedback, real-world friction, bug reports, and organic tool recommendations across specialized tech subreddits.

## Monitored Subreddits
- **AI & ML:** r/LocalLLaMA, r/MachineLearning, r/artificial, r/ClaudeAI, r/OpenAI
- **Web & Software:** r/programming, r/webdev, r/reactjs, r/Python, r/node
- **Infrastructure & Security:** r/devops, r/kubernetes, r/netsec, r/selfhosted, r/sysadmin
- **Ecosystems & Business:** r/Telegram, r/SaaS, r/startups

## Extraction Strategy
- Use public RSS endpoints: `https://www.reddit.com/r/{subreddit}/top/.rss?t=day`
- Focus on recurrent patterns:
  - *"Anyone else having issues with X?"* -> Reliability/stability signal.
  - *"I replaced X with Y and cut costs by 80%"* -> Emerging migration trend.
  - *"Show Reddit: I built an autonomous agent for X"* -> Build opportunity signal.

## Rules
- Treat Reddit as a sentiment indicator, not absolute truth. Always cross-verify code claims.
