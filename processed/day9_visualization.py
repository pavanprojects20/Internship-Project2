
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("processed/day3_processed_logs.csv")

attack_counts = df["Username"].value_counts()

plt.figure(figsize=(8,5))

attack_counts.plot(kind="bar")

plt.title("IoT Honeypot Attack Attempts")
plt.xlabel("Usernames")
plt.ylabel("Number of Attempts")

plt.tight_layout()

plt.savefig("processed/day9_attack_chart.png")

print("Day 9 visualization completed.")
print("Attack chart saved successfully.")
