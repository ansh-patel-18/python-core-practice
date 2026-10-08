class InsufficientBalanceError(Exception):
    pass
class Bank:
    def __init__(self, holder, balance):
        self.balance = balance
        self.holder = holder

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("[ERROR] Amount must be in number.")
        if amount <= 0:
            raise ValueError("[ERROR] Amount must be greater than 0.")
        if self.balance < amount:
            raise InsufficientBalanceError(f"Insufficent funds : Requred Balance : {amount}, Available balance : {self.balance}")
        self.balance -= amount
        print("Transaction Complete")
        print(f"[SUCCESS] Avl bal : {self.balance}")

if __name__ == "__main__":
    acc = Bank("Ansh", 500)


    try:
        acc.withdraw(1000)
    except InsufficientBalanceError as err:
        print(err)

    try:
        acc.withdraw(-50)
    except ValueError as e:
        print(e)


    try:
        acc.withdraw("awnca")
    except TypeError as er:
        print(er)



# #----------------------------------------------------------------------------------------------------------------------------


# 1. Clear domain-specific custom exception
class InsufficientBalanceError(Exception):
    pass

class Bank:
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    def withdraw(self, amount):
        # Step 1: Pehle Type Validate karo (Standard TypeError use karo)
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number (int or float).")
        
        # Step 2: Negative numbers block karo
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than 0.")

        # Step 3: Domain rule check karo (Custom Exception)
        if amount > self.balance:
            raise InsufficientBalanceError(
                f"Insufficient funds: Required {amount}. Available {self.balance}"
            )

        self.balance -= amount
        print(f"Success! {amount} withdrawn. Remaining balance: {self.balance}")
        return self.balance


if __name__ == "__main__":
    account = Bank("Ansh", 1000)

    # Test 1: Sahi Transaction
    account.withdraw(200)

    # Test 2: Custom Exception Trigger karna
    try:
        account.withdraw(1500)
    except InsufficientBalanceError as err:
        print(f"Custom Error Caught: {err}")

    # Test 3: Type Error Trigger karna
    try:
        account.withdraw("invalid_amount")
    except TypeError as err:
        print(f"Type Error Caught: {err}")