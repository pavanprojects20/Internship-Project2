
import time

log_file = "logs/raw_logs.txt"

print("Starting Day 7 Live Monitoring...\n")

known_lines = set()

while True:

    with open(log_file, "r") as file:

        lines = file.readlines()

        for line in lines:

            if line not in known_lines:

                known_lines.add(line)

                if "admin" in line or "root" in line:

                    alert = f"[ALERT] Suspicious Login Attempt Detected:\n{line}"

                    print(alert)

                    with open("processed/day7_live_alerts.txt", "a") as alert_file:
                        alert_file.write(alert + "\n")

    time.sleep(2)
