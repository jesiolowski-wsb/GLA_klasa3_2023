#1

import re
tekst ="Dokumentacja pojazdów: Ford Mustang VIN: AFAFP404XYF223456 należał do Steve'a, zanim został sprzedany z VIN: W0L0XCE075E033456. W naszej bazie znajdują się również pojazdy importowane takie jak Nissan z VIN: JN1TANR35U0001234."
wzor=re.compile(r'\b[\w]{17}\b')
wvin=wzor.findall(tekst)
euvin=[VIN for VIN in wvin if VIN.startswith('A') or VIN.startswith('B') or VIN.startswith('C') or VIN.startswith('D') or VIN.startswith('E')]
print(wvin)
print(euvin)

#3
def zakod(poczatek):
    dlugosc=len(poczatek.replace('@', ''))
    return '*' * dlugosc + '@'
tekst = "Kontakt do naszych pracowników: Jan Kowalski - jan.kowalski@example.com, Anna Nowak - anna.nowak@company.org. Prosimy o przesyłanie wszelkich zapytań na te adresy.")
wzor=r'\b[a-zA-Z]+\.[a-zA-Z]+@'
kroptekst=re.sub(wzor,zakod,tekst)
print(kroptekst)
