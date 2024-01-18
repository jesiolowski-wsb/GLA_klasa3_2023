#zrobiłem taki kod, jest on może o wiele trudniejszy niż na czym polega zadanie, ale zrobiłem go tak że osoba może sama stworzyć jakieś konto bez zmieniania coś w kodzie.
class BankAccount:
    def __init__(self, owner, balance, status):
        self.owner = owner
        self.status = status
        self.balance = balance
    def deposit(self):
        depositing = int(input("How much would you like to deposit into your account? "))
        self.balance += depositing
        balanceL[n] = self.balance
        print(f"Your current money amount in your bank is now: {self.balance} pln")
    def withdraw(self):
        withdrawing = int(input("How much would you like to withdraw from your account? "))
        if self.balance >= withdrawing:
            self.balance -= withdrawing
            print(f"Your current money amount in your bank is now: {self.balance} pln")
        else:
            if self.balance == 0:
                print(f"You now have nothing on your account, so you cant withdraw anything")
            else:
                self.balance -= withdrawing
                print(f"You now have nothing on your account, but you withdrew {withdrawing - (self.balance) * (-1)} anyway.")
        balanceL[n] = self.balance
    def get_balance(self):
        print(f"Your current money amount in your bank is now: {self.balance} pln")
class Bank:
    def __init__(self, bankname):
        self.bankname = bankname
    def add_account(self):
        namesL.append('')
        statusL.append('')
        balanceL.append('')
        bankL.append('')
    def get_total_balance(self):
        sum = 0
        for x in range(n + 1):
            sum += int(balanceL[x])
        print(f"Total amount in all of your accounts is {sum}\n pln")
n = 0
namesL = ['']
statusL = ['']
balanceL = ['']
bankL = ['']
c = True
while c == True:
    if input("Would you like to create a new bank account? ").lower() in ["tak","yes"]:
        name1 = namesL[n] = input("Great! what name would you like for the account? ").capitalize()
        status1 = statusL[n] = "online"
        balance1 = balanceL[n] = input("All right, how much cash would you wanna start with? ")
        bank1 = bankL[n] = input("In which bank should this account be in?\n I have some suggestions like Mbank, ING, MilleniumBank lub IKO ")
        while balance1.isnumeric() == False:
            balance1 = balanceL[n] = input("Please type a real number, so how much would you wanna start with then? ")
        client1 = BankAccount(name1, int(balance1), status1)
        client1bank = Bank(bank1)
        print(f"\nDone!, all set up! Your account information is \n Account name: {client1.owner} \n Account balance: {client1.balance} pln \n Account status: {client1.status}\n Bank account at: {client1bank.bankname} \n")
        b = True
        while b == True:
            if len(namesL) > 1:
                choice = input(f"What would you like to do with your {client1.owner} account now\n 1.Withdraw cash\n 2.Deposit cash\n 3.Check its balance and details\n 4.Create another account\n 5.Nothing more\n 6.Sum up all of your accounts\n 7.Enter one of your other accounts\n")
            else:
                choice = input(f"What would you like to do with your {client1.owner} account now\n 1.Withdraw cash\n 2.Deposit cash\n 3.Check its balance and details\n 4.Create another account\n 5.Nothing more\n")
            a = True
            while a == True:
                try:
                    int(choice)
                except:
                    choice = input("Please input a correct option: ")
                else:
                    if int(choice) in {1, 2, 3, 4, 5, 6, 7} and len(namesL) > 1:
                        print("Right\n")
                        a = False
                    elif int(choice) in {1, 2, 3, 4, 5}:
                        print("Right\n")
                        a = False
                    else:
                        choice = input("Please input a correct option: ")
            if int(choice) == 1:
                client1.withdraw()
            elif int(choice) == 2:
                client1.deposit()
            elif int(choice) == 3:
                client1.get_balance()
                print(f"\n Account name: {client1.owner} \n Account balance: {client1.balance} pln \n Account status: {client1.status}\n Bank account at: {client1bank.bankname}")
            elif int(choice) == 4:
                print("Closing account called: ", namesL[n], "\nWith a status: ", statusL[n], "\nWith a balance off: ", balanceL[n], "pln \nAnd the bank its in: ", bankL[n])
                a = False
                b = False
                n += 1
                client1bank.add_account()
            elif int(choice) == 5:
                print(f"Alright thank you for creating a bank account at {client1bank.bankname}")
                b = c = False
            elif int(choice) == 6:
                client1bank.get_total_balance()
            elif int(choice) == 7:
                print(f"Which account would you like to enter? \n")
                for i in range(len(namesL)):
                    print((i+1),'.',namesL[i])
                answer = int(input(''))
                n = answer-1
                client1.balance = balanceL[n]
                client1.status = statusL[n]
                client1.owner = namesL[n]
                client1bank.bankname = bankL[n]
    else:
        print("Why did you enter then? Well anyway, goodbye!")
        c = False
def rysuj_choinke(wysokosc):
    if wysokosc == 1:
        print("*")
        print("|")
    else:
        amount = 1
        characters = int((wysokosc*2) - amount)
        spaces = int((characters/2)) * " "
        for x in range(wysokosc):
            print(spaces + "*"*amount + spaces)
            amount += 2
            characters = (wysokosc * 2) - amount
            spaces = int((characters/2)) * " "
        print(((wysokosc-1)*" ") + "|")
rysuj_choinke(8)
