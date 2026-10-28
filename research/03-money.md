# 03 — Follow the money (Step 3)

## 3.1 Money signals

Collected 2026-10-28 for the 12 Gate 2 passes. Four research agents ran in parallel, one per group of three
candidates. Their full tables, with every link, are in `collect/money-3.1-group-{a,b,c,d}.md`. Four claims
were spot-checked against the Xero App Store and held: ControlC's archive quote, Paidnice's 83 reviews,
Fergus's 79 reviews and the Fergus buyer's quote. 3.2 (search against) and 3.3 (price anchor and Gate 3)
are below.

**How to read it.** A signal is **B1** when a buyer states what they pay, lose or spend in hours, or when
paying users review a tool built for this job. Review counts from the Xero App Store and Shopify App Store
count as B1. They carry three caveats:
- Both stores pool reviews from every country, so they are **not proven Australian**.
- Paidnice (83 of 83 five-star) and Chaser look like solicited review sets.
- Pricing pages and bookkeepers' service fees are **S**. ATO, Fair Work and ACCC figures are **R**. Neither
  counts toward the gate.

Each B1 signal is graded:
- **Exact:** spend on this candidate's job.
- **Adjacent:** spend on a wider or neighbouring job, often to the tool the buyers complain about.
- **None:** no spend found.

New buyer items get ids **M-01…**. Ledger ids are as before.

**Bottom line:** money for the exact job shows up clearly for **inventory-beside-xero**, **getting-paid**
and **records-after-exit**. It shows up in broad form for **job-costing** and **dispatch-workflow**. That
spending mostly goes to incumbents that already sell the fix, so 3.2 has to find a group they serve badly.
Four candidates show money only for a neighbouring job: payroll-in-ledger, entry-review, bill-capture and
supplier-payment-runs (one tool, 3 reviews). **invoice-layout** and **payday-super** have no B1 for their
job. **shipping-charge-errors** has one review, and its main buyer item describes a carrier that closed
in January 2026.

### Summary

