plik = open('wynik.txt', 'w+', encoding="utf-8")

def szestastowy(a, b):
    wynik = a + b
    return hex(wynik)

while 1:
    try:
        a = int(input("Podaj pierwsza liczbe całkowitą: "))
        b = int(input("Podaj druga liczbe całkowitą: "))
        print(szestastowy(a, b))
        x = 'Wynik dodawania liczby %d i liczby %d w systemie szestastowym wynosi: %s'
        plik.write(x % (a, b, szestastowy(a, b)))
        break
    except ValueError:
        print('Nie wczytano liczby całkowitej!!!')
