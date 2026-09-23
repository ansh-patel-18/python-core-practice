# SCENARIO 1: Bina kisi dunder method ke plain class
class BadOrder:

  def __init__(self, order_id: str, symbol: str, shares: int):
    self.order_id = order_id
    self.symbol = symbol
    self.shares = shares


# SCENARIO 2: Sirf __str__ likha, __repr__ nahi likha
class HalfBakedOrder:

  def __init__(self, order_id: str, symbol: str, shares: int):
    self.order_id = order_id
    self.symbol = symbol
    self.shares = shares

  def __str__(self) -> str:
    return f"Order {self.order_id}: {self.shares} shares of {self.symbol}"


if __name__ == "__main__":
  b1 = BadOrder("ORD001", "TCS", 10)
  b2 = BadOrder("ORD002", "INFY", 25)

  h1 = HalfBakedOrder("ORD101", "RELIANCE", 50)
  h2 = HalfBakedOrder("ORD102", "TATAMOTORS", 100)

  print("=== PROBLEM 1: ASLI KOODA (Default Python Behavior) ===")
  # Single object print kiya:
  print(b1)
  # List print ki:
  print([b1, b2])

  print("\n=== PROBLEM 2: DHOKHA (__str__ inside List) ===")
  # Single object print kiya -> Sundar dikhega:
  print(h1)

  # LEKIN jab backend list ya queue ko print karega -> DEKHO KYA HOTA HAI:
  order_queue = [h1, h2]
  print(order_queue)