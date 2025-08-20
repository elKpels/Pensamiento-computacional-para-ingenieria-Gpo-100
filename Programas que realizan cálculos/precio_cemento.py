#   Sergio Tadeo Herrera Rivas
#   A01765128

cantidad_bultos = int(input('Ingrese la cantidad de bultos de cemento: '))
precio_bulto = int(input('Ingrese el precio por bulto de cemento: '))
impuesto = 0.16
subtotal = cantidad_bultos * precio_bulto
costo_total = subtotal + (subtotal * impuesto)
print('El subtotal es:', subtotal)
print('El impuesto es:', subtotal * impuesto)
print('El costo total es:', costo_total)