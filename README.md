# Network Hardening & Protocol Audit Portfolio
**Owner:** Hassaballah Adam
**Lab Environment:** Ubuntu 24.04 (Noble Numbat)

## [S05] Operation Grid Lock: Subnetting & Connectivity
**Scenario:** Restored network connectivity by identifying a CIDR mismatch between host and gateway.
* **The Problem:** Subnet mask was too restrictive (/27), preventing communication with the gateway (.1).
* **The Solution:** Adjusted the interface to a /24 mask to widen the broadcast domain.
* **Artifact:** `subnet_blueprint.txt`

## [S06] Operation Hidden Door: DNS & Service Interrogation
**Scenario:** Audited the "Deception Layer" where local DNS was hijacked and services were cloaked.
* **The Problem:** `/etc/hosts` was modified to redirect Google traffic to localhost; a web service was hidden on a non-standard port.
* **The Fix:** Sanitized `/etc/hosts` to restore legitimate DNS resolution.
* **Discovery:** Used `ss -tuln` to locate a cloaked Nginx service on **Port 8080**.
* **Artifact:** `protocol_audit.txt`# Security Hardening Automation This script automates the remediation of insecure file permissions on Linux systems, focusing on the Access Control Matrix (ACM) and securing sensitive identity files like /etc/shadow.
