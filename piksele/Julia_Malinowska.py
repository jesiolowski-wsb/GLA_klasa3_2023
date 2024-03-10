with open("dane.txt", "r") as plik:
    lista = plik.read().replace("\n", " ").split(" ")
    N = 0
    n = 256
    for x in lista:
        if x != '':
            if N < int(x):
                N = int(x)
            if n > int(x):
                n = int(x)


print(N, n)
