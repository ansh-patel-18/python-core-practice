class CartItem:
    def __init__(self, name: str, price: float, quantity: int = 1):
        self.name = name

        # Negative price check
        if price <= 0:
            print(f"Error: Invalid price {price} for {name}. Setting to 0.0")
            self.price = 0.0
        else:
            self.price = price

        # Negative ya zero quantity check
        if quantity <= 0:
            print(f"Error: Invalid quantity {quantity} for {name}. Setting to 1")
            self.quantity = 1
        else:
            self.quantity = quantity

    def get_subtotal(self) -> float:
        # Apni hi properties ko use karke calculation ki
        return self.price * self.quantity


class ShoppingCart:
    def __init__(self, customer_name: str):
        self.customer_name = customer_name
        self.items = []  # Yahan CartItem ke objects store honge
        self.discount_percent = 0.0

    def add_item(self, item: CartItem) -> None:
        # Check duplicate by name
        for existing_item in self.items:
            if existing_item.name == item.name:
                existing_item.quantity += item.quantity
                return

        # Naya item hai toh list mein add karo
        self.items.append(item)

    def apply_discount(self, percent: float) -> bool:
        if 1.0 <= percent <= 50.0:
            self.discount_percent = percent
            return True
        else:
            print("Invalid discount percent. Must be between 1 and 50.")
            return False

    def calculate_bill(self, tax_rate: float = 0.18) -> dict:
        subtotal = 0.0
        # Har object ka subtotal loop chala kar joda
        for item in self.items:
            subtotal += item.get_subtotal()

        discount_amount = subtotal * (self.discount_percent / 100.0)
        discounted_subtotal = subtotal - discount_amount
        tax = discounted_subtotal * tax_rate
        final_total = discounted_subtotal + tax

        return {
            "subtotal": subtotal,
            "discount": discount_amount,
            "tax": tax,
            "final_total": final_total,
        }

    def print_invoice(self) -> None:
        if len(self.items) == 0:
            print("Cart is empty.")
            return

        bill = self.calculate_bill()

        print("\n" + "=" * 40)
        print(f"INVOICE FOR: {self.customer_name}")
        print("=" * 40)
        for item in self.items:
            print(
                f"- {item.name} x {item.quantity} = Rs.{item.get_subtotal():.1f}"
            )
        print("-" * 40)
        print(f"Subtotal       : Rs.{bill['subtotal']:.1f}")
        print(f"Discount ({self.discount_percent:.0f}%) : Rs.{bill['discount']:.1f}")
        print(f"Tax (18% GST)  : Rs.{bill['tax']:.1f}")
        print(f"\nTOTAL PAYABLE  : Rs.{bill['final_total']:.1f}")
        print("=" * 40 + "\n")


if __name__ == "__main__":
    cart = ShoppingCart(customer_name="Ansh Patel")

    item1 = CartItem(name="Laptop Bag", price=1200.0, quantity=1)
    item2 = CartItem(name="Wireless Mouse", price=600.0, quantity=2)
    item3 = CartItem(name="Laptop", price=1200.0, quantity=1)  # Duplicate

    cart.add_item(item1)
    cart.add_item(item2)
    cart.add_item(item3)

    cart.apply_discount(10.0)
    cart.print_invoice()