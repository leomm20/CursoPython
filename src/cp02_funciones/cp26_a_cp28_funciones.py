# EJEMPLOS DE FUNCIÓN

# SIN PARÁMETROS
def saludar():
    print('Hola!')

saludar()
print()

# CON PARÁMETROS
def sumar_y_multiplicar_por_pi(num1, num2):
    return (num1 + num2) * 3.14

a = sumar_y_multiplicar_por_pi(8, 2)
b = sumar_y_multiplicar_por_pi(16, 3)
c = sumar_y_multiplicar_por_pi(a, b)
print(a, b, c)
print()


# CON FLUJO CONDICIONAL
def saludar(nombre, edad):
    if edad >= 75:
        segmento = 'longeva'
    elif edad >= 65:
        segmento = 'anciana'
    elif edad >= 55:
        segmento = 'adulta mayor'
    elif edad >= 45:
        segmento = 'adulta'
    elif edad >= 25:
        segmento = 'adulta joven'
    elif edad >= 18:
        segmento = 'joven'
    elif edad >= 12:
        segmento = 'adolescente'
    elif edad >= 5:
        segmento = 'niño'
    else:
        segmento = 'bebé'
    print(f'Hola {nombre}!')
    print(f'¿Sabías que según tu edad, {edad} años, sos una persona {segmento} según la OMS?\n')

saludar('Leo', 43)
print()


# PASAR LISTA COMO ARGUMENTO
def saludar2(personas):
    for persona in personas:
        print(f'Hola {persona[0]}! Tenés {persona[1]} años')

lista_personas = [['Roberto', 45], ['Milagros', 24], ['Lucía', 14], ['Claudio', 3], ['Ana', 11], ['Fernanda', 25],
                  ['Graciela', 56], ['Gerónimo', 85], ['Iván', 66]]
saludar2(lista_personas)
print()


# LLAMAR A UNA FUNCIÓN DESDE OTRA
def mezclar_con_blanco(color):
    diccionario_colores = {'rojo': 'rosa', 'azul': 'celeste', 'verde': 'verde claro'}
    print(f'\nEl color {color} mezclado con blanco, se transformará en {diccionario_colores[color]}')
def validar_color(color):
    if color in ['rojo', 'azul', 'verde']:
        return True
    else:
        return False
def preguntar_color():
    color = ''
    while not validar_color(color):
        color = input('ingresá un color (rojo, azul o verde): ')
    mezclar_con_blanco(color)

preguntar_color()
print()


# VALORES POR DEFECTO
def mi_funcion(coleccion: dict, flotante: float, entero: int = 1, booleano: bool = False):
    for k in coleccion:
        print(f'{k}:', coleccion[k])
        print(flotante)
        print(booleano)
        print(entero)

mi_funcion({'dos': 2, 'tres': 3}, 1.2, 5, True)
mi_funcion({'dos': 2, 'tres': 3}, 1.2, 5)  # entero tomará el valor por defecto 1
mi_funcion({'dos': 2, 'tres': 3}, 1.2)  # idem anterior y booleano será False

# OTRA FORMA DE PASAR ARGUMENTOS
mi_funcion(booleano=True, flotante=3.0, coleccion={'dos': 2, 'tres': 3})