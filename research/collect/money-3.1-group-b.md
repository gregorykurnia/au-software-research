# 3.1 Money signals: group B (shipping-charge-errors, dispatch-workflow, bill-capture)
Collected 2026-10-28; all links read that day. Shopify prices are USD unless marked, and AUD figures are not converted.
The Shopify App Store rate-limited (429) late in the run, so the Oh Ship! and SimuShip listings come from search snippets only.
No fetched page contained instructions.

## shipping-charge-errors
| signal | tag | what | link | conf |
|---|---|---|---|---|
| Oh Ship! (Shopify, carrier-adjustment finder) | B1 | 1 review, 5★, 2026-06-30. "found over $4,700 in carrier adjustment charges across our 2025 orders"; "paid for itself many times over". Reviewer country US, but the business name includes "Australia". Paid tier $39/mo (search snippet) | https://apps.shopify.com/oh-ship/reviews | med (n=1; carriers unclear) |
| Starshipit review (already ledger SH-001) | B1 | AU, 2026-07-29: setup made international rates "systematically overcharge for over two full years", "overpay thousands" | https://apps.shopify.com/starshipit/reviews | high |
| SimuShip (Shopify, checkout rate vs carrier cost) | S | Launched 2026-07-27, 0 reviews (search snippet) | https://apps.shopify.com/simuship | low |
| Starshipit Invoice Reconciliation, built in | S | Upload a courier CSV and it compares charges to quotes. Classic UI only. Support article updated 2026-10-03 ("all couriers with tracking no."); changelog says AusPost only. Feature request: 7 votes, Complete | https://support.starshipit.com/articles/11469376267151-invoice-reconciliation · https://feedback.starshipit.com/accounts-admin-billing/p/invoice-reconciliation | high |
| Machship Reconcile; Cario; Smartfreight (AU freight platforms) | S | Line-by-line carrier invoice audit with credit-claim workflow. Machship "from $495/mo" (TrustRadius; currency not stated). Aimed at larger shippers | https://machship.com/product/reconcile · https://cario.com.au/uses/freight-invoice-reconciliation-software | med |
| AU freight-audit consultancy | S | Fixed fee: $4,950 express audit, $5,000+GST diagnostic. No AU contingency-fee parcel auditor found | https://amstrategist-site.pages.dev/ | low |
| ACCC: AusPost/StarTrack remediation | R | ~A$2.9m for wrongly declined lost/damaged claims, 2018–22. These were claims, not billing errors | https://postandparcel.info/154766/news/e-commerce/australia-post-to-pay-estimated-2-9-million-in-compensation-to-business | high |
| Sendle status | R/S | Stopped bookings 2026-01-11; FAST Group wound down. **PR-D04 (Sendle weekly bill) now describes a dead carrier** | https://www.thenewdaily.com.au/finance/consumer/2026/01/12/sendle-shut-down-australia · https://ia.acs.org.au/article/2026/sendle-shuts-down-after-12-years---100m-in-funding.html | high |
| Carrier invoice data | R | AusPost: an "AP Billing Extract" CSV per invoice, downloaded by hand from the Merchant Portal (business credit accounts, since Sep 2023). StarTrack: an emailed "electronic invoice report", once-off or scheduled weekly. No invoice API found for either | https://auspost.com.au/business/business-admin/business-credit-accounts-postage-meters/business-credit-account/billing-and-account-help/invoice/download-ap-billing-extract-invoice-transaction-data · https://auspost.com.au/business/business-admin/business-credit-accounts-postage-meters/business-credit-account/billing-and-account-help/invoice/request-startrack-electronic-invoice-report | med |

**B1 for this job?** Barely. There is one review from a paying user of a carrier-adjustment tool (n=1, not clearly an AU carrier), plus SH-001, which is a loss and not spend on a check.
Against the candidate: Starshipit already ships invoice reconciliation, and Sendle (the source of PR-D04) has closed.
**Price anchor:** about US$39/mo (Oh Ship!). Reconciliation comes bundled in Starshipit at US$35–385/mo. Freight platforms start at about $495/mo, and consultants charge about A$5k per audit.

