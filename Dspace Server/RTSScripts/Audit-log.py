# Script en python que crea los archivos actualizados del DSPACE y los renombra para que se cosechen
# Usando Archivematica Automation-tools
# eScire 2019
# Hecho para python 3.6+
# ChangeLog
# - Se añadio debug_Class para llevar un registro de las acciones hechas - 28/02/19 - Gerardo Flores

import subprocess, shlex, os, time, sys

#Clase de debugeo
class debug_Class(object):
    """docstring fordebug."""
    log_file = ""
    def __init__(self):
        superdebug, self).__init__()
        log_file = "Audit_log-" + time.strftime("%m%y")+".log"

    def Writelog(string):
        f = open(log_file, "a")
        f.write(time.strftime("%d%m%y-%H:%M:%S")+"\t"+string+"\n")
        f.close()


def get_file_name(replicate_path, partial_name_file):
    for file_name in os.listdir(replicate_path):
        if partial_name_file in file_name:
            return file_name, file_name.replace(".zip", time.strftime("%d%m%y")+".zip")

if __name__ == "__main__":
    logObj = debug_Class()
    cont = 0
    #Paths de las rutas del archivo
        #Path de instalacion de dspacePre
    dspace_path = "/Files/dspaceAPP"
        #Path de la carpeta de replicacion
    replicate_path = "/Files/dspaceAPP/repstore/aip-store/"
        #Path de los archivos auditados
    siteaudit_path_file = "/Files"
    f = open(os.path.join(siteaudit_path_file, "siteaudit.log"))

    for linea in f.readlines():
        if "Local and remote checksums differ for:" in linea:
            aux = linea.replace("\n", "").replace("Local and remote checksums differ for: ", "")
            aux2 = aux.split("/")
            cont ++
            if int(aux2[1]) != 0:
                print(aux)
                logObj.Writelog(aux)
                command = dspace_path + "/bin/dspace curate -t transmitaip -i " + aux+ " -r - > " + os.path.join(siteaudit_path_file, "sitebackup.log") + " 2>&1"
                print(command)
                logObj.Writelog(command)
                logObj.Writelog(subprocess.call(shlex.split(command)))
                time.sleep(30)
                file_name, file_name_copy = get_file_name(replicate_path, aux2[0] + "-" + aux2[1] + ".zip")
                copy_command = "cp -rf " + replicate_path+"/"  + file_name + " " + replicate_path+"/" + file_name_copy
                logObj.Writelog(copy_command)
                logObj.Writelog(subprocess.call(shlex.split(copy_command)))
                print(file_name)
                logObj.Writelog("Finish " + file_name)
    print("- Fin proceso -")
    logObj.Writelog("- Fin proceso - \n Se procesaron " + cont + " archivos ")
