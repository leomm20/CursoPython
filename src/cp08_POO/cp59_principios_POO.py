print('# IDENTIDAD')


class Perro:
    pass


# perro 1 es único
# perro 2 y 3 hacen referencia al mismo objeto
perro1 = Perro()
perro2 = Perro()
print(perro1)
print(perro2)
perro3 = perro2
print(perro3)
del perro2
print(perro3)
print('\n############\n')


print('# RECOLECCIÓN DE BASURA (en memoria)')

import gc
print(gc.isenabled())
print(gc.get_count())
del perro3
print(gc.get_count())
perro4 = Perro()
print(gc.get_count())
print('\n############\n')


print('# HERENCIA')


class Animal:
    pelaje = 'pelo corto'

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        pass

    def moverse(self):
        print('Se movió')


class Perro(Animal):
    def __init__(self, nombre, cantidad_patas):
        super().__init__(nombre)
        self.patas = cantidad_patas

    def hablar(self):
        print('woof, woof!')


perro = Perro('Felipe', 4)
print(perro.nombre)
print(perro.patas)
print(perro.pelaje)
perro.hablar()
perro.moverse()
print('\n############\n')


print('# HERENCIA MÚLTIPLE')


class Padre:
    nombre = 'Padre'

    def hablar(self):
        print('Soy el padre')


class Madre:
    __nombre = 'Madre'

    def hablar(self):
        print('Soy la madre')


class Hija(Madre, Padre):
    pass


hija = Hija()
hija.hablar()
print(hija.nombre)
print('\n############\n')


print('# PRIORIDAD DE HERENCIA')
print(Hija.__mro__)
print('\n############\n')


print('# ENCAPSULAMIENTO')


class Perro:
    __rabo = True

    def __tiene_rabo(self):
        return self.__rabo

    def mover_rabo(self):
        if self.__tiene_rabo():
            print('Movió el rabo')
        else:
            print('No tiene rabo')


perro = Perro()
perro.mover_rabo()
# print(perro.__rabo)  # esto dará un error en el IDE, y si se ejecuta, el programa finalizará con exit code 1
print('\n############\n')


print('# POLIMORFISMO')


class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice muuh")


class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice meeh")


oveja = Oveja("pedro")
vaca = Vaca("juana")
animales = [oveja, vaca]
for animal in animales:
    animal.hablar()
print('\n############\n')


print('# EN ESTE OTRO EJEMPLO, TAMBIÉN SE OBSERVA EL POLIMORFISMO')


def animal_habla(object):
    object.hablar()


animal_habla(vaca)

print('\n############\n')

print('# Y OTRO EJEMPLO MÁS, CON len()')

texto = "texto"
lista = ["bla", "ble"]
tupla = ("blo", "blu", "bla")
listas = [texto, lista, tupla]
for item in listas:
    print(len(item))
print('\n############\n')


print('# ABSTRACCIÓN')


class Validaciones:
    def devolver_cuit_con_dv(self, cuit_sin_dv):
        # validaciones minimas
        if len(cuit_sin_dv) != 10:
            return -1
        base = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
        # calculo el digito verificador:
        aux = 0
        for i in range(10):
            aux += int(cuit_sin_dv[i]) * base[i]
        aux = 11 - (aux - (int(aux / 11) * 11))
        if aux == 11:
            aux = 0
        if aux == 10:
            aux = 9
        return cuit_sin_dv + str(aux)


validacion = Validaciones()
cuit_sin_dv = '2045889876'
print(validacion.devolver_cuit_con_dv(cuit_sin_dv))


print('\n# MODULARIDAD')
print("""
Consiste en la descomposición de algo grande y complejo, en partes más sencillas y 
manejables. Mientras que la Abstracción se enfoca en reducir la complejidad lógica, la 
modularidad se preocupa por aspectos físicos o de implementación. Por ejemplo, las 
clases se agrupan en paquetes para poder administrarlas mejor.\n
""")

print('# COHESIÓN')


def cohesion_debil_suma():
    num1 = float(input("Elige un número"))
    num2 = float(input("Elige otro número"))
    resultado = num1 + num2
    return resultado


def cohesion_fuerte_suma(num1, num2):
    resultado = num1 + num2
    return resultado


def cohesion_aun_mas_fuerte_suma(lista_numeros):
    resultado = 0
    for nro in lista_numeros:
        resultado += nro
    return resultado


print("""
En el primer caso, no sólo se pide al usuario el ingreso de los números, sino que se 
realiza una conversión a float, es decir, 2 tareas no relacionadas fuertemente a la 
finalidad de la función, que es sumar. En el segundo, ya hay una cohesión fuerte, dado 
que la función se encarga de realizar la tarea para la cual fue creada, sumar, como 
dijimos, sin embargo, está limitada, sólo sirve para 2 números. En cambio, el tercer 
caso muestra una real fuerte cohesión, dado que permite sumar una cantidad 
indefinida de números, pudiendo reutilizar esta función para cualquier operación 
de suma.\n 
""")


print('# ACOPLAMIENTO')


class Clase1:
    x = True


class Clase2:
    def __init__(self, valor):
        if Clase1.x:
            self.valor = valor


mi_clase2 = Clase2('Hola')
print(mi_clase2.valor)

print("""\nSi bien en principio este código va a funcionar, si en algún momento el valor de la 
variable x de la Clase1 cambiara a False, dejará de hacerlo.
Este es un ejemplo muy trivial, pero a medida que el software se va complejizando, no 
es raro realizar este tipo de acciones sin darnos cuenta, por tal motivo, siempre hay que 
tener en cuenta el Acoplamiento, así como la Cohesión""")
