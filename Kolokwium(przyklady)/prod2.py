import math

def produkcja(a, b, c):
        print("Na wyprodukowanie %d szt towaru potrzeba %d dni" % (a, math.ceil(a / (b * c))))

while 1:
    try:
        a = int(input("Podaj liczbę towaru jaką chcesz wyprodukować: "))
        b = int(input("Podaj jaką liczbę towaru można wyprodukować w ciągu jednej godziny: "))
        c = int(input("Podaj liczbę godzin w dobie: "))

        if c >= 13:
            print("Nie można pracować tyle godzin w jednej dobie!!!!")
            c = int(input("Podaj ponownie liczbę godzin w dobie: "))
        print(produkcja(a, b, c))
        break
    except ValueError:
        print("Podaj liczby całkowite!!!!!!")