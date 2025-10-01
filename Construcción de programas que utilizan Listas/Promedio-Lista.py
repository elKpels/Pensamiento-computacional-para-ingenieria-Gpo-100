#   Sergio Tadeo Herrera Rivas
#   A01765128

listona = []

cantidadNumeros = int(input("¿Cuántos números deseas ingresar? "))

for i in range(cantidadNumeros):
    numero = int(input("Dame un número: "))
    listona.append(numero)

print("Los números ingresados son:", listona)

if listona:
    promedio = sum(listona) / len(listona)
    print("El promedio de los números ingresados es:", promedio)
else:
    print("No se ingresaron números para calcular el promedio.")