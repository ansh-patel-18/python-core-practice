class BankAccount:
    def __init__(self, holder:str, balance:float):
        self.holder = holder
        self.balance = balance

    def withdraw(self, amount:float):
        if amount > self.balance:
            print(f"[parent] Insufficient balance for {self.holder}. Required amount of balance {amount}")
            return False
        self.balance -= amount
        print(f"available bal : {self.balance}")
        return True

    
class DemetAccount(BankAccount):
    def __init__(self, holder:str, balance : float):
        self.transaction_fee = 20.0

    def withdraw(self, amount):
        total_debit = self.transaction_fee + amount
        print(f"[child] Applying Demet withdrawel fee: Rs.{self.transaction_fee}")

        success = super().withdraw(total_debit)
        if success:
            print(f"[Child] Rs.{amount} withdrawn + Rs.{self.transaction_fee} fee changed.")
        return success

if __name__ == "__main__":
    u1 = BankAccount(holder="Ansh patel", balance=5000)
    u1.withdraw(5000)