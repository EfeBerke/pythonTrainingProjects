class User():
    def __init__(self, name):
        self._name = name
        self.wallet = Wallet()

class PaymentMethod():
    def __init__(self):
        self._balance = 0 # Initially balance is zero.

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit value cannot be smaller than zero.")
        else:
            self._balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Withdraw value cannot be smaller than zero.")
        
        elif amount <= self._balance:
            self._balance -= amount
        else:
            raise ValueError("Withdrawal exceeds available balance.")

    # Public Function
    def get_balance(self):
        return self._balance

class CreditCard(PaymentMethod):
    def __init__(self, credit_limit):
        super().__init__()
        self._credit_limit = credit_limit

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Withdraw value cannot be smaller than zero.")
        
        elif amount <= self._balance + self._credit_limit:
            self._balance -= amount
        else:
            raise ValueError("Withdrawal exceeds available balance + limit.")

class CryptoWallet(PaymentMethod):
    def __init__(self):
        super().__init__()
        self._fee_rate = 0.2

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Withdraw value cannot be smaller than zero.")
        
        elif (1+ self._fee_rate) * amount <= self._balance:
            self._balance -= amount * (1+ self._fee_rate)
        else:
            raise ValueError("Withdrawal exceeds available balance + limit.")

class Wallet():
    def __init__(self, method: PaymentMethod):
        self.method = method

    def add_money(self, amount):
        self.method.deposit(amount)

    def pay(self, amount):
        self.method.withdraw(amount)

    def get_wallet_balance(self):
        return self.method.get_balance()


w1 = Wallet(PaymentMethod())
w2 = Wallet(CreditCard(200))
w3 = Wallet(CryptoWallet())

wallets = [w1, w2, w3]

for wallet in wallets:
    wallet.add_money(100)
    wallet.pay(50)

for w in wallets:
    print(w.get_wallet_balance())