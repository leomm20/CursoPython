# Counter

from collections import Counter

print(Counter("texto"))
print(Counter("la vaca Lola, la vaca Lola, tiene cabeza y tiene cola".split()))
print()

lista = [1, 1, 1, 2, 3, 4, 23, 52, 2, 32, 2, 32, 3, 3, 3, 2, 2, 2, 2, 1, 1]
print(Counter(lista))
print()

print(Counter(lista).most_common())
print(Counter(lista).most_common(2))


# defaultdict

from collections import defaultdict
mi_dict1 = {'uno': 1, 'dos': 2, 'tres': 3}
# print(mi_dict1['cuatro']) # Dará un error, finalizando el programa
mi_dict2 = defaultdict(lambda: 'Sin valor')
for k in mi_dict1.keys():
    mi_dict2[k] = mi_dict1[k]
print(mi_dict2['tres'])
print(mi_dict2['cuatro'])


# namedtuple

from collections import namedtuple
Persona = namedtuple("Persona", ["nombre", "altura", "peso"])
leo = Persona("Leo", 1.71, 70)
print(leo)

print(leo.altura)
print(leo[1])

# deque
from collections import deque # puede agregar o quitar por izq o der
lista_ciudades = deque(["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])
print(lista_ciudades)
lista_ciudades.appendleft("BsAs")
lista_ciudades.append('Córdoba')
print(lista_ciudades)
print(lista_ciudades[0])
print(lista_ciudades[-1])
