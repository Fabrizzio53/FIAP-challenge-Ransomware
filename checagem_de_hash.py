from ast import Continue
import os
import hashlib
from time import sleep
import win32api
import psutil
from datetime import datetime
import time
import signal
import requests

usuarios = []
lista = []
usuario = os.getlogin()
usuariofinal = ""

def recuperar_arquivos(usuariofinal):
    url = "https://github.com/Fabrizzio53/Dummy/raw/main/senhas.pdf"
    url1 = "https://github.com/Fabrizzio53/Dummy/raw/main/trabalho.pptx"
    url2 = "https://github.com/Fabrizzio53/Dummy/raw/main/money.docx"
    url3 = "https://github.com/Fabrizzio53/Dummy/raw/main/contas.txt"

    response = requests.get(url)
    response1 = requests.get(url1)
    response2 = requests.get(url2)
    response3 = requests.get(url3)

    #remover

    os.system(f"rmdir /S /Q C:\\Users\\{usuariofinal}\\Desktop\\filesran")
    os.system(f"rmdir /S /Q C:\\Users\\{usuariofinal}\\Documents\\filesran")
    os.system(f"rmdir /S /Q C:\\Users\\{usuariofinal}\\Downloads\\filesran")

    try:
        os.mkdir(f"C:\\Users\\{usuariofinal}\\Desktop\\filesran")
    except FileExistsError:
        os.system(f"rmdir /S /Q C:\\Users\\{usuariofinal}\\Desktop\\filesran")
        os.mkdir(f"C:\\Users\\{usuariofinal}\\Desktop\\filesran")
    
    try:
        os.mkdir(f"C:\\Users\\{usuariofinal}\\Documents\\filesran")
    except FileExistsError:
        os.system(f"rmdir /S /Q C:\\Users\\{usuariofinal}\\Documents\\filesran")
        os.mkdir(f"C:\\Users\\{usuariofinal}\\Documents\\filesran")

    try:
        os.mkdir(f"C:\\Users\\{usuariofinal}\\Downloads\\filesran")
    except FileExistsError:
        os.system(f"rmdir /S /Q C:\\Users\\{usuariofinal}\\Downloads\\filesran")
        os.mkdir(f"C:\\Users\\{usuariofinal}\\Downloads\\filesran")

    with open(f"C:\\Users\\{usuariofinal}\\Desktop\\filesran\\contas.txt","wb") as file:
        file.write(response3.content)

    with open(f"C:\\Users\\{usuariofinal}\\Desktop\\filesran\\money.docx","wb") as file:
        file.write(response2.content)


    with open(f"C:\\Users\\{usuariofinal}\\Desktop\\filesran\\senhas.pdf","wb") as file:
        file.write(response.content)

    with open(f"C:\\Users\\{usuariofinal}\\Desktop\\filesran\\trabalho.pptx","wb") as file:
        file.write(response1.content)


    #==================================#

    with open(f"C:\\Users\\{usuariofinal}\\Documents\\filesran\\contas.txt","wb") as file:
        file.write(response3.content)

    with open(f"C:\\Users\\{usuariofinal}\\Documents\\filesran\\money.docx","wb") as file:
        file.write(response2.content)


    with open(f"C:\\Users\\{usuariofinal}\\Documents\\filesran\\senhas.pdf","wb") as file:
        file.write(response.content)

    with open(f"C:\\Users\\{usuariofinal}\\Documents\\filesran\\trabalho.pptx","wb") as file:
        file.write(response1.content)


    #==========================#

    with open(f"C:\\Users\\{usuariofinal}\\Downloads\\filesran\\contas.txt","wb") as file:
        file.write(response3.content)

    with open(f"C:\\Users\\{usuariofinal}\\Downloads\\filesran\\money.docx","wb") as file:
        file.write(response2.content)


    with open(f"C:\\Users\\{usuariofinal}\\Downloads\\filesran\\senhas.pdf","wb") as file:
        file.write(response.content)

    with open(f"C:\\Users\\{usuariofinal}\\Downloads\\filesran\\trabalho.pptx","wb") as file:
        file.write(response1.content)

    print("recuperando arquivos")
    win32api.MessageBox(0, 'Alerta', 'Ransonware detectado')

with open("C:\\backupconfig\\contas.txt","r") as conta:
    conta = conta.readlines()

for i in range(len(conta)):
    usuarios.append(conta[i].replace("\n",""))

for i in range(len(usuarios)):

    if os.getlogin() == usuarios[i]:
        usuariofinal = usuarios[i]
        break

if usuariofinal == "":
    print("Usuário não autorizado")
    quit()



