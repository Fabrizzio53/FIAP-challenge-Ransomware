import os
import hashlib
from time import sleep
import win32api
import psutil
from datetime import datetime
import time
import signal
import requests
from datetime import date
import socket

repetir = 0
BLOCK_SIZE = 65536
usuarios = []
lista = []
lista2 = []
usuario = os.getlogin()
usuariofinal = ""
eula = "C:\\backupconfig"


def recuperar_arquivos_adm():


    try:
        if os.path.isfile(f"{eula}\\iscas.txt") == True:
            with open(f"{eula}\\iscas.txt","r") as iscas:


                url = "https://github.com/Fabrizzio53/Dummy/raw/main/senhas.pdf"
                url1 = "https://github.com/Fabrizzio53/Dummy/raw/main/trabalho.pptx"
                url2 = "https://github.com/Fabrizzio53/Dummy/raw/main/money.docx"
                url3 = "https://github.com/Fabrizzio53/Dummy/raw/main/contas.txt" 

                socket.gethostbyname("www.google.com.br")
                response = requests.get(url)
                response1 = requests.get(url1)
                response2 = requests.get(url2)
                response3 = requests.get(url3)

                iscalinhas = iscas.readlines()

                iscas_usuario = []

                for i in range(len(iscalinhas)):
                    iscas_usuario.append(iscalinhas[i].replace("\n",""))

                for i in range(len(iscas_usuario)):  


                    while True:
                        try:
                            os.mkdir(f"{iscas_usuario[i]}\\filesran")
                            break
                        except FileExistsError:
                            os.system(f'rmdir /S /Q "{iscas_usuario[i]}\\filesran"')
                            os.mkdir(f"{iscas_usuario[i]}\\filesran")
                            break                      

                    with open(f"{iscas_usuario[i]}\\filesran\\contas.txt","wb") as file:
                        lista.append(f"{iscas_usuario[i]}\\filesran\\contas.txt")
                        file.write(response3.content)

                    with open(f"{iscas_usuario[i]}\\filesran\\money.docx","wb") as file:

                        lista.append(f"{iscas_usuario[i]}\\filesran\\money.docx")
                        file.write(response2.content)


                    with open(f"{iscas_usuario[i]}\\filesran\\senhas.pdf","wb") as file:
                        
                        lista.append(f"{iscas_usuario[i]}\\filesran\\senhas.pdf")
                        file.write(response.content)

                    with open(f"{iscas_usuario[i]}\\filesran\\trabalho.pptx","wb") as file:
                        
                        lista.append(f"{iscas_usuario[i]}\\filesran\\trabalho.pptx")
                        file.write(response1.content)

                iscas_usuario.clear()
        else:
            pass    


        for i in conta:
            i = i.replace('\n','')

            url = "https://github.com/Fabrizzio53/Dummy/raw/main/senhas.pdf"
            url1 = "https://github.com/Fabrizzio53/Dummy/raw/main/trabalho.pptx"
            url2 = "https://github.com/Fabrizzio53/Dummy/raw/main/money.docx"
            url3 = "https://github.com/Fabrizzio53/Dummy/raw/main/contas.txt"


            

            socket.gethostbyname("www.google.com.br")
            response = requests.get(url)
            response1 = requests.get(url1)
            response2 = requests.get(url2)
            response3 = requests.get(url3)

            #remover

            while True:
                try:
                    os.mkdir(f"C:\\Users\\{i}\\Documents\\filesran")
                    break
                except FileExistsError:
                    os.system(f"rmdir /S /Q C:\\Users\\{i}\\Documents\\filesran")
                    os.mkdir(f"C:\\Users\\{i}\\Documents\\filesran")
                    break


            while os.path.isdir(f"C:\\Users\\{i}\\Desktop\\filesran") == True:
                os.system(f"rmdir /S /Q C:\\Users\\{i}\\Desktop\\filesran")
                

            try:
                os.mkdir(f"C:\\Users\\{i}\\Desktop\\filesran")
                
            except FileExistsError:
                os.system(f"rmdir /S /Q C:\\Users\\{i}\\Desktop\\filesran")
                os.mkdir(f"C:\\Users\\{i}\\Desktop\\filesran")
                
            
            while True:
                try:
                    os.mkdir(f"C:\\Users\\{i}\\Documents\\filesran")
                    break
                except FileExistsError:
                    os.system(f"rmdir /S /Q C:\\Users\\{i}\\Documents\\filesran")
                    os.mkdir(f"C:\\Users\\{i}\\Documents\\filesran")
                    break

            while True:
                try:
                    os.mkdir(f"C:\\Users\\{i}\\Downloads\\filesran")
                    break
                except FileExistsError:
                    os.system(f"rmdir /S /Q C:\\Users\\{i}\\Downloads\\filesran")
                    os.mkdir(f"C:\\Users\\{i}\\Downloads\\filesran")
                    break

            with open(f"C:\\Users\\{i}\\Desktop\\filesran\\contas.txt","wb") as file:
                file.write(response3.content)

            with open(f"C:\\Users\\{i}\\Desktop\\filesran\\money.docx","wb") as file:
                file.write(response2.content)


            with open(f"C:\\Users\\{i}\\Desktop\\filesran\\senhas.pdf","wb") as file:
                file.write(response.content)

            with open(f"C:\\Users\\{i}\\Desktop\\filesran\\trabalho.pptx","wb") as file:
                file.write(response1.content)


            #==================================#

            with open(f"C:\\Users\\{i}\\Documents\\filesran\\contas.txt","wb") as file:
                file.write(response3.content)

            with open(f"C:\\Users\\{i}\\Documents\\filesran\\money.docx","wb") as file:
                file.write(response2.content)


            with open(f"C:\\Users\\{i}\\Documents\\filesran\\senhas.pdf","wb") as file:
                file.write(response.content)

            with open(f"C:\\Users\\{i}\\Documents\\filesran\\trabalho.pptx","wb") as file:
                file.write(response1.content)


            #==========================#

            with open(f"C:\\Users\\{i}\\Downloads\\filesran\\contas.txt","wb") as file:
                file.write(response3.content)

            with open(f"C:\\Users\\{i}\\Downloads\\filesran\\money.docx","wb") as file:
                file.write(response2.content)


            with open(f"C:\\Users\\{i}\\Downloads\\filesran\\senhas.pdf","wb") as file:
                file.write(response.content)

            with open(f"C:\\Users\\{i}\\Downloads\\filesran\\trabalho.pptx","wb") as file:
                file.write(response1.content)

            print("recuperando arquivos")

        win32api.MessageBox(0, 'Alerta', 'Ransonware detectado')

    except (socket.gaierror, requests.exceptions.ConnectionError):
            
        #remover

        if os.path.isfile(f"{eula}\\iscas.txt") == True:

            with open(f"{eula}\\iscas.txt","r") as iscas:

                iscalinhas = iscas.readlines()

                iscas_usuario = []

                for i in range(len(iscalinhas)):
                    iscas_usuario.append(iscalinhas[i].replace("\n",""))

                for i in range(len(iscas_usuario)):  

                    while True:        
                        try:
                            os.mkdir(f"{iscas_usuario[i]}\\filesran")
                            break
                        except FileExistsError:
                            os.system(f'rmdir /S /Q "{iscas_usuario[i]}\\filesran"')
                            os.mkdir(f"{iscas_usuario[i]}\\filesran")
                            break   

                    os.system(f'copy "C:\\Program Files (x86)\\Backup\\contas.txt" "{iscas_usuario[i]}\\filesran\\contas.txt"')
                    os.system(f'copy "C:\\Program Files (x86)\\Backup\\money.docx" "{iscas_usuario[i]}\\filesran\\money.docx"')
                    os.system(f'copy "C:\\Program Files (x86)\\Backup\\senhas.pdf" "{iscas_usuario[i]}\\filesran\\senhas.pdf"')
                    os.system(f'copy "C:\\Program Files (x86)\\Backup\\trabalho.pptx" "{iscas_usuario[i]}\\filesran\\trabalho.pptx"')

                iscas_usuario.clear()
        else:
            pass  

        for i in conta:
            i = i.replace('\n','')

            while os.path.isdir(f"C:\\Users\\{i}\\Desktop\\filesran") == True:
                os.system(f"rmdir /S /Q C:\\Users\\{i}\\Desktop\\filesran")
                

            try:
                os.mkdir(f"C:\\Users\\{i}\\Desktop\\filesran")
                
            except FileExistsError:
                os.system(f"rmdir /S /Q C:\\Users\\{i}\\Desktop\\filesran")
                os.mkdir(f"C:\\Users\\{i}\\Desktop\\filesran")
                
            
            while True:
                try:
                    os.mkdir(f"C:\\Users\\{i}\\Documents\\filesran")
                    break
                except FileExistsError:
                    os.system(f"rmdir /S /Q C:\\Users\\{i}\\Documents\\filesran")
                    os.mkdir(f"C:\\Users\\{i}\\Documents\\filesran")
                    break

            while True:
                try:
                    os.mkdir(f"C:\\Users\\{i}\\Downloads\\filesran")
                    break
                except FileExistsError:
                    os.system(f"rmdir /S /Q C:\\Users\\{i}\\Downloads\\filesran")
                    os.mkdir(f"C:\\Users\\{i}\\Downloads\\filesran")
                    break


            os.system(f'copy "C:\\Program Files (x86)\\Backup\\contas.txt" "C:\\Users\\{i}\\Desktop\\filesran\\contas.txt"')
            os.system(f'copy "C:\\Program Files (x86)\\Backup\\money.docx" "C:\\Users\\{i}\\Desktop\\filesran\\money.docx"')
            os.system(f'copy "C:\\Program Files (x86)\\Backup\\senhas.pdf" "C:\\Users\\{i}\\Desktop\\filesran\\senhas.pdf"')
            os.system(f'copy "C:\\Program Files (x86)\\Backup\\trabalho.pptx" "C:\\Users\\{i}\\Desktop\\filesran\\trabalho.pptx"')




            os.system(f'copy "C:\\Program Files (x86)\\Backup\\contas.txt" "C:\\Users\\{i}\\Documents\\filesran\\contas.txt"')
            os.system(f'copy "C:\\Program Files (x86)\\Backup\\money.docx" "C:\\Users\\{i}\\Documents\\filesran\\money.docx"')
            os.system(f'copy "C:\\Program Files (x86)\\Backup\\senhas.pdf" "C:\\Users\\{i}\\Documents\\filesran\\senhas.pdf"')
            os.system(f'copy "C:\\Program Files (x86)\\Backup\\trabalho.pptx" "C:\\Users\\{i}\\Documents\\filesran\\trabalho.pptx"')                


            os.system(f'copy "C:\\Program Files (x86)\\Backup\\contas.txt" "C:\\Users\\{i}\\Downloads\\filesran\\contas.txt"')
            os.system(f'copy "C:\\Program Files (x86)\\Backup\\money.docx" "C:\\Users\\{i}\\Downloads\\filesran\\money.docx"')
            os.system(f'copy "C:\\Program Files (x86)\\Backup\\senhas.pdf" "C:\\Users\\{i}\\Downloads\\filesran\\senhas.pdf"')
            os.system(f'copy "C:\\Program Files (x86)\\Backup\\trabalho.pptx" "C:\\Users\\{i}\\Downloads\\filesran\\trabalho.pptx"')


        os.system("cls")
        win32api.MessageBox(0, 'Alerta', 'Ransonware detectado')
    


