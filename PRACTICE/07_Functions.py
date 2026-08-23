# def is_eligible_for_loan(monthly_salary : int, credit_score : int):
#     if monthly_salary >= 30000 and credit_score >=700:
#         return True
#     else:
#         return False
# result1 = is_eligible_for_loan(55000, 750)
# result2 = is_eligible_for_loan(20000, 690)

# print("user 1 Eligible? ",result1)
# print("user 2 Eligible? ",result2)


########################################################################################################


def can_enter_age(age : int, has_pass : bool):
    if  age >= 18 and has_pass == True:
        return True
    else:
        return False

user_age = int(input("Enter your age : "))
user_pass = input("you have pass ? (yes / not) : ")

has_valid_pass = user_pass.strip().lower() in ("yes", "y", "true")

is_allowed = can_enter_age(user_age, has_valid_pass)

if is_allowed:
    print("Entry Granted")
else:
    print("Entry Denied")





