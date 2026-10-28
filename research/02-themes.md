# 02 — Themes (Step 2.3)

Coded 2026-10-28 with the `feedback-analysis` method on all 381 ledger items (`02-complaints.csv`).
Item-level codes: `02-coding.csv`. Counts computed by `tools/code_themes.py` (rerun it to check).
An item carries 1–3 codes. "Sources" counts source sites (ProductReview Xero and MYOB = one site), so it
is conservative. "Top page" = largest share of a theme's items from one thread or review page.

**Bottom line:** 15 unserved-job themes (above the ~8 that would trigger 2.3b, so no workaround hunt
needed). But half the ledger (184 items) is pure vendor complaint, and most job themes are feature gaps
in Xero or MYOB where paid add-ons already exist (S, `02-context.md`). The job themes that look most
fixable from outside the platform with B1 money behind them: **inventory for Xero users squeezed by
Cin7 prices**, **getting paid (statements, chasing)**, **carrier charge errors**, **payroll-only users
priced out of Xero**, **bills on hold / batch credits**. Step 3 decides whether any of them is already
solved.

## 1. Coding frame

| Code | Tag | Definition | Example id |
|---|---|---|---|
| J-INVDOC | Unserved job | Invoice content and delivery: attachments, per-invoice addresses, service dates, hidden lines, bank details per invoice, packing slips | MI-73 |
| J-INVENTORY | Unserved job | Stock control inside or beside the ledger: kits, reorder alerts, receiving, landed cost, price levels, duplicates | XI-037 |
| J-RECON | Unserved job (mostly vendor, see below) | Bank feeds and reconciliation: auto-match errors, bulk posting, statement conversion, bank rules | XI-023 |
| J-PAYROLL | Unserved job | Other payroll admin: payslip adjustments, approvers, staff lists and rates, pay-run setup, payroll-only use | XI-010 |
| J-PAYSUPER | Unserved job | Paying super under Payday Super: choosing the date, receipts, clearing old or duplicate payments | MI-02 |
| J-AP | Unserved job | Bills and paying suppliers: default terms, disputed bills, credits in batch payments, bill data capture | XI-005 |
| J-SHIPOPS | Unserved job | E-commerce dispatch: order edits, multi-parcel orders, two couriers, tracking status, paying the carrier | SH-010 |
| J-ARCHASE | Unserved job | Getting paid: auto statements, ageing, late interest, receipts, quote follow-ups, payment reports | XI-001 |
| J-JOBCOST | Unserved job | Project and job costing for trades: deposits, progress invoices, quote-to-project, cost rates | XI-035 |
| J-MULTI | Unserved job | Several entities or clients: consolidation, repeated contact changes, user access, practice worksheets | XI-016 |
| J-RECORDS | Unserved job | Keeping or exporting records after leaving, selling or restructuring, without a full subscription | MI-63 |
| J-COMPLY | Unserved job | Tax obligations outside the ledger: payroll tax on contractors, GST registration, government portals | WP-01 |
| J-SHIPCOST | Unserved job | Carrier charges that are wrong or unchecked: overcharged rates, surcharges, double charges | PR-D04 |
| J-AUDIT | Unserved job | Checking other people's entries: audit trail, compulsory fields, working papers on journals | MI-42 |
| J-ASSETS | Unserved job | Fixed asset register missing from MYOB Business | MI-23 |
| V-RELIAB | Vendor complaint | Bugs, outages, broken integrations or sync, data loss, carrier delivery failures | XA-030 |
| V-PRICE | Vendor complaint | Price rises, plan restructures, paying for unused features, costly add-ons | PR-X46 |
| V-LEADS | Vendor complaint | hipages: lead price, lead quality, expiring credits, contracts | PR-H17 |
| V-UX | Vendor complaint | Forced product changes and UI regressions (MYOB new UI, AI auto-match, offline removed) | MI-57 |
| V-BILLING | Vendor complaint | Charged after cancelling, hard cancellation, lock-in contracts, exit fees | PR-M31 |
| V-SUPPORT | Vendor complaint | Slow, unhelpful or missing support | PR-M09 |
| V-FIELDAPP | Vendor complaint | Missing features in one trade field app that rivals have (Android, offline, navigation) | XA-006 |
| N-NARROW | Vendor complaint, names a group | Wants a cheaper, narrower or simpler product than the full plan | PR-X47 |
| M-AGAINST | Market signal | Evidence against building: price resistance, no felt pain, status quo wins, accountant lock-in | WP-07 |

