'''
Ejercicio 16 - Seguridad automóviles

Para evaluar la seguridad de los automóviles, la empresa NCAP realiza pruebas que representan acciones reales que se 
dan en las rutas y que pueden significar daño, o incluso la muerte, tanto para  los  pasajeros  como  para  los  
peatones. En  estas  pruebas,  los  fabricantes  de  automóviles tienen que demostrar que sus autos vienen equipados 
con los elementos tecnológicos y técnicos necesarios  para  evitar  que  se  produzca  un  accidente  o  para  mitigar 
sus efectos cuando sea irreversible. Algunas de las pruebas consisten en Impactos frontales, Laterales y Latigazos 
cervicales.

Se realizan 5 pruebas de seguridad (numeradas del 1 al 5) sobre cada uno de los autos de un grupo, el resultado de 
cada prueba es un número real entre 0,0 y 1,0 inclusive, donde un 1,0 indica que la prueba fue superada en un 100%.

Se desea realizar un algoritmo que, recibiendo como datos, los resultados de cada una de las 5 pruebas realizadas, 
informe por cada auto:
    ● El promedio de las 5 pruebas.
    ● La cantidad de pruebas con resultados inferiores a 0,5.

Para todos los autos:
    ● La cantidad de autos que obtienen en las 5 pruebas resultados superiores a 0,8.
    ● El mejor promedio de las 5 pruebas.

Se desconoce la cantidad de autos a evaluar, proponer un fin de datos adecuados.
'''
### DEFINO UNA FUNCION PARA LA CARGA DE LAS PRUEBAS ###

def cargadedatos(pruebas,resultados):
    sumaresultados=0
    contadorinferior=0

    for i in range(5):
        resultadoprueba=float(input("Ingrese los datos de la prueba "+ str(i+1) +" (entre 0.0 y 1.0)\n"))
        while resultadoprueba>(1) or resultadoprueba<0:
            resultadoprueba=float(input("Ingrese un valor válido\nIngrese los datos de la prueba "+ str(i+1) +" (entre 0.0 y 1.0)\n"))
        pruebas.append(resultadoprueba)
        
        if resultadoprueba<0.5:
            contadorinferior=contadorinferior+1
        
        sumaresultados=sumaresultados+resultadoprueba
    
    promedio=sumaresultados/5

    if promedio>=0.8:
        resultados[0]=resultados[0]+1
    
    if promedio>resultados[1]:
        resultados[1]=promedio
    
    print("\n### RESULTADOS VEHÍCULO ###\n\nEl promedio de las pruebas realizadas es de",round(promedio,3))
    print("El vehículo tuvo",contadorinferior,"Pruebas con resultados inferior a 0,5\n")

### COMIENZO DEL CÓDIGO ###
    
salir=False

while salir==False:
    pruebas=[]
    resultados=[0,0]

    cargadedatos(pruebas,resultados)

    opcion = str(input("¿Desea ingresar otro vehículo?\nSi / No\n"))
    opcion = opcion.upper()
    while opcion != "SI" and opcion != "NO":
        opcion = str(input("Ingrese una respuesta válida\n¿Desea ingresar otro vehículo?\nSi / No\n"))
        opcion = opcion.upper()
    print("")
    
    if opcion=="NO":
        salir = True

print("### RESULTADOS FINAL ###\n\nLa cantidad de autos que obtuvieron en las 5 pruebas resultados superiores a 0,8 fueron",resultados[0])
print("El mejor promedio de las 5 pruebas fue de", round(resultados[1],3),"\n")