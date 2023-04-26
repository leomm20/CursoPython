import configparser
import sys
import os

if not os.path.exists("config.ini"):
    file_config = open('config.ini', 'w')
    file_config.write("[DEFAULT]\n")
    file_config.write(f"dir1={os.getcwd()}\n")
    file_config.close()
    print("#####")
    print("##### VERIFICAR CONTENIDO DE CONFIG.INI Y VOLVER A EJECUTAR:"
          "\n##### " + os.path.join(os.getcwd(), "config.ini"))
    print("#####")
    sys.exit()

config = configparser.ConfigParser()
config.read('config.ini')
section = "DEFAULT"
if section not in config:
    print("#####")
    print("##### Verificar etiqueta de configuración")
    print("#####")
    sys.exit()
dir1 = config[section]["dir1"]
print('\nLeído:', dir1)
