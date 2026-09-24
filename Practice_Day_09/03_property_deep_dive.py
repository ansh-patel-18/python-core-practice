class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = 0.0
        self.price = price

    @property
    def price(self):
        print("[GETTER TRIGGED] price padhi jaa rahi he.")
        return self._price

    @price.setter
    def price(self, new_price: float):
        print(f"[SETTER TRIGGERED] Nayi value check ho rahi hai: {new_price}")
        if new_price <= 0:
            print(f"--> REJECTED: Price Rs.{new_price} zero ya negative nahi ho sakti!")
            return

        self._price = float(new_price)
        print(f"--> ACCEPTED: _price update ho gayi: Rs.{self._price}")

if __name__ == "__main__":
    print("--- 1. OBJECT CREATION ---")
    p = Product("Ansh patel", 5000)
    print("="*50)
    print(p.price)