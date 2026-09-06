# Pass 2: Source Corroboration & Validation Protocol

## Objective
Filter noise, detect spam, deduplicate syndicated PR campaigns, verify publication timestamps, and establish cross-platform corroboration for every raw candidate.

## Validation Gates

### Gate 1: Timestamp & Recency Verification
- Verify the true creation or release date.
- Disqualify articles where old news from 6+ months ago was re-syndicated.
- If an old tool is resurfacing due to a new milestone or major controversy, re-label as `Resurfacing Trend`.

### Gate 2: Duplicate News Clustering
- Identify if multiple news items describe the exact same underlying event (e.g. 10 articles reporting an Anthropic model update).
- Cluster them into a single canonical event entity. Count the independent reporting outlets as evidence points.

### Gate 3: Anti-Spam & Anti-Hallucination Filter
- Run the candidate against `references/anti_patterns.md`:
  - Check GitHub repos for fake star farms (commit history, single markdown file, no actual code).
  - Verify author credibility and benchmark reproducibility.
  - Reject clickbait claims ("RIP Software Engineers") without architectural backing.

### Gate 4: Cross-Source Triangulation
- Test if the candidate appears in at least TWO independent channels:
  - Example A: GitHub commit + Hacker News discussion.
  - Example B: Official announcement + Reddit community thread.
  - Example C: Breaking X developer thread + working demo repository.
- If only one source exists, flag as `[Unverified / Early Signal]`.

## Output of Pass 2
A cleaned list of verified candidates with verified URLs, primary documentation references, and corroborated platform signals.
