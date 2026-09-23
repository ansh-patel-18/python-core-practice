class BankAccount:
    def __init__(self, holder:str, balance: float):
        self.holder = holder
        self.__balance = balance

    def get_balance(self):
        return self.__balance

if __name__ == "__main__":
    acc = BankAccount("Ansh", 5000)

    print("Method ke zariye balance : ", acc.get_balance())

    print("\nObject ki asli memory dictionary (__dict__):")
    print(acc.__dict__)

    print("\nMangled name se direct access: ",
          acc._BankAccount__balance,
    )
    acc.BankAccount__balance = -99999.0
    print("Bahar se hacked balance: ", acc.get_balance())

    # 4. DIRECT ACCESS CRASH TEST:
    # Agar neeche wali line uncomment karoge, toh terminal par AttributeError aayega:
    print(acc._BankAccount__balance)