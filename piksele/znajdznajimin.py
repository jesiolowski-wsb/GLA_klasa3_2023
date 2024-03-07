liczbamaks = 0
liczbamin = 0
with open('dane1.txt') as dane:
    dane = dane.read()
    tabela = dane.split()
    liczbamin = tabela[0]
    liczbamin = int(liczbamin)
    for x in tabela:
        x = int(x)
        if x > liczbamaks:
            liczbamaks = x
        elif x < liczbamin:
            liczbamin = x
print(f"maks to {liczbamaks}, a min to {liczbamin}")

