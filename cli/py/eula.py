from datetime import date
from msilib.schema import File
import os
import hashlib
import shutil
import requests
from time import sleep
import socket
import win32api
import sys

if len(sys.argv) > 2:
   print(f"Esse programa apenas aceita 1 parâmetro ou nenhum: python {sys.argv[0]} -h ou --help")
   quit()

elif len(sys.argv) > 1:
   if sys.argv[1] == "-h" or sys.argv[1] == "--help":
      print(f"""   
    #                               #     #                                           
   # #   #    # ##### #             ##   ##   ##   #      #    #   ##   #####  ###### 
  #   #  ##   #   #   #             # # # #  #  #  #      #    #  #  #  #    # #      
 #     # # #  #   #   #    #####    #  #  # #    # #      #    # #    # #    # #####  
 ####### #  # #   #   #             #     # ###### #      # ## # ###### #####  #      
 #     # #   ##   #   #             #     # #    # #      ##  ## #    # #   #  #      
 #     # #    #   #   #             #     # #    # ###### #    # #    # #    # ###### 
                                                                                
                                                                                
=======================================================================================

Este programa usa de arquivos iscas na área de trabalho, documentos e downloads e
vigia eles caso um ransomware os encripte, para rodar o programa digite no seu terminal:

python {sys.argv[0]} ou duplo clique no executável e seguir as instruções dentro do programa.

=======================================================================================

argumentos:

-h     - Mostra essa mensagem

--help - Mostra essa mensagem

=======================================================================================

Para mais informações por favor consulte a nossa página no github e leia o README.MD
toda a documentação se encontra lá
                                                                                
https://github.com/Fabrizzio53/FIAP-challenge-Ransomware                                                                              """)
   else:
        print(f'O argumento "{sys.argv[1]}" não é valido apenas -h ou --help')
        quit()

