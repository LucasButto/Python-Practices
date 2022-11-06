'''
Ejercicio 17 - Empresa de traslado.

Una empresa de traslado quiere obtener una estadística del rendimiento de cada uno de sus autos. Diariamente guarda 
para cada uno de sus 7 autos de lujo la cantidad de viajes realizados en el día y el total de km diarios.

Se necesita analizar el rendimiento de los autos durante el mes de noviembre del corriente año. Para ello se solicita:
    ● Generar el número de auto (número entero de 1 a 7) y el número de día (número entero de 1 a 30). No son datos 
    que se ingresan por teclado.
    ● Ingresar el total de viajes realizados en el día y el total de kilómetros diarios para cada uno de los autos 
    durante cada uno de los 30 días del mes de noviembre.

Calcular y mostrar:
    ● Por auto:
        ○ El total de viajes realizados.
        ○ El total de km. realizados.
        
    ● Para todos los autos:
        ○ El auto con menos cantidad de viajes realizados en el mes y cuál es ese valor. Se sabe que hay un solo auto.
'''
import random

### COMIENZO DEL CÓDIGO ###

mayorviajes=-1

for i in range(7):
    print("\n### MES NOVIEMBRE VEHÍCULO",i+1,"###\n")

    totalviajes=0
    totalkilometros=0

    for j in range(30):
        print("Día",j+1)

        viaje=random.randrange(15) #int(input("Ingrese la cantidad de viajes que realizó el vehículo\n"))
        while viaje<0:
            viaje=int(input("Ingrese una cantidad mayor o igual a 0\nIngrese la cantidad de viajes que realizó el vehículo\n"))

        totalviajes=totalviajes+viaje

        if viaje==0:
            kilometros=0
        else:
            kilometros=random.randrange(1,150) #int(input("Ingrese la cantidad de kilómetros que realizó\n"))
            while kilometros<1:
                kilometros=int(input("Ingrese una cantidad mayor que 0\nIngrese la cantidad de kilómetros que realizó\n"))

        totalkilometros=totalkilometros+kilometros
    
    print("\n### RESULTADOS VEHÍCULO ###\n\nLa cantidad de viajes realizados fue de",totalviajes,"viajes con un total de",totalkilometros,"Km")

    if totalviajes>mayorviajes:
        mayorviajes=totalviajes
        automayor=i+1

print("\n### RESULTADOS FINALES ###\n\nEl vehículo que más viajes realizó fue el vehículo",automayor,"con un total de",mayorviajes,"viajes\n")