#----------------------- Segunda fun????o ---------------------------#



def recuperar_arquivos(usuariofinal):



    url = "https://github.com/Fabrizzio53/Dummy/raw/main/senhas.pdf"
    url1 = "https://github.com/Fabrizzio53/Dummy/raw/main/trabalho.pptx"
    url2 = "https://github.com/Fabrizzio53/Dummy/raw/main/money.docx"
    url3 = "https://github.com/Fabrizzio53/Dummy/raw/main/contas.txt"

    try:

        if os.path.isfile(f"{eula}\\iscas.txt") == True:
            with open(f"{eula}\\iscas.txt","r") as iscas:


                url = "https://github.com/Fabrizzio53/Dummy/raw/main/senhas.pdf"
                url1 = "https://github.com/Fabrizzio53/Dummy/raw/main/trabalho.pptx"
                url2 = "https://github.com/Fabrizzio53/Dummy/raw/main/money.docx"
                url3 = "https://github.com/Fabrizzio53/Dummy/raw/main/contas.txt" 

                socket.gethostbyname("www.google.com.br")
                response = requests.get(url)
                response1 = requests.get(url1)
                response2 = requests.get(url2)
                response3 = requests.get(url3)

                iscalinhas = iscas.readlines()

                iscas_usuario = []

                for i in range(len(iscalinhas)):
                    iscas_usuario.append(iscalinhas[i].replace("\n",""))

                for i in range(len(iscas_usuario)): 

                    try:
                        with open(f"{iscas_usuario[i]}\\filesran\\checar.txt","w") as e:
                            e.write("Checado")
                            pass
                        while True:
                            try:
                                os.mkdir(f"{iscas_usuario[i]}\\filesran")
                                break
                            except FileExistsError:
                                os.system(f'rmdir /S /Q "{iscas_usuario[i]}\\filesran"')
                                os.mkdir(f"{iscas_usuario[i]}\\filesran")
                                break                      

                        with open(f"{iscas_usuario[i]}\\filesran\\contas.txt","wb") as file:
                            lista.append(f"{iscas_usuario[i]}\\filesran\\contas.txt")
                            file.write(response3.content)

                        with open(f"{iscas_usuario[i]}\\filesran\\money.docx","wb") as file:

                            lista.append(f"{iscas_usuario[i]}\\filesran\\money.docx")
                            file.write(response2.content)


                        with open(f"{iscas_usuario[i]}\\filesran\\senhas.pdf","wb") as file:
                            
                            lista.append(f"{iscas_usuario[i]}\\filesran\\senhas.pdf")
                            file.write(response.content)

                        with open(f"{iscas_usuario[i]}\\filesran\\trabalho.pptx","wb") as file:
                            
                            lista.append(f"{iscas_usuario[i]}\\filesran\\trabalho.pptx")
                            file.write(response1.content)

                    except PermissionError:
                        continue

                iscas_usuario.clear()
        else:
            pass    

        response = requests.get(url)
        response1 = requests.get(url1)
        response2 = requests.get(url2)
        response3 = requests.get(url3)

        #remover

        os.system(f"rmdir /S /Q C:\\Users\\{usuariofinal}\\Desktop\\filesran")
        os.system(f"rmdir /S /Q C:\\Users\\{usuariofinal}\\Documents\\filesran")
        os.system(f"rmdir /S /Q C:\\Users\\{usuariofinal}\\Downloads\\filesran")

        while os.path.isdir(f"C:\\Users\\{usuariofinal}\\Desktop\\filesran") == True:
            os.system(f"rmdir /S /Q C:\\Users\\{usuariofinal}\\Desktop\\filesran")
            

        try:
            os.mkdir(f"C:\\Users\\{usuariofinal}\\Desktop\\filesran")
            
        except FileExistsError:
            os.system(f"rmdir /S /Q C:\\Users\\{usuariofinal}\\Desktop\\filesran")
            os.mkdir(f"C:\\Users\\{usuariofinal}\\Desktop\\filesran")
            
        
        while True:
            try:
                os.mkdir(f"C:\\Users\\{usuariofinal}\\Documents\\filesran")
                break
            except FileExistsError:
                os.system(f"rmdir /S /Q C:\\Users\\{usuariofinal}\\Documents\\filesran")
                os.mkdir(f"C:\\Users\\{usuariofinal}\\Documents\\filesran")
                break

        while True:
            try:
                os.mkdir(f"C:\\Users\\{usuariofinal}\\Downloads\\filesran")
                break
            except FileExistsError:
                os.system(f"rmdir /S /Q C:\\Users\\{usuariofinal}\\Downloads\\filesran")
                os.mkdir(f"C:\\Users\\{usuariofinal}\\Downloads\\filesran")
                break

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

    except (socket.gaierror, requests.exceptions.ConnectionError):

        if os.path.isfile(f"{eula}\\iscas.txt") == True:
            with open(f"{eula}\\iscas.txt","r") as iscas:
                iscalinhas = iscas.readlines()

                iscas_usuario = []

                for i in range(len(iscalinhas)):
                    iscas_usuario.append(iscalinhas[i].replace("\n",""))

                for i in range(len(iscas_usuario)): 

                    try:
                        with open(f"{iscas_usuario[i]}\\filesran\\checar.txt","w") as e:
                            e.write("Checado")

                        while True:
                            try:
                                os.mkdir(f"{iscas_usuario[i]}\\filesran")
                                break
                            except FileExistsError:
                                os.system(f'rmdir /S /Q "{iscas_usuario[i]}\\filesran"')
                                os.mkdir(f"{iscas_usuario[i]}\\filesran")
                                break                      

                        os.system(f'copy "C:\\Program Files (x86)\\Backup\\contas.txt" "{iscas_usuario[i]}\\filesran\\contas.txt"')
                        os.system(f'copy "C:\\Program Files (x86)\\Backup\\money.docx" "{iscas_usuario[i]}\\filesran\\money.docx"')
                        os.system(f'copy "C:\\Program Files (x86)\\Backup\\senhas.pdf" "{iscas_usuario[i]}\\filesran\\senhas.pdf"')
                        os.system(f'copy "C:\\Program Files (x86)\\Backup\\trabalho.pptx" "{iscas_usuario[i]}\\filesran\\trabalho.pptx"')

                    except PermissionError:
                        continue

                iscas_usuario.clear()
        else:
            pass
            
        os.system(f"rmdir /S /Q C:\\Users\\{usuariofinal}\\Desktop\\filesran")
        os.system(f"rmdir /S /Q C:\\Users\\{usuariofinal}\\Documents\\filesran")
        os.system(f"rmdir /S /Q C:\\Users\\{usuariofinal}\\Downloads\\filesran")

        while os.path.isdir(f"C:\\Users\\{usuariofinal}\\Desktop\\filesran") == True:
            os.system(f"rmdir /S /Q C:\\Users\\{usuariofinal}\\Desktop\\filesran")
            

        try:
            os.mkdir(f"C:\\Users\\{usuariofinal}\\Desktop\\filesran")
            
        except FileExistsError:
            os.system(f"rmdir /S /Q C:\\Users\\{usuariofinal}\\Desktop\\filesran")
            os.mkdir(f"C:\\Users\\{usuariofinal}\\Desktop\\filesran")
            
        
        while True:
            try:
                os.mkdir(f"C:\\Users\\{usuariofinal}\\Documents\\filesran")
                break
            except FileExistsError:
                os.system(f"rmdir /S /Q C:\\Users\\{usuariofinal}\\Documents\\filesran")
                os.mkdir(f"C:\\Users\\{usuariofinal}\\Documents\\filesran")
                break

        while True:
            try:
                os.mkdir(f"C:\\Users\\{usuariofinal}\\Downloads\\filesran")
                break
            except FileExistsError:
                os.system(f"rmdir /S /Q C:\\Users\\{usuariofinal}\\Downloads\\filesran")
                os.mkdir(f"C:\\Users\\{usuariofinal}\\Downloads\\filesran")
                break


        os.system(f'copy "C:\\Program Files (x86)\\Backup\\contas.txt" "C:\\Users\\{usuariofinal}\\Desktop\\filesran\\contas.txt"')
        os.system(f'copy "C:\\Program Files (x86)\\Backup\\money.docx" "C:\\Users\\{usuariofinal}\\Desktop\\filesran\\money.docx"')
        os.system(f'copy "C:\\Program Files (x86)\\Backup\\senhas.pdf" "C:\\Users\\{usuariofinal}\\Desktop\\filesran\\senhas.pdf"')
        os.system(f'copy "C:\\Program Files (x86)\\Backup\\trabalho.pptx" "C:\\Users\\{usuariofinal}\\Desktop\\filesran\\trabalho.pptx"')




        os.system(f'copy "C:\\Program Files (x86)\\Backup\\contas.txt" "C:\\Users\\{usuariofinal}\\Documents\\filesran\\contas.txt"')
        os.system(f'copy "C:\\Program Files (x86)\\Backup\\money.docx" "C:\\Users\\{usuariofinal}\\Documents\\filesran\\money.docx"')
        os.system(f'copy "C:\\Program Files (x86)\\Backup\\senhas.pdf" "C:\\Users\\{usuariofinal}\\Documents\\filesran\\senhas.pdf"')
        os.system(f'copy "C:\\Program Files (x86)\\Backup\\trabalho.pptx" "C:\\Users\\{usuariofinal}\\Documents\\filesran\\trabalho.pptx"')                


        os.system(f'copy "C:\\Program Files (x86)\\Backup\\contas.txt" "C:\\Users\\{usuariofinal}\\Downloads\\filesran\\contas.txt"')
        os.system(f'copy "C:\\Program Files (x86)\\Backup\\money.docx" "C:\\Users\\{usuariofinal}\\Downloads\\filesran\\money.docx"')
        os.system(f'copy "C:\\Program Files (x86)\\Backup\\senhas.pdf" "C:\\Users\\{usuariofinal}\\Downloads\\filesran\\senhas.pdf"')
        os.system(f'copy "C:\\Program Files (x86)\\Backup\\trabalho.pptx" "C:\\Users\\{usuariofinal}\\Downloads\\filesran\\trabalho.pptx"')

    os.system("cls")
    win32api.MessageBox(0, 'Alerta', 'Ransonware detectado')







