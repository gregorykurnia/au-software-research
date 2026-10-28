# 03 — Follow the money (Step 3)

## 3.1 Money signals

Collected 2026-10-28 for the 12 Gate 2 passes. Four research agents ran in parallel, one per group of three
candidates. Their full tables, with every link, are in `collect/money-3.1-group-{a,b,c,d}.md`. Four claims
were spot-checked against the Xero App Store and held: ControlC's archive quote, Paidnice's 83 reviews,
Fergus's 79 reviews and the Fergus buyer's quote. 3.2 (search against) and 3.3 (price anchor) come next;
**Gate 3 is not judged yet.**

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
