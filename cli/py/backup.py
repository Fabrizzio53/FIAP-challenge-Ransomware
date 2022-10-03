import os
import shutil
from datetime import date
from time import sleep
import py7zr
import getpass
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

Este programa é um complemente do eula e do checador, para usar ele basta digitar no terminal:

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


    nome = os.getlogin()

    if nome != "Administrador":
        print("O script precisa ser rodado como administrador")
        quit()


    else:
        
        with open(f"C:\\backupconfig\\pastas.txt","r") as dirs:
    
            dirslinhas = dirs.readlines()

        senha = getpass.getpass(prompt='Digite uma senha que vai proteger o backup: ')

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


        os.system("cls")
        print("Iniciando backup.....")
        sleep(3)

        if os.path.isdir("C:\\Program Files (x86)\\Backup\\backup") == True:
            os.system(f'attrib +h /s /d "C:\\Program Files (x86)\\Backup\\backup"')
            pass
        else:
            os.mkdir("C:\\Program Files (x86)\\Backup\\backup")
            os.system(f'attrib +h /s /d "C:\\Program Files (x86)\\Backup\\backup"')

        if os.path.isdir(f"C:\\Users\\backup\\{d1}") == True:
            input(f"[*] A pasta de backup C:\\Users\\backup\\{d1} já existe por favor apague ela e tente novamente")
    
        else:

            for i in range(len(dirs2)):
                try:  
                    shutil.copytree(dirs2[i],f"C:\\Users\\backup\\{d1}\\{dirs3[i]}")
                except FileExistsError:
                    pass
                except shutil.Error:
                    pass

            with open("C:\\backupconfig\\backup_logs.txt","a") as logs:
                logs.write(f"Backup feito em: {d1}\n")
        
            try:
                with py7zr.SevenZipFile(f'C:\\Program Files (x86)\\Backup\\backup\\{d1}.7z','w', password=senha) as archive:
                    archive.writeall(f"C:\\Users\\backup\\{d1}", f'backup{d1}')
            except PermissionError:
                pass
            
            os.system(f'attrib +h /s /d "C:\\Program Files (x86)\\Backup"')
            os.system(f'attrib +h /s /d "C:\\Program Files (x86)\\Backup\\backup\\{d1}.7z"')
            os.system(f'attrib +h /s /d "C:\\Program Files (x86)\\Backup\\backup"')
            os.system(f'attrib +h /s /d "C:\\Users\\backup"')
            os.system(f'attrib +h /s /d "C:\\Users\\backup\\{d1}"')
                
            os.system(f"cacls C:\\Users\\backup\\{d1} /e /p nobackup:N")
            os.system(f'cacls "C:\\Program Files (x86)\\Backup\\backup\\{d1}.7z" /e /p nobackup:N')
            os.system(f'cacls "C:\\Program Files (x86)\\Backup\\backup\\{d1}.7z" /e /p Todos:N')

            
            os.system("cls")
            input("Backup finalizado")
















    

