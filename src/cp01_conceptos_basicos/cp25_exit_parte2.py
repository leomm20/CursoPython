

# Para probar, ingresá 3 números enteros, y luego volvé a ejecutar pero esta vez, ingresá letras en lugar de números


lista = []
nro = 0  # esta asignación es sólo para que el IDE no de un Warning
contador = 3
while contador != 0:
    nro = input('Ingresá un número: ')
    if nro.isnumeric():
        nro = int(nro)
        print('OK!')
        break
    else:
        contador -= 1
    if contador != 0:
        print(f'El valor ingresado no es un número. Te quedan'
              f' {contador} intentos')
    else:
        print('Te quedaste sin intentos. Chau!')
        exit()
nro_por_pi = nro * 3.14
# etc
