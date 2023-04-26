total = float(input('Ingresá el valor total de lo consumido: '))
cantidad_personas = int(input('Gasto a repartir entre cuántas personas?: '))
total_con_propina = total * 1.10  # Considerando un 10% de propina
total_a_pagar_por_cada_uno = round(total_con_propina / cantidad_personas, 2)
print(f'\nLa suma a abonar por cada persona es de ${total_a_pagar_por_cada_uno}')
print()

# DAR FORMATO A UN NÚMERO
total_a_pagar_por_cada_uno = '{:.2f}'.format(round(total_con_propina / cantidad_personas, 2))
total_a_pagar_por_cada_uno = '%.2f' % (round(total_con_propina / cantidad_personas, 2))
