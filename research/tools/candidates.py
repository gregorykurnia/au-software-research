"""Step 2.4: problem candidates and their Gate 2 counts.

Run from the repo root: python3 research/tools/candidates.py
Prints the Gate 2 table used in research/02-candidates.md. Which ids support which candidate is
Claude's judgement (2026-10-28); the counts and checks below are mechanical.

Gate 2: at least 5 buyer items (B1 or B2) from at least 2 independent sources, and not mostly
(more than half) from one page or one person.
- Source = source site (the part of `source` before ":"), so ProductReview Xero, MYOB and Sendle
  count as one site.
- Page = one idea or forum thread, or one product's review listing (query string and paging
  ignored). Stricter than the 2.3 "Top page", which split listings by star filter.
- Person: items are counted per person, not per excerpt. Same person = role "same" (the item
  before it), the same review listing on the same date (one review cut into several excerpts), or
  listed in SAME_PERSON. Idea-board comments can't be matched to people, so the page check covers them.
"""
import csv
from collections import Counter, defaultdict

LEDGER = "research/02-complaints.csv"
REVIEW_SITES = {"ProductReview", "Xero App Store", "Apple App Store AU", "Shopify App Store", "Trustpilot"}
# Same wording one day apart, both about Starshipit: one reviewer posting on two sites.
SAME_PERSON = {"TP-018": "SH-011"}


def rng(prefix, a, b, width=3):
    return " ".join(f"{prefix}-{n:0{width}d}" for n in range(a, b + 1))


# slug -> ids. Order = order of the cards in 02-candidates.md: passes by B1, then B2, then sources
# (the Step 4.2 rule), then fails.
CANDIDATES = {
    "inventory-beside-xero": f"{rng('XA', 19, 27)} AP-028 PR-X12 PR-X38 PR-X39 PR-X40 TP-022 TP-023 "
                             f"{rng('XI', 37, 44)}",
    "shipping-charge-errors": "PR-D04 SH-001 SH-011 SH-034 TP-015 TP-018",
    "payroll-in-ledger": "PR-X02 PR-X33 PR-X34 PR-M25 XI-010 XI-011 XI-012 "
                         "MI-39 MI-40 MI-43 MI-51 MI-52 MI-69 MI-70",
    "getting-paid": "XI-001 AP-027 MI-29 MI-30 MI-32 PR-X37 XI-002 XI-003 XI-008 XI-009 XI-017",
    "job-costing": "PR-X07 PR-X17 PR-X28 XA-009 XA-014 XI-030 XI-032 XI-033 XI-034 XI-035 XI-036",
    "records-after-exit": "MI-62 MI-63 MI-64 PR-M21 PR-M40 PR-X20 PR-X36",
    "entry-review": "MI-12 MI-13 MI-41 MI-42 XI-015 XI-027",
    "invoice-layout": "MI-17 MI-18 MI-21 MI-22 MI-31 MI-32 MI-33 MI-36 MI-37 MI-49 MI-50 MI-66 MI-67 MI-68 "
                      "PR-X01 PR-M19 AP-029 XA-012 XI-007 XI-026 XI-028 XI-031",
    "payday-super": "MI-01 MI-02 MI-03 MI-04 MI-05 MI-06 MI-07 MI-08 MI-09 MI-10 MI-11 MI-60 MI-61 "
                    "PR-X19 PR-M25 XI-013",
    "dispatch-workflow": "SH-003 SH-007 SH-010 SH-029 SH-030 SH-031 SH-032 SH-033 SH-038 SH-041 "
                         "TP-017 XA-029 MI-55 MI-56",
    "supplier-payment-runs": "MI-14 MI-15 MI-16 MI-65 XI-004 XI-005 XI-006 XI-020 XI-024 XI-025",
    "bill-capture": "PR-X03 PR-X04 PR-X08 PR-M38 XA-033 XA-034",
    "ndis-service-dates": "MI-71 MI-72 MI-73 MI-74 PR-X44",
    "payroll-only-plan": "PR-X47 PR-X48 PR-X09 PR-X23",
    "multi-entity-repeat": "XI-016 XI-021 PR-X20 PR-X32",
    "tax-obligations": "WP-01 WP-02 WP-03 WP-10 WP-11 WP-12 WP-13",
    "bank-data-housekeeping": "XI-014 XI-018 XI-019 XI-023",
    "quote-follow-up": "XI-029 AP-030",
    "fixed-assets-myob": "MI-23 MI-24",
}


def site(r):
    return r["source"].split(":")[0].strip()


def page(r):
    return r["source"] if site(r) in REVIEW_SITES else r["url"].split("?")[0].split("#")[0]


def people(rows):
    """id -> id of the first item by the same person."""
    person, first_on, prev = {}, {}, None
    for i, r in rows.items():
        if r["role_as_stated"].lower().startswith("same"):
            person[i] = person[prev]
        elif site(r) in REVIEW_SITES and (r["source"], r["date"]) in first_on:
            person[i] = first_on[(r["source"], r["date"])]
        else:
            person[i] = i
        first_on.setdefault((r["source"], r["date"]), person[i])
        prev = i
    for i, j in SAME_PERSON.items():
        person[i] = person[j]
    return person


def main():
    rows = {r["id"]: r for r in csv.DictReader(open(LEDGER))}
    person = people(rows)

    print("| Slug | People | Same person | B1 | B2 | Sources | Source names | Top page | G2 | Why |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    for slug, ids in CANDIDATES.items():
        ids = ids.split()
        assert len(ids) == len(set(ids)) and all(i in rows for i in ids), slug
        assert all(rows[i]["type"] in ("B1", "B2") for i in ids), slug
        who = defaultdict(list)
        for i in ids:
            who[person[i]].append(i)
        n = len(who)
        b1 = sum(any(rows[i]["type"] == "B1" for i in its) for its in who.values())
        srcs = Counter(site(rows[its[0]]) for its in who.values())
        pages = Counter(page(rows[its[0]]) for its in who.values())
        top = pages.most_common(1)[0][1] / n
        why = []
        if n < 5:
            why.append(f"{n} people < 5")
        if len(srcs) < 2:
            why.append("1 source")
        if top > 0.5:
            why.append(f"{round(top*100)}% one page")
        g2 = "fail" if why else "pass"
        merged = " ".join("=".join(its) for its in who.values() if len(its) > 1)
        print(f"| {slug} | {n} | {merged or '-'} | {b1} | {n-b1} | {len(srcs)} | "
              f"{', '.join(f'{s} {v}' for s, v in srcs.most_common())} | {round(top*100)}% | {g2} | "
              f"{'; '.join(why)} |")


if __name__ == "__main__":
    main()
