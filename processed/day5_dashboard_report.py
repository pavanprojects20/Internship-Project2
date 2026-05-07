
import pandas as pd

df = pd.read_csv("processed/day3_processed_logs.csv")

total_attempts = len(df)
unique_ips = df["IP"].nunique()
unique_users = df["Username"].nunique()

dashboard = f"""
========== IoT Honeypot Dashboard ==========

Total Login Attempts : {total_attempts}

Unique IP Addresses  : {unique_ips}

Unique Usernames     : {unique_users}

Most Targeted Username:
{df['Username'].mode()[0]}

============================================
"""

with open("processed/day5_dashboard_summary.txt", "w") as file:
    file.write(dashboard)

print(dashboard)
