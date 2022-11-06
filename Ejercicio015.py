'''
Ejercicio 15 – Empresa cadetería

La empresa de cadetería “Envío Veloz” dispone de los datos relacionados con todos los envíos realizados 
durante un determinado día.

De cada envío se conoce la siguiente información: número de cadete que realizó el envío (valor entero), 
número de envío (valor entero) y una indicación de si el envío fue nocturno o no (carácter S o N). Los datos 
se encuentran agrupados por número de cadete.

No se sabe cuántos envíos hizo cada cadete ni se sabe cuántos envíos se realizaron en el día. Sí se sabe que 
un número de cadete igual a 0 indica que no hay más datos de envíos a procesar.

Se conocen también, el costo de un envío del tipo nocturno y el costo del envio del tipo no nocturno. 
Cada cadete cobrará el 5% del costo del envío.

A partir del ingreso de los datos antes mencionados, calcule e informe:

● El importe a cobrar por cada uno de los cadetes.
● El número de cadete que cobrará más y el monto correspondiente. Si hay más de uno, informar el primero que se encuentre.
● La indicación de si hubo más envíos nocturnos o más envíos no nocturnos, o igual cantidad de envíos nocturnos y no nocturnos.
'''

### DEFINO UNA FUNCION PARA LA CARGA DE DATOS ###

def cargadedatos(listacadetes,listaenvios,listaturno,numscadetes):
    salir=False
    while salir==False:
        cadete=int(input("Ingrese el número de cadete:\n"))
        while cadete<0:
            cadete=int(input("Ingrese un número de caddete válido\nIngrese el número de cadete:\n"))
        
        if cadete==0:
            break
        else:
            listacadetes.append(cadete)
        
        if cadete not in numscadetes:
            numscadetes.append(cadete)
        
        banderaenvio=0
        while banderaenvio==0:
            envio=int(input("Ingrese el número de envío:\n"))
            while envio<1:
                envio=int(input("Ingrese número de envío mayor a 0\nIngrese el número de envío:\n"))
            if envio not in listaenvios:
                    listaenvios.append(envio)
                    banderaenvio=1
            else:
                print("Ya ingresó ese envío")
        
        turno=str(input("El envío fue nocturno?\nSi / No\n"))
        turno=turno.upper()
        while turno!="SI" and turno!="NO":
            turno=str(input("Ingrese una respuesta válida\nEl envío fue nocturno?\nSi / No\n"))
            turno=turno.upper()
        listaturno.append(turno)

### DEFINO UNA FUNCION PARA ACOMODAR LOS DATOS CARGADOS ###

def acomodador(listacadetes,listaenvios,listaturno,numscadetes):
    for i in range(len(listacadetes)-1):
        for j in range(i+1,len(listacadetes)):
            if listacadetes[j]<listacadetes[i]:
                temp=listacadetes[j]
                listacadetes[j]=listacadetes[i]
                listacadetes[i]=temp

                temp=listaenvios[j]
                listaenvios[j]=listaenvios[i]
                listaenvios[i]=temp

                temp=listaturno[j]
                listaturno[j]=listaturno[i]
                listaturno[i]=temp

    for i in range(len(numscadetes)-1):
        for j in range(i+1,len(numscadetes)):
            if numscadetes[j]<numscadetes[i]:
                temp=numscadetes[j]
                numscadetes[j]=numscadetes[i]
                numscadetes[i]=temp

### DEFINO UNA FUNCION PARA IMPRIMIR LOS RESULTADOS ###

def imprimirresultados(listacadetes,listaturno,numscadetes):
    
    print("\n### RESULTADOS DEL DIA ###\n")
    
    preciod=600
    precion=900
    mayor=0
    for i in range(len(numscadetes)):
        suma=0
        for j in range(len(listacadetes)):
            
            if listacadetes[j]==numscadetes[i]:
                if listaturno[j]=="SI":
                    suma=suma+precion
                else:
                    suma=suma+preciod
        
        if suma>mayor:
            mayor=suma
            cadetemayor=numscadetes[i]
        
        print("El cadete",numscadetes[i],"debe cobrar $",suma)

    print("\nEl cadete número",cadetemayor,"es quien mayor cobró con un total de $",mayor)

    contadornoche=0
    contadordia=0
    for i in range(len(listacadetes)):
        if listaturno[i]=="SI":
            contadornoche=contadornoche+1
        else:
            contadordia=contadordia+1

    if contadornoche==contadordia:
        print("\nHubo la misma cantidad de envíos nocturnos que diurnos\n")
    else:
        if contadornoche>contadordia:
            print("\nHubo más envíos nocturnos que diurnos\n")
        else:
            print("\nHubo más envíos diurnos que nocturnos\n")

### COMIENZO DEL CÓDIGO ###

listacadetes=[]
listaenvios=[]
listaturno=[]
numscadetes=[]

cargadedatos(listacadetes,listaenvios,listaturno,numscadetes)

acomodador(listacadetes,listaenvios,listaturno,numscadetes)

imprimirresultados(listacadetes,listaturno,numscadetes)
