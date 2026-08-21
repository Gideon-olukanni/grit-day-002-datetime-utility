"""
GRIT — Day 2 of 1825
Day Calculator — datetime in practice
Programming & Software | August 18, 2026

Applies Python's datetime module to the 1825 Daily Projects OS.
Converts between day numbers and calendar dates, generates schedules,
and computes progress statistics.

Usage:
    python3 day_calculator.py                       # show today
    python3 day_calculator.py day 100               # lookup day 100
    python3 day_calculator.py date 2026-11-24       # lookup a date
    python3 day_calculator.py schedule 1 14         # 14-day schedule from day 1
    python3 day_calculator.py milestones            # key milestone dates

Requirements:
    Python 3.7+  |  No external libraries  |  No API key
"""

import datetime
import sys


# ─────────────────────────────────────────────────────────────
# CONSTANTS
# ─────────────────────────────────────────────────────────────

START_DATE  = datetime.date(2026, 8, 17)   # Day 1
TOTAL_DAYS  = 1825

DOMAINS = [
    'AI & Automation',
    'Programming & Software',
    'Data & Analytics',
    'Neuroscience & Neuroengineering',
    'Physics & Engineering',
    'Chemistry & Materials',
    'Biology & Life Science',
    'Business & Fintech',
    'Design & Creative Technology',
    'Education & Knowledge Systems',
    'Leadership & Communication',
    'Research & Scientific Thinking',
]

DIFFICULTIES = ['Beginner', 'Beginner+', 'Intermediate', 'Intermediate+', 'Advanced']
TIMES        = ['30-60 min', '60-90 min', '90-120 min', '2-3 hrs']
YEAR_THEMES  = {1: 'Foundations', 2: 'Build', 3: 'Research', 4: 'Scale', 5: 'Mastery'}

MILESTONES = [1, 10, 30, 50, 100, 180, 200, 300, 365, 500, 730, 1000, 1095, 1460, 1825]


# ─────────────────────────────────────────────────────────────
# CORE FUNCTIONS
# ─────────────────────────────────────────────────────────────

def date_for_day(n):
    """Return the calendar date for day n (1–1825).
    
    Uses timedelta arithmetic: Day 1 is START_DATE + 0 days,
    Day 2 is START_DATE + 1 day, Day N is START_DATE + (N-1) days.
    """
    if not 1 <= n <= TOTAL_DAYS:
        return None
    return START_DATE + datetime.timedelta(days=n - 1)


def day_for_date(d):
    """Return the journey day number for a calendar date.
    
    Subtracts START_DATE from d to get a timedelta, then reads .days.
    Adds 1 to convert from zero-indexed offset to one-indexed day number.
    Returns None for dates outside the journey.
    """
    n = (d - START_DATE).days + 1
    return n if 1 <= n <= TOTAL_DAYS else None


