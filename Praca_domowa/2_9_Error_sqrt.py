#Napisz skrypt, który liczy pierwiastek z liczby podanej przez użytkownika
# jeśli użytkownik poda wartość ujemną to powinien być wyłapany błąd.
import math

print('Policz pierwiastek z liczby: ')

x = input('Podaj liczbę i zatwierdź przyciskiem ENTER: ')
x = int(x)

try:
    pierwiastek = math.sqrt(x)
    print(pierwiastek)
except ValueError:
    print('Błąd!! Wprowadzono liczbę ujemną!!')