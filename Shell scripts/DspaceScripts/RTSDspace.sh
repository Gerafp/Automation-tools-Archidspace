#!/bin/sh

echo "----------------------------------------"
echo "|          Copiando los archivos       |"
echo "----------------------------------------"
/home/archi/dspace/bin/dspace curate -q replication -r - > /home/archi/dspace/log/replication-queue.log 2>&1

echo "----------------------------------------"
echo "|            Cambiando permisos        |"
echo "----------------------------------------"
chmod 766 /home/archi/DspaceSaves/aip-store/*
