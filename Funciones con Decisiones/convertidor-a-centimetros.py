# Sergio Tadeo Herrera Rivas
# A01765128

def convertir_desde_pulgadas(pulgadas):
    return pulgadas * 2.54

def convertir_desde_pies(pies):
    return pies * 30.48

def convertir_desde_yardas(yardas):
    return yardas * 91.44

def preguntar():
    opcion = str(input("¿Desde qué unidad deseas convertir a centímetros?\n1 - pulgadas\n2 - pies\n3 - yardas\nTu opción: "))
    return opcion

opcion = preguntar()

if opcion == "1":
    pies = float(input("Introduce la medida en pies: "))
    print(f"{pies} pies son {convertir_desde_pies(pies)} centímetros.")


elif opcion == "2":
    pulgadas = float(input("Introduce la medida en pulgadas: "))
    print(f"{pulgadas} pulgadas son {convertir_desde_pulgadas(pulgadas)} centímetros.")

elif opcion == "3":
    yardas = float(input("Introduce la medida en yardas: "))
    print(f"{yardas} yardas son {convertir_desde_yardas(yardas)} centímetros.")
    
else:
    print("\nOpción no válida. Intentemos de nuevo.\n")
    preguntar()