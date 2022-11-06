'''
Ejercicio 14 – Kiosco cubanitos

Un kiosco vende cubanitos rellenos de 3 sabores distintos: chocolate (C), dulce de leche (D) y pasta de maní (P).

Los cubanitos se venden en paquetitos individuales o en cajas de 6 unidades. Las cajas pueden contener cubanitos 
todos del mismo sabor o de sabores mezclados (2 de cada sabor).

Se dispone del detalle de las ventas realizadas en cada uno de los 24 días hábiles del último mes, con la siguiente 
información: Tipo de empaque 1 (unitario), 2 (caja) sabor (Chocolate / Dulce de leche / Pasta de maní / Mezcla) y 
cantidad comprada.

No se conoce la cantidad de ventas realizadas para cada día, pero un código de tipo de empaque igual a 0 (cero) 
indica fin de ventas del día.

El kiosco necesita saber:
● Para cada día del mes, los porcentajes de ventas de cada uno de los 3 sabores.
● La recaudación total del mes, sabiendo que cada cubanito cuesta $10.
● El día de mayor recaudación, informando también la recaudación correspondiente. Se asumen que todos los días hubo 
ventas y que no hubo días con igual recaudación.

Se solicita hacer el análisis del problema y el algoritmo en pseudocódigo que resuelva la situación problemática planteada.
'''

### DEFINO UNA FUNCION PARA LA CARGA DE DATOS ###

def crearlista(i, listaempaque, listasabor, listacantidad):
    
    sabores={"D","C","P"}
    salir=False
    cantidaddia=0
    cantidadc=0
    cantidadd=0
    cantidadp=0
    cantidadm=0
    recaudaciondia=0

    while salir==False:
        
        empaque=int(input("Ingrese el tipo de empaque que quiere\n1 - Unitario\n2 - Caja 6 unidades\n0 - no hay mas ventas\n"))
        while empaque!=1 and empaque!=2 and empaque!=0:
            empaque=int(input("Ingrese una opción válida\nIngrese el tipo de empaque que quiere\n1 - Unitario\n2 - Caja 6 unidades\n0 - No hay mas ventas\n"))

        if empaque==0:
            break
        
        listaempaque.append(empaque)

        if empaque==1:
            sabor=str(input("ingrese el gusto que quiere\nC - Chocolate\nD - Dulce de leche\nP - Pasta de maní\n"))
            sabor=sabor.upper()
            while sabor not in sabores:
                sabor=str(input("Ingrese una opción válida\nIngrese el gusto que quiere\nC - Chocolate\nD - Dulce de leche\nP - Pasta de maní\n"))
                sabor=sabor.upper()
            listasabor.append(sabor)
        
        if empaque==2:
            sabor=str(input("ingrese los gustos que quiere en la caja\nC - Solo Chocolate\nD - Solo Dulce de leche\nP - Solo Pasta de maní\nM - Mezcla (2 de cada uno)\n"))
            sabor=sabor.upper()
            while sabor not in sabores and sabor!="M":
                sabor=str(input("Ingrese una opción válida\nIngrese los gustos que quiere en la caja\nC - Solo Chocolate\nD - Solo Dulce de leche\nP - Solo Pasta de maní\nM - Mezcla (2 de cada uno)\n"))
                sabor=sabor.upper()
            listasabor.append(sabor)

        cantidad=int(input("Ingrese la cantidad que quiera comprar\n"))
        while cantidad<1:
            cantidad=int(input("Ingrese una cantidad mayor a 0\nIngrese la cantidad que quiera comprar\n"))
        listacantidad.append(cantidad)

        if empaque==1:
            cantidaddia=cantidaddia+cantidad
        if empaque==2:
            cantidaddia=cantidaddia+cantidad*6

        if sabor=="C":
            if empaque==1:
                cantidadc=cantidadc+cantidad
            if empaque==2:
                cantidadc=cantidadc+(cantidad*6)
                
        if sabor=="D":
            if empaque==1:
                cantidadd=cantidadd+cantidad
            if empaque==2:
                cantidadd=cantidadd+(cantidad*6)
        
        if sabor=="P":
            if empaque==1:
                cantidadp=cantidadp+cantidad
            if empaque==2:
                cantidadp=cantidadp+(cantidad*6)
        
        if sabor=="M":
            cantidadm=cantidadm+(cantidad)
        
        if empaque==2:
            recaudaciondia=recaudaciondia+((cantidad*6)*10)
        else:
            recaudaciondia=recaudaciondia+((cantidad*1)*10)
    
    print("\n### RESULTADOS DEL DIA ###\n")

    if cantidaddia==0:
        print("No se realizaron ventas ese día\n")
    else:
        porcentajec=(cantidadc+(cantidadm*2))/cantidaddia*100
        porcentajed=(cantidadd+(cantidadm*2))/cantidaddia*100
        porcentajep=(cantidadp+(cantidadm*2))/cantidaddia*100
        
        resultadosdia(porcentajec, porcentajed, porcentajep)

    return recaudaciondia

def resultadosdia(porcentajec, porcentajed, porcentajep):
    print("El %",round(porcentajec,3),"de las ventas fue del sabor de chocolate")
    print("El %",round(porcentajed,3),"de las ventas fue del sabor de dulce de leche")
    print("El %",round(porcentajep,3),"de las ventas fue del sabor de pasta de maní\n")


### COMIENZO DEL CÓDIGO ###

listadias=[]
listaempaque=[]
listasabor=[]
listacantidad=[]
recaudacionmes=0
recaudacionmayor=0

for i in range(2):
    print("Día",i+1)
    listadias.append(i+1)
    recaudacion=crearlista(i, listaempaque, listasabor, listacantidad)
    
    if recaudacion>recaudacionmayor:
        recaudacionmayor=recaudacion
        diamayor=i+1
    
    recaudacionmes=recaudacionmes+recaudacion

print("\n### RESULTADOS DE LA SEMANA ###\n")
print("La recaudación mayor del mes fue en el día",diamayor,"con un total de $",recaudacionmayor)
print("La recaudación total del mes fue de $",recaudacionmes,"\n")