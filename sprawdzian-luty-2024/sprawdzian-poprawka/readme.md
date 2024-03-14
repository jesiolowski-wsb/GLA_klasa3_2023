# Wyrażenia regularne
Do rozwiązań użyj wyrażeń regularnych ([dokumentacja W3Schools](https://www.w3schools.com/python/python_regex.asp), [re docs](https://docs.python.org/3/library/re.html), [online regex tester](https://regex101.com/) [polski tutorial](https://ggoralski.gitlab.io/python-wprowadzenie/czesc_ii/2_01-regex/))

### SEKCJA A: zwracanie listy wyników
Napisz program który używa wyrażeń regularnych do:
- wyszukiwania i wyświetlania wszystkich numerów identyfikacyjnych pojazdów (VIN) zawartych w danym tekście przy założeniu ze numer VIN to ciąg składający się z 17 znaków (cyfry i litery)
- policzenia, ile z tych numerów VIN odpowiada pojazdom wyprodukowanym w Europie (zakładając, że europejskie VINy zaczynają się od liter od A do E).
- pokazania tych numerów VIN.

```
tekst ="Dokumentacja pojazdów: Ford Mustang VIN: AFAFP404XYF223456 należał do Steve'a, zanim został sprzedany z VIN: W0L0XCE075E033456. W naszej bazie znajdują się również pojazdy importowane takie jak Nissan z VIN: JN1TANR35U0001234."
```

### SEKCJA B: wyszukiwanie wzorca (wynik: true / false)
W pliku hasła.txt zapisane są różne hasła użytkowników. Niektóre z nich są słabe, ponieważ składają się z prostych powtórzeń lub sekwencji (np. "aaa", "1234", "abcd").

```
zaq1@WSX
123abcABC!
aaaBBBccc

```

Zadania do wykonania:
1. Podaj liczbę haseł, które są uznawane za słabe ze względu na występowanie trzech takich samych znaków obok siebie (podpowiedź: dowolny znak to (.) ) **lub** prostych sekwencji cyfr/ liter (takich jak 1234, abcd lub zxcv).
2. Podaj liczbę haseł, które zawierają znaki z zakresu: mala lub wielka litera, dowolna cyfra, znaki specjalne z zakresu **@$!%*?&** i gdzie ciąg ma minimum 8 znaków.

### SEKCJA C: zmiana treści wg. wzorca
Napisz program, który używa funkcji sub z modułu re, aby zanonimizować adresy email w podanym tekście. Program powinien zastąpić część lokalną adresu email (wszystko przed znakiem "@") gwiazdkami (*), zachowując domenę i tld (top-level domain).#### Wymagania:

```
"Kontakt do naszych pracowników: Jan Kowalski - jan.kowalski@example.com, Anna Nowak - anna.nowak@company.org. Prosimy o przesyłanie wszelkich zapytań na te adresy."
```
powinien w wyniku działania na ekranie wyświetlić
```
"Kontakt do naszych pracowników: Jan Kowalski - ************@example.com, Anna Nowak - ***********@company.org. Prosimy o przesyłanie wszelkich zapytań na te adresy."
```

#### Podpowiedź
Frazy /  klucze do wyszukania w dokumentacji to:
- Raw String Notation
- findall, search, sub
- \d
- {}
- []
- ?

### Gotowe odpowiedzi wyśllij na githuba umieszczając w bieżącym folderze (tj. sprawdzian-luty-2024) w pliku / plikach ze swoim imieniem i nazwiskiem w nazwie
