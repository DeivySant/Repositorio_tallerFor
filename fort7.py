lista = [2,7,4,6,9,1,2,2,2,3,4,5,4,6,3,1,2,4,7]
listan = []

for numero in lista :
    if numero in listan :
        break
    else:
        listan.append(numero)
print(f"La nueva lista sin repetidos es : {listan}")
