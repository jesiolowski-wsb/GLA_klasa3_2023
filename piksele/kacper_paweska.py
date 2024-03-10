with open('dane.txt', 'r') as file:
    data = [list(map(int, line.split())) for line in file]

x = max(max(row) for row in data)
y = min(min(row) for row in data)


with open('wyniki6.txt', 'a') as z:
    z.write("6.1\n")
    z.write(f"{x} (najjasniejszy) i {y} (najciemniejszy)\n")
