"""Step 2.3: code every ledger item into themes and count them.

Run from the repo root: python3 research/tools/code_themes.py
Writes research/02-coding.csv (id, codes, complaint_type) and prints the count tables used in
research/02-themes.md. The coding below is Claude's judgement, item by item (2026-10-28).
"""
import csv
import re
from collections import Counter, defaultdict

LEDGER = "research/02-complaints.csv"
OUT = "research/02-coding.csv"

# code -> (tag, definition). U = unserved job, V = vendor complaint, M = market signal (neither).
FRAME = {
    "J-PAYSUPER": ("U", "Paying super under Payday Super: choosing the payment date, receipts, clearing old or "
                        "duplicate payments, approval reminders"),
    "J-PAYROLL":  ("U", "Other payroll admin: payslip adjustments, approvers, staff lists and rates, old pay items, "
                        "pay-run setup"),
    "J-INVDOC":   ("U", "Invoice content and delivery: attachments, per-invoice addresses, service dates, hidden "
                        "lines, bank details per invoice, packing slips"),
    "J-ARCHASE":  ("U", "Getting paid: auto statements, ageing, late interest, receipts, quote follow-ups, payment "
                        "behaviour reports, bad-debt write-off"),
    "J-AP":       ("U", "Bills and paying suppliers: default terms, disputed bills, credits in batch payments, "
                        "paying from the ledger, bill data capture"),
    "J-RECON":    ("U", "Bank feeds and reconciliation: auto-match errors, bulk posting, statement conversion, "
                        "bank rules, out-of-sync balances"),
    "J-JOBCOST":  ("U", "Project and job costing for trades: deposits and progress invoices, quote-to-project, "
                        "staff cost rates, project spreadsheets"),
    "J-INVENTORY": ("U", "Stock control inside or beside the ledger: kits, reorder alerts, receiving, landed cost, "
                         "price levels, duplicate items, stock counts"),
    "J-SHIPOPS":  ("U", "E-commerce dispatch workflow: order edits, multi-parcel orders, two couriers, tracking "
                        "status, paying the carrier, 3PL"),
    "J-SHIPCOST": ("U", "Carrier charges that are wrong or unchecked: overcharged rates, surcharges, double "
                        "charges, unread weekly bills"),
    "J-MULTI":    ("U", "Several entities or clients: consolidation, repeated contact changes, per-entity export, "
                        "user access, practice worksheets"),
    "J-AUDIT":    ("U", "Checking other people's entries: audit trail, compulsory fields, working papers attached "
                        "to journals"),
    "J-RECORDS":  ("U", "Keeping or exporting records after leaving, selling or restructuring, without a full "
                        "subscription"),
    "J-ASSETS":   ("U", "Fixed asset register missing from MYOB Business"),
    "J-COMPLY":   ("U", "Tax and compliance obligations outside the ledger: payroll tax on contractors, GST "
                        "registration, government portals"),
    "N-NARROW":   ("V", "Wants a cheaper, narrower or simpler product than the full plan (vendor complaint that "
                        "names a group)"),
    "V-PRICE":    ("V", "Price rises, plan restructures, paying for features not used, costly add-ons"),
    "V-BILLING":  ("V", "Billing errors, charged after cancelling, hard cancellation, lock-in contracts, exit fees"),
    "V-SUPPORT":  ("V", "Slow, unhelpful or missing support"),
    "V-RELIAB":   ("V", "Bugs, outages, broken integrations or sync, data loss, carrier delivery failures"),
    "V-UX":       ("V", "Forced product changes and UI regressions: new layouts, removed features, AI auto-match, "
                        "forced online"),
    "V-FIELDAPP": ("V", "Missing features in one trade field app that rivals have (Android, offline, navigation, "
                        "MMS)"),
    "V-LEADS":    ("V", "Lead marketplace (hipages): lead price, lead quality, expiring credits, contracts"),
    "M-AGAINST":  ("M", "Evidence against building: price resistance to new tools, no felt pain, status quo wins, "
                        "accountant lock-in"),
}

# id -> (codes, complaint type). Types: bug, confusion, missing, expectation, price, service, none.
C = {}


def code(ids, codes, ctype):
    for i in ids.split():
        assert i not in C, i
        C[i] = (codes.split(), ctype)


