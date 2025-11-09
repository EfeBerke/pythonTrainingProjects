# Simple bank system (OOP)

class BankAccount:

    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    # Public Functions
    def get_deposit(self, amount):
        self._balance += amount
        print(self._name, "deposited", amount, "→ new balance:", self._balance)
        return self._balance

    def get_withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            print(self._name, "withdrew", amount, "→ new balance:", self._balance)
        else:
            print(self._name, "does not have enough money!")
        return self._balance

if __name__ == "__main__":
    account1 = BankAccount("Alice", 100)
    account2 = BankAccount("Bob", 200)

    # Transactions
    account1.get_deposit(50)
    account2.get_withdraw(100)
    account1.get_withdraw(200)