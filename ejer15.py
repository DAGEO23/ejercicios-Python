numeroInicial = int(input("Ingrese el numero inicial de la registradora: "))
numeroFinal = int(input("Ingrese el numero final de la registradora: "))
valorPasaje = float(input("ingrese el valor del pasaje"))
totalPasajeros = numeroInicial + numeroFinal
empresa = valorPasaje * 0.75
conductor = valorPasaje - empresa
print(f"El total de pasajeros es: {totalPasajeros} pasajeros")
print(f"El total liquidado para la empresa es: {empresa}")
print(f"El total liquidado para el conductor es: {conductor}")

