# class Wallet:
#     def __init__(self, owner, initial_balance):
#         self.owner = owner

#         self._balance = 0.0
#         self.balance = initial_balance

#     @property
#     def balance(self):
#         return self._balance

#     @balance.setter
#     def balance(self, new_amount):
#         if new_amount < 0:
#             print(f"[REJECTED] Rs. {new_amount} is Invalid amount.")
#             return
#         if new_amount>100000.0:
#             print(print(f"[REJECTED] Rs.{new_amount} limit cross kar raha hai! Max 1 Lakh allowed."))
#             return 
#         self._balance = float(new_amount)
#         print(f"[SUCCESS] Balance updated to: Rs.{self._balance:.2f}")

#     @property
#     def currency(self):
#         return "INR"

# if __name__ == "__main__":
#     w = Wallet(owner="Ansh patel", initial_balance=550)
#     w.balance = 12000
#     print(w.balance,w.currency)
#     print("\n--- TEST 1: Padhna (Getter Test) ---")
#     # Dekho: koi w.balance() bracket nahi lagaya, normal variable ki tarah padha:
#     print(f"Current Balance: Rs.{w.balance} {w.currency}")

#     print("\n--- TEST 2: Valid Update (Setter Test) ---")
#     # Variable ki tarah value assign ki:
#     w.balance = 12000.0
#     print(f"Updated Balance: Rs.{w.balance}")   

class orderitem:
    def __init__(self, symbol, qty, price):
        self.symbol = symbol.upper()
        self.qty = qty
        self.price = price

        # self.total_cost = qty * price
    @property
    def total_cost(self):
        return self.qty * self.price

item = orderitem("tatamotors", 10, 1500)
print(item.total_cost)
item.price = 3000
print(item.total_cost)