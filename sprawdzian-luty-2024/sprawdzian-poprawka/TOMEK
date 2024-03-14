import re

txt = "Dokumentacja pojazdów: Ford Mustang VIN: AFAFP404XYF223456 należał do Steve'a, zanim został sprzedany z VIN: W0L0XCE075E033456. W naszej bazie znajdują się również pojazdy importowane takie jak Nissan z VIN: BN1TANR35U0001234."
print("ZADANIE 1 -----------------------")
x = re.findall("\w{17}", txt)
print(f"Wszystkie numery VIN: {x}")
y = re.findall("[A-E]\w{16}", txt)
print(f"Numery z Europy: {y}")
print()

print("ZADANIE 2 -----------------------")
txt = open("hasla.txt", "r")
hasla = txt.read()
zle = re.findall(r"[1234]{4}|(.)\1\1|[abcd]{4}|[zxcv]{4}",hasla)
#print(zle)
print(f"Liczba zlych hasel: {len(zle)}")
dobre=re.findall(r"[a-zA-Z0-9@$!%*?&]{8}", hasla)
#print(dobre)
print(f"Liczba dobrych hasel: {len(dobre)}")
print()

print("ZADANIE 3 -----------------------")
txt = "Kontakt do naszych pracowników: Jan Kowalski - jan.kowalski@example.com, Anna Nowak - anna.nowak@company.org. Prosimy o przesyłanie wszelkich zapytań na te adresy."
cenz = re.sub(r"[^@ ]+@","************@",txt)
print(cenz)