#----------------------------In??cio do programa----------------------------#



with open("C:\\backupconfig\\contas.txt","r") as conta:
    conta = conta.readlines()

with open("C:\\backupconfig\\logs_antimalware.txt","a") as data_log_anti_malware:
    today = date.today()

    d1 = today.strftime("_%d_%m_%Y")

    data_log_anti_malware.write("=======================================\n")
    data_log_anti_malware.write(f"{d1}\n")
    data_log_anti_malware.write("=======================================\n")

for i in range(len(conta)):
    usuarios.append(str(conta[i]).replace("\n",""))

for i in range(len(usuarios)):

    if os.getlogin() == usuarios[i]:
        usuariofinal = usuarios[i]
        break


#--------------------Checagem de n??vel--------------------------------#   

if usuariofinal == "":
    print("Usu??rio n??o autorizado")
    quit()




#--------------------Programa caso n??o seja administrador------------------------#

if usuariofinal != "Administrador":

    #--------------------------Forma????o de hash-------------------------------------#

    if os.path.isfile("C:\\backupconfig\\iscas.txt") == True:

        with open("C:\\backupconfig\\iscas.txt","r") as iscas:
            iscas = iscas.readlines()

            for i in iscas:
                i = i.replace('\n','')
                try:
                    with open(f"{i}\\filesran\\checar.txt","w") as e:
                        lista.append(f"{i}\\filesran\\contas.txt")
                        lista.append(f"{i}\\filesran\\money.docx")
                        lista.append(f"{i}\\filesran\\senhas.pdf")
                        lista.append(f"{i}\\filesran\\trabalho.pptx") 

                except PermissionError:
                    continue

 

    else:
        pass    

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

    #with open(f"C:\\backupconfig\\{usuariofinal}\\hash_original.txt","r") as config:
        #linhas = config.readlines()

    with open(f"C:\\backupconfig\\{usuariofinal}\\hash_original.txt","r") as config:
        linhas = config.readlines()
        for i in range(len(linhas)):
            lista2.append(linhas[i])


    #------------------------In??co da an??lise de comportamento-----------------------------#

    while True:


        sleep(1) 
