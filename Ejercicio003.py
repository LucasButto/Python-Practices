'''
Ejercicio 3 – Fábrica ventiladores.
En una fábrica de ventiladores se trabaja en 3 turnos: 
Mañana, Tarde y Noche, todos los días laborables.

De un determinado mes, se conoce la cantidad de días laborables que hubo 
y de cada día laborable del mismo se tiene, 
sin orden alguno, las siguientes ternas de datos: 
número del día, turno y cantidad de ventiladores producidos.

Observación:
Debido a que todos los días se cumplen los 3 turnos, habiendo 5 días laborables 
tenemos 15 ternas de datos.

Se pide procesar la información correspondiente a un determinado mes para conocer:
● En qué día y en qué turno se produjeron más ventiladores.
● En qué día y en qué turno se hicieron menos ventiladores.
Tener en cuenta que es necesario validar la consistencia del número de día (valor entero 
que pertenezca al intervalo [1, 31]) y la codificación del turno (letras M, T o N).

'''

dias=set(range(1,32))
turnos={"M", "T", "N"}
laborables=[0, 0, 0, 0, 0]
turnom=[1, 1, 1, 1, 1]
turnot=[1, 1, 1, 1, 1]
turnon=[1, 1, 1, 1, 1]
cantidadmayor=0
cantidadmenor=0
bandera=0


for i in range(15):
    
    salir1=False

    while salir1==False:
        dia= int(input("Ingrese el dia: \n"))
    
        while dia not in dias:
            print("Ingreso no válido")
            dia= int(input("Ingrese el dia: \n"))
    
        for i in range(5):
            if laborables[i]==0 or laborables[i]==dia:
                laborables[i] = dia
                salir1=True
                break
                
            if laborables[i]==dia and (turnom[i]==1 or turnot[i]==1 or turnon[i]==1):
                salir1=True
                break
        
        for i in range(5):
            if laborables[i]==dia and (turnom[i]==0 and turnot[i]==0 and turnon[i]==0):
                salir1=False
                print("Ya cargó los 3 turnos de este día")
                break
        
        if dia not in laborables:
            print("Ingrese un dia laborable")
    
    salir2=False

    while salir2==False:

        turno= input("Ingrese el turno trabajado: \n M: Mañana \n T: Tarde \n N: Noche \n")
        turno=turno.upper()
    
        while turno not in turnos:
            print("Ingreso no válido")
            turno= input("Ingrese el turno trabajado: \n M: Mañana \n T: Tarde \n N: Noche \n")
            turno=turno.upper()
    
        for i in range(5):
            
            if turno=="M" and laborables[i]==dia and turnom[i]!=0:
                turnom[i]=0
                salir2=True
                break
    
            if turno=="T" and laborables[i]==dia and turnot[i]!=0:
                turnot[i]=0
                salir2=True
                break

            if turno=="N" and laborables[i]==dia and turnon[i]!=0:
                turnon[i]=0
                salir2=True
                break
        
        if salir2==False:
            print("ya ingresó ese turno en ese día")         

    cantidad= int(input("Ingrese la cantidad de ventiladores producidos: \n"))
    while cantidad<0:
        print("Ingreso no válido")
        cantidad= int(input("Ingrese la cantidad de ventiladores producidos: \n"))

    if i==1 and bandera==0:
        cantidadmayor=cantidad
        diamayor=dia
        turnomayor=turno

        cantidadmenor=cantidad
        diamenor=dia
        turnomenor=turno
        
        bandera=1

    if cantidad > cantidadmayor:
        cantidadmayor=cantidad
        diamayor=dia
        turnomayor=turno

    if cantidad < cantidadmenor:
        cantidadmenor=cantidad
        diamenor=dia
        turnomenor=turno

print("El día que mas se produjeron ventiladores fue el ",diamayor,"en el turno", turnomayor,"con un total de",cantidadmayor,"ventiladores")
print("El día que menos se produjeron ventiladores fue el ",diamenor,"en el turno", turnomenor,"con un total de",cantidadmenor,"ventiladores")
