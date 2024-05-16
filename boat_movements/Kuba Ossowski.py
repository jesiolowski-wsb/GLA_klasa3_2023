gameMatrix = [
    [False, True,  True,  False, False, False],
    [True,  True,  True,  False, False, False],
    [True,  True,  True,  True,  True,  True],
    [False, True,  True,  False, True,  True],
    [False, True,  True,  True,  False, True],
    [False, False, False, False, False, False],
]
x = 3
y = 2
def can_travel_to(m, x, y, a, b):
    if x + 2 <= a:
        if x - 1 <= a:
            if m[a][b]:
                print("1")
                return True
            else:
                print('0')
                return False
        else:
            return False
    elif y + 1 >= b:
        if y - 1 <= b:
            if m[a][b]:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

a = int(input('a?'))
b = int(input('b?'))
print(can_travel_to(gameMatrix, x, y, a, b))





# print(can_travel_to(gameMatrix, 3, 2, 2, 2))  # True, ruch jest dopuszczalny
# print(can_travel_to(gameMatrix, 3, 2, 3, 4))  # False, nie można przepłynąć przez ląd
# print(can_travel_to(gameMatrix, 3, 2, 3, 3))  # False, nie można przepłynąć przez ląd
# print(can_travel_to(gameMatrix, 3, 2, 3, 5))  # False, nie można przepłynąć przez ląd + zbyt daleko
# print(can_travel_to(gameMatrix, 3, 2, 6, 2))  # False, poza dopuszczalnym zakresem
# print('1 ruch w prawo')
# print('2 ruch w lewo')
# print('3 ruch w górę')
# print('4 ruch w dół')
# input1 = input('12345?')
# print('')
# if input1.lower() == '1':
#
# elif input1.lower() == '2':
#
# elif input1.lower() == '3':
#
# elif input1.lower() == '4':
#
# elif input1.lower() == '5':
#
# else:
#     quit()

