lista = ['a', 1, 'b', 2.22, 'z']
print(lista[4])
print(len(lista))
print(lista[1:4])
print()

lista = [1, 2, 3]
lista2 = [4, 5, 6]
print(lista + lista2)
print()

lista = [1, 2, 3]
x, y, z = lista
print(x, y, z)
print()

lista = [1, 2, 3]
lista[1] = 'a'
print(lista)
print()

lista = [1, 2, 3]
lista.append('b')
print(lista)
print()

lista = [1, 2, 3, 4, 5]
borrado = lista.pop(1)
print(lista)
print(borrado)
print()

lista = [3, 2, 1.11, 88, 1]
lista.sort()
print(lista)
print()

nueva_lista = lista.sort()
print(type(nueva_lista))
print()

lista = [3, 2, 'a', 88, 1.11]
# lista.sort()  # dará un error

lista = [3, 2, 1.11, 88, 1]
lista.reverse()
print(lista)
print()

lista = [1, 2, 3, 1]
print(lista.count(1))
print()

lista = [1, 2, 1]
print(lista.index(1, 1))
print()

lista.clear()
