'''
Ejercicio 1 – Socios Clubes

Luego de recabar datos de los socios en cada uno de los 17 clubes más importantes de la ciudad
se quiere determinar, para cada una de ellos, entre los censados mayores de edad (tienen 18 años o más)
quienes son más numerosos, los que son temporales (código 1) o los que son permanentes (código 2).
Para resolver esto se dispone, por cada socio de cada uno de los clubes, su código de asociado 
(1 para temporal, 2 para permanente) y la edad. Ver ejemplo.
Un código de asociado 0 (cero) indica que no hay más datos de ese club.
Valide el código entre 0, 1 y 2; no permita otros valores.
Validar la edad que no sea negativa y reconfirme si es mayor a 100.

'''

# Datos a ingresar codigo, edad
# for i in range(1,18):     para manejar los clubes
# while (codigo != 0):      while anidado dentro de for
# validar el codigo 0,1,2
# Chequear la edad la validez de la edad con un while para verificar no sea < 0 y > 100
# Reconfirme si es > 100
# Contadores para tipos de asociados


########   Programa Principal   #########



for i in range(1,18):
    
    salir=False
    j=1
    temporal=0
    permanente=0
    
    print("")
    print("Club ", i,":")
    
    
    while salir==False:
        print("")
        print("Ingrese el código de la persona ", j)
        print("1 para temporal")
        print("2 para permanente")
        print("0 (cero) no hay más datos del club ", i)
        codigo = int(input())
        
        while codigo!=0 and codigo!=1 and codigo!=2: #While codigo not in codigos     codigos = {0, 1, 2}
            print("Ingrese un código válido")
            print("Ingrese el código de la persona ", j)
            print("1 para temporal")
            print("2 para permanente")
            print("0 (cero) no hay más datos del club ", i)
            codigo = int(input())

        if codigo!=0:
            print("Ingrese la edad de la persona ", j)
            edad = int(input())

            while edad<=0: #while edad not in range(150)
                print("Ingrese una edad válida")
                print("Ingrese la edad de la persona ", j)
                edad = int(input())

            if edad>=100:   
                print("Ingresó una edad mayor a 100 años")
                print("Su edad de ", edad, "es correcta?")
                print("1 - Si   2 - No") 

                respuesta=int(input()) #respuesta=respuesta.upper() pone lo que escribio en mayusculas
                                       #respuesta=respuesta.lower() pone lo que escribio en minusculas
                
                while respuesta!=1 and respuesta!=2:
                    print("Ingrese una respuesta válida")
                    print("Su edad de ", edad, "es correcta?")
                    print("1 - Si   2 - No")
                    respuesta = int(input())
                
                if respuesta==1:
                    if (codigo == 1):
                        temporal=temporal+1
                        j=j+1
                    else:
                        permanente=permanente+1
                        j=j+1

            else: 
                if edad>=18 and edad<100:
                    if (codigo == 1):
                        temporal=temporal+1
                        j=j+1
                    else:
                        permanente=permanente+1
                        j=j+1
            
        else:
            salir=True
            
                
    print("")
    if temporal==0 and permanente==0:
        print("No hubo socios mayores a 18 años en el club", i)
    else:
        if temporal==permanente:
            print("Entre los censados del club", i, "mayores de edad hay la misma cantidad de socios temporales y permanente con una cantidad de", temporal, "socios en cada grupo")
        else:
            if temporal>permanente:
                print("Entre los censados del club", i, "mayores de edad quienes son más numerosos son los temporales con ", temporal, "socios")
            else:
                print("Entre los censados del club", i, "mayores de edad quienes son más numerosos son los permanentes con ", permanente, "socios")        
