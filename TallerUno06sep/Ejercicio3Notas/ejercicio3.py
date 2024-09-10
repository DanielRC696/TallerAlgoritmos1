# Función para validar notas
def validar_nota(nota_num):
    while True:
        nota = float(input(f"Ingrese la {nota_num} nota (1 a 5): "))
        if nota < 1 or nota > 5:
            print(f"Error: La {nota_num} nota debe estar entre 1 y 5.")
        else:
            return nota

# Pedir las 4 notas usando la función de validación
nota1 = validar_nota("primera")
nota2 = validar_nota("segunda")
nota3 = validar_nota("tercera")
nota4 = validar_nota("cuarta")
#Calcular Promedio
promedio = (nota1 + nota2 + nota3 + nota4) / 4

print(f"El promedio del estudiante es: {promedio:.2f}")

if promedio >= 4:
    print("Excelente")
    descuento = 0.2
elif promedio >= 3:
    print("Bien")
    descuento = 0
else:
    print("Deficiente")
    descuento = 0


# Ingresar costo de la matricula
costo_matricula = float(input("Ingrese el costo de la matricula :"))

# Calcular el costo final con descuento aplicado
costo_final = costo_matricula * (1 - descuento)


print(f"El costo final de la matrícula es: {costo_final:.2f}")


