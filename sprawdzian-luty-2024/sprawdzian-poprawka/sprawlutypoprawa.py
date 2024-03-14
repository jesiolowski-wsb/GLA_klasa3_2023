import re

tekst ="Dokumentacja pojazdów: Ford Mustang VIN: AFAFP404XYF223456 należał do Steve'a, zanim został sprzedany z VIN: W0L0XCE075E033456. W naszej bazie znajdują się również pojazdy importowane takie jak Nissan z VIN: JN1TANR35U0001234."

vinyle = re.findall(r'\S{17}', tekst)
eurovinyle = re.findall(r'\b(?=[A-E])\S{17}', tekst)

liczbaeuro = len(eurovinyle)

print(f"europejskich Vinow jest {liczbaeuro}")
print(f"euro Viny to {eurovinyle}")

def czypowtarza(numer):
    return bool(re.search(r"(\w)\1\1",numer))
def czycos(numer):
    return bool(re.search(r"1234", numer))
def czycoss(numer):
    return bool(re.search(r"zxcv", numer))

liczba = 0
with open("hasla.txt", "r") as plik:
    for linia in plik:
        numer = linia.strip()
        if czypowtarza(numer):
            liczba += 1
        if czycos(numer):
            liczba +=1
        if czycoss(numer):
            liczba +=1

print(f"slabych hasel jest {liczba}")

