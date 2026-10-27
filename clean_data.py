"""clean_data.py — YOU build this (Unit 2 L11).

Write a program that reads data/u2_student_performance_data.csv,
handles missing values and impossible values (a GPA of 9? an age of 3?),
converts the right columns to numbers, and writes a CLEAN csv:

    data/clean_student_performance.csv

Keep every column, fix every row — or drop rows you cannot trust,
and keep a count of what you dropped. Print a summary at the end.
"""
# TODO: your cleaning code here
import csv

SANITY = {
    "Age": (10, 22),
    "Math Score": (0, 100),
    "Science Score": (0, 100),
    "English Score": (0, 100),
    "Overall GPA": (0.0, 4.0),
    "Hours Studied Per Week": (0, 60),
    "Sleep Hours Per Night": (0, 14),
    "Absence Rate": (0.0, 1.0),
}

def to_float(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        return None

def is_blank(value):
    return value is None or str(value).strip() == ""

def is_impossible(column, value):
    if column not in SANITY:
        return False
    low, high = SANITY[column]
    return not (low <= value <= high)

# 1. READ
with open("data/u2_student_performance_data.csv", newline="") as f:
    rows = list(csv.DictReader(f))

rows_in = len(rows)
print(f"Rows in: {rows_in}")

# 2. CLEAN
clean_rows = []
dropped_counts = {"blank": 0, "impossible": 0}

for r in rows:
    drop_reason = None

    # Convert numeric columns, track blanks and impossibles
    for col in SANITY:
        if is_blank(r[col]):
            drop_reason = f"blank {col}"
            dropped_counts["blank"] += 1
            break
        val = to_float(r[col])
        if val is None:
            drop_reason = f"unparseable {col}"
            dropped_counts["impossible"] += 1
            break
        if is_impossible(col, val):
            drop_reason = f"impossible {col}={val}"
            dropped_counts["impossible"] += 1
            break
        r[col] = val  # replace string with float

    if drop_reason:
        print(f"Dropped row: {drop_reason}")
        continue

    clean_rows.append(r)

rows_out = len(clean_rows)
rows_dropped = rows_in - rows_out
print(f"Rows out: {rows_out}")
print(f"Rows dropped: {rows_dropped}")
print(f"Dropped by reason: {dropped_counts}")

# Sanity check: counts must add up
assert rows_in == rows_out + rows_dropped, "Count mismatch — cleaning logic bug"

# 3. WRITE
header = list(rows[0].keys())  # original header order
with open("data/u2_student_performance_clean.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for r in clean_rows:
        writer.writerow([r[col] for col in header])

print("Wrote data/u2_student_performance_clean.csv")