| # | Slug | B1 for this job | Strongest signals | What buyers pay today (A$ unless marked; 3.3 firms up) | Flags for 3.2 |
|---|---|---|---|---|---|
| 1 | inventory-beside-xero | **Exact, strong** | Cin7 Core 223 reviews, Unleashed 394, Katana 72, TidyStock 43; M-01 price A$1,188→2,148/yr; ledger XA-019–027 | US$349–729/mo (Cin7 Core, Unleashed); Katana $99→179/mo implied by M-01 (currency not stated); low end unpriced | Xero tracked inventory; TidyStock, inFlow, ReorderPilot (free beta) at the low end |
| 2 | getting-paid | **Exact** | Paidnice 83 (2025–26: M-03, M-04), Chaser 374, CreditorWatch Collect 91, ezyCollect 35; ledger XI-001 | US$69–99/mo (Paidnice) to A$399+/mo (Chaser) | Xero free reminders; Xero auto-statements in development |
| 3 | records-after-exit | **Exact, small dollars** | ControlC 34 reviews, incl. M-07 (non-trading entity, no Xero sub); Numerint 24; ledger PR-M21, PR-M40 | A$2.50/mo (MYOB read-only); US$8–25/mo (ControlC); A$13/org/mo (Ledgerscope); one-off £10–300 (Numerint) | Xero side already has 3 paid tools; no MYOB tool found |
| 4 | job-costing | **Broad** (exact gap thinner) | Fergus 79 incl. M-09 ($70/user, 10 h/mo); Simpro 69 (setup NZ$6k, $3k+); ServiceM8 351; Tradify 187; Payapps 4 (2021) and WorkGuru 21 name spreadsheet hours; ledger XI-033, PR-X28 | A$29–149/mo (ServiceM8 incl GST); US$47–61/user (Tradify); ~$70/user (Fergus buyer) | The paid trade apps already sell costing and progress invoicing |
| 5 | dispatch-workflow | **Broad** (gaps unpriced) | SellerDash 680 reviews (AU, M-10 "hours a week"); Starshipit 210 (Shopify) + 42 Trustpilot incl. M-11 extra fees; Shippit 89; ledger XA-029 | ~US$10–140/mo (SellerDash to Starshipit); up to US$385–1,599 | Crowded and cheap; rivals may already fill each named gap |
| 6 | payroll-in-ledger | **Adjacent** (award, roster, payroll add-ons) | Deputy 148, EH Payroll/KeyPay 37 (M-12: 2 people 3 days → 1 person 1 day), Tanda 51; ledger PR-X34 (pays accountant) | A$3–8/employee/mo (payroll software); A$5–20/employee/run (bureau, S) | Nothing found for stale pay items or approver moves; STP rules (hard limit 2) |
| 7 | entry-review | **Adjacent** (file review in general) | XBert 68 (M-13 "cut my review… in half"), Dext Precision 272; ledger MI-42, XI-015 (hours) | A$7–99/client/mo + A$29/user (XBert); +A$10/client/mo (Dext add-on) | Do these already flag back-dated, uncoded and unsupported entries? Sold to Xero practices, not MYOB office staff |
| 8 | bill-capture | **Adjacent** (paid to the incumbents) | Dext 1,118 reviews (Xero) + 1,991 (Trustpilot, M-14); AutoEntry 465; Lightyear 146 | A$0 (Hubdoc, free with Xero); ~A$34–62/mo (Dext); $155–255/mo (Lightyear) | No spend on fixing misreads; Hubdoc free |
| 9 | supplier-payment-runs | **Exact but tiny** | BatchPay 3 reviews, A$20/mo (M-15, M-16, 2023); ApprovalMax 667 and Lightyear 146 are for approvals and capture | A$20/mo (BatchPay) to ~NZ$171/mo (ApprovalMax Premium, low conf.) | Does Xero AU make ABA batch files natively? (a forum reply and a BatchPay reviewer disagree) |
| 10 | shipping-charge-errors | **Barely** (n=1) | Oh Ship! 1 review, M-17 "$4,700 in carrier adjustment charges" (reviewer listed US); ledger SH-001 is a loss, not spend on a check | ~US$39/mo (Oh Ship!); bundled in Starshipit; Machship from ~$495/mo; consultant ~A$5k per audit (S) | Starshipit ships invoice reconciliation; **Sendle closed 2026-01-11** (PR-D04 is about Sendle); no carrier invoice API found |
| 11 | invoice-layout | **None** | No paid Xero or MYOB layout tool found; only ledger AP-029 (a Xero price complaint) | ~US$35–150 one-off Fiverr template (S); MYOB Business Pro A$70 → AccountRight Plus A$165/mo list for custom forms | Xero custom .docx themes are free; the fix belongs to MYOB |
| 12 | payday-super | **None** beyond PR-M25 (time) | No super or clearing-house app on the Xero App Store; moving super money is free or near-free | A$0–0.30/employee/batch (Xero, Payroller, QuickSuper free; EH A$0.20–0.30) | Law is permanent; MYOB: super still paid when authorised (no fix announced); Xero scheduled super "not on the roadmap" (2026-06-18) |

USD prices are as listed by the vendor. No conversion was made; at roughly A$1.5 per US$ (low confidence),
US$349 is about A$530.

### New buyer items (B1 unless marked; excerpts under 25 words, no names)

