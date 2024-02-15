import re
a = re.findall(r'\b.pl\b', "Historia przegiegu tranzakcji sklepu X: anna_kowalska@wp.pl zakupił(a) produkt od marcin.lewandowski@gmail.org jakiś czas potem sprzedając go dalej dodając marżę w wysokości 25% tak że produkt wylądował u johnDoe@sample.net. Następnie historia traci klarowność - w bazie mamy informację jedynie o adresie unknown-person@o2.pl")
print(len(a))
print(a)
with open("numery.txt", "r") as num:
    x = num.read()
    b = re.findall(r"(\d)\1\1", x)
    print(len(b))


c = re.findall("\+48", "Kontakt do naszych oddziałów: Warszawa +48 123 456 789, Berlin +49 234 567 890, Nowy Jork +1 987 654 3210, Londyn +44-843-243-3224")

print(len(c))