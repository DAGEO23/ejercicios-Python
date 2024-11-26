altoMuro = int(input("Ingrese el alto del muro: "))
anchoMuro = int(input("Ingrese el ancho del muro: "))
area = altoMuro * anchoMuro
baldosasNecesarias = area // 3.5
print(f"El area total del baño es de: {area} metros")
print(f"El numero de baldosas para cubrir el baño es: {baldosasNecesarias} baldosas")