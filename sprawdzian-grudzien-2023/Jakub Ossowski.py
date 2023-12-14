class BankAccount:
    def __init__(self, balance):
        self.balance = balance


Bal = BankAccount(100)

while True:
    print("wybierz numerek:")
    print("1. withdraw")
    print("2. deposit")
    print("3. get_balance")
    print("4. wyjdź")

    a = int(input())

    if a == 1:
        print("How much do you want to withdraw?")
        w = int(input())
        Bal.balance -= w
        print("Balans konta:", Bal.balance, "zł")
        print("")
    elif a == 2:
        print("How much do you want to deposit?")
        d = int(input())
        Bal.balance += d
        print("Balans konta:", Bal.balance, "zł")
        print("")
    elif a == 3:
        print("Balans konta:", Bal.balance, "zł")
        print("")
    elif a == 4:
        break
    else:
        print("0")
