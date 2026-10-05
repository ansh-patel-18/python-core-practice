class TradingSystemError(Exception):
    """Base exception for this entire module (Sabka parent)."""

    pass

class InsufficientFundsError(TradingSystemError):
    """Raised when account balance is lower than order value."""

    def __init__(self, current_balance: float, required_amount: float):
        self.current_balance = current_balance
        self.required_amount = required_amount
        self.shortage = required_amount - current_balance

        super().__init__(
            f"Order rejected: Balance Rs.{current_balance} hai, lekin chahiye"
            f" Rs.{required_amount} (Shortage: Rs.{self.shortage})"
        )

class TredingAccount:
    def __init__(self, account_id, balance):
        self.account_id = account_id
        self.balance = balance

    def execute_buy(self, symbol:str, amount:float):
        if amount > self.balance:
            raise InsufficientFundsError(
                current_balance = self.balance, required_amount = amount
            )
        self.balance -= amount
        print(f"[{self.account_id}] SUCCESS: {symbol} khareeda Rs.{amount} mein.")

if __name__ == "__main__":
    acc = TredingAccount(account_id="ACC_909", balance=5000)

    # try:
    #     acc.execute_buy(symbol="TATAMOTORS", amount=2000)
    #     print(f"Bacha hua balance: Rs.{acc.balance}\n")
    # except InsufficientFundsError as e:
        # print("Caught : ",e)


    try:
        print("Attempting to buy expensive stock (Rs.8000)...")
        acc.execute_buy(symbol="RELIANCE", amount=8000.0)
    except InsufficientFundsError as err:
        print("\n--- ERROR CAUGHT AT API LAYER ---")
        print(f"Status Code : 400 Bad Request")
        print(f"Message     : {err}")
        print(f"Shortfall   : Rs.{err.shortage} deposit karne padenge.")