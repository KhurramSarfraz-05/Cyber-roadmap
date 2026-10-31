#!/usr/bin/env python3
"""
Simple TCP Port Scanner
Author: Khurram Sarfraz
Usage: python3 portscanner.py <target_ip> [start_port] [end_port]
"""

import socket
import sys
from datetime import datetime

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        sock.close()
        return result == 0
    except socket.error:
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 portscanner.py <target_ip> [start_port] [end_port]")
        sys.exit(1)

    target = sys.argv[1]
    start_port = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    end_port = int(sys.argv[3]) if len(sys.argv) > 3 else 1024

    print(f"\nScanning target: {target}")
    print(f"Port range: {start_port}-{end_port}")
    print(f"Started at: {datetime.now()}\n")

    open_ports = []

    try:
        for port in range(start_port, end_port + 1):
            if scan_port(target, port):
                try:
                    service = socket.getservbyport(port)
                except OSError:
                    service = "unknown"
                print(f"[+] Port {port} is OPEN  ({service})")
                open_ports.append(port)
    except KeyboardInterrupt:
        print("\nScan interrupted by user.")
        sys.exit(0)

    print(f"\nScan complete. {len(open_ports)} open port(s) found.")
    print(f"Finished at: {datetime.now()}")

if __name__ == "__main__":
    main()
