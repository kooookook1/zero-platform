#!/usr/bin/env python3
"""
ZERO Platform - Demo Tools Simulator
© 2025 ZERO Platform. All rights reserved.

This script creates demo versions of security tools for testing the platform
when the actual tools are not available.
"""

import os
import sys
import time
import random

def simulate_nmap(target):
    """Simulate nmap scan"""
    print(f"Starting Nmap 7.94 ( https://nmap.org ) at {time.strftime('%Y-%m-%d %H:%M')} UTC")
    print(f"Nmap scan report for {target}")
    
    # Simulate some open ports
    ports = [22, 80, 443, 8080, 3306]
    for port in random.sample(ports, random.randint(2, 4)):
        service = {22: 'ssh', 80: 'http', 443: 'https', 8080: 'http-proxy', 3306: 'mysql'}
        print(f"{port}/tcp open  {service.get(port, 'unknown')}")
        time.sleep(0.5)
    
    print(f"\nNmap done: 1 IP address (1 host up) scanned in {random.randint(5, 15)} seconds")

def simulate_nikto(target):
    """Simulate nikto scan"""
    print(f"- Nikto v2.5.0")
    print(f"+ Target IP:          {target}")
    print(f"+ Target Hostname:    {target}")
    print(f"+ Target Port:        80")
    print(f"+ Start Time:         {time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    findings = [
        "+ Server: Apache/2.4.41",
        "+ Retrieved x-powered-by header: PHP/7.4.3",
        "+ The anti-clickjacking X-Frame-Options header is not present.",
        "+ The X-XSS-Protection header is not defined.",
        "+ The X-Content-Type-Options header is not set.",
        "+ Root page / redirects to: /login.php",
        "+ Cookie PHPSESSID created without the httponly flag",
    ]
    
    for finding in findings:
        print(finding)
        time.sleep(0.3)
    
    print(f"+ {len(findings)} host(s) tested")

def simulate_sqlmap(target):
    """Simulate sqlmap scan"""
    print("        ___")
    print("       __H__")
    print(" ___ ___[']_____ ___ ___  {1.7.2#stable}")
    print("|_ -| . [)]     | .'| . |")
    print("|___|_  [']_|_|_|__,|  _|")
    print("      |_|V...       |_|   https://sqlmap.org")
    print()
    print(f"[*] starting @ {time.strftime('%H:%M:%S')}")
    print(f"[*] testing connection to the target URL")
    print(f"[*] checking if the target is protected by some kind of WAF/IPS")
    time.sleep(1)
    print("[*] testing if the target URL content is stable")
    time.sleep(1)
    print("[*] target URL content is stable")
    print("[*] testing if GET parameter 'id' is dynamic")
    time.sleep(1)
    print("[*] confirming that GET parameter 'id' is dynamic")
    print("[*] heuristic (basic) test shows that GET parameter 'id' might be injectable")
    time.sleep(1)
    print("[*] testing for SQL injection on GET parameter 'id'")
    print("[*] testing 'AND boolean-based blind - WHERE or HAVING clause'")
    time.sleep(2)
    print("[*] GET parameter 'id' appears to be 'AND boolean-based blind - WHERE or HAVING clause' injectable")

def simulate_hydra(target, service="ssh"):
    """Simulate hydra brute force"""
    print(f"Hydra v9.4 (c) 2022 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).")
    print()
    print(f"Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"[DATA] max 16 tasks per 1 server, overall 16 tasks, 14344399 login tries (l:1/p:14344399), ~896525 tries per task")
    print(f"[DATA] attacking {service}://{target}:22/")
    
    time.sleep(2)
    attempts = ["admin:admin", "root:root", "admin:password", "user:user"]
    for attempt in attempts:
        print(f"[ATTEMPT] target {target} - login \"{attempt.split(':')[0]}\" - pass \"{attempt.split(':')[1]}\"")
        time.sleep(0.5)
    
    if random.choice([True, False]):
        print(f"[22][{service}] host: {target}   login: admin   password: admin")
        print("1 of 1 target successfully completed, 1 valid password found")
    else:
        print("0 of 1 target completed, 0 valid passwords found")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 demo_tools.py <tool> [target] [options...]")
        sys.exit(1)
    
    tool = sys.argv[1]
    target = sys.argv[2] if len(sys.argv) > 2 else "example.com"
    
    print(f"ZERO Platform Demo Tool - Simulating {tool}")
    print("=" * 50)
    
    if tool == "nmap":
        simulate_nmap(target)
    elif tool == "nikto":
        simulate_nikto(target)
    elif tool == "sqlmap":
        simulate_sqlmap(target)
    elif tool == "hydra":
        service = sys.argv[3] if len(sys.argv) > 3 else "ssh"
        simulate_hydra(target, service)
    else:
        print(f"Demo for {tool} not implemented yet.")
        print("Available demos: nmap, nikto, sqlmap, hydra")

if __name__ == "__main__":
    main()