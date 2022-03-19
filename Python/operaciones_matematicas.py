# OPERACIONES MATEMATICAS
# USANDO OPERADORESMATEMATICOS Y FUNCIONES MATEMATICAS


import math

# Entrada de datos



número1 = float(input("escribe un número: "))#convertir a entero o decimal
número2 = float(input("escribe otro número: "))


#Proceso (Calculo u operaciones matematicas y/o lógicas)
suma = número1 + número2
resta = número1 - número2
multiplicacion = número1 * número2
division = número1 / número2
potencia1 = número1 ** número2
potencia2 = pow(número1,número2)
cuadrado = número1 ** 2
cubo = pow(número2,3)

raiz_cuadrada1 = pow(número1,1/2)
raiz_cuadrada2 = math.sqrt(número2)
raiz_cubica = pow(9,1/3)

modulo_residuo = número1 % número2






#Salida de datos
print("La suma =",suma)
print("La suma =" + str(suma))#concatenacion (union de textos)
#Convertir un tipo dedato en otro dato
print(f"La suma = {suma} " )


#Salida de datos
print("La resta =",resta)
print("La resta =" + str(resta))#concatenacion (union de textos)
#Convertir un tipo dedato en otro dato
print(f"La resta = {resta} " )

#Salida de datos
print("La multiplicacion =",multiplicacion)
print("La multiplicacion =" + str(multiplicacion))#concatenacion (union de textos)
#Convertir un tipo dedato en otro dato
print(f"La multiplicacion = {multiplicacion} " )

#Salida de datos
print("La division =",division)
print("La division =" + str(division))#concatenacion (union de textos)
#Convertir un tipo dedato en otro dato
print(f"La division = {division} " )
print(f"El modulo de número1 entre número2 = {modulo_residuo}")
