class Order:
    def __init__(self, order_id: str, symbol: str, shares: int):
        self.order_id = order_id
        self.symbol = symbol.upper()
        self.shares = shares

    def __repr__(self):
        return f"Order(order_id={self.order_id}, symbol={self.symbol}, shares={self.shares})"

    def __str__(self):
        return f"[{self.symbol}] {self.shares} shares (Ref: {self.order_id})"

if __name__ == "__main__":
    o1 = Order("ORD1", "infy", 10)
    o2 = Order("ORD2", "tcs", 5)

    print("--- DIRECT PRINT (__str__ ) ---")
    order2 = [o1, o2]
    print(order2)

    print("--- INSIDE LIST (__repr__) ---")
    orders = [o1,o2]
    print(orders)