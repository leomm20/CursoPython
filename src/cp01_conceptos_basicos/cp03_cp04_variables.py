nombre = 'Juan'
apellido = 'Pérez'
numero_1 = 123
numero_2 = 456
print(apellido + ', ' + nombre)
suma = numero_1 + numero_2
print(suma)
print()

# INGRESO DE DATOS POR CONSOLA
nombre = input('Ingresá tu nombre: ')
edad = input('Ingresá tu edad: ')
print('Te llamás ' + nombre + ' y tenés ' + edad + ' años')
print()

un_numero = input('Ingresá un número: ')
otro_numero = int(input('Ingresá otro número: '))
print(int(un_numero) + otro_numero)
print(type(un_numero))
print(type(otro_numero))
print()

nro = 2
nro2 = 2.0
suma = nro + nro2
print(suma)
print(type(suma))
print()

# Declarar tipo de variable
entero: int = 0
decimal: float = 10.0
print(type(entero), type(decimal))
# solamente sirve como información para quien utiliza el IDE, porque se ejecutará igual si ponemos otro tipo de dato:
entero: int = 11.02  # el IDE marca error, pero se ejecutará igual
print(type(entero))

"""
Reglas nombres de las variables:
1- Unidad: los nombres que lleven más de una palabra, se separarán con un guión bajo: 
mi_variable
2- Fácilmente identificable: nombre_perro
3- Obviar el hispanismo (si bien el intérprete lo podrá ejecutar, el IDE te lo marcará como 
algo a corregir, es decir, como warning y no como error): año => anio, nombre_árbol => 
nombre_arbol
4- Deben comenzar siempre con una letra: mes_8
5- Y no pueden contener ninguno de los siguientes signos: :”’,<>/?|()!@#$%^&*~-+
6- No pueden llamarse como las palabras clave, reservadas por Python, ej.: print, input, 
string, int. En tal caso, utilizar: mi_print, mi_input, etc
"""