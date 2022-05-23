lista = [3, 5, 1, 6, 7, 3, 2, 7, 7, 7, 7]

def najwieksze(lista):
    ile_najwiekszych = lista.count(max(lista))
    lista2 = []
    i = 0
    for j in lista:
        if j != max(lista):
            lista2.append(j)
    return lista2

print(najwieksze(lista))

