import os,sys
os.system("cls")
import random
while True:
    a1 = int(input("Ingrese un numero entre 2 y 5: "))
    if 1<a1<6:
        break 
matriz =[]
pares=0
for i in range(a1):
    aletorio = random.randint(1,100)
    matriz.append(aletorio)
    print(aletorio)
    if aletorio % 2 == 0:
        pares = pares+1
print("Arreglo:",matriz)
print("Cantidad de pares: ",pares)