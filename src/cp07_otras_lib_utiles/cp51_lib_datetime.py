import datetime
mi_dia_hora = datetime.datetime(2023, 3, 20, 12, 30, 15, 1500)
print(mi_dia_hora)
print()

print(mi_dia_hora.year, mi_dia_hora.month, mi_dia_hora.day, mi_dia_hora.hour,
      mi_dia_hora.minute, mi_dia_hora.second, mi_dia_hora.microsecond)
print()

print(datetime.time(12, 30, 15, 1500))
print()

mi_hora = datetime.time(12, 30, 15, 1500)
print(mi_hora.hour, mi_hora.minute, mi_hora.second, mi_hora.microsecond)
print()

print(datetime.date(2023, 3, 20))
print()

mi_dia = datetime.date(2023, 3, 20)
print(mi_dia.year, mi_dia.month, mi_dia.day)
print()

print(mi_dia_hora.strftime('%d-%m-%Y'))
print()

mi_fecha = datetime.datetime.strptime('20230320 12:30:15', '%Y%m%d %H:%M:%S')
print(mi_fecha)
print(type(mi_fecha))
print()

print(mi_fecha.replace(year=2020))
print()

nueva_fecha = mi_fecha + datetime.timedelta(days=5)
print(nueva_fecha)
print()

mi_fecha = datetime.datetime.strptime('20230320', '%Y%m%d')
mi_otra_fecha = datetime.datetime.strptime('20230325', '%Y%m%d')
diferencia = mi_otra_fecha - mi_fecha
print(diferencia.days)
