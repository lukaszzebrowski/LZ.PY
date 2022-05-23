# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import math

a = math.e + 36 / 7 ** 3 + (2 / 5 + math.pi) ** (1 / 3)
print(a)

string = """(5pkt.) Napisz skrypt, w którym utworzysz zmienną typu łańcucha znakowego.
        Twoim zadaniem jest sprawdzenie ile w łańcuch znakowym jest małych,
        ile dużych liter a także ile liczb. Wyniki wyświetl na ekranie."""

duze = 0
male = 0
liczba = 0

for znak in string:
    if znak.isupper():
        duze += 1
    elif znak.islower():
        male +=1
    elif znak.isdigit():
        liczba += 1

print("W łańcuchu jest", duze, "duzych liter,", male, "małych liter", liczba, "liczb.")

while 1:
    try:
        dziesietna = int(input("Podaj liczbe w systemie dziesiętnym: "))
        print(hex(dziesietna))
        break
    except ValueError:
        print("Błąd!!!")

def przemnozenie(lista, a):
    wynik= []
    for i in lista:
        wynik.append(i * a)
    return wynik

list = [2, 4, 5, 1, 2, 7, 9]

a = int(input("Podaj wartość a: "))

print(przemnozenie(list, a))






