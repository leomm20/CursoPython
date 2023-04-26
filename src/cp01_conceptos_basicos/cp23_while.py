nro = 1
while nro != 4:
    print(f'ejecutado {nro}')
    nro += 1  # ATENCIÓN: si esta última línea no se agrega, loopeará indefinidamente
print()

frio = False
while not frio:
    if input('hace frío? (s/n): ') == 's':
        frio = True # ATENCIÓN: ésta es la línea de salida del while
        print('Apagá el ventilador!')
    else:
        print('Encendé el ventilador')

