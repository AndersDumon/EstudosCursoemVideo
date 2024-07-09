def ordem(lista):
    n =len(lista)
    for i in range(n):
        trocou = False
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j],lista[j+1] = lista[j+1], lista[j]
                trocou = True
        if not trocou:
            break
    return lista


lista = [1, 5, 6, 8, 7, 41, 2, 3, 96, 5, 8, 6]
print(lista)
listaordenada = ordem(lista)
print(listaordenada)
