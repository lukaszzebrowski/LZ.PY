#Stwórz słownik skrótów powszechnie używanych w gazetach lub artykułach internetowych.
# Jako klucz przyjmij skrót danego słowa, wartość to rozwinięcie tego skrótu.

slownik = {'tj': 'to jest', 'str': 'strona', 'tzw': 'tak zwany', 'zob': 'zobacz'}

print(slownik['tj'])
print(slownik.keys())
print(slownik.values())

slownik['np'] = 'na przykład'

print(slownik['np'])
print(slownik.keys())
print(slownik.values())

