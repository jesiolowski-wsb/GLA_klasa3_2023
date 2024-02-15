# SEKCJA A: zwracanie listy wyników
# Napisz program który używa wyrażeń regularnych do:
# - wyszukiwania i wyświetlania wszystkich adresów e-mail zawartych w danym tekście.
# - policzeniu ile ze znalezionych adresów pochodzi z serwisów w Polsce
# - pokazaniu tych adresów

import re
tekst = "(...) Historia przegiegu tranzakcji sklepu X: anna_kowalska@wp.pl zakupił(a) produkt od marcin.lewandowski@gmail.org jakiś czas potem sprzedając go dalej dodając marżę w wysokości 25% tak że produkt wylądował u johnDoe@sample.net. Następnie historia traci klarowność - w bazie mamy informację jedynie o adresie unknown-person@o2.pl"
mail = re.findall(r'\w+@+\w+\.+\w+|\w+\.\w+@+\w+\.+\w+|\w+-+\w+@+\w+\.+\w+',tekst)
print(f"maile: {mail}")

polski_mail = re.findall(r'\w+@+\w+\.+pl|\w+-+\w+@+\w+\.+pl', tekst)

print(f"ilosc numerow z Polski: {len(polski_mail)}")

print(f"polskie maile: {polski_mail}")


# SEKCJA B
with open('numery.txt', "r") as file:
    numbers = file.read()
    numbers_split = numbers.split("\n")
    numbers_str = ' '.join(numbers_split)
i = 0
three_digits_count = 0
while i in range(0,1000):
    three_digits = re.search(r'(\d)\1{2,}', numbers_split[i])
    if three_digits != None:
        three_digits_count += 1
    i += 1
print(f"numery o co najmniej trzech takich samych cyfrach obok siebie: {three_digits_count}")

# SEKCJA C
telefony = "Kontakt do naszych oddziałów: Warszawa +48 123 456 789, Berlin +49 234 567 890, Nowy Jork +1 987 654 3210, Londyn +44-843-243-3224"
kontakt = re.sub(r"-", " ", telefony)
kontakt = re.sub(r"(\d){3,}", r"***", kontakt)
print(kontakt)