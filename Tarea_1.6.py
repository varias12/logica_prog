#Tarea 1
#Ejercicio 6
#Chicharronera

import math

#Entrada de datos

a = int(input("Valor de a"))
b = int(input("Valor de b"))
c = int(input("Valor de c"))


#Proceso

X1 = (-b-math.sqrt(pow(b,2)-4*a*c))/(2*a)
X2 = (-b+math.sqrt(pow(b,2)-4*a*c))/(2*a)

#Salida de datos

print("X1 es igual a:",X1)
print("X1 es igual a:",X2)





