# Wyrażenia regularne
Do rozwiązań użyj wyrażeń regularnych ([dokumentacja W3Schools](https://www.w3schools.com/python/python_regex.asp), [re docs](https://docs.python.org/3/library/re.html), [online regex tester](https://regex101.com/) )

### SEKCJA A: zwracanie listy wyników
Napisz program który używa wyrażeń regularnych do:
- wyszukiwania i wyświetlania wszystkich adresów e-mail zawartych w danym tekście.
- policzeniu ile ze znalezionych adresów pochodzi z serwisów w Polsce
- pokazaniu tych adresów

```
tekst = "(...) Historia przegiegu tranzakcji sklepu X: anna_kowalska@wp.pl zakupił(a) produkt od marcin.lewandowski@gmail.org jakiś czas potem sprzedając go dalej dodając marżę w wysokości 25% tak że produkt wylądował u johnDoe@sample.net. Następnie historia traci klarowność - w bazie mamy informację jedynie o adresie unknown-person@o2.pl"
```

### SEKCJA B: wyszukiwanie wzorca (wynik: true / false)
W pliku `numery.txt` zapisanych jest 1000 numerów telefonów (jeden numer na wiersz). Numery telefonów są zapisane bez żadnych dodatkowych znaków (tylko cyfry). Maksymalna długość numeru telefonicznego to 15 cyfr. Przykładowe numery w tym pliku to:

```
8532920888
6105000455181
646454074
```

Zadania do wykonania:
1. Podaj liczbę numerów telefonów, które zawierają co najmniej trzy te same cyfry obok siebie (np. 111, 222 itd.)
2. Wszystkie numery telefonów o tej samej liczbie cyfr tworzą jedną "rodzinę". Podaj liczbę niepustych rodzin numerów telefonów

### SEKCJA C: zmiana treści wg. wzorca
Napisz program który używa funkcji sub z modułu re aby zanonimizować numery telefonów w podanym tekście. Program powinien zachować numery kierunkowe krajów (np. +48 dla Polski), ale zastąpić resztę numeru telefonu gwiazdkami * tak, aby ukryć rzeczywiste numery telefonów.

#### Wymagania:

Program powinien identyfikować różne formaty numerów telefonów - w tym międzynarodowe numery zaczynające się od + oraz potencjalne spacje, myślniki i nawiasy w numerach.
- Każdy numer telefonu powinien zostać zanonimizowany do postaci: kod kierunkowy + " *****", gdzie liczba gwiazdek odpowiada długości oryginalnego numeru bez kodu kierunkowego.
- Tekst na wejściu może zawierać różne numery telefonów z różnych krajów.

```
tekst = "Kontakt do naszych oddziałów: Warszawa +48 123 456 789, Berlin +49 234 567 890, Nowy Jork +1 987 654 3210, UK +44-843-243-3224"
```
powinien w wyniku działania na ekranie wyświetlić
```
Kontakt do naszych oddziałów: Warszawa +48 *********, Berlin +49 *********, Nowy Jork +1 **********, UK +44 **********
```
