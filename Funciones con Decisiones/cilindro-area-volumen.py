# Sergio Tadeo Herrera Rivas
# A01765128

def area_cilindro(radio, altura):
    return 2 * 3.1416 * radio * (radio + altura)

def volumen_cilindro(radio, altura):
    return 3.1416 * radio**2 * altura


radio = float(input("Introduce el radio del cilindro: "))
altura = float(input("Introduce la altura del cilindro: "))

print(f"\nEl área del cilindro es: {area_cilindro(radio, altura):.2f}")
print(f"El volumen del cilindro es: {volumen_cilindro(radio, altura):.2f}")