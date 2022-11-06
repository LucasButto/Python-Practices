'''
Ejercicio 7 – Salto en largo

En un torneo de salto en largo se pueden inscribir hasta 50 participantes. 
Cada participante está identificado con un número no necesariamente correlativo y 
realiza 3 saltos, de los cuales se registra el largo del mismo.

Se pide, primero realizar un bosquejo de los datos. Luego realizar un algoritmo que informe 
el ganador de la competencia (aquel que saltó más lejos en cualquiera de los 3 intentos), 
la distancia del salto ganador y cuántos participantes se inscribieron.

Desafío extra: suponer que un participante puede no realizar los 3 saltos y que en este caso 
se lo considera descalificado, por lo que no se lo tendrá en cuenta para elegir al ganador de 
la competencia. Modificar el algoritmo anterior para contemplar este caso.
'''

### DEFINO UNA FUNCION PARA CREAR LA LISTA DE COMPETIDORES ###

def crearlista(concursantes):
    
    for i in range(concursantes):
        saltos.append([0]*3)

    for i in range(concursantes):
    
        banderaid=0
        
        while banderaid==0:
            id= int(input("Ingrese el id del participante: \n"))
            if id not in ids:
                while id<0:
                    id= int(input("Ingrese un id de participante válido \nIngrese el id del participante:"))
                ids.append(id)
                banderaid=1
            else:
                print("Ya ingresó ese ID")
        
        for j in range(3):
            print("salto",j+1)
            salto= float(input("Ingrese la distancia del salto en cm:\nSi no realizó el salto ingrese 0\n"))
            while salto<0:
                salto= float(input("Ingrese una distacia válida\nIngrese la distancia del salto en cm:\nSi no realizó el salto ingrese 0\n"))
            saltos[i][j]=salto
        
        respuesta=input("Desea ingresar otro concursante?\n Si - No\n")
        respuesta=respuesta.upper()
            
        while respuesta!="SI" and respuesta!="NO":
            respuesta=input("Ingrese una opción válida \nDesea ingresar otro concursante?\n Si - No\n")
            respuesta=respuesta.upper()
            
        if respuesta=="NO":
            break


### COMIENZO DEL CÓDIGO ###

ids=[]
saltos=[]
contadorsaltos=0
concursantes=50

crearlista(concursantes)

contador=len(ids)

saltomax=saltos[0][0]

for i in range(contador):
    
    if saltos[i][0]==0 or saltos[i][1]==0 or saltos[i][2]==0:
       contador=contador-1 
    
    if saltos[i][0]!=0 and saltos[i][1]!=0 and saltos[i][2]!=0:
        for j in range(3):
            if saltos[i][j]>saltomax:
                saltomax=saltos[i][j]
                idganador=ids[i]   
            
        
        

print("El ganador de la competencia fue el concunrsante con el ID",idganador,"con un salto de",saltomax,"cm")
print("La cantidad total de concursantes fue de",contador)

