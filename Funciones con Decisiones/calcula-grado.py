# Sergio Tadeo Herrera Rivas
# A01765128

def calcular_grado(calificacion):
    if calificacion <= 1.0 and calificacion >= 0.0:
        if calificacion >= 0.9:
            return "A"
        elif calificacion >= 0.8:
            return "B"
        elif calificacion >= 0.7:
            return "C"
        elif calificacion >= 0.6:
            return "D"
        else:
            return "F"
    else:
        return "Calificación no válida"

calificacion = float(input("Introduce la calificación del estudiante: "))
nota = calcular_grado(calificacion)
print(f"El grado del estudiante es: {nota}")
