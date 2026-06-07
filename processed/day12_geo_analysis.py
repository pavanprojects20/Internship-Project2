import pandas as pd

df = pd.read_csv("processed/day3_processed_logs.csv")

report = """
========== ATTACK SOURCE ANALYSIS ==========\n
"""

for ip in df["IP"].unique():

    report += f"IP Address: {ip}\n"
    report += "Location: Localhost Simulation\n\n"

with open("processed/day12_geo_report.txt", "w") as file:

    file.write(report)

print(report)
