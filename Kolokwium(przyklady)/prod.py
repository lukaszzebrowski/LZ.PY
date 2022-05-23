def produkcja(a, b, c):
    if a <= (b * c):
        print(str(a) + " szt towaru można wyprodukować w jednym dniu pracy")
    else:
        print(str(a) + " szt towaru nie można wyprodukować w jednym dniu pracy")

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