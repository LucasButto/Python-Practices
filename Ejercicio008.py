'''
Ejercicio 8 – Comercio diamantes

Una empresa dedicada al comercio de diamantes posee 15 talladores, identificados con un número del 1 al 15. 
Un experto clasificador evalúa los diamantes de acuerdo a tres criterios: el peso en quilates (un número real), 
la pureza (texto de 3 caracteres) y el color (una letra entre la ‘D’ y la ‘Z’).

Semanalmente el experto clasifica los diamantes y vuelca esta información en una tabla ordenada por número de tallador, 
es decir, comienza por los diamantes del tallador 1, luego los del 2 y así sucesivamente hasta terminar con los 15 
talladores. Se dispone de la cantidad de diamantes que tallo cada uno.

Realizar un ejemplo de la tabla y datos que puede contener en la que se vuelca la información. Luego realizar un algoritmo 
que recibiendo los datos de la tabla generada por el experto muestre:

Por cada tallador:
    ● La cantidad de diamantes cuyo color esté entre la ‘D’ y la ‘G’.
    ● El peso total de los diamantes tallados.
En general:
    ● La cantidad total de diamantes tallados.
'''
### DEFINO UNA FUNCION PARA CREAR LA LISTA DE TALLADORES ###

def crearlista():
    
    for i in range(15):
    
        print("Tallador",i+1)
        
        cantidad=int(input("Ingrese la cantidad de diamantes del tallador\n"))
        while cantidad<0:
            cantidad=int(input("Ingrese una cantidad válida\nIngrese la cantidad de diamantes del tallador\n"))
        for j in range(cantidad):
            idtallador.append(i+1)

        if cantidad>0:
            for j in range(cantidad):    
                print("Diamante",j+1)
                
                peso=float(input("Ingrese el peso del diamante en quilates\n"))
                while peso<=0:
                    peso=float(input("Ingrese un pesomayora 0\nIngrese el peso del diamante en quilates\n"))
                listapeso.append(peso)

                pureza=str(input("Ingrese la pureza del diamante\n"))
                while len(pureza)!=3:
                    pureza=str(input("Ingrese una pureza válida\nIngrese la pureza del diamante\n"))
                listapureza.append(pureza)
            
                color=str(input("Ingrese el color del diamante\n"))
                color=color.lower()
                while color not in colores:
                    color=str(input("Ingrese un color válido\nIngrese el color del diamante\n"))
                    color=color.lower()
                listacolor.append(color)
        else:
            print("No ingresó diamantes para tallar")

### IMPRIMO LA LISTA DE TALLADORES ###

def imprimirlista():

    totalcantidad=len(idtallador)

    print(listanombres[0],listanombres[1],listanombres[2],listanombres[3])

    for i in range(totalcantidad):
        print(idtallador[i], listapeso[i], listapureza[i], listacolor[i])

### COMIENZO DEL CÓDIGO ###

colores=['d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
coloresespecificos=['d', 'e', 'f', 'g']
listapeso=[]
listapureza=[]
listacolor=[]
colorespecifico=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
listanombres=["TALLADOR", "PESO", "PUREZA", "COLOR"]
idtallador=[]

crearlista()

imprimirlista()

totalcantidad=len(idtallador)
j=0
totalpeso=0

for i in range(totalcantidad):

    if idtallador[i]==j+1:
        if listacolor[i] in coloresespecificos:
            colorespecifico[j]=colorespecifico[j]+1
        totalpeso=totalpeso+listapeso[i]
    else:
        print("\nLa cantidad de diamantes cuyo color esté entre la ‘D’ y la ‘G’ del tallador",j+1,"es de",colorespecifico[j])
        print("El peso total de los diamantes tallados del tallador",j+1,"es de",totalpeso,"\n")
        
        j=j+1
        totalpeso=0
        
        if idtallador[i]==j+1:
            if listacolor[i] in coloresespecificos: 
                colorespecifico[j]=colorespecifico[j]+1
            totalpeso=totalpeso+listapeso[i]

print("\nLa cantidad de diamantes cuyo color esté entre la ‘D’ y la ‘G’ del tallador",j+1,"es de",colorespecifico[j])
print("El peso total de los diamantes tallados del tallador",j+1,"es de",totalpeso,"\n")

print("La cantidad total de diamantes tallados es de",totalcantidad)
    