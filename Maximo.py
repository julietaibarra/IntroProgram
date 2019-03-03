def maximo(lista):
    maxi=lista[0]#maxi toma el valor del indice 0.
    for i in range(len(lista)):#Se recorre la lista.
        if lista[i]>maxi:#se compara el valor del indice i con el del indice 0.
            maxi=lista[i] #si el valor del incice i es mayor toma el lugar de maxi.
            #indice=i
    return maxi
lista=[1,5,9,56,29,50]

print(maximo(lista))



#for i in range(len(lista)):
        #lista_cantidad.append(len(i))
def maximoIndice(lista):
    maxi=lista[0]
    for i in range(len(lista)):
        if lista[i]>maxi:
            maxi=lista[i]
            indice=i
    return indice
lista=[977,465,9887,456,3,123,7888]
print(maximoIndice(lista))
