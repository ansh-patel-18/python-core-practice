class OrderValidator:
  """1. STATIC METHODS: Azaad helper functions jo class namespace mein band hain."""

  @staticmethod
  def is_valid_lot(qty: int) -> bool:
    # Nifty/BankNifty style lot size validation (multiple of 25)
    return qty > 0 and qty % 25 == 0

  @staticmethod
  def is_valid_symbol(symbol: str) -> bool:
    return isinstance(symbol, str) and symbol.isupper() and 2 <= len(symbol) <= 10


class BaseOrder:
  """2. BASE CLASS: Encapsulation, Properties, aur Logging."""

  exchange = "NSE"

  def __init__(self, order_id: str, symbol: str, qty: int, price: float):
    self.order_id = order_id
    self.symbol = symbol.upper()
    self.qty = qty

    # Internal storage (Single underscore convention)
    self._price = 0.0

    # Private internal audit token (Double underscore name-mangling)
    self.__audit_token = f"HASH_{order_id}_{self.symbol}"

    # Constructor ke time hi setter trigger kiya validation ke liye
    self.price = price

  # Getter: order.price
  @property
  def price(self) -> float:
    return self._price

  # Setter: order.price = 500.0 (Validation guard)
  @price.setter
  def price(self, new_price: float):
    if new_price <= 0:
      print(f"[{self.order_id}] REJECTED: Price Rs.{new_price} invalid hai. Update blocked.")
      return
    self._price = float(new_price)

  # Computed Property: Live formula, RAM mein dead store nahi hota
  @property
  def total_cost(self) -> float:
    return self.qty * self._price

  # Dunder Method: Developer debugging representation
  def __repr__(self) -> str:
    return (
        f"BaseOrder(id='{self.order_id}', symbol='{self.symbol}',"
        f" qty={self.qty}, price={self._price})"
    )


class MarginOrder(BaseOrder):
  """3. CHILD CLASS: Inheritance, super(), Child Computed Property, aur ClassMethod."""

  def __init__(
      self,
      order_id: str,
      symbol: str,
      qty: int,
      price: float,
      leverage: int = 5,
  ):
    # Parent class ke constructor ko clean handover
    super().__init__(order_id, symbol, qty, price)
    self.leverage = leverage

  # Child-specific Computed Property (Parent ke total_cost ko use karta hai)
  @property
  def margin_required(self) -> float:
    return self.total_cost / self.leverage

  # Class Method: API Dictionary se direct object produce karne ki factory
  @classmethod
  def from_dict(cls, payload: dict):
    # Dictionary se values nikaali aur cls() ke zariye __init__ ko de di
    return cls(
        order_id=payload["id"],
        symbol=payload["symbol"],
        qty=int(payload["qty"]),
        price=float(payload["price"]),
        leverage=int(payload.get("leverage", 5)),
    )

  # Overridden Dunder Method
  def __repr__(self) -> str:
    return (
        f"MarginOrder(id='{self.order_id}', symbol='{self.symbol}',"
        f" qty={self.qty}, price={self._price}, leverage={self.leverage}x)"
    )




# =========================================================
# FORENSIC EXECUTION RUNNER
# =========================================================
if __name__ == "__main__":
  print("=" * 65)
  print("STAGE 1: STATIC METHOD CHECKS (Bina Object Banaye)")
  print("=" * 65)
  print("Kya 50 valid lot hai?  ->", OrderValidator.is_valid_lot(50))
  print("Kya 30 valid lot hai?  ->", OrderValidator.is_valid_lot(30))
  print("Kya 'TCS' valid symbol? ->", OrderValidator.is_valid_symbol("TCS"))

  print("\n" + "=" * 65)
  print("STAGE 2: DIRECT OBJECT CREATION & COMPUTED PROPERTY")
  print("=" * 65)
  ord1 = BaseOrder("ORD_101", "TCS", qty=25, price=3500.0)
  print("Object Representation (repr) :", ord1)
  print("Total Cost (Computed)        : Rs.", ord1.total_cost)

  print("\n" + "=" * 65)
  print("STAGE 3: SETTER VALIDATION & LIVE REFRESH")
  print("=" * 65)
  # Attack test (Negative value)
  ord1.price = -500.0
  print("Price after attack attempt   : Rs.", ord1.price)

  # Valid update test
  ord1.price = 3600.0
  print("Price after valid update     : Rs.", ord1.price)
  print("Total Cost recalculated live : Rs.", ord1.total_cost)

  print("\n" + "=" * 65)
  print("STAGE 4: CLASSMETHOD ALTERNATIVE CONSTRUCTOR (API Payload)")
  print("=" * 65)
  # Frontend/API se aane wala raw dict payload:
  api_payload = {
      "id": "ORD_202",
      "symbol": "INFY",
      "qty": 50,
      "price": 1400.0,
      "leverage": 4,
  }

  # Direct factory se child object banaya:
  ord2 = MarginOrder.from_dict(api_payload)
  print("Child Object via Factory     :", ord2)
  print("Full Order Value             : Rs.", ord2.total_cost)
  print("Margin Required to Pay (4x)  : Rs.", ord2.margin_required)

  print("\n" + "=" * 65)
  print("STAGE 5: ENCAPSULATION & MEMORY AUDIT")
  print("=" * 65)
  print("Protected attribute accessible via getter:", ord2.price)
  print(
      "Direct internal storage variable name    :",
      [k for k in ord2.__dict__ if "_price" in k][0],
  )
  print(
      "Mangled Private token in RAM             :",
      [k for k in ord2.__dict__ if "audit_token" in k][0],
  )