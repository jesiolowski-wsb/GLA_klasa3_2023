gameMatrix = [
    [False, True,  True,  False, False, False],
    [True,  True,  True,  False, False, False],
    [True,  True,  True,  True,  True,  True],
    [False, True,  True,  False, True,  True],
    [False, True,  True,  True,  False, True],
    [False, False, False, False, False, False],
]

def can_travel_to(gameMatrix, currentx, currenty, x, y):
    a = 0
    while a < len(gameMatrix):
        b = 0
        row = ""
        while b < len(gameMatrix[0]):
            if a == currentx and b == currenty:
                row += "B "
            elif a == x and b == y:
                row += "M "
            else:
                if gameMatrix[a][b] == True:
                    row += ". "
                else:
                    row += "x "
            b+=1
        print(row)
        a+=1
    i = 0
    if ((x or y) > 5) or ((x or y) < 0):
        return False
    if gameMatrix[x][y] == False:
        return False
    if abs(y-currenty) > 1:
        return False
    if currentx-x in range(-1,3):
        while i < abs(currentx-x):
            if gameMatrix[i][y] == False:
                return False
            i+=1
        return True
    else:
        return False



print(can_travel_to(gameMatrix, 3, 2, 2, 2)) # True, ruch jest dopuszczalny
print(can_travel_to(gameMatrix, 3, 2, 3, 4)) # False, nie można przepłynąć przez ląd
print(can_travel_to(gameMatrix, 3, 2, 3, 3)) # False, nie można przepłynąć przez ląd
print(can_travel_to(gameMatrix, 3, 2, 3, 5)) # False, nie można przepłynąć przez ląd + zbyt daleko
print(can_travel_to(gameMatrix, 3, 2, 6, 2)) # False, poza dopuszczalnym zakresem