def rng(prefix, a, b, width=2):
    return " ".join(f"{prefix}-{n:0{width}d}" for n in range(a, b + 1))


# --- MYOB Idea Exchange ---
code(rng("MI", 1, 11), "J-PAYSUPER", "missing")
code("MI-12 MI-13", "J-AUDIT", "missing")
code("MI-14 MI-16", "J-AP", "missing")
code("MI-15", "J-AP V-PRICE", "missing")
code("MI-17 MI-18", "J-INVDOC", "missing")
code("MI-19", "V-UX", "expectation")
code("MI-20", "V-PRICE V-UX", "price")
code("MI-21 MI-22", "J-INVDOC V-UX", "missing")
code("MI-23 MI-24", "J-ASSETS", "missing")
code("MI-25 MI-26 MI-27 MI-28", "V-UX", "expectation")
code("MI-29 MI-30", "J-ARCHASE", "missing")
code("MI-31 MI-33", "J-INVDOC", "missing")
code("MI-32", "J-INVDOC J-ARCHASE", "missing")
code("MI-34 MI-35", "V-UX", "expectation")
code("MI-36 MI-37", "J-INVDOC", "missing")
code("MI-38", "V-UX", "expectation")
code("MI-39 MI-40", "J-PAYROLL", "missing")
code("MI-41 MI-42", "J-AUDIT", "missing")
code("MI-43", "J-PAYROLL V-UX", "expectation")
code("MI-44 MI-45", "V-UX", "expectation")
code("MI-46", "V-UX J-RECON", "expectation")
code("MI-47 MI-48", "V-UX J-RECON", "expectation")
code("MI-49 MI-50", "J-INVDOC V-UX", "missing")
code("MI-51 MI-52", "J-PAYROLL", "missing")
code("MI-53 MI-54", "V-UX", "expectation")
code("MI-55 MI-56", "J-INVDOC J-SHIPOPS", "missing")
code("MI-57 MI-58 MI-59", "V-UX J-RECON", "expectation")
code("MI-60 MI-61", "J-PAYSUPER", "missing")
code("MI-62 MI-63 MI-64", "J-RECORDS", "missing")
code("MI-65", "J-AP", "missing")
code("MI-66 MI-68", "J-INVDOC", "missing")
code("MI-67", "J-INVDOC J-MULTI", "missing")
code("MI-69 MI-70", "J-PAYROLL", "missing")
code("MI-71 MI-72 MI-73 MI-74", "J-INVDOC", "missing")

# --- ProductReview: Xero ---
code("PR-X01", "J-INVDOC V-UX", "expectation")
code("PR-X02", "J-PAYROLL V-RELIAB", "bug")
code("PR-X03 PR-X04 PR-X08", "J-AP", "missing")
code("PR-X05", "J-RECON V-RELIAB", "bug")
code("PR-X06", "V-UX", "expectation")
code("PR-X07", "J-JOBCOST", "missing")
code("PR-X09", "J-PAYROLL V-PRICE", "price")
code("PR-X10", "V-PRICE", "price")
code("PR-X11", "V-PRICE", "price")
code("PR-X12", "J-INVENTORY", "missing")
code("PR-X13 PR-X14", "V-PRICE", "price")
code("PR-X15", "V-RELIAB", "expectation")
code("PR-X16", "V-PRICE", "price")
code("PR-X17", "J-JOBCOST", "missing")
code("PR-X18", "V-PRICE V-UX", "price")
code("PR-X19", "J-PAYSUPER", "expectation")
code("PR-X20", "J-RECORDS J-MULTI", "missing")
code("PR-X21", "J-RECON V-RELIAB", "bug")
code("PR-X22", "M-AGAINST", "none")
code("PR-X23", "V-PRICE N-NARROW", "price")
code("PR-X24", "M-AGAINST", "none")
code("PR-X25", "V-PRICE", "price")
code("PR-X26", "V-RELIAB V-SUPPORT", "bug")
code("PR-X27", "V-BILLING", "service")
code("PR-X28", "J-JOBCOST V-RELIAB", "bug")
code("PR-X29", "V-PRICE", "price")
code("PR-X30", "J-RECON V-RELIAB", "bug")
code("PR-X31", "V-SUPPORT", "service")
code("PR-X32", "J-MULTI", "missing")
code("PR-X33 PR-X34", "J-PAYROLL", "confusion")
code("PR-X35", "V-PRICE N-NARROW", "price")
code("PR-X36", "J-RECORDS", "missing")
code("PR-X37", "J-ARCHASE", "missing")
code("PR-X38 PR-X39", "J-INVENTORY", "missing")
code("PR-X40", "J-INVENTORY V-RELIAB", "bug")
code("PR-X41", "M-AGAINST N-NARROW", "none")
code("PR-X42", "J-RECON V-RELIAB", "bug")
code("PR-X43", "N-NARROW", "expectation")
code("PR-X44", "J-INVDOC", "missing")
code("PR-X45 PR-X46", "V-PRICE", "price")
code("PR-X47 PR-X48", "V-PRICE N-NARROW J-PAYROLL", "price")

