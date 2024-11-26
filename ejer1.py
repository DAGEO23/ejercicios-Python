salarioBasico = int(input(" Ingrese su salario basico: "))
retencion = salarioBasico * 0.18
bonificacion = salarioBasico * 0.013
salarioNeto = (salarioBasico - retencion) + bonificacion
print(f" Su salario neto corresponde a : {salarioNeto} ")