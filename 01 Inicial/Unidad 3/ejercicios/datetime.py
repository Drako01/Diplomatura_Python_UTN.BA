###############################################################
#### USO datetime
#### https://docs.python.org/3.8/library/datetime.html
#### (proporciona clases y objetos)
###############################################################
# from datetime import datetime, date, time, timedelta
import datetime
import calendar

datetime.datetime.now()
print(datetime.datetime.utcnow())
print(datetime.datetime.now())
print(datetime.datetime.now().day)
print(datetime.datetime.now().month)
print(datetime.datetime.now().minute)
print(datetime.datetime.now().second)
print(datetime.datetime.now().microsecond)
print(datetime.MINYEAR)
print(datetime.MAXYEAR)
print("-------------------------------------------")
# USO TODO LO QUE PUEDO USAR CON time
print(datetime.datetime.now().strftime("%m"))
print(datetime.datetime.today().strftime("%H:%M:%S--%d/%m/%y"))
""""
%a - Nombre del día de la semana
%A - Nombre del día completo
%b - Nombre abreviado del mes
%B - Nombre completo del mes
%c - Fecha y hora actual
%d - Día del mes
%H - Hora (formato 24 horas)
%I - Hora (formato 12 horas)
%j - Día del año
%m - Mes en número
%M- Minutos
%p - Equivalente de AM o PM
%S - Segundos
%U - Semana del año (domingo como primer día de la semana)
%w - Día de la semana
%W - Semana del año (lunes como primer día de la semana)
%x - Fecha actual
%X - Hora actual
%y - Número de año (14)
%Y - Numero de año entero (2014)
%Z - Zona horaria
"""
actual = datetime.datetime.now()
anterior = datetime.datetime(1975, 9, 15, 0, 0, 0)
print(actual - anterior)


print("-------------------------------------------")
# Obtener calendario
año = datetime.datetime.today().year
mes = datetime.datetime.today().month
calendario_mes = calendar.month(año, mes)
print(calendario_mes)

print("-------------------------------------------")
# Obtener calendario
año = datetime.datetime.today().year
mes = datetime.datetime.today().month
calendario = calendar.month(año, mes)
print(calendario)

print("-------------------------------------------")
# Diferencia de fechas
hoy = datetime.date.today()
hace5 = datetime.timedelta(days=5)
# mañana = hoy + datetime.timedelta(days=1)
# diferencia_en_dias = mañana – hoy
print(hoy)
print(hace5)
print(hoy - hace5)  # Resto 5 días
