# 02 — Candidates (Steps 2.4–2.5) and Gate 2

Built 2026-10-28 from `02-themes.md` and the ledger (`02-complaints.csv`). Which ids support which
candidate is Claude's judgement; the counts are from `tools/candidates.py` (rerun it to check).
Every candidate comes from an unserved-job theme, plus the two named vendor groups carried by 2.3
(payroll-only Xero users, Cin7 Core users).

**Bottom line:** 19 candidates; **12 pass Gate 2, 7 fail.** Gate 2 is a low bar: it counts complaints,
not spending. Only two passes have more than two B1 items: **inventory-beside-xero** (10 B1, but 8 are
one vendor's price rises) and **shipping-charge-errors** (4 B1, but only 5 people). The other ten have
0–2 B1, and some of those are spend on the platform, not on this job (MI-15, AP-029). For six of the
twelve passes Xero lists part of the fix as *In development* (e.g. XI-001 statements, XI-026 addresses,
XI-030 progress invoices, XI-010 public-holiday payslips): Step 3 has to weigh that. Two near-misses could come back
with one more independent source: **payroll-only-plan** and **ndis-service-dates**.

## Gate 2 as applied

- **Buyer items** = B1/B2 ledger items about this exact problem, **counted per person**: one review cut
  into several excerpts, role "same", or the one reviewer who posted on two sites (SH-011 = TP-018)
  counts once.
- **Independent sources** = source sites (8 in the ledger; ProductReview Xero, MYOB and Sendle are one).
- **Not mostly one thread** = no more than half the people from one idea thread, forum thread or one
  product's review listing. This is stricter than the 2.3 "Top page" column.
- Pass needs ≥5 people, ≥2 sites and ≤50% from one page.

| # | Slug | Problem (short) | People | B1 | B2 | Sites | Top page | G2 |
|---|---|---|---|---|---|---|---|---|
| 1 | inventory-beside-xero | Stock control Xero lacks; Cin7 Core keeps rising | 23 | 10 | 13 | 5 | 39% | pass |
| 2 | shipping-charge-errors | Wrong shipping charges go unchecked for months | 5 | 4 | 1 | 3 | 40% | pass |
| 3 | payroll-in-ledger | Pay-run setup and manual payslip fixes in Xero/MYOB | 13 | 2 | 11 | 3 | 15% | pass |
| 4 | getting-paid | Statements, ageing, interest and receipts sent by hand | 11 | 2 | 9 | 4 | 18% | pass |
| 5 | job-costing | Job profit and progress claims kept in spreadsheets | 11 | 2 | 9 | 3 | 27% | pass |
| 6 | records-after-exit | Keeping 5–7 years of books after selling or closing | 7 | 2 | 5 | 2 | 43% | pass |
| 7 | entry-review | Finding other people's back-dated or uncoded entries | 6 | 2 | 4 | 2 | 33% | pass |
| 8 | invoice-layout | Invoices not in the form the customer needs | 22 | 1 | 21 | 5 | 14% | pass |
| 9 | payday-super | Super paid on MYOB's date, no receipts, double-pay risk | 16 | 1 | 15 | 3 | 38% | pass |
| 10 | dispatch-workflow | Re-keying orders the shipping app can't handle | 14 | 1 | 13 | 4 | 43% | pass |
| 11 | supplier-payment-runs | No holds, credits or term-based due dates in bill runs | 10 | 1 | 9 | 2 | 30% | pass |
| 12 | bill-capture | Retyping supplier bills the capture tool misread | 5 | 0 | 5 | 2 | 40% | pass |
| 13 | ndis-service-dates | Service dates on NDIS invoices | 5 | 1 | 4 | 2 | 80% | fail |
| 14 | payroll-only-plan | Payroll-only Xero users priced out | 4 | 2 | 2 | 1 | 100% | fail |
| 15 | multi-entity-repeat | Same work repeated in each entity's file | 4 | 1 | 3 | 2 | 50% | fail |
| 16 | tax-obligations | Payroll tax and GST duties the ledger doesn't flag | 4 | 1 | 3 | 1 | 50% | fail |
| 17 | bank-data-housekeeping | Bulk bank data jobs for bookkeepers | 4 | 0 | 4 | 1 | 25% | fail |
| 18 | quote-follow-up | Following up sent quotes | 2 | 0 | 2 | 2 | 50% | fail |
| 19 | fixed-assets-myob | No asset register in MYOB Business | 2 | 1 | 1 | 1 | 100% | fail |

Order: passes by B1, then B2, then sites (the Step 4.2 rule). "Votes" below are Xero or MYOB idea votes:
global, and free to cast.

## Passing candidates

### 1. inventory-beside-xero
**Problem:** small product businesses on Xero can't run stock control in Xero (kits, receiving against
POs, landed cost, price levels, preferred supplier per SKU, duplicate parts), and the add-on many use,
Cin7 Core (formerly DEAR), has gone up in price every year.
- **Who:** two groups. Xero-only product sellers who want basic stock features (XI-037–044, PR-X12,
  PR-X38); Cin7 Core users weighing a move (XA-020–027, TP-022).
