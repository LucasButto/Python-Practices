'''
Ejercicio 4 – Planta autopartes
Una planta que produce autopartes posee varias máquinas destinadas a la producción de determinadas piezas. 
Se dispone de una planilla que, durante la última semana, se ha completado manualmente. En la misma se anota:

● Número de identificación de la máquina (número entero).
● Tiempo de funcionamiento semanal (en horas, minutos y segundos).
● Cantidad de piezas producidas (número entero).
Se desconoce la cantidad de máquinas que se encuentran trabajando actualmente.

Se requiere procesar esta información tal que se determine:
● El rendimiento de cada máquina (cantidad de piezas/tiempo en segundos).
● La cantidad total de piezas producidas en la planta esa semana.
'''

salir=False
maquinas=[]
tiempo=[]
rendimientos=[]
cantidad=0
total=0

while salir==False:
    
    maquina= int(input("Ingrese el número de máquina: \n"))
    while maquina<1:
        maquina= int(input("Ingrese un numero mayor que 0 \nIngrese el número de máquina: \n"))
    maquinas.append(maquina)

    horas= int(input("Ingrese el tiempo de funcionamiento de la maquina en horas, minutos y segundos: \n"))
    minutos=int(input())
    segundos=int(input())

    minutos=minutos+horas*60
    segundos=segundos+minutos*60

    producidas=int(input("Ingrese la cantidad de piezas producidas por la maquina \n"))
    
    total=total+producidas

    rendimientos.append(producidas/segundos)

    respuesta= input("Desea ingresar otra máquina? \nSi / No \n")
    respuesta=respuesta.upper()

    if respuesta=="NO":
        salir=True
    
    cantidad=cantidad+1


for i in range(cantidad):
    print("maquina:",maquinas[i], "rendimiento: ", rendimientos[i], "piezas por segundo")

print("Cantidad de piezas fabricadas en total en la semana: ",total)
    