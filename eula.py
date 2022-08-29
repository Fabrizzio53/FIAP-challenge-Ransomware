from datetime import date
import os
import hashlib
import shutil
import requests
from time import sleep

usuario = os.getlogin()
eula = "C:\\backupconfig"
lista = []
BLOCK_SIZE = 65536 

url = "https://github.com/Fabrizzio53/Dummy/raw/main/senhas.pdf"
url1 = "https://github.com/Fabrizzio53/Dummy/raw/main/trabalho.pptx"
url2 = "https://github.com/Fabrizzio53/Dummy/raw/main/money.docx"
url3 = "https://github.com/Fabrizzio53/Dummy/raw/main/contas.txt"

response = requests.get(url)
response1 = requests.get(url1)
response2 = requests.get(url2)
response3 = requests.get(url3)



if os.path.isdir("C:\\backupconfig"):
    refazer = int(input("Você já fez a configuração, você quer apagar a config e refazer ela?\n 1 - Sim\n 2 - Não\n : "))

    if refazer == 1:
        usuarios = []
        with open(f"{eula}\\contas.txt","r") as file:
            
            usuarioslinhas = file.readlines()

        
        for i in range(len(usuarioslinhas)):
            usuarios.append(usuarioslinhas[i].replace("\n",""))

        for i in range(len(usuarios)):

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
            
    


        os.system(f"rmdir /S /Q {eula}")
            

        print("Reinicie o programa")
    else:
        quit()

else:
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

    print("1 - O script deve ser rodado como administrador para criar as permissões e pastas necessárias.\n")

    print("2 - Após o script ser rodado a conta deve voltar aos privilégios normais (obs: não sendo administrativa)\n")

    print("3 - A conta deve ser de um usuário normal já que o ransomware não vai conseguir alterar arquivos na pasta\n")

    aceito = input("Aceita os termos? S ou N: ").upper()

    if aceito == "S":
        os.system("cls")
        os.system("mkdir "+eula)
        resposta = input("Configuração:\n 1- backup padrão o programa vai pegar as pastas mais importantes.\n 2- Pastas padrões e suas escolhas. \n 3- Apenas minhas escolhas.\n : ")

        if int(resposta) == 1:
            f = open(f"{eula}\\pastas.txt","a")
            f.write(f"C:\\Users\\{os.getlogin()}\\Desktop\n")
            f.write(f"C:\\Users\\{os.getlogin()}\\OneDrive\n")
            f.write(f"C:\\Users\\{os.getlogin()}\\Documents\n")
            f.write(f"C:\\Users\\{os.getlogin()}\\Pictures\n")
            f.write(f"C:\\Users\\{os.getlogin()}\\Music")
            f.close()

        elif int(resposta) == 2:
            continuar = "S"
            f = open(f"{eula}\\pastas.txt","a")
            f.write(f"C:\\Users\\{os.getlogin()}\\Desktop\n")
            f.write(f"C:\\Users\\{os.getlogin()}\\OneDrive\n")
            f.write(f"C:\\Users\\{os.getlogin()}\\Documents\n")
            f.write(f"C:\\Users\\{os.getlogin()}\\Pictures\n")
            f.write(f"C:\\Users\\{os.getlogin()}\\Music\n")
            while continuar == "S":
                pastas = input("Digite a pasta que você quer fazer backup exemplo C:\\Users\\Teste\\Downloads : ")
                f.write(f"{pastas}\n")
                continuar  = input("Deseja continuar S ou N? ").upper()
                if continuar == "N":
                    f.close()
                    break
        
        elif int(resposta) == 3:
            continuar = "S"
            f = open(f"{eula}\\pastas.txt","a")
            while continuar == "S":
                pastas = input("Digite a pasta que você quer fazer backup exemplo C:\\Users\\Teste\\Downloads : ")
                f.write(f"{pastas}\n")
                continuar  = input("Deseja adicionar mais pastas? S ou N: ").upper()
                if continuar == "N":
                    f.close()
                    break

        else:
            print("Opção inválida")
            quit()        

        continuar = "S"
        os.system("cls")
        f = open(f"{eula}\\contas.txt","a")
        while continuar == "S":
            resposta2 = input("Configuração 2:\n Digite o nome das contas que NÃO irão ter acesso ao backup usuários comuns\n : ")
            f.write(f"{resposta2}\n")
            continuar = input("Deseja adicionar mais contas? S ou N ").upper()
            if continuar == "N":
                f.close()
                break
            
        os.system("net localgroup backup /add")
        os.system("net localgroup backup Administrador /add")
        os.system("net localgroup nobackup /add")

        os.system("cls")

        usuariosarquivo = open(f"{eula}\\contas.txt","r")

        usuarioslinhas = usuariosarquivo.readlines()

        usuarios = []

        for i in range(len(usuarioslinhas)):
            usuarios.append(usuarioslinhas[i].replace("\n",""))

        for i in range(len(usuarios)):
            os.system(f"net localgroup nobackup {usuarios[i]} /add")


        print("Criando arquivos dummy")
        sleep(3)
        
        with open("C:\\backupconfig\\contas.txt","r") as conta:
            conta = conta.readline()
            

        for i in range(len(usuarios)):
            os.mkdir(f"C:\\backupconfig\\{usuarios[i]}")
            os.mkdir(f"C:\\Users\\{usuarios[i]}\\Desktop\\filesran")
            os.mkdir(f"C:\\Users\\{usuarios[i]}\\Documents\\filesran")
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

        print("Arquivos dummy criados em: \nDesktop\nDocuments\nDownloads\nNão modifique eles")

        os.system('schtasks /create /sc daily /tn backup_fiap /tr C:\\Users\\Administrador\\Desktop\\main.py')

        desligar = int(input("Você precisa reiniciar o pc, quer reiniciar agora?\n 1 - Sim\n 2 - Não\n : "))

        if desligar == 1:
            os.system("shutdown /r /f")
        else:
            os.system("cls")
            print("Para que a pasta de backup ficar protejido, lembre-se de reiniciar o computador o quanto antes.")


    else:
        quit()

