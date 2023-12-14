class BankAccount:
    def __init__(self, dane):
        self.balance = 0
        self.dane = dane
        self.history = []
    def __str__(self):
        wynik = self.dane + " " + str(self.balance)
        return wynik
    def __int__(self):
        return self.balance
    def deposit(self, sum):
        self.balance += sum
        self.history.append("deposit" + str(sum))
    def withdraw(self, sum):
        self.balance -= sum
        self.history.append("withdraw" + str(sum))
    def get_balance(self):
        print(self.balance)
    def show_history(self):
        print(self.history)
class Bank:
    def __init__(self, nazwa):
        self.total_balance = 0
        self.nazwabanku = nazwa
        self.accounts = []
    def __str__(self):
        l = len(self.accounts)
        wynik = self.nazwabanku + " " + str(l)
        return wynik
    def add_account(self, konto):
        self.accounts.append(konto)
    def get_total_balance(self):
        for konto in self.accounts:
            self.total_balance += int(konto)
        print(self.total_balance)
def rysuj_choinke(poziom):
    for x in range(poziom):
        print((poziom - x)*" ",end="")
        print("*"*(1 + 2 * x))
    print(" "*poziom,end="")
    print("|")
konto = BankAccount("Jan Korowicki")
konto1 = BankAccount("Kacper Paweska")
rysuj_choinke(8)
while 1:
    print("wybierz co chcesz zrobić i którym kontem(j.k lub k.p):")
    print("1.deposit(konto) 2.withdraw(konto) 3.get balance(konto) 4.show history(konto)")
    osoba = input("które konto?: ")
    wybor = input("wybierz operacje od 1 do 4")
    if osoba == "j.k":
        if wybor == "1":
            suma = input("Ile chcesz wplaci?: ")
            konto.deposit(int(suma))
        if wybor == "2":
            suma = input("Ile chcesz wypłacic?: ")
            konto.withdraw(int(suma))
        if wybor == "3":
            konto.get_balance()
        if wybor == "4":
            konto.show_history()
    if osoba == "k.p":
        if wybor == "1":
            suma = input("Ile chcesz wplaci?: ")
            konto1.deposit(int(suma))
        if wybor == "2":
            suma = input("Ile chcesz wypłacic?: ")
            konto1.withdraw(int(suma))
        if wybor == "3":
            konto1.get_balance()
        if wybor == "4":
            konto1.show_history()
