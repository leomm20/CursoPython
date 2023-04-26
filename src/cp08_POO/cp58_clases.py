class Automovil:
    pass


mi_auto = Automovil()
del mi_auto


class Perro:
    raza = 'Bulldog'

    def __init__(self, nombre):
        self.name = nombre

    def correr(self, metros):
        print(f'El perro corrió {metros} metros')

    def __str__(self):
        return f'Este perro se llama {self.name}'

    def __del__(self):
        print(f'Eliminaste a perro {self.name}!')


perro = Perro('Felipe')
perro.correr(10)
print(perro.name)
print(perro.raza)
print(perro)
del perro
print('\n############\n')


class Pajaro:
    # ATRIBUTOS DE CLASE
    alas = True

    # CONSTRUCTOR
    # ATRIBUTOS DE INSTANCIA
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    # MÉTODO DE INSTANCIA (self)
    def volar(self, metros):
        print(f"el pájaro voló {metros} metros")

    # MÉTODO DE CLASE (cls)
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"puso {cantidad} huevos")

    @staticmethod
    def mirar():
        print("el pájaro mira")


# SIN INSTANCIAR
print(Pajaro.alas)
Pajaro.alas = False
print(Pajaro.alas)
Pajaro.poner_huevos(4)
# Pajaro.volar(10) # El mismo IDE dará un error, y de continuar, el intérprete informará que falta 1 argumento
# Pajaro.color # También el IDE nos dará un error, y de continuar, informará que no tiene el atributo color
# INSTANCIANDO, CREANDO EL OBJETO
mi_pajaro = Pajaro('negro', 'canario')
print(mi_pajaro.alas)
mi_pajaro.poner_huevos(5)
