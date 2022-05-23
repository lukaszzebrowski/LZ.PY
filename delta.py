import math

def row_kwadratowe(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("brak pierwiastków")
        return -1
    elif delta == 0:
        print("jeden pierwiastek")
        x = (-b) / (2 * a)
        return x
    else:
        print("dwa pierwiastki")
        x1 = round((-b - math.sqrt(delta)) / (2 * a), 2)
        x2 = round((-b + math.sqrt(delta)) / (2 * a), 2)
        return x1, x2

x = (int(input("Podaj liczbe a: \n")))
y = (int(input("Podaj liczbe b: \n")))
z = (int(input("Podaj liczbe c: \n")))

print(row_kwadratowe(x, y, z))