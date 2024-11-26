herencia = int(input("ingrese el valor de la herencia: "))
esposa = herencia  * 0.40
restante = herencia - esposa
hijo1 = restante * 0.30
hijo2 = restante * 0.20
hijo3 = restante * 0.40
hijo4 = restante * 0.10
print(f"la herencia asignada para el primer hijo es: {hijo1}")
print(f"la herencia asignada para el segundo hijo es:{hijo2} ")
print(f"la herencia asignada para el tercer hijo es:{hijo3} ")
print(f"la herencia asignada para el cuarto hijo es:{hijo4} ")
print(f"la herencia asignada para la esposa es:{esposa} ")