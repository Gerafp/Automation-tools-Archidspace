#Script para la subida masiva de archivos a archivematica

import ast
import base64
import logging
import os
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
      --user (Usuario del DashBoard) \
      --api-key (Key del usuario de DashBoard) \
      --ss-user (Usuario del SS) \
      --ss-api-key (Key del usuario del SS)  \
      --transfer-source (UUI del transfer-source del SS) \
      --am-url http://localhost \
      --ss-url http://localhost:8000 "
    remove_commstr = "/opt/archivematica/transfer-source-helpers/dspace-transfer-src-delete.py /etc/archivematica/automation-tools/dspace-transfer.src.conf"
    transfer_pid_file = "/usr/lib/archivematica/automation-tools/transfers/pid.lck" #Ubicacion por default

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
                #Eliminamos el archivo pid en caso de que exista
                pid_lck(transfer_pid_file)
                time.sleep(30)
                i += 1
                state = subprocess.call(shlex.split(deposit_commstr), env=env)
        else:
            print("---------------------------------------------")
            print("Se revisará en estado y se intentará eliminar")
            print("---------------------------------------------")

            state = subprocess.call(shlex.split(deposit_commstr), env=env)

        state = subprocess.call(shlex.split(remove_commstr), env=env)
        if state == 1:
            print("---------------------------------------------")
            print("Borrado completo, haciendo nueva transferencia")
            print("---------------------------------------------")
            state = subprocess.call(shlex.split(retrieve_commstr), env=env)
            flag = 0
        else:
            flag += 1

    if flag == 2:
        print("Ocurrio un error en la subida de archivos en archivematica, revisé los depositos en el DashBoard")

if __name__ == '__main__':
    main()