# --- ProductReview: MYOB ---
code("PR-M01 PR-M03 PR-M07 PR-M11 PR-M14 PR-M22 PR-M31", "V-BILLING", "service")
code("PR-M02", "V-BILLING V-SUPPORT", "service")
code("PR-M04 PR-M08 PR-M09 PR-M12 PR-M13 PR-M15 PR-M23 PR-M30 PR-M35", "V-SUPPORT", "service")
code("PR-M05 PR-M06", "V-UX", "confusion")
code("PR-M10", "V-UX", "missing")
code("PR-M16", "V-BILLING", "service")
code("PR-M17", "V-RELIAB V-SUPPORT", "bug")
code("PR-M18 PR-M32", "V-UX V-PRICE", "expectation")
code("PR-M19", "J-INVDOC V-RELIAB", "bug")
code("PR-M20 PR-M33", "J-RECON V-RELIAB", "bug")
code("PR-M21 PR-M40", "J-RECORDS", "price")
code("PR-M24", "V-RELIAB", "bug")
code("PR-M25", "J-PAYSUPER J-PAYROLL", "confusion")
code("PR-M26", "N-NARROW", "price")
code("PR-M27", "V-BILLING", "service")
code("PR-M28", "V-SUPPORT", "service")
code("PR-M29", "V-UX", "expectation")
code("PR-M34", "V-UX", "expectation")
code("PR-M36", "V-PRICE", "price")
code("PR-M37", "V-UX", "expectation")
code("PR-M38", "J-AP V-RELIAB", "bug")
code("PR-M39", "V-UX", "expectation")

# --- ProductReview: hipages, Sendle, Shopify ---
code("PR-H01 PR-H05 PR-H11 PR-H12 PR-H19", "V-LEADS V-BILLING", "expectation")
code("PR-H02", "V-LEADS V-SUPPORT", "service")
code("PR-H03 PR-H04 PR-H06 PR-H07 PR-H08 PR-H10 PR-H13 PR-H14 PR-H15 PR-H16 PR-H17 PR-H18 PR-H21 PR-H22",
     "V-LEADS", "price")
code("PR-H09", "V-LEADS V-BILLING", "service")
code("PR-H20", "V-LEADS M-AGAINST", "none")
code("PR-S01 PR-S02", "V-SUPPORT", "service")
code("PR-S03", "V-BILLING", "service")
code("PR-S04", "V-SUPPORT", "service")
code("PR-D01 PR-D03", "V-RELIAB", "service")
code("PR-D02 PR-D05", "V-RELIAB", "expectation")
code("PR-D04", "J-SHIPCOST", "missing")

# --- Whirlpool ---
code("WP-01 WP-02 WP-03", "J-COMPLY", "missing")
code("WP-04 WP-06 WP-07 WP-08 WP-09", "M-AGAINST", "none")
code("WP-05", "M-AGAINST J-RECON", "none")
code("WP-10", "J-COMPLY", "none")
code("WP-11", "J-COMPLY", "none")
code("WP-12 WP-13", "J-COMPLY", "service")

# --- Apple App Store AU ---
code("AP-001 AP-002 AP-003 AP-004 AP-005 AP-006 AP-007 AP-009 AP-010 AP-011 AP-013", "V-LEADS", "price")
code("AP-008 AP-012 AP-014", "V-LEADS V-BILLING", "service")
code("AP-015 AP-017 AP-018 AP-022 AP-024", "V-RELIAB", "bug")
code("AP-016", "V-RELIAB V-PRICE", "bug")
code("AP-019", "V-RELIAB V-FIELDAPP", "bug")
code("AP-020 AP-021 AP-023 AP-025 AP-026", "V-FIELDAPP", "missing")
code("AP-027", "V-PRICE J-ARCHASE", "price")
code("AP-028", "J-INVENTORY V-RELIAB", "bug")
code("AP-029", "V-PRICE J-INVDOC", "price")
code("AP-030", "J-ARCHASE", "missing")
code("AP-031", "V-PRICE", "price")

