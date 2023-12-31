import math
def rysujchoinke(x):
    stars = 3
    space = x
    print(' '*(x+1),'\33[33m' + '*')
    for i in range(x):
        print(' '*space,"\033[0;32m" + '*'*stars)
        stars += 2
        space -= 1
    print(' '*(x+1), '\33[33m' + '|')

g = int(input("ile rzedow ma miec choinka? "))
rysujchoinke(g)