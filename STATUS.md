# STATUS

**Current step:** 3.3 done (2026-10-28): price anchors and Gate 3 in `research/03-money.md` §3.3. **2 pass Gate 3: inventory-beside-xero and job-costing**, both anchored at about A$50–150 a month per business. entry-review and eight others fail. Gate 4 needs 3–5 survivors, so the owner approved a trades widening (2026-10-28, see decision log).
**Next command:** `go` in a fresh chat. It runs, in order: (1) re-read the 40 hipages items with the job reframed as "get trade work without paying per lead" (enters at 2.5 only if it holds up); (2) Step 4 on inventory-beside-xero and job-costing; (3) trades widening from the new sources T1–T3 in `01-sources.md` (T1 Seek and T2 Etsy need the Mac on with Claude in Chrome; T3 runs from the server). New items then go through 2.3–Step 3 like everything else.

## Bar (from 00-bar.md)
A$2,500/month revenue ex-GST · 25–45 customers at A$50–100 · ≤5% of reachable buyers · income within 12 months (by ~2027-10).

## Candidates

| Slug | Problem | G2 | G3 | G4 | G5 | G6 | G7 | G8 | Status |
|---|---|---|---|---|---|---|---|---|---|
| inventory-beside-xero | Stock control Xero lacks; Cin7 Core keeps rising | pass | pass | | | | | | in (Gate 3 pass; anchor A$50–150/mo) |
| shipping-charge-errors | Wrong shipping charges go unchecked for months | fail (revised 3.2: 4 people, two jobs) | | | | | | | out; SmartCompany quotes could reopen the carrier-bill half |
| payroll-in-ledger | Pay-run setup and manual payslip fixes in Xero/MYOB | pass | fail | | | | | | out (only the platform can fix it) |
| getting-paid | Statements, ageing, interest and receipts sent by hand | pass | fail | | | | | | out (free/bundled solves it) |
| job-costing | Job profit and progress claims kept in spreadsheets | pass | pass | | | | | | in (Gate 3 pass; anchor A$50–150/mo; WorkflowMax A$22/user is the threat) |
| records-after-exit | Keeping 5–7 years of books after selling or closing | pass | fail | | | | | | out (A$2.50–7 bundled options; one-off) |
| entry-review | Finding other people's back-dated or uncoded entries | pass | fail | | | | | | out (group rests on one thread per platform) |
| invoice-layout | Invoices not in the form the customer needs | pass | fail | | | | | | out (no B1) |
| payday-super | Super paid on MYOB's date, no receipts, double-pay risk | pass | fail | | | | | | out (only MYOB can fix it; AFSL flag) |
| dispatch-workflow | Re-keying orders the shipping app can't handle | pass | fail | | | | | | out (gaps filled by Shopify or rivals) |
| supplier-payment-runs | No holds, credits or term-based due dates in bill runs | pass | fail | | | | | | out (Xero ABA and bill payments built in) |
| bill-capture | Retyping supplier bills the capture tool misread | pass | fail | | | | | | out (free capture closing the gap) |
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
| 2026-10-28 | 3.2: four parallel agents searched against all 12; four claims spot-checked (Statey, Shopify AusPost labels, Xero ABA export, MyDataXport) | Same groups as 3.1; full tables in `collect/against-3.2-group-*.md` | 03-money.md §3.2 |
| 2026-10-28 | shipping-charge-errors: Gate 2 revised to fail, out | Sendle closed (PR-D04 stale) and SH-011 = TP-018, leaving 4 people over two jobs; below the bar of 5 | SH-001, SH-011, SH-034, TP-015 |
| 2026-10-28 | Gate 3 outlook: likely pass inventory-beside-xero, job-costing; borderline entry-review; rest likely fail | Rest solved by free/bundled features or closing on Xero's 2026 roadmap, platform-only fixes, no B1, or one-off. Gate itself waits for 3.3 | 03-money.md §3.2 |
| 2026-10-28 | Lawyer flags: payday-super (moving super money needs an AFSL), payroll-in-ledger (a read-only checker probably avoids ATO software rules, low–medium confidence) | Playbook: regulated-service check | collect/against-3.2-group-c.md |
| 2026-10-28 | 3.3: prices from 3.1–3.2 plus six pricing pages opened; ledger prices for Cin7 and Katana users | Anchors per candidate in a table; WorkGuru's pricing changed to A$350 for 10 users | 03-money.md §3.3 |
| 2026-10-28 | Gate 3: pass inventory-beside-xero, job-costing; fail the other nine | Others are solved by free/bundled tools, fixable only by the platform, or lack B1 | 03-money.md §3.3 |
| 2026-10-28 | entry-review fails Gate 3 after one more search | XI-015 thread adds only 2 change-history comments (M-19, M-20), not proven AU; narrowed groups fail Gate 2's one-page rule | XI-015, M-19, M-20, MI-41, MI-42 |
| 2026-10-28 | XI-015 date corrected 2025-11-26 → 2025-09-22 | Ledger had the thread's newest comment date, not the quoted comment's | collect/xero-ideas.csv |
| 2026-10-28 | Anchors: A$50–150/mo for both passes; inventory aimed at Xero-only sellers missing basics, not Cin7 leavers | Cin7 leavers pay more but need a full replacement, which isn't an 8-week v1 | XA-023–026, M-01, M-09, XI-033 |
| 2026-10-28 | Trades widening approved: Seek job ads, Etsy templates, Reddit via search snippets (T1–T3); Facebook dropped for now | 97% of the ledger came from reviews and idea boards, which surface platform gaps; these look for tool-less jobs and the money behind them | 01-sources.md update |
| 2026-10-28 | Plan for `go`: hipages re-read, then Step 4 on the two passes, then T1–T3 collection | Gate 4 needs 3–5 survivors and only 2 pass Gate 3; trades holds both strongest signals (job-costing, hipages spend) | 03-money.md §3.3 |
