with open('dane.txt', 'r') as file:
    colours = file.read()
    colours_split_n = colours.split("\n")
    colours_split_n_str = ' '.join(colours_split_n)
    colours_split = colours_split_n_str.split(" ")

for i in range(len(colours_split)):
    colours_split[i] = int(colours_split[i])

max_colours = max(colours_split)
print(max_colours)

min_colours = min(colours_split)
print(min_colours)