#------------------------Checagem de hash----------------------------------------------#

        for i in range(len(lista)):
            file_hash = hashlib.md5()
            try: 
                with open(lista[i], 'rb') as f: 
                    fb = f.read(BLOCK_SIZE) 
                    while len(fb) > 0: 
                        file_hash.update(fb) 
                        fb = f.read(BLOCK_SIZE) 

                    hashed = file_hash.hexdigest()

#-------------------------An??lise se o hash ?? igual-----------------------------------#

                    if hashed == "c9ea7603f3226a21d2d45943d1e6ed69" or hashed == "0cc4c614b06fff2b5883ecbbea77c06a" or hashed == "d4e4a6870de35f02025745cd527ebdf1" or hashed == "e93a0f540a9c78d7ab34a3f74c5ec145":
                        continue


#-------------------------Matando o processo------------------------------------------#


#-----------------------------Tempo---------------------------------------------------#
                    else:
                        agora = datetime.now()            
                                    
                        for proc in psutil.process_iter():
                            if str(proc.name()) == "msedge.exe" or str(proc.name()) == "System Idle Process" or str(proc.name()) == "System" or str(proc.name()) == "python.exe" or str(proc.name()) == "smartscreen.exe" or str(proc.name()) == "RuntimeBroker.exe" or str(proc.name()) == "SearchFilterHost.exe" or str(proc.name()) == "backgroundTaskHost.exe" or str(proc.name()) == "SearchProtocolHost.exe" or str(proc.name()) == "Registry" or str(proc.name()) == "svchost.exe" or str(proc.name()) == "wininit.exe" or str(proc.name()) == "OneDrive.exe" or str(proc.name()) == "powershell.exe" or str(proc.name()) == "Code.exe" or str(proc.name()) == "WmiPrvSE.exe" or str(proc.name()) == "dllhost.exe" or str(proc.name()) == "UserOOBEBroker.exe" or str(proc.name()) == "FileCoAuth.exe" or str(proc.name()) == "audiodg.exe" or str(proc.name()) == "taskhostw.exe" or str(proc.name()) == "SearchApp.exe" or str(proc.name()) == "cmd.exe" or str(proc.name()) == "Microsoft.Photos.exe" or str(proc.name()) == "HxTsr.exe" or str(proc.name()) == "conhost.exe" or str(proc.name()) == "TiWorker.exe" or str(proc.name()) == "checagem_de_hash.exe" or str(proc.name()) == "WMIADAP.exe" or str(proc.name()) == "ShellExperienceHost.exe" or str(proc.name()) == "TrustedInstaller.exe" or str(proc.name()) == "ctfmon.exe" or str(proc.name()) == "MoUsoCoreWorker.exe" or str(proc.name()) == "SearchIndexer.exe" or str(proc.name()) == "explorer.exe" or str(proc.name()) == "Cortana.exe" or str(proc.name()) == "TextInputHost.exe" or str(proc.name()) == "sihost.exe" or str(proc.name()) == "ApplicationFrameHost.exe":
                                continue
                
                            else:
                                horasprocessos = int(time.strftime("%H",time.localtime(proc.create_time())))*3600
                                minutoprocessos = int(time.strftime("%M",time.localtime(proc.create_time())))*60
                                segundossprocessos = int(time.strftime("%S",time.localtime(proc.create_time())))
                                totalprocessos = horasprocessos + minutoprocessos + segundossprocessos

                                horaatual = int(agora.strftime("%H"))*3600
                                minutoatual = int(agora.strftime("%M"))*60
                                segundosatual = int(agora.strftime("%S"))

                                totalagora = horaatual + minutoatual + segundosatual
                                

                                if abs(totalagora - totalprocessos) > 320:
                                    continue
                                else:
                                    try:
                                        os.kill(proc.pid, signal.SIGTERM)
                                        print("matei o processo: ", proc.name())
                                        
                                        with open("C:\\backupconfig\\logs_antimalware.txt","a") as logs:
                                            logs.write(f"=======================\n")
                                            logs.write(f"Hash mudado no arquivo:{lista[i]}\n")
                                            logs.write(f"Hash original:{lista2[i]}\n")
                                            logs.write(f"Hash alterado:{hashed}\n")
                                            logs.write(f"Hor??rio:{int(horaatual/3600)}:{int(minutoatual/60)}:{int(segundosatual)}\n")
                                            logs.write(f"processo: {proc.name()}\n")
                                    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess, PermissionError):
                                        continue
                            
