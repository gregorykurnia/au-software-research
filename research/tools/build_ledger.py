"""Build research/02-complaints.csv from research/manual/*.md tables and research/collect/*.csv.

Checks every row: excerpt under 25 words (longer ones are cut to 24 + "…" and flagged),
date on or after the cutoff, type B1/B2. Prints a summary. Run from the repo root:
    python3 -I research/tools/build_ledger.py
"""
import csv, glob, re, sys
from collections import Counter

CUTOFF = "2023-10-27"
COLS = ["id", "date", "source", "url", "segment", "role_as_stated", "excerpt", "type",
        "votes_or_likes", "money_signal", "workaround"]
OUT = "research/02-complaints.csv"
flags = []


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def clean(s):
    return s.replace("**", "").strip()


def md_link(s):
    m = re.search(r"\[([^\]]*)\]\(([^)]+)\)", s)
    return (m.group(1), m.group(2)) if m else (s, "")


def myob(path):
    rows, ideas, section = [], {}, ""
    for line in open(path, encoding="utf-8"):
        if line.startswith("## "):
            section = line
        if not line.startswith("|"):
            continue
        c = cells(line)
        if "MYOB Business: top 30" in section and c[0].isdigit():
            title, url = md_link(c[1])
            ideas[c[0]] = (url, f"{c[4]} votes; {c[3]}")
        elif re.match(r"MI-\d+", c[0]):
            url, votes = ideas.get(c[2], ("", ""))
            rows.append(dict(id=c[0], date=c[1], source="MYOB Idea Exchange: MYOB Business", url=url,
                             segment=c[3], role_as_stated=c[4], excerpt=c[5], type=clean(c[6]),
                             votes_or_likes=votes, money_signal=c[7], workaround=c[8] if len(c) > 8 else ""))
    return rows


def productreview(path):
    rows, links, seg, src = [], {}, "", ""
    names = {"Xero": ("A", "xero"), "MYOB": ("A", "myob"), "hipages": ("B", "home-improvement-pages"),
             "Shopify": ("D", "shopify"), "Sendle": ("D", "sendle")}
    for line in open(path, encoding="utf-8"):
        if line.startswith("## "):
            for n, (s, slug) in names.items():
                if line[3:].startswith(n):
                    seg, src = s, n
        if not line.startswith("|"):
            continue
        c = cells(line)
        if c[0] in names and c[1].startswith("http"):
            links[c[0]] = c[1]
        elif re.match(r"PR-[A-Z]+\d+", c[0]):
            rows.append(dict(id=c[0], date=c[1], source=f"ProductReview: {src}", url=links.get(src, ""),
                             segment=seg, role_as_stated=c[3], excerpt=c[4], type=clean(c[5]),
                             votes_or_likes="1–3★", money_signal=c[6] if len(c) > 6 else "", workaround=""))
    return rows


def whirlpool(path):
    rows = []
    for line in open(path, encoding="utf-8"):
        c = cells(line) if line.startswith("|") else []
        if c and re.match(r"WP-\d+", c[0]):
            rows.append(dict(id=c[0], date=c[1], source="Whirlpool", url=f"https://forums.whirlpool.net.au/thread/{c[2]}",
                             segment=c[3], role_as_stated=c[4], excerpt=c[5], type=clean(c[6]),
                             votes_or_likes="", money_signal=c[7] if len(c) > 7 else "", workaround=""))
    return rows


def collected():
    rows = []
    for f in sorted(glob.glob("research/collect/*.csv")):
        with open(f, encoding="utf-8", newline="") as fh:
            rows += [{k: (r.get(k) or "").strip() for k in COLS} for r in csv.DictReader(fh)]
    return rows


def check(r):
    ex = r["excerpt"]
    quoted = ex.startswith('"') or ex.startswith("“")
    if not quoted and not ex.startswith("[summary]") and r["id"][:2] in ("MI", "PR", "WP"):
        r["excerpt"] = "[summary] " + ex
        flags.append(f"{r['id']}: not a quote, marked [summary]")
    words = r["excerpt"].replace("[summary] ", "").split()
    if len(words) >= 25:
        r["excerpt"] = " ".join(words[:24]).rstrip('".,;') + '…"' * quoted
        flags.append(f"{r['id']}: excerpt cut to 24 words")
    if not re.match(r"\d{4}-\d{2}(-\d{2})?$", r["date"]):
        flags.append(f"{r['id']}: date '{r['date']}' not ISO")
    elif r["date"] < CUTOFF[: len(r["date"])]:
        flags.append(f"{r['id']}: dated {r['date']}, before cutoff")
    if r["type"] not in ("B1", "B2"):
        flags.append(f"{r['id']}: type '{r['type']}'")
    return r


rows = myob("research/manual/myob-idea-exchange.md") + productreview("research/manual/productreview.md") \
    + whirlpool("research/manual/whirlpool.md") + collected()
rows = [check(r) for r in rows]
ids = Counter(r["id"] for r in rows)
flags += [f"{i}: duplicate id" for i, n in ids.items() if n > 1]

with open(OUT, "w", encoding="utf-8", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=COLS)
    w.writeheader()
    w.writerows(rows)

print(f"{len(rows)} rows -> {OUT}")
print("by source:", dict(Counter(r["source"].split(":")[0] for r in rows)))
print("by segment:", dict(Counter(r["segment"] for r in rows)))
print("by type:", dict(Counter(r["type"] for r in rows)))
print(f"{len(flags)} flags:")
for f in flags:
    print("  " + f)
