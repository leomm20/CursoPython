numeros = (1, 2, 3)
numeros2 = 4, 5, 6
print()

tupla = (1, 2, 3)
lista = list(tupla)
lista.append(4)
tupla = tuple(lista)
print(tupla)
print()

tupla = (1, 2, 3)
x, y, z = tupla
print(x, y, z)
print()

tupla = (1, 2, 1)
print(tupla.count(1))
print()

tupla = ('a', 1, 'c', 'd', 'c')
print(tupla.index('c', 3))
