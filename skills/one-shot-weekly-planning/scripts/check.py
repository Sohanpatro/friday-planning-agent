#!/usr/bin/env python3
"""The report's fact gate. Three commands, run from the working folder.

  python3 scripts/check.py list      writes checklist.md from sections/*.md
  python3 scripts/check.py readback  prints sections 1-5 whole and records it; section 6 must be written after this
  python3 scripts/check.py verify    compares check-results.md against checklist.md; prints PASS or FAIL
  python3 scripts/check.py assemble  writes the report; refuses unless verify passes and user-canon.md is not the empty default

A wrong number in a plan ends the trust, and every run so far skipped a written
"compare with code" instruction. So the comparison is this file, and assembly
needs it to pass. Nothing here judges prose.
"""
import re, sys, glob, os, datetime, hashlib, json, time

DAYS = "monday|tuesday|wednesday|thursday|friday|saturday|sunday"
MONTHS = "january|february|march|april|may|june|july|august|september|october|november|december"
COUNTS = "one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|twenty|thirty|forty|fifty|hundred"
UNITS = "hour|day|week|month|task|session|call|people|coach|night|evening|minute|item|outcome|errand|entr"
# A load-bearing claim: a digit, a weekday, a month with a day number, money, or a spelled-out count next to a unit.
CLAIM = re.compile(r"\d|\b(?:%s)\b|\b(?:%s)\s+\d|\$|\b(?:%s)\s+(?:%s)" % (DAYS, MONTHS, COUNTS, UNITS), re.I)
NAME = re.compile(r"\b[A-Z][a-z]+ [A-Z][a-z]+\b")
GUIDE = {"1": 475, "2": 375, "3": 425, "4": 525, "5": 525, "6": 375}

def prose_words(text):
    """Words outside tables and headings: the guide's sizes are for prose."""
    n = 0
    for line in text.split("\n"):
        s = line.strip()
        if not s or s.startswith("#") or s.startswith("|"):
            continue
        n += len(s.split())
    return n

def sizes():
    for path in sorted(glob.glob("sections/*.md")):
        sec = os.path.basename(path)[0]
        w = prose_words(open(path, encoding="utf-8").read())
        g = GUIDE.get(sec)
        if g:
            flag = "  <- more than a quarter over: trim" if w > g * 1.25 else ""
            print("section %s prose: %d words (guide %d)%s" % (sec, w, g, flag))

def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()

def readback():
    paths = ["sections/%d.md" % i for i in range(1, 6)]
    missing = [x for x in paths if not os.path.exists(x)]
    if missing:
        sys.exit("readback refused: missing %s" % missing)
    for x in paths:
        print("=" * 20, x, "=" * 20)
        print(open(x, encoding="utf-8").read())
    first = json.load(open("readback.json"))["time"] if os.path.exists("readback.json") else time.time()
    json.dump({"time": first, "sha": {x: sha(x) for x in paths}},
              open("readback.json", "w"))  # keeps the FIRST readback time: section 6 must follow that one
    print("readback recorded. Now write section 6 from what is above.")

def sentences(text):
    text = re.sub(r"\|", " | ", text)
    for para in text.split("\n"):
        para = para.strip()
        if not para or para.startswith("#") or set(para) <= set("|-: "):
            continue
        for s in re.split(r"(?<=[.!?])\s+(?=[A-Z*\"])", para):
            s = s.strip()
            if s:
                yield s

def build_list():
    rows, seen = [], set()
    for path in sorted(glob.glob("sections/*.md")):
        sec = os.path.basename(path)[0]
        for s in sentences(open(path, encoding="utf-8").read()):
            if not CLAIM.search(s):
                continue
            plain = re.sub(r"[*_`|#]", "", s).strip()
            # A short line is kept when it carries a digit: table rows and totals ("Week | 0.6 | 8.1") are where wrong sums hide.
            if (len(plain.split()) < 5 and not re.search(r"\d", plain)) or re.match(r"^\d+[.)]?$", plain):
                continue
            if plain.lower().startswith(("day ", "when ", "outcome ", "task ", "free ", "change ", "why ")):
                continue
            if True:
                key = re.sub(r"\W+", " ", s.lower()).strip()
                if key in seen:
                    continue
                seen.add(key)
                rows.append("%d. [§%s] %s" % (len(rows) + 1, sec, s[:300]))
    open("checklist.md", "w", encoding="utf-8").write(
        "# Checklist: every sentence with a number, date, weekday, time or money in it. Names inside them count too.\n"
        "# The checker returns ONE line per number, in order: <n>. OK <where> | WRONG <correct value, where> | NO SOURCE\n\n"
        + "\n".join(rows) + "\n")
    print("checklist.md: %d lines" % len(rows))
    sizes()
    print("Next: the checker returns one line per number. Then `verify`. Then `assemble`.")

