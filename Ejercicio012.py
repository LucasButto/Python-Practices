'''
Ejercicio 12 – Línea de producción

El sector de ensamble de una línea productiva de una empresa está dotado de 15 operadores los 
cuales están distribuidos en 3 turnos. Los operadores están identificados con un número del 1 al 15. 
Del 1 al 5 están en el primer turno, del 6 al 10 en el segundo y del 11 al 15 en el tercero.

Cada un determinado período de tiempo (se desconoce la cantidad de días transcurridos hasta esa fecha), 
el Gerente de Producción necesita evaluar distintos indicadores asociados con sus objetivos anuales. 
Para realizar esto extrae los siguientes datos del sistema de gestión: día y mes de la producción, 
costo unitario de cada unidad ensamblada ese día y cantidad de productos ensamblados.

Realizar los siguientes algoritmos:

Algoritmo A:
● ¿Cuál es el costo total de producción por las unidades de cada día?
● Determinar el promedio de productos por colaboradores del turno 2 ensamblados en cada día.
● Calcular la cantidad de ausencias por turno en todo el período. 

Algoritmo B:
● Determinar la jornada (día y mes) de mayor ensamble en todo el período. Considerar que hay una sola
● Determinar el promedio diario de productos ensamblados del mes 6.
● Informar a medida que se vayan ingresando los datos mediante el texto “Alerta de ensamble” si, en 
ese día, la cantidad de productos ensamblados no superó las 400 unidades o superó las 1700.

Algoritmo C:
● Determinar la cantidad total de productos ensamblados en cada turno en el período evaluado.
● Determinar el mes en el cuál se produjo el mayor costo unitario y cuál fue ese mismo.
'''
### DEFINO UNA FUNCION PARA SABER CUANTOS DIAS TENDRA CADA MES ###

def cantidaddias(i, dias30, dias31):
    if i+1 in dias30:
        cantidad=30
    else:
        if i+1 in dias31:
            cantidad=31
        else:
            cantidad=28
    
    return cantidad

### DEFINO UNA FUNCION PARA EL ALGORITMO A ###

def algoritmoA(contadordias,listadias,listameses,costototaldia,sumaturno2,ausentes1,ausentes2,ausentes3):
    for i in range(contadordias):
        
        costototaldia=0
        for j in range(15):
            costototaldia=costototaldia+listacostounitario[i]*listaensamblados[i][j]
        print("El costo total del día",listadias[i],", mes",listameses[i],"es de $",costototaldia)
        
        for j in range(5,10):
            sumaturno2=sumaturno2+listaensamblados[i][j]
        promedio=sumaturno2/5
        print("El promedio de productos por colaboradores del turno 2 ensamblados en el día",listadias[i],"del mes",listameses[i],"es de",promedio,"productos ensamblados por operador")

        for j in range(15):

            if j<5:
                if listaensamblados[i][j]==0:
                    ausentes1=ausentes1+1
            if j>=5 and j<10:
                if listaensamblados[i][j]==0:
                    ausentes2=ausentes2+1
            if j>=10 and j<15:
                if listaensamblados[i][j]==0:
                    ausentes3=ausentes3+1

    print("Ausencias turno 1:",ausentes1)
    print("Ausencias turno 2:",ausentes2)
    print("Ausencias turno 3:",ausentes3)

### DEFINO UNA FUNCION PARA EL ALGORITMO B ###

def algoritmoB(contadordias,listameses,listadias,sumames6,alerta400_1700,bandera400_1700): 
    
    if bandera400_1700==True:
        if alerta400_1700<400 or alerta400_1700>1700:
            print("\nAlerta de ensamble\n")       
        
    if bandera400_1700==False:
        mayorensamble=-1
        for i in range(contadordias):
            ensambledia=0
            for j in range(15):
                ensambledia=ensambledia+listaensamblados[i][j]
            
            if ensambledia>mayorensamble:
                mayorensamble=ensambledia
                mayordiaensamble=listadias[i]
                mayormesensamble=listameses[i]  
        print("La jornada con mayor ensamble de todo el período fue en el mes",mayormesensamble,", día",mayordiaensamble,"con un total de",mayorensamble,"ensambles en ese día")

        for i in range(contadordias):
            for j in range(15):
                if listameses[i]==6:
                    sumames6=sumames6+listaensamblados[i][j]
            promedio=sumames6/15
            if listameses[i]==6:
                print("El promedio de productos ensamblados del mes 6, día",listadias[i],"es de",promedio,"productos ensamblados por operador")

