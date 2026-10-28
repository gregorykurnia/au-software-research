# 01 — Segments and sources (Step 2.1)

Checked 2026-10-27. "Loads" means a plain automated fetch returned readable posts or reviews.
Collection window for 2.2: items dated on or after **2023-10-27**, plus older requests that are
still active.

## Proposed segments

| # | Segment | Buyer | Why it fits | Automated data | Flags |
|---|---|---|---|---|---|
| **A** | Xero/MYOB ecosystem (default) | bookkeepers, BAS agents, small business owners | richest public buyer data; buyers install add-ons from an app store, so a remote seller can reach them | **High** | BAS/tax-agent work is regulated: a tool for the agent only |
| **B** | Trades and home services | owners of electrical, plumbing, building and cleaning firms (1–20 staff) | admin-heavy (quotes, invoices, jobs, compliance paperwork); buy apps online; AU/NZ-made tools dominate | **Medium–high** | crowded job-management market |
| **C** | NDIS and allied health providers | small NDIS providers, sole-trader therapists, support coordinators | very admin-heavy (claims, price-guide changes, service agreements) | **Low**: most buyer talk is in Facebook groups and Reddit, both manual | disability/health data (privacy, AU hosting); plan management is an NDIS service, so the product stays a tool; NDIS rules change often (recency check) |
| **D** | Australian e-commerce sellers | Shopify and marketplace sellers | online by definition; used to buying apps; app stores give a remote seller distribution | **Medium** | global competitors; the AU angle must be specific (AusPost, GST, Xero sync) |
| E | *Reserve:* hospitality and retail employers | café, restaurant and shop owners | award wages, rosters, Payday Super (from 1 Jul 2026) | Medium; app reviews are mostly from staff, not owners | swap in if a segment above comes up empty |

**Approved 2026-10-27: A, B and D.** C dropped for now (thin automated data); E stays the reserve.

## Sources that load (2.2 subagents use these)

