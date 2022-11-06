'''
Ejercicio 5 – Control empleados

Del reloj de marcación del personal de una empresa se obtienen los siguientes datos: 
número de día, ID del empleado y cantidad de horas extras que trabajó (número entero).

Estos datos se vuelcan a una planilla donde están ordenados por día. Se sabe que todos 
los días que la empresa abrió hubo algún trabajador que hizo horas extras, y que en un 
mismo día no hubo dos empleados con igual cantidad de horas extras.

Se requiere procesar esta información para obtener:
● Para cada día:
    ○ El ID del empleado que trabajó la mayor cantidad de horas extras.
    ○ El promedio de horas extras trabajadas (cantidad total de horas extras/cantidad 
    total de personas que trabajaron extras).
● Para todo el período en estudio:
    ○ La cantidad de días que se trabajó.
'''

salirdias=False
i=1
repetido=0
mayor=0

while salirdias==False:
    
    ids=[]
    extras=[]
    salirempleados= False
    cantidad=0
    horastotal=0
    banderaidhoras=0

    print("Día",i)
    while salirempleados==False:
        
        while banderaidhoras==0:
            id= int(input("Ingrese el ID del empleado: \n"))
            if id not in ids:
                while id<0:
                    id= int(input("Ingrese un número de id mayor que 0 \nIngrese el ID del empleado:\n"))
                ids.append(id)
                banderaidhoras=1
            else:
                print("Ya ingresó ese ID")
        banderaidhoras=0
        
        while banderaidhoras==0:
            horas=int(input("Ingrese las horas extras que trabajó el empleado\n"))
            if horas not in extras:
                while horas<0:
                    horas=int(input("Ingrese una cantidad de horas validad (mayor que 0)\nIngrese las horas extras que trabajó el empleado"))
                extras.append(horas)
                banderaidhoras=1
            else:
                print("Ya ingresó esas horas extras")
        banderaidhoras=0
        
        if horas>mayor:
            idmayor=id
            mayor=horas

        cantidad=cantidad+1
        horastotal=horastotal+horas

        respuesta= input("Desea ingresar otro empleado? \nSi / No \n")
        respuesta=respuesta.upper()

        while respuesta!="SI" and respuesta!="NO":
            respuesta=input("Ingrese una opción válida \nDesea ingresar otro empleado?\nSi / No\n")
            respuesta=respuesta.upper()
        
        if respuesta=="NO":
            salirempleados=True
        
        
        
    print("El empleado que más horas extras realizó fue el",idmayor,"con un total de",mayor,"horas extras")
    print("El promedio de horas extras trabajadas en el día",i,"fue de",horastotal/cantidad,"horas por empleado")
    
    respuesta=input("Desea ingresar otro día?\nSi / No\n")
    respuesta=respuesta.upper()

    while respuesta!="SI" and respuesta!="NO":
        respuesta=input("Ingrese una opción válida \nDesea ingresar otro día?\nSi / No\n")
        respuesta=respuesta.upper()

    if respuesta=="NO":
        salirdias=True
    else:
        i=i+1

print("La cantidad de días que se trabajó fue de",i,"días")