# STATUS

**Current step:** 2.2 collection in progress. Chrome sources done 2026-10-27 (`research/manual/`: MYOB Idea Exchange, ProductReview, Whirlpool; Reddit blocked by the extension). Still to do: automated sources on the server; Facebook by the owner; Reddit by hand or skip (owner's choice).
**Next command:** `next`

## Bar (from 00-bar.md)
A$2,500/month revenue ex-GST · 25–45 customers at A$50–100 · ≤5% of reachable buyers · income within 12 months (by ~2027-10).

## Candidates

| Slug | Problem | G2 | G3 | G4 | G5 | G6 | G7 | G8 | Status |
|---|---|---|---|---|---|---|---|---|---|
| — | none yet | | | | | | | | |

## Smoke-test pass numbers
Not set yet (Step 8.4). Defaults: ≥100 targeted visitors per finalist; pass at ≥10% qualified email sign-ups; strong pass if anyone asks to pay early.

## Decision log

| Date | Decision | Why | Evidence ids |
|---|---|---|---|
| 2026-10-27 | Planning rate 1 AUD = 10,500 IDR, kept | Actual ~12,550; cautious rate gives ~19% cushion | 00-bar src 4 |
| 2026-10-27 | Revenue target A$2,500/month ex-GST | Covers A$1,905 take-home + costs at every price point | 00-bar §1.2–1.3 |
| 2026-10-27 | Time limit 12 months | Owner's answer | — |
| 2026-10-27 | No seeds from first attempt | Owner chose to start clean from buyer complaints | — |
| 2026-10-27 | Gate 1 passed | Owner confirmed the bar in 00-bar.md | — |
| 2026-10-27 | Proposed segments A Xero/MYOB, B trades, C NDIS/allied health, D e-commerce; E hospitality as reserve | Admin-heavy, online, reachable from Indonesia; C has thin automated data | 01-sources |
| 2026-10-27 | Segments A, B, D approved; C dropped, E reserve | Owner's choice; C had thin automated data | 01-sources |
| 2026-10-27 | Bot-blocked public sites via Claude in Chrome on the owner's Mac; Facebook by hand | Owner allowed browser for public sites; a plain headless browser on the server was blocked by all of them | 01-sources |
| 2026-10-27 | Chrome collection done: MYOB Idea Exchange 74, ProductReview 119, Whirlpool 13 excerpts; Reddit not collected | The extension refuses reddit.com; no workaround tried. Sendle and Shopify added on ProductReview to cover segment D | manual/*.md |
