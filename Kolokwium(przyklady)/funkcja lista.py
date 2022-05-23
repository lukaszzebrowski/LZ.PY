lista_num = [1, 2, 3, 4, 5]

def rownanie(lista):
    wynik = []
    for x in lista:
        wynik.append(4 * (x ** 2) - 5 * x - 4)
    return wynik

print(lista_num)
print(rownanie(lista_num))
