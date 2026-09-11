class Wallet:
    def __init__(self, owner: str, initial_balance: float = 0.0):
        self.owner = owner
        self.history = []
        if initial_balance < 0:
            self.balance = 0.0
        else:
            self.balance = initial_balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        self.history.append(f"Deposit: +Rs.{amount}")

    def withdraw(self, amount: float) -> bool:
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount > self.balance:
            print("Insufficient balance.")
            return False
        self.balance -= amount
        self.history.append(f"Withdrawal: -Rs.{amount}")
        return True

    def print_statement(self) -> None:
        print(f"\n--- Statement for {self.owner} ---")
        print(f"Current Balance: Rs.{self.balance}")
        print("\nTransaction History:")
        for item in self.history:
            print(f"  - {item}")
        print("---------------------------------\n")

class SavingWallet(Wallet):
    def __init__(self, owner: str, initial_balance: float = 0.0, interest_rate:float = 0.05):
        super().__init__(owner, initial_balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        self.history.append(f"Interest Applied : +Rs.{interest:.2f}")
        print(f"Interest credited: Rs.{interest:.2f}")

    def withdraw(self, amount:float):
        fee = 10.0
        total_deduction = amount + fee

        if amount <=0:
            print("Withdrawel amount must be positive.")
            return False

        if total_deduction > self.balance:
            print(f"Insufficient funds! Needed Rs.{total_deduction} "
                f"(Amount: {amount} + Fee: {fee}), but Balance is Rs.{self.balance}"
                )
            return False
        self.balance -= total_deduction
        self.history.append(f"Withdrawal (incl. Rs.{fee} fee): -Rs.{total_deduction}")
        return True

if __name__ == "__main__":
    # Test execution
    sw = SavingWallet(owner="Ansh Patel", initial_balance=1000.0, interest_rate=0.05)
    sw.deposit(450.0)  
    sw.apply_interest()
    sw.withdraw(200)
    sw.print_statement()