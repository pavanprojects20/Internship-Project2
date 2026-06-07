import pandas as pd

df = pd.read_csv("processed/day3_processed_logs.csv")

attempt_counts = df.groupby("IP").size()

report = """
========== BRUTE FORCE DETECTION REPORT ==========\n
"""

for ip, count in attempt_counts.items():

    if count >= 3:

        report += f"[ALERT] Possible Brute Force Attack from {ip} | Attempts: {count}\n"

    else:

        report += f"[INFO] {ip} | Attempts: {count}\n"

with open("processed/day13_bruteforce_report.txt", "w") as file:

    file.write(report)

print(report)
