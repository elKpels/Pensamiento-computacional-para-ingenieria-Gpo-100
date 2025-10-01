#   Sergio Tadeo Herrera Rivas
#   A01765128

def contar_pares_impares(lista):
    contador_pares = 0
    contador_impares = 0
    for numero in lista:
        if numero % 2 == 0:
            contador_pares += 1
        else:
            contador_impares += 1
    return contador_pares, contador_impares

numeros = []
while True:
    numero = int(input("Dame un número (negativo para terminar): "))
    if numero < 0:
        break
    numeros.append(numero)

pares, impares = contar_pares_impares(numeros)
print("Cantidad de numeros pares:", pares)
print("Cantidad de numeros impares:", impares)