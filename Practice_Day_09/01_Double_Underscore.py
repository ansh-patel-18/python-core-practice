class OrderEngine:
    def __init__(self, symbol, quantity, price):
        self.symbol = symbol.upper()
        self.quantity = quantity
        self.price = price

    def __calculate_risk_exposure(self):
        return self.quantity * self.price * 1.5

    def __is_suspicious(self):
        return self.quantity > 1000

    def place_order(self):
        print(f"\n[PIPLINE] Validating {self.symbol} order...")

        if self.__is_suspicious():
            print("[REJECTED] High volume order flagged for manual review.")
            return False

        risk = self.__calculate_risk_exposure()
        print(f"[PASSED] Risk exposure calculated: Rs.{risk:.2f}")
        print(f"[SUCCESS] Order placed for {self.quantity} shares of {self.symbol}.")
        return True

if __name__ == "__main__":
    order = OrderEngine(symbol="tatamotors", quantity=5000, price=125.25)
    order.place_order()

    print("---Hacking Attempts")
    leaked_risk = order._OrderEngine__calculate_risk_exposure()
    print(f"BYPASS: Mangled name se chal gaya -> Rs.{leaked_risk:.2f}")

    