#----------------------------------------------Uso de CPU------------------------------------------------#                                           
                            
                        for repetir in range(0,3):
                            for proc2 in psutil.process_iter():
                                if str(proc2.name()) == "msedge.exe" or str(proc2.name()) == "TextInputHost.exe" or str(proc2.name()) == "SecurityHealthService.exe" or str(proc2.name()) == "MpCopyAccelerator.exe" or str(proc2.name()) == "PhoneExperienceHost.exe" or str(proc2.name()) == "SecurityHealthSystray.exe" or str(proc2.name()) == "StartMenuExperienceHost.exe" or str(proc2.name()) == "SearchIndexer.exe" or str(proc2.name()) == "NisSrv.exe" or str(proc2.name()) == "sihost.exe" or str(proc2.name()) == "MsMpEng.exe" or str(proc2.name()) == "MemCompression" or str(proc2.name()) == "ShellExperienceHost.exe" or str(proc2.name()) == "VBoxTray.exe" or str(proc2.name()) == "fontdrvhost.exe" or str(proc2.name()) == "services.exe" or str(proc2.name()) == "winlogon.exe" or str(proc2.name()) == "ctfmon.exe" or str(proc2.name()) == "explorer.exe" or str(proc2.name()) == "SgrmBroker.exe" or str(proc2.name()) == "spoolsv.exe" or str(proc2.name()) == "lsass.exe" or str(proc2.name()) == "csrss.exe" or str(proc2.name()) == "smss.exe" or str(proc2.name()) == "dwm.exe" or str(proc2.name()) == "System Idle Process" or str(proc2.name()) == "System" or str(proc2.name()) == "smartscreen.exe" or str(proc2.name()) == "RuntimeBroker.exe" or str(proc2.name()) == "SearchFilterHost.exe" or str(proc2.name()) == "backgroundTaskHost.exe" or str(proc2.name()) == "SearchProtocolHost.exe" or str(proc2.name()) == "Registry" or str(proc2.name()) == "svchost.exe" or str(proc2.name()) == "wininit.exe" or str(proc2.name()) == "OneDrive.exe" or str(proc2.name()) == "powershell.exe" or str(proc2.name()) == "Code.exe" or str(proc2.name()) == "WmiPrvSE.exe" or str(proc2.name()) == "dllhost.exe" or str(proc2.name()) == "UserOOBEBroker.exe" or str(proc2.name()) == "FileCoAuth.exe" or str(proc2.name()) == "audiodg.exe" or str(proc2.name()) == "taskhostw.exe" or str(proc2.name()) == "SearchApp.exe" or str(proc2.name()) == "cmd.exe" or str(proc2.name()) == "Microsoft.Photos.exe" or str(proc2.name()) == "HxTsr.exe" or str(proc2.name()) == "conhost.exe" or str(proc2.name()) == "Cortana.exe" or str(proc2.name()) == "checagem_de_hash.exe" or str(proc.name()) == "WMIADAP.exe":
                                    continue

                                else: 
                                    if proc2.cpu_percent(interval=0.4) > 20:
                                        try:
                                            os.kill(proc2.pid, signal.SIGTERM)
                                            with open("C:\\backupconfig\\logs_antimalware.txt","a") as logs:
                                                logs.write(f"=======================\n")
                                                logs.write(f"Hash mudado no arquivo:{lista[i]}\n")
                                                logs.write(f"Hash original:{lista2[i]}\n")
                                                logs.write(f"Hash alterado:{hashed}\n")
                                                logs.write(f"Hor??rio:{int(horaatual/3600)}:{int(minutoatual/60)}:{int(segundosatual)}\n")
                                                logs.write(f"processo: {proc2.name()}\n")
                                                logs.write(f"processo com muito uso na cpu\n")
                                        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess, PermissionError):
                                            continue                                                
                                            
                                    else:
                                        continue                           
                                        
                        f.close()
                        recuperar_arquivos(usuariofinal)
                                

            except FileNotFoundError:
#-----------------------------Tempo---------------------------------------------------#
                        agora = datetime.now()
                        for proc in psutil.process_iter():
                            if str(proc.name()) == "msedge.exe" or str(proc.name()) == "System Idle Process" or str(proc.name()) == "System" or str(proc.name()) == "python.exe" or str(proc.name()) == "smartscreen.exe" or str(proc.name()) == "RuntimeBroker.exe" or str(proc.name()) == "SearchFilterHost.exe" or str(proc.name()) == "backgroundTaskHost.exe" or str(proc.name()) == "SearchProtocolHost.exe" or str(proc.name()) == "Registry" or str(proc.name()) == "svchost.exe" or str(proc.name()) == "wininit.exe" or str(proc.name()) == "OneDrive.exe" or str(proc.name()) == "powershell.exe" or str(proc.name()) == "Code.exe" or str(proc.name()) == "WmiPrvSE.exe" or str(proc.name()) == "dllhost.exe" or str(proc.name()) == "UserOOBEBroker.exe" or str(proc.name()) == "FileCoAuth.exe" or str(proc.name()) == "audiodg.exe" or str(proc.name()) == "taskhostw.exe" or str(proc.name()) == "SearchApp.exe" or str(proc.name()) == "cmd.exe" or str(proc.name()) == "Microsoft.Photos.exe" or str(proc.name()) == "HxTsr.exe" or str(proc.name()) == "conhost.exe" or str(proc.name()) == "TiWorker.exe" or str(proc.name()) == "checagem_de_hash.exe" or str(proc.name()) == "WMIADAP.exe" or str(proc.name()) == "ShellExperienceHost.exe" or str(proc.name()) == "TrustedInstaller.exe" or str(proc.name()) == "ctfmon.exe" or str(proc.name()) == "MoUsoCoreWorker.exe" or str(proc.name()) == "SearchIndexer.exe" or str(proc.name()) == "explorer.exe" or str(proc.name()) == "Cortana.exe" or str(proc.name()) == "TextInputHost.exe" or str(proc.name()) == "sihost.exe" or str(proc.name()) == "ApplicationFrameHost.exe":
                                continue

                            else:

                                horasprocessos = int(time.strftime("%H",time.localtime(proc.create_time())))*3600
                                minutoprocessos = int(time.strftime("%M",time.localtime(proc.create_time())))*60
                                segundossprocessos = int(time.strftime("%S",time.localtime(proc.create_time())))
                                totalprocessos = horasprocessos + minutoprocessos + segundossprocessos

                                horaatual = int(agora.strftime("%H"))*3600
                                minutoatual = int(agora.strftime("%M"))*60
                                segundosatual = int(agora.strftime("%S"))

                                totalagora = horaatual + minutoatual + segundosatual
                                

                                if abs(totalagora - totalprocessos) > 320:
                                    continue
                                else:
                                    try:
                                        os.kill(proc.pid, signal.SIGTERM)
                                        print("matei o processo: ", proc.name())
                                        with open("C:\\backupconfig\\logs_antimalware.txt","a") as logs:
                                            logs.write(f"=======================================\n")
                                            logs.write(f"Hash mudado no arquivo e extens??o modificada:{lista[i]}\n")
                                            logs.write(f"Hash original:{lista2[i]}\n")
                                            logs.write(f"Hash alterado:{hashed}\n")
                                            logs.write(f"Hor??rio:{int(horaatual/3600)}:{int(minutoatual/60)}:{int(segundosatual)}\n")
                                            logs.write(f"processo: {proc.name()}\n")
                                    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess, PermissionError):
                                        continue

                #----------------------------------------------Uso de CPU------------------------------------------------# 

                        for repetir in range(0,3):
                            for proc2 in psutil.process_iter():
                                if str(proc2.name()) == "msedge.exe" or str(proc2.name()) == "TextInputHost.exe" or str(proc2.name()) == "SecurityHealthService.exe" or str(proc2.name()) == "MpCopyAccelerator.exe" or str(proc2.name()) == "PhoneExperienceHost.exe" or str(proc2.name()) == "SecurityHealthSystray.exe" or str(proc2.name()) == "StartMenuExperienceHost.exe" or str(proc2.name()) == "SearchIndexer.exe" or str(proc2.name()) == "NisSrv.exe" or str(proc2.name()) == "sihost.exe" or str(proc2.name()) == "MsMpEng.exe" or str(proc2.name()) == "MemCompression" or str(proc2.name()) == "ShellExperienceHost.exe" or str(proc2.name()) == "VBoxTray.exe" or str(proc2.name()) == "fontdrvhost.exe" or str(proc2.name()) == "services.exe" or str(proc2.name()) == "winlogon.exe" or str(proc2.name()) == "ctfmon.exe" or str(proc2.name()) == "explorer.exe" or str(proc2.name()) == "SgrmBroker.exe" or str(proc2.name()) == "spoolsv.exe" or str(proc2.name()) == "lsass.exe" or str(proc2.name()) == "csrss.exe" or str(proc2.name()) == "smss.exe" or str(proc2.name()) == "dwm.exe" or str(proc2.name()) == "System Idle Process" or str(proc2.name()) == "System" or str(proc2.name()) == "smartscreen.exe" or str(proc2.name()) == "RuntimeBroker.exe" or str(proc2.name()) == "SearchFilterHost.exe" or str(proc2.name()) == "backgroundTaskHost.exe" or str(proc2.name()) == "SearchProtocolHost.exe" or str(proc2.name()) == "Registry" or str(proc2.name()) == "svchost.exe" or str(proc2.name()) == "wininit.exe" or str(proc2.name()) == "OneDrive.exe" or str(proc2.name()) == "powershell.exe" or str(proc2.name()) == "Code.exe" or str(proc2.name()) == "WmiPrvSE.exe" or str(proc2.name()) == "dllhost.exe" or str(proc2.name()) == "UserOOBEBroker.exe" or str(proc2.name()) == "FileCoAuth.exe" or str(proc2.name()) == "audiodg.exe" or str(proc2.name()) == "taskhostw.exe" or str(proc2.name()) == "SearchApp.exe" or str(proc2.name()) == "cmd.exe" or str(proc2.name()) == "Microsoft.Photos.exe" or str(proc2.name()) == "HxTsr.exe" or str(proc2.name()) == "conhost.exe" or str(proc2.name()) == "Cortana.exe" or str(proc2.name()) == "checagem_de_hash.exe":
                                    continue

                                else: 
                                    if proc2.cpu_percent(interval=0.4) > 20:
                                        try:
                                            os.kill(proc2.pid, signal.SIGTERM)
                                            with open("C:\\backupconfig\\logs_antimalware.txt","a") as logs:
                                                logs.write(f"=======================================\n")
                                                logs.write(f"Hash mudado no arquivo e extens??o modificada:{lista[i]}\n")
                                                logs.write(f"Hash original:{lista2[i]}\n")
                                                logs.write(f"Hash alterado:{hashed}\n")
                                                logs.write(f"Hor??rio:{int(horaatual/3600)}:{int(minutoatual/60)}:{int(segundosatual)}\n")
                                                logs.write(f"processo: {proc2.name()}\n")
                                                logs.write(f"processo com muito uso na cpu\n")
                                        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess, PermissionError):
                                            continue                                        
                                    else:
                                        continue

                            

                        f.close()
                        recuperar_arquivos(usuariofinal)
                                          

                                        

            except PermissionError:
                continue    
           