lista.append(f"C:\\Users\\{usuariofinal}\\Desktop\\filesran\\contas.txt")
lista.append(f"C:\\Users\\{usuariofinal}\\Desktop\\filesran\\money.docx")
lista.append(f"C:\\Users\\{usuariofinal}\\Desktop\\filesran\\senhas.pdf")
lista.append(f"C:\\Users\\{usuariofinal}\\Desktop\\filesran\\trabalho.pptx")

#=======================================#

lista.append(f"C:\\Users\\{usuariofinal}\\Documents\\filesran\\contas.txt")
lista.append(f"C:\\Users\\{usuariofinal}\\Documents\\filesran\\money.docx")
lista.append(f"C:\\Users\\{usuariofinal}\\Documents\\filesran\\senhas.pdf")
lista.append(f"C:\\Users\\{usuariofinal}\\Documents\\filesran\\trabalho.pptx")


#=========================================#


lista.append(f"C:\\Users\\{usuariofinal}\\Downloads\\filesran\\contas.txt")
lista.append(f"C:\\Users\\{usuariofinal}\\Downloads\\filesran\\money.docx")
lista.append(f"C:\\Users\\{usuariofinal}\\Downloads\\filesran\\senhas.pdf")
lista.append(f"C:\\Users\\{usuariofinal}\\Downloads\\filesran\\trabalho.pptx")

BLOCK_SIZE = 65536 

