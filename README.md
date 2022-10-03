![85b4b690-b807-447b-ac68-31e7f51c519b](https://user-images.githubusercontent.com/88493503/192865524-96caaa45-5a7c-4939-998a-8a860046c13f.jpg)


# Apenas em Windows

> Obs: Anti-Malware-Operation é uma empresa **fictícia** qualquer semelhança são meras conhecidências

## Script python que protege o backup de seus arquivos e checa por ransomwares na máquina se baseando em tempo e uso de processador

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
👜 py7zr

>📚Bibliotecas📚

obs: Python versão 3 deve ser instalado, todas as bibliotecas devem estar instalados na máquina. O uso de internet é OBRIGATÓRIA durante o eula

> OBS

Sugerimos não rodar aplicativos não reconhecidos como modo administrador, o script é obrigatório rodar como Administrador no backup e no eula, o checador é aconselhável rodar também com o privilégio mais alto, caso contrário algumas coisas não poderão ser feitas por falta de privilégios

>--------------

# Setup

Antes de iniciar o programa por favor inicie o setup.py, ele vai instalar as bibliotecas necessárias, caso haja algum erro com o pip siga o tutorial no próprio site do python de comno resolver.

python setup.py

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

Aqui você deve digitar suas contas o programa não consegue ainda detectar se a conta digitada é válida no sistema operacional então preste muito atenção nesta parte, após digitar ele vai perguntar se você quer continuar, caso positivo aperte S se não aperte N e enter

Configuração2:

Aqui você vai poder escolher o tipo de backup:

1 - Backup padrão (Pastas como Desktop, Documents, Downloads)

2 - Pastas padrões e suas escolhas (Desktop, Documents, Download e pastas que você escolher)

3 - Apenas minhas escolhas ( Você escolhe as pastas)

![Screenshot_3](https://user-images.githubusercontent.com/88493503/192853827-94353f1b-3799-4de7-a8eb-bd7934e043d4.png)

Configuração3:

![image](https://user-images.githubusercontent.com/88493503/193648407-e01ede33-8dab-4fa3-8162-e122536af253.png)

O programa agora vai criar arquivos Dummy/iscas que vão servir para detectar se um ransomware está na máquina, pedimos para NÃO alterar esses arquivos que se encontra na pasta filesran!!!

Caso você tenha escolhido a primeira opção além de criar os arquivos iscas nos locais citados acima o programa vai criar também nos locais que você escolheu, vale ressaltar que a pasta precisa ter sido antes criada, por exemplo se você quer colocar esses arquivos em uma pasta chamada detectador na sua área de trabalho essa pasta detectador precisa estar já criada antes de selecionar ela, vale lembrar também que caso você reinicie as configurações apenas a pasta com os arquivos iscas "filesran" são deletados e não a pasta que você escolheu para receber os arquivos

Em seguida ele vai criar links simbólicos e vai mover todos os arquivos para a pasta C:\Program Files(x86)\Backup é por aqui que os executáveis se encontram e você pode apenas executar eles pelo link simbólico que se encontra na área de trabalho na pasta anti-malware-operation

Em seguida pedimos que reinicia o computador, você não precisa fazer isso agora, porém, como o script cria um grupo e altera permissões de pasta é necessário reiniciar o pc para que o windows aplique corretamente as permissões

grupo criado:

![image](https://user-images.githubusercontent.com/88493503/192855165-749d4d48-4f51-433f-9f22-c45e0c475a7e.png)

Reconfigurar arquivos e grupos:

Basta apertar a tecla 1 e deixar o programa seguir em frente, essa opção deve ser escolhida caso algum arquivo no programa tenha dado problema

Permitir ou negar acesso ao backup para o Administrador:

A pasta backup que se encontra em C:\Users\backup tem os backups feito pelo programa backup.py e nem mesmo o administrador tem acesso para fazer com que um ransomware não encripte eles (mesmo que a gente recomende o backup em um sistema de cloud, qualquer ransomware que rode como administrador não vai ter permissão de escrita e consequentemente não vai poder encriptar os arquivos) essas 2 opções servem para te dar acesso ao backup ou não.

>--------------

# Backup

O backup.py é executado sempre de 1 em 1 dia ao iniciar o backup ele vai pedir uma senha, essa senha vai ser usado para proteger um "shadow" do primeiro backup e ele se encontra em C:\Program Files(x86)\Backup)\backup compactado com uma senha e permissão 0 para Todos, essa medida é feita para que caso o primeiro backup tenha sido comprometido o segundo está lá para defender, lembre-se que para acessar o backup o visualizar itens ocultos deve estar ativado, para isso clique em explorador de arquivos- Exibir - Itens ocultos

![image](https://user-images.githubusercontent.com/88493503/192856357-5f6cfc09-8eda-4409-a910-1e7cf4701231.png)

Dica: Sugerimos colocar uma cópia do backup na núvem para mais segurança, lembre-se também que nem o Administrador tem acesso a esse backup, para fazer com que se tenha acesso clique com o botão direito - propriedades - Segurança - Todos - Editar - Remover isso permite que qualquer um consiga acessar.

![Screenshot_4](https://user-images.githubusercontent.com/88493503/192856690-f700bb80-a8a0-44df-8d26-818e26170cf2.png)

O programa também loga todos os dias que o backup foi ativado, ele se encontra em C:\backupconfig\backup_logs

![image](https://user-images.githubusercontent.com/88493503/193089736-d7c77e2b-3fcf-4b03-bce9-dcc97c16cf22.png)


>--------------

# Checador

O checador analisa pelos arquivos iscas criado no eula.py e se baseia em hash, hash é um cálculo matemático muito útil em checar integridades dos arquivos, caso ele detecte que o hash original do arquivo foi alterado ele começa a matar os processos mais recentes e aqueles que estão com alto uso de cpu, por isso pedimos para não alterar esses arquivos.

Quando o programa detectar os processos mais recentes ou que estão com alto uso na cpu além de te avisar pela linha de comandos ele te avisa que um ransomware foi detectado e cataloga essas informações em C:\backupconfig\logs_antimalware

![image](https://user-images.githubusercontent.com/88493503/193090541-0a0c77df-788c-42a1-9881-e4d9dfc76695.png)

Aqui você vê um dos arquivos iscas em seu estado normal ou seja sem nenhum erro, vamos ver caso a gente altere sua extensão ou seu conteudo

![image](https://user-images.githubusercontent.com/88493503/193090786-710c1f19-3f18-4e15-a5b3-c845d128dd9b.png)

![image](https://user-images.githubusercontent.com/88493503/193090917-1ca0a69a-3f8c-4cc8-a750-29c9e55c6e78.png)

O nosso programa detecta essa mudança matou os processos recentes que nesse caso foi o Taskmgr.exe e matou também o notepad.exe ambos foram um teste em seguida ele avisa que houve uma detectação:

![image](https://user-images.githubusercontent.com/88493503/193091041-44e4d870-f5c1-4761-97a9-0bcfd99823e8.png)

se checarmos nos logs:

![image](https://user-images.githubusercontent.com/88493503/193091082-08fd8046-8b83-450c-88fc-b7f09bc82a62.png)



Dica - O programa funciona mesmo não sendo executado como Administrador, porém, pedimos que ele seja executado com o maior nível de privilégio para ter um sucesso maior

>--------------

# Interface Gráfica

![image](https://user-images.githubusercontent.com/88493503/193103935-bebfc73d-741b-45e7-8ea5-751cd16da7e8.png)

O programa possui uma interface gráfica caso não queria usar a linha de comandos, ela conecta todos os nossos programas em 1 só, é igual a cli,porém, com alguns botões e informações mais interativas, caso tenha dúvida cheque a documentação nesse github

>--------------

# Informações adicionais

Vale ressaltar que esse script **NÃO** substitui a utilização de um programa de antivirus como o windows defender por exemplo, ele serve como um apoio e nem sempre vai detectar o vírus, porém, seu backup vai estar a salvo, sugerimos também colocar o backup na núvem, nunca compartilhar senhas, sempre desconfie de programas, nunca pague o resgate e por fim caso realmente tenha sido infectado leve o computador para um especialista técnico.

Icon made by: https://www.flaticon.com/free-icon/bug_14410#

Version 2.0

2 - Principal 

0 - Correção de bugs

>--------------

# Patch Notes

Adiciona a opção escolher pasta para receber os arquivos iscas e correção 
