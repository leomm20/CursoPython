from os import getcwd, makedirs
# o directamente
import os

# OBTIENE EL DIRECTORIO DONDE SE ENCUENTRA ESTE ARCHIVO
print(getcwd())  # usando from os import getcwd
print()

# CAMBIA DE DIRECTORIO
print(os.getcwd())  # usando import os
os.chdir('C:\\1CursoPython\\CursoPython')
print(os.getcwd())
os.chdir('C:\\1CursoPython\\CursoPython\\src\\cp05_lib_utiles_os')
print()

# CREA UN DIRECTORIO
if not os.path.exists('dir_test'):
    makedirs('dir_test')

# UNIÓN DE RUTAS
ruta = os.path.join(os.getcwd(), 'mi_archivo4.txt')
print(ruta)

# DIRECTORIO BASE (mismo funcionamiento tanto para archivo como para directorio)
print(os.path.dirname(ruta))

# NOMBRE DE ARCHIVO (mismo funcionamiento tanto para archivo como para directorio)
print(os.path.basename(ruta))
print()

# LISTA DIRECTORIOS Y ARCHIVOS QUE ESTÉN EN EL DIRECTORIO
print(os.listdir())
print()

# ES UN DIRECTORIO?
print(os.path.isdir(r'C:\1CursoPython\CursoPython\src\cp05_lib_utiles_os\__init__.py'))
print()

# ES UN ARCHIVO?
print(os.path.isfile(r'C:\1CursoPython\CursoPython\src\cp05_lib_utiles_os\__init__.py'))
print()

# RECORRE EL ARBOL DE DIRECTORIOS Y ARCHIVOS
caminos = os.walk(os.path.dirname(os.getcwd()))
for c in caminos:
    print(c)
print()

os.system('date')  # muestra fecha y pide actualización (dar Enter en la Terminal para continuar)
os.system('notepad')  # abre el notepad (en windows)
os.system('cls')  # borra el contenido de la consola

# Este último sólo funciona en cmd (símbolo de sistema), no en la terminal de PyCharm.
# Para la consola, una alternativa sería la siguiente:
def clear():
    os.system('cls')
    print('\n'*1000)

print()

"""
os.replace() y os.rename()
Ambos métodos permiten modificar el nombre y ubicación de un archivo o directorio.
La diferencia entre ambos, es que rename() dará un error si el archivo o directorio ya 
existe, mientras que replace(), si es un archivo, lo sobreescribirá, si, en cambio, es un 
directorio, también dará un error.
"""

# RMDIR - ELIMINAR UN DIRECTORIO (si no está vacío, dará un error)
# REMOVE - ELIMINAR UN ARCHIVO
dir_actual = os.getcwd()
os.chdir(os.path.join(os.getcwd(), 'dir_test'))
for e in os.listdir():
    if os.path.isfile(e):
        os.remove(e)
    else:
        os.rmdir(e)
os.chdir(dir_actual)
os.rmdir('dir_test')

