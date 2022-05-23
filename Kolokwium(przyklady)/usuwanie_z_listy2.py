lista = [1, 3, 5, 1, 6, 7, 3, 1, 2, 7, 7, 7, 7, 1]

def najwieksze(lista):
    ile_najwiekszych = lista.count(min(lista))
    lista2 = []
    i = 0
    for j in lista:
        if j != min(lista):
            lista2.append(j)
    return lista2

print(najwieksze(lista))

