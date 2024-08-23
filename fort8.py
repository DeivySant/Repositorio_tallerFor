lista = [1,2,3,5,4,6,7,8,9,10]

ascendente = True
for numero in range(len(lista)):
    if numero == 0: pass
    elif numero > 0 :
        if lista[numero] < lista[numero-1]:
            ascendente = False
if ascendente == True:
    print("La lista es ascendente")
else:
    print("La lista no es ascendente")
        

