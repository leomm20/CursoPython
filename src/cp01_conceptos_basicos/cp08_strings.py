palabra = 'Python'
print(palabra[1])  # y
print(palabra[-2])  # o
print(palabra[1:3])  # yt
palabra = 'Colaboración'
print(palabra[1:8:2])  # oaoa
print(palabra[:8:2])  # Clbr
print(palabra[1::2])  # oaoain
print(palabra[::-1])  # nóicarobaloC
print()

cadena = 'Colaborar'
posicion_find = cadena.find('o')
print(posicion_find)  # 1
print()

cadena = 'Colaborar'
posicion_find = cadena.find('o')
segunda_posicion_find = cadena.find('o', posicion_find + 1)
print(posicion_find)
print(segunda_posicion_find)
# 1
# 5
print()

cadena = 'Colaborar'
posicion_find = cadena.find('o')
segunda_posicion_find = cadena.find('o', posicion_find + 1)
tercera_posicion_find = cadena.find('o', segunda_posicion_find + 1)
print(posicion_find)
print(segunda_posicion_find)
print(tercera_posicion_find)
"""
1
5
-1
"""
print()
print(cadena.find('o', 2, 4))  # -1
print()

# in
cadena = 'Agua de mar'
print('de' in cadena)
print('De' in cadena)
print()

cadena = '''
Esto
es
un
poema
'''
print(cadena)
print()

print(cadena.find('es'))  # 6
print()

"""
len() => indica la cantidad de caracteres que tiene una cadena
upper() => pasa toda la cadena a minúsculas
lower() => pasa toda la cadena a mayúsculas
split() => separa cada letra en un item de una lista
join() => une cadenas según un separador
replace() => reemplaza un substring en una cadena
strip() => quita espacios y saltos de línea
"""

cadena = 'Esto es una prueba'
lista = cadena.split()
print(lista)
print()

a = 'Esto'
b = 'es'
c = 'una'
d = 'prueba'
cadena = ' '.join([a, b, c, d])  # El espacio es la unión entre las cadenas
print(cadena)
print()

cadena = 'Esto es una prueba'
cadena = cadena.replace('Esto', 'Esta')
print(cadena)
print()

cadena = '55' * 10
print(cadena)
print()

cadena = ' Hola, cómo estás? \n'
print('-' + cadena + '-')
cadena = cadena.strip()
print('-' + cadena + '-')
