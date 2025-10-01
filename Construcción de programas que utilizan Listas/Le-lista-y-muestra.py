#   Sergio Tadeo Herrera Rivas
#   A01765128

listona = []

cantidadNumeros = int(input("¿Cuántos números deseas ingresar? "))

for i in range(cantidadNumeros):
    numero = int(input("Dame un número: "))
    listona.append(numero)

print("Los números ingresados son:")
for num in listona:
    print(num)