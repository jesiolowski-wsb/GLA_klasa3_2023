plik = open("2024/piksele/dane.txt", "r")
tekst = plik.read()
tekst = tekst.replace('\n', ' ')
tekst = tekst.split(' ')
tekst.pop()
tekst = list(map(int, tekst))

print("max", max(tekst))
print("min", min(tekst), "\n")
