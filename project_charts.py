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
