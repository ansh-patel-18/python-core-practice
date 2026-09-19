class BankAccount:
    def __init__(self, holder:str, balance : float):
        print("\n[1] -> Parent (BankAccount) __init__ start hua.")
        self.holder = holder
        self.balance = balance

    def withdraw(self, amount:float):
        print(f"\n[A] -> Parent withdraw() run hua. Checking balance for Rs.{amount}")
        if amount > self.balance:
            print(f"[B] -> FAILED: Insufficient balance! (Current: Rs.{self.balance})")
            return False
        self.balance -= amount
        print(f"[C] -> SUCCESS: Rs.{amount} deducted. New balance: Rs.{self.balance}")
        return True

class DemetAccount(BankAccount):
    def __init__(self, holder:str, balance:float, dp_id:str):
        print("[0] -> Child (DematAccount) __init__ call hua.")

        super().__init__(holder, balance)

        self.dp_id = dp_id
        self.brokerage_fee = 20.0
        print(f"[3] -> Child ne apna specific data set kiya: dp_id='{self.dp_id}', fee=Rs.{self.brokerage_fee}")
    
    def withdraw(self, amount:float):
        print(f"\n[*] -> Child withdraw() intercept kiya. Requested: Rs.{amount}")
        total_debit = amount + self.brokerage_fee
        print(f"[*] -> Brokerage fee jodi (Rs.{self.brokerage_fee}). Total banna: Rs.{total_debit}")
        
        success = super().withdraw(total_debit)
        if success:
            print("[*] -> Transaction complete through Demat portal.")
            return success

if __name__ == "__main__":
    print("\n=== STEP 1: OBJECT CREATION ===")
    acc = DemetAccount(holder="Ansh patel", balance=5000, dp_id="IN214112")

    print("\n=== STEP 2: WITHDRAWAL TEST ===")
    acc.withdraw(1000)

    print("\n=== STEP 3: OVER-LIMIT TEST ===")
    acc.withdraw(4500.0)