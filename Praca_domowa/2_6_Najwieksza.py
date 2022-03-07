# Wczytaj trzy liczby całkowite a,b,c i sprawdź, która z nich jest największa.
# W zależności od wyniku wyświetl odpowiedni komunikat.
# Użyj zagnieżdżeń.

print('Podaj 3 liczby, a my sprawdzimy, która jest największa.')

a = int(input('Podaj liczbe a: '))
b = int(input('Podaj liczbe b: '))
c = int(input('Podaj liczbe c: '))


if (a != b) & (a != c) & (b != c):
    if (a > b) & (a > c):
        print('Liczba a jest największa')
    elif (b > a) & (b > c):
        print('Liczba b jest największa')
    elif (c > b) & (c > a):
        print('Liczba c jest największa')
else:
    if (a == b) & (a > c):
        print('Liczby a i b są równe, i większe od c.')
    elif (a == c) & (a > b):
        print('Liczby a i c są równe, i większe od b.')
    elif (b == c) & (b > a):
        print('Liczby b i c są równe, i większe od a.')
    else:
        print('Liczby są równe')

