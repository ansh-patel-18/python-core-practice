class BaseOrder:
    def __init__(self, order_id: str, symbol: str, shares: int, price: float):
        self.order_id = order_id
        self.symbol = symbol.upper()
        self.shares = shares
        self.price = price

    def calculate_total(self):
        return self.shares * self.price

    def execute(self):
        if self.shares <= 0 or self.price <= 0:
            print(f"[{self.symbol}] FAILED: Invalid shares or price!")
            return False
        
        print(f"[{self.symbol}] Order {self.order_id} executed. Total: Rs. {self.calculate_total():.2f}")
        return True

class DeliveryOrder(BaseOrder):
    def __init__(self, order_id: str, symbol: str, shares: int, price: float):
        super().__init__(order_id, symbol, shares, price)
        self.stt_rate = 0.001

    def calculate_total(self):
        base_total =  super().calculate_total()
        return base_total +  (base_total * self.stt_rate)
         
    def execute(self):
        print(f"[{self.symbol} | Delivery] Applying 0.1% STT Tax...")
        return super().execute()

class IntradayOrder(BaseOrder):
    def __init__(self, order_id: str, symbol: str, shares: int, price: float, leverage: float = 5.0):
        super().__init__(order_id, symbol, shares, price)
        self.leverage = leverage

    def calculate_total(self):
        base_total = super().calculate_total()
        margin_amount = base_total / self.leverage
        return margin_amount

    def execute(self):
        print(f"[{self.symbol} | Intraday] Margin required with {self.leverage}x leverage...")
        return super().execute()


if __name__ == "__main__":
    orders = [
        BaseOrder(order_id="ORD101", symbol="TATAMOTORS", shares=10, price=600.0),
        DeliveryOrder(order_id="ORD102", symbol="INFY", shares=10, price=1500.0),
        IntradayOrder(order_id="ORD103", symbol="RELIANCE", shares=10, price=2500.0, leverage=5.0),
        BaseOrder(order_id="ORD104", symbol="HDFCBANK", shares=-5, price=1600.0),  # Rejection Test
    ]

    print("=" * 65)
    print("STARTING BATCH ORDER EXECUTION (POLYMORPHIC LOOP)")
    print("=" * 65)

    for order in orders:
        status = order.execute()
        print(f"Execution Successful: {status}")
        print("-" * 65)