# GENERAR NÚMERO ENTERO
from random import randint
print(randint(0, 10))
print()

# GENERAR NÚMERO ENTRE 0 Y 1
from random import random
print(random())
print()

# ELEGIR 1 VALOR ENTRE LOS VALORES DE UNA LISTA O TUPLA (no funciona con diccionarios y sets)
from random import choice
lista_nombres = ['Maria', 'Juan', 'Pedro', 'Cristina']
print(choice(lista_nombres))

