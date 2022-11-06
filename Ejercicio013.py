'''
Ejercicio 13 - Guardia hospital

En la guardia de un hospital ingresan pacientes todos los días durante una semana, y de cada uno se tiene: 
número de documento, cobertura (O: Obra social - P: Prepaga), edad. A su vez, se los clasifica según la 
prioridad de atención:

    ● Rojo: Atención inmediata - pacientes críticos.
    ● Naranja: Atención en menos de 10 minutos - pacientes graves o emergentes.
    ● Amarillo: Atención en un máximo de 60 minutos - urgencias comunes.
    ● Verde: Atención en menos de 120 minutos - urgencias menores.
    ● Azul: Demora máxima de 240 minutos - problemas no urgentes.

Los datos se leen en orden de día (1 a 7), pero no se sabe cuántos pacientes ingresan cada día. Proponer un fin 
de datos conveniente para los datos de un día, y desarrollar un algoritmo para ingresar y procesar los datos, 
el que debería mostrar los siguientes resultados:

Por día:
    ● El promedio de edades de los pacientes que ingresaron.
    ● Mostrar si ingresaron con cobertura por obra social, prepaga o iguales cantidades.
    ● x. La cantidad de pacientes por cada clasificación en atención. / Proporción sobre el total.

Con respecto a la semana completa:
    ● El número de documento, sexo y edad de la persona de mayor edad que haya ingresado.
    ● La cantidad total de pacientes ingresados.
        o ¿Qué día ingresaron más pacientes críticos o graves?
'''
### DEFINO UNA FUNCION PARA LA CARGA DE DATOS DE LOS PACIENTES ###

def cargadedatos(listadias,listadni,listacoberturas,listaedades,listasexos,listaprioridad):

    atencion={"ROJO", "NARANJA", "AMARILLO",  "VERDE", "AZUL"}
    
    for i in range(7):
        salirdias=False
        pacientesdia=0
        validardni=[]
        print("\nDía",i+1,":")
        while salirdias==False:
            listadias.append(i+1)
            pacientesdia=pacientesdia+1
            
            banderadni=0
            while banderadni==0:
                dni=int(input("Ingrese el DNI del paciente "+ str(pacientesdia) +":\n"))
                while dni>99999999 or dni<1000000:
                    dni=(int(input("Ingrese un DNI válido\nIngrese el DNI del paciente "+ str(pacientesdia) +":\n")))
                if dni not in validardni:
                    validardni.append(dni)
                    banderadni=1
                else:
                    print("Ya ingresó ese DNI este día")
            listadni.append(dni)

            cobertura=str(input("Ingrese la cobertura del paciente "+ str(pacientesdia) +":\nO: Obra social - P: Prepaga\n"))
            cobertura=cobertura.upper()
            while cobertura!="O" and cobertura!="P":
                cobertura=str(input("Ingrese una cobertura válida\nIngrese la cobertura del paciente "+ str(pacientesdia) +":\nO: Obra social - P: Prepaga\n"))
                cobertura=cobertura.upper()
            listacoberturas.append(cobertura)

            edad=int(input("Ingrese la edad del paciente "+ str(pacientesdia) +":\n"))
            while edad<1:
                edad=int(input("Ingrese una edad mayor a 0\nIngrese la edad del paciente "+ str(pacientesdia) +":\n"))
            listaedades.append(edad)

            sexo=str(input("Ingrese el sexo del paciente "+ str(pacientesdia) +":\nM - Masculino / F - Femenino\n"))
            sexo=sexo.upper()
            while sexo!="M" and sexo!="F":
                sexo=str(input("Ingrese un sexo válido\nIngrese el sexo del paciente "+ str(pacientesdia) +":\nM - Masculino / F - Femenino\n"))
                sexo=sexo.upper()
            listasexos.append(sexo)

            prioridad=str(input("Ingrese la prioridad de atención del paciente "+ str(pacientesdia) +":\nRojo: Atención inmediata - pacientes críticos.\nNaranja: Atención en menos de 10 minutos - pacientes graves o emergentes.\nAmarillo: Atención en un máximo de 60 minutos - urgencias comunes.\nVerde: Atención en menos de 120 minutos - urgencias menores.\nAzul: Demora máxima de 240 minutos - problemas no urgentes.\n"))
            prioridad=prioridad.upper()
            while prioridad not in atencion:
                prioridad=str(input("Ingrese una prioridad de atención válida\nIngrese la prioridad de atención del paciente "+ str(pacientesdia) +":\nRojo: Atención inmediata - pacientes críticos.\nNaranja: Atención en menos de 10 minutos - pacientes graves o emergentes.\nAmarillo: Atención en un máximo de 60 minutos - urgencias comunes.\nVerde: Atención en menos de 120 minutos - urgencias menores.\nAzul: Demora máxima de 240 minutos - problemas no urgentes.\n"))
                prioridad=prioridad.upper()
            listaprioridad.append(prioridad)

            respuesta=str(input("Quiere ingresar otro paciente?\nSi / No\n"))
            respuesta=respuesta.upper()
            while respuesta!="SI" and respuesta!="NO":
                respuesta=str(input("Ingrese una respusta válida\nQuiere ingresar otro paciente?\nSi / No\n"))
                respuesta=respuesta.upper()
            
            if respuesta=="NO":
                salirdias=True
        
        
        resultadosdias(i,listadias,listadni,listaedades,listacoberturas,listaprioridad)
    
    resultadossemana(listadni,listaedades,listasexos,listaprioridad)

