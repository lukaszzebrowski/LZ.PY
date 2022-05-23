import math

def procenty(a, b):
        procent = (b / a) * 100
        return round(procent, 1)

while 1:
    try:
        a = int(input("Podaj maksymalna liczbę punktów: "))
        b = int(input("Podaj zdobytą liczbę punktów: "))

        while b < 0 or a < 0 or a <= b:
            print("Podano błedne liczby!!!!")
            a = int(input("Podaj maksymalna liczbę punktów: "))
            b = int(input("Podaj zdobytą liczbę punktów: "))

        print(b, "pkt stanowi " + str(procenty(a, b)) + "% wszystkich punktów")
        break
    except ValueError:
        print("Podaj liczby całkowite!!!!!!")