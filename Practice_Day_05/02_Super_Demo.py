class BankAccount():
    def __init__(self, holder:str, balance:float):
        self.holder = holder
        self.balance = balance

    def withdraw(self, amount:float):
        if amount > self.balance:
            print(f"[Failed] Insufficient balance! (Current balance : {self.balance})")
            return False

        self.balance -= amount
        print(f"[SUCCESS] Rs.{amount} deducted. Avl balance : {self.balance}")
        return True

class DemetAccount(BankAccount):
    def __init__(self, holder:str, balance:float, dp_id : str):
        print(print("[0] -> Child (DematAccount) __init__ call hua."))

        super().__init__(holder, balance)

        self.dp_id = dp_id

if __name__ == "__main__":
    u1 = BankAccount(holder="Ansh Patel", balance=5836.40)
    u1.withdraw(1200)
