'''
Ejercicio 9 – Laboratorio bactereológico

En un laboratorio de bacteriología, se tienen clasificados los tipos de análisis que se realizan en 27 categorías. 
De cada categoría de análisis se conoce la cantidad de reactivos necesarios y de cada uno de ellos se tiene:
    ● miligramos a usar.
    ● temperatura de fusión del mismo (entero).

Los valores de los datos se ingresarán desde teclado. Desarrollar un programa que permita procesar esos datos para 
obtener para cada categoría de análisis:
    ● El peso total de los materiales reactivos necesarios;
    ● La cantidad de reactivos requieren entre 10 y 20 mg;
    ● El porcentaje de reactivos que tienen una temperatura de fusión superior a los 50 ºC.
    
Además, se desea conocer cuál categoría consume mayor cantidad de reactivos en mg y cuál es esa cantidad.
'''
### DEFINO UNA FUNCION PARA VALIDAR LA CANTIDAD DE REACTIVOS ###

def validarreactivos():
    
    resultado=int(input("Ingrese la cantidad de reactivos:\n"))
    
    while resultado<=0:
        resultado=int(input("Ingrese una cantidad mayor a 0\nIngrese la cantidad de reactivos:"))
    
    return resultado
    
### DEFINO UNA FUNCION PARA IMPRIMIR LOS RESULTADOS DEL FINAL ###

def imprimirresultados(pesototal,contador1020,porcentaje):
    print("\nEl peso total de los materiales reactivos necesarios es",pesototal)
    print("La cantidad de reactivos requieren entre 10 y 20 mg son",contador1020)
    print("El porcentaje de reactivos que tienen una temperatura de fusión superior a los 50 ºC es %",porcentaje,"\n")

### COMIENZO DEL CÓDIGO ###

mayor=0

for i in range(1):
    
    pesototal=0
    contador1020=0
    contadorporc=0
    
    print("categoría",i+1)
    
    reactivos=validarreactivos()
    
    for j in range(reactivos):
        print("reactivo",j+1)
        miligramos=float(input("Ingrese los miligramos a usar\n"))
        while miligramos<=0:
            miligramos=float(input("Ingrese una cantidad mayor a 0\nIngrese los miligramos a usar"))

        pesototal=pesototal+miligramos

        if pesototal>mayor:
            mayor=pesototal
            categoria=i+1

        if miligramos<=20 and miligramos>=10:
            contador1020=contador1020+1
        
        temp=int(input("Ingrese la temperatura de fusión del mismo en ºC\n"))

        if temp>50:
            contadorporc=contadorporc+1
        
    porcentaje=contadorporc*100/reactivos
    
    imprimirresultados(pesototal,contador1020,porcentaje)
    

print("La categoría que consume mayor cantidad de reactivos en mg es la",categoria,"º con un total de",mayor,"mg en reactivos\n")