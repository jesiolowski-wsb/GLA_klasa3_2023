import re

# 1
tekst = "(...) Historia przegiegu tranzakcji sklepu X: anna_kowalska@wp.pl zakupił(a) produkt od marcin.lewandowski@gmail.org jakiś czas potem sprzedając go dalej dodając marżę w wysokości 25% tak że produkt wylądował u johnDoe@sample.net. Następnie historia traci klarowność - w bazie mamy informację jedynie o adresie unknown-person@o2.pl"

reg = re.compile(r"[\w\d._-]+@[\w]+.[\w]+")
resoult = re.findall(reg, tekst)
print("Wszystkie adresy: " + ", ".join(resoult))

reg = re.compile(r"[\w\d._-]+@[\w]+\.pl")
resoult = re.findall(reg, tekst)
print("Wszystkie adresy z polski: " + ", ".join(resoult))
print(f"Jest ich {len(resoult)}")

# 2
families = []
rep_count = 0

fp = open("numery.txt")
c = fp.read()
c = [s for s in c.split('\n')]
correct_number = re.compile(r"^[0-9]{1,15}$")
repeating = re.compile(r"(\d)\1\1")
for a in c:
    ret = re.search(correct_number, a)
    if ret:
    	if ret.span()[1] not in families:
    		families.append(ret.span()[1])

    	ret = re.search(repeating, a)
    	if ret:
    		rep_count+=1

print(f"Liczba numerów z conajmniej trzema powtórkami: {rep_count}")
print(f"Rodziny: {families} ich liczba {len(families)}")

# 3
tekst = "Kontakt do naszych oddziałów: Warszawa +48 123 456 789, Berlin +49 234 567 890, Nowy Jork +1 987 654 3210, Londyn +44-843-243-3224"

reg = re.compile(r"(\+[0-9]+)([ -][0-9]+[ -][0-9]+[ -][0-9]+)")

def podmiana(match):
	return f"{match.group(1)} {'*'*len(match.group(2))}"

print(re.sub(reg, podmiana, tekst))