### DEFINO UNA FUNCION PARA EL ALGORITMO C ###

def algoritmoC(listacostounitario,contadordias,listameses,listadias,totalensambles1,totalensambles2,totalensambles3):
    
    for i in range(contadordias):
        for j in range(15):
            if j<5:
                totalensambles1=totalensambles1+listaensamblados[i][j]
            if j>=5 and j<10:
                totalensambles2=totalensambles2+listaensamblados[i][j]
            if j>=10 and j<15:
                totalensambles3=totalensambles3+listaensamblados[i][j]
    print("Cantidad total de productos ensamblados en turno 1:",totalensambles1)
    print("Cantidad total de productos ensamblados en turno 2:",totalensambles2)
    print("Cantidad total de productos ensamblados en turno 3:",totalensambles3)

    mayorcostounitario=0
    for i in range(contadordias):
        if listacostounitario[i]>mayorcostounitario:
            mayorcostounitario=listacostounitario[i]
            mayordiacosto=listadias[i]
            mayormescosto=listameses[i] 
    print("El período en el cual se produjo el mayor costo unitario fue el mes",mayormescosto,",día",mayordiacosto,"con un costo unitario de $",mayorcostounitario,"\n")

### COMIENZO DEL CÓDIGO ###

dias30=[4,6,9,11]
dias31=[1,3,5,7,8,10,12]
listacostounitario=[]
listaensamblados=[]
listadias=[]
listameses=[]
costototaldia=float(0)
contadordias=0
sumaturno2=0
sumames6=0
ausentes1=0
ausentes2=0
ausentes3=0
bandera400_1700=False
alerta400_1700=0
totalensambles1=0
totalensambles2=0
totalensambles3=0


for i in range(365):
    listaensamblados.append([0]*15)

for i in range(12):
    
    cantidad=cantidaddias(i, dias30, dias31)
    print("\nMes",i+1,"\n")

    for j in range(cantidad):
        empleados=1
        listameses.append(i+1)
        listadias.append(j+1)
        print("Día",j+1)
        costounitario=float(input("Ingrese el costo unitario del día "+ str(j+1) +" del mes "+ str(i+1) +":\n"))
        while costounitario<=0:
            costounitario=float(input("Ingrese un costo unitario mayor a 0\nIngrese el costo unitario del día "+ str(j+1) +" del mes "+ str(i+1) +":\n"))
        listacostounitario.append(costounitario)
        
        for k in range(3):
            print("Turno",k+1)
            
            for l in range(5):
                print("Empleado",empleados)
                
                ensamblados=int(input("Ingrese la cantidad de productos ensamblados del empleado:\n"))
                while ensamblados<0:
                    ensamblados=int(input("Ingreso no válido\nIngrese la cantidad de productos ensamblados del empleado:\n"))
                
                listaensamblados[j][empleados-1]=ensamblados
                
                alerta400_1700=alerta400_1700+ensamblados

                empleados=empleados+1
        
        contadordias=contadordias+1
        
        if alerta400_1700<400 or alerta400_1700>1700:
            bandera400_1700=True
            algoritmoB(contadordias,listameses,listadias,sumames6,alerta400_1700,bandera400_1700)
        bandera400_1700=False

        respuesta=str(input("Desea evaluar la producción?\nSi \ No\n"))
        respuesta=respuesta.upper()
        while respuesta!="SI" and respuesta!="NO":
            respuesta=str(input("Ingrese una opción válida\nDesea evaluar la producción?\nSi \ No\n"))
            respuesta=respuesta.upper()
        
        if respuesta=="SI":
            print("\n### EVALUACIÓN DE LA PRODUCCIÓN ###\n")
            algoritmoA(contadordias,listadias,listameses,costototaldia,sumaturno2,ausentes1,ausentes2,ausentes3) 
            algoritmoB(contadordias,listameses,listadias,sumames6,alerta400_1700,bandera400_1700)           
            algoritmoC(listacostounitario,contadordias,listameses,listadias,totalensambles1,totalensambles2,totalensambles3)        