#------------------------------------Programa caso seja o administrador-----------------------#


else:
    with open("C:\\backupconfig\\contas.txt","r") as conta:
        conta = conta.readlines()


 #--------------------------Forma????o de hash-------------------------------------#

    if os.path.isfile("C:\\backupconfig\\iscas.txt") == True:

        with open("C:\\backupconfig\\iscas.txt","r") as iscas:
            iscas = iscas.readlines()

            for i in iscas:
                i = i.replace('\n','')
                lista.append(f"{i}\\filesran\\contas.txt")
                lista.append(f"{i}\\filesran\\money.docx")
                lista.append(f"{i}\\filesran\\senhas.pdf")
                lista.append(f"{i}\\filesran\\trabalho.pptx")  

    else:
        pass 

    for i in conta:

        i = i.replace('\n','')

        lista.append(f"C:\\Users\\{i}\\Desktop\\filesran\\contas.txt")
        lista.append(f"C:\\Users\\{i}\\Desktop\\filesran\\money.docx")
        lista.append(f"C:\\Users\\{i}\\Desktop\\filesran\\senhas.pdf")
        lista.append(f"C:\\Users\\{i}\\Desktop\\filesran\\trabalho.pptx")

        #=======================================#

        lista.append(f"C:\\Users\\{i}\\Documents\\filesran\\contas.txt")
        lista.append(f"C:\\Users\\{i}\\Documents\\filesran\\money.docx")
        lista.append(f"C:\\Users\\{i}\\Documents\\filesran\\senhas.pdf")
        lista.append(f"C:\\Users\\{i}\\Documents\\filesran\\trabalho.pptx")


        #=========================================#


        lista.append(f"C:\\Users\\{i}\\Downloads\\filesran\\contas.txt")
        lista.append(f"C:\\Users\\{i}\\Downloads\\filesran\\money.docx")
        lista.append(f"C:\\Users\\{i}\\Downloads\\filesran\\senhas.pdf")
        lista.append(f"C:\\Users\\{i}\\Downloads\\filesran\\trabalho.pptx")

        with open(f"C:\\backupconfig\\{i}\\hash_original.txt","r") as config:
            linhas = config.readlines()
            for i in range(len(linhas)):
                lista2.append(linhas[i])

          

 #------------------------In??co da an??lise de comportamento-----------------------------#

    while True:

        sleep(1)
#------------------------Checagem de hash----------------------------------------------#



        for i in range(len(lista)):
            file_hash = hashlib.md5()
            try: 
                with open(lista[i], 'rb') as f: 
                    fb = f.read(BLOCK_SIZE) 
                    while len(fb) > 0: 
                        file_hash.update(fb) 
                        fb = f.read(BLOCK_SIZE) 

                    hashed = file_hash.hexdigest()


                    #str(lista2[i]).replace("\n","") 

#-------------------------An??lise se o hash ?? igual-----------------------------------#
                    if hashed == "c9ea7603f3226a21d2d45943d1e6ed69" or hashed == "0cc4c614b06fff2b5883ecbbea77c06a" or hashed == "d4e4a6870de35f02025745cd527ebdf1" or hashed == "e93a0f540a9c78d7ab34a3f74c5ec145":
                        continue


#-------------------------Matando o processo------------------------------------------#


