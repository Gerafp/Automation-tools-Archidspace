#!/bin/bash

echo "Activando el source"
source /usr/share/python/automation-tools/bin/activate

echo "Eliminado registro de entradas"
python /usr/lib/archivematica/automation-tools/transfers/amclient.py close-completed-transfers --am-user-name jgama d007fa2eed787fa7e57c40c0642b23fc0c710699 --am-url http://148.206.79.5

echo "Elimnando registros de ingestas"
python /usr/lib/archivematica/automation-tools/transfers/amclient.py close-completed-ingests --am-user-name jgama d007fa2eed787fa7e57c40c0642b23fc0c710699 --am-url http://148.206.79.5
