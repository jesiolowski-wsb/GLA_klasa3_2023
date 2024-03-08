import re

# 1
tekst = "(...) Historia przegiegu tranzakcji sklepu X: anna_kowalska@wp.pl zakupił(a) produkt od marcin.lewandowski@gmail.org jakiś czas potem sprzedając go dalej dodając marżę w wysokości 25% tak że produkt wylądował u johnDoe@sample.net. Następnie historia traci klarowność - w bazie mamy informację jedynie o adresie unknown-person@o2.pl"

adresy_email = re.findall(r'[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+', tekst)
adresy_email_pl = [email for email in adresy_email if email.endswith('.pl')]

print("Znalezione adresy e-mail:", adresy_email)
print("\nLiczba adresów e-mail z Polski:", len(adresy_email_pl))
print("Adresy e-mail z Polski:", adresy_email_pl)

# 2
def czy_powtarzajace_cyfry(numer):
    return bool(re.search(r"(\d)\1\1", numer))


def liczba_numerow_z_powtorzeniami(nazwa_pliku):
    liczba = 0
    with open(nazwa_pliku, "r") as plik:
        for linia in plik:
            numer = linia.strip()
            if czy_powtarzajace_cyfry(numer):
                liczba += 1
    return liczba


print("Odp. 1: ", liczba_numerow_z_powtorzeniami("numery.txt"))


def liczba_rodzin_numerow(nazwa_pliku):
    dlugosci = set()
    with open(nazwa_pliku, "r") as plik:
        for linia in plik:
            numer = linia.strip()
            dlugosci.add(len(numer))
    return len(dlugosci)


print("Odp. 2: ", liczba_rodzin_numerow("numery.txt"))

# 3
tekst = "Kontakt do naszych oddziałów: Warszawa +48 123 456 789, Berlin +49 234 567 890, Nowy Jork +1 987 654 3210, Londyn +44-843-243-3224"

# Wyrażenie regularne do identyfikacji numerów telefonów
wzor_numeru = r'(\+\d{1,3})[\s-]?\d{1,3}[\s-]?\d{3}[\s-]?\d{3,4}'

# Funkcja zastępująca numery telefonów
def anonimizuj_numer(match):
    kod_kierunkowy = match.group(1)  # Kod kierunkowy
    dlugosc_num = len(match.group(0).replace(" ", "").replace("-", "")) - len(kod_kierunkowy)
    return kod_kierunkowy + " " + "*" * dlugosc_num

anonimizowany_tekst = re.sub(wzor_numeru, anonimizuj_numer, tekst)

print(anonimizowany_tekst)
