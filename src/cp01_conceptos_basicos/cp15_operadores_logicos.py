"""
AND
A   B   Res
F   F   F
F   T   F
T   F   F
T   T   T

OR
A   B   Res
F   F   F
F   T   T
T   F   T
T   T   T
"""

print(1 == 1 and 1 == 2)  # retornará False
print(1 == 1 or 1 == 2)  # retornará True
print(not 1 == 1)  # retornará False
print()

print(True and False or False)  # retornará False
print(True or False and False)  # retornará True
print(True and False or False and True)  # retornará False

"""
De mayor a menor prioridad:
() paréntesis
** exponente
+x -x positivo, negativo
* / % // multiplicación, división, módulo, división de piso
+ - suma y resta
< <= > >= == != is in operadores de comparación
not negación
and operador lógico AND
or operador lógico OR
if else expresión condicional
lambda expresión lambda
= % /= //= -= += *= **= operadores de asignación
"""