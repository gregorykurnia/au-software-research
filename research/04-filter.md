# 04 — Fit filter (Step 4)

First pass 2026-10-28 on the two Gate 3 passes. The trades widening (T1–T3) may add candidates. Each
one that passes Gate 3 gets a row here, and Gate 4 is judged once that is done.

**Bottom line:** **both pass every limit**, and neither is a clean pass. The real constraints are a
narrow v1 and Xero's API pricing. Xero only lists apps on the App Store at **Plus, A$245 a month**,
and Xero Projects' API **can't take costs**: it handles tasks and time only. So a job-costing tool has
to keep its own cost ledger. Ranked by evidence: **1. inventory-beside-xero, 2. job-costing.**
**Gate 4 isn't met yet** (2 of 3–5). 4.3 (registering the ventures) waits for the widening.

## 4.1 Pass / fail / unknown

| Limit | inventory-beside-xero | job-costing |
|---|---|---|
| 1. Sold and supported online from Indonesia | **pass**: self-serve Xero connect; item import by CSV; buyers find apps on the App Store or by search (Step 6 checks) | **pass**: same; office staff and owners, not site crews |
| 2. No licence or accreditation for v1 | **pass** | **pass** |
| 3. Recurs at least quarterly | **pass**: receiving, pricing and selling, daily to weekly | **pass**: per job, weekly to monthly, and each progress claim (XI-030, XI-033) |
| 4. v1 solo in ~8 weeks | **pass, if narrow**: one or two of kits, price levels and receiving against POs (XI-037, XI-042, XI-044, XI-039). A Cin7 replacement fails this limit, so Cin7 leavers aren't the v1 buyer (3.3) | **pass, if narrow**: budgets and committed costs per job from Xero POs and bills (XI-035), plus progress claims (XI-030). The Projects API has no write endpoint for costs [1], so the app keeps its own job ledger, as CostTracker does |
| 5. ≤5% of reachable buyers | **pass** (low confidence): Xero had ~2.02m AU subscribers at 30 Sep 2025 [2]; even 1% selling stock is ~20,000, against ~900 needed at A$50. 7.1 sizes it properly | **pass** (low confidence): 462,939 construction businesses, 98.6% under 20 staff (Master Builders citing ABS, June 2025) [3]; the Xero Projects subset is unknown. 7.1 sizes it |
| No regulated service | **pass** (but wrong stock counts reach the BAS, AP-028: the tool records stock and never lodges) | **pass** (progress claims under security-of-payment acts are the builder's documents; the tool formats them and gives no legal advice) |
| Data hosted in Australia | **pass**: Vercel and Neon both offer Sydney (ap-southeast-2) | **pass**: same |
| Platform allows it; API cost fits the price | **pass**: Accounting API Items, POs, invoices, bills. Xero tiers [4]: Core A$35 (≤50 connections, **no App Store listing**), Plus A$245 (≤1,000, listing optional). Certification is required to offer the app to users [5]. At 25–45 customers × A$50–150, A$245 is 4–20% of revenue, which the bar already budgets | **pass with a limit**: Projects API reads project totals and writes tasks and time only [1]. The Accounting API covers POs, bills and tracking. Same Xero tiers |

**Platform risk, both:** Xero can change tiers and fees on 60 days' notice, suspend an integration, or
end the terms on 30 days' notice [5]. Xero shipped five features near earlier candidates in 2026 (3.2).

## Risks found in this step

- **inventory-beside-xero: Xero bundles.** The kits idea (XI-037, 167 votes) is "Under review", and staff
  said on 2025-06-06 that they were "doing some early testing of the teams concepts for being able to
  bundle inventory" [6]. A commenter (2026-05-01, not staff) says a focus group was told "early this year".
  Kits alone is too thin a v1 for that reason. Pair it with price levels (XI-042, XI-044; "Not in
  pipeline", no status) or receiving (XI-039).
- **inventory-beside-xero: free rival.** Zoho Inventory's free tier already has kits, price lists and a Xero
  integration (3.2). Step 5 must find a group it serves badly.
- **job-costing: the app can't write into Xero Projects.** Costs live in the app, so buyers keep two places
  for one job. That's acceptable for firms that already left Projects for spreadsheets (XI-035), but it's
  close to what WorkflowMax (A$22/user) and CostTracker (from US$159) already sell.
- **Listing cost before revenue.** Listing on the App Store from day one costs A$245 a month before the first
  customer. The alternative is starting on Core (A$35, no listing) and selling through search and the
  landing page. Step 6 and 8 decide.

## 4.2 Ranking by evidence weight

B1 people first, then B2 people, then sites. Gate 2 counts are from `tools/candidates.py`; Step 3 B1 added.

| Rank | Slug | B1 people | B2 people | Sites | Notes |
|---|---|---|---|---|---|
| 1 | inventory-beside-xero | 10 (+ M-01, M-02) | 13 | 5 | 8 of the 10 ledger B1 are Cin7 price rises, a group v1 doesn't target |
| 2 | job-costing | 2 (+ M-09) | 9 | 3 | Thin on B1. XI-033 ("a couple of days work per month") carries the money case |

## 4.3 Register survivors

Waiting. Gate 4 needs 3–5 survivors. Once the trades widening (T1–T3) has gone through 2.3–Step 3, register
the top 3–5 with `/venture:new-venture`. If the widening adds none, the owner decides whether to go on with
two (below the gate) or widen again (reserve segment E, hospitality).

## Sources (checked 2026-10-28)

1. Xero Projects OpenAPI spec: endpoints are Projects, ProjectsUsers, Tasks and Time; expenses appear only as
   read-only totals. https://raw.githubusercontent.com/XeroAPI/Xero-OpenAPI/master/xero-projects.yaml (R)
2. Xero H1 FY26 investor deck via search summary: Australia ~2.02m subscribers at 30 Sep 2025.
   https://brandfolder.xero.com/NE531UQB/as/ks8qbt4tj62mb8j6hpq6mz/Investor_Deck_H1_FY26_Xero (R, medium:
   not opened directly)
3. Master Builders Australia, citing ABS June 2025. https://masterbuilders.com.au/About-Us/Our-Industry/ (S
   citing R)
4. Xero developer pricing, effective 2 Mar 2026, ex-tax: Starter free (5), Core A$35 (50, 10 GB), Plus
   A$245 (1,000, 50 GB), Advanced A$1,445; overage A$2.40/GB; App Store listing from Plus.
   https://developer.xero.com/pricing (R)
5. Xero Developer Platform Commercial Terms (updated 2025-12-04; s2.1 certification, s2.2(f) fee changes,
   s8 suspension, s9(a) 60 days' notice, s10(a) 30 days to end).
   https://developer.xero.com/xero-developer-platform-commercial-terms (R)
6. Xero Product Ideas, "Inventory – Bundle multiple products together within tracked inventory", 167 votes,
   Under review. https://productideas.xero.com/forums/967139-purchase-orders-bills-inventory/suggestions/45007927-inventory-bundle-multiple-products-together-with
   (B2 thread; staff reply is S)
