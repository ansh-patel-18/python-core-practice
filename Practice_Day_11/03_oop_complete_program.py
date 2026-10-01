# # -----------------------<<< Program 1 >>>-----------------------------<<<

# class BankAccount:
#     def __init__(self, holder:str, balance: float):
#         self.holder = holder
#         self.balance = balance

#     def withdraw(self, amount:float):
#         if amount > self.balance:
#             print("[ERROR] amount is not available")
#             return False
#         if amount < 0:
#             print("[ERROR] Nagetive Amount. Enter valid amount.")
#             return False
#         self.balance -= amount
#         print("Amount Debited \t: ", amount)
#         print("Total Amount \t: ",self.balance)
#         return True

# class SavingAccount(BankAccount):
#     def __init__(self, holder, balance, min_bal):
#         super().__init__(holder, balance)

#         self.min_bal = min_bal

#     def withdraw(self, amount):
#         if (self.balance - amount) < self.min_bal:
#             print("[ERROR] Transaction block because minimum balance is mandatory")
#             return False
#         return super().withdraw(amount)


# class DemetAccount(BankAccount):
#     def __init__(self, holder:str, balance:float, dp_id:str):
        
#         super().__init__(holder, balance)

#         self.dp_id = dp_id
#         self.tax = 20.0

#     def withdraw(self, amount:float):
#         total = amount + self.tax
#         print(f"[*] -> Brokerage fee jodi (Rs.{self.tax}). Total banna: Rs.{total}")

#         success = super().withdraw(total)
#         if success:
#             print("Transaction complete thruout demet.")
#             return success

        
# if __name__ == "__main__":
#     acc = [BankAccount(holder="Ansh", balance=3000),
#            SavingAccount(holder="Raj", balance=300, min_bal=1000),
#            DemetAccount(holder="Jeel", balance=3000, dp_id="IN620273")]
    
#     requested_withdraw = 500

#     print("="*60)
#     print(f"BATCH WITHDRAW PROCESSING: Rs. {requested_withdraw} EACH")
#     print("="*60)

#     for data in acc:
#         data.withdraw(requested_withdraw)
#         print("="*100)


# # ------------------------<<< Program 2 >>>---------------------------<<<


class Order:
    def __init__(self, order_id: str, symbol: str, shares: int):
        self.order_id = order_id
        self.symbol = symbol.upper()
        self.shares = shares


    def __repr__(self):
        return f"Order(order_id={self.order_id}, symbol={self.symbol}, shares={self.shares})"

    # def __str__(self):
        # return f"[{self.symbol}] {self.shares} shares (Ref: {self.order_id})"

    
if __name__ == "__main__":
    o1 = Order("ORD1", "infy", 10)
    o2 = Order("ORD2", "tcs", 5)

    # 1. DIRECT OBJECT PRINT (Trigger karega __str__)
    print("--- DIRECT OBJECT PRINT ---")
    print(o1)
    print(o2)

    # 2. INSIDE CONTAINER (Trigger karega __repr__)
    print("\n--- INSIDE LIST ---")
    orders = [o1, o2]
    print(orders)