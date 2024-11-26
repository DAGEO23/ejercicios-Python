desempleo = int(input("ingre el desempleo en ibague: "))
primerTrimestre = desempleo * 0.095
segundoTrimestre = desempleo * 0.015
desempleoFinal = (desempleo - segundoTrimestre) + primerTrimestre
print(f"El desempleo actual en ibague es: {desempleoFinal}")