else:
 



    usuario = os.getlogin()
    eula = "C:\\backupconfig"
    lista = []
    BLOCK_SIZE = 65536 

    url = "https://github.com/Fabrizzio53/Dummy/raw/main/senhas.pdf"
    url1 = "https://github.com/Fabrizzio53/Dummy/raw/main/trabalho.pptx"
    url2 = "https://github.com/Fabrizzio53/Dummy/raw/main/money.docx"
    url3 = "https://github.com/Fabrizzio53/Dummy/raw/main/contas.txt"

    try:
        socket.gethostbyname("www.google.com.br")
        response = requests.get(url)
        response1 = requests.get(url1)
        response2 = requests.get(url2)
        response3 = requests.get(url3)

    except (socket.gaierror, requests.exceptions.ConnectionError):
        win32api.MessageBox(0, 'Sem internet', 'Por favor rode esse script com internet ativa!')
        quit()


    #=========================Primeira checagem=====================================================#

    while True:
        try:
            socket.gethostbyname("www.google.com.br")
            decisao = int(input("Bem vindo a configuração, selecione uma opção:\n 1 - Reconfigurar arquivos/grupos\n 2 - Iniciar a config\n 3 - Permitir o Administrador acessar o backup\n 4 - Negar o Administrador acessar o backup\n\n : "))
            
            if decisao > 5 or decisao < 0:
                os.system("cls")
                print("Por favor digite apenas números de 1 a 4\n")

            else:
                break

        except ValueError:
            os.system("cls")
            print("Por favor digite apenas números\n")
        
        except socket.gaierror:
            win32api.MessageBox(0, 'Sem internet', 'Por favor rode esse script com internet ativa!')
            quit()

    #=========================Decisão 1=====================================================#

    if decisao == 1:

        print("[*] Checando pastas:")
        sleep(2)


    #====================Checando se uma pasta existe===========================================#

        if os.path.isdir("C:\\backupconfig"):


    #======================Apagando arquivos dummy=============================================#

            print("\n[*] Apagando arquivos dummy:")
            usuarios = []
            with open(f"{eula}\\contas.txt","r") as file:
                
                usuariosarquivo = file

                usuarioslinhas = usuariosarquivo.readlines()

                for i in range(len(usuarioslinhas)):
                    usuarios.append(usuarioslinhas[i].replace("\n",""))


                for i in range(len(usuarios)):

                    if os.path.isdir(f"C:\\Users\\{usuarios[i]}\\Desktop\\anti-malware-operation") == True:
                        shutil.rmtree(f"C:\\Users\\{usuarios[i]}\\Desktop\\anti-malware-operation")
                    else:
                        continue

                    if os.path.isdir(f"C:\\Users\\{usuarios[i]}\\Desktop\\filesran") == True:
                        shutil.rmtree(f"C:\\Users\\{usuarios[i]}\\Desktop\\filesran")
                    else:
                        continue

                    if os.path.isdir(f"C:\\Users\\{usuarios[i]}\\Documents\\filesran") == True:
                        shutil.rmtree(f"C:\\Users\\{usuarios[i]}\\Documents\\filesran")
                    else:
                        continue

                    if os.path.isdir(f"C:\\Users\\{usuarios[i]}\Downloads\\filesran") == True:
                        shutil.rmtree(f"C:\\Users\\{usuarios[i]}\\Downloads\\filesran")
                    else:
                        continue


    #======================Apagando grupo nobackup=============================================#
            print("[*] Apagando grupo nobackup")
            sleep(2)
            os.system(f"net localgroup nobackup /delete")
            
                    
            print("[*] grupo apagado com sucesso")
            print("[*] Apagando pasta de configuração")
            sleep(2)

    #======================Apagando pasta config=============================================#
            print("[*] removendo eula")
            shutil.rmtree(eula)
            print("[*] removendo backup")
            shutil.rmtree("C:\\Program Files (x86)\\Backup")     
            sleep(2)   
            os.system("cls")


    #=====================Apagando tarefa agendada=============================================#

            os.system(f"schtasks /delete /tn backup_anti-malware-operation /F")
            print("[*] Tarefa apagada")
            sleep(2)
            os.system("cls")

    #====================================Fim===================================================#        
            
            print("[*] Reinicie o programa")
        else:
            print("Arquivos de backup não encontrados, por favor selecione a opção correta")
            quit()


    #====================================Decisão 2======================================#

    elif decisao == 2:

        while True:
            print("""

    ******    *******   ****     ** ******** **   ******** 
    **////**  **/////** /**/**   /**/**///// /**  **//////**
    **    //  **     //**/**//**  /**/**      /** **      // 
    /**       /**      /**/** //** /**/******* /**/**         
    /**       /**      /**/**  //**/**/**////  /**/**    *****
    //**    **//**     ** /**   //****/**      /**//**  ////**
    //******  //*******  /**    //***/**      /** //******** 
    //////    ///////   //      /// //       //   ////////  
        """)

            print("Para que o backup tenha um súcesso maior contra ransomware primeiro você deve seguir esses passos!\n")

            print("1 - O script deve rodar com a conta de Administrador ou com privilégios administrativos.\n")

            print("2 - Sugerimos que o eula sempre seja rodado como administrador\n")

            print("3 - A pasta de backup por padrão esta indisponível para todas as contas, para fazer com que o adm tenha acesso basta rodar o script novamente e escolher a opção 3\n")

            print("4 - Para bloquear o acesso ao administrador novamente digite a opção 4 no começo do programa\n")

            print("5 - Sugerimos que para tarefas não administrativas não rode nada a não ser esses scripts com privilégios administrativos\n")

            aceito = input("Aceita os termos? S ou N: ").upper()


    #===========================Checagem dos termos===================================================#

            if aceito != "S" and aceito != "N":
                os.system("cls")
                print("Por favor digite apenas S ou N, S = Sim, N = Não\n")
                input("Aperte qualquer botão para continuar ")

            else:
                break

        if aceito == "S":


    #===========================Contas que não vão acessar o backup=======================================#

            if os.path.isdir(eula) == True:
                os.system("cls")
                input("[*] Você tem uma pasta que não foi apagado corretamente, reinicie o programa e escolha a opção 1")
                quit()
            else:
                os.system("mkdir "+eula)

            f = open(f"{eula}\\contas.txt","a")

            continuar = "S"
            
            while continuar == "S":
                os.system("cls")
                resposta2 = input("Configuração\n\nDigite o nome das contas que NÃO irão ter acesso ao backup usuários comuns\n\n: ")
                f.write(f"{resposta2}\n")

                while True:

                    continuar = input("\nDeseja adicionar mais contas? S ou N ").upper()

                    if continuar != "S" and continuar != "N":
                        os.system("cls")
                        print("Por favor digite apenas S ou N, S = Sim, N = Não\n")
                        input("Aperte qualquer botão para continuar ")

                    else:
                        break

                if continuar == "N":
                    f.write("Administrador\n")
                    f.close()
                    break
                
            os.system("net localgroup nobackup /add")

        
            os.system("cls")

            while True:

    #===============================================Escolha de backup=====================================#

                try:

                    resposta = int(input("Configuração 2\n\n1- backup padrão o programa vai pegar as pastas mais importantes.\n2- Pastas padrões e suas escolhas. \n3- Apenas minhas escolhas.\n\n: "))
                
                    if resposta > 3 or resposta < 0:
                        os.system("cls")
                        print("Por favor digite apenas 1,2 ou 3\n")

                    else:

                        break

                except ValueError:
                    os.system("cls")
                    print("Por favor digite apenas números\n")



            usuariosarquivo = open(f"{eula}\\contas.txt","r")

            usuarioslinhas = usuariosarquivo.readlines()

            usuarios = []

            for i in range(len(usuarioslinhas)):
                usuarios.append(usuarioslinhas[i].replace("\n",""))

            if int(resposta) == 1:
                
                f = open(f"{eula}\\pastas.txt","a")

                for i in range(len(usuarios)):
                
                    
                    f.write(f"C:\\Users\\{usuarios[i]}\\Desktop\n")
                    f.write(f"C:\\Users\\{usuarios[i]}\\OneDrive\n")
                    f.write(f"C:\\Users\\{usuarios[i]}\\Documents\n")
                    f.write(f"C:\\Users\\{usuarios[i]}\\Pictures\n")
                    f.write(f"C:\\Users\\{usuarios[i]}\\Music\n")

                f.close()

            elif int(resposta) == 2:

                continuar = "S"

                f = open(f"{eula}\\pastas.txt","a")

                for i in range(len(usuarios)):

                    f.write(f"C:\\Users\\{usuarios[i]}\\Desktop\n")
                    f.write(f"C:\\Users\\{usuarios[i]}\\OneDrive\n")
                    f.write(f"C:\\Users\\{usuarios[i]}\\Documents\n")
                    f.write(f"C:\\Users\\{usuarios[i]}\\Pictures\n")
                    f.write(f"C:\\Users\\{usuarios[i]}\\Music\n")
                    
                while continuar == "S":
                    os.system("cls")
                    pastas = input("Digite a pasta que você quer fazer backup exemplo C:\\Users\\Teste\\Downloads : ")
                    f.write(f"{pastas}\n")

                    while True:

                        continuar  = input("Deseja continuar S ou N? ").upper()

                        if continuar != "S" and continuar != "N":
                            os.system("cls")
                            print("Por favor digite apenas S ou N, S = Sim, N = Não\n")
                            input("Aperte qualquer botão para continuar ")

                        else:
                            break


                    if continuar == "N":
                        f.close()
                        break
            
            elif int(resposta) == 3:
                continuar = "S"
                f = open(f"{eula}\\pastas.txt","a")
                while continuar == "S":
                    os.system("cls")
                    pastas = input("Digite a pasta que você quer fazer backup exemplo C:\\Users\\Teste\\Downloads : ")
                    f.write(f"{pastas}\n")

                    while True:

                        continuar  = input("Deseja continuar S ou N? ").upper()

                        if continuar != "S" and continuar != "N":
                            os.system("cls")
                            print("Por favor digite apenas S ou N, S = Sim, N = Não\n")
                            input("Aperte qualquer botão para continuar ")

                        else:
                            break

                    if continuar == "N":
                        f.close()
                        break
    

            continuar = "S"
            

            os.system("cls")


    #==================================Adicionando usuários ao grupo nobackup=========================#

            for i in range(len(usuarios)):
                os.system(f"net localgroup nobackup {usuarios[i]} /add")


    #===================================Criando arquivos Dummy=======================================#

            os.system("cls")
            sleep(1)
            print("Criando arquivos dummy")
            sleep(3)        
            for i in range(len(usuarios)):
                os.mkdir(f"C:\\backupconfig\\{usuarios[i]}")
                os.mkdir(f"C:\\Users\\{usuarios[i]}\\Desktop\\filesran")
                os.system(f'mkdir "C:\\Users\\{usuarios[i]}\\Documents\\filesran"')
                os.mkdir(f"C:\\Users\\{usuarios[i]}\\Downloads\\filesran")

                with open(f"C:\\Users\\{usuarios[i]}\\Desktop\\filesran\\contas.txt","wb") as file:
                    lista.append(f"C:\\Users\\{usuarios[i]}\\Desktop\\filesran\\contas.txt")
                    file.write(response3.content)

                with open(f"C:\\Users\\{usuarios[i]}\\Desktop\\filesran\\money.docx","wb") as file:

                    lista.append(f"C:\\Users\\{usuarios[i]}\\Desktop\\filesran\\money.docx")
                    file.write(response2.content)


                with open(f"C:\\Users\\{usuarios[i]}\\Desktop\\filesran\\senhas.pdf","wb") as file:
                    
                    lista.append(f"C:\\Users\\{usuarios[i]}\\Desktop\\filesran\\senhas.pdf")
                    file.write(response.content)

                with open(f"C:\\Users\\{usuarios[i]}\\Desktop\\filesran\\trabalho.pptx","wb") as file:
                    
                    lista.append(f"C:\\Users\\{usuarios[i]}\\Desktop\\filesran\\trabalho.pptx")
                    file.write(response1.content)


                #==================================#

                with open(f"C:\\Users\\{usuarios[i]}\\Documents\\filesran\\contas.txt","wb") as file:
                    lista.append(f"C:\\Users\\{usuarios[i]}\\Documents\\filesran\\contas.txt")
                    file.write(response3.content)

                with open(f"C:\\Users\\{usuarios[i]}\\Documents\\filesran\\money.docx","wb") as file:

                    lista.append(f"C:\\Users\\{usuarios[i]}\\Documents\\filesran\\money.docx")
                    file.write(response2.content)


                with open(f"C:\\Users\\{usuarios[i]}\\Documents\\filesran\\senhas.pdf","wb") as file:
                    
                    lista.append(f"C:\\Users\\{usuarios[i]}\\Documents\\filesran\\senhas.pdf")
                    file.write(response.content)

                with open(f"C:\\Users\\{usuarios[i]}\\Documents\\filesran\\trabalho.pptx","wb") as file:
                    
                    lista.append(f"C:\\Users\\{usuarios[i]}\\Documents\\filesran\\trabalho.pptx")
                    file.write(response1.content)


                #==========================#

                with open(f"C:\\Users\\{usuarios[i]}\\Downloads\\filesran\\contas.txt","wb") as file:
                    lista.append(f"C:\\Users\\{usuarios[i]}\\Downloads\\filesran\\contas.txt")
                    file.write(response3.content)

                with open(f"C:\\Users\\{usuarios[i]}\\Downloads\\filesran\\money.docx","wb") as file:

                    lista.append(f"C:\\Users\\{usuarios[i]}\\Downloads\\filesran\\money.docx")
                    file.write(response2.content)


                with open(f"C:\\Users\\{usuarios[i]}\\Downloads\\filesran\\senhas.pdf","wb") as file:
                    
                    lista.append(f"C:\\Users\\{usuarios[i]}\\Downloads\\filesran\\senhas.pdf")
                    file.write(response.content)

                with open(f"C:\\Users\\{usuarios[i]}\\Downloads\\filesran\\trabalho.pptx","wb") as file:
                    
                    lista.append(f"C:\\Users\\{usuarios[i]}\\Downloads\\filesran\\trabalho.pptx")
                    file.write(response1.content)







    #=====================================Tirando o hash dos arquivos originais========================#

                if os.path.isfile(f"C:\\backupconfig\\{usuarios[i]}\\hash_original.txt") == True:
                    pass
                else:
                    for i2 in range(len(lista)):

                        file_hash = hashlib.md5() 
                        with open(lista[i2], 'rb') as f: 
                            fb = f.read(BLOCK_SIZE) 
                            while len(fb) > 0: 
                                file_hash.update(fb) 
                                fb = f.read(BLOCK_SIZE) 

                            hashed = file_hash.hexdigest()

                        with open(f"C:\\backupconfig\\{usuarios[i]}\\hash_original.txt",'a') as f2:
                            f2.write(f"{hashed}\n")

                        os.system(f"cacls C:\\backupconfig\\{usuarios[i]} /e /p {usuarios[i]}:R")
                        os.system(f'cacls C:\\backupconfig\\{usuarios[i]} /e /p "Usuários Autenticados":R')
                            
                lista.clear()

            os.system("cls")

            print("Arquivos dummy criados em: \n\nDesktop\nDocuments\nDownloads\n\nNão modifique eles!!!!")
            input("\nAperte qualquer botão para continuar ")


    #====================================Movendo os arquivos=============================================#


            os.system("cls")
            print("Movendo arquivos para C:\\Program Files (x86)\\Backup")
            try:
                os.mkdir("C:\\Program Files (x86)\\Backup")

                

                with open("C:\\Program Files (x86)\\Backup\\contas.txt","wb") as file:
                    file.write(response3.content)

                with open("C:\\Program Files (x86)\\Backup\\money.docx","wb") as file:
                    file.write(response2.content)


                with open("C:\\Program Files (x86)\\Backup\\senhas.pdf","wb") as file:

                    file.write(response.content)

                with open("C:\\Program Files (x86)\\Backup\\trabalho.pptx","wb") as file:

                    file.write(response1.content)
            except FileExistsError:
                pass
            sleep(1)
            try:
                shutil.move("eula.py","C:\Program Files (x86)\Backup")
                shutil.move("backup.py","C:\Program Files (x86)\Backup")
                shutil.move("checagem_de_hash.py","C:\Program Files (x86)\Backup")
            except FileNotFoundError:
                win32api.MessageBox(0, 'Erro', 'Script não pode mover os arquivos, reinicia o programa!')
                quit()

            os.system("cls")



    #=================================Criando links simbólicos============================================#        

            print("Criando links simbólicos")

            sleep(2)

            for i in range(len(usuarios)):
                try:
                    os.mkdir(f"C:\\Users\\{usuarios[i]}\\Desktop\\anti-malware-operation")
                    os.system(f'mklink C:\\Users\\{usuarios[i]}\\Desktop\\anti-malware-operation\\eula.py "C:\\Program Files (x86)\\Backup\\eula.py"')
                    os.system(f'mklink C:\\Users\\{usuarios[i]}\\Desktop\\anti-malware-operation\\backup.py "C:\\Program Files (x86)\\Backup\\backup.py"')
                    os.system(f'mklink C:\\Users\\{usuarios[i]}\\Desktop\\anti-malware-operation\\checagem_de_hash.py "C:\\Program Files (x86)\\Backup\\checagem_de_hash.py"')
                except FileExistsError:
                    pass



            os.system("cls")

            os.system('schtasks /create /sc daily /tn backup_anti-malware-operation /tr "C:\\Program Files (x86)\\Backup\\backup.py" /F')



            os.system("cls")

    #=====================================Reinciar===================================================#

            while True:

                try:

                    desligar = int(input("Você precisa reiniciar o pc, quer reiniciar agora?\n 1 - Sim\n 2 - Não\n : "))

                    if desligar < 0 or desligar > 2:
                        os.system("cls")
                        print("Digite apenas 1 ou 2")

                    else:

                        break

                except ValueError:
                    os.system("cls")
                    print("Por favor digite apenas números\n")

            if desligar == 1:
                os.system("shutdown /r /f")
            else:
                os.system("cls")
                print("Para que a pasta de backup ficar protejido, lembre-se de reiniciar o computador o quanto antes.")


        else:
            os.system("cls")
            print("Você precisa aceitar nossos termos :(")
            quit()


    #=====================================Decisão 3=================================================#


    elif decisao==3:
        os.system("cls")
        os.system(f"net localgroup nobackup Administrador /delete")
        print("\nLembre-se de reinciciar o pc e após ter feito tudo necessário bloqueie o administrador de acessar o backup.")

        


    #=====================================Decisão 4=================================================#


    elif decisao == 4:
        os.system("cls")
        os.system(f"net localgroup nobackup Administrador /add")       
        print("\nAdministrador sem acesso ao backup, lembre-se de reiniciar o pc")
        


    #=======================================Fim do programa======================================#