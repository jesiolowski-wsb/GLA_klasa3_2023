import re
tekst = "(...) Historia przegiegu tranzakcji sklepu X: anna_kowalska@wp.pl zakupił(a) produkt od marcin.lewandowski@gmail.org jakiś czas potem sprzedając go dalej dodając marżę w wysokości 25% tak że produkt wylądował u johnDoe@sample.net. Następnie historia traci klarowność - w bazie mamy informację jedynie o adresie unknown-person@o2.pl"
wynik = re.findall("[A-Za-z,-,_]+@[a-z0-9]+[.][a-z]+", tekst)
polskie = re.findall("[A-Za-z,-,_]+@[a-z0-9]+[.][p,l,P,L]+", tekst)

print(wynik)
print(polskie)
