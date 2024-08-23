lista = [2,7,4,6,9,1,2,2,2,3,4,5,4,6,3,1,2,4,7]
elemento = 7
cantidad = 0
for numero in lista:
    if numero == elemento:
        cantidad +=1
print(f"el elemeto {elemento} aparece {cantidad} veces en la lista")