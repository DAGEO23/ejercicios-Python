#En clase de programación, se sacan 4 notas del 15%,30%,30%,25% respectivamente. Se
#pide diseñar un algoritmo que permita mostrar la nota definitiva de un estudiante.
#Teniendo en cuenta que la primera nota consta del promedio de dos talleres, la segunda
#de tres evaluaciones, la tercera nota de un trabajo final y la última es el promedio de 4
#quizzes. 
taller1=int(input("Ingrese la nota del primer taller: "))
taller2=int(input("Ingrese la nota del segundo taller: "))
ta1=taller1*0.15
ta2=taller2*0.15
talleres= (ta1+ta2)/2
evaluacion1=int(input("Ingrese la nota de la primer evaluacion: "))
evaluacion2=int(input("Ingrese la nota de la segunda  evaluacion: "))
evaluacion3=int(input("Ingrese la nota de la tercer  evaluacion: "))
eva1=evaluacion1 * 0.30
eva2=evaluacion2 * 0.30
eva3=evaluacion3 * 0.30
evaluaciones=(eva1+eva2+eva3) 
trabajo=int(input("Ingrese la nota del trabajo final "))
tra1=trabajo * 0.30
trabajoFinal= tra1
quizz1=int(input("Ingrese la nota del primer quizz: "))
quizz2=int(input("Ingrese la nota de la segunda  quizz: "))
quizz3=int(input("Ingrese la nota de la tercer  quizz: "))
quizz4=int(input("Ingrese la nota de la cuarto  quizz: "))
qui1=quizz1 * 0.25
qui2=quizz2 * 0.25
qui3=quizz3 * 0.25
qui4=quizz4 * 0.25
quizzes= (qui1 + qui2+ qui3 + qui4) /4
notaDefinitiva=(talleres + evaluaciones + trabajoFinal + quizzes)/4
print(f"su nota definitiva es de: {notaDefinitiva}")