| Id | Candidate | Date | Source | Excerpt or fact | Link |
|---|---|---|---|---|---|
| M-01 | inventory-beside-xero | 2024-01-22 | Xero App Store: Katana | "My price went from $1,188.00 a year to $2,148.00 a year after they made their new plans." | https://apps.xero.com/au/app/katana-cloud-inventory/reviews |
| M-02 | inventory-beside-xero | 2025-07-02 | Xero App Store: Unleashed | "Even something as simple as integrating the shopify API costs $60 a month." | https://apps.xero.com/au/app/unleashed-software/reviews |
| M-03 | getting-paid | 2026-06-17 | Xero App Store: Paidnice | "helped us to save many man hours to automate sending statement and calculate late interests" | https://apps.xero.com/au/app/paidnice/reviews |
| M-04 | getting-paid | 2025-08-07 | Xero App Store: Paidnice | "First round of late penalties and everyone magically paid their bill… All in on the Pro plan." | same |
| M-05 | getting-paid | 2015-10-30 | Xero App Store: CreditorWatch Collect (Debtor Daddy) | "saved us $200/ week and 10hrs / week, for doing reconciliation and debt collecting!" (old) | https://apps.xero.com/au/app/creditorwatch-collect/reviews |
| M-06 | getting-paid | 2025-06-03 | Xero App Store: ezyCollect | Quote was "nearly three times what was advertised" (B2: a prospect, not a payer) | https://apps.xero.com/au/app/ezycollect/reviews |
| M-07 | records-after-exit | 2026-05-20 | Xero App Store: ControlC | View the company file "without the need to maintain a Xero subscription for a non-trading entity" | https://apps.xero.com/au/app/controlc/reviews |
| M-08 | records-after-exit | 2026-02-18 | Xero App Store: ControlC | "light years ahead of Ledgerscope - for the same price" (switched between paid tools) | same |
| M-09 | job-costing | 2026-03 | Xero App Store: Fergus | "We pay roughly $70 a user a month, but it easily saves me 10 hours a month" | https://apps.xero.com/au/app/fergus/reviews |
| M-10 | dispatch-workflow | n.d. | Shopify App Store: SellerDash (AU) | "has saved me hours a week manually entering addresses" | https://apps.shopify.com/mypost-shipping-australia-post/reviews |
| M-11 | dispatch-workflow | 2025-08-25 | Trustpilot: Starshipit (AU) | Address edits didn't sync, "which led to paying extra shipping fees" | https://www.trustpilot.com/review/starshipit.com |
| M-12 | payroll-in-ledger | 2026-06 | Xero App Store: Employment Hero Payroll | "What used to take 2 people 3 days to complete a pay run now only takes 1 person 1 day" | https://apps.xero.com/au/app/keypay/reviews |
| M-13 | entry-review | n.d. | Xero App Store: XBert | "cut my review of work time down in half" | https://apps.xero.com/au/app/xbert/reviews |
| M-14 | bill-capture | n.d. | Trustpilot: Dext (AU) | "All for the cost of 1 hrs bookkeeping/month" | https://www.trustpilot.com/review/dext.com |
| M-15 | supplier-payment-runs | 2023-11-27 | Xero App Store: BatchPay | Without an ABA file paying "has been a bit of a hassle since we have to do it one by one manually." | https://apps.xero.com/au/app/batchpay/reviews |
| M-16 | supplier-payment-runs | 2023-09-27 | Xero App Store: BatchPay | "We also regularly need to pay more than 200 bills at a time." | same |
| M-17 | shipping-charge-errors | 2026-06-30 | Shopify App Store: Oh Ship! | "found over $4,700 in carrier adjustment charges across our 2025 orders" (reviewer listed US) | https://apps.shopify.com/oh-ship/reviews |
| M-18 | payday-super | 2026-06-18 | Xero Product Ideas | "Schedule superannuation payments": 87 votes, Accepted; staff: not on the roadmap (B2, not money) | https://productideas.xero.com (idea 51486163) |

n.d. = the agents didn't record the review's date; the listings are active in 2026. Month-only dates are as
the agents recorded them.

### Seller and official context (S/R: explains, doesn't count)

- **Late payment** (R/S): Xero data shows invoices paid 6.6 days late on average (Dec 2025 quarter), an
  estimated A$15,257 a year per business. Vendor data, not opened directly.
- **Super Guarantee** (R): the ATO raised A$1.73bn of SGC in 2024-25, including A$209m in penalties
  (search summary; the ATO page returned 403). The free ATO clearing house closed 1 Jul 2026.
- **Underpayments** (R): Fair Work recovered A$358m in back-pay in 2024-25, about 60% from large
  corporates. No small-business split.
