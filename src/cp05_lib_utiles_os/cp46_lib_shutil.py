import shutil

# COPIA ARBOL COMPLETO
shutil.copytree('dir1', 'dir2')

# ELIMINA ARBOL DE DIRECTORIO - ATENCIÓN!!! BORRA SIN IMPORTAR SI CONTIENE ARCHIVOS/DIRECTORIOS O NO!!!
# shutil.rmtree('dir2')

# MUEVE ARCHIVOS Y DIRECTORIOS
shutil.move('dir1/dir11/dir11_file1', 'dir1/dir/dir11_file1')

# COPIA Y RENOMBRA ARCHIVOS Y DIRECTORIOS
shutil.copy('dir1/dir11/dir11_file1', 'dir1/dir/dir11_file1')

# GENERA ARCHIVO COMPRIMIDO DEL DIRECTORIO, INCLUIDOS LOS SUBDIRECTORIOS
shutil.make_archive('test', 'zip', 'dir1')

# DESCOMPRIME ARCHIVO EN EL INDICADO EN EL 2DO ARGUMENTO
shutil.unpack_archive('test.zip', '1')
