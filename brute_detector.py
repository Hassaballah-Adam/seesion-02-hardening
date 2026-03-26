# Phase 2: The Deep Dive
attack_count = 0

try:
    # Double-Door Logic: Reading the Dirty Log ('r') and Writing the Clean Report ('w')
    with open("auth_audit.log", "r") as log_file:
        with open("brute_report.txt", "w") as report_file:
            
            # The Conveyor Belt: Checking every line
            for line in log_file:
                # The Signature Search
                if "Failed password" in line:
                    report_file.write(line)
                    attack_count += 1

    # The Final Audit: This runs only after the files are closed
    print(f"[*] Audit Complete. Extracted {attack_count} threat signatures to brute_report.txt")

except FileNotFoundError:
    print("[-] Alert: Evidence missing! Check if auth_audit.log exists.")