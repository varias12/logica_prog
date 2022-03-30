# Funciones: Tareas o acciones a ejecutar
# Sintaxis:
#def Nombre_de_la_Función(Argumentos o Parametros)
#Nombrar como verbos (ar, er,etc.)


#PARADIGMA O ENFOQUE FUNCIONAL


def Sumar(a, b):# Obtiene ó recibe 2 parametros
    suma = a+b
    return suma #devuelbe o retorna

def Restar(a, b):# Obtiene ó recibe 2 parametros
    restar = a-b
    return restar #devuelbe o retorna

def Multiplcar(a, b):# Obtiene ó recibe 2 parametros
    multiplicar = a*b
    return multiplicar #devuelbe o retorna

def Dividir(a, b):# Obtiene ó recibe 2 parametros
    dividir = a/b
    return dividir #devuelbe o retorna
    



# Mandar a llamar o invocar una Función y el resultado se asigna a una variable
s = suma = Sumar(2, 3)# Se envían o pasa 2 parametros
m = multiplica = Multiplcar(20, 10)
dividir = Dividir(45, 5)
r = Restar (20, 15)


#Salida
print(f"La suma = {s}")
print(f"La suma = {Sumar(20,10)}")
print(f"La resta = {r}")
print(f"La multiplicación = {multiplica}")
print(f"La divición = {dividir}")


