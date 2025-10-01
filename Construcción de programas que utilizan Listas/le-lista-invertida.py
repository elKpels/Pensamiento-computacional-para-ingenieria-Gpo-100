#   Sergio Tadeo Herrera Rivas
#   A01765128

listona = []
listainvertida = []
cantidadNumeros = int(input("¿Cuántos números deseas ingresar? "))

for i in range(cantidadNumeros):
    numero = int(input("Dame un número: "))
    listona.append(numero)

listainvertida = listona[::-1]

print("La lista invertida es:")
for num in listainvertida:
    print(num)