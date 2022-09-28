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

>--------------

# Eula

O eula aceita apenas um argumento ou nenhum

python eula.py -h ou --help

Este argumento serve para ser um mini guia e um link para este github

![Screenshot_1](https://user-images.githubusercontent.com/88493503/192852634-4e26601e-b31e-43b9-82eb-911bbba93f89.png)

Ao abrir o programa sem nenhum argumento ele vai se iniciar e 4 opções estarão presentes:

1 - Reconfigurar arquivos/grupos

2 - Iniciar a config

3 - Permitir o Administrador acessar o backup

4 - Negar o Administrador acesssar o backup

Caso seja a primeira vez que o programa está sendo rodado por favor aperta 2 e enter

![Screenshot_2](https://user-images.githubusercontent.com/88493503/192853005-9fa922de-af10-4eac-8f68-43d2c460d769.png)

Você deve aceitar os termos, caso não aceite o programa não vai rodar, para aceitar digite S e aperte enter.

Configuração:

Digite o nome das contas que NÃO irão ter acesso ao backup usuários comuns:

Aqui você deve digitar suas contas o programa não consegue ainda detectar se a conta digita é válida no sistema operacional então preste muito atenção nesta parte, após digitar ele vai perguntar se vocÊ quer continuar, caso positivo aperte S se não aperte N e enter

Configuração2:

Aqui você vai poder escolher o tipo de backup:

1 - Backup padrão (Pastas como Desktop, Documents, Downloads)

2 - Pastas padrões e suas escolhas (Desktop, Documents, Download e pastas que você escolher)

3 - Apenas minhas escolhas ( Você escolhe as pastas)

![Screenshot_3](https://user-images.githubusercontent.com/88493503/192853827-94353f1b-3799-4de7-a8eb-bd7934e043d4.png)

O programa agora vai criar arquivos Dummy/iscas que vão servir para detectar se um ransomware está na máquina, pedimos para NÃO alterar esses arquivos que se encontra na pasta filesran!!!

Em seguida ele vai criar links simbólicos e vai mover todos os arquivos para a pasta C:\Program Files(x86)\Backup é por aqui que os executáveis se encontram e você pode apenas executar eles pelo link simbólico que se encontra na área de trabalho na pasta anti-malware-operation

Em seguida pedimos que reinicia o computador, você não precisa fazer isso agora, porém, como o scrip cria um grupo e altera permissões de pasta é necessário reiniciar o pc para que o windows aplique corretamente as permissões

grupo criado:

![image](https://user-images.githubusercontent.com/88493503/192855165-749d4d48-4f51-433f-9f22-c45e0c475a7e.png)


Reconfigurar arquivos e grupos:

Basta apertar a tecla 1 e deixar o programa seguir em frente, essa opção deve ser escolhida caso algum arquivo no programa tenha dado problema

Permitir ou negar acesso ao backup para o Administrador:

A pasta backup que se encontra em C:\Users\backup tem os backups feito pelo programa backup.py e nem mesmo o administrador tem acesso para fazer com que um ransomware não encripte eles (mesmo que a gente recomenda o backup em um sistema de cloud qualquer ransomware que rode como administrador não vai ter permissão de escrita e consequentemente não vai poder encriptar os arquivos) essas 2 opções servem para te dar acesso ao backup ou não.

>--------------

# Backup

O backup.py é executado sempre de 1 em 1 dia ao iniciar o backup ele vai pedir uma senha, essa senha vai ser usado para proteger um "shadow" do primeiro backup e ele se encontra em C:\Program Files(x86)\Backup)\backup compactado com uma senha e permissão 0 para Todos, essa medida é feita para que caso o primeiro backup tenha sido comprometido o segundo está lá para defender, lembre-se que para acessar o backup visualizar itens ocultos deve estar ativado, para isso clique em explorador de arquivos-Exibir-Itens ocultos

![image](https://user-images.githubusercontent.com/88493503/192856357-5f6cfc09-8eda-4409-a910-1e7cf4701231.png)

Dica: Sugerimos colocar uma cópia do backup na núvem para mais segurança, lembre-se também que nem o Administrador tem acesso a esse backup, para fazer com que se tenha acesso clique com o botão direito - propriedades - Segurança - Todos - Editar - Remover isso permite que qualquer um consiga acessar.

![Screenshot_4](https://user-images.githubusercontent.com/88493503/192856690-f700bb80-a8a0-44df-8d26-818e26170cf2.png)

>--------------

# Checador

O checador analisa pelos arquivos iscas criado no eula.py e se baseia em hash, hash é um cálculo matemático muito útil em checar integridades dos arquivos, caso ele detecte que o hash original do arquivo foi alterado ele começa a matar os processos mais recentes e aqueles que estão com alto uso de cpu, por isso pedimos para não alterar esses arquivos.


Dica - O programa funciona mesmo não sendo executado como Administrador, porém, pedimos que ele seja executado com o maior nível de privilégio para ter um sucesso maior

>--------------

# Informações adicionais

Vale ressaltar que esse script **NÃO** substitui a utilização de um programa de antivirus como o windows defender por exemplo, ele serve como um apoio e nem sempre vai detectar o vírus, porém, seu backup vai estar a salvo, sugerimos também colocar o backup na núvem, nunca compartilhar senhas, sempre desconfie de programas, nunca pague o resgate e por fim caso realmente tenha sido infectado leve o computador para um especialista técnico.
