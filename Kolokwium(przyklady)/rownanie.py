def rownanie(x, y ,z):
    wynik = (a + b) ** 3 * c
    return wynik

while 1:
    try:
        a = int(input("Podaj pierwsza liczbe całkowitą: "))
        b = int(input("Podaj druga liczbe całkowitą: "))
        c = int(input("Podaj trzecia liczbe całkowitą: "))

        print(rownanie(a, b, c))
        break
    except ValueError:
        print("Błąd, wprowadć liczby jeszcze raz!!!")