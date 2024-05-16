gameMatrix = [
    [False, True, True, False, False, False],
    [True, True, True, False, False, False],
    [True, True, True, True, True, True],
    [False, True, True, False, True, True],
    [False, True, True, True, False, True],
    [False, False, False, False, False, False],]

def can_travel_to(game_matrix, start_y, start_x, final_y, final_x):
    if final_x > 5 or final_y > 5:
        return False

    if gameMatrix[final_y][final_x] == False:
        return False

    if start_y - final_y == 1 or start_y - final_y == -1:
        return True
    if start_y - final_y > 1 or start_y - final_y < -1:
        return False

    if start_x - final_x in range(-1,3):
        i = 0
        while i < abs(start_x-final_x):
            if gameMatrix[i][final_x] == False:
                return False
            i += 1
        else:
            return True

    if start_x - final_x not in range(-1,3):
        return False


print(can_travel_to(gameMatrix, 0, 2, 0, 1))
print(can_travel_to(gameMatrix, 2, 5, 2, 6))
print(can_travel_to(gameMatrix, 2, 5, 1, 5))
print(can_travel_to(gameMatrix, 2, 5, 3, 5))
print(can_travel_to(gameMatrix, 4, 2, 4, 4))
print(can_travel_to(gameMatrix, 3, 2, 2, 2))  # True, ruch jest dopuszczalny
print(can_travel_to(gameMatrix, 3, 2, 3, 4))  # False, nie można przepłynąć przez ląd
print(can_travel_to(gameMatrix, 3, 2, 3, 3))  # False, nie można przepłynąć przez ląd
print(can_travel_to(gameMatrix, 3, 2, 3, 5))  # False, nie można przepłynąć przez ląd + zbyt daleko
print(can_travel_to(gameMatrix, 3, 2, 6, 2))  # False, poza dopuszczalnym zakresem

