# 00 — The bar (Step 1)

Set 2026-10-27. Step 4 and Gate 7 judge every candidate against this file.

## 1.2 Income target

| Item | A$/month | Note |
|---|---|---|
| Take-home target | **1,905** | 20,000,000 IDR at planning rate 1 AUD = 10,500 IDR |
| Hosting + database (Sydney region) | 70 | Vercel Pro + Neon paid tier; medium confidence |
| Email, error monitoring, helpdesk | 40 | starter tiers; low confidence |
| Domain, misc | 5 | |
| Indonesian accountant (annual SPT, amortised) | 25 | low confidence |
| Platform API (e.g. Xero) | 35–245 | Xero Core A$35 (≤50 connections), Plus A$245 (≤1,000) [R, 1] |
| Payment / merchant of record | 5% + ~A$0.76 per charge | Paddle 5% + US$0.50, incl. GST collection [S, 2] |
| Indonesian income tax | 0.5% of gross (budgeted) | PPh final 0.5% for individuals ≤ Rp4.8bn turnover, no time limit; first Rp500m/yr effectively 0% [R, 3] |

**Monthly revenue target: A$2,500 ex-GST (A$30k/yr).** The default holds: at every price below, the
revenue needed after all costs is A$2,200–2,565, so A$2,500 is the round planning number.

**Exchange rate check:** the actual rate is about 12,500–12,600 IDR per AUD (July–Sept 2026
snapshots [R/S, 4]), ~19% above the planning rate. That is a cushion, not a problem: at today's
rate A$2,500 is ~31m IDR gross. Keep 10,500 as the cautious rate.

**Flags (low confidence, accountant check before taking money):** whether foreign-source SaaS
income qualifies for the 0.5% final regime; whether an Australian GST registration is needed if
not using a merchant of record (Step 9.2).

## 1.3 Customer maths

Customers needed to clear A$1,905 take-home after the costs above. Xero tier switches to Plus
(A$245) above 50 connections. "Reach needed" = customers ÷ 5% (the 1.4 limit).

| Price A$/mo | Fees as % of price | Customers needed | Revenue | Reachable buyers needed (5%) |
|---|---|---|---|---|
| 15 | 10.1% | 171 | 2,565 | ~3,400 |
| 25 | 8.0% | 101 | 2,525 | ~2,000 |
| 50 | 6.5% | 45 | 2,250 | ~900 |
| 100 | 5.8% | 23 | 2,300 | ~460 |
| 200 | 5.4% | 12 | 2,400 | ~240 |

Read-off: below A$25 the fixed per-charge fee and the Xero Plus tier bite, and you need 100+
customers sold remotely. A$50–100 is the sweet spot for a solo founder: 25–45 customers.

## 1.4 Hard limits (Step 4 filter; each is pass/fail/unknown)

1. Sold and supported fully online from Indonesia (no site visits, no phone-heavy onboarding).
2. No licence or government accreditation needed for v1.
3. The problem recurs at least quarterly.
4. v1 buildable solo in about 8 weeks.
5. Needs no more than ~5% of the buyers I can reach (see last column above).

Step 4 adds: no regulated-service problem; data can be hosted in Australia; the main platform
allows the integration and its API cost fits the price.

## 1.5 Time limit

**12 months** until income must hit the bar (from 2026-10-27, so by ~2027-10).
Rough budget: research + smoke test ~5 weeks, build ~8 weeks → launch ~2027-02, leaving
~8 months to reach 25–45 customers (≈3–6 new paying customers a month at A$50–100).
Implication: favour problems where buyers already search for or pay for a tool, so sales can
start without a long education cycle.

## Sources
1. Xero developer pricing (official), checked 2026-10-27: https://developer.xero.com/pricing and https://developer.xero.com/faq/pricing-and-policy-updates
2. Paddle 5% + 50c, third-party (competitor) article, Mar 2026: https://dodopayments.com/blogs/paddle-fees-explained — confirm on paddle.com
3. DJP article on PP 20/2026 (in force 22 Apr 2026): https://pajak.go.id/id/artikel/pp-202026-tarif-pph-05-bagi-umkm-orang-pribadi-berlaku-selamanya ; Rp500m threshold: https://ikpi.or.id/maman-tegaskan-pajak-umkm-tak-naik-meski-ada-aturan-baru/
4. OFX AUD/IDR (15 Jul 2026, 12,567): https://www.ofx.com/en-us/exchange-rates/aud-to-idr/ ; longforecast (13 Sep 2026, 12,628): https://longforecast.com/aud-idr
