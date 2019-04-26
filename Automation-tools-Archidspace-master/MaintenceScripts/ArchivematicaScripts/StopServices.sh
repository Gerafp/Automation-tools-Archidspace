echo "Reiniciando los servicios de Archivematica"
sudo service elasticsearch stop
sudo service clamav-daemon stop
sudo service gearman-job-server stop
sudo service archivematica-mcp-server stop
sudo service archivematica-mcp-client stop
sudo service archivematica-storage-service stop
sudo service archivematica-dashboard stop
sudo service nginx stop
sudo service fits stop

