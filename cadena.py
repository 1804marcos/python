import time
import os
fecha = time.strftime("%x")
hora = time.strftime("%X")
covid="ccucgggca"
cadpac=int(input("Dime tu numero de paciente:"))

print("INFORME VIRUS COVID")
print("fecha:",fecha)
print("hora:",hora)

print("numero paciente",cadpac)
if cadpac == covid:
    resul=print("tienes covid andy")
    pon="positivo"
else:
    resul=print("limpio como el culo de un bb")
    pon="negativo"

tupla=(fecha,hora,cadpac,pon)
print(tupla)