# --- Shopify App Store ---
code("SH-001 SH-034", "J-SHIPCOST", "bug")
code("SH-002 SH-020", "V-PRICE", "expectation")
code("SH-003 SH-007", "J-SHIPOPS V-RELIAB", "missing")
code("SH-004 SH-035 SH-036 SH-037", "V-PRICE", "price")
code("SH-005 SH-006 SH-016 SH-017", "V-BILLING", "service")
code("SH-008 SH-009 SH-012 SH-014 SH-015 SH-018 SH-024 SH-025 SH-026 SH-027 SH-040", "V-RELIAB", "bug")
code("SH-010 SH-029 SH-030 SH-031 SH-033 SH-041", "J-SHIPOPS", "missing")
code("SH-011", "J-SHIPCOST V-BILLING", "bug")
code("SH-013 SH-019 SH-021 SH-023", "V-SUPPORT", "service")
code("SH-022", "V-PRICE", "price")
code("SH-028", "V-RELIAB V-SUPPORT", "bug")
code("SH-032 SH-038", "J-SHIPOPS V-RELIAB", "bug")
code("SH-039", "V-RELIAB", "service")
code("SH-042", "V-RELIAB", "missing")

# --- Trustpilot ---
code("TP-001", "V-RELIAB", "bug")
code("TP-002 TP-004", "V-PRICE", "price")
code("TP-003", "V-FIELDAPP", "missing")
code("TP-005", "V-FIELDAPP", "missing")
code("TP-006", "V-UX", "expectation")
code("TP-007 TP-016 TP-020 TP-024", "V-BILLING", "service")
code("TP-008", "V-SUPPORT", "service")
code("TP-009", "V-RELIAB", "bug")
code("TP-010 TP-011 TP-012 TP-013", "V-LEADS", "price")
code("TP-014", "V-RELIAB", "bug")
code("TP-015", "J-SHIPCOST", "bug")
code("TP-017", "J-SHIPOPS V-SUPPORT", "missing")
code("TP-018", "J-SHIPCOST V-BILLING", "bug")
code("TP-019", "V-SUPPORT", "service")
code("TP-021", "V-BILLING", "service")
code("TP-022", "V-PRICE", "price")
code("TP-023", "J-INVENTORY V-RELIAB", "bug")

# --- Xero App Store ---
code("XA-001 XA-016 XA-030 XA-032", "V-RELIAB J-RECON", "bug")
code("XA-002 XA-011", "V-PRICE", "price")
code("XA-003 XA-010", "V-RELIAB", "bug")
code("XA-004 XA-005 XA-006", "V-FIELDAPP", "missing")
code("XA-007 XA-008 XA-013", "V-FIELDAPP", "missing")
code("XA-009 XA-014", "J-JOBCOST", "missing")
code("XA-012", "J-INVDOC V-FIELDAPP", "missing")
code("XA-015", "V-BILLING", "service")
code("XA-017", "V-RELIAB V-PRICE", "bug")
code("XA-018", "V-PRICE", "price")
code("XA-019", "J-INVENTORY", "missing")
code("XA-020 XA-021 XA-022 XA-023 XA-024 XA-025 XA-026 XA-027", "V-PRICE J-INVENTORY", "price")
code("XA-028", "V-SUPPORT", "service")
code("XA-029", "J-SHIPOPS", "missing")
code("XA-031", "V-PRICE V-SUPPORT", "price")
code("XA-033 XA-034", "J-AP V-RELIAB", "bug")

