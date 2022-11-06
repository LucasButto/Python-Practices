'''
Ejercicio 6 – Temperaturas diarias

A lo largo de un día se ha registrado la temperatura de un determinado ambiente 
a intervalos de media hora comenzando a las 00:00 hs. Se desea conocer:
    ● La cantidad de veces que la temperatura superó los 25°C.
    ● La temperatura máxima y la mínima, con la hora correspondiente.
'''
horas=0
minutos=0
contador=0

while horas!=24:

    print(horas,":",minutos,"hs")
    
    temp= float(input("Ingrese la temperatura: \n"))
    while temp<-89.2 or temp>56.7:
        temp= float(input("Ingrese una temperatura válida \nIngrese la temperatura:\n"))
    
    if horas==0 and minutos==0:
        tempmayor=temp
        horamayor=horas
        minutosmayor=minutos

        tempmenor=temp
        horamenor=horas
        minutosmenor=minutos
    
    if temp>tempmayor:
        tempmayor=temp
        horamayor=horas
        minutosmayor=minutos
    
    if temp<tempmenor:
        tempmenor=temp
        horamenor=horas
        minutosmenor=minutos
    
    if temp>25:
        contador=contador+1
    
    if minutos==0:
        minutos=minutos+30
    else:
        horas=horas+1
        minutos=minutos-30
    
print("Durante el día, la temperatura superó los 25°C",contador,"veces")
print("La temperatura mínima del día fue de",tempmenor,"°C a las",horamenor,":",minutosmenor,"hs")
print("La temperatura máxima del día fue de",tempmayor,"°C a las",horamayor,":",minutosmayor,"hs")
    
    