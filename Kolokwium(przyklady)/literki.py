literki_plik = open("literki.txt", "w+", encoding="utf-8")

def literki(tekst):
    licz_male = 0
    licz_duze = 0
    licz_num =  0
    for znak in tekst:
        if znak.isupper():
            licz_duze += 1
        elif znak.islower():
            licz_male += 1
        elif znak.isdigit():
            licz_num += 1
    tekst_po = "W wczytanym ciągu znakowym jest: %d dużych liter, %d małych liter, %d liczb"
    print(tekst_po % (licz_duze, licz_male, licz_num))
    literki_plik.write(tekst_po % (licz_duze, licz_male, licz_num))



tekst = input("Wczytaj dowolny ciąg znakowy: ")

if len(tekst) == 0:
    print("Nie wczytano nappisu, podaj napis jeszcze raz!!!!")
    tekst = input("Wczytaj dowolny ciąg znakowy: ")

literki(tekst)


