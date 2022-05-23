import math

def rownanie(x, y, z):
    wynik = math.sqrt(x) + math.sin(y) + z ** 2
    return wynik

while 1:
    try:
        a = int(input("Podaj liczbę a: "))

        while a < 0:
            print("Nie można policzyć pierwiastka stopnia parzystego z liczby ujemnej")
            a = int(input("Podaj ponownie liczbę a: "))

        b = int(input("Podaj liczbę b: "))
        c = int(input("Podaj liczbę c: "))

        print(rownanie(a, b, c))
        break

    except ValueError:
        print("Wszystkie liczby muszą być liczbami całkowitymi dodatnimi!!!!")
