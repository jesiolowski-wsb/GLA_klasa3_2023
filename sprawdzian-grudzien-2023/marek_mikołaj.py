class BankAccount:
   def __init__(self, owner, balance):
       self.owner = owner
       self.balance = balance
       self.historia = []
   def getbalance(self):
       print(f"Balans na twoim koncie wynosi: {self.balance}")
   def withdraw(self):
       p = int(input("Jaką sumę chciałbyś wyprowadzić z konta? : "))
       self.balance = self.balance - p
       print(f"Balans na twoim koncie po tej operacji wynosi: {self.balance}")
       self.historia.append("withdraw" + p)
   def deposit(self):
       z = int(input("Jaką sumę chciałbyś wprowadzic do konta? : "))
       self.balance = self.balance + z
       print(f"Balans na twoim koncie po tej operacji wynosi: {self.balance}")
       self.historia.append("deposit" + z)
   def pokazhistorie(self):
        print(self.historia)
class Bank:
   def __init__(self, nazwabanku):
       self.nazwabanku = nazwabanku
       self.pieniadze = []
   def add_account(self, wpłata):
       self.pieniadze.append(wpłata)
       print(self.pieniadze)
   def get_total_balance(self):
       m = sum(self.pieniadze)
       print(m)
klient0 = BankAccount("Mikołaj", 9800)
klient1 = BankAccount("Bartosz", 150)
while 2:
    j = int(input("Na którym koncie chciałbys wykonac operacje: 0 czy 1 : "))
    if j == 0:
        d = int(input("Wybierz numer: 1.deposit, 2.withdraw, 3.getbalance, 4.pokaz historie"))
        if d == 1:
            klient0.deposit()
        if d == 2:
            klient0.withdraw()
        if d == 3:
            klient0.getbalance()
        if d == 4:
            print(historia)
    if j == 1:
        d = int(input("Wybierz numer: 1.deposit, 2.withdraw, 3.getbalance, 4.pokaz historie"))
        if d == 1:
            klient1.deposit()
        if d == 2:
            klient1.withdraw()
        if d == 3:
            klient1.getbalance()
        if d == 4:
            klient1.pokazhistorie()

def rysujchoinke(x):
    b = 1

    c = 1
    while c <= x:
        print(" "*(x-c),"*"*b," "*(x-c) )
        c = c+1
        b = b+2
rysujchoinke(5)
