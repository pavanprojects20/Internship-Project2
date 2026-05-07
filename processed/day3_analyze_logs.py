
import pandas as pd

log_file = "logs/raw_logs.txt"

logs = []

with open(log_file, "r") as file:
    for line in file:

        parts = line.strip().split("|")

        if len(parts) == 4:

            timestamp = parts[0].strip()
            ip = parts[1].replace("IP:", "").strip()
            username = parts[2].replace("USERNAME:", "").strip()
            password = parts[3].replace("PASSWORD:", "").strip()

            logs.append([timestamp, ip, username, password])

df = pd.DataFrame(logs, columns=["Timestamp", "IP", "Username", "Password"])

df.to_csv("processed/day3_processed_logs.csv", index=False)

summary = f"""
Total Login Attempts: {len(df)}

Unique IP Addresses:
{df['IP'].nunique()}

Usernames Attempted:
{df['Username'].unique()}
"""

with open("processed/day3_summary_report.txt", "w") as report:
    report.write(summary)

print("Log analysis completed")
print(df)
