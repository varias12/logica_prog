#Tarea 1
#Ejercicio 1

import math

#Entrada de datos

Calificación_1 = float(input("1ra Calificación:")) 
Calificación_2 = float(input("2da Calificación:"))
Calificación_3 = float(input("3ra Calificación:"))

#Proceso

Promedio = float(round((Calificación_1 + Calificación_2 + Calificación_3)/3,2))
if (Promedio>=6):
    print("Aprobado")
elif(Promedio<6):
    print("Reprobado")



#Salida de datos

print("El promedio es:",Promedio)