- **Record keeping** (R): failing to keep records costs 20 penalty units, about A$6,600 (search summary).
- **Shipping** (R): AusPost and StarTrack remediation of ~A$2.9m concerned wrongly declined claims, not
  billing. Carrier invoice data is a CSV downloaded by hand (AusPost) or a report by email (StarTrack).
- **Outsourced services** (S): bookkeeping that includes AR or AP runs about A$300–5,000+ a month. Payroll
  bureaus charge A$5–20 per employee per run. A freight audit costs about A$5k a time.

### What 3.1 changes

- **Sendle closed on 2026-01-11** (two news sources, high confidence). PR-D04 is about a carrier that no
  longer exists. Without it, shipping-charge-errors rests on SH-001, SH-011, SH-034 and TP-015: 4 people.
  That is under the Gate 2 bar of 5, so its Gate 2 pass needs re-checking. 3.2 confirms or drops it.
- Where the money is strongest (inventory, getting-paid, job-costing, bill-capture, dispatch), the spend
  already goes to well-reviewed paid tools. That proves pain but means a crowded market. Gate 3 will need a
  named group those tools serve badly, backed by ids.
- Where tools are missing (invoice-layout, payday-super), nobody pays: Xero offers free workarounds, or
  only MYOB can fix it.

## 3.2 Search against it

Done 2026-10-28. Four research agents ran in parallel, in the same groups as 3.1, and each checked five
things: free templates, features already built into Xero, MYOB or Shopify, government tools, cheap apps and
platform roadmaps. Full tables are in `collect/against-3.2-group-{a,b,c,d}.md`, about 150 sourced rows in
all. Four claims were spot-checked and held:
- Statey: Xero statements with ageing, A$15/35/70 a month ex-GST, 19 reviews.
- Shopify: native AusPost labels in the admin since August 2025.
- Xero AU: exports an ABA file from a batch payment (a forum reply, medium confidence).
- MyDataXport: on MYOB's app marketplace with a "one-time backup for closure".

Almost everything here is **S** (help pages, roadmaps, pricing). It shows what exists. It doesn't prove pain.

**Bottom line:** search against them, 9 of the 12 are solved or closing:
- Free or bundled features fill them, or will within about a year: getting-paid, bill-capture,
  dispatch-workflow, supplier-payment-runs.
- Only the platform itself can fix what's left: payroll-in-ledger, payday-super, invoice-layout on MYOB.
- The owner's job happens once: records-after-exit.
- shipping-charge-errors falls to 4 people and now **fails Gate 2**.

Two keep a named group served badly, backed by B1 and durable: **inventory-beside-xero** and
**job-costing**. Both have paid rivals already selling to that group, which is Step 5's problem, not
Gate 3's. **entry-review** keeps a group on MYOB, but it is thin (2 people).

