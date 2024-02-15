# Wyrażenia regularne

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
1. Podaj liczbę numerów telefonów, które zawierają co najmniej trzy te same cyfry obok siebie (np. 111, 222 itd.). Do finalnego rozwiązania użyj wyrażeń regularnych ([dokumentacja W3Schools](https://www.w3schools.com/python/python_regex.asp), [online regex tester](https://regex101.com/) )
2. Wszystkie numery telefonów o tej samej liczbie cyfr tworzą jedną "rodzinę". Podaj liczbę niepustych rodzin numerów telefonów.