#-----------------------------Tempo---------------------------------------------------#
                    else:
                        agora = datetime.now()            
                                    
                        for proc in psutil.process_iter(): 
                            try:
                                if str(proc.name()) == "msedge.exe" or str(proc.name()) == "System Idle Process" or str(proc.name()) == "System" or str(proc.name()) == "python.exe" or str(proc.name()) == "smartscreen.exe" or str(proc.name()) == "RuntimeBroker.exe" or str(proc.name()) == "SearchFilterHost.exe" or str(proc.name()) == "backgroundTaskHost.exe" or str(proc.name()) == "SearchProtocolHost.exe" or str(proc.name()) == "Registry" or str(proc.name()) == "svchost.exe" or str(proc.name()) == "wininit.exe" or str(proc.name()) == "OneDrive.exe" or str(proc.name()) == "powershell.exe" or str(proc.name()) == "Code.exe" or str(proc.name()) == "WmiPrvSE.exe" or str(proc.name()) == "dllhost.exe" or str(proc.name()) == "UserOOBEBroker.exe" or str(proc.name()) == "FileCoAuth.exe" or str(proc.name()) == "audiodg.exe" or str(proc.name()) == "taskhostw.exe" or str(proc.name()) == "SearchApp.exe" or str(proc.name()) == "cmd.exe" or str(proc.name()) == "Microsoft.Photos.exe" or str(proc.name()) == "HxTsr.exe" or str(proc.name()) == "conhost.exe" or str(proc.name()) == "TiWorker.exe" or str(proc.name()) == "checagem_de_hash.exe" or str(proc.name()) == "WMIADAP.exe" or str(proc.name()) == "ShellExperienceHost.exe" or str(proc.name()) == "TrustedInstaller.exe" or str(proc.name()) == "ctfmon.exe" or str(proc.name()) == "MoUsoCoreWorker.exe" or str(proc.name()) == "SearchIndexer.exe" or str(proc.name()) == "explorer.exe" or str(proc.name()) == "Cortana.exe" or str(proc.name()) == "TextInputHost.exe" or str(proc.name()) == "sihost.exe" or str(proc.name()) == "dwm.exe" or str(proc.name()) == "winlogon.exe" or str(proc.name()) == "lsass.exe" or str(proc.name()) == "fontdrvhost.exe" or str(proc.name()) == "VBoxService.exe" or str(proc.name()) == "spoolsv.exe" or str(proc.name()) == "dasHost.exe" or str(proc.name()) == "StartMenuExperienceHost.exe" or str(proc.name()) == "PhoneExperienceHost.exe" or str(proc.name()) == "SecurityHealthSystray.exe" or str(proc.name()) == "VBoxTray.exe" or str(proc.name()) == "ApplicationFrameHost.exe":
                                    continue
                    
                                else:
                                    horasprocessos = int(time.strftime("%H",time.localtime(proc.create_time())))*3600
                                    minutoprocessos = int(time.strftime("%M",time.localtime(proc.create_time())))*60
                                    segundossprocessos = int(time.strftime("%S",time.localtime(proc.create_time())))
                                    totalprocessos = horasprocessos + minutoprocessos + segundossprocessos

                                    horaatual = int(agora.strftime("%H"))*3600
                                    minutoatual = int(agora.strftime("%M"))*60
                                    segundosatual = int(agora.strftime("%S"))

                                    totalagora = horaatual + minutoatual + segundosatual
                                    

                                    if abs(totalagora - totalprocessos) > 320:
                                        continue
                                    else:
                                        try:
                                            os.kill(proc.pid, signal.SIGTERM)
                                            print("matei o processo: ", proc.name())
                                            
                                            with open("C:\\backupconfig\\logs_antimalware.txt","a") as logs:
                                                logs.write(f"=======================\n")
                                                logs.write(f"Hash mudado no arquivo:{lista[i]}\n")
                                                logs.write(f"Hash original:{lista2[i]}\n")
                                                logs.write(f"Hash alterado:{hashed}\n")
                                                logs.write(f"Hor??rio:{int(horaatual/3600)}:{int(minutoatual/60)}:{int(segundosatual)}\n")
                                                logs.write(f"processo: {proc.name()}\n")
                                        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess, PermissionError):
                                            continue
                            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess, PermissionError):
                                continue  
                            
#----------------------------------------------Uso de CPU------------------------------------------------#                                           
                            
                        for repetir in range(0,3):
                            try:
                                for proc2 in psutil.process_iter():
                                    if str(proc2.name()) == "msedge.exe" or str(proc2.name()) == "TextInputHost.exe" or str(proc2.name()) == "SecurityHealthService.exe" or str(proc2.name()) == "MpCopyAccelerator.exe" or str(proc2.name()) == "PhoneExperienceHost.exe" or str(proc2.name()) == "SecurityHealthSystray.exe" or str(proc2.name()) == "StartMenuExperienceHost.exe" or str(proc2.name()) == "SearchIndexer.exe" or str(proc2.name()) == "NisSrv.exe" or str(proc2.name()) == "sihost.exe" or str(proc2.name()) == "MsMpEng.exe" or str(proc2.name()) == "MemCompression" or str(proc2.name()) == "ShellExperienceHost.exe" or str(proc2.name()) == "VBoxTray.exe" or str(proc2.name()) == "fontdrvhost.exe" or str(proc2.name()) == "services.exe" or str(proc2.name()) == "winlogon.exe" or str(proc2.name()) == "ctfmon.exe" or str(proc2.name()) == "explorer.exe" or str(proc2.name()) == "SgrmBroker.exe" or str(proc2.name()) == "spoolsv.exe" or str(proc2.name()) == "lsass.exe" or str(proc2.name()) == "csrss.exe" or str(proc2.name()) == "smss.exe" or str(proc2.name()) == "dwm.exe" or str(proc2.name()) == "System Idle Process" or str(proc2.name()) == "System" or str(proc2.name()) == "smartscreen.exe" or str(proc2.name()) == "RuntimeBroker.exe" or str(proc2.name()) == "SearchFilterHost.exe" or str(proc2.name()) == "backgroundTaskHost.exe" or str(proc2.name()) == "SearchProtocolHost.exe" or str(proc2.name()) == "Registry" or str(proc2.name()) == "svchost.exe" or str(proc2.name()) == "wininit.exe" or str(proc2.name()) == "OneDrive.exe" or str(proc2.name()) == "powershell.exe" or str(proc2.name()) == "Code.exe" or str(proc2.name()) == "WmiPrvSE.exe" or str(proc2.name()) == "dllhost.exe" or str(proc2.name()) == "UserOOBEBroker.exe" or str(proc2.name()) == "FileCoAuth.exe" or str(proc2.name()) == "audiodg.exe" or str(proc2.name()) == "taskhostw.exe" or str(proc2.name()) == "SearchApp.exe" or str(proc2.name()) == "cmd.exe" or str(proc2.name()) == "Microsoft.Photos.exe" or str(proc2.name()) == "HxTsr.exe" or str(proc2.name()) == "conhost.exe" or str(proc2.name()) == "Cortana.exe" or str(proc2.name()) == "checagem_de_hash.exe" or str(proc.name()) == "WMIADAP.exe":
                                        continue

                                    else: 
                                        if proc2.cpu_percent(interval=0.5) > 20:
                                            try:
                                                os.kill(proc2.pid, signal.SIGTERM)
                                                with open("C:\\backupconfig\\logs_antimalware.txt","a") as logs:
                                                    logs.write(f"=======================\n")
                                                    logs.write(f"Hash mudado no arquivo:{lista[i]}\n")
                                                    logs.write(f"Hash original:{lista2[i]}\n")
                                                    logs.write(f"Hash alterado:{hashed}\n")
                                                    logs.write(f"Hor??rio:{int(horaatual/3600)}:{int(minutoatual/60)}:{int(segundosatual)}\n")
                                                    logs.write(f"processo: {proc2.name()}\n")
                                                    logs.write(f"processo com muito uso na cpu\n")
                                            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess, PermissionError):
                                                continue                                                
                                                
                                        else:
                                            continue     
                            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess, PermissionError):
                                continue                        
                                        
                        f.close()
                        recuperar_arquivos_adm()
                                

            except FileNotFoundError:
