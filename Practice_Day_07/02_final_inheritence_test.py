class BaseOrder:
    def __init__(self, order_id: str, symbol: str, shares: int, price: float):
        self.order_id = order_id
        self.symbol = symbol.upper()
        if shares < 0:
            self.shares = 0.0
        self.shares = shares
        # if price > 0:
            # print("[ERROR] Invalid price")
            # return False
        self.price = price

    def calculate_total(self):
        return self.shares * self.price

    def execute(self):
        if self.shares <= 0 or self.price <= 0:
            return False
        
        print(f"[{self.symbol}] Order {self.order_id} executed. Total: Rs. {self.calculate_total():.2f}")
        return True




if __name__ == "__main__":
    acc = BaseOrder(order_id="ORD101", symbol="sensex", shares=2, price=24578.30)
    acc.calculate_total()
    acc.execute()
