#!/bin/bash

# Fix local Vault permissions
chmod 700 /home/skipy/Vault
chmod 600 /home/skipy/Vault/secrets.txt

# secure system identity files
sudo chmod 640 /etc/shadow
sudo chown root:shadow /etc/shadow

echo "Security Posture Restored."




