class BankAccount:

  def __init__(self, holder: str, balance: float):
    self.holder = holder  
    self._balance = balance 

if __name__ == "__main__":
  acc = BankAccount("Ansh", 5000.0)

  print(f"Holder name: {acc.holder}")
  acc.holder = "Ansh Patel"

  print(f"Balance: {acc._balance}")

  acc._balance = -99999.0
  print(f"Balance: {acc._balance}")