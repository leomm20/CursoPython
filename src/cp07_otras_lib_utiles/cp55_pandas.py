import pandas as pd

tipos_autos = pd.Series(['sedan', 'suv', 'pickup'])
colores = pd.Series(['verde', 'rojo', 'violeta'])
tabla_autos = pd.DataFrame({'Tipo de autos': tipos_autos, 'Color': colores})
print(tabla_autos)
print()

print(tabla_autos.iloc[0, 0])
print(tabla_autos['Tipo de autos'][0])
print()

kilometraje = pd.Series([134000, 45000, 234000])
tabla_autos = tabla_autos.assign(Kilometraje=kilometraje)
print()

duenio = pd.Series(['Carlos', 'Pedro', 'Juan'])
tabla_autos.insert(2, 'Dueño', duenio)
print()

# agregar nueva línea
tabla_autos.loc[len(tabla_autos)] = {'Tipo de autos': 'utilitario', 'Color': 'gris',
                                     'Dueño': 'Leo', 'Kilometraje': 38000}

# o más de una
nueva_linea = pd.DataFrame({'Tipo de autos': ['utilitario'], 'Color': ['gris'],
                            'Dueño': ['Leo'], 'Kilometraje': [38000]})
tabla_autos = pd.concat([tabla_autos, nueva_linea], ignore_index=True)
print(tabla_autos)
print()

# agrega dataframe con 2 líneas
nueva_linea = pd.DataFrame({'Tipo de autos': ['utilitario', 'cuatriciclo'],  'Color': ['gris', 'negro'],
                            'Dueño': ['Leo', 'José'], 'Kilometraje': [38000, 21600]})
tabla_autos = pd.concat([tabla_autos, nueva_linea], ignore_index=True)
print(tabla_autos)
print()

# iloc vs loc
codigos = pd.CategoricalIndex(['9988', '9944', '3344'])
tipos_autos = pd.Series(['sedan', 'suv', 'pickup'])
colores = pd.Series(['verde', 'rojo', 'violeta'])
kilometraje = pd.Series([134000, 45000, 234000])
duenio = pd.Series(['Carlos', 'Pedro', 'Juan'])
tabla_autos = pd.DataFrame({'Tipo de autos': tipos_autos, 'Color': colores,
                            'Dueño': duenio, 'Kilometraje': kilometraje})
tabla_autos.index = codigos
tabla_autos.index.name = 'Códigos'
nueva_linea = pd.DataFrame({'Tipo de autos': ['utilitario'], 'Color': ['gris'],
                            'Dueño': ['Leo'], 'Kilometraje': [38000]}, index=['8833'])
nueva_linea.index.name = 'Códigos'
tabla_autos = pd.concat([tabla_autos, nueva_linea])
print(tabla_autos)
print()
# con indice nombrado
print(tabla_autos.loc['3344', 'Kilometraje'])
print(tabla_autos.iloc[2, 3])
# sin indice nombrado
# print(tabla_autos.loc[2, 'Kilometraje'])

# max, min, mean (promedio)
print(tabla_autos['Kilometraje'].max())
print(tabla_autos['Kilometraje'].min())
print(tabla_autos['Kilometraje'].mean())  # promedio
print()

print(tabla_autos.sort_values('Dueño'))
print(tabla_autos.sort_values('Códigos'))
print()

tabla_autos.to_csv('tabla_autos.csv')
mi_csv = pd.read_csv("tabla_autos.csv")
print(mi_csv)