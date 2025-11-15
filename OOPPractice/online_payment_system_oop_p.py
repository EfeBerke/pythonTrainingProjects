class PaymentMethod:

    def __init__(self, balance = 0):
        self._balance = balance

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
        elif amount <= self._credit_limit + self._balance:
            self._balance -= amount
        else:
            raise ValueError("Withdrawal exceeds available credit limit.")


class PayPal(PaymentMethod):
    pass

class CryptoWallet(PaymentMethod):
    def __init__(self):
        super().__init__()

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Withdraw value cannot be smaller than zero.")
        elif amount * (102/100) <= self._balance:
            self._balance -= amount * (102/100)
        else:
            raise ValueError("Withdrawal with transaction fee exceeds available balance.")



# Testing Payment Methods 

crcard = CreditCard(200) # Creating Credit Card with Limit of 200
ppaccount = PayPal()
crywal = CryptoWallet()

payment_methods = [crcard, ppaccount, crywal]

for method in payment_methods:
    method.deposit(100)

crcard.withdraw(300)
print(crcard.get_balance())

ppaccount.withdraw(50)
print(ppaccount.get_balance())

crywal.withdraw(50)
print(crywal.get_balance())