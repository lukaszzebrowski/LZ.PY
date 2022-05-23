#obsluga bledow za pomoca skladni try except
#try
#-blok instruckji
#except nazwa_bledu
#-blok instrukcji po napotkaniu bledu

liczba1=input('Podaj pierwszą liczbę: ')
liczba2=input('Podaj drugą liczbę: ')

try:
    liczba1=int(liczba1)
    liczba2=int(liczba2)
    wynik=liczba1/liczba2
    print('Winik działania = '+str(wynik))
except ZeroDivisionError:
    print('Nie można dzielić przez 0!!!')
except ValueError:
    print('Nie wczytano liczby całkowitej!!!')