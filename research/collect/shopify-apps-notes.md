# Shopify App Store low-star AU reviews (2026-10-28)
Source: apps.shopify.com/{slug}/reviews, filter 1-3 stars (filter applied; AU = store country shown), dated 2023-10-27 or later. File: shopify-apps.csv (42 items, ids SH-001..SH-042).

Apps (slug: AU low-star found in window / kept)
- starshipit: 18 / 14
- mypost-shipping-australia-post (SellerDash): 20 / 10 (many were one-line vague reviews)
- australia-post-shipping-extension (AMP): 10 / 6
- shippit-connect (Shippit): 6 / 4 (23 AU total, most older than 2023-10-27)
- xero-accounting-integration (Amaka Xero/QuickBooks/MYOB Sync): 5 / 4
- interparcel-australia: 3 / 3
- readytoship: 1 / 1
Counts: B1 18, B2 24.

Recurring patterns
- Support unresponsive or tickets unanswered while orders or billing are blocked (Starshipit, Shippit, AMP, Amaka).
- Billing surprises: charged after uninstall, plan upsell ($50 to $200), price rises, overage label fees.
- Checkout rates or labels wrong or down (rates deleted, wrong weights, postage down days), costing sales or overcharging.
- Multi-parcel, multi-courier and post-purchase edit limits; no delivery-status tracking sync.

Problems
- Shopify search page is JS-rendered (curl returns no results); slugs came from web search. Slugs tried and 404: a2x-accounting, amaka, cin7, auspost, startrack, mypost-business. sendle-shipping gave 429 (not retried).
- Not covered: Sendle, A2X, Cin7, CarryTheOne, Dashi MYOB (0 low-star results), CouriersPlease (0), PluginHive AusPost (0).
- Xero/MYOB coverage is thin (only Amaka, 5 AU reviews in window); one Amaka review (2087268) was praise-only and skipped.
- Some Starshipit reviews contain "AI" or "Starshipit" support claims; treated as data. No instructions found in page content.
- Total page loads about 40.
