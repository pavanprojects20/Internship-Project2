import os

report = """
========== WEEKLY SECURITY REPORT ==========\n
Modules Included:

✓ Attacker Ranking
✓ Attack Source Analysis
✓ Brute Force Detection
✓ Severity Scoring

Generated Reports:
"""

files = [
    "processed/day11_top_attackers_report.txt",
    "processed/day12_geo_report.txt",
    "processed/day13_bruteforce_report.txt",
    "processed/day14_severity_report.txt"
]

for file in files:

    if os.path.exists(file):
        report += f"\n[FOUND] {file}"

    else:
        report += f"\n[MISSING] {file}"

with open("processed/day15_weekly_security_report.txt", "w") as f:
    f.write(report)

print(report)
