#   Sergio Tadeo Herrera Rivas
#   A01765128

costo_nuevo = 1000
costo_usado = 350
juegos_nuevos = int(input('Ingrese el número de juegos nuevos comprados: '))
juegos_usados = int(input('Ingrese el número de juegos usados comprados: '))
costo_total = (juegos_nuevos * costo_nuevo) + (juegos_usados * costo_usado)
print('El costo total es:', costo_total)