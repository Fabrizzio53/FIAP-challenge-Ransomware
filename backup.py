import os
import shutil
from datetime import date




def backup():

    dirs = open(f"C:\\backupconfig\\pastas.txt","r")
   

    dirslinhas = dirs.readlines()

    nome_do_pc = os.getlogin()

    dirs2 = []

    dirs3 = []

    for i in range(len(dirslinhas)):
        if os.path.isdir(dirslinhas[i].replace("\n","")) == True:
            dirs2.append(dirslinhas[i].replace("\n",""))
        else:
            continue

    for i in range(len(dirslinhas)):
        if os.path.isdir(dirslinhas[i].replace("\n","")) == True:
            dirs3.append(dirslinhas[i][3::].replace("\\","_").replace("\n",""))
        else:
            continue

    if dirs2:
        pass
    else:
        print("Erro no programa, a lista não tem pelo menos 1 index")
        quit()

    today = date.today()

    d1 = today.strftime("_%d_%m_%Y")

    print("Iniciando backup.....")

    for i in range(len(dirs2)):
        try:  
            shutil.copytree(dirs2[i],f"C:\\Users\\backup\\{d1}\\{dirs3[i]}")
        except FileExistsError:
            pass
        except shutil.Error:
            pass
            
        
            
            
    os.system(f"cacls C:\\Users\\backup /e /p backup:F")
    os.system(f"cacls C:\\Users\\backup /e /p nobackup:N")

    print("Backup finalizado")

    with open("C:\\backupconfig\\logs.txt","a") as logs:
        logs.write(f"Backup feito em: {d1}\n")










backup()

    