Reminder: remove personal data you do not need before pasting.
(The ledger already stores role labels only; no names or contacts appear in this file.)

## 2. Counts (N = 381 items, 6,585 words of excerpt)

| Code | Items | % items | % text | B1 | B2 | Sources | Top page | Segments | Workaround stated | Max idea votes |
|---|---|---|---|---|---|---|---|---|---|---|
| J-INVDOC | 29 | 8% | 8% | 2 | 27 | 5 | 14% | A27 B4 C3 D2 | 13 | 1,467 |
| J-INVENTORY | 23 | 6% | 6% | 10 | 13 | 5 | 22% | A5 D18 | 9 | 167 |
| J-RECON | 22 | 6% | 6% | 6 | 16 | 5 | 18% | A20 B2 | 3 | 789 |
| J-PAYROLL | 17 | 4% | 5% | 3 | 14 | 3 | 35% | A17 | 2 | 522 |
| J-PAYSUPER | 16 | 4% | 5% | 1 | 15 | 3 | 38% | A16 | 5 | 184 |
| J-AP | 16 | 4% | 5% | 1 | 15 | 4 | 19% | A16 | 4 | 1,283 |
| J-SHIPOPS | 14 | 4% | 3% | 1 | 13 | 4 | 43% | A2 D14 | 7 | 13 |
| J-ARCHASE | 13 | 3% | 4% | 2 | 11 | 4 | 15% | A12 B1 | 6 | 1,176 |
| J-JOBCOST | 12 | 3% | 3% | 2 | 10 | 3 | 25% | A3 B9 | 4 | 620 |
| J-MULTI | 7 | 2% | 2% | 1 | 6 | 3 | 29% | A7 | 2 | 363 |
| J-RECORDS | 7 | 2% | 2% | 2 | 5 | 2 | 43% | A7 | 1 | 12 |
| J-COMPLY | 7 | 2% | 2% | 1 | 6 | 1 | 43% | A7 D2 | 0 | – |
| J-SHIPCOST | 6 | 2% | 1% | 4 | 2 | 3 | 33% | D6 | 0 | – |
| J-AUDIT | 6 | 2% | 2% | 2 | 4 | 2 | 33% | A6 | 0 | 593 |
| J-ASSETS | 2 | 1% | 0% | 1 | 1 | 1 | 100% | A2 | 1 | 28 |
| V-RELIAB | 58 | 15% | 14% | 20 | 38 | 5 | 16% | A20 B14 D24 | 7 | – |
| V-PRICE | 47 | 12% | 12% | 32 | 15 | 6 | 32% | A24 B7 D16 | 7 | 38 |
| V-LEADS | 40 | 10% | 11% | 19 | 21 | 3 | 55% | B40 | 1 | – |
| V-UX | 37 | 10% | 10% | 5 | 32 | 3 | 24% | A36 B1 | 4 | 33 |
| V-BILLING | 33 | 9% | 8% | 20 | 13 | 5 | 30% | A11 B11 D11 | 0 | – |
| V-SUPPORT | 28 | 7% | 7% | 9 | 19 | 4 | 43% | A15 B2 D11 | 1 | – |
| V-FIELDAPP | 15 | 4% | 4% | 1 | 14 | 3 | 20% | B15 | 2 | – |
| M-AGAINST | 10 | 3% | 3% | 0 | 10 | 2 | 40% | A9 B1 | 0 | – |
| N-NARROW | 7 | 2% | 2% | 2 | 5 | 1 | 86% | A7 | 0 | – |

Items by tag: vendor only 184 (48%), job only 134 (35%), both 56 (15%), market signal only 7 (2%).
Idea votes are a separate signal from item counts: one Xero idea row stands for hundreds of voters, but
votes are global (not AU-only) and cost the voter nothing.

## 3. Unserved-job themes, ranked by B1 then B2 then sources

