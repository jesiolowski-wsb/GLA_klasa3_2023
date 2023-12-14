class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0
        self.history = []

    def deposit(self, amount):
        self.balance += amount
        self.history.append(f"Deposit: +{amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.history.append(f"Withdrawal: -{amount}")
        else:
            print("Insufficient funds!")

    def get_balance(self):
        return self.balance

    def get_history(self):
        return self.history

    def __str__(self):
        return f"Wlasciciel konta: {self.owner}, stan konta: {self.balance}"


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def get_total_balance(self):
        total_balance = sum(account.get_balance() for account in self.accounts)
        return total_balance

    def __str__(self):
        return f"Bank {self.name}, liczba kont: {len(self.accounts)}"


def main():
    bank_name = "MurBank"
    bank = Bank(bank_name)

    account1 = BankAccount("Kacper Murawski")
    account2 = BankAccount("Drugikacper Murawski")

    bank.add_account(account1)
    bank.add_account(account2)

    while True:
        print("\nMenu:")
        print("1. Sprawdz stan konta")
        print("2. Wplac pieniadze")
        print("3. Wyplac pieniadze")
        print("4. Sprawdz historie operacji")
        print("5. Wyswietl informacje o banku")
        print("6. Wyjscie")

        choice = input("Wybierz opcje: ")

        if choice == "1":
            account_index = int(input("Podaj numer konta (1 or 2): ")) - 1
            print(f"Stan konta: {bank.accounts[account_index].get_balance()}")

        elif choice == "2":
            account_index = int(input("Podaj numer konta (1 or 2): ")) - 1
            amount = float(input("Podaj kwote do wplaty: "))
            bank.accounts[account_index].deposit(amount)

        elif choice == "3":
            account_index = int(input("Podaj numer konta (1 or 2): ")) - 1
            amount = float(input("Podaj kwote do wyplaty: "))
            bank.accounts[account_index].withdraw(amount)

        elif choice == "4":
            account_index = int(input("Podaj numer konta (1 or 2): ")) - 1
            history = bank.accounts[account_index].get_history()
            for operation in history:
                print(operation)

        elif choice == "5":
            print(str(bank))

        elif choice == "6":
            print("Zakonczono program.")
            break

        else:
            print("Nieprawidlowy wybor. Sprobuj ponownie.")


if __name__ == "__main__":
    main()
#choin


def rysuj_choinke(poziomy, pien='|'):
    for i in range(1, poziomy + 1):
        gwiazdki = '*' * (2 * i - 1)
        spacje = ' ' * (poziomy - i)
        print(spacje + gwiazdki)

    print(pien)