def year_for_day(n):
    """Return the year number (1–5) for day n."""
    return min(5, (n - 1) // 365 + 1)


def info(n):
    """Return a dictionary of all attributes for day n.
    
    Uses modulo (%) for cyclic domain and difficulty rotation:
    (n-1) % 12 maps any day to 0–11, cycling through all 12 domains.
    (n-1) % 5  maps any day to 0–4, cycling through all 5 difficulties.
    (n-1) % 4  maps any day to 0–3, cycling through all 4 time slots.
    """
    y = year_for_day(n)
    return {
        'day':    n,
        'date':   date_for_day(n),
        'domain': DOMAINS[(n - 1) % 12],
        'diff':   DIFFICULTIES[(n - 1) % 5],
        'time':   TIMES[(n - 1) % 4],
        'year':   y,
        'theme':  YEAR_THEMES[y],
    }


def progress(n):
    """Return progress statistics for day n.
    
    Calculates:
    - Percentage of the 1825-day journey completed
    - Days remaining in the journey
    - End date of the journey (Day 1825)
    - Calendar days from today to Day 1825
    - Position within the current year phase
    """
    today   = datetime.date.today()
    end     = date_for_day(TOTAL_DAYS)
    y       = year_for_day(n)
    y_start = (y - 1) * 365 + 1
    y_end   = min(y * 365, TOTAL_DAYS)
    return {
        'pct':              round(n / TOTAL_DAYS * 100, 2),
        'remaining':        TOTAL_DAYS - n,
        'end_date':         end,
        'cal_days_to_end':  (end - today).days,
        'day_in_year':      n - y_start + 1,
        'days_left_in_year': y_end - n,
    }


def upcoming(from_n, count=7):
    """Return schedule for the next `count` days from day `from_n`."""
    end = min(from_n + count, TOTAL_DAYS + 1)
    return [info(n) for n in range(from_n, end)]


# ─────────────────────────────────────────────────────────────
# DISPLAY HELPERS
# ─────────────────────────────────────────────────────────────

DIVIDER = '─' * 60


def print_day(n):
    """Print a full info card for day n."""
    i = info(n)
    s = progress(n)
    date_str = i['date'].strftime('%A, %B %d, %Y')
    print(f'\n{DIVIDER}')
    print(f'  Day {i["day"]:>4} of {TOTAL_DAYS}  —  {date_str}')
    print(DIVIDER)
    print(f'  Domain      : {i["domain"]}')
    print(f'  Difficulty  : {i["diff"]}  |  Time: {i["time"]}')
    print(f'  Year {i["year"]} of 5  — {i["theme"]}  (Day {s["day_in_year"]} of year, {s["days_left_in_year"]} left)')
    print(f'  Progress    : {s["pct"]}% complete  |  {s["remaining"]} days remaining')
    print(f'  Journey end : {s["end_date"].strftime("%B %d, %Y")}  ({s["cal_days_to_end"]} calendar days from today)')
    print(DIVIDER)


def print_schedule_row(i):
    """Print one row of the schedule table."""
    date_str = i['date'].strftime('%Y-%m-%d')
    dow      = i['date'].strftime('%a')
    print(f'  Day {i["day"]:4d} | {date_str} {dow} | {i["diff"]:13s} | {i["domain"]}')


# ─────────────────────────────────────────────────────────────
# CLI COMMANDS
# ─────────────────────────────────────────────────────────────

def cmd_today():
    """Show today's day info and upcoming week."""
    today = datetime.date.today()
    n     = day_for_date(today)

    if n is None:
        print('\n  The 1825-day journey has not started or has ended.')
        print(f'  Day 1 begins: {START_DATE.strftime("%A, %B %d, %Y")}')
        days_to_start = (START_DATE - today).days
        if days_to_start > 0:
            print(f'  {days_to_start} days to go.')
        return

    print('\n  TODAY')
    print_day(n)

    print('\n  UPCOMING 7 DAYS')
    print(f'  {"Day":>7} | {"Date":10}     | {"Difficulty":13} | Domain')
    print(f'  {"-"*7}-+-{"-"*15}-+-{"-"*13}-+-{"-"*30}')
    for row in upcoming(n, 7):
        print_schedule_row(row)
    print()


def cmd_day(n):
    """Show info for a specific day number."""
    try:
        n = int(n)
    except ValueError:
        print(f'  Error: "{n}" is not a valid day number.')
        return
    if not 1 <= n <= TOTAL_DAYS:
        print(f'  Error: Day {n} is outside the journey (1–{TOTAL_DAYS}).')
        return
    print_day(n)


def cmd_date(raw):
    """Show info for a specific calendar date."""
    try:
        d = datetime.datetime.strptime(raw, '%Y-%m-%d').date()
    except ValueError:
        print(f'  Error: "{raw}" is not a valid date. Use YYYY-MM-DD format.')
        return
    n = day_for_date(d)
    if n is None:
        print(f'\n  {d.strftime("%B %d, %Y")} is outside the 1825-day journey.')
        print(f'  Journey: {START_DATE.strftime("%B %d, %Y")} → {date_for_day(TOTAL_DAYS).strftime("%B %d, %Y")}')
        return
    print_day(n)


def cmd_schedule(args):
    """Show a multi-day schedule."""
    today      = datetime.date.today()
    current_n  = day_for_date(today) or 1
    from_n     = int(args[0]) if len(args) > 0 else current_n
    count      = int(args[1]) if len(args) > 1 else 14

    print(f'\n  SCHEDULE — Days {from_n} to {min(from_n + count - 1, TOTAL_DAYS)}')
    print(f'  {"Day":>7} | {"Date":10}     | {"Difficulty":13} | Domain')
    print(f'  {"-"*7}-+-{"-"*15}-+-{"-"*13}-+-{"-"*30}')
    for row in upcoming(from_n, count):
        print_schedule_row(row)
    print()


def cmd_milestones():
    """Show all major milestone dates."""
    print(f'\n  1825-DAY JOURNEY — MILESTONES')
    print(f'  {"Day":>7} | {"Date":22} | {"Theme":12} | Domain')
    print(f'  {"-"*7}-+-{"-"*22}-+-{"-"*12}-+-{"-"*30}')
    for n in MILESTONES:
        i = info(n)
        date_str = i['date'].strftime('%A, %B %d, %Y')
        print(f'  Day {n:4d} | {date_str:22s} | {i["theme"]:12s} | {i["domain"]}')
    print()


def cmd_help():
    print("""
  GRIT Day Calculator — datetime in practice
  Day 2 of 1825 | Gideon Reality Institute of Technology

  Usage:
    python3 day_calculator.py                         today + upcoming week
    python3 day_calculator.py day N                   info for day N (1–1825)
    python3 day_calculator.py date YYYY-MM-DD         info for a calendar date
    python3 day_calculator.py schedule [from] [count] multi-day schedule
    python3 day_calculator.py milestones              key journey milestones
""")


# ─────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────

def main():
    args = sys.argv[1:]

    if len(args) == 0:
        cmd_today()
    elif args[0] == 'day'        and len(args) >= 2:
        cmd_day(args[1])
    elif args[0] == 'date'       and len(args) >= 2:
        cmd_date(args[1])
    elif args[0] == 'schedule':
        cmd_schedule(args[1:])
    elif args[0] == 'milestones':
        cmd_milestones()
    else:
        cmd_help()


if __name__ == '__main__':
    main()