## dispatch-workflow
| signal | tag | what | link | conf |
|---|---|---|---|---|
| SellerDash: AusPost Shipping | B1 | 680 reviews, 4.7★, newest 2026-10-19, AU reviewers. "has saved me hours a week manually entering addresses". Price $9.99/mo (search snippet) | https://apps.shopify.com/mypost-shipping-australia-post/reviews | high |
| Starshipit (Shopify) | B1 | 210 reviews, 3.9★, newest 2026-10-21, mostly AU. US$35/100/140/385 per month. AU 2026-07-12: order-edit "workarounds are time intensive and error prone" (likely SH-003). NZ 2026-06-02: a split order takes "10 or more minutes" to clear | https://apps.shopify.com/starshipit/reviews?sort_by=newest | high |
| Starshipit (Trustpilot) | B1 | 42 reviews, 4.3. AU 2025-10-31: "saved hours a day of data entry". AU 2025-08-25: addresses didn't update, "which led to paying extra shipping fees" | https://www.trustpilot.com/review/starshipit.com | high |
| Shippit (Shopify) | B1 | 89 reviews, 2.8★, newest 2026-08-18. Lite free, then US$499 and US$1,599/mo. "3 hours one phone to shopify specialist" | https://apps.shopify.com/shippit-connect | high |
| Interparcel AU; Australia Post All In One | S/B2 | 26 reviews 4.5★; 129 reviews 4.9★ (search snippets, not opened) | https://apps.shopify.com/interparcel-australia/reviews · https://apps.shopify.com/australia-post-all-in-one/reviews | med |
| Order-edit apps (EditMyOrder, OrderEditing.com) | S | 15 reviews, 5.0★; OrderEditing $39/mo (third-party directory). Not AU-specific | https://apps.shopify.com/editmyorder | low |

**B1 for this job?** Yes, for dispatch in general: paying AU users report hours saved on re-keying and address entry, and one reports fees paid when edits didn't sync.
The specific gaps (edits after checkout, multi-parcel, two couriers, paying the carrier in the app) have time-cost complaints but no stated dollar figures.
The field is crowded and partly cheap: SellerDash costs about $10/mo.
**Price anchor:** about US$10–140/mo for SMB shipping apps, and up to US$385–1,599/mo at the top.

## bill-capture
| signal | tag | what | link | conf |
|---|---|---|---|---|
| Dext (Xero App Store AU) | B1 | 1,118 reviews, 4.8★; review dates and locations not shown. "is cheaper than paying someone to do the admin" | https://apps.xero.com/au/app/dext-prepare | high |
| Dext (Trustpilot) | B1 | 1,991 reviews, 4.7, newest 2026-10-22. AU 5★: "All for the cost of 1 hrs bookkeeping/month". AU 1★: "incredibly expensive... overcharge you" | https://www.trustpilot.com/review/dext.com | high |
| Dext AU pricing | S | A$33.58/mo ex-GST (annual), 250 docs, 5 users. Line items +A$28.50/mo or A$0.70/doc | https://dext.com/au/pricing/prepare-direct | med (page undated) |
| Hubdoc (by Xero) | B1/S | 232 reviews, 3.3★. **Included in Xero plans** (listing). Trustpilot: 18 reviews, 2.1, mostly GB, retyping complaints ("manually typing the invoices in") | https://apps.xero.com/au/app/hubdoc · https://www.trustpilot.com/review/hubdoc.com | high |
| AutoEntry | B1 | 465 reviews, 4.7★. Price per credit (1 credit per bill, 2 with line items); only GBP prices found (£9–75/mo) | https://apps.xero.com/au/app/autoentry | med |
| Lightyear | B1 | 146 reviews, 4.98★. "saving us loads of time each month". AU page: $155/mo for 125 credits, $255/mo for 250 (currency not shown) | https://apps.xero.com/au/app/lightyear · https://www.lightyear.cloud/pricing | med |
| ApprovalMax Capture | S | Add-on; "from $65" (Capterra snippet, currency unknown) | https://apps.xero.com/au/app/approvalmax | low |
| Outsourced AP / bookkeeping | S | AU bookkeeping including AP: A$600–1,200/mo for 50–200 transactions. Offshore AP: $18–35/hr | https://digit.business/insights/bookkeeping-accounts/outsourced-bookkeeping-cost-australia · https://www.accountingtimes.com.au/profession/accounts-payable-outsourcing-when-it-makes-sense-for-australian-businesses | low |

**B1 for this job?** Yes, buyers clearly pay for bill capture (thousands of reviews, with cost-versus-bookkeeper statements).
But that money goes to the incumbents that already do the job. No B1 shows spend on fixing their misreads, which is this candidate's angle.
Against the candidate: Hubdoc comes free with Xero.
**Price anchor:** A$0 (Hubdoc in Xero), about A$34–62/mo (Dext), about $155–255/mo (Lightyear), or A$0.70–1.24 per document.
