#lista=[] nawiasy kwadratowe, moga byc rozne typy, lancuchy, inna lista, int, float
#slownik={} nawiasy klamrowe, (klucz wartosc)<==jeden element, jest unikatowy
#słownik={1:10, 'klucz':'wartosc', 1:20}
#słownik['klucz']

# słownik={'key1':112244,'key2':335566} # utworzenie slownika
# print(słownik['key1'], słownik['key2']) # wyswietlenie calego słownika
# del słownik['key1'] #usuniecie key1
# print(słownik) #sprawdzenie czy usuniety
# słownik['key2'] = 'nowa wartosc' # nadanie nowej wartosci
# print(słownik) #sprawdzenie wartosci

# lista = [1, 2, 3, 4, 5, 6]
# print(lista)
# del lista[0]
# print(lista)
# lista[4] = 10
# print(lista)

lista = []
i = 0

while i<10:
    print('Podaj ' + str(i+1) + ' liczbe' )
    x = int(input())
    if x%2==0:
        lista.append(x)
    i+=1

print(lista)