plik = open('kolokwium.txt', 'r', encoding="utf-8")

tekst = plik.read()
licznik_wielkich_liter = 0
licznik_liczb = 0
licznik_malych_liter = 0

for litera, in tekst[25:48]:
    if litera.isupper():
        licznik_wielkich_liter += 1

for litera, in tekst[:30:]:
    if litera.isdigit():
        licznik_liczb += 1

print(licznik_wielkich_liter)
print(licznik_liczb)
print(tekst.count('a', -20))

licznik_wielkich_liter2 = 0
licznik_malych_liter2 = 0

for litera, in tekst[28:55]:
    if litera.islower():
        licznik_malych_liter2 += 1

for litera, in tekst[64:83]:
    if litera.isupper():
        print(litera)
        licznik_wielkich_liter2 += 1
if licznik_wielkich_liter2 == 0:
    print("W podanym przedziale nie ma wielkich liter")
else:
    print(licznik_wielkich_liter2)

print(licznik_malych_liter2)