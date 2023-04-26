animales = ['Perro', 'Gato', 'Conejo', 'Oso', 'Cebra']
for animal in animales:
    animal = animal.upper()
    print(animal)
print()

clima_semana = {'lunes': 'nublado', 'martes': 'lluvioso', 'miércoles': 'soleado'}
for dia, clima in clima_semana.items():
    print(f'El {dia} estará {clima}')
print()

for i in range(len(animales)):
    animal = animales[i].upper()
    print(animal)
print()

for i in range(1, 4):
    print(animales[i].upper())
print()

for i in range(0, 5, 2):
    print(animales[i].upper())
print()

for i in range(-1, -4, -2):
    print(animales[i].upper())
print()

suma = sum(range(4, 11, 2))
print(suma)
print()

lista = ['a', 'b', 'c', 'd']
for indice, item in enumerate(lista):
    print(f'{indice}: {item}')
print()

for indice, valor in enumerate(range(0, 10, 2)):
    print(f'{indice}: {valor}')
