class BankAccount:
    def __init__(self, holder:str, balance:float):
        self.holder = holder
        self.balance = balance

    def withdraw(self, amount:float):
        if amount > self.balance:
            print(f"[{self.holder} | Regular] FAILED: Low balance (Rs.{self.balance})")
            return False
        self.balance -= amount
        print(f"[{self.holder} | Regular] SUCCESS: Debited Rs.{amount}. Balance left: Rs.{self.balance}")
        return True

class SavingAccount(BankAccount):
    def __init__(self, holder:str, balance:float, min_balance : float):
        super().__init__(holder, balance)
        self.min_balance = min_balance

    def withdraw(self, amount:float):
        if (self.balance - amount) < self.min_balance:
            print(f"[{self.holder} | Savings] FAILED: Violates min balance threshold of Rs.{self.min_balance}")
            return False
        return super().withdraw(amount)

class DemetAccount(BankAccount):
    def __init__(self, holder:str, balance : float, dp_id: str):
        super().__init__(holder, balance)
        self.brokerage = 20.0

    def withdraw(self, amount):
        total = amount + self.brokerage
        print(f"[{self.holder} | Demat] Adding Rs.{self.brokerage} brokerage fee...")
        return super().withdraw(total)

if __name__ == "__main__":
    accounts = [BankAccount(holder="Jay", balance=1000),
                SavingAccount(holder="luv", balance=1500, min_balance=1000),
                DemetAccount(holder="Ansh", balance=200, dp_id="IN346292")]
    
    requested_withdraw = 500

    print("="*60)
    print(f"BATCH WITHDRAW PROCESSING: Rs. {requested_withdraw} EACH")
    print("="*60)


    for acc in accounts:
        acc.withdraw(requested_withdraw)
        print("-"*40)
