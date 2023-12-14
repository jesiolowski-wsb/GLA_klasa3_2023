class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.balance = initial_balance
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposit: +{amount}")

    def withdraw(self, amount):
        self.balance -= amount
        self.transaction_history.append(f"Withdrawal: -{amount}")

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transaction_history

    def __str__(self):
        return f"Właściciel konta: {self.owner}, stan konta: {self.balance}"


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
    bank_name = input("Podaj nazwę banku: ")
    bank = Bank(bank_name)

    account1_owner = input("Podaj właściciela pierwszego konta: ")
    account1 = BankAccount(account1_owner)
    bank.add_account(account1)

    account2_owner = input("Podaj właściciela drugiego konta: ")
    account2 = BankAccount(account2_owner)
    bank.add_account(account2)

    while True:
        print("\nMenu:")
        print("1. Wyświetl saldo wszystkich kont")
        print("2. Wykonaj operację na koncie")

        choice = input("Wybierz opcję: ")

        if choice == "1":
            print(f"\n{bank}\n")
            for account in bank.accounts:
                print(account)

        elif choice == "2":
            account_index = int(input("Podaj numer konta(0/1): "))
            selected_account = bank.accounts[account_index]

            print(f"\nOperacje na koncie {selected_account.owner}:")
            print("1. Wpłata")
            print("2. Wypłata")
            print("3. Wyświetl historię transakcji")

            operation_choice = input("Wybierz operację: ")

            if operation_choice == "1":
                amount = float(input("Podaj kwotę do wpłaty: "))
                selected_account.deposit(amount)
                print("Wpłata zakończona pomyślnie.")

            elif operation_choice == "2":
                amount = float(input("Podaj kwotę do wypłaty: "))
                selected_account.withdraw(amount)
                print("Wypłata zakończona pomyślnie.")

            elif operation_choice == "3":
                history = selected_account.get_transaction_history()
                print("\nHistoria transakcji:")
                for transaction in history:
                    print(transaction)

            else:
                print("):")
                break

        else:
            print("):")
            break


if __name__ == "__main__":
    main()
