#if warunek instrukcja lub blok instrukcji dla warunek 1
#elif waurek 2 instruckja lb blok instrukcji
#elif warunek n: instrukcja lub blok instrukcji
#else: instrukcja gdy warunki niespelnione

a=input('Podaj liczbe a:')
b=input('Podaj liczbe b:')
c=input('Podaj liczbe c:')
d=input('Podaj liczbe d:')
#
# if a>b:
#     print('Liczba a jest wieksza od b')
# elif a<b:
#     print('Liczba a jest mniejsza od b')
# else:
#     print('Liczby sa równe')

a=int(a)
b=int(b)
c=int(c)
d=int(d)

if (a>b) & (c>d):
    print('Liczba a jest wieksza od liczby b i liczba c jest wieksza od liczby d')
else:
    print('Liczba a jest mniejsza niz liczba b lub liczba c jest mniejsza od liczby d')



