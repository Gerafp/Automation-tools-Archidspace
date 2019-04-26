#Script para la subida masiva de archivos a archivematica

import ast
import base64
import logging
import os
import os.path as path
import shutil
import subprocess
import sys
import time
import shlex


def pid_lck(file):
    if path.exists(file):
        print("El archivo existe")
        os.remove(file)

def main():
    env = os.environ.copy()
    retrieve_commstr = "/opt/archivematica/transfer-source-helpers/dspace-transfer-src-retrieve.py /etc/archivematica/automation-tools/dspace-transfer.src.conf"
    deposit_commstr ="/usr/lib/archivematica/automation-tools/transfers/transfer.py --transfer-type dspace \
      --user jgama \
      --api-key d007fa2eed787fa7e57c40c0642b23fc0c710699 \
      --ss-user jgama \
      --ss-api-key 7d15c06314a7b7ea47b89014aabb94b8477fc448 \
      --transfer-source 6272ac9f-6197-409d-8896-9e573bc21314 \
      --am-url http://127.0.0.1 \
      --ss-url http://127.0.0.1:8000"
    remove_commstr = "/opt/archivematica/transfer-source-helpers/dspace-transfer-src-delete.py /etc/archivematica/automation-tools/dspace-transfer.src.conf"
    transfer_pid_file = "/usr/lib/archivematica/automation-tools/transfers/pid.lck"
    retrieve_pid_file = "/var/archivematica/automation-tools/dspace_retrieve_pid.lck"
    contador = 0

    pid_lck(retrieve_pid_file)
    state = subprocess.call(shlex.split(retrieve_commstr), env=env)
    flag = 0
    while state != 1 and flag < 3:
        print("---------------------------------------------")
        print("Subida de archivo completa")
        print("Procesando para subir a archivematica")
        print("---------------------------------------------")
        state = subprocess.call(shlex.split(deposit_commstr), env=env)
        if state == 0:
            #Eliminamos el archivo pid en caso de que exista
            pid_lck(transfer_pid_file)
            i = 1
            print("---------------------------------------------")
            print("Nueva transferencia")
            print("Realizando ingesta a archivematica")
            print("---------------------------------------------")
            while i < 6 and state != 1:
                pid_lck(transfer_pid_file)
                time.sleep(30)
                i += 1
                state = subprocess.call(shlex.split(deposit_commstr), env=env)
        else:
            print("---------------------------------------------")
            print("Se revisará en estado y se intentará eliminar")
            print("---------------------------------------------")
            pid_lck(transfer_pid_file)
            state = subprocess.call(shlex.split(deposit_commstr), env=env)

        state = subprocess.call(shlex.split(remove_commstr), env=env)
        if state == 1:
            print("---------------------------------------------")
            print("Borrado completo, haciendo nueva transferencia")
            print("---------------------------------------------")
            pid_lck(retrieve_pid_file)
            state = subprocess.call(shlex.split(retrieve_commstr), env=env)
            flag = 0
        else:
            flag += 1

    if flag == 2:
        print("Ocurrio un error en la subida de archivos en archivematica, revisé los depositos en el DashBoard")

if __name__ == '__main__':
    main()
