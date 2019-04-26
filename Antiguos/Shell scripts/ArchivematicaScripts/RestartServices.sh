#!/bin/bash
echo "----------------------------------------"
echo "|Reiniciando servicios de Archivematica|"
echo "----------------------------------------"

sudo service elasticsearch restart
sudo service clamav-daemon restart
sudo service gearman-job-server restart
sudo service archivematica-mcp-server restart
sudo service archivematica-mcp-client restart
sudo service archivematica-storage-service restart
sudo service archivematica-dashboard restart
sudo service nginx restart
sudo service fits restart

echo "***********************"
echo "***Proceso terminado***"
echo "***********************"
