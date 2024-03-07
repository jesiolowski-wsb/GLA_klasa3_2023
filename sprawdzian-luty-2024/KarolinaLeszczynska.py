import re

#sekcja A
tekst = "(...) Historia przegiegu tranzakcji sklepu X: anna_kowalska@wp.pl zakupił(a) produkt od marcin.lewandowski@gmail.org jakiś czas potem sprzedając go dalej dodając marżę w wysokości 25% tak że produkt wylądował u johnDoe@sample.net. Następnie historia traci klarowność - w bazie mamy informację jedynie o adresie unknown-person@o2.pl"
x = re.findall(r'\w+[@]+\w+\.+\w+|\w+\.+\w+[@]+\w+\.+\w+|\w+\-+\w+[@]+\w+\.+\w+', tekst)
print("maile:",x)

i=0
count=0
print("maile z polski:")
while i in range(len(x)):
    pl = re.search(r'\.pl', x[i])
    if pl != None:
        count+=1
        print(x[i])
    i+=1
print("liczba maili z polski:", count)

#sekcja B
plik = open("2024/testluty/numery.txt", "r")
numery = plik.read()
numery = numery.split('\n')
numery.pop()

j=0
numbercount = 0
while j in range(len(numery)):
    nrepeat = re.search(r"(\d)\1{2,}", numery[j])
    if nrepeat != None:
        numbercount +=1
    j+=1
print("liczba numerow z powtarzajacymi sie znakami:", numbercount)


#sekcja C
kontakt = "Kontakt do naszych oddziałów: Warszawa +48 123 456 789, Berlin +49 234 567 890, Nowy Jork +1 987 654 3210, Londyn +44-843-243-3224"

y = re.sub(r"-", r" ", kontakt)
y = re.sub(r"[0-9]{3,}", r"***", y)
print(y)
