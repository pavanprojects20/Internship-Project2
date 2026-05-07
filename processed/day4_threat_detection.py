
import pandas as pd

log_file = "processed/day3_processed_logs.csv"

df = pd.read_csv(log_file)

ip_counts = df["IP"].value_counts()

alerts = []

for ip, count in ip_counts.items():

    if count >= 1:

        alerts.append(f"Suspicious Activity Detected from IP: {ip} | Attempts: {count}")

with open("processed/day4_security_alerts.txt", "w") as file:

    for alert in alerts:
        file.write(alert + "\n")

print("Day 4 threat detection completed\n")

for alert in alerts:
    print(alert)
