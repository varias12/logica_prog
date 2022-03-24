#Tarea 1
#Ejercicio 9
#Factura Honorarios 


import math
import locale

locale.setlocale(locale.LC_MONETARY, "es_MX.UTF-8")

#Entrada de datos

#Variables

Mes = str(input("Poner mes:"))
Dias_Laborados = int(input("Poner días laborados:"))
Pago_por_día = float(input("Poner pago por día:"))

#Constante
Tasa_de_IVA_Trasladado = float(.16)
Tasa_de_IVA_Ret = float(2/3)*.16
Tasa_de_ISR_Ret = float(.10)

#Proceso

Pago_base = float(round(Dias_Laborados*Pago_por_día,2))
IVA_Trasladado=float(round(Pago_base*Tasa_de_IVA_Trasladado,2))
Subtotal=float(round(Pago_base+IVA_Trasladado,2))
IVA_Ret=float(round(Pago_base*Tasa_de_IVA_Ret,2))
ISR_Ret=float(round(Pago_base*Tasa_de_ISR_Ret,2))
Pago_Neto=float(round(Subtotal-IVA_Ret-ISR_Ret,2))

#Salida de datos

print("Mes:", Mes)
print("Dias laborados:", Dias_Laborados)
print(F"Pago por día: {locale.currency(Pago_por_día)}")
print(f"Pago Base: {locale.currency(Pago_base)}")
print(f"IVA Trasladado: {locale.currency(IVA_Trasladado)}")
print(f"Subtotal: {locale.currency(Subtotal)}")
print(f"IVA Retenido: {locale.currency(IVA_Ret)}")
print(f"ISR Retenido: {locale.currency(ISR_Ret)}") 
print(f"Pago Neto: {locale.currency(Pago_Neto)}")





