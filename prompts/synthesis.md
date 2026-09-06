# Pass 4: Historical Synthesis & Momentum Protocol

## Objective
Compare today's scored trends against historical records in `data/historical/trend-history.json` to calculate velocity, score deltas ($\Delta S$), and acceleration ($\Delta V$), and maintain the persistent trend lifecycle.

## Mathematical Formulation

### Momentum (Score Delta)
$$\Delta S = S_{\text{today}} - S_{\text{yesterday}}$$
- If $\Delta S > +15$: High Acceleration (Surging).
- If $+5 \le \Delta S \le +15$: Sustained Growth.
- If $-5 \le \Delta S \le +5$: Plateau / Steady State.
- If $\Delta S < -10$: Decelerating / Fading.

### Acceleration
$$\text{Acceleration} = \frac{\Delta S_t - \Delta S_{t-1}}{\Delta t}$$

## Database Sync Procedure
For each trend:
1. Load `data/historical/trend-history.json`.
2. If `topic_id` exists:
   - Update `last_seen` = `current_date`
   - Set `previous_score` = previous `current_score`
   - Set `trend_score` = today's score
   - Record `score_change` = $\Delta S$
   - Append to `score_trajectory` array
3. If new:
   - Create new record with `first_seen` = `current_date`, `status` = `new_entry`
4. Write updated snapshot to `data/trends/YYYY-MM-DD.json` and persist to `trend-history.json`.

## Watchlist Management (Emerging Tech Radar)
Identify topics that score between 55–75 with high Practical Value (>80) and low mainstream saturation (<40). Promote these into `data/historical/radar_watch.json` for continuous tracking before they hit mainstream viral status.