- **Task:** receiving, reordering, pricing and counting: daily to weekly.
- **Today:** a separate inventory app (XI-037); overwrite the unit price on every line (XI-044); one item
  per price level (XI-042); archive duplicates (XI-041); stay on Cin7 because "migrating is a headache"
  (XA-021); invoices made by hand (AP-028).
- **Cost:** US$150 → US$300/month plus integrations (XA-023); US$750/yr → US$5,634/yr proposed in 2025
  (XA-024); $4,400 → $4,972/yr (XA-025); tripled in 2024 (XA-026); wrong stock counts flow into the BAS
  (AP-028).
- **Evidence:** B1 XA-019–027, AP-028 · B2 PR-X12, PR-X38 (=X39), PR-X40, TP-022, TP-023, XI-037–044 ·
  max 167 votes.
- **For Step 3:** proof people pay, not proof a new tool wins: switching cost protects Cin7 (XA-021).
  Search Unleashed, Katana, inFlow, Xero's own tracked inventory and the cheap reorder add-ons. XI-043
  (product grouping) is In development.

### 2. shipping-charge-errors
**Problem:** Australian online sellers pay wrong shipping charges for months (checkout rates set too
high, weight surcharges on correctly measured parcels, reprocessed labels charged twice) because nobody
checks charges against the orders.
- **Who:** Shopify sellers using Starshipit, Shippit and AusPost apps; Sendle senders.
- **Task:** checking the weekly carrier bill and each order's charge: weekly.
- **Today:** nothing: "Most sellers probably never check the weekly bill Sendle sends out" (PR-D04).
- **Cost:** international checkout rates ~$90 instead of ~$34 for two years (SH-001; who paid the
  difference isn't stated); shipments charged twice (SH-011); extra postage despite correct measurements
  (SH-034); weight and dimension surcharges (TP-015).
- **Evidence:** B1 PR-D04, SH-001, SH-011 (=TP-018), SH-034 · B2 TP-015.
- **For Step 3:** thin (exactly 5 people), and no buyer says they would pay for the check. These are two
  checks, not one: checkout rates (SH-001) and carrier bills (the rest). Sendle may have wound down in
  Australia around Jan 2026 (low confidence, `manual/productreview.md`). Search parcel-audit services and
  whether carrier invoices can be read by API.

### 3. payroll-in-ledger
**Problem:** small employers running payroll inside Xero or MYOB can't set up pay runs and STP on their
own, and they fix payslips by hand: public holidays, junior hours, hidden or stale pay items, approver
changes.
- **Who:** small employers and their bookkeepers (PR-X33, MI-39, MI-51); employers of juniors (XI-012).
- **Task:** every pay run, weekly to monthly; setup once, then each change.
- **Today:** ask the accountant (PR-X34); adjust "almost every payslip" each public holiday (XI-010);
  move staff to another approver one by one (MI-51); "another system to keep track of employees" (MI-69).
- **Cost:** accountant fees for setup (PR-X34, amount not stated); "lots of time" on employee and super
  setup (PR-M25); time per run (MI-40).
- **Evidence:** B1 PR-X34 (=X33), PR-M25 · B2 PR-X02, XI-010, XI-011, XI-012, MI-39, MI-40, MI-43, MI-51,
  MI-52, MI-69, MI-70 · max 522 votes (XI-010, In development).
- **For Step 3:** a list of small platform gaps rather than one job; the outside fix is another payroll
  product, a crowded field. Payroll that reports STP must meet the ATO's rules for software providers:
  check against hard limit 2 in Step 4.

### 4. getting-paid
**Problem:** small businesses with account customers chase payment by hand because the ledger won't
send monthly statements automatically, show ageing on statements, add late interest to an invoice,
email receipts (MYOB) or report on how each customer pays.
- **Who:** product and service businesses invoicing on terms (PR-X37); MYOB users who need receipts
  (MI-29, MI-30).
- **Task:** monthly statements, weekly chasing, a receipt per payment.
- **Today:** email each receipt by hand (MI-29); print to PDF and send from their own email (MI-30); delete and
  remake an invoice to add interest (XI-002); a credit note for every short payment (XI-009); a paid
  add-on (XI-001).
- **Cost:** Paid Nice "min $99pm extra" just for automated reminders and statements (XI-001); plan rose
  $25 → $100/month with still no statements (AP-027); "Angry clients, late payments" (MI-32).
- **Evidence:** B1 XI-001, AP-027 · B2 MI-29, MI-30, MI-32, PR-X37, XI-002, XI-003, XI-008, XI-009,
  XI-017 · max 1,176 votes.
- **For Step 3:** Xero auto statements (XI-001) are In development, with testers in Oct 2026 (S): that
  removes the biggest ask. XI-002, 003, 009, 017 are Accepted. Paid chasing add-ons exist (S). The MYOB
  receipts gap is separate and small.

### 5. job-costing
**Problem:** trades and project businesses on Xero keep job budgets, progress claims and labour cost in
spreadsheets because Xero Projects and their trade app don't show true job profit.
- **Who:** builders, trades and project firms using Xero Projects, Tradify or Fergus.
- **Task:** per job weekly to monthly, and every progress claim.
- **Today:** "managing our projects offline in spreadsheets" (XI-035); separate invoices with amounts
  worked out by hand (XI-030); assigning projects to repeating invoices by hand (XI-033).
- **Cost:** "a couple of days work per month" (XI-033); rebillable expenses dropped, "expensive mistakes"
  (PR-X28).
- **Evidence:** B1 XI-033, PR-X28 · B2 PR-X07, PR-X17, XA-009, XA-014, XI-030, XI-032, XI-034, XI-035,
  XI-036 · max 620 votes (XI-035, Accepted).
- **For Step 3:** progress invoicing (XI-030) is In development. Trade job apps (Simpro, AroFlo,
  ServiceM8, Tradify, Fergus) compete hard; XA-009 and XA-014 complain about their reports, so the gap
  may sit inside them rather than in Xero.

### 6. records-after-exit
**Problem:** owners who sell, close or restructure must keep 5–7 years of books, but keeping them means
keeping a subscription, and bulk export is capped.
- **Who:** sold the business (PR-M21); sole trader turned company (MI-63); downgrading user (PR-M40);
  owner of two businesses (PR-X20).
- **Task:** one export at exit, then occasional look-ups.
- **Today:** keep paying (PR-M21); read-only access at A$2.50/month (PR-M40); re-enter by hand (MI-63).
- **Cost:** an ongoing subscription "just to keep records" (MI-63); A$2.50/month (PR-M40).
- **Evidence:** B1 PR-M21, PR-M40 · B2 MI-62, MI-63, MI-64, PR-X20, PR-X36.
- **For Step 3:** a one-off event, so it will likely fail hard limit 3 (recurs quarterly) in Step 4.
  MYOB's read-only plan is the A$2.50 anchor. MI-64 refuses to pay a third party.

### 7. entry-review
**Problem:** bookkeepers and office managers who check other people's entries spend hours finding
back-dated postings, missing job codes and journals with no support, because the ledger doesn't flag
them.
- **Who:** office admin checking staff entries (MI-42); bookkeepers with clients (MI-41); firms dealing
  with auditors (MI-13); Xero users finding postings into past periods (XI-015).
- **Task:** month end and BAS.
- **Today:** go back over every entry (MI-42); correct at month end (MI-41); give an assistant full
  standard access (XI-027).
- **Cost:** "many hours" (MI-42); "hours this morning" (XI-015).
- **Evidence:** B1 MI-42, XI-015 · B2 MI-12, MI-13, MI-41, XI-027 · max 593 votes (XI-015, Not in
  pipeline).
- **For Step 3:** three different checks (back-dated, compulsory codes, attachments). File-health tools
  for practices exist (S). XI-027 is In development.

### 8. invoice-layout
**Problem:** small businesses, mostly on MYOB Business, can't send invoices in the form their customer
needs (PDF attached for the customer's payables system, a different address per job, no cost breakdown,
the right bank account, no shipping fields), so they fix invoices one by one.
- **Who:** subcontractors to builders (MI-37); suppliers to store chains (MI-36); building and
  construction (MI-31); clubs and associations (MI-49, MI-66); service businesses (MI-50); Xero users who
  bill lump sums (XI-031).
- **Task:** every invoice.
- **Today:** email the invoice to themselves, delete the table and forward it (MI-18); a
  recurring-transaction trick (MI-22); tick "include attachments" on each invoice (MI-33, XI-028); a
  custom docx template (XI-031); change the company bank details per invoice (MI-66).
- **Cost:** time per invoice; cost breakdown leaked to a customer (MI-17); "Angry clients, late payments"
  (MI-32); invoices filtered as spam (PR-M19). The one B1 is a price complaint (AP-029).
- **Evidence:** B1 AP-029 · B2 MI-17, MI-18, MI-21, MI-22, MI-31, MI-32, MI-33, MI-36, MI-37, MI-49, MI-50,
  MI-66, MI-67, MI-68, PR-X01, PR-M19, XA-012, XI-007, XI-026, XI-028, XI-031 · max 1,467 votes (XI-026, In
  development).
- **For Step 3:** seven different asks, almost no money. 15 of 22 are MYOB Business gaps, which MYOB is
  "slowly adding them back in" (MI-21). A third party can only fix it by sending its own invoice instead.

### 9. payday-super
**Problem:** since Payday Super began (1 Jul 2026), small employers pay super every pay run, and MYOB's
Pay Super takes the money on the day it's approved rather than a chosen date, gives no quick receipts,
and may pay super already paid through another clearing house.
- **Who:** small employers paying weekly or fortnightly (MI-02, MI-03); bookkeepers and advisers running
  payroll for several small clients (MI-04, MI-05, MI-08, MI-10, XI-013).
- **Task:** every pay run.
- **Today:** schedule bank payments and process on return (MI-02); approve before going on leave (MI-04);
  email MYOB for receipts, 5+ working days (MI-60); journals through a suspense account (MI-11); Outlook
  reminders so clients approve batches before Xero's cut-off (XI-013).
- **Cost:** cash flow (MI-02, MI-03); risk of paying twice (MI-08, MI-09); SGC lodgements when clients pay
  late (MI-10); setup time (PR-M25).
- **Evidence:** B1 PR-M25 · B2 MI-01–11, MI-60, MI-61, PR-X19, XI-013 · max 73 votes.
- **For Step 3:** recency: a new rule, and 14 of 16 are about one MYOB product, which MYOB can fix.
  Moving super money is a clearing-house service (flag for the lawyer check if a candidate touches it).
  The part an outside tool could own is approval chasing for bookkeepers (XI-013, MI-04, MI-05, MI-10):
  only 4 people on its own.

### 10. dispatch-workflow
**Problem:** Australian Shopify sellers re-key orders when their shipping app can't handle edits after
checkout, several parcels in one order, two couriers in one print run, delivered status back to Shopify,
or paying the carrier inside the app.
- **Who:** Shopify sellers on Starshipit, an AusPost app and Interparcel; a seller using a 3PL (TP-017);
  MYOB sellers who need packing slips (MI-55, MI-56).
- **Task:** daily dispatch.
- **Today:** update both platforms by hand (SH-003); delete and re-import orders (SH-007); enter extra
  parcels separately (SH-030); another app for delivery tracking (SH-031); log into Australia Post to pay
  (SH-033); use the invoice as a packing slip (MI-56).
- **Cost:** time; "large chargebacks, return fees, misdeliveries" from address errors (XA-029).
- **Evidence:** B1 XA-029 · B2 SH-003, SH-007, SH-010, SH-029, SH-030, SH-031, SH-032, SH-033, SH-038,
  SH-041, TP-017, MI-55, MI-56.
- **For Step 3:** 6 of 14 are reviews of one AusPost app (SellerDash). These are gaps in named apps
  whose rivals may already fill them; the shipping-app field is crowded.

### 11. supplier-payment-runs
**Problem:** bookkeepers and businesses paying many supplier bills at once can't hold a disputed bill,
net supplier credits inside a batch payment, or set due dates from each supplier's terms, so they work
around it bill by bill.
- **Who:** bookkeepers paying bills for clients (XI-005, MI-65); businesses with regular suppliers
  (MI-14); a company with several entities (MI-15).
- **Task:** weekly or fortnightly payment runs.
- **Today:** apply each credit separately before the batch (XI-024); type every due date (MI-14); log into
  the bank separately (XI-025).
- **Cost:** bills approved by mistake (XI-006); "10+ credits... 20+ bills" per run (XI-024). The one B1 is
  money paid for MYOB itself (MI-15, A$3,780+/yr), not a cost of this job.
- **Evidence:** B1 MI-15 · B2 MI-14, MI-16, MI-65, XI-004, XI-005, XI-006, XI-020, XI-024, XI-025 · max
  1,283 votes (XI-005, Accepted).
- **For Step 3:** many votes, little money. XI-024 is Accepted but a commenter says it isn't on the
  roadmap (S). Outside fix = a payment-run tool that makes the bank file itself; paying from the ledger
  (XI-025) touches payment services.

### 12. bill-capture
**Problem:** small businesses still retype supplier bills because the capture tool misses GST, can't
read emailed invoices, doesn't split lines, or loses bills.
- **Who:** small business owners on Xero (PR-X03); Hubdoc users (XA-033, XA-034); MYOB users (PR-M38).
- **Task:** every bill, weekly.
- **Today:** type it in; "would have been faster entering in Xero directly" (XA-033).
- **Cost:** time; missed supplier payments (PR-M38). No B1.
- **Evidence:** B2 PR-X03 (=X04), PR-X08, PR-M38, XA-033, XA-034.
- **For Step 3:** exactly 5 people, no money signal, and mostly quality complaints about crowded
  existing tools (Dext, Hubdoc, Xero's own capture).

## Failing candidates

| Slug | Who and task | Today and cost | Ids | Why it fails | Could one more search settle it? |
|---|---|---|---|---|---|
| ndis-service-dates | NDIS providers who must show each service date for plan managers; every invoice | Type dates into descriptions, one invoice per service (MI-72, MI-73); a second invoicing program (PR-X44, B1) | MI-71–74, PR-X44 | 4 of 5 from one MYOB thread | Yes: NDIS provider Facebook groups (owner, 15–20 min). Segment C was dropped, and NDIS invoicing tools exist (S) |
| payroll-only-plan | Employers who use Xero only for payroll; every pay run | Plan went A$20 → A$100/month (PR-X47, B1); per-employee fees (PR-X23, B1); considering moving payroll off Xero (PR-X09) | PR-X47, PR-X48, PR-X09, PR-X23 | 4 people, all one ProductReview listing | Yes: a second site (Facebook, or Xero ideas for a payroll-only plan). Even then: MYOB's standalone Payroller exists (PR-M25 uses it) and STP rules apply |
| multi-entity-repeat | Owners and accountants repeating work in each entity's file; monthly | Pay for Syft for consolidated P&L (XI-016, B1); one address change entered per entity (PR-X32); copying worksheets (XI-021) | XI-016, XI-021, PR-X20, PR-X32 | 4 people | No. Narrowed from 2.3's J-MULTI: MI-67 moved to invoice-layout, XI-027 to entry-review, XI-022 (trust types) is a different job |
| tax-obligations | Small employers and sellers missing payroll tax on contractors or the GST threshold | Revenue NSW payroll-tax assessment (WP-01, B1); registered for GST after passing $75k on eBay (WP-11) | WP-01–03, WP-10–13 | 4 people (WP-01–03 one person), Whirlpool only | Unlikely. Also tax advice: lawyer flag |
| bank-data-housekeeping | Bookkeepers moving bank data in bulk: statements to CSV, bank rules, bulk posting | Click each transaction (XI-019, In development); no CSV from clients (XI-023) | XI-014, XI-018, XI-019, XI-023 | 4 people, Xero ideas only | No. Against: WP-05 (banks give 2–7 years of CSV). Paid tools exist (S) |
| quote-follow-up | Trades following up sent quotes | Nothing stated | XI-029 (539 votes, Accepted), AP-030 | 2 people | No |
| fixed-assets-myob | MYOB Business users needing an asset register | A third-party asset system (MI-23, B1) | MI-23, MI-24 | 2 people, one thread | No |

## 2.5 Seeds

None. The owner chose to start clean (decision 2026-10-27). An idea added later with `add idea:` enters
here and goes through Gate 2 with `tools/candidates.py`.

## Considered, not carried

- **Bank reconciliation rework** (MI-46, MI-47, MI-57–59): MYOB's AI auto-match; only MYOB can fix it
  (MI-57 closed 2026-07-13, no opt-out).
- **Broken integrations** (XA-001, XA-016, XA-030, XA-032, PR-X05): buyers want the sync fixed. Only
  XA-001 asks to be warned ("without warning and not notifying us"), so there's no detection job with
  5 people.
- **hipages leads, trade field-app gaps, a cheaper simple ledger** (V-LEADS, V-FIELDAPP; PR-M26, PR-X43):
  the 2.3 decisions stand. You can override them.

## Against, for every candidate

- WP-07: "just having AI scan support forums for complaints and then vibecode a solution to one specific
  problem rarely delivers a USP." That is the known weakness of this method; Step 5's gap and Step 8's
  smoke test are the answer to it.
- Accountants choose the ledger (PR-X22, PR-X24), and doing nothing often wins (PR-X41, WP-09).

## Assumptions

- Grouping ids into candidates and splitting or merging themes is Claude's judgement. Splits and moves are
  noted above.
- Same review listing on the same date = one person. This may merge two real reviewers; it only ever
  lowers counts.
- Source sites stand in for independent sources; two reviews on one site may still be the same kind of
  buyer.
