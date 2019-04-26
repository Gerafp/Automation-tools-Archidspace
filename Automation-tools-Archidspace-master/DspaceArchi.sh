#!/bin/bash
# Prueba

echo "Cambio de path"
source /usr/share/python/automation-tools/bin/activate
echo "Borro pid.lock"
rm /var/archivematica/automation-tools/dspace_retrieve_pid.lck
rm /usr/lib/archivematica/automation-tools/transfers/pid.lck
echo "Inicio cosecha"
python /home/cosei/Automation-tools-Archidspace-master/main.py