with open(f"C:\\backupconfig\\{usuariofinal}\\hash_original.txt","r") as config:
    linhas = config.readlines()

    while True:

        for i in range(len(lista)):
            file_hash = hashlib.md5()
            try: 
                with open(lista[i], 'rb') as f: 
                    fb = f.read(BLOCK_SIZE) 
                    while len(fb) > 0: 
                        file_hash.update(fb) 
                        fb = f.read(BLOCK_SIZE) 

                    hashed = file_hash.hexdigest()

                    if str(linhas[i]).replace("\n","") == hashed:
                        continue

                    else:
                        agora = datetime.now()
                        try:
                            for proc in psutil.process_iter():
                                if str(proc.name()) == "msedge.exe" or str(proc.name()) == "System Idle Process" or str(proc.name()) == "System" or str(proc.name()) == "python.exe" or str(proc.name()) == "smartscreen.exe" or str(proc.name()) == "RuntimeBroker.exe" or str(proc.name()) == "SearchFilterHost.exe" or str(proc.name()) == "backgroundTaskHost.exe" or str(proc.name()) == "SearchProtocolHost.exe" or str(proc.name()) == "Registry" or str(proc.name()) == "svchost.exe" or str(proc.name()) == "wininit.exe" or str(proc.name()) == "OneDrive.exe" or str(proc.name()) == "powershell.exe" or str(proc.name()) == "Code.exe" or str(proc.name()) == "notepad.exe" or str(proc.name()) == "WmiPrvSE.exe" or str(proc.name()) == "dllhost.exe" or str(proc.name()) == "UserOOBEBroker.exe" or str(proc.name()) == "FileCoAuth.exe" or str(proc.name()) == "audiodg.exe" or str(proc.name()) == "taskhostw.exe" or str(proc.name()) == "rundll32.exe" or str(proc.name()) == "SearchApp.exe" or str(proc.name()) == "cmd.exe" or str(proc.name()) == "Microsoft.Photos.exe" or str(proc.name()) == "HxTsr.exe" or str(proc.name()) == "TiWorker.exe":
                                    continue
                                
                                #now = datetime.now()
                                horasprocessos = int(time.strftime("%H",time.localtime(proc.create_time())))*3600
                                minutoprocessos = int(time.strftime("%M",time.localtime(proc.create_time())))*60
                                segundossprocessos = int(time.strftime("%S",time.localtime(proc.create_time())))
                                totalprocessos = horasprocessos + minutoprocessos + segundossprocessos

                                horaatual = int(agora.strftime("%H"))*3600
                                minutoatual = int(agora.strftime("%M"))*60
                                segundosatual = int(agora.strftime("%S"))

                                totalagora = horaatual + minutoatual + segundosatual
                                

                                if abs(totalagora - totalprocessos) > 60:
                                    continue
                                else:
                                    if str(proc.name()) == "msedge.exe" or str(proc.name()) == "System Idle Process" or str(proc.name()) == "System" or str(proc.name()) == "python.exe" or str(proc.name()) == "smartscreen.exe" or str(proc.name()) == "RuntimeBroker.exe" or str(proc.name()) == "SearchFilterHost.exe" or str(proc.name()) == "backgroundTaskHost.exe" or str(proc.name()) == "SearchProtocolHost.exe" or str(proc.name()) == "Registry" or str(proc.name()) == "svchost.exe" or str(proc.name()) == "wininit.exe" or str(proc.name()) == "OneDrive.exe" or str(proc.name()) == "powershell.exe" or str(proc.name()) == "Code.exe" or str(proc.name()) == "notepad.exe" or str(proc.name()) == "WmiPrvSE.exe" or str(proc.name()) == "dllhost.exe" or str(proc.name()) == "UserOOBEBroker.exe" or str(proc.name()) == "FileCoAuth.exe" or str(proc.name()) == "audiodg.exe" or str(proc.name()) == "taskhostw.exe" or str(proc.name()) == "rundll32.exe" or str(proc.name()) == "SearchApp.exe" or str(proc.name()) == "cmd.exe" or str(proc.name()) == "Microsoft.Photos.exe" or str(proc.name()) == "HxTsr.exe" or str(proc.name()) == "TiWorker.exe":
                                        continue
                                    else:
                                        try:
                                            os.kill(proc.pid, signal.SIGTERM)
                                            print("matei o processo: ", proc.name())
                                        except (PermissionError, OSError):
                                            continue

                        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                            continue
            except FileNotFoundError:
                try:
                    agora = datetime.now()
                    for proc in psutil.process_iter():

                        if str(proc.name()) == "msedge.exe" or str(proc.name()) == "System Idle Process" or str(proc.name()) == "System" or str(proc.name()) == "python.exe" or str(proc.name()) == "smartscreen.exe" or str(proc.name()) == "RuntimeBroker.exe" or str(proc.name()) == "SearchFilterHost.exe" or str(proc.name()) == "backgroundTaskHost.exe" or str(proc.name()) == "SearchProtocolHost.exe" or str(proc.name()) == "Registry" or str(proc.name()) == "svchost.exe" or str(proc.name()) == "wininit.exe" or str(proc.name()) == "OneDrive.exe" or str(proc.name()) == "powershell.exe" or str(proc.name()) == "Code.exe" or str(proc.name()) == "notepad.exe" or str(proc.name()) == "WmiPrvSE.exe" or str(proc.name()) == "dllhost.exe" or str(proc.name()) == "UserOOBEBroker.exe" or str(proc.name()) == "FileCoAuth.exe" or str(proc.name()) == "audiodg.exe" or str(proc.name()) == "taskhostw.exe" or str(proc.name()) == "rundll32.exe" or str(proc.name()) == "SearchApp.exe" or str(proc.name()) == "cmd.exe" or str(proc.name()) == "Microsoft.Photos.exe" or str(proc.name()) == "HxTsr.exe" or str(proc.name()) == "TiWorker.exe":
                            continue

                        horasprocessos = int(time.strftime("%H",time.localtime(proc.create_time())))*3600
                        minutoprocessos = int(time.strftime("%M",time.localtime(proc.create_time())))*60
                        segundossprocessos = int(time.strftime("%S",time.localtime(proc.create_time())))
                        totalprocessos = horasprocessos + minutoprocessos + segundossprocessos

                        horaatual = int(agora.strftime("%H"))*3600
                        minutoatual = int(agora.strftime("%M"))*60
                        segundosatual = int(agora.strftime("%S"))

                        totalagora = horaatual + minutoatual + segundosatual
                        

                        if abs(totalagora - totalprocessos) > 60:
                            continue
                        else:
                            if str(proc.name()) == "msedge.exe" or str(proc.name()) == "System Idle Process" or str(proc.name()) == "System" or str(proc.name()) == "python.exe" or str(proc.name()) == "smartscreen.exe" or str(proc.name()) == "RuntimeBroker.exe" or str(proc.name()) == "SearchFilterHost.exe" or str(proc.name()) == "backgroundTaskHost.exe" or str(proc.name()) == "SearchProtocolHost.exe" or str(proc.name()) == "Registry" or str(proc.name()) == "svchost.exe" or str(proc.name()) == "wininit.exe" or str(proc.name()) == "OneDrive.exe" or str(proc.name()) == "powershell.exe" or str(proc.name()) == "Code.exe" or str(proc.name()) == "notepad.exe" or str(proc.name()) == "WmiPrvSE.exe" or str(proc.name()) == "dllhost.exe" or str(proc.name()) == "UserOOBEBroker.exe" or str(proc.name()) == "FileCoAuth.exe" or str(proc.name()) == "audiodg.exe" or str(proc.name()) == "taskhostw.exe" or str(proc.name()) == "rundll32.exe" or str(proc.name()) == "SearchApp.exe" or str(proc.name()) == "cmd.exe" or str(proc.name()) == "Microsoft.Photos.exe" or str(proc.name()) == "HxTsr.exe":
                                continue
                            else:
                                try:
                                    os.kill(proc.pid, signal.SIGTERM)
                                    print("matei o processo: ", proc.name())
                                except (PermissionError, OSError):
                                    continue
                    recuperar_arquivos(usuariofinal)
                          
                    
        
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    continue
                
                
        

            

  
                




 


    
