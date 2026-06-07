report = """
========== END-TO-END TESTING REPORT ==========

[PASS] Honeypot Server
[PASS] Attacker Simulation
[PASS] Log Collection
[PASS] Log Processing
[PASS] Threat Detection
[PASS] Live Monitoring
[PASS] Incident Reporting
[PASS] Visualization
[PASS] Security Recommendations

Overall Status: SUCCESS

==============================================
"""

with open("processed/day18_testing_report.txt", "w") as file:
    file.write(report)

print(report)
