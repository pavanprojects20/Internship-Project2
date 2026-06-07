architecture = """
========== PROJECT ARCHITECTURE ==========

1. Honeypot Server Module
   - Simulates Healthcare IoT Device
   - Captures attacker login attempts

2. Attacker Simulation Module
   - Generates login attempts
   - Creates test attack scenarios

3. Logging Module
   - Stores usernames, passwords,
     timestamps and IP addresses

4. Analysis Module
   - Processes raw logs
   - Converts logs into structured CSV

5. Threat Detection Module
   - Detects suspicious activity
   - Generates security alerts

6. Monitoring Module
   - Provides real-time monitoring
   - Tracks attacker activity

7. Reporting Module
   - Generates incident reports
   - Creates security summaries

8. Visualization Module
   - Generates attack charts
   - Displays attack statistics

=================================
"""

with open(
    "processed/day17_architecture_document.txt",
    "w"
) as file:

    file.write(architecture)

print(architecture)
