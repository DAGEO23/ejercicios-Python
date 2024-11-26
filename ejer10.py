distancia1 = int(input("Ingresa la distancia del día 1 (en metros): "))
distancia2 = int(input("Ingresa la distancia del día 2 (en metros): "))
distancia3 = int(input("Ingresa la distancia del día 3 (en metros): "))
tiempo1 = int(input("Ingresa el tiempo del día 1 (en minutos): "))
tiempo2 = int(input("Ingresa el tiempo del día 2 (en minutos): "))
tiempo3 = int(input("Ingresa el tiempo del día 3 (en minutos): "))
tiempoEntrenamiento = tiempo1 + tiempo2 + tiempo3
distanciaEntrenamiento = distancia1 + distancia2 + distancia3
promedioDistancia = distanciaEntrenamiento//3
promedioTiempo = tiempoEntrenamiento//3
print(f"El promedio de tiempo en los tres dias de entremamiento es de: {promedioTiempo} minutos")
print(f"El promedio de distancia recorrida es de: {promedioDistancia} metros")
print(f"La distancia total recorrida  en los 3 dias de entrenamientos es de : {distanciaEntrenamiento}  metros  con un tiempo total de: {tiempoEntrenamiento} minutos ")
