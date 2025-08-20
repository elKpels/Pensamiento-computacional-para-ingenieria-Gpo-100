#   Sergio Tadeo Herrera Rivas
#   A01765128

costo = 0.80
numero_mensajes = int(input('Ingrese el número de mensajes enviados: '))
numero_megas = float(input('Ingrese el número de megas utilizados: '))
numero_minutos = int(input('Ingrese el número de minutos de llamada: '))
costo_total = (numero_mensajes + numero_megas + numero_minutos) * costo
print('El costo total es:', costo_total)