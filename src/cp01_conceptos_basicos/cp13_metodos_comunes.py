# max, min, sum
lista = [0, 1, 5, 3]
print(max(lista))
print(min(lista))
print(sum(lista))
print()
diccionario = {'a': 1, 'b': 2, 'c': 3}
print(max(diccionario))
print(min(diccionario))
print(max(diccionario.values()))
print(min(diccionario.values()))
print(sum(diccionario.values()))
print()
tupla = {0, 5, 33, 1}
print(max(tupla))
print(min(tupla))
print(sum(tupla))
print()
set1 = (1, 2, 55, 0)
print(max(set1))
print(min(set1))
print(sum(set1))
print()

# zip
tupla = (1, 2, 3, 4, (33, 22))
lista = ['a', 'b', 'c', 'd', 'e']
set1 = {44, 33, 41, 53, 56}
diccionario = {'a': 2, 'b': 5, 'f': 3, 'g': 9, 'h': 88}
zip_tupla = tuple(zip(tupla, diccionario.values()))
zip_lista = list(zip(lista, set1))
zip_set = set(zip(diccionario.values(), lista))
zip_diccionario = dict(zip(diccionario, tupla))
print(zip_tupla)
print(zip_lista)
print(zip_set)
print(zip_diccionario)

# ejemplo
nombres = ['Juan', 'María', 'Reina']
edades = (32, 45, 22)
ciudades = {'Buenos Aires', 'Rosario', 'Bariloche'}
vehiculos_precio = {'moto': 1000, 'patineta': 10, 'bicicleta': 20}
combinados = list(zip(nombres, edades, ciudades, vehiculos_precio))
for nombre, edad, ciudad, vehiculo in combinados:
    print(f'{nombre} tiene {edad} años, vive en {ciudad} y usa una {vehiculo} como vehículo')
