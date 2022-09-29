import os
from time import sleep

print("Instalando as libs.....")

sleep(2)


os.system("pip install pywin32")
os.system("pip install requests")
os.system("pip install py7zr")
os.system("pip install pysimplegui")
os.system("pip install signals")


input("Você já pode rodar o eula.py ou eula.exe")