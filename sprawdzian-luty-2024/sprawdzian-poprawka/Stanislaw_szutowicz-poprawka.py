import re
tekst = "Dokumentacja pojazdów: Ford Mustang VIN: AFAFP404XYF223456 należał do Steve'a, zanim został sprzedany z VIN: W0L0XCE075E033456. W naszej bazie znajdują się również pojazdy importowane takie jak Nissan z VIN: JN1TANR35U0001234."
a = re.findall(r'VIN[A-Z0-9: ]+', tekst)

checka = "A"
checkb = "B"
checkc = "C"
checkd = "D"
checke = "E"

print("The original list : " + str(a))

res = [idx for idx in a if idx[5].lower() == checka.lower() or idx[5].lower() == checkb.lower() or idx[5].lower() == checkc.lower() or idx[5].lower() == checkd.lower() or idx[5].lower() == checke.lower()]

print("The list of matching first letter : " + str(res))