"Outside fix" = can a third-party tool fix it without the platform vendor? (Claude's judgement, for Step 4.)

| # | Theme | What the buyer is trying to do (paraphrase) | Ids | Outside fix | Watch-outs |
|---|---|---|---|---|---|
| 1 | **J-INVENTORY** | Product sellers on Xero want simple stock control; Cin7 Core users want the same functions without repeated price rises | B1: XA-019..XA-027, AP-028. B2: PR-X12, PR-X38–X40, TP-023, XI-037..XI-044 | Yes (add-on market) | 8 of 10 B1 are Cin7 price rises (one vendor). Crowded (Cin7, Unleashed, Katana…) — Step 3 |
| 2 | **J-RECON** | Reconcile bank feeds without re-doing auto-matches or broken syncs | B1: MI-47, MI-57, PR-X05, XA-001, XA-016, XA-030 | Core only: statement-to-CSV XI-023, bank rules XI-018, bulk post XI-019, weekly transaction email XI-014 | 16 of 22 also vendor-coded: mostly MYOB AI auto-match and Dext/ServiceM8 sync bugs. WP-05 argues against statement conversion. Treat as vendor complaint |
| 3 | **J-SHIPCOST** | Catch carrier overcharges and wrong surcharges before paying | B1: PR-D04, SH-001, SH-011, SH-034. B2: TP-015, TP-018 | Yes | Small (6). No item says the buyer checks bills today; PR-D04 says most don't |
| 4 | **J-PAYROLL** | Run small-team payroll without paying for the full ledger, and without manual payslip fixes | B1: PR-X34, PR-X47, PR-M25. B2: MI-39,40,43,51,52,69,70, PR-X02,X09,X33,X48, XI-010..012 | Partly (payroll-only apps) | Payroll-only tools exist (S). 6 of 17 from one review page |
| 5 | **J-INVDOC** | Send invoices with the right details: service dates (NDIS), per-job addresses, attachments, hidden cost lines, bank details per account | B1: PR-X44, AP-029. B2: MI-17,18,21,22,31–33,36,37,49,50,55,56,66–68,71–74, PR-X01, PR-M19, XA-012, XI-007,026,028,031 | Partly: only by replacing invoicing | 20 of 29 are MYOB Business gaps; XI-026 (1,467 votes) is In development at Xero. Service-date sub-job (MI-71–74, PR-X44) is segment C |
| 6 | **J-ARCHASE** | Get paid without chasing by hand: auto statements, ageing, late interest, quote reminders, receipts | B1: XI-001 (pays A$99/mo add-on), AP-027. B2: MI-29,30,32, PR-X37, AP-030, XI-002,003,008,009,017,029 | Yes (add-ons exist, S) | XI-001 auto statements is **In development** at Xero (S): will shrink this |
| 7 | **J-JOBCOST** | Trades and project firms track job cost and progress invoices without spreadsheets | B1: PR-X28, XI-033 ("a couple of days work per month"). B2: PR-X07,X17, XA-009,014, XI-029–032,034–036 | Yes | Job-management apps already serve trades (see V-FIELDAPP); 9 of 12 from Xero ideas |
| 8 | **J-RECORDS** | Keep or export old books after selling, closing or restructuring without paying full price | B1: PR-M21, PR-M40. B2: MI-62–64, PR-X20, PR-X36 | Yes, if exported before cancelling | Only 2 sources; MYOB already offers read-only at A$2.50/mo (PR-M40); one-off, not quarterly |
| 9 | **J-AUDIT** | See who changed what, force job codes, attach working papers | B1: MI-42 ("many hours"), XI-015 ("hours this morning"). B2: MI-12,13,41, XI-027 | Partly | XI-015 "Not in pipeline" at Xero |
| 10 | **J-AP** | Hold disputed bills, apply credits in batch payments, pay from the ledger, default supplier terms | B1: MI-15. B2: MI-14,16,65, PR-X03,X04,X08, PR-M38, XA-033,034, XI-004–006,020,024,025 | Yes (approval/AP add-ons, S) | High votes (XI-005 1,283; XI-024 938, not roadmapped) but only 1 B1 |
| 11 | **J-PAYSUPER** | Pay super on the date the business chooses; get receipts; avoid paying twice when switching clearing house | B1: PR-M25. B2: MI-01–11, MI-60,61, PR-X19, XI-013 | Partly | **Recency:** Payday Super began 1 Jul 2026; 13 of 16 are MYOB's own Pay Super. Likely fades as MYOB fixes it |
| 12 | **J-SHIPOPS** | Dispatch orders with two couriers, multiple parcels, edits after checkout, delivered status | B1: XA-029. B2: MI-55,56, SH-003,007,010,029–033,038,041, TP-017 | Yes | 6 of 14 from one AusPost app's reviews; rival apps may already do it |
| 13 | **J-MULTI** | Run several entities: consolidated reports, one address change for all, per-entity worksheets | B1: XI-016 (pays for Syft). B2: MI-67, PR-X20, PR-X32, XI-021,022,027 | Yes (Syft and others, S) | |
| 14 | **J-COMPLY** | Know payroll-tax and GST obligations the ledger doesn't flag | B1: WP-01. B2: WP-02,03,10–13 | Yes | One site only (Whirlpool); WP-09/10 show no felt pain; touches tax advice (lawyer flag) |
| 15 | J-ASSETS | Fixed asset register in MYOB Business | B1: MI-23. B2: MI-24 | Yes | One thread; fails Gate 2 as it stands |

## 4. Vendor complaints

| Theme | Items | Carry to 2.4? | Why (ids) |
|---|---|---|---|
| V-RELIAB | 58 | No | Bugs and sync failures only the vendor can fix (XA-030, SH-009, TP-014) |
| V-PRICE | 47 | **Partly**, via named groups below | Price alone isn't a job. Two named groups want a narrower, cheaper product: |
| ↳ Xero payroll-only and bank-feeds-only users | 4 | **Yes** → J-PAYROLL | PR-X47 (A$20 → A$100/mo, "We only need Payroll"), PR-X48, PR-X09, PR-X23 |
| ↳ Cin7 Core users facing yearly rises | 8 | **Yes** → J-INVENTORY | XA-020–XA-027; XA-022, XA-024, XA-025 say they're looking elsewhere |
| V-LEADS | 40 | No | Trades want cheaper, better leads, not a narrower hipages; the fix is a two-sided marketplace, not admin software. Strong B1 (PR-H17 A$100–200 per lead). Owner may override |
| V-UX | 37 | No | MYOB Business redesign and AI auto-match (MI-57: reconciling went from 1 h to 3 h). Vendor-only |
| V-BILLING | 33 | No | Cancellation and billing practices (PR-M31, SH-006) |
| V-SUPPORT | 28 | No | Hold times up to 8 h 40 min (PR-M09) |
| V-FIELDAPP | 15 | No | Gaps in one field app that rivals fill (TP-003 "Tradify is much better but more costly") |
| N-NARROW | 7 | Merged into J-PAYROLL | Also PR-M26 "a low cost very simple bookkeeping system", PR-X43. One site, 6 of 7 from one page |

## 5. Complaint types (one per item)

| Type | Items | % |
|---|---|---|
| Missing capability | 145 | 38% |
| Price | 72 | 19% |
| Bug | 54 | 14% |
| Service | 53 | 14% |
| Expectation mismatch | 40 | 10% |
| Not a complaint (context, against) | 12 | 3% |
| Confusion | 5 | 1% |

## 6. Alternatives buyers name (as written, counted)

| Alternative | Items | Ids |
|---|---|---|
| Xero (as the place to move from MYOB) | 5 | MI-23, MI-24, MI-45, PR-M28, PR-M39 |
| A third-party / another app / another system (unnamed) | 6 | MI-23, MI-69, PR-X11, PR-X44, SH-031, XI-037 |
| The accountant | 3 | PR-X22, PR-X34, WP-03 |
| QuickBooks | 2 | PR-X22, XI-019 |
| Spreadsheets | 2 | PR-X41, XI-035 |
| MYOB Enterprise | 1 | PR-X16 |
| Reckon | 1 | PR-M28 |
| Tradify | 1 | TP-003 |
| Syft | 1 | XI-016 |
| Paid Nice | 1 | XI-001 |
| MRPEasy | 1 | XA-024 |
| Custom docx template | 1 | XI-031 |
| Outlook calendar reminders | 1 | XI-013 |
| Print to PDF and external email | 1 | MI-30 |
| Word, pasted in | 1 | XA-017 |
| Australia Post site | 1 | SH-033 |
| Googling a local tradie (vs hipages) | 1 | PR-H20 |

## 7. Representative verbatims (job themes)

- J-INVENTORY: XA-022 "price has completely exploded over the year for the same function i'm using for years"; PR-X39 "I am aware of apps available however the ones on offer arent like anything i require."
- J-PAYROLL: PR-X47 "We only need Payroll... The monthly fee goes from $20 last year to $100 per month going forward."; XI-010 "Every time we have a public holiday we need to manually adjust almost every payslip."
- J-SHIPCOST: PR-D04 "Most sellers probably never check the weekly bill Sendle sends out, because it often goes straight to your spam folder."
- J-INVDOC: MI-73 "My NDIS clients need the service date, and now I lose time each week having to add it in manually."
- J-ARCHASE: XI-001 "Paid Nice has good features but not feasible at min $99pm extra for basic plan just to get automated reminders/statements sent."
- J-JOBCOST: XI-033 "Its a couple of days work per month to manually apply."; XI-035 "We are currenly managing our projects offline in spreadsheets"
- J-AP: XI-024 "Applying the credit separately is not efficient, especially when there are 10+ credits they want to use when they pay 20+ bills."
- J-PAYSUPER: MI-02 "We pay weekly, and have an extended Christmas closure… Cashflow does not allow us to pay it all before our closure."
- J-AUDIT: MI-42 "I spend many hours having to go back over entries by other office staff."
- M-AGAINST: WP-07 "just having AI scan support forums for complaints and then vibecode a solution to one specific problem rarely delivers a USP"

## 8. Checks

**Loud minority:** no code has share of text more than twice its share of items, so none is flagged.
**Thread concentration (Gate 2's "not one thread"):** V-LEADS 55% one page, N-NARROW 86%, J-ASSETS 100%,
J-SHIPOPS / J-RECORDS / J-COMPLY / V-SUPPORT 43%, J-PAYSUPER 38%. All others ≤35%.
**Bias:** every source here is a complaint channel (1–3★ reviews, idea boards, problem threads). A run of
complaints is not a rate. Idea boards over-represent features the platform lacks; reviews over-represent
billing and support anger; forums over-represent long-running problems. Xero idea votes are global.
**Switching or cancelling (24 items):** MI-35, MI-38, MI-45, PR-X09, PR-X16, PR-X24, PR-M10, PR-M11,
PR-M20, PR-M39, PR-S03, PR-D03, PR-H01, PR-H05, AP-008, AP-013, TP-003, XA-020, XA-022, XA-024, XA-025,
XA-031, SH-006, SH-016. Most move between big vendors (MYOB ↔ Xero); a churn analysis adds little here.
**Injected content:** none found.

## 9. Top 5 findings

1. **Half the ledger is vendor anger, not unmet jobs** — 184 of 381 items (48%) carry only vendor codes;
   V-RELIAB 58, V-PRICE 47, V-LEADS 40. These need the vendor to fix them.
2. **Inventory beside Xero has the most money evidence** — 23 items, 10 B1, 5 sources (XA-019–027, AP-028,
   XI-037–044), but 8 of the B1 are one vendor's price rises; crowded market to check in Step 3.
3. **Payroll-only Xero users are a named group priced out** — PR-X47, PR-X48, PR-X09, PR-X23 inside a
   17-item payroll theme; one review site dominates (6 of 17 from one page).
4. **Invoice and getting-paid gaps carry the most votes but little money** — J-INVDOC 29 items, J-ARCHASE 13,
   J-AP 16; ideas with 938–1,467 votes; only 5 B1 between them; two top asks are In development at Xero (S).
5. **Small but money-backed: carrier overcharges** — J-SHIPCOST 6 items, 4 B1, 3 sources (SH-001 paid ~$90
   instead of ~$34 for two years); thin on count.

## 10. What we cannot conclude from this data

- How common any need is across Australian businesses: complaints are not a rate.
- Willingness to pay for a new tool, except where buyers state what they pay now (B1 ids above).
- Segment C (NDIS) and E (hospitality) — not sampled beyond 3 MYOB items and 1 review.
- Facebook-group and Reddit buyers — not collected; quieter, tool-less jobs are under-counted.
- Whether the add-ons named in `02-context.md` already solve these jobs (Step 3).

## 11. Assumptions

- Grouping into these 24 codes and the 1–3 codes per item are Claude's judgement (`02-coding.csv`).
- "Outside fix" and "Carry to 2.4?" are Claude's judgement, to be tested in Steps 3–4.
- Source sites stand in for independent sources; two reviews on one page may be the same kind of buyer.
