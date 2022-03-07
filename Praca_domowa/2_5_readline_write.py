#Napisz skrypt gdzie pobierzesz trzy liczby całkowite, gdzie wykonasz obliczenia: a^b + c.
#Użyj instrukcji readline() i write()).

import sys as system

print("Program liczy a^b+c\n")

system.stdout.write("Wprowadź a: ")
a = system.stdin.readline()

system.stdout.write("Wprowadź b: ")
b = system.stdin.readline()

system.stdout.write("Wprowadź c: ")
c = system.stdin.readline()

wynik = int(a)**int(b)+int(c)

system.stdout.write(str(wynik))








