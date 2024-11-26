#El terreno comprado por un influencers tuvo la siguiente destinación: 40% para cultivos,
#25% Para construir vivienda, 15% para zonas verdes. Leer el área total del terreno en
#metros cuadrados e imprimir el área para cada destino, y el área que queda disponible
#para otros proyectos.
terreno=int(input("ingrese el area total del terreno comprado: "))
cultivos=terreno*0.4
viviendas=terreno*0.25
zonasVerdes=terreno*0.15
terrenoAsignado=cultivos + viviendas + zonasVerdes
areaDisponible=terreno - terrenoAsignado
print(f"El area asiganada para los cultivos es de: {cultivos} metros")
print(f"El area asignada para las viviendas es de : {viviendas} metros")
print(f"El area asignada para las zonas verdes es de : {zonasVerdes} metros")
print(f"El area disponible para otros proyectos es de: {areaDisponible}metros")
