import csv
import matplotlib.pyplot as plt

with open("data/u2_campus_threat_daily_clean.csv", newline="") as f:
    rows = list(csv.DictReader(f))

# Data is already sorted by date in the file
dates = [r["date"] for r in rows]
phishing = [r["phishing_reports"] for r in rows]
failed = [r["failed_logins"] for r in rows]

plt.figure(figsize=(10, 5))
plt.plot(dates, phishing, marker="o", label="Phishing reports", alpha=0.7)
plt.plot(dates, failed, marker="s", label="Failed logins", alpha=0.7)
plt.title("Daily Phishing Reports and Failed Logins — Oct 5 to Dec 3, 2026")
plt.xlabel("Date")
plt.ylabel("Count")
plt.legend()
plt.xticks(rotation=45)   # angle the date labels so they don't overlap
plt.tight_layout()        # prevents label cutoff
plt.savefig("chart1_timeline.png", dpi=150)
plt.clf()

from datetime import datetime

def is_weekend(d):
    return datetime.strptime(d, "%Y-%m-%d").weekday() >= 5   # 5 = Sat, 6 = Sun

wd, we = [], []
for row in rows:
    (we if is_weekend(row["date"]) else wd).append(int(row["phishing_reports"]))

avg_wd, avg_we = sum(wd) / len(wd), sum(we) / len(we)
print(f"weekday {avg_wd:.2f} ({len(wd)} days) | weekend {avg_we:.2f} ({len(we)} days)")

plt.figure(figsize=(6, 4))
plt.bar(["Weekday", "Weekend"], [avg_wd, avg_we])
plt.text(0, avg_wd, f"{avg_wd:.2f}", ha="center", va="bottom")
plt.text(1, avg_we, f"{avg_we:.2f}", ha="center", va="bottom")
plt.title("<your finding, for your audience>")
plt.xlabel("Day type")
plt.ylabel("Average phishing reports")
plt.ylim(bottom=0)
plt.tight_layout()
plt.savefig("chart2_weekday_weekend.png")
plt.clf()

rates = [float(row["login_success_rate"]) for row in rows]

plt.figure(figsize=(7, 4))
plt.hist(rates, bins=15, edgecolor="white")
plt.title("<your finding, for your audience>")
plt.xlabel("Login success rate")
plt.ylabel("Number of days")
plt.tight_layout()
plt.savefig("chart3_success_rate.png")
plt.clf()