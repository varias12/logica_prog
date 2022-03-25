#Cisterna

import math


# Entrada de datos

Metros=float(input("Poner nivel de agua en metros de cisterna:"))

#Proceso
 
if Metros < 0:
    print("Fuga en cisterna.")
elif Metros == 0:
    print("Encender bomba de agua.")
elif Metros > 0 and Metros<= 2:
    print("Acelerar bomba.")
elif Metros > 2 and Metros <= 4:
    print("Bomba trabajando.")
elif Metros > 4 and Metros < 6:
    print("Desacelerar bomba.")
elif Metros == 6:
    print("Apagar bomba.")
else:
    print("Desbordamiento de Agua en cisterna.")










#Salida de datos



