# FIAP-challenge-Ransomware

# Apenas em Windows

> Obs: Anti-Malware-Operation é uma empresa **fictícia** qualquer semelhança são meras conhecidências

## Script python que protege o backup de seus arquivos e checa por ransomwares na máquina se baseando em tempo e uso de processador

Esse script foi feito em python e transformado em um .exe usando o pyinstaller, o software é de código livre e de uso livre, qualquer usuário é livre para atualizar, modificar e distribuir o software.

>📚Bibliotecas📚 

💻 os  
🧠 shutil  
📆 datetime/date  
🕗 time/sleep  
📶 signal  
📞 requests  
📐 hashlib  
📏 PySimpleGUI 
 🪟  Win32api  
➕ Hashlib  
🧨 socket  

>📚Bibliotecas📚

obs: Python versão 3 deve ser instalado, todas as bibliotecas devem estar instalados na máquina.


# CLI

> 📝 Eula 

para rodar o arquivo em cli basta clicar 2 vezes no executável ou digitar o comando: python3 eula.py, em seguida siga as instruções no próprio programa.

> 💾 Backup

Para o backup funcionar o eula precisa ter sua saida 100%, ou seja sem erros, ao executar o programa ele vai pedir por uma senha, sugerimos **NÃO** usar a mesma senha da do login da conta Administrador, ela vai ser usada para compactar o backup e proteger ele com uma senha.

> 💻 Checagem

O programa usa arquivos iscas que caso o ransomware mude sua extensão ou hash o sistema entra em modo de lockdown protegendo ainda mais as pastas backup e detectando processos que foram abertos recentemente e pelo seu uso de processador

> OBS

Sugerimos não rodar aplicativos não reconhecidos como modo administrador, o script é obrigatório rodar como Administrador no backup e no eula, o checador é aconselhável rodar também com o privilégio mais alto, caso contrário algumas coisas não poderão ser feitas por falta de privilégios

# GUI

> 📝 Eula 

para rodar o arquivo em gui basta clicar 2 vezes no executável ou digitar o comando: python3 eula.py, em seguida siga as instruções no próprio programa.

> 💾 Backup

Para o backup funcionar o eula precisa ter sua saida 100%, ou seja sem erros, ao executar o programa ele vai pedir por uma senha, sugerimos **NÃO** usar a mesma senha da do login da conta Administrador, ela vai ser usada para compactar o backup e proteger ele com uma senha.

> 💻 Checagem

O programa usa arquivos iscas que caso o ransomware mude sua extensão ou hash o sistema entra em modo de lockdown protegendo ainda mais as pastas backup e detectando processos que foram abertos recentemente e pelo seu uso de processador

> OBS

Sugerimos não rodar aplicativos não reconhecidos como modo administrador, o script é obrigatório rodar como Administrador no backup e no eula, o checador é aconselhável rodar também com o privilégio mais alto, caso contrário algumas coisas não poderão ser feitas por falta de privilégios

# Informações adicionais

Vale ressaltar que esse script **NÃO** substitui a utilização de um programa de antivirus como o windows defender por exemplo, ele serve como um apoio e nem sempre vai detectar o vírus, porém, seu backup vai estar a salvo, sugerimos também colocar o backup na núvem, nunca compartilhar senhas, sempre desconfie de programas, nunca pague o resgate e por fim caso realmente tenha sido infectado leve o computador para um especialista técnico.
