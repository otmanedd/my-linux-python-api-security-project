#!/bin/bash
# Löscht alle Log-Dateien, die älter als 7 Tage sind
find /var/log -name "*.log" -type f -mtime +7 -exec rm -f {} \;
echo "Alte Log-Dateien wurden gelöscht."