| # | Slug | Free or bundled solves it? | Strongest against (S unless marked) | Group served badly (ids) | Lasts 2 years? | Gate 3 outlook |
|---|---|---|---|---|---|---|
| 1 | inventory-beside-xero | Partly | Zoho Inventory: free tier with kits and a Xero integration (AU edition); paid about A$43–54/mo incl GST (search only). Katana free up to 30 SKUs | Xero sellers missing one or two basics (XI-037, XI-042, XI-044, PR-X12, PR-X38); Cin7 Core leavers (XA-020, 022, 024, 025). Price gap between Zoho and inFlow US$186+, TidyStock NZ$127+ | Yes: no Xero kits, price levels or landed cost dated for AU; Xero Inventory Plus is US-only; XI-043 is categories, not variants | **Likely pass** |
| 2 | getting-paid | Mostly | Xero's scheduled statements went to testers 2026-10-27; free reminders, pay-now links and days-to-pay in Xero; Statey A$15/mo already sells statements | MYOB users wanting emailed receipts (MI-29, MI-30; 20 votes) | No: the 1,176-vote ask ships within ~12 months | Likely fail |
| 3 | records-after-exit | Partly, well enough | MYOB read-only A$2.50/mo incl GST (invite-only, ends 2026-12-31); Xero Ledger A$7/mo via an accountant; a Xero file can be reactivated for 7 years; free exports; MyDataXport on MYOB for closures | MYOB Business owners leaving (MI-62–64), but MI-64 refuses to pay a third party | Yes (5-year rule) | Likely fail; fails hard limit 3 anyway (one-off) |
| 4 | job-costing | Mostly for trades; partly for Xero-only firms | ServiceM8 (351 reviews), Tradify (187), Fergus (79) sell costing at A$30–77/user; Xero Projects has budgets and profit, but on Ultimate only | Xero Projects users who outgrew it: PO costs to projects (XI-035, 620 votes), cost-rate history (XI-034), repeating invoices (XI-033, B1 "a couple of days work per month"), import (XI-036). WorkGuru, Projectworks and WorkflowMax by BlueRock already target them | Yes: progress payments (XI-030) still In development; deposits live June 2026, Stripe only | **Likely pass** (group backed by B1 XI-033) |
| 5 | dispatch-workflow | Mostly | 4 of 6 named gaps filled by Shopify or a rival app; native AusPost labels in Shopify since Aug 2025 | MYOB Business packing slips (MI-55, MI-56, one thread); Starshipit two couriers (SH-010, one person) | No: gaps close yearly | Likely fail |
| 6 | payroll-in-ledger | Partly | XI-010 public holidays: Xero "first release planned for later this year" (2026-09-07); free Fair Work tool and FWC pay-rates API; Deputy, Tanda, RosterElf check awards at timesheet | None an outside tool can serve: MI-39, MI-40, MI-51, MI-52 are settings inside MYOB | Residue only | Likely fail |
| 7 | entry-review | Partly | MYOB's free Journal Security Audit filters by entry date (back-dating); Xero lock dates; XBert flags lock-date moves and attachments over $75 | MYOB staff fixing missing job codes (MI-42 B1 "many hours", MI-41); Xero non-practice users hunting back-dated posts (XI-015, one id) | Yes: Xero declined compulsory tracking (2025-07-15) and an audit trail report (2025-12-08) | Borderline: B1 and a group exist, but 2 people |
| 8 | invoice-layout | Xero: mostly; MYOB Business: no | Xero .docx themes and branding themes; multiple addresses In development; Peppol free on both. A third party can't change MYOB's invoice, only send its own PDF | MYOB Business users whose customers set the form (MI-17, 18, 31, 32, 33, 36, 37, 66, 67) | MYOB unknown; Xero gap closing | Likely fail: no B1 for the job |
| 9 | payday-super | Partly | Xero: multiple authorisers done (Aug 2026), advisor notifications In development; Employment Hero HeroClear already chases approvers; clearing free or <A$0.30 | MYOB employers (MI-01–06, MI-60, MI-61); only MYOB can fix Pay Super | First-year bumps of a July 2026 rule | Likely fail: no B1; moving super money needs an AFSL (lawyer flag) |
| 10 | shipping-charge-errors | Partly | AusPost flags each adjustment free ("Entered As" vs "We Detected") with a free dispute route; no AusPost/StarTrack invoice API found | SH-034 only; SmartCompany 2026-03-26 quotes sellers but is S | Yes | **Gate 2 fail (revised):** 4 people, two jobs |
| 11 | supplier-payment-runs | Mostly | Xero AU exports ABA files, sets due dates per supplier, pays bills in-app (Airwallex A$0.35); Batchly (Apr 2026, 9 reviews) nets credits in runs | Xero bookkeepers needing a hold flag (XI-004, XI-005; free Chrome extensions only); MYOB Business supplier terms (MI-14–16; AccountRight has it) | Shrinking | Likely fail |
| 12 | bill-capture | Partly, closing fast | Xero AI capture in AU beta since 2026-07-02 with line items, GST next; MYOB AI capture free on Lite/Pro; Hubdoc still in Xero plans | Xero users wanting free line splits (PR-X08); email-body invoices (PR-X04), already handled by cheap apps | No | Likely fail (also no B1) |

"Gate 3 outlook" is a reading, not the gate. Gate 3 is judged after 3.3.

