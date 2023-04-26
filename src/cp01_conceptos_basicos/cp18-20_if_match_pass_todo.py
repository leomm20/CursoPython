# if
clima = input('Ingresá cómo está el clima hoy (llueve, nublado, soleado): ').lower()
if clima == 'soleado':
    print('\nLlevá protector solar')
elif clima == 'llueve':  # elif se puede poner las veces que uno quiera
    print('\nDefinitivamente llevá un paraguas')
else:  # opcional
    print('\nPor las dudas, llevá un paraguas')
print()

# match_case
lista = list(range(1, 11))
for e in lista:
    match e:
        case 5:
            print(e, '-', 'cinco')
        case 8:
            print(e, '-', 'ocho')
        case 3:
            print(e, '-', 'tres')
        case _:  # también se puede escribir case other
            print(e, '-', 'ni 5, ni 8 ni 3')
print()

# pass / TODO
a = True
if a:
    # TODO completar con código para hacer 'x' cosa
    pass

a = True
if not a:
    # TODO completar con código para hacer 'x' cosa
    pass
