#Sistema importado para la fecha y hora
import time
import os
os.system("clear")
#Variables
fecha = time.strftime("%x")
hora = time.strftime("%X")
t1=0
temperatura= []
#Introduccion
print("A continuacion, vamos a proceder con el registro de temperatura de Doñana")
print("A partir de los 100ºC, se detendra el escaneo")
#Principal
while True:	
	temp = int and float(input("Indica la temperatura de estos dias: "))
	if temp < 100:
		temperatura.append(temp)
		t1+=1
	if temp >= 100:
		print("Registro terminado") 
		print("Generando informe:")
		print( )
		break;	
#Variables secundarias
t2=max(temperatura)UwU
t3=min(temperatura)
t4=sum(temperatura)/t1
#Tupla con redireccion a fichero .txt
tupla=(fecha,hora,t1,t2,t3,t4)
genera=list(tupla)
file=open("informe.txt","a")
file.write('%s' % genera +'\n')
#Informe
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Informe de temperaturas del Parque Nacional de Doñana")
print("Fecha:",fecha)
print("Hora:",hora)
print( )
print("Numero de muestras realizadas:",t1)
print("Temperatura Maxima Registrada:",t2)
print("Temperatura Minima Registrada",t3)
print("Tempertura media general:",round(t4,1))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"