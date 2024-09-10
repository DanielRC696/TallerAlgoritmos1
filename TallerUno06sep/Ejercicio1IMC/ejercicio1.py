# Ingrese el peso en kilogramos
peso = float(input("Por favor ingrese el peso en Kilogramos: "))

# Ingrese la altura en metros
altura = float(input("Por favor ingrese su altura en metros: "))

# calcula el indice de masa corporal
imc = peso / (altura ** 2)

print(f" Su indice de masa corporal es: {imc:.2f}")