### Corrections and flags from 3.2

- **shipping-charge-errors, Gate 2 revised to fail.** Sendle stopped bookings on 2026-01-11, so PR-D04 is
  gone, and SH-011 and TP-018 are one person. That leaves 4 people (SH-001, SH-011, SH-034, TP-015), split
  over two jobs: checkout rates and carrier bills. The SmartCompany article (2026-03-26) quotes sellers on
  AusPost adjustments; adding those quotes as B2 could reopen the carrier-bill half (owner's call).
- **Card fixes:**
  - XI-012 is about super for under-18s working 30+ hours, not junior pay rates.
  - XI-043 ("In development") is product categories, not variants.
  - Xero AU does make ABA batch files, which settles the 3.1 conflict.
- **3.1 missed:** MyDataXport (MYOB archive), Statey (Xero statements, A$15), Batchly (Xero credits in
  payment runs) and Zoho Inventory's free tier.
- **Lawyer flags:**
  - payday-super: moving super money is a licensed service (ASIC treats clearing houses as non-cash
    payment facilities).
  - payroll-in-ledger: a read-only checker that never lodges STP probably avoids ATO software rules
    (low–medium confidence).
- **Rival platforms are shipping fast.** Xero shipped or tested bill payments, AI capture, statements,
  deposits and super authorisers in 2026. A candidate that sits just next to Xero's roadmap fades fast.
  The two durable ones (inventory, Projects) are areas Xero has said nothing dated about.

## 3.3 Price anchor and Gate 3

Done 2026-10-28. Most prices come from 3.1–3.2. This step adds buyer-stated prices from the ledger and
opens six pricing pages for the three candidates still in play. AUD ex-GST unless marked. US$ is
converted at about A$1.5 (low confidence), as in 3.1.

**Bottom line:** **2 pass Gate 3: inventory-beside-xero and job-costing.** entry-review fails: after
narrowing, its group rests on one idea thread. The other eight fail because free or bundled tools solve
the job, only the platform can fix it, or there is no B1. Both passes anchor at about **A$50–150 a
month per business**. That fits the bar (25–45 customers at A$50–100). Gate 4 wants 3–5 survivors, so
two is short.

### New prices opened (S)

| Tool | Price as shown | For which candidate | Link | Conf. |
|---|---|---|---|---|
| Cin7 Core | US$349 Standard (5 users, 2 integrations), US$599 Pro, US$1,199 Advanced a month. "Prices are in USD", for new customers; extra integrations unpriced | inventory | https://www.cin7.com/pricing/ | high |
| Zoho Inventory | Standard about A$53.90 a month incl. GST, or A$43 billed annually (500 orders, 2 users). Review site, verified 2026-03-18; no official AU page found | inventory | https://softwarehq.pages.dev/review/zoho-inventory | medium |
| WorkflowMax by BlueRock | Per user a month (monthly billing): Essentials A$12.22 (3–25 users), Pro A$22 (from 5), Advanced A$37.78 (from 10). Costs on jobs and Xero sync on all plans; progress invoicing (by % of quote or phase) on Pro and up | job-costing | https://workflowmax.com/pricing | high |
| WorkGuru | **Changed:** A$350 a month for 10 users, then A$35 a user; inventory +A$300. 3.2's "A$30/user, min 5" is out of date | job-costing | https://workguru.io/pricing | high |
| CostTracker (Xero app) | POs committed against project budgets. US$159 (1–5 users), A$275 (6–10), billed annually; 1 review | job-costing | https://apps.xero.com/au/app/costtracker | high |
| XBert | Fee per user plus per client file by activity tier; amounts not public. Capterra "from A$99 a month"; an aggregator shows $8.40–118.80 a client plus $34.80 a user, currency not stated | entry-review | https://support.xbert.io/en/articles/5635656-understanding-xbert-pricing | low |

### Price anchors

| # | Slug | What buyers pay today for this job (B1 first) | Nearest priced alternative (S) | Anchor |
|---|---|---|---|---|
| 1 | inventory-beside-xero | Cin7/DEAR users: US$300 a month plus integrations (XA-023); US$5,634 a year proposed, about US$470 a month (XA-024); $4,400 → $4,972 a year, about $370–415 a month (XA-025, currency not stated); US$50 a month in 2015, tripled in 2024 (XA-026). Katana $1,188 → $2,148 a year, about $99 → $179 a month (M-01) | Zoho free tier, then about A$43–54 incl. GST; TidyStock from NZ$127 (about A$115); inFlow US$186 (about A$280); Cin7 Core US$349 (about A$525) | **Xero-only sellers missing basics: A$50–150.** Cin7 leavers paid about A$450–700, but a Cin7 replacement isn't an 8-week v1 (hard limit 4, Step 4) |
| 2 | job-costing | Fergus about $70 a user a month, "saves me 10 hours a month" (M-09). Time: "a couple of days work per month" (XI-033), about A$640–960 a month at A$40–60 an hour (estimate, low confidence) | Xero Projects needs Ultimate: +A$36 a month incl. GST over Comprehensive. WorkflowMax Pro A$22 a user (min 5, A$110); CostTracker A$275 (6–10 users); WorkGuru A$350 (10 users); ServiceM8 A$29–149 incl. GST | **A$50–150 a month per firm.** WorkflowMax sets a low ceiling: progress invoicing for 5 users at A$110 |
| 3 | entry-review | Time only: "many hours" (MI-42), "hours this morning" (XI-015). Nobody is seen paying for this exact check | XBert from about A$99 a month for practices (low confidence); Dext Data Health +A$10 a client | No anchor for the narrow job |
| 4 | getting-paid | Paidnice US$69–99 (XI-001 calls it "min $99pm") | Statey A$15–70; CreditorWatch Collect about A$89 (search only); Chaser from A$399 | A$15–150 |
| 5 | records-after-exit | A$2.50 a month incl. GST to keep MYOB (PR-M40); ControlC US$8–25 (M-07, M-08) | Xero Ledger A$7 via a partner; Numerint one-off £10–300 | A$2.50–25 a month |
| 6 | payroll-in-ledger | Pays the accountant for setup, amount not stated (PR-X34) | Payroller A$0–5.50 per employee; award tools A$8+ per person; bureau A$5–20 per employee per run | A$3–8 per employee a month |
| 7 | invoice-layout | No B1 | Freelance .docx template US$35–150 one-off; AccountRight step-up about A$95 a month | One-off, under A$150 |
| 8 | payday-super | No spend; time only (PR-M25) | Clearing A$0–0.30 per employee per batch | About A$0 |
| 9 | dispatch-workflow | SellerDash and Starshipit users (M-10, M-11); amounts not stated | ReadyToShip US$0.05 a label; SellerDash US$9.99; Starshipit US$35–140 | US$10–140 |
| 10 | supplier-payment-runs | BatchPay A$20 a month (M-15, M-16) | Batchly about A$25 (low); Xero bill payments A$0.35 each | A$20–35 |
| 11 | bill-capture | Dext "the cost of 1 hrs bookkeeping/month" (M-14) | Hubdoc and Xero AI capture free; Dext A$33.58 (+A$28.50 line items) | A$0–60 |

### Gate 3

Pass needs at least one B1 money signal, and nothing free or bundled already solving it well; if
something does, a named group it serves badly, backed by ids.

| # | Slug | B1? | Free or bundled solves it well? | Gate 3 | One line of evidence |
|---|---|---|---|---|---|
| 1 | inventory-beside-xero | Yes, exact | No | **pass** | Xero has no kits, price levels or landed cost and no dated AU plan (3.2); sellers use a second app or duplicate items (XI-037, XI-042, XI-044); Cin7 users pay US$300–470 a month and complain of rises (XA-023–026) |
| 2 | job-costing | Yes | No, for Xero Projects users | **pass** | Projects can't take PO costs (XI-035, 620 votes) and repeating invoices take "a couple of days work per month" (XI-033, B1). The fixes are paid apps (WorkflowMax, CostTracker), not free ones |
| 3 | entry-review | Yes (time) | Partly | **fail** | MYOB's free audit report handles back-dating. What's left is two small groups on one thread each: MYOB job codes (MI-41, MI-42) and Xero change history (XI-015, M-19, M-20). Narrowed to either, it fails Gate 2's one-page rule |
| 4 | getting-paid | Yes | Yes | fail | Free Xero reminders, Statey at A$15 and Xero statements in testing (2026-10-27). The MYOB receipts group (MI-29, MI-30) has no B1 |
| 5 | records-after-exit | Yes, small | Yes, well enough | fail | MYOB A$2.50, Xero Ledger A$7, free exports; MI-64 won't pay a third party. Also a one-off (hard limit 3) |
| 6 | payroll-in-ledger | Adjacent only | Partly | fail | Xero's public-holiday fix is due this year; the MYOB gaps are settings only MYOB can change (MI-39, MI-40, MI-51, MI-52) |
| 7 | invoice-layout | No | Xero mostly | fail | No B1 for the job; the MYOB form can only be changed by MYOB |
| 8 | payday-super | Time only (PR-M25) | Partly | fail | Only MYOB can fix Pay Super; clearing is free; moving super money needs an AFSL |
| 9 | dispatch-workflow | Broad | Mostly | fail | 4 of 6 gaps filled by Shopify or rivals; what's left is one thread (MI-55, MI-56) or one person (SH-010) |
| 10 | supplier-payment-runs | Tiny | Mostly | fail | Xero AU does ABA files and in-app bill payments; Batchly nets credits. The hold group (XI-004, XI-005) has no B1 |
| 11 | bill-capture | Adjacent only | Closing | fail | Hubdoc free, Xero AI capture in AU beta, MYOB capture free on Lite/Pro |
| — | shipping-charge-errors | — | — | out at Gate 2 | Revised in 3.2 to 4 people |

### entry-review: one more search

The rule is that unknown counts as fail unless one more search can settle it. So the XI-015 idea page was
read (20 newest comments, 2026-10-28). Most comments ask for a general audit trail (payroll, leave, XPM,
contacts). Only three are about changed or back-dated transactions: XI-015, M-19 and M-20. Several mention
Sage or the CRA, which suggests non-AU users. Xero staff, 2025-12-08: a full audit trail "is not in our
plans". That settles it: the group is real, but its evidence is one page and not proven Australian.

| Id | Candidate | Date | Source | Excerpt (B2) | Link |
|---|---|---|---|---|---|
| M-19 | entry-review | 2025-02-17 | Xero Product Ideas (XI-015 thread) | "It's so frustrating when prior year data changes." | https://productideas.xero.com/forums/967133-reports-tax/suggestions/45050950-audit-trail-report |
| M-20 | entry-review | 2024-05-22 | same | "You should be able to see the audit trail by account code, by posting date" | same |

Ledger fix: XI-015's date was the thread's newest comment (2025-11-26); the quoted comment is
2025-09-22. Corrected in `collect/xero-ideas.csv` and the ledger rebuilt.

### Risks carried to Step 4 and later

- **inventory-beside-xero:** two groups with different anchors. Xero-only sellers missing one or two
  basics fit an 8-week v1 at A$50–150. Cin7 leavers pay more but need a full replacement and a
  migration. Step 4 should pick the first group, or test whether the second fits hard limit 4.
- **job-costing:** WorkflowMax by BlueRock now sells job costing with progress invoicing at A$22 a user.
  That is Step 5's main threat. XI-035 is "Accepted" on Xero's board (no date). If Xero ships PO costs
  to projects, the wedge narrows. Step 7.4 should check what "Accepted" means on the board.
- **Gate 4 needs 3–5 survivors; only 2 pass Gate 3.** Ways to add one, cheapest first: Facebook to
  rescue payroll-only-plan or ndis-service-dates (15–20 min each, [YOU]); the hipages lead-cost
  override (2.3 decision); reserve segment E (hospitality) through 2.1.
