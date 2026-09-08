def calculate_tax(amount: float):
    tax = amount * 0.18
    return tax

a = int(input("Enter any amount : "))

c_tax = calculate_tax(a)
print(calculate_tax(a))
# print(c_tax)