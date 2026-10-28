# 02 — hipages re-read (2.5 check)

Done 2026-10-28. The 40 hipages items (PR-H01–22, AP-001–014, TP-010–013) were re-read with the job
reframed as **"get trade work without paying per lead"**, to see if it enters at 2.5.

**Bottom line: it doesn't hold up. Not entered.** The money is real (16 people state spend), but it is
spend on hipages, and the items are about hipages' price, quality and contracts. Only **one** item
(PR-H20) points at the reframed job, and none asks for a tool or describes a workaround. The jobs a tool
could do here (own site, Google profile, review requests, booking) are free or already sold cheaply and
crowded, and a tool can't create demand: that takes a marketplace or an agency. Re-opens only if T3
(Reddit snippets) finds 5+ trades describing how they win work directly.

## Two readings, counted with `tools/candidates.py` rules

| Reading | Ids | People | B1 | Sites | Top page | Gate 2 |
|---|---|---|---|---|---|---|
| Broad: paying per lead, poor return | 33 lead-cost items (account and contract-only items dropped: PR-H01–03, H09, H12, H16, AP-012) | 29 | 16 | 3 (PR 13, Apple 13, TP 3) | 45% | pass on numbers |
| Narrow: wants work without lead fees | PR-H20 only | 1 | 0 | 1 | 100% | **fail** |

Same person: PR-H04 = H05 = TP-012 (same words on two sites, two days apart); PR-H07 = H08; PR-H10 = H11
(same listing, same date). The broad reading is the 2.3 vendor complaint V-LEADS again: only hipages, or a
rival marketplace, can fix lead price and quality. The 2.3 decision stands.

## What the 40 items actually say

| What the item is about | People (approx.) | Example ids |
|---|---|---|
| Lead price and price rises | 11 | PR-H07, PR-H17 (A$100–200/lead), AP-003 (+20–30%/yr), AP-004, AP-010 |
| Dead, fake, far or tiny leads | 9 | PR-H10, PR-H13, PR-H15, AP-001, AP-009 (4 of 33 converted, ~A$550) |
| Subscription, nothing in return | 7 | PR-H14 (A$480, no jobs), PR-H19, TP-011, TP-013 |
| Contracts, cancel fees, lost credits | 9 | PR-H05 (A$900 exit), PR-H09, PR-H21, AP-006 |
| Platform rules (waitlist, licence, bans) | 3 | PR-H02, PR-H16, PR-H22 |
| **Names a way to win work directly** | **1** | PR-H20: "a customer can google someone local and approach them" |

## Compared to what (all S, seller pages; checked 2026-10-28)

| Route to work without hipages | Cost | Source |
|---|---|---|
| Google Business Profile | Free; depends on reviews | https://tradiescaler.pages.dev/lead-generation/hipages-alternatives (affiliate) |
| Google Local Services Ads (pay per verified call) | ~A$15–60 a lead (estimates, no official AU price) | https://light-leads.pages.dev/post/the-2026-guide-to-google-ads-and-local-service-ads-for-australian-tradies |
| ServiceSeeking, Oneflare | A$5–50 a quote credit | tradiescaler (above) |
| Airtasker | ~15–20% commission | tradiescaler (above) |
| Tradie website that "ranks locally" | A$30 a month flat (vendor claim) | https://sitenest.pages.dev/blog/hipages-alternatives-for-tradies |
| ServiceM8 (booking forms, job app) | A$0–349 a month | https://www.capterra.com.au/reviews/110711/servicem8 |
| Agency care plans | A$297–997 a month | search result, unverified domain |

Against, worth noting: at least five new `pages.dev` sites (TradesPro, Tradie Scaler, SiteNest, TradieKit,
Light Leads) already sell tradie websites, lead comparisons and hipages alternatives. Solo builders are
already crowding this exact pitch.

## Why it fails, in one line each

- **Gate 2 (narrow):** 1 person, 1 site.
- **Unserved job vs vendor complaint:** the items want hipages cheaper and honest, not a different tool.
- **Hard limit 4 and ACL:** a v1 can be built in 8 weeks, but its promise (jobs) depends on Google
  rankings, not the software. Claiming it would be hard to back up.
- **Compared to what:** free Google profile, word of mouth and A$5–60 alternatives already exist.
