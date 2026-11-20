import socket
from datetime import datetime

target = input("Enter target IP: ")

ports = [22, 80, 443, 445, 3389, 8080, 8000]

risk_levels = {
    22: "MEDIUM - SSH access",
    80: "LOW - HTTP service",
    443: "LOW - HTTPS service",
    445: "HIGH - SMB file sharing",
    3389: "HIGH - Remote Desktop",
    8080: "MEDIUM - Alternative web service",
    8000: "MEDIUM - Development server"
}

open_ports = []

print(f"\nScanning {target}...\n")

for port in ports:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        sock.close()

        if result == 0:
            print(f"[OPEN] Port {port}")
            print(f"  Risk: {risk_levels.get(port, 'UNKNOWN')}")
            open_ports.append(port)
        else:
            print(f"[CLOSED/FILTERED] Port {port}")

    except socket.error as error:
        print(f"Error: {error}")

report = f"""
CYBERSECURITY SCAN REPORT
Target: {target}
Date: {datetime.now()}

OPEN PORT DETAILS:
"""

for port in open_ports:
    report += f"\nPort {port}: {risk_levels.get(port, 'UNKNOWN')}"

report += f"""

Total Open Ports: {len(open_ports)}
"""

with open("security_report.txt", "w") as file:
    file.write(report)

print("\nScan completed!")
print("Security report updated!")




