class Stocks:
    def __init__(self, price):
        self._price = 0.0
        self.price = price
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print(f"[REJECTED] Rs.{new_price} invalid hai! Price 0 ya negative nahi ho sakti.")
            return
        self._price = new_price
        print(f"[ACCEPTED] Price update ho gai: Rs. {self._price}")

if __name__ == "__main__":
    s = Stocks(500)
    print("Current Price: ",s.price)
    s.price = 1650
    s.price = -520
    print("After Attack, price is still safe: ", s.price)

#------------------------<<< 2nd program >>>--------------------------------

class Demo:
    def __init__(self):
        self._val = 0

    @property
    def val(self):
        print(">>> GETTER CHALA (Value padhi gayi!)")
        return self._val

    @val.setter
    def val(self, new_val):
        print(">>> SETTER CHALA (Value likhi gayi!)")
        self._val = new_val

if __name__ == "__main__":
    d = Demo()

    print("\n--- Test 1: Likhna ---")
    d.val = 100  # Yahan sirf SETTER chalega
    
    print("\n--- Test 2: Padhna ---")
    x = d.val  # Yahan sirf GETTER chalega   
   