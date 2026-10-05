class LowBalanceError(Exception):
    pass

def withdraw(balance:int, amount:int):
    if balance < amount:
        raise LowBalanceError("Account mein paisa nahi hai")
    
    return balance - amount

if __name__ == "__main__":
    account_balance = 2000
    withdraw_amount = 500

    try:
        account_balance = withdraw(account_balance, withdraw_amount)

        print("Withdrawal successful! Avl amount : ", account_balance) 

    except LowBalanceError as err:
        print("\n[HANDLED] Catch ho gaya! Reason:", err)
    
    print("Program abhi bhi zinda hai. Agla task chal sakta hai.")