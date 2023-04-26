
# DECORADORES
def despedir(funcion):
    def nueva_funcion(nombre_):
        funcion(nombre_)
        print(f'Chau {nombre_}!')
    return nueva_funcion

@despedir  # DECORADOR
def saludar(nombre):
    print(f'Hola {nombre}!')
    return nombre

saludar('Viviana')
print()

# GENERADORES
def restar():
    x = "Te quedan 2 vidas"
    yield x
    x = "Te queda 1 vida"
    yield x
    x = "Game Over"
    yield x

perder_vida = restar()
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
# si se ejecuta 1 vez más, dará un error
print()

# otro ejemplo
def generar():
    x = 1
    yield x
    while True:
        x += 1
        yield x

generador = generar()
for i in range(1, 3):
    print(next(generador))
print()

# otro, gestor de turnos
def generar_turno(seccion):
    x = 1
    yield f'{seccion}: {x}'
    while True:
        x += 1
        yield f'{seccion}: {x}'

turno_retiro_estudios = generar_turno('RET')
turno_laboratorio = generar_turno('LAB')
for i in range(1, 4):
    print(next(turno_retiro_estudios))
for i in range(1, 3):
    print(next(turno_laboratorio))
for i in range(1, 4):
    print(next(turno_retiro_estudios))
for i in range(1, 3):
    print(next(turno_laboratorio))
print()