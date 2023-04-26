bebidas_precios = {'Coca-cola': 600, 'Pepsi': 500, 'Manaos-cola': 200}
print(bebidas_precios['Manaos-cola'])
print()

# print(bebidas_precios['manaos'])  # dará error

precios = {'Bebidas': {'Coca-cola': 600, 'Pepsi': 500, 'Manaos-cola': 200},
           'Comidas': {'Pancho': 50, 'Hamburguesa': 75}, 'Propina_y_cubiertos': (100, 50)}
print(precios['Comidas']['Pancho'])
print(precios['Propina_y_cubiertos'])
print()

print(precios['Propina_y_cubiertos'][0])
print()

print(precios.keys())
print(precios.values())
print(precios.items())
print()

diccionario = {'llave': 1, 'llave2': 2}
x, y = diccionario.values()
print(x, y)
print()

x, y = diccionario
print(x, y)
print()

diccionario = {'a': 1, 'b': 2, 'c': 3}
diccionario.pop('b')
print(diccionario)
print()

diccionario.popitem()  # elimina la última llave-valor