| Source | Segments | How (URL pattern) | Check result | Caveats |
|---|---|---|---|---|
| Xero Product Ideas | A (+ B, D via invoicing, inventory) | `productideas.xero.com/forums/{id}-{slug}/filters/top` | ✓ 13 boards, e.g. Invoices & quotes 1,031 ideas, Reports & tax 905; vote counts and statuses shown | List pages have no dates. Statuses seen: In development, Accepted, Completed, **Not in pipeline** (Xero's "declined") |
| Xero App Store reviews | A, B, C, D, E | `apps.xero.com/au/app/{slug}/reviews?rating=1&page=N` | ✓ dates in page data; rating filter and paging work (6 per page) | Reviewer country isn't shown |
| Apple App Store, AU reviews | A, B, C, E | `itunes.apple.com/au/rss/customerreviews/page={1-10}/id={id}/sortBy=mostRecent/json` | ✓ 50 per page with date, stars and text; Australian store only | Newest 500 only. Many reviewers are staff or field workers, not the buyer, so record the role only when it's stated |
| Trustpilot | A, B, D, E | `trustpilot.com/review/{domain}` | ✓ MYOB: 560 reviews, 1.3★; reviewer country shown | Keep AU reviewers only; skews to billing and support complaints |
| Shopify App Store reviews | D | `apps.shopify.com/{slug}/reviews?ratings[]=1&ratings[]=2` | ✓ Starshipit review page loads (other guessed slugs 404) | Check in 2.2 that the star filter applies and that store country is shown |
| ATO Community | A | `community.ato.gov.au` | ~ landing page shows question titles only; bodies need a JavaScript browser (not installed here) | Low priority; mostly individual taxpayers |
| QuickBooks AU Community | A | `quickbooks.intuit.com/learn-support/.../business-discussions-au` | ~ loads, but top posts are 1–2 years old | Dropped: too quiet |

### Apps to mine per segment (verified ids and review counts)

- **A:** Xero App Store: Dext (1,118 reviews), Hubdoc (232). Apple AU: Xero (id 441880705, 46,101 ratings),
  MYOB Team (1454466288, 221). Trustpilot: xero.com, myob.com. Automated MYOB data is thin; see manual list.
- **B:** Xero App Store: ServiceM8 (351), Tradify (187), Fergus (79), simPRO (69), AroFlo (17). Apple AU:
  ServiceM8 (378062736, 5,575), Tradify (984378901, 4,108), Fergus Go (1484018778, 564), AroFlo (6450022414, 98),
  hipages for business (1531412737, 872: tradies on lead costs). No public feature boards: ServiceM8's
  "Feature Wishes" is in-app only; none found for Tradify or Fergus.
- **C:** Xero App Store: ShiftCare (73), Splose (9). Apple AU: ShiftCare (1252971579, 18,411, mostly support
  workers), Brevity (1407670897, 11). Cliniko: no Xero App Store page or iOS app found. No public feature boards found.
- **D:** Xero App Store: A2X (949), Cin7 Core (223). Shopify App Store: Starshipit plus AU shipping and
  accounting apps, picked in 2.2.
- **E (reserve):** Xero App Store: Deputy (148), Employment Hero (20). Apple AU: Deputy (477070330, 8,247).

## Blocked from the server: Claude in Chrome on your Mac, or by hand

All of these returned HTTP 403 or refused the fetch tool on 2026-10-27. A plain headless browser on the
server was blocked too (bot verification on ProductReview, Capterra, Whirlpool, myob.lithium.com, G2 and
even the ATO). Rule since 2026-10-27 (`CLAUDE.md`): public pages go through **Claude in Chrome on your Mac**,
slowly; Facebook stays **by hand**.

| # | Source | Segments | Route | What to collect |
|---|---|---|---|---|
| 1 | **Facebook groups** | A, B, D | by hand, 45–60 min | Join 1–2 per segment: Australian, 1,000+ members, posts in the last week. Read only. Search terms: A "bookkeepers Australia", "BAS agents"; B "tradies business Australia" (one known: Lifestyle Tradie's "Kick-Ass Tradies"); D "Shopify Australia", "Australian online sellers". Copy posts that complain, ask for a tool or describe a workaround |
| 2 | **Reddit** | A, D | Chrome | r/AusFinance, r/smallbusiness (AU posts), r/bookkeeping, r/shopify: "Xero", "MYOB", "BAS", "invoice", "shipping" |
| 3 | **MYOB Idea Exchange** | A | Chrome | Top 30 ideas by votes: title, votes, status ("Not Likely" = declined). The community moved to `myob.lithium.com` |
| 4 | **ProductReview.com.au** | A, B | Chrome | 1–3★ reviews of Xero, MYOB and any listed job-management app |
| 5 | Whirlpool (Business & Finance) | A | Chrome, optional | |
| — | Capterra AU, G2 | A, B, D | Chrome, only if the above come up thin | US-skewed |

**Chrome results, 2026-10-27** (files in `research/manual/`):
- MYOB Idea Exchange: ✓ now on `community.myob.com`. Business top 30 with comments, plus AccountRight top 30 as a
  list (74 excerpts).
- ProductReview: ✓ Xero, MYOB, hipages (trade side), Shopify and Sendle (seller side), 119 excerpts. ServiceM8,
  Tradify, Fergus, simPRO and AroFlo are not listed there.
- Whirlpool: ✓ but thin. No business forum; 4 threads read (13 excerpts).
- Reddit: ✗ the Chrome extension refuses reddit.com outright. Do it by hand or skip it (see `manual/reddit.md`).

**How to hand it over:** Chrome sessions and your Facebook copies both go into `research/manual/<source>.md`
(text, link, date; any format), pushed to GitHub. Claude cuts excerpts to under 25 words and strips names
and contact details when merging them into the ledger in 2.2.

## Update 2026-10-28: trades widening (approved)

Why: 97% of the ledger came from reviews and idea boards, which surface platform gaps that Xero and MYOB
close. These sources look for trades jobs done **without software** and the money behind them. Segment B
only. Approved by the owner 2026-10-28; Facebook dropped for now.

| # | Source | Route | What to collect | Tag |
|---|---|---|---|---|
| T1 | **Seek job ads** for admin roles at AU trades businesses (e.g. "admin plumbing", "office manager electrical", "trades administrator") | Chrome on the Mac; public ads only; a few dozen pages | The manual tasks listed (chasing certificates, timesheets, job booking, quoting, compliance paperwork). Business-posted ads only, not recruiters | B1 when the business pays a person for the task (staff spend); note pay if shown |
| T2 | **Etsy spreadsheet templates** for trades (job tracker, quote, invoice, compliance log) | Chrome on the Mac; listings and their reviews | Sales or review counts, price, AU relevance, buyer reviews naming the job | Sales of a template for the job = B1; review text = B2 |
| T3 | **Search-result snippets that index Reddit** (AU trades and small-business threads) | Normal web search from the server, no visits to reddit.com | Snippets with "spreadsheet", "Excel", "manually", "how do you handle", "hipages" | B2 (B1 if time or money stated) |

Output: `research/manual/seek.md`, `manual/etsy.md`, `collect/reddit-snippets.md`, then merged into the ledger
by `tools/build_ledger.py` and recoded (2.3) for segment B.

## Notes for 2.2

- Rough yield, low confidence: A 100+ items automated, B 60–80, D 40–60, C under 30 without Facebook.
- Collect 1–3★ reviews and feature requests only. Volume: at most about 10 pages per app per source.
- Xero ideas: take dates from each idea page's latest comment, since list pages have none (to verify in 2.2).
- Every row needs a stated role or business type, or the role column stays blank. Staff reviews can stay but count as weaker evidence.

## Sources checked
Xero Product Ideas https://productideas.xero.com/forums/967115-invoices-quotes/filters/top ·
Xero App Store https://apps.xero.com/au/app/servicem8/reviews ·
Apple AU feed https://itunes.apple.com/au/rss/customerreviews/page=1/id=984378901/sortBy=mostRecent/json ·
Trustpilot https://www.trustpilot.com/review/myob.com ·
Shopify https://apps.shopify.com/starshipit/reviews ·
ATO Community https://community.ato.gov.au/ ·
QuickBooks AU https://quickbooks.intuit.com/learn-support/business-discussions/misc/03/business-discussions-au ·
MYOB Idea Exchange (via search) https://myob.lithium.com/discussions/welcome/announcing-changes-to-our-ideas-exchange/881081 ·
ServiceM8 Feature Wishes https://www.servicem8.com/updates/feature-wish-list ·
Kick-Ass Tradies group (S, mentioned by its host) https://www.lifestyletradie.com.au/?p=766 ·
Blocked (403 / refused): community.myob.com, myob.lithium.com, capterra.com.au, getapp.com.au,
softwareadvice.com.au, g2.com, productreview.com.au, forums.whirlpool.net.au, reddit.com, community.shopify.com.

### Brief for the Mac session (T1, T2), written 2026-10-28

Open Claude Code on the Mac in this repo (pull first), with Claude in Chrome on. Say: "run T1 and T2 from
`research/01-sources.md`". Go slowly, a few dozen pages per source, public pages only, no logins. Push when
done. Excerpts under 25 words, no names or contact details.

**T1 Seek → `research/manual/seek.md`.** Search, Australia-wide, last 30 days: "trades administrator",
"admin plumbing", "office manager electrical", "admin assistant builder", "office administrator
construction", "service coordinator HVAC", "scheduler plumbing". Keep ads posted by the business itself
(skip recruiters and labour hire). Aim for 30–50 ads. One table:

| id | date | url | business type, staff if stated | role | duties excerpt | type | pay | tools named |
|---|---|---|---|---|---|---|---|---|
| SK-01 | 2026-10-20 | https://www.seek.com.au/job/… | plumbing, 12 staff | trades admin | "chase compliance certificates, enter timesheets, …" | B1 | A$60–65k | ServiceM8, Xero |

Every business-posted ad is B1 (the business pays a person to do these tasks). Add a line under the table
with the count of ads seen vs kept, and the 5 most common duties.

**T2 Etsy → `research/manual/etsy.md`.** Search: "tradie job tracker spreadsheet", "construction job
costing spreadsheet", "plumber invoice template", "electrician quote template", "progress claim template",
"SWMS template Australia", "tradie business spreadsheet". For the top 10–15 relevant listings record the
listing; for listings with reviews, up to 5 reviews that name the job. Two tables:

| id | url | title (short) | price | listing reviews | shop sales | AU relevance |
|---|---|---|---|---|---|---|
| ET-01 | https://www.etsy.com/au/listing/… | Tradie job tracker | A$24 | 38 | 2,100 | mentions GST, ABN |

| id | date | listing id | buyer role if stated | excerpt | type |
|---|---|---|---|---|---|
| ET-R01 | 2026-05-02 | ET-01 | electrician | "finally stopped losing track of which jobs were invoiced" | B2 |

A listing with reviews counts as B1 (people paid for a tool for this job); shop-level sales alone are
weaker (note it). Review text is B2, or B1 if it states time or money.
