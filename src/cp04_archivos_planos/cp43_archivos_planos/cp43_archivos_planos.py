print('# LEER TO.DO EL CONTENIDO')
archivo = open('mi_archivo.txt', 'r')
contenido = archivo.read()
print(type(contenido))
print(contenido)
archivo.close()
print('#'*10)

print('# OTRA FORMA, sin utilizar funciones')
archivo = open('mi_archivo.txt', 'r')
for linea in archivo:
    print(linea, end='')
print()
archivo.close()
print('#'*10)

print('# LEER TO.DO EL CONTENIDO, CON SALIDA COMO LISTA')
archivo = open('mi_archivo.txt', 'r')
contenido = archivo.readlines()
print(type(contenido))
print(contenido)
archivo.close()
print('#'*10)

print('# OTRA FORMA, USANDO readlines()')
archivo = open('mi_archivo.txt', 'r')
lineas = archivo.readlines()
for linea in lineas:
    # print(linea, end='')
    print(linea.strip())
# print()
print('#'*10)

print('# LEER LÍNEA POR LÍNEA (PUNTERO)')
archivo = open('mi_archivo.txt', 'r')
print(archivo.readline(), end='')
print(archivo.readline(), end='')
archivo.close()
print('#'*10)

# ESCRIBIR (borrando su contenido)
archivo = open('mi_archivo2.txt', 'w')
archivo.write('Hola!\nEsta es una\nprueba!\n')
archivo.close()

# ESCRIBIR (agregando al contenido existente
archivo = open('mi_archivo2.txt', 'a')
archivo.write('Línea agregada')
archivo.close()

# WRITELINES

# Acepta iteradores, aunque sólo strings
archivo = open('mi_archivo3.txt', 'w')
diccionario = {'a': 1, 'b': 2}
archivo.writelines((str(diccionario.keys()), str(diccionario.values())))
archivo.write('\n')
lista = ['a', 'b', 'c']
archivo.writelines(lista)
archivo.write('\n')
set1 = {'d', 'e', 'f'}
archivo.writelines(set1)
archivo.write('\n')
tupla = ('g', 'h', 'i')
archivo.writelines(tupla)
archivo.close()


# Si contienen números, la alternativa sería agregar str()
archivo = open('mi_archivo4.txt', 'w')
diccionario = {'a': 1, 'b': 2}
archivo.writelines((str(diccionario.keys()), str(diccionario.values())))
archivo.write('\n')
lista = [1, 2, 3]
archivo.writelines(str(lista))
archivo.write('\n')
set1 = {4, 5, 6}
archivo.writelines(str(set1))
archivo.write('\n')
tupla = (7, 8, 9)
archivo.writelines(str(tupla))
archivo.close()