### DEFINO UNA FUNCION PARA MOSTRAR LOS RESULTADOS DE CADA DIA ###

def resultadosdias(i,listadias,listadni,listaedades,listacoberturas,listaprioridad):
    
    totaledades=0
    cantidaddia=0
    cantidadobra=0
    cantidadprepaga=0
    rojos=0
    naranjas=0
    amarillos=0
    verdes=0
    azules=0

    for j in range(len(listadni)):
        
        if listadias[j]==i+1:
            totaledades=totaledades+listaedades[j]
            cantidaddia=cantidaddia+1
            
            if listacoberturas[j]=="O":
                cantidadobra=cantidadobra+1
            
            if listacoberturas[j]=="P":
                cantidadprepaga=cantidadprepaga+1
            
            if listaprioridad[j]=="ROJO":
                rojos=rojos+1
            
            if listaprioridad[j]=="NARANJA":
                naranjas=naranjas+1
            
            if listaprioridad[j]=="AMARILLO":
                amarillos=amarillos+1
            
            if listaprioridad[j]=="VERDE":
                verdes=verdes+1
            
            if listaprioridad[j]=="AZUL":
                azules=azules+1

        
    promedioedades=totaledades/cantidaddia
    promediorojo=(rojos*100)/cantidaddia
    promedionaranja=(naranjas*100)/cantidaddia
    promedioamarillo=(amarillos*100)/cantidaddia
    promedioverde=(verdes*100)/cantidaddia
    pormedioazul=(azules*100)/cantidaddia

    print("\n### RESULTADOS DEL DIA ###\n")
    print("El promedio de edades de los pacientes que ingresaron el día",i+1,"es de",round(promedioedades,2),"años")
    print("En el día",i+1,",",cantidadobra,"pacientes ingresaron con obra social y",cantidadprepaga,"pacientes ingresaron con prepaga")
    print("En el día",i+1,", el %",round(promediorojo,3),"de los pacientes fueron de clasificación rojo")
    print("En el día",i+1,", el %",round(promedionaranja,3),"de los pacientes fueron de clasificación naranja")
    print("En el día",i+1,", el %",round(promedioamarillo,3),"de los pacientes fueron de clasificación amarillo")
    print("En el día",i+1,", el %",round(promedioverde,3),"de los pacientes fueron de clasificación verde")
    print("En el día",i+1,", el %",round(pormedioazul,3),"de los pacientes fueron de clasificación azul")
    
### DEFINO UNA FUNCION PARA MOSTRAR LOS RESULTADOS DE LA SEMANA ###

def resultadossemana(listadni,listaedades,listasexos,listaprioridad):
    mayoredad=0
    for j in range(len(listadni)):
        if listaedades[j]>mayoredad:
            mayoredad=listaedades[j]
            dnimayor=listadni[j]
            sexomayor=listasexos[j]
    
    mayorgravesfinal=-1

    for i in range(7):
        mayorgraves=0
        for j in range(len(listadni)):
            if (listaprioridad[j]=="ROJO" or listaprioridad[j]=="NARANJA") and listadias[j]==i+1:
                mayorgraves=mayorgraves+1
        if mayorgraves>mayorgravesfinal:
            mayorgravesfinal=mayorgraves
            mayordiagraves=listadias[i]
    
    print("\n### RESULTADOS DE LA SEMANA ###\n")        
    print("El mayor paciente de la semana fue el dni",dnimayor,"con",mayoredad,"años y de sexo",sexomayor)
    print("La cantidad total de pacientes ingresados en la semana fue de",len(listadni),"pacientes")
    print("El día que ingresaron más pacientes críticos o graves fue el día",mayordiagraves,"con un total de",mayorgravesfinal,"pacientes\n")


### COMIENZO DEL CÓDIGO ###

listadias=[]
listadni=[]
listacoberturas=[]
listaedades=[]
listasexos=[]
listaprioridad=[]

cargadedatos(listadias,listadni,listacoberturas,listaedades,listasexos,listaprioridad)