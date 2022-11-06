'''
Ejercicio 10 – Clasificación películas

El sistema de clasificación de contenido de las películas por edades.
Uno de los sistemas de clasificación de películas dispone las siguientes categorías:

Clasificación           Descripción                      Color de fondo
G                  Todas las audiencias                     VERDE
P               Asistencia de padres recomendada            VERDE
M               Asistencia de padres muy recomendada        AMARILLO
R                       Restringido                         AMARILLO
N               Prohibida para menores de 17                ROJO

Para anticipar el contenido de la película o del avance (resumen de la película), se creó una calificación 
especial con franjas de color. Los colores se refieren a los colores de fondo en los avances, aparecidos al principio.

Situación problemática
Se solicita realizar un algoritmo en pseudocódigo que, entre otras tareas, muestre el color de fondo a partir del dato 
de la clasificación, partiendo de un listado de películas de diferentes países.

El listado contiene la siguiente información:
    ● Código de país (entero entre 1 y 30);
    ● Código de película (entero);
    ● Clasificación (carácter).
El listado está ordenado por código de país. Se sabe que en total son 30 países. No se sabe cuántas películas hay por 
cada país, pero un código de película igual a 0 indica el final.

El algoritmo deberá solicitar por cada película los tres datos. A partir del dato de clasificación mostrar en pantalla 
el nombre del color correspondiente (VERDE, AMARILLO o ROJO). Además, se debe calcular por cada país el porcentaje de 
películas calificadas como G o P.

El algoritmo deberá mostrar también el código del país con mayor cantidad de películas y dicha cantidad.
'''
### DEFINO UNA FUNCION PARA IMPRIMIR LOS COLORES DE LA CLASIFICACIÓN DE LA PELÍCULA Y DEVUELVE UN CONTADOR###

def imprimircolores(clasificacion, contadorporc):

    if clasificacion=="G" or clasificacion=="P":
        print("VERDE")
        contadorporc=contadorporc+1
            
    if clasificacion=="M" or clasificacion=="R":
        print("AMARILLO")
            
    if clasificacion=="N":
        print("ROJO")
    
    return contadorporc

### COMIENZO DEL CÓDIGO ###

clasificaciones=["G","P","M","R","N"]
mayor=0
bandera=0

for i in range(3):
    cod_pelicula=1
    cantidad=0
    contadorporc=0
    listapeliculas=[]
    
    while cod_pelicula!=0:

        print("Código del país:",i+1)

        while bandera==0:
            cod_pelicula=int(input("Ingrese el código de la película\nsi no hay más películas ingrese 0\n"))
            if cod_pelicula not in listapeliculas:
                while cod_pelicula<0:
                    cod_pelicula=int(input("Ingrese un código válido\nIngrese el código de la película\nsi no hay más películas ingrese 0\n"))
                listapeliculas.append(cod_pelicula)
                bandera=1
            else:
                print("Ya ingresó ese código")

        bandera=0

        if cod_pelicula==0:
            break
        
        clasificacion=str(input("Ingrese la clasificación de la película:\nG-Todas las audiencias\nP-Asistencia de padres recomendada\nM-Asistencia de padres muy recomendada\nR-Restringido\nN-Prohibida para menores de 17\n"))
        clasificacion=clasificacion.upper()
        while clasificacion not in clasificaciones:
            clasificacion=str(input("Ingrese un código válido\nIngrese la clasificación de la película:\nG-Todas las audiencias\nP-Asistencia de padres recomendada\nM-Asistencia de padres muy recomendada\nR-Restringido\nN-Prohibida para menores de 17\n"))
            clasificacion=clasificacion.upper()
        
        contadorporc=imprimircolores(clasificacion,contadorporc)

        cantidad=cantidad+1
    
    if cantidad>mayor:
        mayor=cantidad
        maspeliculas=i+1

    if cantidad!=0:
        porcentaje=contadorporc*100/cantidad

    print("\nEl porcentaje de películas calificadas como G o P del país",i+1,"es del %",porcentaje,"\n")
        
print("El país con mayor cantidad de películas es el",maspeliculas,"con un total de",mayor,"películas\n")
