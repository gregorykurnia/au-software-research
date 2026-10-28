# STATUS

**Current step:** 3.1 done (2026-10-28): `research/03-money.md` has money signals for the 12 Gate 2 passes. Exact-job B1 money: inventory-beside-xero, getting-paid, records-after-exit; broad: job-costing, dispatch-workflow; adjacent only: payroll-in-ledger, entry-review, bill-capture, supplier-payment-runs (tiny); none: invoice-layout, payday-super; barely: shipping-charge-errors. Gate 3 waits for 3.2 (search against) and 3.3 (price anchor).
**Next command:** `next` (runs 3.2)

## Bar (from 00-bar.md)
A$2,500/month revenue ex-GST · 25–45 customers at A$50–100 · ≤5% of reachable buyers · income within 12 months (by ~2027-10).

## Candidates

| Slug | Problem | G2 | G3 | G4 | G5 | G6 | G7 | G8 | Status |
|---|---|---|---|---|---|---|---|---|---|
| inventory-beside-xero | Stock control Xero lacks; Cin7 Core keeps rising | pass | | | | | | | in |
| shipping-charge-errors | Wrong shipping charges go unchecked for months | pass | | | | | | | in |
| payroll-in-ledger | Pay-run setup and manual payslip fixes in Xero/MYOB | pass | | | | | | | in |
| getting-paid | Statements, ageing, interest and receipts sent by hand | pass | | | | | | | in |
| job-costing | Job profit and progress claims kept in spreadsheets | pass | | | | | | | in |
| records-after-exit | Keeping 5–7 years of books after selling or closing | pass | | | | | | | in |
| entry-review | Finding other people's back-dated or uncoded entries | pass | | | | | | | in |
| invoice-layout | Invoices not in the form the customer needs | pass | | | | | | | in |
| payday-super | Super paid on MYOB's date, no receipts, double-pay risk | pass | | | | | | | in |
| dispatch-workflow | Re-keying orders the shipping app can't handle | pass | | | | | | | in |
| supplier-payment-runs | No holds, credits or term-based due dates in bill runs | pass | | | | | | | in |
| bill-capture | Retyping supplier bills the capture tool misread | pass | | | | | | | in |
| ndis-service-dates | Service dates on NDIS invoices | fail (80% one thread) | | | | | | | out; Facebook could rescue |
| payroll-only-plan | Payroll-only Xero users priced out | fail (4 people, 1 site) | | | | | | | out; Facebook could rescue |
| multi-entity-repeat | Same work repeated in each entity's file | fail (4 people) | | | | | | | out |
| tax-obligations | Payroll tax and GST duties the ledger doesn't flag | fail (4 people, 1 site) | | | | | | | out |
| bank-data-housekeeping | Bulk bank data jobs for bookkeepers | fail (4 people, 1 site) | | | | | | | out |
| quote-follow-up | Following up sent quotes | fail (2 people) | | | | | | | out |
| fixed-assets-myob | No asset register in MYOB Business | fail (2 people) | | | | | | | out |

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
| 2026-10-28 | 2.3 done: 24 themes; 2.3b workaround hunt skipped | 15 unserved-job themes, above the ~8 trigger | 02-themes.md, 02-coding.csv |
| 2026-10-28 | Vendor complaints not carried to 2.4 except two named groups: Xero payroll-only users, Cin7 Core users facing price rises | Playbook rule: only a named group wanting a narrower, cheaper alternative | PR-X47, PR-X48, PR-X09, PR-X23; XA-020–027 |
| 2026-10-28 | hipages lead costs (40 items, 19 B1) not carried | Trades want cheaper leads, not narrower software; fix is a two-sided marketplace. Owner may override | PR-H17, AP-009 |
| 2026-10-28 | J-RECON treated as mostly vendor complaint | 16 of 22 items also vendor-coded (MYOB AI auto-match, sync bugs) | MI-57, XA-030 |
| 2026-10-28 | 2.4: 19 candidates from the 15 job themes plus the two named vendor groups | One recurring task for one buyer per candidate; themes split or merged where the job differs (moves noted in the file) | 02-candidates.md |
| 2026-10-28 | Gate 2 counts people, not excerpts; ≤50% from one thread or review listing | One review cut into several excerpts, or one reviewer on two sites (SH-011 = TP-018), is one person | tools/candidates.py |
| 2026-10-28 | Gate 2: 12 pass, 7 fail; 2.5 had no seeds | Counts in `tools/candidates.py`. Only inventory-beside-xero and shipping-charge-errors have 3+ B1 | 02-candidates.md |
| 2026-10-28 | payroll-only-plan and ndis-service-dates out for now; Facebook could add a second source | Matches the 2026-10-28 plan to use Facebook only for promising candidates; both have known blockers (Payroller exists; segment C dropped) | PR-X47, PR-X23; MI-71–74, PR-X44 |
| 2026-10-28 | 3.1: four parallel research agents, one per three candidates; four claims spot-checked on the Xero App Store | Web-heavy step; full tables kept in `collect/money-3.1-group-*.md` | 03-money.md |
| 2026-10-28 | App-store review counts count as B1, graded exact / adjacent / none for this job | Playbook: reviews from paying users of a tool for this job are B1; spend on the platform or a neighbouring tool doesn't prove this job | M-01–M-17 |
| 2026-10-28 | shipping-charge-errors flagged: Sendle closed 2026-01-11, so PR-D04 is stale and only 4 people remain | Recency check; 3.2 confirms or drops it | PR-D04, SH-001, SH-011, SH-034, TP-015 |
