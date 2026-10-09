import csv
import matplotlib.pyplot as plt

with open("data/u2_dataset1_study_habits.csv") as f:
    rows = list(csv.reader(f))

data = rows[1:]                        
print(len(data))                      
hours  = [float(r[1]) for r in data]
scores = [float(r[2]) for r in data]

plt.scatter(hours, scores, s=15)
plt.title("Test Score vs. Study Hours (52 Students)")
plt.xlabel("Weekly Study Hours (hrs)")
plt.ylabel("Test Score (points)")
plt.grid(True)
plt.savefig("score_vs_hours.png", dpi=150)

