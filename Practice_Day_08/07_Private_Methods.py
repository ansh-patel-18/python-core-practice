class ATM:
    def __init__(self, pin: int):
        self.__secret_pin = pin

    def __verify_pin(self, user_pin: int):
        return user_pin == self.__secret_pin

    def withdraw_cash(self, user_pin : int, amount: float):
        if self.__verify_pin(user_pin):
            print(f"SUCCESS: Rs.{amount} debited.")
        else:
            print("REJECTED: Wrong PIN")
    

if __name__ == "__main__":
    my_atm = ATM(pin=1234)
    my_atm.withdraw_cash(user_pin=1234, amount=500)