class BankAccount:
    def __init__ (self, name, balance):
        self.name = name
        self.balance = balance
    def __str__ (self):
        print(f"Owner: {self.name}, Balance: {self.balance}")

    def deposit(self):
        plus = input("How much do you want to deposit? ")
        self.balance = self.balance + int(plus)
        print("Success! Your balance is: ", self.balance)

    def withdraw(self):
        plus = input("How much do you want to withdraw? ")
        if int(plus) > self.balance:
            print("Error - insufficient funds.")
        else:
            self.balance = self.balance - int(plus)
            print("Success! Your balance is: ", self.balance)

    def getbalance(self):
        print("Your balance is: ", self.balance)
        
class Bank:
    def __init__(self,bankname):
        self.accounts = []
        self.bankname = bankname
    def __str__(self):
        print(f"Bank: {self.bankname}, Account Number: {self.accounts}")

    def addaccount(self, bankaccount):
        self.accounts.append(bankaccount)

    def getotalbalance(self):
        totalbalance=0
        for account in self.accounts:
            totalbalance += account.balance 
        print("Total balance is: ", totalbalance)

bank = Bank(input("What bank is your account in? "))
bankaccount1 = BankAccount("Krzysiu", 200)
bankaccount2 = BankAccount("Marysia", 500)
bank.addaccount(bankaccount1)
bank.addaccount(bankaccount2)
bank.getotalbalance()
bankaccount1.deposit()
bankaccount1.withdraw()
bankaccount1.getbalance()