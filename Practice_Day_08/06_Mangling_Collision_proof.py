class PaymentGateway:
    def __init__(self):
        self.__secret_key = "Base_SECRET_999"

    def process_base_payment(self):
        print(f"[BASE ENGINE] Using key: {self.__secret_key}")

class HDFCGateway(PaymentGateway):

    def __init__(self):
        super().__init__()
        # Child class ne anjaane mein SAME naam ka variable bana diya:
        self.__secret_key = "HDFC_CUSTOM_111"

    def process_hdfc_payment(self):
        print(f"[HDFC ENGINE] Using key: {self.__secret_key}")


if __name__ == "__main__":
    gateway = HDFCGateway()

    print("--- EXECUTION TEST ---")
    # Child class ka method:
    gateway.process_hdfc_payment()
    # Parent class ka method:
    gateway.process_base_payment()

    print("\n--- MEMORY DICTIONARY (__dict__) ---")
    # Parde ke peeche dekho dono keys safe hain ya overwrite hui:
    for key, val in gateway.__dict__.items():
        print(f"{key} -> {val}")
