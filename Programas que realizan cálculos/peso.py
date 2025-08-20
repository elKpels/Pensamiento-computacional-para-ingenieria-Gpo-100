#   Sergio Tadeo Herrera Rivas
#   A01765128

pesoinicial = float(input('Ingrese su peso en kg: '))
pesofinal = float(input('Ingrese su peso final en kg: '))
meses = int(input('Ingrese el número de meses transcurridos: '))
pérdida_peso = pesoinicial - pesofinal
promedio_mensual = pérdida_peso / meses
print('La pérdida de peso promedio por mes es:', promedio_mensual, 'kg')