#-----------------------------Tempo---------------------------------------------------#
                        agora = datetime.now()
                        for proc in psutil.process_iter():
                            try:
                                if str(proc.name()) == "msedge.exe" or str(proc.name()) == "System Idle Process" or str(proc.name()) == "System" or str(proc.name()) == "python.exe" or str(proc.name()) == "smartscreen.exe" or str(proc.name()) == "RuntimeBroker.exe" or str(proc.name()) == "SearchFilterHost.exe" or str(proc.name()) == "backgroundTaskHost.exe" or str(proc.name()) == "SearchProtocolHost.exe" or str(proc.name()) == "Registry" or str(proc.name()) == "svchost.exe" or str(proc.name()) == "wininit.exe" or str(proc.name()) == "OneDrive.exe" or str(proc.name()) == "powershell.exe" or str(proc.name()) == "Code.exe" or str(proc.name()) == "WmiPrvSE.exe" or str(proc.name()) == "dllhost.exe" or str(proc.name()) == "UserOOBEBroker.exe" or str(proc.name()) == "FileCoAuth.exe" or str(proc.name()) == "audiodg.exe" or str(proc.name()) == "taskhostw.exe" or str(proc.name()) == "SearchApp.exe" or str(proc.name()) == "cmd.exe" or str(proc.name()) == "Microsoft.Photos.exe" or str(proc.name()) == "HxTsr.exe" or str(proc.name()) == "conhost.exe" or str(proc.name()) == "TiWorker.exe" or str(proc.name()) == "checagem_de_hash.exe" or str(proc.name()) == "WMIADAP.exe" or str(proc.name()) == "ShellExperienceHost.exe" or str(proc.name()) == "TrustedInstaller.exe" or str(proc.name()) == "ctfmon.exe" or str(proc.name()) == "MoUsoCoreWorker.exe" or str(proc.name()) == "SearchIndexer.exe" or str(proc.name()) == "explorer.exe" or str(proc.name()) == "Cortana.exe" or str(proc.name()) == "TextInputHost.exe" or str(proc.name()) == "sihost.exe" or str(proc.name()) == "dwm.exe" or str(proc.name()) == "winlogon.exe" or str(proc.name()) == "lsass.exe" or str(proc.name()) == "fontdrvhost.exe" or str(proc.name()) == "VBoxService.exe" or str(proc.name()) == "spoolsv.exe" or str(proc.name()) == "dasHost.exe" or str(proc.name()) == "StartMenuExperienceHost.exe" or str(proc.name()) == "PhoneExperienceHost.exe" or str(proc.name()) == "SecurityHealthSystray.exe" or str(proc.name()) == "VBoxTray.exe" or str(proc.name()) == "ApplicationFrameHost.exe":
                                    continue

                                else:

                                    horasprocessos = int(time.strftime("%H",time.localtime(proc.create_time())))*3600
                                    minutoprocessos = int(time.strftime("%M",time.localtime(proc.create_time())))*60
                                    segundossprocessos = int(time.strftime("%S",time.localtime(proc.create_time())))
                                    totalprocessos = horasprocessos + minutoprocessos + segundossprocessos

                                    horaatual = int(agora.strftime("%H"))*3600
                                    minutoatual = int(agora.strftime("%M"))*60
                                    segundosatual = int(agora.strftime("%S"))

                                    totalagora = horaatual + minutoatual + segundosatual
                                    

                                    if abs(totalagora - totalprocessos) > 320:
                                        continue
                                    else:
                                        try:
                                            os.kill(proc.pid, signal.SIGTERM)
                                            print("matei o processo: ", proc.name())
                                            with open("C:\\backupconfig\\logs_antimalware.txt","a") as logs:
                                                logs.write(f"=======================================\n")
                                                logs.write(f"Hash mudado no arquivo e extens??o modificada:{lista[i]}\n")
                                                logs.write(f"Hash original:{lista2[i]}\n")
                                                logs.write(f"Hash alterado:{hashed}\n")
                                                logs.write(f"Hor??rio:{int(horaatual/3600)}:{int(minutoatual/60)}:{int(segundosatual)}\n")
                                                logs.write(f"processo: {proc.name()}\n")
                                        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess, PermissionError):
                                            continue
                            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess, PermissionError):
                                continue  

                #----------------------------------------------Uso de CPU------------------------------------------------# 

                        for repetir in range(0,3):
                            try:
                                for proc2 in psutil.process_iter():
                                    if str(proc2.name()) == "msedge.exe" or str(proc2.name()) == "TextInputHost.exe" or str(proc2.name()) == "SecurityHealthService.exe" or str(proc2.name()) == "MpCopyAccelerator.exe" or str(proc2.name()) == "PhoneExperienceHost.exe" or str(proc2.name()) == "SecurityHealthSystray.exe" or str(proc2.name()) == "StartMenuExperienceHost.exe" or str(proc2.name()) == "SearchIndexer.exe" or str(proc2.name()) == "NisSrv.exe" or str(proc2.name()) == "sihost.exe" or str(proc2.name()) == "MsMpEng.exe" or str(proc2.name()) == "MemCompression" or str(proc2.name()) == "ShellExperienceHost.exe" or str(proc2.name()) == "VBoxTray.exe" or str(proc2.name()) == "fontdrvhost.exe" or str(proc2.name()) == "services.exe" or str(proc2.name()) == "winlogon.exe" or str(proc2.name()) == "ctfmon.exe" or str(proc2.name()) == "explorer.exe" or str(proc2.name()) == "SgrmBroker.exe" or str(proc2.name()) == "spoolsv.exe" or str(proc2.name()) == "lsass.exe" or str(proc2.name()) == "csrss.exe" or str(proc2.name()) == "smss.exe" or str(proc2.name()) == "dwm.exe" or str(proc2.name()) == "System Idle Process" or str(proc2.name()) == "System" or str(proc2.name()) == "smartscreen.exe" or str(proc2.name()) == "RuntimeBroker.exe" or str(proc2.name()) == "SearchFilterHost.exe" or str(proc2.name()) == "backgroundTaskHost.exe" or str(proc2.name()) == "SearchProtocolHost.exe" or str(proc2.name()) == "Registry" or str(proc2.name()) == "svchost.exe" or str(proc2.name()) == "wininit.exe" or str(proc2.name()) == "OneDrive.exe" or str(proc2.name()) == "powershell.exe" or str(proc2.name()) == "Code.exe" or str(proc2.name()) == "WmiPrvSE.exe" or str(proc2.name()) == "dllhost.exe" or str(proc2.name()) == "UserOOBEBroker.exe" or str(proc2.name()) == "FileCoAuth.exe" or str(proc2.name()) == "audiodg.exe" or str(proc2.name()) == "taskhostw.exe" or str(proc2.name()) == "SearchApp.exe" or str(proc2.name()) == "cmd.exe" or str(proc2.name()) == "Microsoft.Photos.exe" or str(proc2.name()) == "HxTsr.exe" or str(proc2.name()) == "conhost.exe" or str(proc2.name()) == "Cortana.exe" or str(proc2.name()) == "checagem_de_hash.exe":
                                        continue

                                    else: 
                                        if proc2.cpu_percent(interval=0.5) > 20:
                                            try:
                                                os.kill(proc2.pid, signal.SIGTERM)
                                                with open("C:\\backupconfig\\logs_antimalware.txt","a") as logs:
                                                    logs.write(f"=======================================\n")
                                                    logs.write(f"Hash mudado no arquivo e extens??o modificada:{lista[i]}\n")
                                                    logs.write(f"Hash original:{lista2[i]}\n")
                                                    logs.write(f"Hash alterado:{hashed}\n")
                                                    logs.write(f"Hor??rio:{int(horaatual/3600)}:{int(minutoatual/60)}:{int(segundosatual)}\n")
                                                    logs.write(f"processo: {proc2.name()}\n")
                                                    logs.write(f"processo com muito uso na cpu\n")
                                            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess, PermissionError):
                                                continue                                        
                                        else:
                                            continue
                            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess, PermissionError):
                                continue                                                    
                                

                        f.close()
                        recuperar_arquivos_adm()
                                          

                                        

            except PermissionError:
                continue    

       
    

    


        




 


    
