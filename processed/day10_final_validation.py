
import os

files_to_check = [
    "logs/raw_logs.txt",
    "processed/day3_processed_logs.csv",
    "processed/day3_summary_report.txt",
    "processed/day4_security_alerts.txt",
    "processed/day5_dashboard_summary.txt",
    "processed/day7_live_alerts.txt",
    "processed/day8_incident_report.txt",
    "processed/day9_attack_chart.png"
]

report = "\n========== FINAL PROJECT VALIDATION ==========\n\n"

for file in files_to_check:

    if os.path.exists(file):

        report += f"[OK] {file} exists\n"

    else:

        report += f"[MISSING] {file} not found\n"

report += "\nProject validation completed successfully.\n"

with open("processed/day10_project_status_report.txt", "w") as output:
    output.write(report)

print(report)

