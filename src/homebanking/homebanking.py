import os


class Persona:
    def __init__(self, apellido, nombre):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    saldo = 0.00

    def __init__(self, apellido, nombre):
        super().__init__(apellido, nombre)
        self.numero_cuenta = abs(hash(apellido + nombre))

    def __str__(self):
        return f"Apellido: {self.apellido}, Nombre: {self.nombre}, Cuenta: {self.numero_cuenta}, Saldo: {self.saldo}"

    def depositar(self, importe):
        self.saldo += importe

    def retirar(self, importe):
        if self.saldo >= importe:
            self.saldo -= importe
            return True
        else:
            return False


def clear():
    os.system('cls')
    print('\n'*1000)


def crear_cliente(apellido, nombre):
    if apellido != "" and nombre != "":
        cliente = Cliente(apellido, nombre)
        return cliente
    else:
        return False


def seleccionar_cliente(clientes):
    if len(clientes) == 0:
        clear()
        return False
    print("Seleccione cliente:")
    cont = 1
    for c in clientes:
        print(f"[{cont}] - {c.apellido}, {c.nombre}")
        cont += 1
    sel = input("Ingrese opción: ")
    while not sel.isnumeric() or int(sel) not in range(1, cont):
        sel = input("Error! Ingrese opción: ")
    return clientes[int(sel) - 1]


def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


# INICIO
seleccion = 0
clientes = []
cliente = ''

clear()
while True:
    print("Elija la opción deseada:")
    print("[1] - Crear cliente")
    print("[2] - Seleccionar cliente")
    print("[3] - Consultar Saldo")
    print("[4] - Depositar")
    print("[5] - Retirar")
    print("[6] - Salir")
    seleccion = input("Su opción: ")
    match seleccion:
        case '1':
            clear()
            apellido = input("Ingrese apellido del cliente: ")
            nombre = input("Ingrese nombre del cliente: ")
            while apellido == "" or nombre == "":
                print("Por favor, completar!")
                apellido = input("Ingrese apellido del cliente: ")
                nombre = input("Ingrese nombre del cliente: ")
            cliente = crear_cliente(apellido, nombre)
            if not cliente:
                print("Error al generar el cliente!")
            else:
                clientes.append(crear_cliente(apellido, nombre))
                clear()
                print(f'Cliente "{cliente}" ha sido generado\n')
        case '2':
            cliente = seleccionar_cliente(clientes)
            clear()
            if cliente:
                clear()
                print(f"Cliente {cliente.apellido}, {cliente.nombre} seleccionado\n")
            else:
                print("No exiten clientes!\n")
        case '3':
            clear()
            if cliente:
                print(f"Cliente {cliente.apellido}, {cliente.nombre} tiene un saldo de ${cliente.saldo}\n")
            else:
                print("Primero tiene que seleccionar un cliente\n")
        case '4':
            clear()
            if cliente:
                importe = input(f"Ingrese importe a depositar para cliente {cliente.apellido}, {cliente.nombre} "
                                f"(0 para salir): ")
                while not is_number(importe) or float(importe) < 0:
                    importe = input("Error! Ingrese importe mayor o igual a $0: ")
                importe = round(float(importe), 2)
                if importe == 0:
                    clear()
                    continue
                cliente.depositar(float(importe))
                clear()
                print(f"Se han depositado ${importe} en la cuenta del cliente {cliente.apellido}, {cliente.nombre}\n")
            else:
                print("Primero tiene que seleccionar un cliente\n")
        case '5':
            clear()
            if cliente:
                importe = input(f"Ingrese importe a retirar para cliente {cliente.apellido}, {cliente.nombre} "
                                f"(0 para salir): ")
                while not is_number(importe) or float(importe) < 0:
                    importe = input("Error! Ingrese importe mayor o igual a $0: ")
                importe = round(float(importe), 2)
                if importe == 0:
                    clear()
                    continue
                clear()
                if cliente.retirar(float(importe)):
                    print(f"Se han retirado ${importe} de la cuenta del cliente {cliente.apellido}, {cliente.nombre}\n")
                else:
                    print(f"No hay fondos suficientes para el importe ingresado\n")
            else:
                print("Primero tiene que seleccionar un cliente\n")
        case '6':
            clear()
            print("Gracias por utilizar este HomeBanking!")
            break
        case _:
            clear()
            print('Opción inválida\n')

