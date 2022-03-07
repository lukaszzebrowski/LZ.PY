#Napisz skrypt, który za pomocą pętli while pobiera 10 liczb,
# następnie dodaje do listy tylko parzyste liczby.


i = 1
parzyste = []

while i<=10:
    x = input('Podaj ' + str(i) + ' liczbę:')
    x = int(x)
    i += 1
    if x%2 == 0:
        parzyste.append(x)

if len(parzyste) == 0:
    print('Nie podałeś żadnej liczby parzystej.')
else:
    print(parzyste)
