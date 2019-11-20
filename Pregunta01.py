import os
os.system("cls")
def contarletra(texto,letra):
    contador = 0
    for i in texto:
        if i == letra:
            contador = contador +1
    print(contador) 

palabra = input("Ingrese una palabra:")
buscador = input("letra que desea buscar:")
contarletra(palabra,buscador)