def verify():
    want = [int(m.group(1)) for m in re.finditer(r"^(\d+)\. ", open("checklist.md", encoding="utf-8").read(), re.M)]
    if not os.path.exists("check-results.md"):
        print("FAIL: check-results.md missing"); return False
    got, bad = {}, []
    for line in open("check-results.md", encoding="utf-8"):
        m = re.match(r"\s*(\d+)\s*[.):-]?\s*(OK|WRONG|NO SOURCE)\b", line, re.I)
        r = re.match(r"\s*(\d+)\s*[-–]\s*(\d+)", line)
        if r and not m:
            bad.append("block range not accepted: " + line.strip()[:80])
        elif m:
            got[int(m.group(1))] = m.group(2).upper()
    missing = [n for n in want if n not in got]
    counts = {k: sum(1 for v in got.values() if v == k) for k in ("OK", "WRONG", "NO SOURCE")}
    print("checklist %d lines · verdicts %d · %s" % (len(want), len(got), counts))
    for b in bad: print(b)
    if missing: print("FAIL: no verdict for lines %s" % missing[:40])
    if bad or missing:
        print("FAIL"); return False
    print("PASS")
    print("Before assembling: re-read references/writing-standard.md whole, then run `python3 scripts/check.py readback` and write section 6 from it, if you have not.")
    return True

def assemble(header):
    if not verify():
        sys.exit("assemble refused: verify must PASS")
    canon = "references/user-canon.md"
    if os.path.exists(canon):
        body = re.sub(r"<!--.*?-->", "", open(canon, encoding="utf-8").read(), flags=re.S)
        if not re.search(r"^\s*[-*] ", body, re.M):
            sys.exit("assemble refused: references/user-canon.md holds no setup facts (step 0 writes them)")
    if not os.path.exists("readback.json"):
        sys.exit("assemble refused: run `python3 scripts/check.py readback` before writing section 6")
    rb = json.load(open("readback.json"))
    if os.path.exists("sections/6.md") and os.path.getmtime("sections/6.md") < rb["time"]:
        sys.exit("assemble refused: section 6 is older than the readback; rewrite it from the readback")
    changed = [x for x, h in rb["sha"].items() if not os.path.exists(x) or sha(x) != h]
    if changed:
        print("note: changed since readback (fix pass): %s" % ", ".join(changed))
    sizes()
    parts = [open(p, encoding="utf-8").read().strip() for p in sorted(glob.glob("sections/*.md"))]
    if len(parts) != 6:
        sys.exit("assemble refused: expected 6 section files, found %d" % len(parts))
    name = header.get("file") or "win-the-week-%s.md" % datetime.date.today().isoformat()
    text = (header.get("text", "").strip() + "\n\n---\n\n" + "\n\n---\n\n".join(parts)
            + "\n\nWant more on any part of this? Name the section and I'll go deeper.\n")
    open(name, "w", encoding="utf-8").write(text)
    print("assembled %s · %d words" % (name, len(text.split())))

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "list": build_list()
    elif cmd == "verify": sys.exit(0 if verify() else 1)
    elif cmd == "readback": readback()
    elif cmd == "assemble":
        h = {"file": None, "text": ""}
        for a in sys.argv[2:]:
            if a.startswith("--file="): h["file"] = a[7:]
            elif a.startswith("--header="): h["text"] = open(a[9:], encoding="utf-8").read()
        assemble(h)
    else: print(__doc__)
