from msilib.schema import File
import PySimpleGUI as sg
from datetime import date
from multiprocessing.sharedctypes import Value
import os
import hashlib
import shutil
import requests
from time import sleep
import webbrowser as wb
import sys
import socket
import win32api
from checagem_de_hash import analisador
import py7zr
import getpass

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

    response = requests.get(url)
    response1 = requests.get(url1)
    response2 = requests.get(url2)
    response3 = requests.get(url3)

    def introducao():
        sg.theme('LightGrey1')
        layout = [
            [sg.Image(filename='anti_malware_operation.png')],
            [sg.Text('Bem-Vindo ao programa Anti-Ransomware')], 
            [sg.Text('Da equipe Anti-Malware-Operation')],
            [sg.Button('Backup', size=(16,0))], [sg.Button('Eula', size=(16,0))],[sg.Button('GitHub', size=(16,0))],[sg.Button('Analisador de Hash', size=(16,0))], [sg.Button('Sair', size=(16,0))]
        ]
        return sg.Window('Anti-Malware-Operation',element_justification='c', layout=layout, finalize=True)


    def EULA():
        sg.theme('LightGrey1')
        layout = [
            [sg.Text('Bem vindo a configuração, selecione uma opção:')],
            [sg.Button('Reconfigurar arquivos/grupos', size=(35,0))], 
            [sg.Button('Iniciar a config', size=(35,0))],
            [sg.Button('Permitir o Administrador acessar o backup', size=(35,0))], 
            [sg.Button('Negar o Administrador acessar o backup', size=(35,0))],
            [sg.Button('Voltar', size=(35,0))]
        ]
        return sg.Window('Anti-Malware-Operation',element_justification='c', layout=layout, finalize=True)

    def INICIAR_CONFIG():
        sg.theme('LightGrey1')
        layout = [
            [sg.Text('Para que o backup tenha um súcesso maior contra ransomware primeiro você deve seguir esses passos!')],
            [sg.Text('1 - O script deve rodar com a conta de Administrador ou com privilégios administrativos.')],
            [sg.Text('2 - Sugerimos que o eula sempre seja rodado como administrador')],
            [sg.Text('3 - A pasta de backup por padrão esta indisponível para todas as contas, para fazer com que o adm tenha acesso basta rodar o script novamente e escolher a opção 3')],
            [sg.Text('4 - Para bloquear o acesso ao administrador novamente digite a opção 4 no começo do programa')],
            [sg.Text('5 - Sugerimos que para tarefas não administrativas não rode nada a não ser esses scripts com privilégios administrativos')],
            [sg.Button('Voltar'), sg.Button('Não Aceito os Termos'), sg.Button('Aceito os Termos')]
        ]
        return sg.Window('Anti-Malware-Operation', layout=layout, finalize=True)

    def add_conta():
        sg.theme('LightGrey1')
        layout = [
            [sg.Text('Caso queira adicionar alguma conta que NÃO irá ter acesso ao backup, clique em (Adcionar conta), caso não queira fazer nada clique em (Proximo)',size=(30,0))],
            [sg.Button('Voltar'), sg.Button('Adicionar Conta'), sg.Button('Proximo')]
        ]    
        
        return sg.Window('Anti-Malware-Operation',element_justification='c', layout=layout, finalize=True)

    def config2():
        sg.theme('LightGrey1')
        layout = [
            [sg.Text('Selecione uma opção, para salvar suas pastas:')],
            [sg.Button('Backup padrão o programa vai pegar as pastas mais importantes.',size=(40,0))],
            [sg.Button('Pastas padrões e suas escolhas.',size=(40,0))],
            [sg.Button('Apenas minhas escolhas.',size=(40,0))],
            [sg.Text('Depois de selecionar alguma opção, clique em finalizar')],
            [sg.Button('Finalizar',size=(40,0))]
        ]
        return sg.Window('Anti-Malware-Operation',element_justification='c', layout=layout, finalize=True)


    janela1, janela2, janela3, janela4, janela5 = introducao(), None, None, None, None

    while True:
        window,event,values = sg.read_all_windows()
        if window == janela1 and event == sg.WIN_CLOSED:
            break
        if window == janela2 and event == sg.WIN_CLOSED:
            break
        if window == janela3 and event == sg.WIN_CLOSED:
            break
        if window == janela4 and event == sg.WIN_CLOSED:
            break
        if window == janela5 and event == sg.WIN_CLOSED:
            break
        if window == janela1 and event == 'Sair':
            break
        if window == janela1 and event == 'Eula':
            janela1.hide()
            janela2 = EULA()
        if window == janela2 and event == 'Voltar':
            janela2.hide()
            janela1.un_hide()


        if window == janela1 and event == 'GitHub':
            wb.open('https://github.com/Fabrizzio53/FIAP-challenge-Ransomware')


    #Analisador de Hash#
        if window == janela1 and event == 'Analisador de Hash':
           analisador()
    #Fim-Analisador de Hash#


    #Backup#

        if window == janela1 and event == 'Backup':
            nome = os.getlogin()
            if nome != "Administrador":
                sg.popup_ok("O script precisa ser rodado como administrador")
                quit()
            else:
                with open(f"C:\\backupconfig\\pastas.txt","r") as dirs:
                    dirslinhas = dirs.readlines()
                senha = sg.popup_get_text(password_char="*",message='Digite uma senha que vai proteger o backup: ')
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
                    sg.popup_ok("Erro no programa, a lista não tem pelo menos 1 index")
                    quit()

                today = date.today()

                d1 = today.strftime("_%d_%m_%Y")


                os.system("cls")
                sg.popup_auto_close("Iniciando backup.....")
                sleep(3)

                if os.path.isdir("C:\\Program Files (x86)\\Backup\\backup") == True:
                    pass
                else:
                    os.mkdir("C:\\Program Files (x86)\\Backup\\backup")

                if os.path.isdir(f"C:\\Users\\backup\\{d1}") == True:
                    sg.popup_ok(f"[*] A pasta de backup C:\\Users\\backup\\{d1} já existe por favor apague ela e tente novamente")

                

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
                    sg.popup_ok("Backup finalizado")


    #Fim Backup#

    #Eula#
        #Reconfigurar arquivos/grupos#
        if window == janela2 and event == 'Reconfigurar arquivos/grupos':
            sg.popup_auto_close("Checando pastas:")
            if os.path.isdir("C:\\backupconfig"):
                sg.popup_auto_close("\n[*] Apagando arquivos dummy:")
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

                sg.popup_auto_close("[*] Apagando grupo nobackup")
                sleep(2)
                os.system(f"net localgroup nobackup /delete")
                        
                sg.popup_auto_close("Grupo apagado com sucesso")

                sg.popup_auto_close("Apagando pasta de configuração")
                sleep(2)

                os.system(f"rmdir /S /Q {eula}")
                os.system('rmdir /S /Q "C:\\Program Files (x86)\\Backup"')
                sg.popup_auto_close("Pasta apagada")     
                sleep(2)   
                os.system("cls")

                sg.popup_ok("Reinicie o programa")
            else:
                sg.popup_ok("Arquivos de backup não encontrados, por favor selecione a opção correta")
                quit()
        #Fim - Reconfigurar arquivos/grupos#

        #Iniciar a config#
        if window == janela2 and event == 'Iniciar a config':
            janela2.hide()
            janela3 = INICIAR_CONFIG()

        if window == janela3 and event == 'Voltar':
            janela3.hide()
            janela2.un_hide()
        
        if window == janela3 and event == 'Não Aceito os Termos':
            break

        if window == janela3 and event == 'Aceito os Termos':
            janela3.hide()
            janela4 = add_conta()
        
        if window == janela4 and event == 'Voltar':
            janela4.hide()
            janela3.un_hide()
        
        if window == janela4 and event == 'Adicionar Conta':
            os.system("mkdir "+eula)
            f = open(f"{eula}\\contas.txt","a")
            resposta2 = sg.popup_get_text('Digite o nome das contas que NÃO irão ter acesso ao backup usuários comuns', 'Ex:Teste2')
            f.write(f"{resposta2}\n")
            f.close()

        if window == janela4 and event == 'Proximo':
            f = open(f"{eula}\\contas.txt","a")
            f.write("Administrador\n")
            f.close()
            os.system("net localgroup nobackup /add")
            janela4.hide()
            janela5 = config2()


        if window == janela5 and event == 'Backup padrão o programa vai pegar as pastas mais importantes.':
            usuariosarquivo = open(f"{eula}\\contas.txt","r")

            usuarioslinhas = usuariosarquivo.readlines()

            usuarios = []

            for i in range(len(usuarioslinhas)):
                usuarios.append(usuarioslinhas[i].replace("\n",""))
                f = open(f"{eula}\\pastas.txt","a")

                for i in range(len(usuarios)):
                        
                            
                        f.write(f"C:\\Users\\{usuarios[i]}\\Desktop\n")
                        f.write(f"C:\\Users\\{usuarios[i]}\\OneDrive\n")
                        f.write(f"C:\\Users\\{usuarios[i]}\\Documents\n")
                        f.write(f"C:\\Users\\{usuarios[i]}\\Pictures\n")
                        f.write(f"C:\\Users\\{usuarios[i]}\\Music\n")

                f.close()
            sg.popup_auto_close('O programa foi executado com sucesso')
        
        if window == janela5 and event == 'Pastas padrões e suas escolhas.':
            usuariosarquivo = open(f"{eula}\\contas.txt","r")

            usuarioslinhas = usuariosarquivo.readlines()

            usuarios = []

            for i in range(len(usuarioslinhas)):
                usuarios.append(usuarioslinhas[i].replace("\n",""))
                f = open(f"{eula}\\pastas.txt","a")

                for i in range(len(usuarios)):

                    f.write(f"C:\\Users\\{usuarios[i]}\\Desktop\n")
                    f.write(f"C:\\Users\\{usuarios[i]}\\OneDrive\n")
                    f.write(f"C:\\Users\\{usuarios[i]}\\Documents\n")
                    f.write(f"C:\\Users\\{usuarios[i]}\\Pictures\n")
                    f.write(f"C:\\Users\\{usuarios[i]}\\Music\n")

                    pastas = sg.popup_get_folder('Digite a pasta que você quer fazer backup exemplo C:\\Users\\Teste\\Downloads :')
                    f.write(f"{pastas}\n")

                f.close()
            sg.popup_auto_close('O programa foi executado com sucesso')
        
        if window == janela5 and event == 'Apenas minhas escolhas.':
            usuariosarquivo = open(f"{eula}\\contas.txt","r")

            usuarioslinhas = usuariosarquivo.readlines()

            usuarios = []
            for i in range(len(usuarioslinhas)):
                usuarios.append(usuarioslinhas[i].replace("\n",""))
                f = open(f"{eula}\\pastas.txt","a")
                pastas = sg.popup_get_folder('Digite a pasta que você quer fazer backup exemplo C:\\Users\\Teste\\Downloads :')
                f.write(f"{pastas}\n")
            
            f.close()
            sg.popup_auto_close('O programa foi executado com sucesso')

        if window == janela5 and event == 'Finalizar':
            usuariosarquivo = open(f"{eula}\\contas.txt","r")

            usuarioslinhas = usuariosarquivo.readlines()

            usuarios = []

            for i in range(len(usuarioslinhas)):
                usuarios.append(usuarioslinhas[i].replace("\n",""))
                
            for i in range(len(usuarios)):
                os.system(f"net localgroup nobackup {usuarios[i]} /add")

            sleep(1)
            sg.popup_auto_close("Criando arquivos dummy")
            sleep(3)
                    
            for i in range(len(usuarios)):
                try:
                    os.mkdir(f"C:\\backupconfig\\{usuarios[i]}")
                    os.mkdir(f"C:\\Users\\{usuarios[i]}\\Desktop\\filesran")
                    os.mkdir(f"C:\\Users\\{usuarios[i]}\\Documents\\filesran")
                    os.mkdir(f"C:\\Users\\{usuarios[i]}\\Downloads\\filesran")
                except FileExistsError:
                    continue

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

            sg.popup_auto_close("Arquivos dummy criados em: \n\nDesktop\nDocuments\nDownloads\n\nNão modifique eles!!!!")
            


    #====================================Movendo os arquivos=============================================#


            os.system("cls")
            sg.popup_auto_close("Movendo arquivos para C:\\Program Files (x86)\\Backup")
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
                shutil.move("anti_malware_operation.png","C:\Program Files (x86)\Backup")
                shutil.move("interfaceSimple.py","C:\Program Files (x86)\Backup")
                shutil.move("backup.py","C:\Program Files (x86)\Backup")
                shutil.move("checagem_de_hash.py","C:\Program Files (x86)\Backup")
            except FileNotFoundError:
                win32api.MessageBox(0, 'Erro', 'Script não pode mover os arquivos, reinicia o programa!')
                quit()                

            os.system("cls")



    #=================================Criando links simbólicos============================================#        

            sg.popup_auto_close("Criando links simbólicos")

            sleep(2)

            for i in range(len(usuarios)):

                os.mkdir(f"C:\\Users\\{usuarios[i]}\\Desktop\\anti-malware-operation")
                os.system(f'mklink C:\\Users\\{usuarios[i]}\\Desktop\\anti-malware-operation\\interfaceSimple.py "C:\\Program Files (x86)\\Backup\\interfaceSimple.py"')
                os.system(f'mklink C:\\Users\\{usuarios[i]}\\Desktop\\anti-malware-operation\\backup.py "C:\\Program Files (x86)\\Backup\\backup.py"')
                os.system(f'mklink C:\\Users\\{usuarios[i]}\\Desktop\\anti-malware-operation\\checagem_de_hash.py "C:\\Program Files (x86)\\Backup\\checagem_de_hash.py"')


            os.system("cls")

            os.system('schtasks /create /sc daily /tn backup_anti-malware-operation /tr "C:\\Program Files (x86)\\Backup\\backup.py" /F')

            os.system("cls")

    #=====================================Reinciar===================================================#

            
            desligar = sg.popup_yes_no("Você precisa reiniciar o pc, quer reiniciar agora?: ")

            if values == 'Yes':
                    os.system("shutdown /r /f")
            else:
                    os.system("cls")
                    sg.popup_auto_close("Para que a pasta de backup ficar protejido, lembre-se de reiniciar o computador o quanto antes.")
                    break



        #Fim - Iniciar a config#

        #Permitir o Administrador acessar o backup#
        if window == janela2 and event == 'Permitir o Administrador acessar o backup':
            os.system("cls")
            os.system(f"net localgroup nobackup Administrador /delete")
            sg.popup_ok("Lembre-se de reinciciar o pc e após ter feito tudo necessário bloqueie o administrador de acessar o backup.")
            

        #Fim - Permitir o Administrador acessar o backup#

        #Negar o Administrador acessar o backup#
        if window == janela2 and event == 'Negar o Administrador acessar o backup':
            os.system("cls")
            os.system(f"net localgroup nobackup Administrador /add")
            sg.popup_ok("\nAdministrador sem acesso ao backup, lembre-se de reiniciar o pc")
        #Fim - Negar o Administrador acessar o backup#
    #Fim Eula#