#!/usr/bin/env python3
import subprocess
import json
import os

print("[*] Initiating System Audit...")

# INSTRUCTION 1: Use subprocess.run() to execute 'ps aux'
process_list = subprocess.run(["ps", "aux"], capture_output=True, text=True)# 


# INSTRUCTION 2: Search the captured output for the malicious process
if "unauthorized_cryptominer" in process_list.stdout:
    print("[!] THREAT DETECTED: Cryptominer found running!")

# INSTRUCTION 3: If found, create a dictionary and save it to 'security_alert.json'
if "unauthorized_cryptominer" in process_list.stdout:
        print("[!] THREAT DETECTED: Cryptominer found running!")
        
        # This dictionary belongs INSIDE the if block
        alert_data = {
            "event": "Unauthorized Process",
            "severity": "High",
            "process": "unauthorized_cryptominer"
        }

        # Instruction 3: How do you turn a Dictionary into a file? 
        # Which tool handles that translation?
        with open("security_alert.json", "w") as alert_file:
            json.dump(alert_data, alert_file, indent=4)


print("[+] Audit Complete.")
alert_data = {
            "event": "Unauthorized Process",
            "severity": "High",
            "process": "unauthorized_cryptominer"
        }
