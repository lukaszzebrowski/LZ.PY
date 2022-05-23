lista = [1, 3, 5, 1, 6, 7, 3, 1, 2, 7, 7, 7, 7, 1]

def najmnieksze(lista):
    print(min(lista))
    return lista.count(min(lista))

def najwieksze(lista):
    print(max(lista))
    return lista.count(max(lista))

print(najmnieksze(lista))
print(najwieksze(lista))