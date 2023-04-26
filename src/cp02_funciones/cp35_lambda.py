print((lambda x, nro: x + nro)(2, 3))
print()

(lambda: print('Hola mundo!'))()
print()

suma_condicional = lambda x, nro: x + nro
print(suma_condicional(2, 3))
print()

y = (lambda x, nro: x + nro if x > 2 else None)(2, 3)
print(y)
print()

lista_nros = [1, 2, 3]
decimal = 2.0
print((lambda lista, nro: [e + nro for e in lista])(lista_nros, decimal))
