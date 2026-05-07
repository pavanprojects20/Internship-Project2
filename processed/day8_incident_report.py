
import pandas as pd

df = pd.read_csv("processed/day3_processed_logs.csv")

attack_stats = df.groupby("Username").size().reset_index(name="Attempts")

attack_stats.to_csv("processed/day8_attack_statistics.csv", index=False)

report = f"""
========== Incident Report ==========

Total Login Attempts : {len(df)}

Unique IP Addresses  : {df['IP'].nunique()}

Detected Usernames:
{list(df['Username'].unique())}

Most Targeted Username:
{df['Username'].mode()[0]}

=====================================
"""

with open("processed/day8_incident_report.txt", "w") as file:
    file.write(report)

print(report)
print("\nAttack statistics exported successfully.")

