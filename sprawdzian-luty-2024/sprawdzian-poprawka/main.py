import re
tekst ="Dokumentacja pojazdów: Ford Mustang VIN: AFAFP404XYF223456 należał do Steve'a, zanim został sprzedany z VIN: W0L0XCE075E033456. W naszej bazie znajdują się również pojazdy importowane takie jak Nissan z VIN: JN1TANR35U0001234."
a = re.findall(r'VIN[A-Z0-9: ]+', tekst)
print(a)
b = 0
c = re.findall(r'\b[A-E]', str(a))
print(c)
d = (re.search(str(c), tekst))
print(d)
print(str(tekst[41, 58]))