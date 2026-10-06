class InsufficientFundError(Exception):
    pass
def withdraw(balance, amount):
    if balance < amount:
        raise InsufficientFundError(f"Requiered : {amount}, Available : {balance}")
    print("Transaction Successfull.")
    return balance - amount

try:
    withdraw(500, 12)
except InsufficientFundError as err:
    print(f"Transaction Failed: {err}")
