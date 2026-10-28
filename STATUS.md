# STATUS

**Current step:** 2.2 done (2026-10-28): `research/02-complaints.csv` has 381 buyer items (B1 111, B2 270) from 8 sources; A 213, B 89, D 85. Next: 2.3 code it into themes.
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
| 2026-10-28 | Skip Reddit; Facebook later, targeted after 2.3 | A already well covered; Facebook used only to add an independent source to promising candidates (15–20 min each) | manual/reddit.md |
| 2026-10-28 | Ledger built: 381 items, 8 sources, over the 150–300 aim | A came rich from Chrome sources; B and D needed the app stores. `research/tools/build_ledger.py` rebuilds it and checks excerpt length and dates | 02-complaints.csv |
| 2026-10-28 | 5 vague B1 tags downgraded to B2 (MI-32, PR-M02, PR-M05, PR-H06, PR-H18) | No amount or time stated | 02-complaints.csv |
| 2026-10-28 | Playbook: 2.3 tags themes unserved job vs vendor complaint; new 2.3b workaround hunt if <~8 unserved-job themes | Review sites and idea boards over-represent complaints about existing tools; tool-less jobs show up in forums and Facebook | CLAUDE.md |
