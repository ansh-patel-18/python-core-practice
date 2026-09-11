class Wallet:
    def __init__(self, owner:str, initial_balance : float = 0.0):
        self.owner = owner
        self.history = []

        if initial_balance < 0:
            print("[WARNING] Negative balance not allowed. Set to 0.0")
            self.balance = 0.0
        else:
            self.balance = initial_balance

    def deposit(self, amount: float):
        if amount <= 0 :
            print("[ERROR] Deposit amount must be greater than 0")
            return
        
        self.balance += amount
        self.history.append(f"Credited : Rs.{amount}")
        print(f"Credited \t: {amount}")
            
                        

    def withdraw(self, amount:float):
        if amount <= 0 :
            print("[ERROR] Enter valid amount")
        elif amount>self.balance:
            print(f"[Falied] insufficient funds! Current balance: {self.balance}")
        else:
            self.balance -= amount 
            self.history.append(f"Debited : -Rs.{amount}")
            print(f"Debited \t: {amount}")
            

    def print_statement(self):
        print("\n---Bank Detail---")
        print(f"Owner Name \t: {self.owner}")
        print(f"Avl Balance \t: {self.balance}")
        print("\n---Transaction History---")
        if not self.history:
            print("No transaction yet.")
        else:
            for txn in self.history:
                print(f" -> {txn}")

if __name__ == "__main__":
    w = Wallet(owner="Ansh Patel", initial_balance=500)
    w.deposit(200)
    w.withdraw(100)
    w.withdraw(300)
    w.print_statement()