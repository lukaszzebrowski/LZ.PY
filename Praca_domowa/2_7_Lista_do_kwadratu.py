# Napisz skrypt, gdzie stworzysz listę składającą się z liczb typu int i float.
# Następnie za pomocą użycia pętli for podnieś każdą liczbę do kwadratu.

lista = [5, 3.5, 6, 2.6, 1, 2, 3.6]
lista2 = []
for licznik in lista:
    lista2.append(licznik**2)

print('Lista:\n' + str(lista))
print('Lista podniesiona do kwadratu:\n' + str(lista2))


