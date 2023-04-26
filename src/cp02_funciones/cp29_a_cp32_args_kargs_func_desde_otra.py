# *args (tupla)
def sumar_varios(*args):
    resultado = 0
    for a in args:
        resultado += a
    return resultado

print(sumar_varios(1, 1, 1))
print()

# **kargs (diccionario)
def operacion_matematica(**kwargs):
    resultado = 0
    if kwargs['operacion'] == '-':
        resultado = kwargs['a'] - kwargs['b']
    elif kwargs['operacion'] == '*':
        resultado = kwargs['a'] * kwargs['b']
    elif kwargs['operacion'] == '/':
        resultado = kwargs['a'] / kwargs['b']
    elif kwargs['operacion'] == '**':
        resultado = kwargs['a'] ** kwargs['b']
    else:
        resultado = kwargs['a'] + kwargs['b']
    return round(resultado, 3)

print(operacion_matematica(a=2, b=3, operacion='+'))
print(operacion_matematica(a=2, b=3, operacion='-'))
print(operacion_matematica(a=2, b=3, operacion='*'))
print(operacion_matematica(a=2, b=3, operacion='/'))
print(operacion_matematica(a=2, b=3, operacion='**'))
print(operacion_matematica(a=2, b=1/3, operacion='**'))
print()


# USO DE GLOBAL
# Lo ideal es no tener nombres iguales dentro y fuera de una función, a fin de evitar conflictos.

# esta función actuará sobre la variable externa, lo cual no es lo ideal
def saludar1():
    print(texto)

# esta otra utilizará su propia variable, por más que se llame igual a la que está afuera
def saludar2():
    texto = 'Hola'
    print(texto)

# IDEAL para actuar sobre la variable externa
def saludar3():
    global texto
    texto = 'Hola'
    print(texto)

texto = 'Chau'
# 1
saludar1()
print(texto)
print()
# 2
saludar2()
print(texto)
print()
# 3
saludar3()
print(texto)
print()


# FUNCIÓN COMO ARGUMENTO

# usando global
def saludar4():
    global nombre
    print(f'Hola {nombre}!')
def despedir(funcion):
    global nombre
    print(f'Chau {nombre}!')

nombre = 'Juan'
despedir(saludar4())


# usando variables propias (ideal)
def saludar5(nombre):
    print(f'Hola {nombre}!')
    return nombre
def despedir5(funcion):
    nombre_ = funcion
    print(f'Chau {nombre_}!')

name = 'Juan'
despedir5(saludar5(name))
print()


# FUNCIÓN EN VARIABLE
def saludar6(name):
    print(f'Hola {name}')
    return 0

llamar_funcion = saludar6('Pedro')
print(llamar_funcion)
print()

# otro ejemplo
def saludar7(nombre):
    print(f'Hola {nombre}!')
    return nombre
def despedir7(funcion):
    nombre = funcion
    print(f'Chau {nombre}!')
    return 0

llamar_funcion = despedir7(saludar7('Pedro'))
print(llamar_funcion)
print()

