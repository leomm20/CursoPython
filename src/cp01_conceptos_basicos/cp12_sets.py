set1 = set([1, 2, 'a', 'b'])
set2 = {1, 2, 'a', 'b'}
print()

set1 = {1, 2, 'a', 'b'}
set1.add('c')
set1.add('a')
print(set1)
print()

set1 = {'a', 'b', 'c'}
set1.discard('b')
print(set1)
print()

set1.pop()  # elimina aleatoriamente
set1.clear()  # elimina to.do el contenido
print()

set1 = {1, 2, 3}
set2 = {4, 5, 6}
set3 = set1.union(set2)
print(set3)
print()

set1 = {1, 2, 3, 4}
set2 = {4, 1, 6}
print(set1.difference(set2))
print(set2.difference(set1))
print()

set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.intersection(set2))
print()

set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.symmetric_difference(set2))
print()