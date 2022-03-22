#Tarea 1
#Ejercicio 2


import math

#Entrada de datos

captura = (input("Escriba los grados (ejemplo 5°F, 3°C ó 10°K):"))

escala = captura[-2:]



#Proceso

if escala == "°C":
    valor = int(captura[:-2])
    fahrenheit = valor * 9/5 + 32
    kelvin = valor + 273.15

    print("{} es equivalente a {}°F".format(captura,fahrenheit))
    print("{} es equivalente a {}°K".format(captura,kelvin))

elif escala == "°F":
    valor = int(captura[:-2])
    celcius = 5/9 * (valor - 32)
    kelvin = celcius + 273.15

    print("{} es equivalente a {}°C".format(captura,celcius))
    print("{} es equivalente a {}°K".format(captura,kelvin))

elif escala == "°K":
    valor = int(captura[:-2])
    celcius = valor - 273.15
    fahrenheit = celcius * 9/5 + 32

    print("{} es equivalente a {}°F".format(captura,fahrenheit))
    print("{} es equivalente a {}°C".format(captura,celcius))

    


else:
    print("No a escrito un valor de temperatura valido.")




    




