'''
Ejercicio 2 – Central telefónica

Una central telefónica registra la duración de cada llamada, expresada en segundos.
A partir de esta información se quiere convertir la duración de cada llamada a:
horas, minutos y segundos y mostrarla.

Luego, al finalizar el ingreso de datos y el proceso de conversión, determinar:

    La cantidad de llamadas que superaron los 10 minutos.
    El promedio de duración de las llamadas (en segundos).
    La mínima duración de llamada (en segundos).

    No se sabe cuántas llamadas se han registrado, proponer un fin de datos.

''' 

# Datos: duración llamada en segundos.
# Estructura de contro: while.
# Convetir a horas, minutos y segundos
# Contar llamadas.
# Sumar --> luego hacer el promedio.
# Buscar el minimo.
# Mostrar resultados.

###########  Programa principal  ###########

salir=False
j=1
suma=0
ContadorLlamadas=0
ContadorLlamadas10=0
Minimo=10000000000000000000000000

while salir==False:
    
    ContadorHoras=0
    ContadorMinutos=0

    horas=0
    minutos=0

    print("")
    print("Ingrese la duración de la llamada", j, "(En segundos)")
    print("Ingrese 0 (cero) para finalizar la carga de datos")
    duracion = int(input())

    while duracion<0:
        print("Ingreso no válido")
        print("Ingrese la duración de la llamada", j, "(En segundos)")
        duracion = int(input())
    
    if duracion!=0:
        ContadorLlamadas=ContadorLlamadas+1
        suma=suma+duracion
        
        if duracion<Minimo:
            Minimo=duracion
        
        while duracion>59:
            duracion=duracion-60
            ContadorMinutos=ContadorMinutos+1
        
        while ContadorMinutos>59:
            ContadorMinutos=ContadorMinutos-60
            ContadorHoras=ContadorHoras+1
        
        if ContadorMinutos>=10 or ContadorHoras>=1:
            ContadorLlamadas10=ContadorLlamadas10+1

        print("La llamada",j,"duró:")
        print(ContadorHoras,"horas",ContadorMinutos,"minutos ",duracion,"segundos")
        
        j=j+1
    else:
        salir=True
        

promedio=suma/ContadorLlamadas
print("")
print(ContadorLlamadas10," llamadas duraron más de 10 minutos")
print("El promedio de duracion de las llamadas es de",round(promedio,2),"segundos")
print("La mínima duración de llamada fue de",Minimo,"segundos")
