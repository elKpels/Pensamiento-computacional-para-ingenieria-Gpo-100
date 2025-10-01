#   Sergio Tadeo Herrera Rivas
#   A01765128

listona = []

cantidadNumeros = int(input("¿Cuántos números deseas ingresar? "))

for i in range(cantidadNumeros):
    numero = int(input("Dame un número: "))
    listona.append(numero)

def elevar_cuadrado(lista):
    return [x**2 for x in lista]

print("Lista original:", listona)
print("Lista al cuadrado:", elevar_cuadrado(listona))