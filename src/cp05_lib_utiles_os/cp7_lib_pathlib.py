from pathlib import Path
import os

# ARMAR UNA RUTA
archivo = Path(os.getcwd(), 'dir1/dir2', 'dir11_file2.txt') # concatena strings
print(archivo)
print(archivo.name)  # nombre y extensión del archivo
print(archivo.stem)  # sólo nombre del archivo
print(archivo.suffix)  # sólo la extensión (incluye el punto)
print(archivo.read_text())  # lee el contenido del archivo
print(archivo.exists())  # indica si existe o no el archivo o directorio
print()

# CONSULTA POR UBICACIÓN DEL DIRECTORIO DEL USUARIO
base = Path.home()
print(base)
print()

# EJEMPLO DE USO PATH (pathlib)
base = Path.home()
ruta = Path(base, 'escritorio', Path('test/test_file.txt'))
print(ruta)
print()

# RUTA PADRE
ruta = Path(base, 'escritorio', Path('test/test_file.txt'))
print(ruta.parent)
print(ruta.parent.parent)
print(ruta.parent.parent.parent)
print(ruta.parent.parent.parent.parent)
print(ruta.parent.parent.parent.parent.parent)
print(ruta.parent.parent.parent.parent.parent.parent)

# RUTA A PARTIR DE OTRA
base = Path.home()
ruta = Path(base, 'escritorio', Path('test/test_file.txt'))
print(ruta.with_name('otro_nombre.xls'))
print(ruta.with_stem('cambia_solo_nombre'))
print(ruta.with_suffix('.doc'))  # cambia sólo la extensión

# FILTRAR ARCHIVOS (GLOB)
ruta = Path(os.getcwd(), 'dir1', 'dir2')
archivos_filtrados = ruta.glob('*.txt')
for a in archivos_filtrados:
    print(a)

# FILTRAR ARCHIVOS RECURSIVAMENTE (GLOB pero con doble asterisco)
ruta = Path(os.getcwd(), 'dir1')
archivos_filtrados = ruta.glob('**/*.txt')
for a in archivos_filtrados:
    print(a)

# RENOMBRAR ARCHIVOS O DIRECTORIOS
ruta = Path(os.getcwd(), 'dir1')
Path.rename(Path(ruta, 'dir2'), Path(ruta, 'dir2_nuevo_nombre'))
