palabra = 'Python'
lista = []
for letra in palabra:
    lista.append(letra)
print(lista)
print()

lista = [letra for letra in 'Python']
print(lista)
print()

lista = [n/2 for n in range(0, 10) if n > 2]
print(lista)
print()

lista = [n for n in range(0, 10) if n > 2]
print(lista)
print()

lista = [n/2 if n > 2 else 'no' for n in range(0, 10)]
print(lista)
print()

lista_celsius = [21, 39.5, -10, 0, 15]
lista_fahrenheit = [c * 9/5 + 32 for c in lista_celsius]
print('Celsius:', lista_celsius)
print('Fahrenheit:', lista_fahrenheit)
