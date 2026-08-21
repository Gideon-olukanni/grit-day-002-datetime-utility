# GRIT Day 2 — Explain: Python datetime Module (Cycle 1)

**Gideon Reality Institute of Technology | 1825 Daily Projects OS**
**Day 2 of 1825 | Programming & Software | Year 1: Foundations | August 18, 2026**

---

## What This Is

A complete explanation of Python's `datetime` standard library module
(four classes, all key methods, format code reference, arithmetic patterns)
plus a command-line Day Calculator that applies every concept to the
1825-day personal project system.

Built as Day 2 of a 1,825-consecutive-day project.

---

## Files

| File | Purpose |
|---|---|
| `datetime_explained.md` | Complete module reference — the Explain artifact |
| `day_calculator.py` | CLI: day↔date, schedule, milestones, progress stats |
| `index.html` | Visual reference page (open in browser, works offline) |

---

## Quick Start

No installation required. Python 3.7+.

```bash
git clone https://github.com/[username]/grit-day-002-datetime-utility
cd grit-day-002-datetime-utility

# Show today's day info and upcoming week
python3 day_calculator.py

# Look up a specific day
python3 day_calculator.py day 100

# Find the day number for a date
python3 day_calculator.py date 2026-11-24

# Generate a schedule
python3 day_calculator.py schedule 1 14

# All milestone dates
python3 day_calculator.py milestones
```

---

## Core Functions

```python
# The entire calendar engine is two functions:

def date_for_day(n):
    return START_DATE + datetime.timedelta(days=n - 1)

def day_for_date(d):
    return (d - START_DATE).days + 1
```

---

## Technologies

Python 3 (`datetime`, `sys`) · Markdown · HTML · CSS

---

## Part of the 1825 Daily Projects OS

Day 2 returns as Cycle 2 at Day 14 (timezone awareness),
Cycle 3 at Day 26 (SQLite + datetime), and so on.

---

## License

MIT
