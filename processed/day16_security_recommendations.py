import os

report = """
========== SECURITY RECOMMENDATIONS ==========\n
"""

severity_file = "processed/day14_severity_report.txt"

if os.path.exists(severity_file):

    with open(severity_file, "r") as f:
        content = f.read()

    if "HIGH" in content:
        report += "\n[HIGH] Enable account lockout policies."
        report += "\n[HIGH] Investigate suspicious IP activity."

    if "MEDIUM" in content:
        report += "\n[MEDIUM] Increase monitoring frequency."

    if "LOW" in content:
        report += "\n[LOW] Continue routine monitoring."

else:
    report += "\nSeverity report not found."

with open("processed/day16_recommendations_report.txt", "w") as f:
    f.write(report)

print(report)
