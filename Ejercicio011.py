'''
Problema 11 – Empresa empleados

Una empresa está dividida en 15 secciones. De cada sección se tiene: número que la identifica, 
cantidad de empleados que trabajan en ella. Durante un determinado período se registró en cada 
sección de la empresa los siguientes datos de cada uno de sus empleados: Número de identificación 
del empleado, turno en el que trabajó (M: Mañana; T: Tarde) y cantidad de horas que trabajó.

Se desea procesar esta información para poder saber:
    ● El promedio de horas que se trabajó en cada sección.
    ● Para toda la empresa, si hubo o no un turno en el que se trabajó más cantidad de horas, 
    y en caso afirmativo en cuánto se superó al otro.
'''
### DEFINO UNA FUNCION PARA VALIDAR LOS IDS DE LOS EMPLEADOS ###

def validarid(empleados):
    bandera=0
    while bandera==0:
        id=int(input("Ingrese el id del empleado:\n"))
        if id not in listaid:
            while empleados<1:
                empleados=int(input("Ingrese un id de empleados válido\nIngrese el id del empleado:\n"))
            listaid.append(id)
            bandera=1
        else:
            print("Ya ingresó ese ID")

### DEFINO UNA FUNCION PARA IMPRIMIR LOS RESULTADOS FINALES ###

def imprimirresultados(promedioseccion,turnom,turnot):
    for i in range(2):
        print("\nEl promedio de horas que se trabajó en la sección",i+1,"fue de",promedioseccion[i],"horas\n")

    if turnom>turnot:
        difhoras=turnom-turnot
        print("En el turno mañana se trabajó",difhoras,"horas de más que en el turno tarde\n")
    else:
        if turnot>turnom:
            difhoras=turnot-turnom
            print("En el turno tarde se trabajó",difhoras,"horas de más que en el turno mañana\n")
        else:
            print("En ambos turnos se trabajó la misma cantidad de horas\n")

### COMIENZO DEL CÓDIGO ###

listaturnos=["M","T"]
promedioseccion=[]
turnom=0
turnot=0
listaid=[]

for i in range(2):

    
    cantidadseccion=0
    
    print("sección",i+1)
    
    empleados=int(input("Ingrese la cantidad de empleados de la sección:\n"))
    while empleados<1:
        empleados=int(input("Ingrese una cantidad de empleados válida\nIngrese la cantidad de empleados de la sección:\n"))
    
    for j in range(empleados):
        
        print("Empleado",j+1)
        
        validarid(empleados)
        
        turno=str(input("Ingrese el turno en el que trabajó:\nM - Mañana / T - Tarde\n"))
        turno=turno.upper()
        while turno not in listaturnos:
            turno=str(input("Ingrese un turno válido\nIngrese el turno en el que trabajó:\nM - Mañana / T - Tarde\n"))
            turno=turno.upper()
        
        horas=int(input("Ingrese la cantidad de horas que trabajó el empleado:\n"))
        while horas<1:
            horas=int(input("Ingrese una cantidad de horas mayor a 0\nIngrese la cantidad de horas que trabajó el empleado:\n"))
        
        cantidadseccion=cantidadseccion+horas

        if turno=="M":
            turnom=turnom+horas
        
        if turno=="T":
            turnot=turnot+horas
        
    promedioseccion.append(cantidadseccion/empleados)

imprimirresultados(promedioseccion,turnom,turnot)
