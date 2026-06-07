import pandas as pd

df = pd.read_csv("processed/day3_processed_logs.csv")

ip_ranking = df.groupby("IP").size().sort_values(ascending=False)

report = """
========== TOP ATTACKERS REPORT ==========\n
"""

for ip, count in ip_ranking.items():
    report += f"IP: {ip} | Attempts: {count}\n"

with open("processed/day11_top_attackers_report.txt", "w") as file:
    file.write(report)

print(report)
