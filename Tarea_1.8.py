#Tarea 8

#Entrada de datos

#Variables
#Obtener un número y determinar lo siguiente:

número = float(input("Pon un número:"))

#a) si es negativo y mayor a -100 imprimir los números impares de forma DESCENDENTE

if número <0 and número> -100:
    for número in range(-1,-100,-1):#(inicio,final,incremento)
        print(número)
#b) si es positivo y menor a 100 mostrar los números pares de forma ASCENDENTE
    
elif número >0 and número < 100:
    for número in range(2,101,2):#(inicio,final,incremento)
        print(número)
#c) en otro caso imprimir No Válido

else:
         print("NV")








