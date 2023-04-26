nro1 = input('Ingresá el nominador: ')
nro2 = input('Ingresá el denominador: ')
try:
    nro1 = float(nro1)
    nro2 = float(nro2)
    resultado = nro1/nro2
except ZeroDivisionError as err:  # as err es opcional
    print('El divisor no puede ser cero!', f'- {err} -')
except Exception as err:  # Exception as err es opcional
    print('Error en el ingreso de datos', f'- {err} -')
else:
    print(f'El resultado de {round(nro1, 2)}/{round(nro2, 2)} es {round(resultado, 2)}')
finally:
    print('Esto se imprime sin importar si lo ejecutado en el try surgió o no un problema')
