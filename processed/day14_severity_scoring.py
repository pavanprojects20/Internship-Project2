import pandas as pd

df = pd.read_csv("processed/day3_processed_logs.csv")

attempt_counts = df.groupby("IP").size()

report = """
========== ATTACK SEVERITY REPORT ==========\n
"""

for ip, count in attempt_counts.items():

    if count >= 5:

        severity = "HIGH"

    elif count >= 3:

        severity = "MEDIUM"

    else:

        severity = "LOW"

    report += f"IP: {ip} | Attempts: {count} | Severity: {severity}\n"

with open("processed/day14_severity_report.txt", "w") as file:

    file.write(report)

print(report)

