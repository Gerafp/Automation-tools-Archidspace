#!/bin/sh
#  Este Script busca cambios en el sitio de DSpace y los exporta
# con nuevo nombre de archivo para llevar un control de cambios  (Historia)
# Se apoya del Script en Python 3.6 de la carpeta RTSScripts
# Posteriormente termina de hacer el respaldo del contenido que sobra
rm /Files/siteaudit.log
rm /Files/sitebackup.log
echo "Haciendo la auditoria general en busca de cambios..."
/Files/dspaceAPP/bin/dspace curate -t auditaip -i 11191/0 -r - > /Files/siteaudit.log 2>&1
echo "Haciendo la copia de los elementos actualizados..."
python /Files/RTSScripts/Audit-log.py
echo "Haciendo la copia de los elementos restantes..."
/Files/dspaceAPP/bin/dspace curate -t transmitaip -i 11191/0 -r - > /Files/sitebackup.log 2>&1
echo "Fin del RTS"








