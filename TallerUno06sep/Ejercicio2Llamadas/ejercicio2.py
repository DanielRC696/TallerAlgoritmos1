# Ingresa el destino de la llamada
destino = input("ingrese el destino de la llamada (EEUU, Canada, Europa, RestoDelMundo):")

#Ingresa la duracion de la llamada en minutos
duracion = float(input("ingrese la duracion de la llamada en minutos: "))

# listas de destinos y tarifas
lista_destinos = ["EEUU","Canada","Europa","RestoDelMundo"]
lista_tarifas = [900,800,950,1250]

# Busca el destino en la lista y obtiene la tarifa correspondiente
if destino in lista_destinos:
    # encuentra el indice del destino
    indice = lista_destinos.index(destino)

    # obtiene la tarifa segun el indice
    tarifa = lista_tarifas[indice]

 #calcula el costo total de la llamada
    costo_total = tarifa * duracion

# Verificar si se aplica el descuento
    if duracion > 15:
       descuento = costo_total * 0.20
       costo_total -= descuento  # Restamos el descuento del costo total

# Mostrar el costo final
    print(f"El costo total de la llamada es: {costo_total:.2f} pesos")
else:
    print("Destino no válido.")