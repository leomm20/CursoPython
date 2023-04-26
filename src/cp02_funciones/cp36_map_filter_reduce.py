
# MAP - aplica una función a cada uno de los elementos de una lista

enteros = [1, 2, 4, 7]
cuadrados = list(map(lambda x: x ** 2, enteros))
print(cuadrados)
print()

# otro ejemplo
def cuadrado(x):
    return x ** 2
def cubo(x):
    return x ** 3

enteros = [1, 2, 4, 7]
valores = list(map(lambda x: [cubo(x), cuadrado(x)], enteros))
print(valores)
print()

# otro ejemplo, agregando las funciones a una lista
funciones = [cubo, cuadrado]
enteros = [1, 2, 4, 7]
valores = []
for e in enteros:
    valores.append(list(map(lambda x: x(e), funciones)))
print(valores)
print()

# FILTER - Filtra una lista de elementos para los que una función devuelve True
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares = list(filter(lambda x: x % 2 == 0, valores))
print(pares)
print()

# REDUCE - cálculo acumulativo sobre una lista de valores y devolver el resultado
from functools import reduce

valores = [2, 4, 6, 5, 4]
suma = reduce(lambda x, y: x + y, valores)
print(suma)
print()