# --- Xero Product Ideas ---
code("XI-001 XI-002 XI-003 XI-008 XI-017", "J-ARCHASE", "missing")
code("XI-004 XI-005 XI-006 XI-024 XI-020 XI-025", "J-AP", "missing")
code("XI-007 XI-026 XI-028 XI-031", "J-INVDOC", "missing")
code("XI-009", "J-ARCHASE J-RECON", "missing")
code("XI-010 XI-011 XI-012", "J-PAYROLL", "missing")
code("XI-013", "J-PAYSUPER", "missing")
code("XI-014 XI-018 XI-019 XI-023", "J-RECON", "missing")
code("XI-015", "J-AUDIT", "missing")
code("XI-016 XI-021 XI-022", "J-MULTI", "missing")
code("XI-027", "J-MULTI J-AUDIT", "missing")
code("XI-029", "J-ARCHASE J-JOBCOST", "missing")
code("XI-030 XI-032 XI-033 XI-034 XI-035 XI-036", "J-JOBCOST", "missing")
code(rng("XI", 37, 44, 3), "J-INVENTORY", "missing")

# Items that mention cancelling or moving to an alternative (skill step 4); judged from the excerpt.
SWITCH = ("MI-35 MI-38 MI-45 PR-X09 PR-X16 PR-X24 PR-M10 PR-M20 PR-M39 PR-S03 PR-D03 AP-008 AP-013 TP-003 "
          "XA-020 XA-022 XA-024 XA-025 XA-031 SH-006 SH-016 PR-M11 PR-H01 PR-H05").split()


def main():
    rows = list(csv.DictReader(open(LEDGER)))
    ids = [r["id"] for r in rows]
    missing = [i for i in ids if i not in C]
    extra = [i for i in C if i not in ids]
    assert not missing and not extra, (missing, extra)
    for i, (codes, _) in C.items():
        assert 1 <= len(codes) <= 3 and all(c in FRAME for c in codes), i

    words = {r["id"]: len(re.findall(r"\w+", r["excerpt"])) for r in rows}
    total_words = sum(words.values())
    by = {r["id"]: r for r in rows}
    n = len(rows)

    with open(OUT, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["id", "codes", "complaint_type"])
        for i in ids:
            w.writerow([i, " ".join(C[i][0]), C[i][1]])

    items = defaultdict(list)
    for i in ids:
        for c in C[i][0]:
            items[c].append(i)

    def src_family(s):
        s = s.split(":")[0].strip()
        return s

    print(f"N items {n}; total excerpt words {total_words}\n")
    print("| Code | Tag | Items | % items | % text | B1 | B2 | Sources | Source names | Segments | "
          "Workaround stated | Votes (max idea) | Loud? |")
    print("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    order = sorted(FRAME, key=lambda c: (FRAME[c][0] != "U", -len(items[c])))
    for c in order:
        its = items[c]
        k = len(its)
        si = k / n
        st = sum(words[i] for i in its) / total_words
        b1 = sum(by[i]["type"] == "B1" for i in its)
        srcs = Counter(src_family(by[i]["source"]) for i in its)
        segs = Counter(s.strip() for i in its for s in by[i]["segment"].split(","))
        wa = sum(bool(by[i]["workaround"].strip()) for i in its)
        votes = [int(m.group(1).replace(",", "")) for i in its
                 for m in [re.match(r"([\d,]+) votes", by[i]["votes_or_likes"])] if m]
        loud = "LOUD" if k >= 2 and st > 2 * si and st >= 0.10 else ""
        print(f"| {c} | {FRAME[c][0]} | {k} | {round(si*100)}% | {round(st*100)}% | {b1} | {k-b1} | {len(srcs)} | "
              f"{', '.join(f'{s} {v}' for s, v in srcs.most_common())} | "
              f"{' '.join(f'{s}{v}' for s, v in sorted(segs.items()))} | {wa} | {max(votes) if votes else '-'} | {loud} |")

    print("\nItems per code:")
    for c in order:
        print(c, " ".join(items[c]))

    print("\nComplaint types:", Counter(t for _, t in C.values()).most_common())
    ut = Counter()
    for i, (codes, t) in C.items():
        tags = {FRAME[c][0] for c in codes}
        ut["U only" if tags == {"U"} else "V only" if tags == {"V"} else "M only" if tags == {"M"} else
           "mixed"] += 1
    print("Items by tag:", ut.most_common())
    print("\nSegment split (items):", Counter(by[i]["segment"] for i in ids).most_common())
    print("Switching/cancel items:", len(SWITCH), " ".join(SWITCH))
    assert all(s in by for s in SWITCH)


if __name__ == "__main__":
    main()
