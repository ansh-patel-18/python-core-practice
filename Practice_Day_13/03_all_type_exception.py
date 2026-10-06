class NegativeBalanceError(Exception):
    pass

balance = 500
withdraw_balance = 800
try:
    if balance < withdraw_balance:
        raise NegativeBalanceError("Account me itne pase nahi he ")
    balance -= withdraw_balance
    print("Available Balance : ", balance)


except NegativeBalanceError as e:
    # 3. Use yahan pakdo
    print(f"Transaction Blocked: {e}")

print("ATM Machine normal state me hai.")