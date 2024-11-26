#Un cliente de telefonía celular realiza cuatro llamadas: dos a un primer operador, y dos al
#segundo operador. El cliente desea conocer el costo de cada llamada, El costo total de las
#llamadas a cada operador, y el total de las cuatro llamadas.

costoLlamada = 200
operador_1 = 5
operador_2 = 10
costo_operador_1 = operador_1 * costoLlamada
costo_operador_2= operador_2 * costoLlamada
costoTotal= costo_operador_1 + costo_operador_2
print(f"el costo de cada llamada es de:  {costoLlamada}  pesos   el costo del operador 1 es de:  {costo_operador_1} pesos el costo del operador 2 es de: {costo_operador_2} pesos  y el total de las 4 llamadas es de: {costoTotal} pesos")